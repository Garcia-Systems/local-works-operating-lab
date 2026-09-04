"""Small, explicit engagement-scope model for Chapter 14.

Scope records what must be true and where the work stops.  They are not
technical designs, prices, proposals, contracts, or partner selections.
"""

from dataclasses import dataclass, field
from enum import Enum


class ScopeStatus(Enum):
    DRAFT = "Draft"
    NEEDS_VALIDATION = "Needs validation"
    READY_FOR_ESTIMATE = "Ready for estimate"
    BLOCKED = "Blocked"


class EstimateReadiness(Enum):
    READY_FOR_ESTIMATE = "Ready for estimate"
    NEEDS_CUSTOMER_CLARIFICATION = "Needs customer clarification"
    NEEDS_TECHNICAL_VALIDATION = "Needs technical validation"
    NEEDS_SCOPE_REDUCTION = "Needs scope reduction"
    BLOCKED = "Blocked"


class Priority(Enum):
    MUST = "Must"
    SHOULD = "Should"
    COULD = "Could"
    NOT_IN_SCOPE = "Not in scope"


class SystemClassification(Enum):
    IN_SCOPE = "In scope"
    DEPENDENCY_ONLY = "Dependency only"
    OUT_OF_SCOPE = "Out of scope"
    UNKNOWN = "Unknown"


class AssumptionStatus(Enum):
    CONFIRMED = "Confirmed"
    UNCONFIRMED = "Unconfirmed"
    INVALIDATED = "Invalidated"


class RequestDisposition(Enum):
    REQUESTED = "Requested"
    INCLUDED = "Included"
    DEFERRED = "Deferred"
    REJECTED = "Rejected"
    CHANGE_LATER = "Change later"


class ScopeRiskCategory(Enum):
    AMBIGUOUS_REQUIREMENT = "Ambiguous requirement"
    UNVALIDATED_ASSUMPTION = "Unvalidated assumption"
    THIRD_PARTY_DEPENDENCY = "Third-party dependency"
    CUSTOMER_DEPENDENCY = "Customer dependency"
    DATA_COMPLEXITY = "Data complexity"
    POLICY_COMPLEXITY = "Policy complexity"
    INTEGRATION_UNCERTAINTY = "Integration uncertainty"
    ACCEPTANCE_AMBIGUITY = "Acceptance ambiguity"
    OTHER = "Other"


@dataclass(frozen=True)
class ScopeBoundary:
    trigger: str
    end_condition: str

    def __post_init__(self) -> None:
        if not self.trigger.strip() or not self.end_condition.strip():
            raise ValueError("A workflow boundary requires a trigger and end condition.")


@dataclass(frozen=True)
class ScopeItem:
    statement: str
    priority: Priority = Priority.MUST
    design_decision: str | None = None

    def __post_init__(self) -> None:
        if not self.statement.strip():
            raise ValueError("A scope item requires a statement.")


@dataclass(frozen=True)
class ScopeExclusion:
    statement: str
    reason: str = "Outside this workflow boundary"


@dataclass(frozen=True)
class ScopedSystem:
    name: str
    classification: SystemClassification
    role: str = ""


@dataclass(frozen=True)
class ScopeAssumption:
    statement: str
    why_it_matters: str
    status: AssumptionStatus
    impact_if_false: str
    critical: bool = False
    evidence: str = "UNKNOWN"


@dataclass(frozen=True)
class ScopeDependency:
    dependency: str
    owner: str
    status: AssumptionStatus
    impact_if_unavailable: str
    technical: bool = False
    critical: bool = False


@dataclass(frozen=True)
class CustomerResponsibility:
    statement: str


@dataclass(frozen=True)
class LocalWorksResponsibility:
    statement: str


@dataclass(frozen=True)
class DeliveryResponsibility:
    statement: str


@dataclass(frozen=True)
class AcceptanceCriterion:
    given: str
    when: str
    then: str


