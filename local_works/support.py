"""Operational post-launch support boundaries for Chapter 27.

The module records a decision; it is not a ticketing system, a contract, an
SLA engine, or incident-response implementation.  Classification and
commercial treatment are deliberately separate.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto
from typing import Iterable


class SupportRequestType(Enum):
    DEFECT = auto()
    WARRANTY_CANDIDATE = auto()
    HOW_TO = auto()
    CONFIGURATION_ASSISTANCE = auto()
    ROUTINE_SUPPORT = auto()
    INCIDENT = auto()
    THIRD_PARTY_ISSUE = auto()
    CUSTOMER_ENVIRONMENT_ISSUE = auto()
    DATA_ISSUE = auto()
    ACCESS_ISSUE = auto()
    DOCUMENTATION_QUESTION = auto()
    ENHANCEMENT = auto()
    NEW_PROJECT = auto()
    TRAINING = auto()
    UNKNOWN = auto()


class SupportSource(Enum):
    CUSTOMER = auto()
    LOCAL_WORKS = auto()
    DELIVERY_PARTNER = auto()
    VENDOR = auto()
    MONITORING = auto()
    OTHER = auto()


class SupportStatus(Enum):
    NEW = auto()
    TRIAGING = auto()
    WAITING_FOR_CUSTOMER = auto()
    WAITING_FOR_VENDOR = auto()
    WAITING_FOR_DELIVERY_PARTNER = auto()
    IN_PROGRESS = auto()
    RESOLVED = auto()
    CLOSED = auto()
    DEFERRED = auto()
    DECLINED = auto()
    ESCALATED = auto()


class SupportPriority(Enum):
    URGENT = auto()
    HIGH = auto()
    NORMAL = auto()
    LOW = auto()


class IncidentSeverity(Enum):
    """Routing metadata only; response mechanics belong to Chapter 28."""
    SEVERE = auto()
    HIGH = auto()
    MODERATE = auto()
    LOW = auto()


class WarrantyOutcome(Enum):
    WARRANTY_APPLIES = auto()
    LIKELY_WARRANTY = auto()
    WARRANTY_DOES_NOT_APPLY = auto()
    MORE_EVIDENCE_REQUIRED = auto()
    DISPUTED = auto()
    NOT_APPLICABLE = auto()


class Responsibility(Enum):
    LOCAL_WORKS = auto()
    DELIVERY_PARTNER = auto()
    VENDOR = auto()
    CUSTOMER = auto()
    SHARED = auto()
    UNDETERMINED = auto()


class CommercialTreatment(Enum):
    PENDING_CLASSIFICATION = auto()
    NO_CHARGE_WARRANTY = auto()
    INCLUDED_SUPPORT = auto()
    BILLABLE_SUPPORT = auto()
    PREPAID_SUPPORT = auto()
    QUOTE_REQUIRED = auto()
    NEW_PROJECT_DISCOVERY = auto()
    CUSTOMER_HANDLES = auto()
    VENDOR_HANDLES = auto()
    GOODWILL_NO_CHARGE = auto()
    DECLINE = auto()


class SupportEntitlement(Enum):
    NONE = auto()
    WARRANTY_ONLY = auto()
    LIMITED_SUPPORT = auto()
    MONTHLY_SUPPORT = auto()
    PREPAID_HOURS = auto()
    INCIDENT_ONLY = auto()
    CUSTOM = auto()


class SupportPlanStatus(Enum):
    HYPOTHETICAL = auto()
    ACTIVE_SIMULATED = auto()
    EXPIRED_SIMULATED = auto()
    NOT_APPLICABLE = auto()


class SupportAction(Enum):
    HANDLE_AS_WARRANTY = auto()
    HANDLE_AS_INCLUDED_SUPPORT = auto()
    HANDLE_AS_BILLABLE_SUPPORT = auto()
    REQUEST_MORE_INFORMATION = auto()
    ESCALATE_TO_DELIVERY_PARTNER = auto()
    ESCALATE_TO_VENDOR = auto()
    ROUTE_TO_INCIDENT_RESPONSE = auto()
    QUOTE_ENHANCEMENT = auto()
    START_NEW_PROJECT_DISCOVERY = auto()
    CUSTOMER_SELF_SERVICE = auto()
    DECLINE = auto()


@dataclass(frozen=True)
class WarrantyClock:
    launch_date: date
    warranty_start: date
    warranty_end: date
    request_date: date
    hypothetical: bool = True

    @property
    def within_assumed_period(self) -> bool:
        """Timing is one input, never a responsibility decision."""
        return self.warranty_start <= self.request_date <= self.warranty_end


@dataclass(frozen=True)
class WarrantyAssessment:
    outcome: WarrantyOutcome
    related_requirement: object | None = None
    related_acceptance_criterion: object | None = None
    delivered_behavior: str = ""
    expected_behavior: str = ""
    worked_at_acceptance: bool | None = None
    external_system_changed: bool | None = None
    customer_changed_configuration: bool | None = None
    within_intended_workflow: bool | None = None
    warranty_clock: WarrantyClock | None = None
    evidence: tuple[str, ...] = ()
    uncertainty: str | None = None
    rationale: str = ""


@dataclass(frozen=True)
class SupportPlan:
    name: str
    entitlement: SupportEntitlement
    included_request_types: frozenset[SupportRequestType] = frozenset()
    included_hours_or_capacity: float | None = None
    response_expectation: str = "Not specified"
    excluded_work: tuple[str, ...] = ()
    third_party_coordination: str = "Not specified"
    after_hours: str = "Not specified"
    term: str = "Not specified"
    status: SupportPlanStatus = SupportPlanStatus.HYPOTHETICAL

    def includes(self, request_type: SupportRequestType) -> bool:
        return request_type in self.included_request_types


@dataclass(frozen=True)
class SupportBoundary:
    warranty_assumption_days: int | None
    entitlement: SupportEntitlement
    plan: SupportPlan | None = None
    operational_not_legal: bool = True


@dataclass(frozen=True)
class SupportClassification:
    primary_type: SupportRequestType = SupportRequestType.UNKNOWN
    secondary_types: tuple[SupportRequestType, ...] = ()
    responsibility: Responsibility = Responsibility.UNDETERMINED
    warranty: WarrantyAssessment | None = None
    evidence: tuple[str, ...] = ()


@dataclass
class SupportRequest:
    request_id: str
    requested_on: date
    source: SupportSource
    customer_statement: str
    classification: SupportClassification = field(default_factory=SupportClassification)
    priority: SupportPriority = SupportPriority.NORMAL
    status: SupportStatus = SupportStatus.NEW
    affected_workflow: str = ""
    expected_behavior: str = ""
    actual_behavior: str = ""
    security_sensitive: bool = False
    owner_hours: float = 0.0
    delivery_partner_hours: float = 0.0
    estimated_internal_cost: float = 0.0
    documentation_improvement: str | None = None
    expansion_signal: str | None = None

    def __post_init__(self) -> None:
        if min(self.owner_hours, self.delivery_partner_hours, self.estimated_internal_cost) < 0:
            raise ValueError("support effort and cost cannot be negative")


@dataclass(frozen=True)
class SupportDecision:
    request_id: str
    action: SupportAction
    commercial_treatment: CommercialTreatment
    responsibility: Responsibility
    next_action: str
    rationale: str = ""


@dataclass
class SupportHistory:
    requests: list[SupportRequest] = field(default_factory=list)
    decisions: list[SupportDecision] = field(default_factory=list)

    def add(self, request: SupportRequest, decision: SupportDecision | None = None) -> None:
        self.requests.append(request)
        if decision is not None:
            if decision.request_id != request.request_id:
                raise ValueError("decision must refer to the request being added")
            self.decisions.append(decision)

    @property
    def total_owner_hours(self) -> float:
        return sum(item.owner_hours for item in self.requests)

    @property
    def goodwill_requests(self) -> tuple[SupportRequest, ...]:
        ids = {d.request_id for d in self.decisions
               if d.commercial_treatment is CommercialTreatment.GOODWILL_NO_CHARGE}
        return tuple(r for r in self.requests if r.request_id in ids)

    @property
    def cumulative_goodwill_owner_hours(self) -> float:
        return sum(item.owner_hours for item in self.goodwill_requests)

    @property
    def cumulative_goodwill_partner_hours(self) -> float:
        return sum(item.delivery_partner_hours for item in self.goodwill_requests)

    @property
    def cumulative_goodwill_internal_cost(self) -> float:
        return sum(item.estimated_internal_cost for item in self.goodwill_requests)

    def repeated_request_signal(self, request_types: Iterable[SupportRequestType] | None = None,
                                threshold: int = 2) -> bool:
        kinds = list(request_types) if request_types is not None else [r.classification.primary_type for r in self.requests]
        return any(kinds.count(kind) >= threshold for kind in set(kinds))


def recommended_action(request: SupportRequest) -> SupportAction:
    """Route only high-confidence cases; preserve uncertainty for triage."""
    kind = request.classification.primary_type
    warranty = request.classification.warranty
    if request.security_sensitive or kind in {SupportRequestType.INCIDENT, SupportRequestType.DATA_ISSUE}:
        return SupportAction.ROUTE_TO_INCIDENT_RESPONSE
    if warranty and warranty.outcome in {WarrantyOutcome.WARRANTY_APPLIES, WarrantyOutcome.LIKELY_WARRANTY}:
        return SupportAction.HANDLE_AS_WARRANTY
    if warranty and warranty.outcome in {WarrantyOutcome.MORE_EVIDENCE_REQUIRED, WarrantyOutcome.DISPUTED}:
        return SupportAction.REQUEST_MORE_INFORMATION
    if kind is SupportRequestType.THIRD_PARTY_ISSUE:
        return SupportAction.ESCALATE_TO_VENDOR
    if kind is SupportRequestType.ENHANCEMENT:
        return SupportAction.QUOTE_ENHANCEMENT
    if kind is SupportRequestType.NEW_PROJECT:
        return SupportAction.START_NEW_PROJECT_DISCOVERY
    if kind is SupportRequestType.UNKNOWN:
        return SupportAction.REQUEST_MORE_INFORMATION
    return SupportAction.HANDLE_AS_INCLUDED_SUPPORT
