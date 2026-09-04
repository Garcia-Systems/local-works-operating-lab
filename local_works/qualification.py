"""Transparent opportunity qualification for Chapter 11.

Qualification consumes prior evidence and decides whether more Local Works
attention is warranted.  It neither scores leads nor selects/approves a project.
"""

from dataclasses import dataclass, field
from enum import Enum

from local_works.economics import EconomicSignificance


class QualificationDimension(Enum):
    PROBLEM_UNDERSTANDING = "Problem understanding"
    ECONOMIC_SIGNIFICANCE = "Economic significance"
    CUSTOMER_PRIORITY = "Customer priority"
    URGENCY = "Urgency"
    AUTHORITY = "Authority"
    BUDGET_CAPACITY = "Budget/capacity"
    TECHNICAL_PLAUSIBILITY = "Technical plausibility"
    ORGANIZATIONAL_FEASIBILITY = "Organizational feasibility"
    MEASURABILITY = "Measurability"
    LOCAL_WORKS_FIT = "Local Works fit"
    COMMERCIAL_RISK = "Commercial risk"


class QualificationRating(Enum):
    STRONG = "Strong"
    ACCEPTABLE = "Acceptable"
    UNCERTAIN = "Uncertain"
    WEAK = "Weak"
    DISQUALIFYING = "Disqualifying"


class QualificationDecision(Enum):
    ADVANCE_TO_SOLUTION_DESIGN = "Advance to solution design"
    MORE_EVIDENCE_REQUIRED = "More evidence required"
    NURTURE = "Nurture"
    REFER_ELSEWHERE = "Refer elsewhere"
    DECLINE = "Decline"
    DISQUALIFY = "Disqualify"


class BudgetStatus(Enum):
    KNOWN_BUDGET = "Known budget"
    PLAUSIBLE_CAPACITY = "Plausible capacity"
    UNKNOWN = "Unknown"
    INSUFFICIENT = "Insufficient"
    UNWILLING_TO_INVEST = "Unwilling to invest"


class AuthorityRole(Enum):
    USER = "User"
    INFLUENCER = "Influencer"
    CHAMPION = "Champion"
    DECISION_MAKER = "Decision maker"
    BUDGET_OWNER = "Budget owner"
    TECHNICAL_APPROVER = "Technical approver"
    PROCUREMENT_OR_OTHER_APPROVER = "Procurement / other approver"


class RiskSeverity(Enum):
    CONCERN = "Concern"
    MAJOR_CONCERN = "Major concern"
    DISQUALIFIER = "Disqualifier"


@dataclass(frozen=True)
class DimensionAssessment:
    dimension: QualificationDimension
    rating: QualificationRating
    evidence: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.evidence:
            raise ValueError("A dimension requires evidence, including an explicit unknown.")


@dataclass(frozen=True)
class QualificationRisk:
    description: str
    severity: RiskSeverity
    context: str = ""


@dataclass(frozen=True)
class QualificationGap:
    unknown: str
    next_evidence: str


@dataclass
class QualificationAssessment:
    opportunity: str
    dimensions: list[DimensionAssessment]
    economic_significance: EconomicSignificance
    budget_status: BudgetStatus
    authority_roles: tuple[AuthorityRole, ...] = ()
    risks: list[QualificationRisk] = field(default_factory=list)
    gaps: list[QualificationGap] = field(default_factory=list)
    positive_signals: list[str] = field(default_factory=list)
    concerns: list[str] = field(default_factory=list)
    expected_presales_hours: float | None = None
    rationale: str = ""

    def __post_init__(self) -> None:
        if not self.opportunity.strip() or not self.rationale.strip():
            raise ValueError("Qualification requires an opportunity and rationale.")
        if self.expected_presales_hours is not None and self.expected_presales_hours < 0:
            raise ValueError("Expected pre-sales hours cannot be negative.")
        names = [item.dimension for item in self.dimensions]
        if len(names) != len(set(names)):
            raise ValueError("Each qualification dimension may appear only once.")

    def rating_for(self, dimension: QualificationDimension) -> QualificationRating:
        for item in self.dimensions:
            if item.dimension is dimension:
                return item.rating
        raise KeyError(f"Missing dimension: {dimension.value}")

    @property
    def hard_disqualifiers(self) -> tuple[QualificationRisk, ...]:
        return tuple(risk for risk in self.risks if risk.severity is RiskSeverity.DISQUALIFIER)

    @property
    def unknowns(self) -> tuple[str, ...]:
        return tuple(gap.unknown for gap in self.gaps)

    @property
    def decision(self) -> QualificationDecision:
        """Apply visible gates in precedence order; there is no numeric score."""
        if self.hard_disqualifiers or any(
            item.rating is QualificationRating.DISQUALIFYING for item in self.dimensions
        ):
            return QualificationDecision.DISQUALIFY
        if self.economic_significance is EconomicSignificance.ECONOMICALLY_TRIVIAL:
            return QualificationDecision.DECLINE
        if self.rating_for(QualificationDimension.LOCAL_WORKS_FIT) is QualificationRating.WEAK:
            return QualificationDecision.REFER_ELSEWHERE
        if self.rating_for(QualificationDimension.CUSTOMER_PRIORITY) is QualificationRating.WEAK:
            return QualificationDecision.NURTURE
        if self.budget_status in (BudgetStatus.INSUFFICIENT, BudgetStatus.UNWILLING_TO_INVEST):
            return QualificationDecision.DECLINE
        evidence_gates = (
            QualificationDimension.PROBLEM_UNDERSTANDING,
            QualificationDimension.AUTHORITY,
            QualificationDimension.TECHNICAL_PLAUSIBILITY,
            QualificationDimension.ORGANIZATIONAL_FEASIBILITY,
        )
        if self.economic_significance is EconomicSignificance.MORE_EVIDENCE_REQUIRED or any(
            self.rating_for(item) in (QualificationRating.UNCERTAIN, QualificationRating.WEAK)
            for item in evidence_gates
        ):
            return QualificationDecision.MORE_EVIDENCE_REQUIRED
        return QualificationDecision.ADVANCE_TO_SOLUTION_DESIGN

    @property
    def selects_solution(self) -> bool:
        return False

    @property
    def creates_proposal(self) -> bool:
        return False

    @property
    def guarantees_sale(self) -> bool:
        return False
