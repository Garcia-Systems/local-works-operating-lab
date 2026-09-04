"""Chapter 29 models recurring-support economics, not billing or an SLA.

Money and hours are fictional planning assumptions.  Warranty, goodwill and
customer value deliberately remain separate from paid support economics.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Iterable, Mapping

from .support import SupportPlan

UNKNOWN = "UNKNOWN"


class SupportWorkCategory(Enum):
    HOW_TO = auto()
    CONFIGURATION = auto()
    ROUTINE_TROUBLESHOOTING = auto()
    INCIDENT_COORDINATION = auto()
    VENDOR_COORDINATION = auto()
    DELIVERY_PARTNER_COORDINATION = auto()
    DOCUMENTATION = auto()
    TRAINING = auto()
    SMALL_CHANGE = auto()
    ADMINISTRATION = auto()
    REPORTING = auto()
    OTHER = auto()


class RevenueModel(Enum):
    MONTHLY_FLAT_FEE = auto()
    PREPAID_HOURS = auto()
    PAY_AS_YOU_GO = auto()
    INCIDENT_FEE = auto()
    HYBRID = auto()
    NONE = auto()


class PartnerCostModel(Enum):
    PER_HOUR = auto()
    PREPAID_HOURS = auto()
    MONTHLY_RETAINER = auto()
    PER_INCIDENT = auto()
    WARRANTY_INCLUDED = auto()
    VENDOR_INCLUDED = auto()
    UNKNOWN = auto()


class InterruptionRisk(Enum):
    LOW = auto()
    MODERATE = auto()
    HIGH = auto()
    UNKNOWN = auto()


class CapacityState(Enum):
    HEALTHY = auto()
    BUSY = auto()
    STRAINED = auto()
    OVER_CAPACITY = auto()
    UNKNOWN = auto()


class RolloverPolicy(Enum):
    NO_ROLLOVER = auto()
    LIMITED_ROLLOVER = auto()
    ROLLOVER = auto()
    NOT_APPLICABLE = auto()


class OverageTreatment(Enum):
    BILLABLE_HOURLY = auto()
    QUOTE_REQUIRED = auto()
    DEFER_TO_NEXT_PERIOD = auto()
    NEW_PROJECT = auto()
    WAIVED_GOODWILL = auto()
    NOT_SUPPORTED = auto()


class SupportPlanVerdict(Enum):
    VIABLE = auto()
    VIABLE_WITH_BOUNDARIES = auto()
    VIABLE_AT_HIGHER_PRICE = auto()
    VIABLE_WITH_LOWER_SCOPE = auto()
    PAY_AS_YOU_GO_BETTER = auto()
    PREPAID_HOURS_BETTER = auto()
    CUSTOMER_SHOULD_USE_VENDOR_SUPPORT = auto()
    NOT_ECONOMICALLY_SENSIBLE = auto()
    NOT_OPERATIONALLY_SUSTAINABLE = auto()
    INSUFFICIENT_EVIDENCE = auto()


@dataclass(frozen=True)
class SupportDemandProfile:
    requests_per_month: float | str = UNKNOWN
    incidents_per_month: float | str = UNKNOWN
    owner_hours_per_month: float | str = UNKNOWN
    partner_hours_per_month: float | str = UNKNOWN
    vendor_coordination_hours: float | str = UNKNOWN
    training_hours: float | str = UNKNOWN
    configuration_hours: float | str = UNKNOWN
    documentation_hours: float | str = UNKNOWN
    after_hours_events: float | str = UNKNOWN
    high_severity_incidents: float | str = UNKNOWN
    routine_requests: float | str = UNKNOWN
    enhancement_requests_misrouted_as_support: float | str = UNKNOWN
    request_mix: Mapping[SupportWorkCategory, float] = field(default_factory=dict)
    seasonality: str = UNKNOWN
    uncertainty: str = UNKNOWN


@dataclass(frozen=True)
class SupportUsage:
    owner_hours: float
    partner_hours: float = 0.0
    vendor_coordination_hours: float = 0.0
    incidents: int = 0
    after_hours_events: int = 0
    goodwill_owner_hours: float = 0.0
    goodwill_partner_hours: float = 0.0
    warranty_owner_hours: float = 0.0
    warranty_partner_hours: float = 0.0
    work_mix: Mapping[SupportWorkCategory, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        values = (self.owner_hours, self.partner_hours, self.vendor_coordination_hours,
                  self.goodwill_owner_hours, self.goodwill_partner_hours,
                  self.warranty_owner_hours, self.warranty_partner_hours)
        if min(values) < 0 or self.incidents < 0 or self.after_hours_events < 0:
            raise ValueError("support usage cannot be negative")

    @property
    def paid_support_owner_hours(self) -> float:
        """Owner usage excludes separately recorded warranty and goodwill."""
        return self.owner_hours


@dataclass(frozen=True)
class SupportCost:
    partner_cost: float = 0.0
    fixed_direct_cost: float = 0.0
    variable_direct_cost: float = 0.0
    owner_hour_value: float = 0.0
    after_hours_availability_cost: float = 0.0

    @property
    def direct_cost(self) -> float:
        return (self.partner_cost + self.fixed_direct_cost +
                self.variable_direct_cost + self.after_hours_availability_cost)


@dataclass(frozen=True)
class SupportRevenue:
    model: RevenueModel
    amount: float


@dataclass(frozen=True)
class SupportContribution:
    revenue: float
    partner_cost: float
    other_direct_cost: float
    owner_hours: float
    owner_hour_value: float

    @property
    def contribution(self) -> float:
        return self.revenue - self.partner_cost - self.other_direct_cost

    @property
    def imputed_owner_time_value(self) -> float:
        return self.owner_hours * self.owner_hour_value

    @property
    def after_owner_time(self) -> float:
        return self.contribution - self.imputed_owner_time_value

    @property
    def margin(self) -> float | None:
        return None if self.revenue == 0 else self.contribution / self.revenue

    @property
    def contribution_per_owner_hour(self) -> float | None:
        return None if self.owner_hours == 0 else self.contribution / self.owner_hours


@dataclass(frozen=True)
class PartnerAvailability:
    available: bool | None = None
    response_reliability: str = UNKNOWN
    after_hours_available: bool | None = None
    continuity: str = UNKNOWN
    replacement_difficulty: str = UNKNOWN


@dataclass(frozen=True)
class SupportCustomerValue:
    benefits: tuple[str, ...]
    preventive_activities: tuple[str, ...] = ()
    evidence_strength: str = UNKNOWN
    value_state: str = UNKNOWN


@dataclass(frozen=True)
class SupportPlanOption:
    name: str
    revenue: SupportRevenue
    support_plan: SupportPlan | None
    included_owner_capacity: float | None
    included_partner_capacity: float = 0.0
    incident_treatment: str = "Approved separately"
    vendor_coordination: str = "Not included"
    after_hours: str = "Not included"
    exclusions: tuple[str, ...] = ()
    rollover: RolloverPolicy = RolloverPolicy.NOT_APPLICABLE
    overage: OverageTreatment = OverageTreatment.QUOTE_REQUIRED
    partner_cost_model: PartnerCostModel = PartnerCostModel.UNKNOWN
    unlimited: bool = False


@dataclass(frozen=True)
class SupportCapacity:
    monthly_owner_hours_available: float | None
    planned_support_hours: float
    incident_buffer: float
    after_hours_capacity: bool | None = None
    customer_count: int = 1

    @property
    def usable_planned_capacity(self) -> float | None:
        if self.monthly_owner_hours_available is None:
            return None
        return max(0.0, self.monthly_owner_hours_available - self.incident_buffer)

    @property
    def utilization(self) -> float | None:
        if not self.monthly_owner_hours_available:
            return None
        return self.planned_support_hours / self.monthly_owner_hours_available

    @property
    def state(self) -> CapacityState:
        if self.monthly_owner_hours_available is None:
            return CapacityState.UNKNOWN
        if self.planned_support_hours > self.monthly_owner_hours_available:
            return CapacityState.OVER_CAPACITY
        usable = self.usable_planned_capacity
        assert usable is not None
        if self.planned_support_hours > usable:
            return CapacityState.STRAINED
        ratio = self.planned_support_hours / usable if usable else float("inf")
        return CapacityState.BUSY if ratio >= 0.75 else CapacityState.HEALTHY


@dataclass(frozen=True)
class SupportBreakEven:
    monthly_revenue: float
    other_direct_cost: float
    owner_hour_value: float
    partner_hour_rate: float

    @property
    def owner_hours(self) -> float | None:
        if self.owner_hour_value <= 0:
            return None
        return max(0.0, self.monthly_revenue - self.other_direct_cost) / self.owner_hour_value

    @property
    def partner_hours(self) -> float | None:
        if self.partner_hour_rate <= 0:
            return None
        return max(0.0, self.monthly_revenue - self.other_direct_cost) / self.partner_hour_rate


@dataclass(frozen=True)
class SupportScenario:
    name: str
    usage: SupportUsage
    revenue: float
    partner_hour_rate: float
    other_direct_cost: float
    owner_hour_value: float
    capacity: SupportCapacity
    partner_available: bool = True
    interruption_risk: InterruptionRisk = InterruptionRisk.LOW

    @property
    def economics(self) -> SupportContribution:
        return SupportContribution(self.revenue, self.usage.partner_hours * self.partner_hour_rate,
                                   self.other_direct_cost, self.usage.owner_hours,
                                   self.owner_hour_value)

    def verdict(self) -> SupportPlanVerdict:
        if not self.partner_available and self.usage.partner_hours > 0:
            return SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE
        if self.capacity.state is CapacityState.OVER_CAPACITY:
            return SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE
        if self.economics.after_owner_time < 0:
            return SupportPlanVerdict.NOT_ECONOMICALLY_SENSIBLE
        if self.capacity.state is CapacityState.STRAINED or self.interruption_risk is InterruptionRisk.HIGH:
            return SupportPlanVerdict.VIABLE_WITH_BOUNDARIES
        return SupportPlanVerdict.VIABLE


@dataclass(frozen=True)
class AnnualSupportEconomics:
    revenue: float
    partner_cost: float
    direct_cost: float
    owner_hours: float
    contribution: float
    owner_time_adjusted_contribution: float
    incidents: int


def aggregate_annual(scenarios: Iterable[SupportScenario]) -> AnnualSupportEconomics:
    months = tuple(scenarios)
    economics = tuple(month.economics for month in months)
    return AnnualSupportEconomics(
        sum(item.revenue for item in economics),
        sum(item.partner_cost for item in economics),
        sum(item.partner_cost + item.other_direct_cost for item in economics),
        sum(month.usage.owner_hours for month in months),
        sum(item.contribution for item in economics),
        sum(item.after_owner_time for item in economics),
        sum(month.usage.incidents for month in months),
    )


def burden_concentration(owner_hours_by_customer: Mapping[str, float]) -> dict[str, float | None]:
    total = sum(owner_hours_by_customer.values())
    return {customer: (hours / total if total else None)
            for customer, hours in owner_hours_by_customer.items()}


def assess_plan(scenarios: Iterable[SupportScenario]) -> SupportPlanVerdict:
    """A recurring plan must survive its supplied stress cases."""
    cases = tuple(scenarios)
    if not cases:
        return SupportPlanVerdict.INSUFFICIENT_EVIDENCE
    verdicts = {case.verdict() for case in cases}
    if SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE in verdicts:
        return SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE
    if SupportPlanVerdict.NOT_ECONOMICALLY_SENSIBLE in verdicts:
        return SupportPlanVerdict.NOT_ECONOMICALLY_SENSIBLE
    if SupportPlanVerdict.VIABLE_WITH_BOUNDARIES in verdicts:
        return SupportPlanVerdict.VIABLE_WITH_BOUNDARIES
    return SupportPlanVerdict.VIABLE


def compare_monthly_with_payg(monthly: Iterable[SupportScenario], payg: Iterable[SupportScenario]) -> SupportPlanVerdict:
    recurring = tuple(monthly)
    usage_based = tuple(payg)
    if not recurring or not usage_based:
        return SupportPlanVerdict.INSUFFICIENT_EVIDENCE
    if assess_plan(recurring) in {SupportPlanVerdict.NOT_ECONOMICALLY_SENSIBLE,
                                 SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE}:
        return SupportPlanVerdict.PAY_AS_YOU_GO_BETTER
    recurring_adjusted = sum(case.economics.after_owner_time for case in recurring)
    payg_adjusted = sum(case.economics.after_owner_time for case in usage_based)
    return (SupportPlanVerdict.PAY_AS_YOU_GO_BETTER if payg_adjusted > recurring_adjusted
            else SupportPlanVerdict.VIABLE_WITH_BOUNDARIES)
