"""Chapter 30's ethical, evidence-preserving relationship planning model.

This module records decisions; it does not contact customers, publish proof, or
implement a CRM.  Activity is not a proxy for health and a signal is not a sale.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto

UNKNOWN = "UNKNOWN"


class RelationshipStatus(Enum):
    ACTIVE_PROJECT = auto(); STABILIZING = auto(); SUPPORTED = auto(); HEALTHY = auto()
    QUIET = auto(); EXPANSION_DISCOVERY = auto(); AT_RISK = auto(); ENDING = auto()
    CHURNED = auto(); DORMANT = auto(); UNKNOWN = auto()


class HealthRating(Enum):
    STRONG = auto(); HEALTHY = auto(); MIXED = auto(); AT_RISK = auto(); UNKNOWN = auto()


class EvidenceType(Enum):
    MEASURED = auto(); PARTIALLY_MEASURED = auto(); OBSERVED = auto()
    ANECDOTAL = auto(); EXPECTED_ONLY = auto(); UNKNOWN = auto()


class RetentionRisk(Enum):
    LOW = auto(); MODERATE = auto(); HIGH = auto(); UNKNOWN = auto()


class ExpansionDecision(Enum):
    NO_ACTION = auto(); MONITOR = auto(); HANDLE_IN_SUPPORT = auto(); DOCUMENT_ONLY = auto()
    CONFIGURE = auto(); INTEGRATE = auto(); AUTOMATE = auto(); CUSTOM_PROJECT = auto()
    DISCOVERY_REQUIRED = auto(); DEFER = auto(); REFER_OUT = auto(); LEAVE_ALONE = auto()


class ExpansionPipelineState(Enum):
    SIGNAL = auto(); QUALIFYING = auto(); DISCOVERY = auto(); ECONOMICS = auto()
    PROPOSAL = auto(); WON = auto(); LOST = auto(); DEFERRED = auto(); LEAVE_ALONE = auto()


class ReferralReadiness(Enum):
    READY = auto(); POTENTIALLY_READY = auto(); WAIT_FOR_MEASUREMENT = auto()
    WAIT_FOR_STABILITY = auto(); NOT_APPROPRIATE = auto(); DO_NOT_ASK = auto(); UNKNOWN = auto()


class ReferralPipelineState(Enum):
    REQUEST_NOT_APPROPRIATE = auto(); READY_TO_ASK = auto(); ASKED_SIMULATED = auto()
    INTRODUCTION_RECEIVED_SIMULATED = auto(); QUALIFIED = auto(); NOT_QUALIFIED = auto()
    NO_RESPONSE = auto(); DECLINED = auto()


class CaseStudyReadiness(Enum):
    NOT_READY = auto(); MEASUREMENT_PENDING = auto(); PERMISSION_REQUIRED = auto()
    CONFIDENTIALITY_REVIEW_REQUIRED = auto(); READY_FOR_INTERNAL_CASE = auto()
    READY_FOR_INTERNAL_TRAINING_SUMMARY = auto(); READY_FOR_PUBLIC_CASE = auto()
    DO_NOT_PUBLISH = auto(); UNKNOWN = auto()


class ChurnReason(Enum):
    VALUE_NOT_CLEAR = auto(); PRICE = auto(); SUPPORT_QUALITY = auto(); INCIDENT_FAILURE = auto()
    VENDOR_CHANGE = auto(); CUSTOMER_INTERNAL_CAPABILITY = auto(); BUSINESS_CLOSED = auto()
    NEW_PROVIDER = auto(); PROJECT_COMPLETE_NO_SUPPORT_NEEDED = auto(); POOR_FIT = auto()
    OWNER_CAPACITY = auto(); OTHER = auto(); UNKNOWN = auto()


class RelationshipAction(Enum):
    NO_ACTION = auto(); CHECK_IN = auto(); VALUE_REVIEW = auto(); DOCUMENTATION_IMPROVEMENT = auto()
    SUPPORT_PLAN_ADJUSTMENT = auto(); RESOLVE_OPEN_ISSUE = auto(); SCOPE_NEW_DISCOVERY = auto()
    REFER_TO_VENDOR = auto(); GRACEFUL_OFFBOARDING = auto(); MAINTAIN = auto()
    SUPPORT_LIGHTLY = auto(); EXPAND = auto(); MONITOR = auto(); LEAVE_ALONE = auto()


class SignalSource(Enum):
    SUPPORT = auto(); DEFERRED_CHANGE = auto(); REVIEW = auto(); CUSTOMER_REQUEST = auto()
    MEASUREMENT = auto(); HYPOTHETICAL = auto(); UNKNOWN = auto()


class ReuseConfidence(Enum):
    HYPOTHESIS = auto(); EARLY_SIGNAL = auto(); REPEATED_PATTERN = auto(); STRONG_EVIDENCE = auto()


@dataclass(frozen=True)
class CustomerOutcomeEvidence:
    metric: str
    baseline: float | str = UNKNOWN
    current_value: float | str = UNKNOWN
    measurement_window: str = UNKNOWN
    evidence_type: EvidenceType = EvidenceType.UNKNOWN
    source: str = UNKNOWN
    confidence: str = UNKNOWN
    notes: str = ""

    @property
    def is_measured(self) -> bool:
        return self.evidence_type in {EvidenceType.MEASURED, EvidenceType.PARTIALLY_MEASURED}


@dataclass(frozen=True)
class RelationshipHealth:
    customer_value: HealthRating = HealthRating.UNKNOWN
    solution_reliability: HealthRating = HealthRating.UNKNOWN
    support_experience: HealthRating = HealthRating.UNKNOWN
    trust: HealthRating = HealthRating.UNKNOWN
    communication: HealthRating = HealthRating.UNKNOWN
    commercial_health: HealthRating = HealthRating.UNKNOWN
    owner_burden: HealthRating = HealthRating.UNKNOWN
    partner_dependency: HealthRating = HealthRating.UNKNOWN
    vendor_dependency: HealthRating = HealthRating.UNKNOWN
    measured_outcomes: HealthRating = HealthRating.UNKNOWN
    future_opportunity: HealthRating = HealthRating.UNKNOWN
    customer_engagement: HealthRating = HealthRating.UNKNOWN
    overall: HealthRating = HealthRating.UNKNOWN


@dataclass(frozen=True)
class RelationshipSignal:
    description: str
    evidence: str = UNKNOWN
    severity: RetentionRisk = RetentionRisk.UNKNOWN


@dataclass(frozen=True)
class ExpansionSignal:
    description: str
    source: SignalSource = SignalSource.UNKNOWN
    frequency: str = UNKNOWN
    burden: str = UNKNOWN
    priority: str = UNKNOWN
    evidence: str = UNKNOWN
    pipeline_state: ExpansionPipelineState = ExpansionPipelineState.SIGNAL
    qualified: bool = False


@dataclass(frozen=True)
class ExpansionOpportunity:
    signal: ExpansionSignal
    problem: str
    affected_users: str = UNKNOWN
    authority: str = UNKNOWN
    urgency: str = UNKNOWN
    budget_capacity: str = UNKNOWN
    feasible: bool | None = None
    measurable: bool | None = None
    simpler_alternative: str = UNKNOWN
    expected_value: float | str = UNKNOWN
    delivery_cost: float | str = UNKNOWN
    owner_hours: float | str = UNKNOWN
    customer_price: float | str = UNKNOWN
    support_impact: str = UNKNOWN
    decision: ExpansionDecision = ExpansionDecision.DISCOVERY_REQUIRED

    @property
    def contribution(self) -> float | None:
        if not isinstance(self.customer_price, (int, float)) or not isinstance(self.delivery_cost, (int, float)):
            return None
        return float(self.customer_price - self.delivery_cost)

    @property
    def contribution_per_owner_hour(self) -> float | None:
        return None if self.contribution is None or not isinstance(self.owner_hours, (int, float)) or self.owner_hours == 0 else self.contribution / self.owner_hours


@dataclass(frozen=True)
class ReferralRequest:
    readiness: ReferralReadiness
    wording: str
    optional: bool = True
    simulated_only: bool = True
    sent: bool = False

    def __post_init__(self) -> None:
        if not self.optional or not self.simulated_only or self.sent:
            raise ValueError("Chapter 30 permits only optional, unsent simulations")


@dataclass(frozen=True)
class ChurnEvent:
    reason: ChurnReason
    healthy: bool
    evidence: str = UNKNOWN
    lessons: tuple[str, ...] = ()


@dataclass(frozen=True)
class OffboardingPlan:
    documentation_handoff: bool = False
    access_review: bool = False
    open_issue_summary: bool = False
    ownership_confirmed: bool = False
    contacts_handed_off: bool = False
    final_commercial_status: str = UNKNOWN
    support_termination_date: str = UNKNOWN


@dataclass(frozen=True)
class RelationshipEconomics:
    project_revenue: float = 0; project_direct_cost: float = 0
    support_revenue: float = 0; support_direct_cost: float = 0
    incident_direct_cost: float = 0; expansion_revenue: float = 0
    expansion_direct_cost: float = 0; other_direct_cost: float = 0
    acquisition_hours: float = 0; delivery_hours: float = 0; support_hours: float = 0
    incident_hours: float = 0; review_hours: float = 0; expansion_hours: float = 0
    referral_admin_hours: float = 0; owner_hour_value: float = 0

    @property
    def project_contribution(self) -> float: return self.project_revenue - self.project_direct_cost
    @property
    def support_contribution(self) -> float: return self.support_revenue - self.support_direct_cost
    @property
    def expansion_contribution(self) -> float: return self.expansion_revenue - self.expansion_direct_cost
    @property
    def cumulative_revenue(self) -> float: return self.project_revenue + self.support_revenue + self.expansion_revenue
    @property
    def cumulative_direct_cost(self) -> float: return self.project_direct_cost + self.support_direct_cost + self.incident_direct_cost + self.expansion_direct_cost + self.other_direct_cost
    @property
    def cumulative_contribution(self) -> float: return self.cumulative_revenue - self.cumulative_direct_cost
    @property
    def total_owner_hours(self) -> float: return self.acquisition_hours + self.delivery_hours + self.support_hours + self.incident_hours + self.review_hours + self.expansion_hours + self.referral_admin_hours
    @property
    def owner_time_adjusted_contribution(self) -> float: return self.cumulative_contribution - self.total_owner_hours * self.owner_hour_value
    @property
    def contribution_per_owner_hour(self) -> float | None: return None if self.total_owner_hours == 0 else self.cumulative_contribution / self.total_owner_hours
    @property
    def expansion_contribution_per_owner_hour(self) -> float | None: return None if self.expansion_hours == 0 else self.expansion_contribution / self.expansion_hours


@dataclass(frozen=True)
class RelationshipReview:
    period: str
    working: tuple[str, ...] = ()
    frustrations: tuple[str, ...] = ()
    outcomes: tuple[CustomerOutcomeEvidence, ...] = ()
    signals: tuple[ExpansionSignal, ...] = ()
    recommended_action: RelationshipAction = RelationshipAction.NO_ACTION


@dataclass(frozen=True)
class RelationshipValue:
    expected_customer_value: str = UNKNOWN
    realized_evidence: tuple[CustomerOutcomeEvidence, ...] = ()
    local_works_economics: RelationshipEconomics = field(default_factory=RelationshipEconomics)


@dataclass(frozen=True)
class CustomerRelationship:
    customer: str
    status: RelationshipStatus = RelationshipStatus.UNKNOWN
    health: RelationshipHealth = field(default_factory=RelationshipHealth)
    retention_risk: RetentionRisk = RetentionRisk.UNKNOWN
    economics: RelationshipEconomics = field(default_factory=RelationshipEconomics)
    locked_in: bool = False
    review_cadence: str = "on-demand"
    overhead_hours_per_month: float = 0
    action: RelationshipAction = RelationshipAction.NO_ACTION

    @property
    def retained_ethically(self) -> bool:
        return not self.locked_in and self.status not in {RelationshipStatus.CHURNED, RelationshipStatus.ENDING}

    @property
    def quiet_is_risk(self) -> bool:
        return self.status is RelationshipStatus.QUIET and self.retention_risk in {RetentionRisk.MODERATE, RetentionRisk.HIGH}


def assess_case_study(*, real_customer: bool, permission: bool | None,
                      measured_evidence: bool, confidentiality_reviewed: bool | None) -> CaseStudyReadiness:
    if not real_customer:
        return CaseStudyReadiness.READY_FOR_INTERNAL_TRAINING_SUMMARY
    if not measured_evidence:
        return CaseStudyReadiness.MEASUREMENT_PENDING
    if permission is not True:
        return CaseStudyReadiness.PERMISSION_REQUIRED
    if confidentiality_reviewed is not True:
        return CaseStudyReadiness.CONFIDENTIALITY_REVIEW_REQUIRED
    return CaseStudyReadiness.READY_FOR_PUBLIC_CASE


def assess_referral(*, stable: bool, health: HealthRating, measured_value: bool,
                    unresolved_dispute: bool, willing: bool | None = None) -> ReferralReadiness:
    if unresolved_dispute or health is HealthRating.AT_RISK:
        return ReferralReadiness.DO_NOT_ASK
    if not stable:
        return ReferralReadiness.WAIT_FOR_STABILITY
    if not measured_value:
        return ReferralReadiness.WAIT_FOR_MEASUREMENT
    if willing is False:
        return ReferralReadiness.NOT_APPROPRIATE
    return ReferralReadiness.READY if willing is True else ReferralReadiness.POTENTIALLY_READY
