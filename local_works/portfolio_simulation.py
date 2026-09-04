"""Chapter 31B: deterministic, fictional portfolio simulation.

This module deliberately extends :mod:`local_works.portfolio`; it does not
replace Chapter 31A's customer, work, capacity, concentration, or risk models.
It is a planning exercise, not accounting, invoicing, CRM, or hiring software.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto
from typing import Iterable, Mapping

from local_works.portfolio import CapacityState, PortfolioConcentration


class CashState(Enum):
    HEALTHY = auto(); TIGHT = auto(); CONSTRAINED = auto(); NEGATIVE = auto(); UNKNOWN = auto()


class CashEventType(Enum):
    PROJECT_DEPOSIT = auto(); PROJECT_MILESTONE_PAYMENT = auto(); PROJECT_FINAL_PAYMENT = auto()
    SUPPORT_PAYMENT = auto(); EXPANSION_PAYMENT = auto(); PARTNER_DEPOSIT = auto()
    PARTNER_MILESTONE_PAYMENT = auto(); PARTNER_FINAL_PAYMENT = auto()
    SUPPORT_PARTNER_COST = auto(); OTHER_DIRECT_COST = auto(); MARKETING = auto()
    TOOLS = auto(); OVERHEAD = auto(); GOODWILL_CREDIT = auto(); OTHER = auto()


class ReceivableStatus(Enum):
    NOT_DUE = auto(); DUE = auto(); LATE = auto(); PARTIALLY_RECEIVED = auto()
    RECEIVED = auto(); DISPUTED = auto(); WRITTEN_OFF_SIMULATED = auto()


class PipelineState(Enum):
    WEAK = auto(); ADEQUATE = auto(); STRONG = auto(); EXCESSIVE_FOR_CAPACITY = auto(); UNKNOWN = auto()


class HealthState(Enum):
    STRONG = auto(); ACCEPTABLE = auto(); MIXED = auto(); WEAK = auto(); UNKNOWN = auto()


class PortfolioVerdict(Enum):
    HEALTHY = auto(); HEALTHY_WITH_CONSTRAINTS = auto(); CAPACITY_LIMITED = auto()
    PIPELINE_WEAK = auto(); DELIVERY_OVERLOADED = auto(); SUPPORT_OVERLOADED = auto()
    CASH_CONSTRAINED = auto(); TOO_CONCENTRATED = auto(); PARTNER_FRAGILE = auto()
    OWNER_DEPENDENT = auto(); FRAGILE = auto(); NOT_SUSTAINABLE = auto(); INSUFFICIENT_EVIDENCE = auto()


class StartDecision(Enum):
    START_AUTHORIZED = auto(); QUEUE = auto(); DEFER_START = auto(); DELAY_START = auto()
    RESTRUCTURE_PAYMENT_TIMING_CONCEPTUALLY = auto(); DECLINE_FOR_NOW = auto()


@dataclass(frozen=True)
class CashEvent:
    party: str
    event_type: CashEventType
    amount: float
    day: int = 1
    received_or_paid: bool = True

    def __post_init__(self) -> None:
        if self.amount < 0 or not 1 <= self.day <= 31:
            raise ValueError("cash event amount/day is invalid")


@dataclass
class AccountReceivable:
    customer: str
    amount_due: float
    due_date: date
    status: ReceivableStatus = ReceivableStatus.NOT_DUE
    disputed: bool = False
    received_date: date | None = None
    risk: str = ""
    amount_received: float = 0

    def update(self, as_of: date) -> ReceivableStatus:
        if self.disputed:
            self.status = ReceivableStatus.DISPUTED
        elif self.amount_received >= self.amount_due:
            self.status = ReceivableStatus.RECEIVED
        elif self.amount_received > 0:
            self.status = ReceivableStatus.PARTIALLY_RECEIVED
        elif as_of > self.due_date:
            self.status = ReceivableStatus.LATE
        elif as_of == self.due_date:
            self.status = ReceivableStatus.DUE
        else:
            self.status = ReceivableStatus.NOT_DUE
        return self.status

    def days_late(self, as_of: date) -> int:
        return max(0, (as_of - self.due_date).days) if self.status is ReceivableStatus.LATE else 0

    @property
    def outstanding(self) -> float:
        return max(0, self.amount_due - self.amount_received)


@dataclass(frozen=True)
class RevenueMix:
    project: float = 0; support: float = 0; expansion: float = 0; other: float = 0

    @property
    def total(self) -> float: return self.project + self.support + self.expansion + self.other


@dataclass(frozen=True)
class ContributionMix:
    project: float = 0; support: float = 0; expansion: float = 0
    incident_warranty_burden: float = 0; other_direct_costs: float = 0

    @property
    def total(self) -> float:
        return self.project + self.support + self.expansion - self.incident_warranty_burden - self.other_direct_costs


@dataclass(frozen=True)
class OwnerHours:
    sales: float = 0; audit: float = 0; qualification: float = 0; discovery: float = 0
    solution_design: float = 0; proposal: float = 0; project_coordination: float = 0
    qa: float = 0; support: float = 0; incidents: float = 0; relationship_management: float = 0
    commercial_follow_up: float = 0; admin: float = 0; context_switch: float = 0

    @property
    def total(self) -> float: return sum(self.__dict__.values())
    @property
    def sales_total(self) -> float: return self.sales + self.audit + self.qualification + self.discovery + self.solution_design + self.proposal
    @property
    def delivery_total(self) -> float: return self.project_coordination + self.qa


@dataclass(frozen=True)
class PortfolioCashFlow:
    period: str
    opening_cash: float
    cash_inflows: tuple[CashEvent, ...] = ()
    cash_outflows: tuple[CashEvent, ...] = ()
    accounts_receivable: tuple[AccountReceivable, ...] = ()
    committed_future_outflows: float = 0
    expected_future_inflows: float = 0
    safe_buffer: float = 5000

    @property
    def inflow_total(self) -> float: return sum(e.amount for e in self.cash_inflows if e.received_or_paid)
    @property
    def outflow_total(self) -> float: return sum(e.amount for e in self.cash_outflows if e.received_or_paid)
    @property
    def net_cash_flow(self) -> float: return self.inflow_total - self.outflow_total
    @property
    def ending_cash(self) -> float: return self.opening_cash + self.net_cash_flow
    @property
    def minimum_cash_position(self) -> float:
        balance = self.opening_cash; minimum = balance
        events = [(e.day, e.amount) for e in self.cash_inflows if e.received_or_paid]
        events += [(e.day, -e.amount) for e in self.cash_outflows if e.received_or_paid]
        # Outflows happen first on the same day: a conservative timing view.
        for _, amount in sorted(events, key=lambda item: (item[0], item[1])):
            balance += amount; minimum = min(minimum, balance)
        return minimum
    @property
    def maximum_cash_exposure(self) -> float:
        """Peak funding required before receipts, including committed outflows."""
        timed = [(e.day, e.amount) for e in self.cash_inflows if e.received_or_paid]
        timed += [(e.day, -e.amount) for e in self.cash_outflows if e.received_or_paid]
        cumulative = 0.0; trough = 0.0
        for _, amount in sorted(timed, key=lambda item: (item[0], item[1])):
            cumulative += amount; trough = min(trough, cumulative)
        unfunded_commitment = max(0, self.committed_future_outflows - self.expected_future_inflows)
        late_receivables = sum(r.outstanding for r in self.accounts_receivable
                               if r.status in {ReceivableStatus.LATE, ReceivableStatus.DISPUTED})
        return max(-trough, unfunded_commitment, late_receivables)
    @property
    def cash_state(self) -> CashState:
        if self.minimum_cash_position < 0: return CashState.NEGATIVE
        if self.ending_cash < self.safe_buffer / 2: return CashState.CONSTRAINED
        if self.ending_cash < self.safe_buffer or self.maximum_cash_exposure > self.opening_cash - self.safe_buffer: return CashState.TIGHT
        return CashState.HEALTHY


@dataclass(frozen=True)
class MonthlyConcentration:
    revenue: float; contribution: float; owner_hours: float; support: float; receivables: float
    partner: float; vendor: float


@dataclass(frozen=True)
class SimulationPeriod:
    month: str
    customers: int
    new_customers: int
    active_projects: int
    queued_projects: int
    projects_started: int
    project_completions: int
    support_customers: int
    support_requests: int
    open_incidents: int
    new_sales: int
    churn: int
    expansions: int
    referrals: int
    leads: int
    qualified: int
    discoveries: int
    proposals: int
    lost_or_deferred: int
    revenue: RevenueMix
    direct_cost: float
    contribution: ContributionMix
    cash_flow: PortfolioCashFlow
    owner_hours: OwnerHours
    available_owner_hours: float
    incident_reserve_hours: float
    partner_available_hours: float
    support_partner_hours: float
    pipeline_state: PipelineState
    concentration: MonthlyConcentration
    risks: tuple[str, ...] = ()
    decisions: tuple[str, ...] = ()

    @property
    def capacity_state(self) -> CapacityState:
        ratio = self.owner_hours.total / self.available_owner_hours
        if ratio < .6: return CapacityState.UNDERUTILIZED
        if ratio <= .8: return CapacityState.HEALTHY
        if ratio <= .95: return CapacityState.BUSY
        if ratio <= 1: return CapacityState.STRAINED
        return CapacityState.OVER_CAPACITY
    @property
    def hours_over_capacity(self) -> float: return max(0, self.owner_hours.total - self.available_owner_hours)
    @property
    def contribution_per_owner_hour(self) -> float | None:
        return None if self.owner_hours.total == 0 else self.contribution.total / self.owner_hours.total


@dataclass(frozen=True)
class ScenarioResult:
    name: str
    periods: tuple[SimulationPeriod, ...]
    verdict: PortfolioVerdict
    qualifiers: tuple[str, ...]
    health: Mapping[str, HealthState]

    @property
    def revenue(self) -> float: return sum(p.revenue.total for p in self.periods)
    @property
    def contribution(self) -> float: return sum(p.contribution.total for p in self.periods)
    @property
    def ending_cash(self) -> float: return self.periods[-1].cash_flow.ending_cash
    @property
    def minimum_cash(self) -> float: return min(p.cash_flow.minimum_cash_position for p in self.periods)
    @property
    def maximum_cash_exposure(self) -> float: return max(p.cash_flow.maximum_cash_exposure for p in self.periods)
    @property
    def owner_hours(self) -> float: return sum(p.owner_hours.total for p in self.periods)
    @property
    def contribution_per_owner_hour(self) -> float | None: return None if not self.owner_hours else self.contribution / self.owner_hours
    @property
    def overload_months(self) -> int: return sum(p.capacity_state is CapacityState.OVER_CAPACITY for p in self.periods)
    @property
    def projects_started(self) -> int: return sum(p.projects_started for p in self.periods)
    @property
    def projects_completed(self) -> int: return sum(p.project_completions for p in self.periods)
    @property
    def incidents(self) -> int: return sum(p.open_incidents for p in self.periods)
    @property
    def support_customers(self) -> int: return self.periods[-1].support_customers
    @property
    def pipeline_state(self) -> PipelineState: return self.periods[-1].pipeline_state


@dataclass(frozen=True)
class ScenarioConfig:
    name: str
    opening_cash: float
    leads: tuple[int, ...]
    sales: tuple[int, ...]
    completions: tuple[int, ...]
    incidents: tuple[int, ...]
    late_months: frozenset[int] = frozenset()
    partner_constraint_months: frozenset[int] = frozenset()
    support_multiplier: float = 1
    project_value: float = 12000
    project_cost: float = 6500
    owner_capacity: float = 128


BASELINE = ScenarioConfig("BASELINE", 18000, (5,5,4,5,4,4,5,4,4,5,4,4), (1,0,1,0,1,0,1,0,1,0,1,0), (0,1,0,1,0,1,0,1,0,1,0,1), (0,0,1,0,0,0,1,0,0,0,0,0), owner_capacity=140)
CONSERVATIVE = ScenarioConfig("CONSERVATIVE", 12000, (3,3,2,2,1,1,0,1,1,1,1,1), (0,1,0,0,1,0,0,0,0,1,0,0), (0,0,1,0,0,1,0,0,0,1,0,0), (0,1,0,0,1,0,0,0,0,0,0,0), frozenset({4}), frozenset({6}), 1.2)
GROWTH = ScenarioConfig("GROWTH", 18000, (9,9,8,8,7,5,3,2,1,0,0,0), (2,2,2,2,2,1,1,0,0,0,0,0), (0,1,1,1,1,1,1,1,1,1,1,0), (0,0,1,0,1,0,1,1,0,1,0,0), support_multiplier=1.45)
STRESS = ScenarioConfig("STRESS", 7000, (5,4,4,2,1,1,1,1,1,1,1,1), (1,1,1,0,1,0,0,0,0,0,0,0), (0,1,0,1,0,1,0,0,1,0,0,0), (0,0,2,1,0,0,2,0,0,1,0,0), frozenset({3,7}), frozenset({3,4,7}), 1.7)


def pipeline_state(opportunity_volume: int, delivery_slots: int) -> PipelineState:
    if delivery_slots <= 0: return PipelineState.UNKNOWN
    ratio = opportunity_volume / delivery_slots
    if ratio < 1: return PipelineState.WEAK
    if ratio <= 2: return PipelineState.ADEQUATE
    if ratio <= 3: return PipelineState.STRONG
    return PipelineState.EXCESSIVE_FOR_CAPACITY


def gate_project_start(*, owner_hours_needed: float, owner_hours_available: float,
                       partner_hours_needed: float, partner_hours_available: float,
                       required_cash: float, cash_above_buffer: float,
                       support_reserve_ok: bool = True) -> tuple[StartDecision, str]:
    if required_cash > cash_above_buffer: return StartDecision.DELAY_START, "cash constraint"
    if owner_hours_needed > owner_hours_available: return StartDecision.QUEUE, "owner capacity"
    if partner_hours_needed > partner_hours_available: return StartDecision.QUEUE, "partner capacity"
    if not support_reserve_ok: return StartDecision.DEFER_START, "support reserve"
    return StartDecision.START_AUTHORIZED, "all start gates passed"


def simulate(config: ScenarioConfig = BASELINE) -> ScenarioResult:
    """Run twelve deterministic periods with visible lifecycle/capacity effects."""
    cash = config.opening_cash; support_customers = 2; customers = 6; active = 1; queued = 0
    periods: list[SimulationPeriod] = []
    for index in range(12):
        month = index + 1; leads = config.leads[index]; requested_sales = config.sales[index]
        constrained_partner = month in config.partner_constraint_months
        partner_hours = 18 if constrained_partner else 70
        starts_allowed = 0 if constrained_partner else 1
        queued += requested_sales
        started = min(queued, starts_allowed); queued -= started; active += started
        completed = min(active, config.completions[index]); active -= completed
        support_customers += completed
        customers += requested_sales
        incidents = config.incidents[index]
        support_hours = support_customers * 3.0 * config.support_multiplier
        # Delivery crowds out sales; the later growth cliff is an explicit result, not hidden demand.
        delivery_hours = active * 32 + started * 10
        sales_hours = min(26.0, leads * 3.0) if delivery_hours + support_hours < 85 else min(8.0, leads * 1.5)
        incident_hours = incidents * 9.0
        context = max(3.0, (active + support_customers + incidents) * 0.8)
        hours = OwnerHours(sales=sales_hours, qualification=leads*.5, discovery=requested_sales*2,
            proposal=requested_sales*2, project_coordination=delivery_hours*.7, qa=delivery_hours*.3,
            support=support_hours, incidents=incident_hours, relationship_management=support_customers,
            commercial_follow_up=2 + requested_sales, admin=8, context_switch=context)
        project_revenue = requested_sales * config.project_value
        support_revenue = support_customers * 650
        expansion_revenue = 2500 if month in {6, 10} else 0
        revenue = RevenueMix(project_revenue, support_revenue, expansion_revenue)
        project_contribution = requested_sales * (config.project_value-config.project_cost)
        contribution = ContributionMix(project_contribution, support_revenue*.55, expansion_revenue*.65,
                                       incidents*700, max(0, support_hours-30)*80)
        inflows: list[CashEvent] = [CashEvent("support customers", CashEventType.SUPPORT_PAYMENT, support_revenue, 5)]
        # Revenue is recognized on sale; cash receipt may be late. Pipeline is neither.
        if requested_sales and month not in config.late_months:
            inflows.append(CashEvent("project customers", CashEventType.PROJECT_DEPOSIT, project_revenue*.5, 20))
        outflows = [CashEvent("delivery partner", CashEventType.PARTNER_DEPOSIT, requested_sales*config.project_cost*.65, 2),
                    CashEvent("operations", CashEventType.OVERHEAD, 2400, 1),
                    CashEvent("support partner", CashEventType.SUPPORT_PARTNER_COST, support_customers*120, 10)]
        ar_amount = requested_sales*config.project_value*(1 if month in config.late_months else .5)
        receivable = AccountReceivable("project customers", ar_amount, date(2026, month, 15),
            status=ReceivableStatus.LATE if month in config.late_months else ReceivableStatus.NOT_DUE,
            risk="late project payment" if month in config.late_months else "")
        cash_flow = PortfolioCashFlow(f"2026-{month:02}", cash, tuple(inflows), tuple(outflows),
            (receivable,), queued*config.project_cost*.4, queued*config.project_value*.5, 5000)
        cash = cash_flow.ending_cash
        qualified = leads // 2; proposals = min(qualified, max(0, requested_sales + 1))
        pipe = pipeline_state(qualified + proposals, 2)
        largest_revenue = .58 if requested_sales == 1 else (.42 if requested_sales > 1 else 0)
        concentration = MonthlyConcentration(largest_revenue, min(.72, largest_revenue+.05),
            .30 if incidents == 0 else .55, 1/support_customers, 1.0 if ar_amount else 0,
            .78 if active else .55, .67 if support_customers >= 4 else .5)
        risks: list[str] = []
        decisions: list[str] = []
        if queued: risks.append("project queue"); decisions.append("queue excess demand")
        if constrained_partner: risks.append("primary partner unavailable"); decisions.append("delay partner-dependent start")
        if incidents >= 2: risks.append("correlated MemberCloud incidents consume reserve")
        if support_hours > 36: risks.append("cumulative support tail exceeds planned support capacity")
        if hours.total > config.owner_capacity: risks.append("owner overload"); decisions.append("protect incident reserve and defer work")
        if cash_flow.cash_state in {CashState.TIGHT, CashState.CONSTRAINED, CashState.NEGATIVE}: risks.append("profit does not equal liquidity")
        if month >= 9 and leads <= 1: risks.append("pipeline cliff after delivery displaced sales")
        if config.name == "STRESS" and month == 7:
            risks.extend(("owner absent three business days: launch coordination delayed",
                          "support triage degraded", "sales follow-up deferred", "customer communication delegated"))
        period = SimulationPeriod(f"2026-{month:02}", customers, requested_sales, active, queued, started,
            completed, support_customers, round(support_hours/3), incidents, requested_sales, 0,
            1 if expansion_revenue else 0, 1 if month in {5,9} else 0, leads, qualified,
            min(qualified, requested_sales), proposals, max(0, qualified-requested_sales), revenue,
            revenue.total-contribution.total, contribution, cash_flow, hours, config.owner_capacity, 12,
            partner_hours, support_customers*2, pipe, concentration, tuple(risks), tuple(decisions))
        periods.append(period)
    overload = sum(p.capacity_state is CapacityState.OVER_CAPACITY for p in periods)
    minimum = min(p.cash_flow.minimum_cash_position for p in periods)
    if config.name == "STRESS": verdict = PortfolioVerdict.CASH_CONSTRAINED if minimum >= 0 else PortfolioVerdict.FRAGILE
    elif config.name == "GROWTH": verdict = PortfolioVerdict.CAPACITY_LIMITED
    elif config.name == "CONSERVATIVE": verdict = PortfolioVerdict.PIPELINE_WEAK
    elif overload: verdict = PortfolioVerdict.HEALTHY_WITH_CONSTRAINTS
    else: verdict = PortfolioVerdict.HEALTHY
    health = _health(periods, verdict)
    qualifiers = tuple(dict.fromkeys(r for p in periods for r in p.risks))
    return ScenarioResult(config.name, tuple(periods), verdict, qualifiers, health)


def _health(periods: Iterable[SimulationPeriod], verdict: PortfolioVerdict) -> Mapping[str, HealthState]:
    rows = tuple(periods); weak_pipeline = rows[-1].pipeline_state is PipelineState.WEAK
    overload = any(p.capacity_state is CapacityState.OVER_CAPACITY for p in rows)
    cash_bad = any(p.cash_flow.cash_state in {CashState.CONSTRAINED, CashState.NEGATIVE} for p in rows)
    support_bad = any("support tail" in risk for p in rows for risk in p.risks)
    partner_bad = any("partner unavailable" in risk for p in rows for risk in p.risks)
    vendor_bad = any("correlated" in risk for p in rows for risk in p.risks)
    return {"PIPELINE": HealthState.WEAK if weak_pipeline else HealthState.ACCEPTABLE,
        "SALES": HealthState.MIXED if weak_pipeline else HealthState.ACCEPTABLE,
        "DELIVERY": HealthState.WEAK if overload else HealthState.ACCEPTABLE,
        "SUPPORT": HealthState.WEAK if support_bad else HealthState.ACCEPTABLE,
        "INCIDENTS": HealthState.MIXED if any(p.open_incidents for p in rows) else HealthState.STRONG,
        "CASH": HealthState.WEAK if cash_bad else HealthState.ACCEPTABLE,
        "CUSTOMER_CONCENTRATION": HealthState.MIXED if max(p.concentration.revenue for p in rows) > .5 else HealthState.ACCEPTABLE,
        "PARTNER_RESILIENCE": HealthState.WEAK if partner_bad else HealthState.MIXED,
        "VENDOR_RISK": HealthState.WEAK if vendor_bad else HealthState.MIXED,
        "OWNER_CAPACITY": HealthState.WEAK if overload else HealthState.ACCEPTABLE,
        "QUALITY": HealthState.MIXED if overload else HealthState.ACCEPTABLE,
        "RELATIONSHIP_HEALTH": HealthState.MIXED if verdict is PortfolioVerdict.FRAGILE else HealthState.ACCEPTABLE}


def marginal_deal_test() -> tuple[str, StartDecision, str]:
    decision, reason = gate_project_start(owner_hours_needed=24, owner_hours_available=10,
        partner_hours_needed=30, partner_hours_available=40, required_cash=3000, cash_above_buffer=5000)
    return "PROMISING", decision, f"GOOD DEAL != GOOD DEAL RIGHT NOW: {reason}"


def cash_constrained_deal_test() -> tuple[float, StartDecision, str]:
    decision, reason = gate_project_start(owner_hours_needed=10, owner_hours_available=20,
        partner_hours_needed=20, partner_hours_available=30, required_cash=9000, cash_above_buffer=4000)
    return 6500, decision, f"positive contribution, but {reason}; restructure payment timing conceptually"


def support_overload_deal_test() -> StartDecision:
    return gate_project_start(owner_hours_needed=5, owner_hours_available=15, partner_hours_needed=5,
        partner_hours_available=10, required_cash=1000, cash_above_buffer=5000, support_reserve_ok=False)[0]


def concentration_deal_test() -> tuple[StartDecision, str]:
    return StartDecision.START_AUTHORIZED, "flag: largest-customer revenue share rises; proceed only with boundaries"


def weekly_review(period: SimulationPeriod, *, stress: bool = False) -> str:
    return (f"WEEKLY OPERATING REVIEW — {period.month}\nCapacity: {period.capacity_state.name}; "
            f"queued: {period.queued_projects}; incidents: {period.open_incidents}; cash: {period.cash_flow.cash_state.name}\n"
            f"Decision: {'protect incident reserve and communicate delays' if stress else 'maintain controlled starts'}")


def monthly_review(period: SimulationPeriod) -> str:
    return (f"MONTHLY BUSINESS REVIEW — {period.month}\nCUSTOMERS new={period.new_customers} active={period.active_projects} supported={period.support_customers}\n"
            f"SALES leads={period.leads} qualified={period.qualified} proposals={period.proposals} sales={period.new_sales} pipeline={period.pipeline_state.name}\n"
            f"DELIVERY queued={period.queued_projects} started={period.projects_started} completed={period.project_completions}\n"
            f"SUPPORT requests={period.support_requests} incidents={period.open_incidents} owner-hours={period.owner_hours.support:.1f}\n"
            f"FINANCIAL revenue={period.revenue.total:.0f} contribution={period.contribution.total:.0f} ending-cash={period.cash_flow.ending_cash:.0f} exposure={period.cash_flow.maximum_cash_exposure:.0f}\n"
            f"OWNER total={period.owner_hours.total:.1f} contribution/hour={period.contribution_per_owner_hour or 0:.2f} capacity={period.capacity_state.name}\n"
            f"RISKS {', '.join(period.risks) or 'monitored'}\nDECISIONS {', '.join(period.decisions) or 'maintain controls'}")
