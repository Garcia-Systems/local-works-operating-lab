"""Two-sided, evidence-aware engagement pricing for Chapter 15.

This module is an internal decision aid.  It neither creates a proposal nor
guarantees a sale, and contribution is deliberately not called profit.
"""

from dataclasses import dataclass, field, replace
from enum import Enum


class PricingModel(Enum):
    FIXED_FEE = "Fixed fee"
    TIME_AND_MATERIALS = "Time and materials"
    PHASED = "Phased"
    RETAINER = "Retainer"
    SUBSCRIPTION = "Subscription"
    HYBRID = "Hybrid"


class PricingDecision(Enum):
    HEALTHY_PRICE_IDENTIFIED = "Healthy price identified"
    RESTRUCTURE_SCOPE = "Restructure scope"
    PHASE_PROJECT = "Phase project"
    NEED_BETTER_COST_ESTIMATE = "Need better cost estimate"
    NEED_BETTER_VALUE_EVIDENCE = "Need better value evidence"
    NO_HEALTHY_PRICE = "No healthy price"
    DECLINE = "Decline"


class CostType(Enum):
    DELIVERY_PARTNER_COST = "Delivery partner cost"
    SOFTWARE_TOOL_COST = "Software / tool cost"
    CONTRACTOR_COST = "Contractor cost"
    SPECIALIST_COST = "Specialist cost"
    TRAVEL_DIRECT_EXPENSE = "Travel / direct expense"
    OTHER_DIRECT_PROJECT_COST = "Other direct project cost"


class RiskType(Enum):
    SCOPE_UNCERTAINTY = "Scope uncertainty"
    DELIVERY_COST_UNCERTAINTY = "Delivery cost uncertainty"
    CUSTOMER_VALUE_UNCERTAINTY = "Customer value uncertainty"
    PAYMENT_RISK = "Payment risk"
    TIMING_RISK = "Timing risk"
    DEPENDENCY_RISK = "Dependency risk"
    SUPPORT_EXPOSURE = "Support exposure"
    CHANGE_RISK = "Change risk"
    OTHER = "Other"


class PaymentTiming(Enum):
    UPFRONT = "Upfront"
    DEPOSIT_PLUS_FINAL = "Deposit plus final"
    MILESTONE = "Milestone"
    MONTHLY = "Monthly"
    ON_COMPLETION = "On completion"


@dataclass(frozen=True)
class PricingComponent:
    name: str
    cost_type: CostType
    amount: float | None
    evidence: str = "UNKNOWN"
    is_delivery_partner: bool = False

    def __post_init__(self) -> None:
        if self.amount is not None and self.amount < 0:
            raise ValueError("Direct cost cannot be negative.")
        if self.amount is None and self.evidence != "UNKNOWN":
            raise ValueError("A missing cost must remain UNKNOWN.")


@dataclass(frozen=True)
class PricingRisk:
    category: RiskType
    severity: str
    evidence: str
    mitigation: str


@dataclass(frozen=True)
class PaymentEvent:
    stage: int
    amount: float
    description: str


@dataclass(frozen=True)
class PaymentStructure:
    timing: PaymentTiming
    customer_payments: tuple[PaymentEvent, ...]
    cost_payments: tuple[PaymentEvent, ...]

    @property
    def deposit(self) -> float:
        return sum(p.amount for p in self.customer_payments if p.stage == 0)

    @property
    def maximum_cash_exposure(self) -> float:
        """Largest cumulative cash deficit, with receipts applied before costs."""
        balance = 0.0
        lowest = 0.0
        stages = sorted({e.stage for e in self.customer_payments + self.cost_payments})
        for stage in stages:
            balance += sum(e.amount for e in self.customer_payments if e.stage == stage)
            balance -= sum(e.amount for e in self.cost_payments if e.stage == stage)
            lowest = min(lowest, balance)
        return -lowest


@dataclass(frozen=True)
class ContributionAnalysis:
    customer_price: float
    delivery_partner_cost: float
    other_direct_cost: float
    owner_hours: float
    owner_hour_value: float

    @property
    def imputed_owner_time_cost(self) -> float:
        return self.owner_hours * self.owner_hour_value

    @property
    def contribution(self) -> float:
        return self.customer_price - self.delivery_partner_cost - self.other_direct_cost

    @property
    def contribution_margin(self) -> float | None:
        return None if self.customer_price == 0 else self.contribution / self.customer_price

    @property
    def contribution_after_owner_time(self) -> float:
        return self.contribution - self.imputed_owner_time_cost

    @property
    def contribution_after_owner_time_margin(self) -> float | None:
        return None if self.customer_price == 0 else self.contribution_after_owner_time / self.customer_price


