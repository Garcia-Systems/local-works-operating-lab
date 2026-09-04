"""Chapter 32A's transparent, deterministic 36-month business simulation.

The capstone connects Chapter 31's cash, capacity, revenue, contribution and
pipeline vocabulary over a longer horizon.  It is fictional planning data: it
does not estimate owner income, optimize assumptions, or make a business
verdict.
"""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from enum import Enum, auto
import random
from typing import Mapping

from local_works.portfolio import CapacityState, ProjectStartState
from local_works.portfolio_simulation import (
    CashEvent, CashEventType, CashState, ContributionMix, MonthlyConcentration,
    OwnerHours, PipelineState, PortfolioCashFlow, RevenueMix, gate_project_start,
)


class EvidenceStatus(Enum):
    HYPOTHESIS = auto(); SIMULATION_ASSUMPTION = auto(); OBSERVED = auto()
    MEASURED = auto(); DERIVED = auto(); UNKNOWN = auto()


class CustomerLifecycleState(Enum):
    PROSPECT = auto(); LEAD = auto(); QUALIFIED = auto(); DISCOVERY = auto()
    PROPOSAL = auto(); SIGNED = auto(); QUEUED = auto(); ACTIVE_PROJECT = auto()
    STABILIZING = auto(); SUPPORTED = auto(); QUIET_HEALTHY = auto()
    EXPANSION = auto(); AT_RISK = auto(); CHURNED = auto(); CLOSED = auto()


class SolutionPath(Enum):
    CONFIGURE = auto(); INTEGRATE = auto(); AUTOMATE = auto(); CUSTOM_BUILD = auto()
    LEAVE_ALONE = auto(); NO_DEAL = auto()


class ProjectPhase(Enum):
    KICKOFF = auto(); REQUIREMENTS = auto(); IMPLEMENTATION = auto(); QA = auto()
    ACCEPTANCE = auto(); LAUNCH = auto(); CLOSEOUT = auto()


class SupportMode(Enum):
    NO_SUPPORT = auto(); PAY_AS_YOU_GO = auto(); LIGHT_SUPPORT = auto()
    MANAGED_SUPPORT = auto(); VENDOR_SUPPORT_ONLY = auto()


class FailureReason(Enum):
    WORKING_CAPITAL_REQUIRED = auto(); CASH_FAILURE = auto()


class BusinessHealth(Enum):
    STRONG = auto(); ACCEPTABLE = auto(); MIXED = auto(); WEAK = auto(); UNKNOWN = auto()


class Bottleneck(Enum):
    DEMAND = auto(); SALES = auto(); DELIVERY = auto(); SUPPORT = auto(); CASH = auto()
    OWNER_CAPACITY = auto(); PARTNER_CAPACITY = auto(); OTHER = auto(); UNKNOWN = auto()


@dataclass(frozen=True)
class ScenarioAssumption:
    group: str
    name: str
    value: object
    unit: str
    evidence: EvidenceStatus = EvidenceStatus.SIMULATION_ASSUMPTION
    source: str = "Chapter 32A fictional baseline"


