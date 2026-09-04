"""Technical-estimate records and comparison rules for Chapter 19.

These records describe a delivery forecast, not a customer quote, project
authorization, or actual delivery.  Comparison is deliberately transparent:
scope differences and normalization adjustments never disappear into a score.
"""

from dataclasses import dataclass, field, replace
from datetime import date
from enum import Enum


class EstimateStatus(Enum):
    REQUESTED = "Requested"
    RECEIVED = "Received"
    NEEDS_CLARIFICATION = "Needs clarification"
    REVISED = "Revised"
    COMPARABLE = "Comparable"
    NOT_COMPARABLE = "Not comparable"
    WITHDRAWN = "Withdrawn"
    REJECTED = "Rejected"
    CONDITIONAL_ESTIMATE = "Conditional estimate"


class EstimateConfidence(Enum):
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"
    VERY_LOW = "Very low"
    UNKNOWN = "Unknown"


class ComponentType(Enum):
    DISCOVERY_OR_TECHNICAL_VALIDATION = "Discovery or technical validation"
    CONFIGURATION = "Configuration"
    FRONTEND = "Frontend"
    BACKEND = "Backend"
    INTEGRATION = "Integration"
    AUTOMATION = "Automation"
    DATA_MIGRATION = "Data migration"
    TESTING = "Testing"
    DEPLOYMENT = "Deployment"
    DOCUMENTATION = "Documentation"
    TRAINING_SUPPORT = "Training/support"
    PROJECT_COORDINATION = "Project coordination"
    OTHER = "Other"


class ScopeAlignment(Enum):
    ALIGNED = "Aligned"
    SCOPE_DEVIATION = "Scope deviation"
    INCOMPLETE_SCOPE = "Incomplete scope"
    UNKNOWN = "Unknown"


class ClarificationStatus(Enum):
    OPEN = "Open"
    ANSWERED = "Answered"
    INCORPORATED = "Incorporated"


class QualityDimension(Enum):
    SCOPE_ALIGNMENT = "Scope alignment"
    ASSUMPTION_CLARITY = "Assumption clarity"
    EXCLUSION_CLARITY = "Exclusion clarity"
    TECHNICAL_REASONING = "Technical reasoning"
    RISK_DISCLOSURE = "Risk disclosure"
    COST_TRANSPARENCY = "Cost transparency"
    TIMELINE_REALISM = "Timeline realism"
    TESTING_COVERAGE = "Testing coverage"
    DOCUMENTATION_COVERAGE = "Documentation coverage"
    HANDOFF_READINESS = "Handoff readiness"
    CONFIDENCE_CALIBRATION = "Confidence calibration"


class QualityRating(Enum):
    STRONG = "Strong"
    ADEQUATE = "Adequate"
    UNCERTAIN = "Uncertain"
    WEAK = "Weak"


class EstimateDecisionType(Enum):
    SELECT_FOR_DELIVERY = "Select for delivery"
    SELECT_FOR_TECHNICAL_DISCOVERY = "Select for technical discovery"
    REQUEST_REVISED_ESTIMATE = "Request revised estimate"
    REQUEST_CLARIFICATION = "Request clarification"
    KEEP_AS_BACKUP = "Keep as backup"
    DO_NOT_SELECT = "Do not select"
    REOPEN_DELIVERY_SEARCH = "Reopen delivery search"
    REVISIT_SOLUTION = "Revisit solution"
    REVISIT_SCOPE = "Revisit scope"


@dataclass(frozen=True)
class EstimateRange:
    lower: float
    upper: float
    unit: str = "USD"

    def __post_init__(self) -> None:
        if self.lower < 0 or self.upper < self.lower:
            raise ValueError("An estimate range requires 0 <= lower <= upper.")

    @property
    def midpoint(self) -> float:
        return (self.lower + self.upper) / 2