@dataclass(frozen=True)
class CustomerEconomicsView:
    current_annual_burden: float | None
    recoverable_annual_value: float | None
    recurring_solution_cost: float | None
    customer_price: float
    other_first_year_customer_cost: float = 0.0
    evidence_quality: str = "UNKNOWN"

    @property
    def annual_net_benefit(self) -> float | None:
        if self.recoverable_annual_value is None or self.recurring_solution_cost is None:
            return None
        return self.recoverable_annual_value - self.recurring_solution_cost

    @property
    def first_year_cost(self) -> float | None:
        if self.recurring_solution_cost is None:
            return None
        return self.customer_price + self.recurring_solution_cost + self.other_first_year_customer_cost

    @property
    def payback_months(self) -> float | None:
        benefit = self.annual_net_benefit
        if benefit is None or benefit <= 0:
            return None
        return (self.customer_price + self.other_first_year_customer_cost) / benefit * 12

    def cumulative_customer_result(self, years: int) -> float | None:
        if years < 1 or self.annual_net_benefit is None:
            return None
        return self.annual_net_benefit * years - self.customer_price - self.other_first_year_customer_cost


@dataclass(frozen=True)
class LocalWorksEconomicsView:
    delivery_partner_cost: float
    other_direct_cost: float
    owner_hours: float
    owner_hour_value: float
    required_direct_contribution: float

    @property
    def imputed_owner_time_cost(self) -> float:
        return self.owner_hours * self.owner_hour_value

    @property
    def economic_floor(self) -> float:
        return (self.delivery_partner_cost + self.other_direct_cost +
                self.imputed_owner_time_cost + self.required_direct_contribution)

    def contribution_at(self, price: float) -> ContributionAnalysis:
        return ContributionAnalysis(price, self.delivery_partner_cost, self.other_direct_cost,
                                    self.owner_hours, self.owner_hour_value)


@dataclass(frozen=True)
class PricingWindow:
    floor: float | None
    ceiling: float | None

    @property
    def has_overlap(self) -> bool | None:
        if self.floor is None or self.ceiling is None:
            return None
        return self.floor <= self.ceiling

    @property
    def decision(self) -> PricingDecision:
        if self.floor is None:
            return PricingDecision.NEED_BETTER_COST_ESTIMATE
        if self.ceiling is None:
            return PricingDecision.NEED_BETTER_VALUE_EVIDENCE
        return (PricingDecision.HEALTHY_PRICE_IDENTIFIED if self.has_overlap
                else PricingDecision.NO_HEALTHY_PRICE)


@dataclass(frozen=True)
class PriceScenario:
    name: str
    model: PricingModel
    customer: CustomerEconomicsView
    local_works: LocalWorksEconomicsView
    scope: str
    phases: tuple[tuple[str, float | None], ...] = ()
    budget_guardrail: float | None = None

    @property
    def contribution(self) -> ContributionAnalysis:
        return self.local_works.contribution_at(self.customer.customer_price)

    def reduce_price(self, new_price: float) -> "PriceScenario":
        """Change price only; scope never changes implicitly."""
        return replace(self, customer=replace(self.customer, customer_price=new_price))


@dataclass(frozen=True)
class DiscountResult:
    discount_rate: float
    discounted_price: float
    contribution: float
    contribution_change_rate: float | None


def discount_sensitivity(analysis: ContributionAnalysis, rate: float) -> DiscountResult:
    if not 0 <= rate <= 1:
        raise ValueError("Discount rate must be between zero and one.")
    price = analysis.customer_price * (1 - rate)
    contribution = price - analysis.delivery_partner_cost - analysis.other_direct_cost
    change = None if analysis.contribution == 0 else (analysis.contribution - contribution) / analysis.contribution
    return DiscountResult(rate, price, contribution, change)


def customer_ceiling_for_payback(annual_net_benefit: float | None,
                                 maximum_payback_months: float,
                                 other_first_year_customer_cost: float = 0.0) -> float | None:
    """A stated payback guardrail, not a universal or value-derived standard."""
    if annual_net_benefit is None or annual_net_benefit <= 0:
        return None
    return max(0.0, annual_net_benefit * maximum_payback_months / 12 -
               other_first_year_customer_cost)


@dataclass
class PricingEstimate:
    scenario: PriceScenario
    window: PricingWindow
    payment: PaymentStructure | None = None
    risks: list[PricingRisk] = field(default_factory=list)
    decision: PricingDecision | None = None

    @property
    def effective_decision(self) -> PricingDecision:
        return self.decision or self.window.decision

    @property
    def creates_proposal(self) -> bool:
        return False

    @property
    def guarantees_sale(self) -> bool:
        return False