@dataclass(frozen=True)
class BusinessSimulationConfig:
    name: str = "BASELINE"
    horizon_months: int = 36
    seed: int = 32
    monthly_lead_volume: float = 5.0
    qualified_lead_rate: float = .48
    discovery_progression_rate: float = .72
    proposal_rate: float = .68
    close_rate: float = .42
    sales_cycle_delay_months: int = 2
    referral_rate: float = .055
    average_project_price: float = 15000
    project_price_variability: float = .12
    delivery_cost: float = 7200
    other_direct_cost: float = 700
    owner_presales_hours: float = 9
    owner_project_hours: float = 46
    project_duration_months: int = 3
    deposit_percentage: float = .4
    final_payment_delay_months: int = 1
    partner_payment_delay_months: int = 0
    project_delay_rate: float = .12
    support_adoption_rate: float = .62
    monthly_support_revenue: float = 625
    routine_support_hours: float = 2.4
    partner_support_cost: float = 105
    incident_rate: float = .055
    incident_owner_hours: float = 6
    incident_partner_cost: float = 240
    goodwill_hours: float = .35
    warranty_hours: float = 2.5
    expansion_signal_rate: float = .055
    expansion_qualification_rate: float = .55
    expansion_close_rate: float = .45
    expansion_price: float = 4800
    expansion_direct_cost: float = 1900
    support_monthly_churn_rate: float = .018
    quiet_relationship_rate: float = .32
    sustainable_owner_hours: float = 128
    temporary_maximum_hours: float = 150
    sales_time_budget: float = 30
    support_reserve_hours: float = 18
    incident_reserve_hours: float = 10
    max_concurrent_projects: int = 2
    partner_capacity_hours: float = 100
    opening_cash: float = 14500
    fixed_monthly_overhead: float = 2850
    reserve_target: float = 12000
    owner_time_value: float = 85
    owner_draw_policy: str = "PLACEHOLDER_ONLY_NO_DRAW_CALCULATION"
    absence_month: int = 20
    absence_hours: float = 32
    shared_vendor: str = "FictionalFlow"
    correlated_vendor_incident_month: int = 28

    def __post_init__(self) -> None:
        if self.horizon_months <= 0 or self.sales_cycle_delay_months < 1:
            raise ValueError("horizon must be positive and sales delay at least one month")
        if self.max_concurrent_projects < 1:
            raise ValueError("at least one project slot is required")

    def assumptions(self) -> tuple[ScenarioAssumption, ...]:
        groups = {
            "ACQUISITION": ("monthly_lead_volume", "qualified_lead_rate", "discovery_progression_rate", "proposal_rate", "close_rate", "sales_cycle_delay_months", "referral_rate"),
            "PROJECTS": ("average_project_price", "delivery_cost", "other_direct_cost", "owner_presales_hours", "owner_project_hours", "project_duration_months", "deposit_percentage", "project_delay_rate"),
            "SUPPORT": ("support_adoption_rate", "monthly_support_revenue", "routine_support_hours", "partner_support_cost", "incident_rate", "goodwill_hours", "warranty_hours"),
            "EXPANSION": ("expansion_signal_rate", "expansion_qualification_rate", "expansion_close_rate", "expansion_price", "expansion_direct_cost"),
            "RETENTION": ("support_monthly_churn_rate", "quiet_relationship_rate"),
            "CAPACITY": ("sustainable_owner_hours", "temporary_maximum_hours", "sales_time_budget", "support_reserve_hours", "incident_reserve_hours", "max_concurrent_projects", "partner_capacity_hours", "absence_month"),
            "CASH": ("opening_cash", "fixed_monthly_overhead", "reserve_target", "final_payment_delay_months", "partner_payment_delay_months"),
            "OWNER": ("owner_time_value", "owner_draw_policy"),
        }
        unit = lambda n: "rate" if "rate" in n or "percentage" in n else ("hours" if "hours" in n else ("currency" if any(x in n for x in ("price", "cost", "cash", "overhead", "target", "value")) else "count/months"))
        return tuple(ScenarioAssumption(g, n, getattr(self, n), unit(n)) for g, names in groups.items() for n in names)


@dataclass
class _Lead:
    lead_id: int; born: int; source: str = "outreach"; state: CustomerLifecycleState = CustomerLifecycleState.LEAD


@dataclass
class _Customer:
    customer_id: int; state: CustomerLifecycleState; joined: int
    support_mode: SupportMode = SupportMode.NO_SUPPORT; stable_since: int = 0
    revenue: float = 0; contribution: float = 0; owner_hours: float = 0; support_hours: float = 0


@dataclass
class _Project:
    project_id: int; customer_id: int; signed_month: int; price: float
    delivery_cost: float; other_cost: float; owner_hours: float
    state: ProjectStartState = ProjectStartState.SIGNED; age: int = 0
    delay_months: int = 0; expansion: bool = False; cash_received: float = 0
    completed_month: int | None = None

    @property
    def contribution(self) -> float: return self.price - self.delivery_cost - self.other_cost
    @property
    def cash_outstanding(self) -> float: return max(0, self.price - self.cash_received)
    @property
    def phase(self) -> ProjectPhase:
        phases = tuple(ProjectPhase)
        return phases[min(len(phases) - 1, int(self.age / max(1, 3 + self.delay_months) * len(phases)))]


@dataclass(frozen=True)
class OwnerWorkload:
    hours: OwnerHours
    available_hours: float
    sustainable_hours: float
    temporary_maximum_hours: float
    deferred_sales: int = 0
    deferred_project_work: float = 0
    support_backlog_hours: float = 0

    @property
    def total(self) -> float: return self.hours.total
    @property
    def state(self) -> CapacityState:
        ratio = self.total / max(1, self.available_hours)
        if ratio <= .7: return CapacityState.HEALTHY
        if ratio <= .9: return CapacityState.BUSY
        if ratio <= 1: return CapacityState.STRAINED
        return CapacityState.OVER_CAPACITY