@dataclass(frozen=True)
class TimelineEstimate:
    duration: EstimateRange
    earliest_start: date | None = None
    expected_completion: date | None = None
    dependencies: tuple[str, ...] = ()


@dataclass(frozen=True)
class EstimateRequest:
    request_version: str
    project: str
    business: str
    opportunity: str
    problem_summary: str
    business_outcome: str
    selected_solution_path: str
    scope_version: str
    included_workflow: tuple[str, ...]
    excluded_workflow: tuple[str, ...]
    required_capabilities: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    known_systems: tuple[str, ...]
    known_constraints: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = ()
    unresolved_technical_questions: tuple[str, ...] = ()
    customer_responsibilities: tuple[str, ...] = ()
    local_works_responsibilities: tuple[str, ...] = ()
    expected_documentation: tuple[str, ...] = ()
    expected_testing: tuple[str, ...] = ()
    expected_deployment: tuple[str, ...] = ()
    continuity_expectations: tuple[str, ...] = ()
    desired_estimate_format: str = "Components, ranges, assumptions, exclusions, risk, and confidence"


@dataclass(frozen=True)
class EstimateComponent:
    category: ComponentType
    description: str
    hours: EstimateRange | None = None
    cost: EstimateRange | None = None
    fixed_cost: float | None = None
    notes: str = ""

    def __post_init__(self) -> None:
        if self.fixed_cost is not None and self.fixed_cost < 0:
            raise ValueError("Fixed cost cannot be negative.")
        if self.cost is not None and self.fixed_cost is not None:
            raise ValueError("Use either a cost range or fixed cost for a component.")

    @property
    def cost_bounds(self) -> tuple[float, float]:
        if self.cost is not None:
            return self.cost.lower, self.cost.upper
        amount = self.fixed_cost or 0.0
        return amount, amount


@dataclass(frozen=True)
class EstimateAssumption:
    statement: str
    importance: str
    evidence_status: str = "UNKNOWN"
    impact_if_false: str = "UNKNOWN"


@dataclass(frozen=True)
class EstimateExclusion:
    statement: str
    consequence: str = "Requires separate decision or cost"


@dataclass(frozen=True)
class EstimateRisk:
    description: str
    impact: str
    likelihood: str = "UNKNOWN"
    mitigation: str = "UNKNOWN"


@dataclass(frozen=True)
class EstimateClarification:
    question: str
    reason: str
    response: str = "UNKNOWN"
    impact: str = "UNKNOWN"
    status: ClarificationStatus = ClarificationStatus.OPEN


@dataclass
class TechnicalEstimate:
    candidate: str
    project: str
    baseline_scope_version: str
    estimated_scope_version: str
    approach: str
    components: list[EstimateComponent]
    estimate_date: date | None = None
    valid_through: date | None = None
    status: EstimateStatus = EstimateStatus.RECEIVED
    scope_alignment: ScopeAlignment = ScopeAlignment.UNKNOWN
    effort: EstimateRange | None = None
    partner_cost: EstimateRange | None = None
    timeline: TimelineEstimate | None = None
    confidence: EstimateConfidence = EstimateConfidence.UNKNOWN
    confidence_reason: str = "UNKNOWN"
    assumptions: list[EstimateAssumption] = field(default_factory=list)
    exclusions: list[EstimateExclusion] = field(default_factory=list)
    risks: list[EstimateRisk] = field(default_factory=list)
    clarifications: list[EstimateClarification] = field(default_factory=list)
    third_party_implementation_cost: EstimateRange | None = None
    recurring_third_party_cost: EstimateRange | None = None
    customer_effort: EstimateRange | None = None
    local_works_effort: EstimateRange | None = None
    technical_discovery_required: bool = False
    discovery_cost: EstimateRange | None = None
    testing: str = "UNKNOWN"
    documentation: str = "UNKNOWN"
    deployment: str = "UNKNOWN"
    support_handoff: str = "UNKNOWN"
    quality: dict[QualityDimension, QualityRating] = field(default_factory=dict)
    implementation_started: bool = False

    def component_cost_total(self) -> EstimateRange:
        bounds = [component.cost_bounds for component in self.components]
        return EstimateRange(sum(x[0] for x in bounds), sum(x[1] for x in bounds))

    def component_effort_total(self) -> EstimateRange | None:
        ranges = [component.hours for component in self.components if component.hours]
        if not ranges:
            return None
        return EstimateRange(sum(x.lower for x in ranges), sum(x.upper for x in ranges), "hours")

    def add_clarification(self, clarification: EstimateClarification) -> None:
        self.clarifications.append(clarification)
        self.status = (EstimateStatus.REVISED if clarification.status in
                       {ClarificationStatus.ANSWERED, ClarificationStatus.INCORPORATED}
                       else EstimateStatus.NEEDS_CLARIFICATION)

    @property
    def can_compare(self) -> bool:
        return (self.baseline_scope_version == self.estimated_scope_version
                and self.scope_alignment is ScopeAlignment.ALIGNED
                and self.status not in {EstimateStatus.NEEDS_CLARIFICATION,
                                        EstimateStatus.NOT_COMPARABLE,
                                        EstimateStatus.WITHDRAWN,
                                        EstimateStatus.REJECTED})


