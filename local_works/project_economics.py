"""Simulated payment, cash-timing, and actual project economics records."""
from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class PaymentStatus(Enum):
    NOT_DUE = "Not due"; DUE = "Due"; INVOICED_SIMULATED = "Invoiced (simulated)"
    RECEIVED_SIMULATED = "Received (simulated)"; PARTIALLY_RECEIVED = "Partially received"
    LATE = "Late"; DISPUTED = "Disputed"; WAIVED = "Waived"; WRITTEN_OFF = "Written off"


@dataclass(frozen=True)
class PaymentRecord:
    amount: float
    status: PaymentStatus
    due_point: str
    invoice_date: date | None = None
    due_date: date | None = None
    received_date: date | None = None

    def days_outstanding(self, as_of: date) -> int:
        if self.received_date or not self.due_date:
            return 0
        return max(0, (as_of - self.due_date).days)


@dataclass(frozen=True)
class PaymentSchedule:
    original_price: float
    approved_paid_changes: float = 0
    credits: float = 0
    payments_received: float = 0

    @property
    def total_customer_charges(self) -> float:
        return self.original_price + self.approved_paid_changes - self.credits

    @property
    def final_amount_due(self) -> float:
        return max(0.0, self.total_customer_charges - self.payments_received)


@dataclass(frozen=True)
class EstimateActual:
    original_estimate: float
    revised_forecast: float | None
    actual: float

    @property
    def variance(self) -> float:
        return self.actual - self.original_estimate


@dataclass(frozen=True)
class OwnerTime:
    activities: dict[str, float] = field(default_factory=dict)
    presales_activities: tuple[str, ...] = ("acquisition", "audit", "discovery", "solution_design", "proposal_sales", "closing")

    @property
    def total_hours(self) -> float:
        return sum(self.activities.values())

    @property
    def presales_hours(self) -> float:
        return sum(self.activities.get(name, 0) for name in self.presales_activities)

    @property
    def delivery_hours(self) -> float:
        return self.total_hours - self.presales_hours


@dataclass(frozen=True)
class ProjectEconomics:
    charges: PaymentSchedule
    delivery_partner_cost: float
    other_direct_costs: float
    owner_time: OwnerTime
    owner_hour_value: float

    @property
    def contribution(self) -> float:
        return self.charges.total_customer_charges - self.delivery_partner_cost - self.other_direct_costs

    @property
    def contribution_margin(self) -> float | None:
        total = self.charges.total_customer_charges
        return None if total == 0 else self.contribution / total

    @property
    def imputed_owner_time_value(self) -> float:
        return self.owner_time.total_hours * self.owner_hour_value

    @property
    def contribution_after_owner_time(self) -> float:
        return self.contribution - self.imputed_owner_time_value

    @property
    def contribution_per_owner_hour(self) -> float | None:
        hours = self.owner_time.total_hours
        return None if hours == 0 else self.contribution / hours


@dataclass(frozen=True)
class CashEvent:
    occurred_on: date
    amount: float
    description: str


def maximum_cash_exposure(events: list[CashEvent]) -> float:
    """Largest negative cumulative cash balance; inflows positive, costs negative."""
    balance = 0.0
    lowest = 0.0
    for event in sorted(events, key=lambda item: item.occurred_on):
        balance += event.amount
        lowest = min(lowest, balance)
    return -lowest


class EvidenceStatus(Enum):
    MEASUREMENT_PENDING = "Measurement pending"
    PARTIALLY_MEASURED = "Partially measured"
    MEASURED = "Measured"
    INCONCLUSIVE = "Inconclusive"


@dataclass(frozen=True)
class ValueRealizationPlan:
    baseline: str
    expected_value_hypothesis: str
    metrics: tuple[str, ...]
    windows: tuple[str, ...] = ("30_DAYS", "60_DAYS", "90_DAYS")
    evidence_status: EvidenceStatus = EvidenceStatus.MEASUREMENT_PENDING
    measured_value: float | None = None
