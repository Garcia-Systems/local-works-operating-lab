"""Hypothetical customer-acquisition economics for Chapter 5.

The models deliberately keep cash, owner time, and outcomes separate.  A result
can describe arithmetic, but cannot establish that a channel works.
"""

from dataclasses import dataclass
from collections.abc import Iterable

from local_works.acquisition import FunnelResult, FunnelStage
from local_works.hypothesis import EvidenceType


@dataclass(frozen=True)
class AcquisitionCost:
    """One attributable acquisition input; either field may be zero."""

    category: str
    cash_amount: float = 0.0
    owner_hours: float = 0.0
    notes: str = ""
    evidence_type: EvidenceType = EvidenceType.HYPOTHESIS

    def __post_init__(self) -> None:
        if self.cash_amount < 0 or self.owner_hours < 0:
            raise ValueError("Acquisition cash and owner hours cannot be negative.")


@dataclass(frozen=True)
class OwnerTimeActivity:
    """A transparent stage/activity time assumption."""

    activity: str
    activity_count: int
    minutes_each: float
    evidence_type: EvidenceType = EvidenceType.HYPOTHESIS

    def __post_init__(self) -> None:
        if self.activity_count < 0 or self.minutes_each < 0:
            raise ValueError("Activity count and minutes cannot be negative.")

    @property
    def owner_hours(self) -> float:
        return self.activity_count * self.minutes_each / 60


@dataclass(frozen=True)
class AcquisitionEconomicsResult:
    name: str
    total_cash_cost: float
    total_owner_hours: float
    assumed_owner_hour_value: float
    customers_acquired: int
    cash_cac: float | None
    owner_hours_per_customer: float | None
    fully_loaded_cac: float | None
    evidence_type: EvidenceType
    is_simulated: bool
    notice: str

    @property
    def owner_time_cost(self) -> float:
        return self.total_owner_hours * self.assumed_owner_hour_value

    @property
    def fully_loaded_acquisition_cost(self) -> float:
        return self.total_cash_cost + self.owner_time_cost


@dataclass(frozen=True)
class StageCost:
    stage: FunnelStage
    count: float
    cash_cost_per_outcome: float | None
    fully_loaded_cost_per_outcome: float | None
    evidence_type: EvidenceType
    is_simulated: bool
    notice: str


@dataclass(frozen=True)
class ChannelEconomics:
    name: str
    costs: tuple[AcquisitionCost, ...]
    customers_acquired: int
    funnel_result: FunnelResult | None = None
    activities: tuple[OwnerTimeActivity, ...] = ()
    evidence_type: EvidenceType = EvidenceType.HYPOTHESIS

    def __post_init__(self) -> None:
        if self.customers_acquired < 0:
            raise ValueError("Customers acquired cannot be negative.")

    @property
    def total_cash_cost(self) -> float:
        return sum(cost.cash_amount for cost in self.costs)

    @property
    def total_owner_hours(self) -> float:
        return (sum(cost.owner_hours for cost in self.costs)
                + sum(activity.owner_hours for activity in self.activities))

    def calculate(self, owner_hour_value: float) -> AcquisitionEconomicsResult:
        if owner_hour_value < 0:
            raise ValueError("Assumed owner-hour value cannot be negative.")
        customers = self.customers_acquired
        cash = self.total_cash_cost
        hours = self.total_owner_hours
        loaded = cash + hours * owner_hour_value
        defined = customers > 0
        simulated = bool(self.funnel_result and self.funnel_result.is_simulated)
        return AcquisitionEconomicsResult(
            self.name, cash, hours, owner_hour_value, customers,
            cash / customers if defined else None,
            hours / customers if defined else None,
            loaded / customers if defined else None,
            self.evidence_type, simulated,
            ("SIMULATED OUTPUT IS NOT OBSERVED EVIDENCE."
             if simulated else "HYPOTHETICAL TRAINING ARITHMETIC — NOT LOCAL WORKS EVIDENCE."),
        )

    def cost_per_stage(self, owner_hour_value: float) -> tuple[StageCost, ...]:
        """Allocate total acquisition cost to each funnel outcome denominator."""
        if self.funnel_result is None:
            return ()
        result = self.calculate(owner_hour_value)
        steps = self.funnel_result.steps
        if not steps:
            return ()
        counts = [(steps[0].transition.from_stage, float(steps[0].entered))]
        counts.extend((step.transition.to_stage, float(step.advanced)) for step in steps)
        return tuple(StageCost(
            stage, count,
            result.total_cash_cost / count if count > 0 else None,
            result.fully_loaded_acquisition_cost / count if count > 0 else None,
            self.funnel_result.evidence_type,
            self.funnel_result.is_simulated,
            self.funnel_result.notice,
        ) for stage, count in counts)


@dataclass(frozen=True)
class AcquisitionPeriod:
    label: str
    economics: ChannelEconomics


def cumulative_economics(
    name: str, periods: Iterable[AcquisitionPeriod]
) -> ChannelEconomics:
    """Include unsuccessful earlier periods rather than only the eventual buyer."""
    period_list = tuple(periods)
    return ChannelEconomics(
        name=name,
        costs=tuple(cost for period in period_list for cost in period.economics.costs),
        activities=tuple(a for period in period_list for a in period.economics.activities),
        customers_acquired=sum(p.economics.customers_acquired for p in period_list),
        evidence_type=EvidenceType.HYPOTHESIS,
    )


def compare_channels(
    channels: Iterable[ChannelEconomics], owner_hour_value: float
) -> tuple[AcquisitionEconomicsResult, ...]:
    """Return comparable views without declaring an economically superior channel."""
    return tuple(channel.calculate(owner_hour_value) for channel in channels)
