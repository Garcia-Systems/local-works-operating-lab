"""Chapter 31A's small, inspectable portfolio operating model.

This is a planning view over records owned by earlier chapters, not a CRM.  In
particular, project, support, incident, opportunity, payment, economics, and
relationship objects are referenced rather than copied into new schemas.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto
from typing import Iterable, Mapping


class LifecycleStage(Enum):
    LEAD = auto(); AUDIT = auto(); QUALIFIED = auto(); DISCOVERY = auto()
    PROPOSAL = auto(); SIGNED = auto(); QUEUED = auto(); ACTIVE_DELIVERY = auto()
    LAUNCH = auto(); SUPPORT = auto(); EXPANSION = auto(); DORMANT = auto()


class WorkCategory(Enum):
    MARKETING = auto(); LEAD_FOLLOW_UP = auto(); AUDIT = auto(); QUALIFICATION = auto()
    DISCOVERY = auto(); SOLUTION_DESIGN = auto(); PROPOSAL = auto(); SALES = auto()
    PROJECT_DELIVERY = auto(); PROJECT_MANAGEMENT = auto(); QA = auto(); LAUNCH = auto()
    SUPPORT = auto(); INCIDENT = auto(); EXPANSION = auto(); COMMERCIAL_COLLECTION = auto()
    RELATIONSHIP_MANAGEMENT = auto(); ADMINISTRATION = auto(); OTHER = auto()


class WorkPriority(Enum):
    CRITICAL = 4; HIGH = 3; NORMAL = 2; LOW = 1

    @classmethod
    def assess(cls, *, incident_severity: str = "", business_stopped: bool = False,
               customer_commitment: bool = False, deadline_imminent: bool = False,
               dependency_blocking: bool = False, cash_at_risk: bool = False) -> "WorkPriority":
        """Expose judgment inputs without an opaque customer-value score."""
        severity = getattr(incident_severity, "name", str(incident_severity)).upper()
        if business_stopped or severity in {"SEVERE", "CRITICAL"}:
            return cls.CRITICAL
        pressures = sum((customer_commitment, deadline_imminent, dependency_blocking, cash_at_risk))
        if severity == "HIGH" or pressures >= 2:
            return cls.HIGH
        if pressures == 1 or severity in {"MODERATE", "NORMAL"}:
            return cls.NORMAL
        return cls.LOW


class WorkStatus(Enum):
    BACKLOG = auto(); READY = auto(); IN_PROGRESS = auto(); BLOCKED = auto()
    DEFERRED = auto(); DONE = auto(); DECLINED = auto()


class CapacityState(Enum):
    UNDERUTILIZED = auto(); HEALTHY = auto(); BUSY = auto(); STRAINED = auto(); OVER_CAPACITY = auto()


class ProjectStartState(Enum):
    SIGNED = auto(); QUEUED = auto(); SCHEDULED = auto(); START_AUTHORIZED = auto()


class PortfolioDecision(Enum):
    DEFER_WORK = auto(); RESEQUENCE = auto(); DECLINE_NEW_WORK = auto()
    DELAY_KICKOFF = auto(); ADD_DELIVERY_PARTNER = auto(); USE_SPECIALIST = auto()
    REDUCE_SCOPE = auto(); PROTECT_INCIDENT_RESERVE = auto(); INCREASE_MARKETING = auto()
    REDUCE_MARKETING = auto(); REFER_OUT = auto()


class ResilienceResult(Enum):
    RESILIENT = auto(); DEGRADED = auto(); SERIOUS_RISK = auto(); BUSINESS_STOPS = auto()


@dataclass(frozen=True)
class PortfolioPeriod:
    name: str
    start: date
    end: date

    def __post_init__(self) -> None:
        if self.end < self.start:
            raise ValueError("portfolio period cannot end before it starts")


@dataclass(frozen=True)
class PortfolioWorkItem:
    work_id: str
    customer_name: str | None
    category: WorkCategory
    priority: WorkPriority
    status: WorkStatus
    owner_hours: float
    partner_hours: float = 0
    due: date | None = None
    business_impact: str = ""
    customer_commitment: bool = False
    dependency_blocking: bool = False
    cash_impact: float = 0
    source_record: object | None = None

    def __post_init__(self) -> None:
        if self.owner_hours < 0 or self.partner_hours < 0:
            raise ValueError("work hours cannot be negative")

    @property
    def open(self) -> bool:
        return self.status not in {WorkStatus.DONE, WorkStatus.DECLINED}


@dataclass
class PortfolioCustomer:
    name: str
    lifecycle_stage: LifecycleStage
    relationship_status: object | None = None
    active_project: object | None = None
    support_arrangement: object | None = None
    open_incidents: tuple[object, ...] = ()
    expansion_opportunities: tuple[object, ...] = ()
    payment_status: object | None = None
    expected_owner_hours: float = 0
    delivery_partner: str | None = None
    vendor: str | None = None
    next_action: str = ""
    risks: tuple[str, ...] = ()
    booked_revenue: float = 0
    contribution: float = 0
    support_burden_hours: float = 0
    receivables: float = 0
    project_start_state: ProjectStartState | None = None

    def __post_init__(self) -> None:
        values = (self.expected_owner_hours, self.booked_revenue, self.support_burden_hours, self.receivables)
        if any(value < 0 for value in values):
            raise ValueError("portfolio quantities cannot be negative")

    @property
    def start_authorized(self) -> bool:
        return self.project_start_state is ProjectStartState.START_AUTHORIZED


@dataclass(frozen=True)
class OwnerCapacity:
    total_working_hours: float
    allocations: Mapping[str, float]
    incident_reserve_hours: float = 0
    context_switch_hours: float = 0

    def __post_init__(self) -> None:
        if min(self.total_working_hours, self.incident_reserve_hours, self.context_switch_hours, *self.allocations.values()) < 0:
            raise ValueError("capacity cannot be negative")

    @property
    def committed_hours(self) -> float:
        return sum(self.allocations.values())

    @property
    def schedulable_hours(self) -> float:
        return max(0, self.total_working_hours - self.incident_reserve_hours - self.context_switch_hours)

    @property
    def customer_delivery_hours(self) -> float:
        keys = {"discovery", "solution_design", "delivery_coordination", "qa", "support"}
        return sum(hours for name, hours in self.allocations.items() if name in keys)

    @property
    def shortfall_hours(self) -> float:
        return max(0, self.committed_hours - self.schedulable_hours)

    @property
    def state(self) -> CapacityState:
        if not self.total_working_hours: return CapacityState.OVER_CAPACITY
        ratio = (self.committed_hours + self.incident_reserve_hours + self.context_switch_hours) / self.total_working_hours
        if ratio < .6: return CapacityState.UNDERUTILIZED
        if ratio <= .8: return CapacityState.HEALTHY
        if ratio <= .95: return CapacityState.BUSY
        if ratio <= 1: return CapacityState.STRAINED
        return CapacityState.OVER_CAPACITY


@dataclass(frozen=True)
class DeliveryCapacity:
    partner_available_hours: float
    committed_hours: float
    owner_coordination_hours: float
    specialist_available_hours: float = 0
    delivery_slots: int = 1
    starts_requested: int = 0
    risk: str = ""

    @property
    def shortfall_hours(self) -> float: return max(0, self.committed_hours - self.partner_available_hours)
    @property
    def constrained(self) -> bool: return self.shortfall_hours > 0 or self.starts_requested > self.delivery_slots
    @property
    def state(self) -> CapacityState:
        if self.constrained: return CapacityState.OVER_CAPACITY
        ratio = self.committed_hours / self.partner_available_hours if self.partner_available_hours else 1
        return CapacityState.BUSY if ratio > .8 else CapacityState.HEALTHY


@dataclass(frozen=True)
class SupportCapacity:
    owner_available_hours: float
    routine_support_hours: float
    incident_reserve_hours: float
    partner_support_hours: float = 0
    vendor_coordination_hours: float = 0

    @property
    def demand_hours(self) -> float:
        return self.routine_support_hours + self.incident_reserve_hours + self.partner_support_hours + self.vendor_coordination_hours
    @property
    def shortfall_hours(self) -> float: return max(0, self.demand_hours - self.owner_available_hours)
    @property
    def overloaded(self) -> bool: return self.shortfall_hours > 0


@dataclass(frozen=True)
class PipelineCoverage:
    leads: int = 0
    qualified_opportunities: int = 0
    discoveries: int = 0
    proposals: int = 0
    expected_close_timing: Mapping[str, str] = field(default_factory=dict)
    potential_revenue: float = 0
    owner_presales_hours: float = 0

    def coverage_ratio(self, revenue_target: float) -> float | None:
        return None if revenue_target <= 0 else self.potential_revenue / revenue_target


@dataclass(frozen=True)
class CapacityConflict:
    name: str
    required_hours: float
    available_hours: float
    affected_work: tuple[str, ...]
    decisions: tuple[PortfolioDecision, ...]
    rationale: str

    @property
    def shortfall_hours(self) -> float: return max(0, self.required_hours - self.available_hours)
    @property
    def exists(self) -> bool: return self.shortfall_hours > 0


@dataclass(frozen=True)
class PortfolioConcentration:
    revenue: Mapping[str, float]
    contribution: Mapping[str, float]
    owner_hours: Mapping[str, float]
    support_burden: Mapping[str, float]
    receivables: Mapping[str, float]
    partners: Mapping[str, float]
    vendors: Mapping[str, float]

    @staticmethod
    def largest_share(values: Mapping[str, float]) -> float:
        total = sum(values.values())
        return 0 if total <= 0 else max(values.values(), default=0) / total

    @property
    def vendor_correlated_risks(self) -> tuple[str, ...]:
        return tuple(name for name, count in self.vendors.items() if count > 1)


@dataclass(frozen=True)
class PortfolioRisk:
    description: str
    affected_customers: tuple[str, ...]
    severity: WorkPriority
    mitigation: PortfolioDecision | None = None


@dataclass
class CustomerPortfolio:
    period: PortfolioPeriod
    customers: list[PortfolioCustomer]
    work_items: list[PortfolioWorkItem]
    owner_capacity: OwnerCapacity
    delivery_capacity: DeliveryCapacity
    support_capacity: SupportCapacity
    pipeline: PipelineCoverage
    risks: list[PortfolioRisk] = field(default_factory=list)

    @property
    def booked_revenue(self) -> float: return sum(c.booked_revenue for c in self.customers)
    @property
    def potential_revenue(self) -> float: return self.pipeline.potential_revenue

    def prioritized_work(self) -> tuple[PortfolioWorkItem, ...]:
        """Priority reflects impact/commitment/blocking/cash, never customer size."""
        return tuple(sorted((w for w in self.work_items if w.open), key=lambda w: (-w.priority.value, w.due or date.max, w.work_id)))

    def concentration(self) -> PortfolioConcentration:
        def by(attr: str) -> dict[str, float]: return {c.name: float(getattr(c, attr)) for c in self.customers}
        partners: dict[str, float] = {}; vendors: dict[str, float] = {}
        for customer in self.customers:
            if customer.delivery_partner: partners[customer.delivery_partner] = partners.get(customer.delivery_partner, 0) + 1
            if customer.vendor: vendors[customer.vendor] = vendors.get(customer.vendor, 0) + 1
        return PortfolioConcentration(by("booked_revenue"), by("contribution"), by("expected_owner_hours"), by("support_burden_hours"), by("receivables"), partners, vendors)

    def owner_absence(self, business_days: int = 3) -> ResilienceResult:
        if business_days <= 0: return ResilienceResult.RESILIENT
        critical_owner_work = any(w.open and w.priority is WorkPriority.CRITICAL and w.owner_hours > 0 for w in self.work_items)
        delegated = all(w.owner_hours == 0 and w.partner_hours > 0 for w in self.work_items if w.open and w.priority in {WorkPriority.CRITICAL, WorkPriority.HIGH})
        if critical_owner_work: return ResilienceResult.BUSINESS_STOPS
        if self.owner_capacity.customer_delivery_hours > 0 and not delegated: return ResilienceResult.SERIOUS_RISK
        if self.work_items: return ResilienceResult.DEGRADED
        return ResilienceResult.RESILIENT


def capacity_conflict(name: str, work: Iterable[PortfolioWorkItem], available_hours: float,
                      decisions: tuple[PortfolioDecision, ...], rationale: str) -> CapacityConflict:
    items = tuple(item for item in work if item.open)
    return CapacityConflict(name, sum(item.owner_hours for item in items), available_hours,
                            tuple(item.work_id for item in items), decisions, rationale)
