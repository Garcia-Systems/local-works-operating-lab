"""Transparent decision models for the gate between audit and discovery.

The objects in this module organize judgment; they do not calculate a hidden
qualification score, approve implementation, or select a technical solution.
"""

from dataclasses import dataclass, replace
from enum import Enum
from types import MappingProxyType
from typing import Mapping

from local_works.audit import AuditFinding
from local_works.hypothesis import EvidenceType


class OpportunityDecision(Enum):
    DISCOVERY_WARRANTED = "Discovery warranted"
    MORE_INFORMATION_NEEDED = "More information needed"
    SIMPLE_IMPROVEMENT = "Simple improvement"
    MONITOR = "Monitor"
    LEAVE_ALONE = "Leave alone"
    REFER_ELSEWHERE = "Refer elsewhere"
    DISQUALIFY = "Disqualify"


class OpportunityDimension(Enum):
    FREQUENCY = "Frequency"
    IMPACT = "Impact"
    AFFECTED_PARTIES = "Affected parties"
    WORKAROUND_BURDEN = "Workaround burden"
    BUSINESS_IMPORTANCE = "Business importance"
    URGENCY = "Urgency"
    AUTHORITY = "Authority"
    MEASURABILITY = "Measurability"
    TECHNICAL_PLAUSIBILITY = "Technical plausibility"
    ECONOMIC_PLAUSIBILITY = "Economic plausibility"
    EVIDENCE_STRENGTH = "Evidence strength"


class DimensionRating(Enum):
    UNKNOWN = "Unknown"
    WEAK = "Weak"
    MODERATE = "Moderate"
    STRONG = "Strong"


@dataclass(frozen=True)
class OpportunitySignal:
    dimension: OpportunityDimension
    statement: str
    rating: DimensionRating
    evidence_status: EvidenceType = EvidenceType.HYPOTHESIS

    def __post_init__(self) -> None:
        if not self.statement.strip():
            raise ValueError("A signal needs an inspectable statement.")


@dataclass(frozen=True)
class OpportunityCandidate:
    """One explicitly framed workflow candidate, sourced from audit findings."""

    name: str
    workflow: str
    source_findings: tuple[AuditFinding, ...]
    problem_statement: str
    grouping_rationale: str

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.workflow.strip():
            raise ValueError("Candidate name and workflow are required.")
        if not self.source_findings:
            raise ValueError("A candidate needs at least one audit finding.")
        if len({id(finding) for finding in self.source_findings}) != len(self.source_findings):
            raise ValueError("A source finding cannot be added twice.")
        if not self.problem_statement.strip():
            raise ValueError("Frame the possible workflow condition, not only a complaint.")
        if len(self.source_findings) > 1 and not self.grouping_rationale.strip():
            raise ValueError("Grouping multiple findings requires an explicit rationale.")

    @classmethod
    def from_finding(
        cls, name: str, workflow: str, finding: AuditFinding, problem_statement: str
    ) -> "OpportunityCandidate":
        return cls(name, workflow, (finding,), problem_statement, "Single source finding.")

    @classmethod
    def group(
        cls,
        name: str,
        workflow: str,
        findings: tuple[AuditFinding, ...],
        problem_statement: str,
        rationale: str,
    ) -> "OpportunityCandidate":
        """Group only findings a human explicitly judges to share a workflow."""
        return cls(name, workflow, findings, problem_statement, rationale)


@dataclass(frozen=True)
class OpportunityAssessment:
    candidate: OpportunityCandidate
    dimensions: Mapping[OpportunityDimension, OpportunitySignal]
    problem_potential: DimensionRating
    commercial_fit: DimensionRating
    positive_signals: tuple[str, ...]
    negative_signals: tuple[str, ...]
    unknowns: tuple[str, ...]
    hard_disqualifiers: tuple[str, ...]
    decision: OpportunityDecision
    rationale: tuple[str, ...]
    next_questions: tuple[str, ...] = ()
    next_action: str = ""
    evidence_status: EvidenceType = EvidenceType.HYPOTHESIS

    def __post_init__(self) -> None:
        object.__setattr__(self, "dimensions", MappingProxyType(dict(self.dimensions)))
        if not self.rationale or any(not reason.strip() for reason in self.rationale):
            raise ValueError("Every opportunity decision needs explicit rationale.")
        if self.decision is OpportunityDecision.DISQUALIFY and not self.hard_disqualifiers:
            raise ValueError("Disqualification requires a preserved hard disqualifier.")

    @property
    def unknown_dimensions(self) -> tuple[OpportunityDimension, ...]:
        return tuple(
            dimension for dimension, signal in self.dimensions.items()
            if signal.rating is DimensionRating.UNKNOWN
        )

    @property
    def implementation_approved(self) -> bool:
        return False

    @property
    def custom_build_selected(self) -> bool:
        return False

    def revised(self, **changes: object) -> "OpportunityAssessment":
        """Create a traceable new judgment without mutating prior evidence."""
        return replace(self, **changes)


def signal(
    dimension: OpportunityDimension,
    statement: str,
    rating: DimensionRating = DimensionRating.UNKNOWN,
    evidence_status: EvidenceType = EvidenceType.HYPOTHESIS,
) -> OpportunitySignal:
    """Readable shorthand used by exercises and callers constructing assessments."""
    return OpportunitySignal(dimension, statement, rating, evidence_status)
