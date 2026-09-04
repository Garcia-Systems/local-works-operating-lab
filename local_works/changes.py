"""Fair, evidence-led change control for the Chapter 24 exercise.

The model records decisions; it does not amend contracts, invoice, approve on
someone's behalf, or execute changed work.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class ChangeType(Enum):
    CLARIFICATION = "Clarification"
    DEFECT = "Defect"
    DELIVERY_CORRECTION = "Delivery correction"
    REQUIREMENT_CORRECTION = "Requirement correction"
    TECHNICAL_DISCOVERY = "Technical discovery"
    DEPENDENCY_CHANGE = "Dependency change"
    CUSTOMER_ENHANCEMENT = "Customer enhancement"
    SCOPE_CHANGE = "Scope change"
    DEFERRED_IDEA = "Deferred idea"
    UNKNOWN = "UNKNOWN"


class ChangeSource(Enum):
    CUSTOMER = "Customer"
    LOCAL_WORKS = "Local Works"
    DELIVERY_PARTNER = "Delivery partner"
    VENDOR = "Vendor"
    TESTING = "Testing"
    TECHNICAL_DISCOVERY = "Technical discovery"
    REGULATORY_OR_POLICY = "Regulatory or policy"
    OTHER = "Other"


class ChangeStatus(Enum):
    SUBMITTED = "Submitted"
    CLASSIFYING = "Classifying"
    IMPACT_ANALYSIS = "Impact analysis"
    AWAITING_CUSTOMER_DECISION = "Awaiting customer decision"
    AWAITING_LOCAL_WORKS_DECISION = "Awaiting Local Works decision"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DEFERRED = "Deferred"
    ABSORBED = "Absorbed"
    WITHDRAWN = "Withdrawn"
    SUPERSEDED = "Superseded"


class Materiality(Enum):
    TRIVIAL = "Trivial"
    SMALL = "Small"
    MATERIAL = "Material"
    MAJOR = "Major"
    UNKNOWN = "UNKNOWN"


class Inclusion(Enum):
    YES = "YES"
    NO = "NO"
    AMBIGUOUS = "AMBIGUOUS"
    UNKNOWN = "UNKNOWN"


class ChangeDecision(Enum):
    ABSORB = "Absorb"
    APPROVE_WITHOUT_PRICE_CHANGE = "Approve without price change"
    APPROVE_WITH_PRICE_CHANGE = "Approve with price change"
    TRADE_SCOPE = "Trade scope"
    PHASE_LATER = "Phase later"
    DEFER = "Defer"
    REJECT = "Reject"
    RETURN_FOR_CLARIFICATION = "Return for clarification"
    REVISIT_SOLUTION = "Revisit solution"
    REVISIT_SCOPE = "Revisit scope"
    PAUSE_PROJECT = "Pause project"


class ApprovalAuthority(Enum):
    CUSTOMER_DECISION_MAKER = "Customer decision maker"
    LOCAL_WORKS = "Local Works"
    DELIVERY_PARTNER = "Delivery partner"
    SHARED = "Shared"


@dataclass(frozen=True)
class BaselineReference:
    scope_version: str
    requirements_version: str
    forecast: date | None = None
    delivery_hours: float | None = None
    predecessor_scope_version: str | None = None


@dataclass(frozen=True)
class ScopeComparison:
    baseline: BaselineReference
    requested_behavior: str
    related_scope_items: tuple[str, ...] = ()
    included_before: Inclusion = Inclusion.UNKNOWN
    new_actor: bool = False
    new_system: bool = False
    new_workflow: bool = False
    new_data: bool = False
    new_acceptance: bool = False
    materiality: Materiality = Materiality.UNKNOWN
    classification_rationale: str = "UNKNOWN"

    @property
    def is_ambiguous(self) -> bool:
        return self.included_before is Inclusion.AMBIGUOUS


@dataclass(frozen=True)
class ChangeEstimate:
    delivery_hours: float | None = None
    local_works_hours: float | None = None
    customer_hours: float | None = None
    confidence: str = "UNKNOWN"
    assumptions: tuple[str, ...] = ()


@dataclass(frozen=True)
class ChangeCommercialImpact:
    delivery_cost: float | None = None
    customer_price: float | None = None
    recurring_cost: float | None = None
    incremental_customer_value: float | None = None

    @property
    def incremental_contribution(self) -> float | None:
        if self.customer_price is None or self.delivery_cost is None:
            return None
        return self.customer_price - self.delivery_cost


@dataclass(frozen=True)
class ChangeScheduleImpact:
    baseline_forecast: date | None
    revised_forecast: date | None
    impact: str = "UNKNOWN"


@dataclass(frozen=True)
class ChangeImpact:
    estimate: ChangeEstimate = field(default_factory=ChangeEstimate)
    commercial: ChangeCommercialImpact = field(default_factory=ChangeCommercialImpact)
    schedule: ChangeScheduleImpact | None = None
    quality: str = "UNKNOWN"
    risk: str = "UNKNOWN"
    testing: str = "UNKNOWN"
    documentation: str = "UNKNOWN"
    dependencies: tuple[str, ...] = ()


@dataclass(frozen=True)
class ChangeApproval:
    authority: ApprovalAuthority
    approver: str
    approved_on: date


@dataclass
class ChangeItem:
    change_id: str
    request: str
    source: ChangeSource
    requested_on: date
    change_types: tuple[ChangeType, ...]
    comparison: ScopeComparison
    impact: ChangeImpact = field(default_factory=ChangeImpact)
    status: ChangeStatus = ChangeStatus.SUBMITTED
    decision: ChangeDecision | None = None
    approval: ChangeApproval | None = None
    rationale: str = "UNKNOWN"
    commercial_treatment: str = "UNDECIDED"
    new_baseline: BaselineReference | None = None
    implementation_executed: bool = False

    @property
    def customer_charge(self) -> float | None:
        """Corrections never manufacture a customer charge."""
        if ChangeType.DEFECT in self.change_types or ChangeType.DELIVERY_CORRECTION in self.change_types:
            return None
        return self.impact.commercial.customer_price

    def decide(self, decision: ChangeDecision, rationale: str) -> None:
        self.decision, self.rationale = decision, rationale
        self.status = {
            ChangeDecision.ABSORB: ChangeStatus.ABSORBED,
            ChangeDecision.PHASE_LATER: ChangeStatus.DEFERRED,
            ChangeDecision.DEFER: ChangeStatus.DEFERRED,
            ChangeDecision.REJECT: ChangeStatus.REJECTED,
        }.get(decision, ChangeStatus.APPROVED)


@dataclass
class ChangeHistory:
    """Append-only baseline lineage and change register."""
    baselines: list[BaselineReference]
    changes: list[ChangeItem] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.baselines = list(self.baselines)

    @property
    def current_baseline(self) -> BaselineReference:
        return self.baselines[-1]

    def record(self, item: ChangeItem) -> None:
        self.changes.append(item)

    def approve_new_baseline(self, item: ChangeItem, scope_version: str,
                             requirements_version: str | None = None,
                             forecast: date | None = None) -> BaselineReference:
        old = self.current_baseline
        new = BaselineReference(scope_version, requirements_version or old.requirements_version,
                                forecast if forecast is not None else old.forecast,
                                old.delivery_hours, old.scope_version)
        self.baselines.append(new)
        item.new_baseline = new
        item.status = ChangeStatus.APPROVED
        return new

    @property
    def cumulative_absorbed_hours(self) -> float:
        return sum((c.impact.estimate.delivery_hours or 0) +
                   (c.impact.estimate.local_works_hours or 0)
                   for c in self.changes if c.status is ChangeStatus.ABSORBED)


def classify_from_baseline(comparison: ScopeComparison) -> tuple[ChangeType, ...]:
    """Offer a conservative classification; evidence-specific types stay human decisions."""
    if comparison.included_before is Inclusion.NO:
        return (ChangeType.CUSTOMER_ENHANCEMENT, ChangeType.SCOPE_CHANGE)
    if comparison.included_before is Inclusion.AMBIGUOUS:
        return (ChangeType.REQUIREMENT_CORRECTION,)
    if comparison.included_before is Inclusion.YES:
        return (ChangeType.CLARIFICATION,)
    return (ChangeType.UNKNOWN,)


def partner_overrun_type(scope_changed: bool, assumption_invalidated: bool) -> ChangeType:
    """Underestimation alone is not customer scope creep."""
    if scope_changed:
        return ChangeType.SCOPE_CHANGE
    if assumption_invalidated:
        return ChangeType.TECHNICAL_DISCOVERY
    return ChangeType.DELIVERY_CORRECTION