@dataclass(frozen=True)
class NormalizationAdjustment:
    category: str
    cost: EstimateRange
    reason: str
    recurring: bool = False


@dataclass(frozen=True)
class NormalizedEstimate:
    estimate: TechnicalEstimate
    adjustments: tuple[NormalizationAdjustment, ...]
    normalized_delivery_cost: EstimateRange
    comparable: bool
    notes: tuple[str, ...] = ()


@dataclass
class EstimateComparison:
    request: EstimateRequest
    estimates: list[TechnicalEstimate]
    normalized: dict[str, NormalizedEstimate] = field(default_factory=dict)
    implementation_started: bool = False

    def normalize(self, candidate: str, adjustments: tuple[NormalizationAdjustment, ...] = ()) -> NormalizedEstimate:
        estimate = next((item for item in self.estimates if item.candidate == candidate), None)
        if estimate is None:
            raise ValueError(f"Unknown estimate candidate: {candidate}")
        aligned = (estimate.baseline_scope_version == self.request.scope_version
                   and estimate.estimated_scope_version == self.request.scope_version
                   and estimate.scope_alignment is ScopeAlignment.ALIGNED)
        if not aligned:
            estimate.status = EstimateStatus.NOT_COMPARABLE
        base = estimate.partner_cost or estimate.component_cost_total()
        included = [a.cost for a in adjustments if not a.recurring]
        if estimate.discovery_cost:
            included.append(estimate.discovery_cost)
        if estimate.third_party_implementation_cost:
            included.append(estimate.third_party_implementation_cost)
        total = EstimateRange(base.lower + sum(x.lower for x in included),
                              base.upper + sum(x.upper for x in included))
        result = NormalizedEstimate(estimate, adjustments, total, aligned,
                                    (() if aligned else ("Scope must be reconciled before comparison.",)))
        self.normalized[candidate] = result
        if aligned and estimate.status not in {EstimateStatus.NEEDS_CLARIFICATION, EstimateStatus.REJECTED}:
            estimate.status = EstimateStatus.COMPARABLE
        return result


@dataclass(frozen=True)
class EstimateDecision:
    candidate: str | None
    decision: EstimateDecisionType
    rationale: str
    estimate_status: EstimateStatus | None = None
    starts_implementation: bool = False

    def __post_init__(self) -> None:
        if self.starts_implementation:
            raise ValueError("Chapter 19 decisions cannot start implementation.")


def answered(clarification: EstimateClarification, response: str, impact: str) -> EstimateClarification:
    """Return an answered immutable clarification for a revision history."""
    return replace(clarification, response=response, impact=impact,
                   status=ClarificationStatus.ANSWERED)