@dataclass(frozen=True)
class ScopeChangeRequest:
    request: str
    disposition: RequestDisposition = RequestDisposition.REQUESTED
    rationale: str = "Requires an explicit scope decision"


@dataclass(frozen=True)
class ScopeRisk:
    category: ScopeRiskCategory
    description: str
    severity: str
    mitigation: str
    status: str = "OPEN"


@dataclass
class ProjectScope:
    business: str
    opportunity: str
    business_outcome: str
    problem_statement: str
    solution_direction: str
    boundary: ScopeBoundary
    included: list[ScopeItem]
    excluded: list[ScopeExclusion]
    actors: list[str] = field(default_factory=list)
    systems: list[ScopedSystem] = field(default_factory=list)
    functional_requirements: list[ScopeItem] = field(default_factory=list)
    non_functional_considerations: list[str] = field(default_factory=list)
    assumptions: list[ScopeAssumption] = field(default_factory=list)
    dependencies: list[ScopeDependency] = field(default_factory=list)
    customer_responsibilities: list[CustomerResponsibility] = field(default_factory=list)
    local_works_responsibilities: list[LocalWorksResponsibility] = field(default_factory=list)
    delivery_responsibilities: list[DeliveryResponsibility] = field(default_factory=list)
    acceptance_criteria: list[AcceptanceCriterion] = field(default_factory=list)
    business_success_metrics: list[str] = field(default_factory=list)
    data_required: list[str] = field(default_factory=list)
    data_excluded: list[str] = field(default_factory=list)
    risks: list[ScopeRisk] = field(default_factory=list)
    change_requests: list[ScopeChangeRequest] = field(default_factory=list)
    status: ScopeStatus = ScopeStatus.DRAFT
    vague: bool = False
    overloaded: bool = False
    blocked: bool = False

    def __post_init__(self) -> None:
        included = {item.statement.strip().casefold() for item in self.included}
        excluded = {item.statement.strip().casefold() for item in self.excluded}
        overlap = included & excluded
        if overlap:
            raise ValueError(f"Items cannot be both included and excluded: {sorted(overlap)}")

    @property
    def requirements_by_priority(self) -> dict[Priority, tuple[ScopeItem, ...]]:
        return {priority: tuple(item for item in self.functional_requirements
                                if item.priority is priority) for priority in Priority}

    def classify_request(self, request: str, disposition: RequestDisposition,
                         rationale: str = "Requires a later scope decision") -> ScopeChangeRequest:
        """Record a request without silently changing included scope."""
        change = ScopeChangeRequest(request, disposition, rationale)
        self.change_requests.append(change)
        return change

    @property
    def estimate_readiness(self) -> EstimateReadiness:
        if self.blocked or any(a.status is AssumptionStatus.INVALIDATED and a.critical
                               for a in self.assumptions):
            return EstimateReadiness.BLOCKED
        if self.overloaded:
            return EstimateReadiness.NEEDS_SCOPE_REDUCTION
        if self.vague or not self.business_outcome.strip() or not self.acceptance_criteria \
                or not self.customer_responsibilities:
            return EstimateReadiness.NEEDS_CUSTOMER_CLARIFICATION
        if any(system.classification is SystemClassification.UNKNOWN for system in self.systems):
            return EstimateReadiness.NEEDS_TECHNICAL_VALIDATION
        if any(dependency.critical and dependency.technical
               and dependency.status is AssumptionStatus.UNCONFIRMED
               for dependency in self.dependencies):
            return EstimateReadiness.NEEDS_TECHNICAL_VALIDATION
        if any(assumption.critical and assumption.status is AssumptionStatus.UNCONFIRMED
               for assumption in self.assumptions):
            return EstimateReadiness.NEEDS_CUSTOMER_CLARIFICATION
        return EstimateReadiness.READY_FOR_ESTIMATE

    @property
    def creates_price(self) -> bool:
        return False

    @property
    def creates_proposal(self) -> bool:
        return False

    @property
    def selects_delivery_partner(self) -> bool:
        return False