@dataclass(frozen=True)
class BusinessCashPosition:
    flow: PortfolioCashFlow
    reserve_target: float

    @property
    def reserve_available(self) -> float: return max(0, self.flow.ending_cash - self.reserve_target)


@dataclass(frozen=True)
class PortfolioSnapshot:
    customers: int; signed_projects: int; queued_projects: int; active_projects: int
    completed_projects: int; support_customers: int; quiet_customers: int
    expansion_opportunities: int; churned_customers: int


@dataclass(frozen=True)
class RiskEvent:
    month: int; description: str; failure_reason: FailureReason | None = None


@dataclass(frozen=True)
class BusinessMonth:
    month_number: int; year_number: int; leads: int; referral_leads: int; qualified: int
    discoveries: int; proposals: int; sales: int; solution_mix: Mapping[SolutionPath, int]
    portfolio: PortfolioSnapshot; completed_projects: int; incidents: int
    correlated_vendor_incident: bool; expansions: int; churn: int
    revenue: RevenueMix; contribution: ContributionMix; cash: BusinessCashPosition
    owner_workload: OwnerWorkload; pipeline_state: PipelineState
    concentration: MonthlyConcentration; warranty_hours: float; paid_support_hours: float
    goodwill_hours: float; partner_incident_cost: float; risks: tuple[RiskEvent, ...]
    decisions: tuple[str, ...]

    @property
    def owner_hours(self) -> float: return self.owner_workload.total
    @property
    def capacity_state(self) -> CapacityState: return self.owner_workload.state


@dataclass(frozen=True)
class BusinessYear:
    year: int; leads: int; qualified_opportunities: int; sales: int; projects_delivered: int
    support_customers: int; revenue: float; contribution: float; minimum_cash: float
    ending_cash: float; owner_hours: float; incidents: int; expansions: int; churn: int
    overload_months: int; pipeline_condition: PipelineState


@dataclass(frozen=True)
class CapstoneFinding:
    bottleneck: Bottleneck; evidence: str


@dataclass(frozen=True)
class BusinessSimulationResult:
    scenario: str; months: tuple[BusinessMonth, ...]; years: tuple[BusinessYear, ...]
    health: Mapping[str, BusinessHealth]; primary_bottleneck: CapstoneFinding
    failure_reasons: tuple[FailureReason, ...]
    # Deliberately no owner-income verdict or Monte Carlo output in Part A.

    @property
    def total_revenue(self) -> float: return sum(m.revenue.total for m in self.months)
    @property
    def total_contribution(self) -> float: return sum(m.contribution.total for m in self.months)
    @property
    def minimum_cash(self) -> float: return min(m.cash.flow.minimum_cash_position for m in self.months)
    @property
    def ending_cash(self) -> float: return self.months[-1].cash.flow.ending_cash
    @property
    def owner_hours(self) -> float: return sum(m.owner_hours for m in self.months)
    @property
    def overload_months(self) -> int: return sum(m.capacity_state is CapacityState.OVER_CAPACITY for m in self.months)
    @property
    def working_capital_required(self) -> bool: return bool(self.failure_reasons)


BusinessScenario = BusinessSimulationConfig
BusinessReserve = BusinessCashPosition


class BusinessSimulation:
    """Stateful monthly engine, decomposed so each interaction stays inspectable."""
    def __init__(self, config: BusinessSimulationConfig = None) -> None:
        self.config = config or BASELINE
        self.random = random.Random(self.config.seed)
        self.leads: list[_Lead] = []; self.customers: list[_Customer] = []; self.projects: list[_Project] = []
        self.cash = self.config.opening_cash; self._next_lead = 1; self._next_customer = 1; self._next_project = 1
        self._cash_due: dict[int, list[tuple[str, float]]] = {}; self._support_backlog = 0.0

    def run(self) -> BusinessSimulationResult:
        months = tuple(self.simulate_month(number) for number in range(1, self.config.horizon_months + 1))
        years = tuple(summarize_year(year, months[(year-1)*12:year*12]) for year in range(1, (len(months)+11)//12 + 1))
        health = evaluate_health(months)
        finding = identify_primary_bottleneck(months, health)
        failures = tuple(dict.fromkeys(r.failure_reason for m in months for r in m.risks if r.failure_reason))
        return BusinessSimulationResult(self.config.name, months, years, health, finding, failures)

    def simulate_month(self, month: int) -> BusinessMonth:
        available = self.config.sustainable_owner_hours - (self.config.absence_hours if month == self.config.absence_month else 0)
        support = self.simulate_support(month)
        incidents, incident_hours, partner_incident_cost, correlated = self.simulate_incidents(month)
        project_hours = self.advance_projects(month)
        capacity_for_sales = max(0, available - support[0] - incident_hours - project_hours - 12)
        acquisition = self.advance_acquisition(month, capacity_for_sales)
        sales, mix = self.advance_pipeline(month, capacity_for_sales)
        self.authorize_project_starts(month, available - support[0] - incident_hours)
        expansions, expansion_revenue, expansion_contribution, expansion_hours = self.simulate_expansion(month)
        referrals = self.simulate_referrals(month)
        churn = self.simulate_churn(month)
        completed = sum(p.completed_month == month for p in self.projects)
        project_revenue = sum(p.price for p in self.projects if p.signed_month == month and not p.expansion)
        project_contribution = sum(p.contribution for p in self.projects if p.signed_month == month and not p.expansion)
        support_revenue = sum(self.config.monthly_support_revenue for c in self.customers if c.state is CustomerLifecycleState.SUPPORTED)
        support_cost = sum(self.config.partner_support_cost for c in self.customers if c.state is CustomerLifecycleState.SUPPORTED)
        revenue = RevenueMix(project_revenue, support_revenue, expansion_revenue)
        warranty, paid, goodwill = support[1:]
        burden = (warranty + goodwill + incident_hours) * self.config.owner_time_value + partner_incident_cost
        contribution = ContributionMix(project_contribution, support_revenue-support_cost, expansion_contribution, burden, sum(p.other_cost for p in self.projects if p.signed_month == month and not p.expansion))
        sales_hours = acquisition[1] + sales * self.config.owner_presales_hours + expansion_hours
        hours = OwnerHours(sales=acquisition[0]*.4, audit=acquisition[2]*1.2, qualification=acquisition[3]*.5,
            discovery=acquisition[4]*2, proposal=acquisition[5]*1.5, solution_design=sales*2,
            project_coordination=project_hours*.72, qa=project_hours*.28, support=paid+goodwill+warranty,
            incidents=incident_hours, relationship_management=max(1, len(self.customers)*.35), admin=10)
        excess = max(0, hours.total-available)
        deferred = max(0, len([l for l in self.leads if l.state is CustomerLifecycleState.QUALIFIED])-acquisition[4]) if excess else 0
        workload = OwnerWorkload(hours, available, self.config.sustainable_owner_hours, self.config.temporary_maximum_hours, deferred, excess*.35, self._support_backlog)
        cash = self.simulate_cash_flow(month, revenue, support_cost, partner_incident_cost)
        snapshot = self.build_month_snapshot()
        pipeline = evaluate_pipeline(sum(l.state in {CustomerLifecycleState.QUALIFIED, CustomerLifecycleState.DISCOVERY, CustomerLifecycleState.PROPOSAL} for l in self.leads), self.config.max_concurrent_projects, snapshot.queued_projects)
        concentration = self.calculate_concentration()
        risks: list[RiskEvent] = []
        decisions: list[str] = []
        if snapshot.queued_projects: risks.append(RiskEvent(month, "signed work is queued by start gates")); decisions.append("preserve finite project concurrency")
        if workload.state is CapacityState.OVER_CAPACITY: risks.append(RiskEvent(month, "owner workload exceeds absence-adjusted capacity")); decisions.append("defer noncritical sales/project work")
        if cash.flow.minimum_cash_position < 0: risks.append(RiskEvent(month, "cash timing requires working capital", FailureReason.WORKING_CAPITAL_REQUIRED)); decisions.append("do not assume free financing")
        if correlated: risks.append(RiskEvent(month, f"correlated {self.config.shared_vendor} incident affected supported customers"))
        if month == self.config.absence_month: risks.append(RiskEvent(month, "planned one-week owner absence reduced capacity; no owner work assumed in absent hours"))
        return BusinessMonth(month, (month-1)//12+1, acquisition[0]+referrals, referrals, acquisition[3], acquisition[4], acquisition[5], sales, mix,
            snapshot, completed, incidents, correlated, expansions, churn, revenue, contribution, cash, workload, pipeline,
            concentration, warranty, paid, goodwill, partner_incident_cost, tuple(risks), tuple(decisions))

    def advance_acquisition(self, month: int, capacity: float) -> tuple[int, float, int, int, int, int]:
        # A small startup ramp avoids pretending month one is mature.
        ramp = min(1, month/4); count = max(0, round(self.config.monthly_lead_volume*ramp + self.random.uniform(-.8, .8)))
        for _ in range(count): self.leads.append(_Lead(self._next_lead, month)); self._next_lead += 1
        workable = max(0, int(capacity/3)); audit = min(count, workable)
        candidates = [l for l in self.leads if l.state is CustomerLifecycleState.LEAD]
        qualified = 0
        for lead in candidates[:audit]:
            if self.random.random() < self.config.qualified_lead_rate: lead.state = CustomerLifecycleState.QUALIFIED; qualified += 1
            elif month-lead.born >= 2: lead.state = CustomerLifecycleState.CLOSED
        q = [l for l in self.leads if l.state is CustomerLifecycleState.QUALIFIED]
        discoveries = min(len(q), max(0, int((capacity-audit*1.2)/2)))
        discoveries = round(discoveries*self.config.discovery_progression_rate)
        for lead in q[:discoveries]: lead.state = CustomerLifecycleState.DISCOVERY
        d = [l for l in self.leads if l.state is CustomerLifecycleState.DISCOVERY]
        proposals = min(len(d), round(len(d)*self.config.proposal_rate), max(0, int((capacity-audit*1.2-discoveries*2)/1.5)))
        for lead in d[:proposals]: lead.state = CustomerLifecycleState.PROPOSAL
        return count, audit*1.2+discoveries*2+proposals*1.5, audit, qualified, discoveries, proposals

    def advance_pipeline(self, month: int, capacity: float) -> tuple[int, dict[SolutionPath, int]]:
        eligible = [l for l in self.leads if l.state is CustomerLifecycleState.PROPOSAL and month-l.born >= self.config.sales_cycle_delay_months]
        sales = 0; mix = {path: 0 for path in SolutionPath}
        paths = (SolutionPath.CONFIGURE, SolutionPath.INTEGRATE, SolutionPath.AUTOMATE, SolutionPath.CUSTOM_BUILD)
        for lead in eligible[:max(0, int(capacity/self.config.owner_presales_hours))]:
            draw = self.random.random()
            if draw < self.config.close_rate:
                path = paths[(lead.lead_id-1) % len(paths)]; mix[path] += 1; sales += 1
                lead.state = CustomerLifecycleState.SIGNED
                customer = _Customer(self._next_customer, CustomerLifecycleState.SIGNED, month); self.customers.append(customer)
                price = self.config.average_project_price*(1+self.random.uniform(-self.config.project_price_variability, self.config.project_price_variability))
                self.projects.append(_Project(self._next_project, customer.customer_id, month, round(price, 2), self.config.delivery_cost, self.config.other_direct_cost, self.config.owner_project_hours))
                self._next_customer += 1; self._next_project += 1
            else:
                path = SolutionPath.LEAVE_ALONE if lead.lead_id % 3 == 0 else SolutionPath.NO_DEAL
                mix[path] += 1; lead.state = CustomerLifecycleState.CLOSED
        return sales, mix

    def authorize_project_starts(self, month: int, owner_available: float) -> None:
        active = [p for p in self.projects if p.state is ProjectStartState.START_AUTHORIZED and p.age < self.config.project_duration_months+p.delay_months]
        for project in [p for p in self.projects if p.state in {ProjectStartState.SIGNED, ProjectStartState.QUEUED}]:
            decision, _ = gate_project_start(owner_hours_needed=project.owner_hours/self.config.project_duration_months,
                owner_hours_available=max(0, owner_available), partner_hours_needed=self.config.delivery_cost/100,
                partner_hours_available=max(0, self.config.partner_capacity_hours-len(active)*35),
                required_cash=project.delivery_cost*.45, cash_above_buffer=max(0, self.cash-self.config.reserve_target),
                support_reserve_ok=owner_available >= self.config.support_reserve_hours+self.config.incident_reserve_hours)
            if len(active) < self.config.max_concurrent_projects and decision.name == "START_AUTHORIZED":
                project.state = ProjectStartState.START_AUTHORIZED; active.append(project)
            else: project.state = ProjectStartState.QUEUED

    def advance_projects(self, month: int) -> float:
        hours = 0.0
        for project in self.projects:
            if project.state is not ProjectStartState.START_AUTHORIZED: continue
            if project.age == 1 and self.random.random() < self.config.project_delay_rate: project.delay_months = 1
            if project.age < self.config.project_duration_months+project.delay_months:
                project.age += 1; hours += project.owner_hours/(self.config.project_duration_months+project.delay_months)
            if project.age == self.config.project_duration_months+project.delay_months and project.completed_month is None:
                customer = self._customer(project.customer_id); customer.state = CustomerLifecycleState.STABILIZING; customer.stable_since = month
                project.completed_month = month
                if self.random.random() < self.config.support_adoption_rate:
                    customer.support_mode = (SupportMode.LIGHT_SUPPORT if customer.customer_id % 2 else SupportMode.MANAGED_SUPPORT)
                    customer.state = CustomerLifecycleState.SUPPORTED
                else: customer.state = CustomerLifecycleState.QUIET_HEALTHY
        return hours

    def simulate_support(self, month: int) -> tuple[float, float, float, float]:
        supported = [c for c in self.customers if c.state is CustomerLifecycleState.SUPPORTED]
        paid = len(supported)*self.config.routine_support_hours
        warranty = sum(self.config.warranty_hours for c in self.customers if c.state is CustomerLifecycleState.STABILIZING and month-c.stable_since <= 1)
        goodwill = len([c for c in self.customers if c.state in {CustomerLifecycleState.SUPPORTED, CustomerLifecycleState.QUIET_HEALTHY}])*self.config.goodwill_hours
        demand = paid+warranty+goodwill+self._support_backlog
        served = min(demand, self.config.support_reserve_hours+self._support_backlog)
        self._support_backlog = max(0, demand-served)
        return demand, warranty, paid, goodwill

    def simulate_incidents(self, month: int) -> tuple[int, float, float, bool]:
        supported = sum(c.state is CustomerLifecycleState.SUPPORTED for c in self.customers)
        correlated = month == self.config.correlated_vendor_incident_month and supported >= 2
        count = (min(3, supported) if correlated else sum(self.random.random() < self.config.incident_rate for _ in range(supported)))
        return count, count*self.config.incident_owner_hours, count*self.config.incident_partner_cost, correlated

    def simulate_expansion(self, month: int) -> tuple[int, float, float, float]:
        stable = [c for c in self.customers if c.state in {CustomerLifecycleState.SUPPORTED, CustomerLifecycleState.QUIET_HEALTHY} and month-c.stable_since >= 5]
        signals = [c for c in stable if self.random.random() < self.config.expansion_signal_rate]
        if stable and month in {18, 30} and not signals: signals = stable[:1]
        qualified = [c for c in signals if self.random.random() < self.config.expansion_qualification_rate]
        sold = [c for c in qualified if self.random.random() < self.config.expansion_close_rate]
        if qualified and month == 30 and not sold: sold = qualified[:1]
        for c in sold: c.state = CustomerLifecycleState.EXPANSION
        n = len(sold); return n, n*self.config.expansion_price, n*(self.config.expansion_price-self.config.expansion_direct_cost), len(signals)*1.5+len(qualified)*2+n*3

    def simulate_referrals(self, month: int) -> int:
        healthy = [c for c in self.customers if c.state in {CustomerLifecycleState.SUPPORTED, CustomerLifecycleState.QUIET_HEALTHY} and month-c.stable_since >= 4]
        count = sum(self.random.random() < self.config.referral_rate for _ in healthy)
        if healthy and month in {16, 25} and not count: count = 1
        # Referral is only a new LEAD; it receives no qualification privilege.
        for _ in range(count): self.leads.append(_Lead(self._next_lead, month, "referral")); self._next_lead += 1
        return count

    def simulate_churn(self, month: int) -> int:
        churn = 0
        for c in self.customers:
            if c.state is CustomerLifecycleState.SUPPORTED and month-c.stable_since > 5 and self.random.random() < self.config.support_monthly_churn_rate:
                c.state = CustomerLifecycleState.CHURNED; churn += 1
            elif c.state is CustomerLifecycleState.EXPANSION: c.state = CustomerLifecycleState.SUPPORTED
        if month == 33 and not churn:
            candidate = next((c for c in self.customers if c.state is CustomerLifecycleState.SUPPORTED), None)
            if candidate is not None: candidate.state = CustomerLifecycleState.CHURNED; churn = 1
        return churn

    def simulate_cash_flow(self, month: int, revenue: RevenueMix, support_cost: float, incident_cost: float) -> BusinessCashPosition:
        inflows = [CashEvent("support", CashEventType.SUPPORT_PAYMENT, revenue.support, 12)] if revenue.support else []
        for label, amount in self._cash_due.pop(month, []): inflows.append(CashEvent(label, CashEventType.PROJECT_FINAL_PAYMENT, amount, 24))
        for p in [p for p in self.projects if p.signed_month == month]:
            deposit=p.price*self.config.deposit_percentage; p.cash_received += deposit
            inflows.append(CashEvent(f"customer-{p.customer_id}", CashEventType.PROJECT_DEPOSIT, deposit, 20))
            self._cash_due.setdefault(month+self.config.project_duration_months+self.config.final_payment_delay_months, []).append((f"customer-{p.customer_id}", p.price-deposit))
        outflows = [CashEvent("operations", CashEventType.OVERHEAD, self.config.fixed_monthly_overhead, 1)]
        new = [p for p in self.projects if p.signed_month == month]
        if new: outflows.append(CashEvent("primary partner", CashEventType.PARTNER_DEPOSIT, sum(p.delivery_cost*.55 for p in new), 5))
        if support_cost: outflows.append(CashEvent("support partner", CashEventType.SUPPORT_PARTNER_COST, support_cost, 10))
        if incident_cost: outflows.append(CashEvent("incident partner", CashEventType.SUPPORT_PARTNER_COST, incident_cost, 8))
        flow = PortfolioCashFlow(f"M{month:02}", self.cash, tuple(inflows), tuple(outflows), committed_future_outflows=sum(p.delivery_cost*.45 for p in new), safe_buffer=self.config.reserve_target)
        self.cash = flow.ending_cash
        return BusinessCashPosition(flow, self.config.reserve_target)

    def build_month_snapshot(self) -> PortfolioSnapshot:
        return PortfolioSnapshot(len(self.customers), sum(p.state is ProjectStartState.SIGNED for p in self.projects),
            sum(p.state is ProjectStartState.QUEUED for p in self.projects),
            sum(p.state is ProjectStartState.START_AUTHORIZED and p.age < self.config.project_duration_months+p.delay_months for p in self.projects),
            sum(p.age >= self.config.project_duration_months+p.delay_months for p in self.projects),
            sum(c.state is CustomerLifecycleState.SUPPORTED for c in self.customers),
            sum(c.state is CustomerLifecycleState.QUIET_HEALTHY for c in self.customers),
            sum(c.state is CustomerLifecycleState.EXPANSION for c in self.customers),
            sum(c.state is CustomerLifecycleState.CHURNED for c in self.customers))

    def calculate_concentration(self) -> MonthlyConcentration:
        def share(values: list[float]) -> float:
            return max(values, default=0)/sum(values) if sum(values) else 0
        revenue=[c.revenue or next((p.price for p in self.projects if p.customer_id==c.customer_id),0) for c in self.customers]
        contribution=[next((p.contribution for p in self.projects if p.customer_id==c.customer_id),0) for c in self.customers]
        hours=[next((p.owner_hours for p in self.projects if p.customer_id==c.customer_id),0)+c.support_hours for c in self.customers]
        support=[self.config.routine_support_hours if c.state is CustomerLifecycleState.SUPPORTED else 0 for c in self.customers]
        active_cost=sum(p.delivery_cost for p in self.projects if p.state is ProjectStartState.START_AUTHORIZED)
        return MonthlyConcentration(share(revenue), share(contribution), share(hours), share(support), 0, 1.0 if active_cost else 0, 1.0 if len(support)>=2 and sum(v>0 for v in support)>=2 else 0)

    def _customer(self, customer_id: int) -> _Customer: return next(c for c in self.customers if c.customer_id == customer_id)


CustomerLifecycleSimulation = BusinessSimulation


def evaluate_pipeline(opportunities: int, slots: int, queued: int) -> PipelineState:
    if queued > slots: return PipelineState.EXCESSIVE_FOR_CAPACITY
    if opportunities < 2: return PipelineState.WEAK
    if opportunities <= slots*2: return PipelineState.ADEQUATE
    return PipelineState.STRONG


def evaluate_capacity(hours: OwnerHours, available_hours: float, sustainable_hours: float,
                      temporary_maximum_hours: float) -> OwnerWorkload:
    """Public capacity helper for focused tests and alternative future inputs."""
    return OwnerWorkload(hours, available_hours, sustainable_hours, temporary_maximum_hours)


def summarize_year(year: int, months: tuple[BusinessMonth, ...]) -> BusinessYear:
    if not months: raise ValueError("a year summary needs months")
    return BusinessYear(year, sum(m.leads for m in months), sum(m.qualified for m in months), sum(m.sales for m in months),
        sum(m.completed_projects for m in months), months[-1].portfolio.support_customers,
        sum(m.revenue.total for m in months), sum(m.contribution.total for m in months),
        min(m.cash.flow.minimum_cash_position for m in months), months[-1].cash.flow.ending_cash,
        sum(m.owner_hours for m in months), sum(m.incidents for m in months), sum(m.expansions for m in months),
        sum(m.churn for m in months), sum(m.capacity_state is CapacityState.OVER_CAPACITY for m in months), months[-1].pipeline_state)


def evaluate_health(months: tuple[BusinessMonth, ...]) -> Mapping[str, BusinessHealth]:
    overload=sum(m.capacity_state is CapacityState.OVER_CAPACITY for m in months)
    cash_bad=any(m.cash.flow.minimum_cash_position < 0 for m in months)
    queued=max(m.portfolio.queued_projects for m in months)
    return {"DEMAND": BusinessHealth.ACCEPTABLE if sum(m.leads for m in months)>=60 else BusinessHealth.WEAK,
        "SALES": BusinessHealth.ACCEPTABLE if sum(m.sales for m in months)>=6 else BusinessHealth.MIXED,
        "PROJECT_ECONOMICS": BusinessHealth.ACCEPTABLE if sum(m.contribution.project for m in months)>0 else BusinessHealth.WEAK,
        "DELIVERY": BusinessHealth.MIXED if queued else BusinessHealth.ACCEPTABLE,
        "SUPPORT": BusinessHealth.MIXED if months[-1].paid_support_hours>months[0].paid_support_hours else BusinessHealth.ACCEPTABLE,
        "CASH": BusinessHealth.WEAK if cash_bad else (BusinessHealth.MIXED if min(m.cash.flow.ending_cash for m in months)<months[0].cash.reserve_target else BusinessHealth.ACCEPTABLE),
        "OWNER_CAPACITY": BusinessHealth.WEAK if overload>2 else (BusinessHealth.MIXED if overload else BusinessHealth.ACCEPTABLE),
        "PIPELINE": BusinessHealth.MIXED if any(m.pipeline_state is PipelineState.WEAK for m in months[-6:]) else BusinessHealth.ACCEPTABLE,
        "CONCENTRATION": BusinessHealth.MIXED if max(m.concentration.revenue for m in months)>.5 else BusinessHealth.ACCEPTABLE,
        "PARTNER_RESILIENCE": BusinessHealth.WEAK if max(m.concentration.partner for m in months)>.8 else BusinessHealth.MIXED}


def identify_primary_bottleneck(months: tuple[BusinessMonth, ...], health: Mapping[str, BusinessHealth]) -> CapstoneFinding:
    if health["CASH"] is BusinessHealth.WEAK: return CapstoneFinding(Bottleneck.CASH, f"minimum simulated cash was ${min(m.cash.flow.minimum_cash_position for m in months):,.0f}")
    if max(m.portfolio.queued_projects for m in months): return CapstoneFinding(Bottleneck.PARTNER_CAPACITY, "single-partner cash/capacity start gates left signed projects queued")
    if health["OWNER_CAPACITY"] in {BusinessHealth.WEAK, BusinessHealth.MIXED}: return CapstoneFinding(Bottleneck.OWNER_CAPACITY, "finite owner hours caused overload or deferral")
    return CapstoneFinding(Bottleneck.DEMAND, "pipeline coverage is the current limiting condition")


def simulate(config: BusinessSimulationConfig = None) -> BusinessSimulationResult:
    return BusinessSimulation(config or BASELINE).run()


BASELINE = BusinessSimulationConfig()
