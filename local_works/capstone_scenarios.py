"""Chapter 32B owner economics and scenario analysis built on the 32A engine.

All values are fictional simulation outputs.  Frequencies produced here describe
the configured draws, not real-world probabilities, and no final verdict is made.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum, auto
import math
import random
import statistics

from local_works.capstone import BASELINE, BusinessSimulationConfig, BusinessSimulationResult, simulate
from local_works.portfolio import CapacityState


class OwnerCompensationPolicy(Enum):
    NO_DRAW = auto(); FIXED_DRAW = auto(); VARIABLE_DRAW = auto()
    RESERVE_FIRST = auto(); PERCENT_OF_AVAILABLE_CASH = auto()


class ReserveState(Enum):
    BELOW_MINIMUM = auto(); MINIMUM_ONLY = auto(); HEALTHY = auto(); ABOVE_TARGET = auto(); UNKNOWN = auto()


class OwnerIncomeTargetState(Enum):
    ACHIEVED = auto(); ACHIEVED_BUT_UNSTABLE = auto(); ACHIEVED_WITH_OVERLOAD = auto()
    ACHIEVED_BUT_CASH_FRAGILE = auto(); NOT_ACHIEVED = auto(); NOT_CASH_SUPPORTED = auto(); UNKNOWN = auto()


class IncomeStabilityState(Enum):
    STABLE = auto(); SOMEWHAT_VARIABLE = auto(); VOLATILE = auto(); VERY_VOLATILE = auto(); UNKNOWN = auto()


class ScenarioBottleneck(Enum):
    DEMAND = auto(); SALES = auto(); ECONOMICS = auto(); DELIVERY = auto(); SUPPORT = auto()
    CASH = auto(); OWNER_CAPACITY = auto(); PARTNER_CAPACITY = auto(); CONCENTRATION = auto(); OTHER = auto(); UNKNOWN = auto()


class BusinessFailureFlag(Enum):
    LOW_DEMAND = auto(); LOW_CONVERSION = auto(); LOW_PROJECT_CONTRIBUTION = auto()
    DELIVERY_OVERLOAD = auto(); SUPPORT_OVERLOAD = auto(); INCIDENT_OVERLOAD = auto()
    CASH_FAILURE = auto(); WORKING_CAPITAL_REQUIRED = auto(); CUSTOMER_CONCENTRATION = auto()
    PARTNER_DEPENDENCY = auto(); OWNER_OVERLOAD = auto(); PIPELINE_COLLAPSE = auto(); OTHER = auto()


class BusinessDesignLever(Enum):
    RAISE_PRICE = auto(); REDUCE_OWNER_DELIVERY_HOURS = auto(); IMPROVE_QUALIFICATION = auto()
    INCREASE_QUALIFIED_LEADS = auto(); REDUCE_SUPPORT_SCOPE = auto(); RAISE_SUPPORT_PRICE = auto()
    INCREASE_DEPOSIT = auto(); CHANGE_PAYMENT_TIMING = auto(); LIMIT_CONCURRENT_PROJECTS = auto()
    USE_ALTERNATE_PARTNER = auto(); DIVERSIFY_CUSTOMERS = auto(); DIVERSIFY_PARTNERS = auto()
    PREFER_CONFIGURATION = auto(); REFER_OUT_BAD_FIT = auto(); PROTECT_SALES_TIME = auto(); OTHER = auto()


@dataclass(frozen=True)
class BusinessReserve:
    minimum_operating_reserve: float
    target_reserve: float
    current_cash: float
    committed_partner_payments: float = 0
    expected_near_term_outflows: float = 0

    @property
    def available_for_owner(self) -> float:
        return max(0.0, self.current_cash-self.minimum_operating_reserve-self.committed_partner_payments-self.expected_near_term_outflows)

    @property
    def reserve_state(self) -> ReserveState:
        if self.current_cash < self.minimum_operating_reserve: return ReserveState.BELOW_MINIMUM
        if self.current_cash == self.minimum_operating_reserve: return ReserveState.MINIMUM_ONLY
        if self.current_cash >= self.target_reserve: return ReserveState.ABOVE_TARGET
        return ReserveState.HEALTHY


@dataclass(frozen=True)
class OwnerIncomeTarget:
    annual_amount: float


@dataclass(frozen=True)
class OwnerIncomeTargetResult:
    target: OwnerIncomeTarget; year: int; actual_draw: float
    state: OwnerIncomeTargetState; reason: str


@dataclass(frozen=True)
class OwnerIncomeStability:
    monthly_draws: tuple[float, ...]; months_with_zero_draw: int; months_below_target: int
    minimum_draw: float; maximum_draw: float; standard_deviation: float
    coefficient_of_variation: float | None; state: IncomeStabilityState


@dataclass(frozen=True)
class OwnerIncomeYear:
    year: int; business_revenue: float; business_contribution: float; owner_draw: float
    owner_hours: float; owner_draw_per_hour: float; contribution_per_hour: float
    minimum_cash: float; ending_cash: float; overload_months: int


@dataclass(frozen=True)
class OwnerIncomeResult:
    simulation: BusinessSimulationResult; policy: OwnerCompensationPolicy
    reserve_minimum: float; monthly_draws: tuple[float, ...]; monthly_post_draw_cash: tuple[float, ...]
    years: tuple[OwnerIncomeYear, ...]; stability: OwnerIncomeStability


@dataclass(frozen=True)
class ScenarioComparison:
    scenario: str; revenue_36_months: float; contribution_36_months: float
    yearly_owner_draws: tuple[float, ...]; ending_cash: float; minimum_cash: float; funding_required: float
    average_owner_hours_week: float; peak_owner_hours_week: float; overload_months: int
    customers_acquired: int; projects_completed: int; support_customers: int; incidents: int
    largest_customer_concentration: float; largest_partner_concentration: float
    primary_bottleneck: ScenarioBottleneck; target_status: OwnerIncomeTargetState
    failure_flags: tuple[BusinessFailureFlag, ...]


@dataclass(frozen=True)
class BreakEvenResult:
    annual_target: float; qualified_leads_per_month: float; sales_per_year: float
    project_contribution: float; maximum_owner_hours_per_project: float
    maximum_support_hours_per_customer_month: float; minimum_opening_cash: float
    assumptions: tuple[str, ...]


@dataclass(frozen=True)
class SensitivityResult:
    assumption: str; low_value: float; base_value: float; high_value: float
    low_year3_draw: float; base_year3_draw: float; high_year3_draw: float
    low_contribution: float; high_contribution: float; low_minimum_cash: float; high_minimum_cash: float
    low_average_hours_week: float; high_average_hours_week: float; low_overload_months: int; high_overload_months: int

    @property
    def absolute_impact(self) -> float: return abs(self.high_year3_draw-self.low_year3_draw)


@dataclass(frozen=True)
class MonteCarloResult:
    runs: int; seed: int; selected_target: float; p10_year3_draw: float; p50_year3_draw: float; p90_year3_draw: float
    cash_nonnegative_frequency: float; target_achieved_frequency: float; overload_frequency: float
    working_capital_frequency: float; concentration_frequency: float
    interpretation: str = "SIMULATION FREQUENCIES UNDER ASSUMPTIONS; not real-world probabilities."


@dataclass(frozen=True)
class OperatingModelResult:
    model: str; comparison: ScenarioComparison


@dataclass(frozen=True)
class LeverTestResult:
    lever: BusinessDesignLever; before: ScenarioComparison; after: ScenarioComparison
    changed_assumptions: tuple[str, ...]; unchanged_assumptions: tuple[str, ...]


class OwnerIncomeModel:
    """Apply draws after the unchanged 32A run, retaining a separate cash ledger."""
    def __init__(self, policy: OwnerCompensationPolicy = OwnerCompensationPolicy.RESERVE_FIRST,
                 minimum_reserve: float | None = None, draw_fraction: float = .50,
                 fixed_monthly_draw: float = 0, monthly_draw_cap: float = 10_000) -> None:
        self.policy, self.minimum_reserve = policy, minimum_reserve
        self.draw_fraction, self.fixed_monthly_draw, self.monthly_draw_cap = draw_fraction, fixed_monthly_draw, monthly_draw_cap

    def calculate(self, result: BusinessSimulationResult, config: BusinessSimulationConfig = BASELINE,
                  monthly_target: float = 75_000/12) -> OwnerIncomeResult:
        minimum = config.reserve_target if self.minimum_reserve is None else self.minimum_reserve
        cash = config.opening_cash; draws: list[float] = []; balances: list[float] = []
        previous_engine_cash = config.opening_cash
        for month in result.months:
            cash += month.cash.flow.ending_cash-previous_engine_cash
            previous_engine_cash = month.cash.flow.ending_cash
            reserve = BusinessReserve(minimum, config.reserve_target, cash,
                                      expected_near_term_outflows=config.fixed_monthly_overhead)
            available = reserve.available_for_owner
            if self.policy is OwnerCompensationPolicy.NO_DRAW: draw = 0.0
            elif self.policy is OwnerCompensationPolicy.FIXED_DRAW: draw = min(available, self.fixed_monthly_draw)
            elif self.policy is OwnerCompensationPolicy.PERCENT_OF_AVAILABLE_CASH: draw = available*self.draw_fraction
            else: draw = min(self.monthly_draw_cap, available*self.draw_fraction)
            cash -= draw; draws.append(round(draw, 2)); balances.append(round(cash, 2))
        years = []
        for index, source in enumerate(result.years):
            sl = slice(index*12, min((index+1)*12, len(draws))); draw = sum(draws[sl]); hours = source.owner_hours
            years.append(OwnerIncomeYear(source.year, source.revenue, source.contribution, draw, hours,
                draw/hours if hours else 0, source.contribution/hours if hours else 0,
                min(balances[sl]), balances[sl][-1], source.overload_months))
        below = sum(x < monthly_target for x in draws); zero = sum(x == 0 for x in draws)
        mean = statistics.fmean(draws) if draws else 0; sd = statistics.pstdev(draws) if len(draws)>1 else 0
        cv = sd/mean if mean else None
        state = (IncomeStabilityState.UNKNOWN if not draws else IncomeStabilityState.STABLE if cv is not None and cv <= .25
                 else IncomeStabilityState.SOMEWHAT_VARIABLE if cv is not None and cv <= .5
                 else IncomeStabilityState.VOLATILE if cv is not None and cv <= 1 else IncomeStabilityState.VERY_VOLATILE)
        stability = OwnerIncomeStability(tuple(draws), zero, below, min(draws, default=0), max(draws, default=0), sd, cv, state)
        return OwnerIncomeResult(result, self.policy, minimum, tuple(draws), tuple(balances), tuple(years), stability)


SCENARIOS: dict[str, BusinessSimulationConfig] = {
    "BASELINE": BASELINE,
    "CONSERVATIVE": replace(BASELINE, name="CONSERVATIVE", monthly_lead_volume=4, qualified_lead_rate=.40, close_rate=.34, sales_cycle_delay_months=3, delivery_cost=7800, routine_support_hours=3.0, final_payment_delay_months=2),
    "OPTIMISTIC": replace(BASELINE, name="OPTIMISTIC", monthly_lead_volume=6, qualified_lead_rate=.55, close_rate=.48, referral_rate=.07, project_delay_rate=.07, incident_rate=.035, expansion_signal_rate=.07),
    "STRESS": replace(BASELINE, name="STRESS", monthly_lead_volume=3.5, close_rate=.3, delivery_cost=8500, routine_support_hours=4.2, incident_rate=.12, final_payment_delay_months=3, partner_capacity_hours=65, opening_cash=9000, absence_hours=40),
    "RAPID_GROWTH": replace(BASELINE, name="RAPID_GROWTH", monthly_lead_volume=10, qualified_lead_rate=.62, close_rate=.55, referral_rate=.09),
    "LOW_DEMAND": replace(BASELINE, name="LOW_DEMAND", monthly_lead_volume=2.0),
    "LOW_PRICE": replace(BASELINE, name="LOW_PRICE", average_project_price=11250),
    "HIGH_SUPPORT_BURDEN": replace(BASELINE, name="HIGH_SUPPORT_BURDEN", support_adoption_rate=.9, routine_support_hours=6.5, incident_rate=.09),
    "CASH_STRESS": replace(BASELINE, name="CASH_STRESS", opening_cash=3500, deposit_percentage=.25, final_payment_delay_months=4, delivery_cost=7800),
    "PARTNER_FAILURE": replace(BASELINE, name="PARTNER_FAILURE", partner_capacity_hours=45, project_delay_rate=.28),
    "CUSTOMER_CONCENTRATION": replace(BASELINE, name="CUSTOMER_CONCENTRATION", monthly_lead_volume=2.6, average_project_price=23000, project_price_variability=.35),
    "OWNER_ABSENCE": replace(BASELINE, name="OWNER_ABSENCE", absence_hours=80),
}


def target_result(income: OwnerIncomeResult, target: OwnerIncomeTarget, year: int = 3) -> OwnerIncomeTargetResult:
    if year > len(income.years): return OwnerIncomeTargetResult(target, year, 0, OwnerIncomeTargetState.UNKNOWN, "year not simulated")
    row = income.years[year-1]
    if row.owner_draw < target.annual_amount:
        state = OwnerIncomeTargetState.NOT_CASH_SUPPORTED if row.business_contribution >= target.annual_amount and row.minimum_cash < income.reserve_minimum else OwnerIncomeTargetState.NOT_ACHIEVED
        return OwnerIncomeTargetResult(target, year, row.owner_draw, state, "draw is below target" if state is OwnerIncomeTargetState.NOT_ACHIEVED else "contribution exists but reserve/cash does not support the draw")
    if row.overload_months: state, reason = OwnerIncomeTargetState.ACHIEVED_WITH_OVERLOAD, "target met during owner overload"
    elif income.stability.months_with_zero_draw or income.stability.state in {IncomeStabilityState.VOLATILE, IncomeStabilityState.VERY_VOLATILE}: state, reason = OwnerIncomeTargetState.ACHIEVED_BUT_UNSTABLE, "target met but monthly draws are interrupted or volatile"
    elif row.minimum_cash < income.reserve_minimum: state, reason = OwnerIncomeTargetState.ACHIEVED_BUT_CASH_FRAGILE, "target met without consistently preserving reserve"
    else: state, reason = OwnerIncomeTargetState.ACHIEVED, "target and reserve conditions met"
    return OwnerIncomeTargetResult(target, year, row.owner_draw, state, reason)


def _bottleneck(name: str, result: BusinessSimulationResult, config: BusinessSimulationConfig) -> ScenarioBottleneck:
    if name == "LOW_DEMAND" or sum(y.sales for y in result.years) < 10: return ScenarioBottleneck.DEMAND
    if name == "LOW_PRICE": return ScenarioBottleneck.ECONOMICS
    if name == "HIGH_SUPPORT_BURDEN": return ScenarioBottleneck.SUPPORT
    if name in {"CASH_STRESS", "STRESS"} and result.minimum_cash < 0: return ScenarioBottleneck.CASH
    if name == "PARTNER_FAILURE": return ScenarioBottleneck.PARTNER_CAPACITY
    if name == "CUSTOMER_CONCENTRATION": return ScenarioBottleneck.CONCENTRATION
    if result.overload_months: return ScenarioBottleneck.OWNER_CAPACITY
    if result.minimum_cash < 0: return ScenarioBottleneck.CASH
    if result.months[-1].portfolio.queued_projects: return ScenarioBottleneck.DELIVERY
    return ScenarioBottleneck.DEMAND


def compare_scenario(config: BusinessSimulationConfig, target: float = 75_000) -> ScenarioComparison:
    result = simulate(config); income = OwnerIncomeModel().calculate(result, config, target/12)
    bottleneck = _bottleneck(config.name, result, config); flags: list[BusinessFailureFlag] = []
    if bottleneck is ScenarioBottleneck.DEMAND: flags.append(BusinessFailureFlag.LOW_DEMAND)
    if bottleneck is ScenarioBottleneck.ECONOMICS: flags.append(BusinessFailureFlag.LOW_PROJECT_CONTRIBUTION)
    if bottleneck is ScenarioBottleneck.SUPPORT: flags.append(BusinessFailureFlag.SUPPORT_OVERLOAD)
    if result.minimum_cash < 0: flags.extend((BusinessFailureFlag.CASH_FAILURE, BusinessFailureFlag.WORKING_CAPITAL_REQUIRED))
    if result.overload_months: flags.append(BusinessFailureFlag.OWNER_OVERLOAD)
    peak_customer = max((m.concentration.revenue for m in result.months), default=0)
    if peak_customer > .5: flags.append(BusinessFailureFlag.CUSTOMER_CONCENTRATION)
    if max((m.concentration.partner for m in result.months), default=0) > .75: flags.append(BusinessFailureFlag.PARTNER_DEPENDENCY)
    return ScenarioComparison(config.name, result.total_revenue, result.total_contribution,
        tuple(y.owner_draw for y in income.years), income.monthly_post_draw_cash[-1], min(income.monthly_post_draw_cash),
        max(0, -min(income.monthly_post_draw_cash)), result.owner_hours/36/4.33,
        max(m.owner_hours for m in result.months)/4.33, result.overload_months,
        result.months[-1].portfolio.customers, sum(m.completed_projects for m in result.months),
        result.months[-1].portfolio.support_customers, sum(m.incidents for m in result.months), peak_customer,
        max((m.concentration.partner for m in result.months), default=0), bottleneck,
        target_result(income, OwnerIncomeTarget(target)).state, tuple(dict.fromkeys(flags)))


def scenario_suite(target: float = 75_000) -> tuple[ScenarioComparison, ...]:
    return tuple(compare_scenario(config, target) for config in SCENARIOS.values())


def break_even(target: float = 75_000, config: BusinessSimulationConfig = BASELINE) -> BreakEvenResult:
    contribution = config.average_project_price-config.delivery_cost-config.other_direct_cost
    sales = (target+12*config.fixed_monthly_overhead)/max(1, contribution)
    funnel_close = config.discovery_progression_rate*config.proposal_rate*config.close_rate
    qualified = sales/12/max(.0001, funnel_close)
    expected_sales = max(1, config.monthly_lead_volume*12*config.qualified_lead_rate*funnel_close)
    required_contribution = (target+12*config.fixed_monthly_overhead)/expected_sales
    max_hours = contribution/max(1, config.owner_time_value)
    support_margin = max(0, config.monthly_support_revenue-config.partner_support_cost)
    max_support = support_margin/max(1, config.owner_time_value)
    probe = simulate(config); opening = config.opening_cash+max(0, -probe.minimum_cash)
    return BreakEvenResult(target, qualified, sales, required_contribution, max_hours, max_support, opening,
        ("current funnel rates", "project contribution funds target plus fixed overhead", "owner-time threshold uses configured owner time value", "cash estimate holds modeled timing constant"))


SENSITIVITY_RANGES = {
    "monthly_lead_volume": (.8, 1.2), "qualified_lead_rate": (.8, 1.2), "close_rate": (.8, 1.2),
    "average_project_price": (.85, 1.15), "delivery_cost": (1.15, .85), "owner_project_hours": (1.2, .8),
    "routine_support_hours": (1.25, .75), "monthly_support_revenue": (.8, 1.2),
    "incident_rate": (1.5, .5), "final_payment_delay_months": (2, .5), "expansion_signal_rate": (.6, 1.4),
}


def sensitivity_analysis(config: BusinessSimulationConfig = BASELINE) -> tuple[SensitivityResult, ...]:
    base = compare_scenario(config)
    rows = []
    for name, (low_factor, high_factor) in SENSITIVITY_RANGES.items():
        value = getattr(config, name)
        low_value = max(1, round(value*low_factor)) if isinstance(value, int) else value*low_factor
        high_value = max(1, round(value*high_factor)) if isinstance(value, int) else value*high_factor
        low = compare_scenario(replace(config, name=f"SENS_{name}_LOW", **{name: low_value}))
        high = compare_scenario(replace(config, name=f"SENS_{name}_HIGH", **{name: high_value}))
        rows.append(SensitivityResult(name, low_value, value, high_value, low.yearly_owner_draws[2], base.yearly_owner_draws[2], high.yearly_owner_draws[2],
            low.contribution_36_months, high.contribution_36_months, low.minimum_cash, high.minimum_cash,
            low.average_owner_hours_week, high.average_owner_hours_week, low.overload_months, high.overload_months))
    return tuple(rows)


def ranked_sensitivities(config: BusinessSimulationConfig = BASELINE) -> tuple[SensitivityResult, ...]:
    return tuple(sorted(sensitivity_analysis(config), key=lambda row: (-row.absolute_impact, row.assumption)))


def percentile(values: list[float], proportion: float) -> float:
    if not values: return 0
    ordered = sorted(values); position = (len(ordered)-1)*proportion; lower = math.floor(position); upper = math.ceil(position)
    return ordered[lower] if lower == upper else ordered[lower]+(ordered[upper]-ordered[lower])*(position-lower)


def monte_carlo(runs: int = 500, seed: int = 3202, target: float = 75_000) -> MonteCarloResult:
    if runs <= 0: raise ValueError("runs must be positive")
    rng = random.Random(seed); draws=[]; cash=target_hits=overload=working=concentrated=0
    for index in range(runs):
        config = replace(BASELINE, name=f"MONTE_CARLO_{index}", seed=rng.randrange(1_000_000),
            monthly_lead_volume=rng.uniform(4, 6), qualified_lead_rate=rng.uniform(.4, .56), close_rate=rng.uniform(.34, .5),
            average_project_price=rng.uniform(13_000, 17_000), delivery_cost=rng.uniform(6500, 8200),
            final_payment_delay_months=rng.choice((1, 1, 2, 3)), routine_support_hours=rng.uniform(2, 3.5),
            incident_rate=rng.uniform(.035, .09))
        row=compare_scenario(config, target); draw=row.yearly_owner_draws[2]; draws.append(draw)
        cash += row.minimum_cash >= 0; target_hits += draw >= target; overload += row.overload_months > 0
        working += row.funding_required > 0; concentrated += row.largest_customer_concentration > .5
    return MonteCarloResult(runs, seed, target, percentile(draws,.1), percentile(draws,.5), percentile(draws,.9),
        cash/runs, target_hits/runs, overload/runs, working/runs, concentrated/runs)


def operating_models() -> tuple[OperatingModelResult, ...]:
    configs = (
        replace(BASELINE,name="PROJECT_ONLY",support_adoption_rate=0,monthly_support_revenue=0,routine_support_hours=0),
        replace(BASELINE,name="PROJECT_PLUS_PAY_AS_YOU_GO",support_adoption_rate=.3,monthly_support_revenue=300,routine_support_hours=1.2),
        replace(BASELINE,name="PROJECT_PLUS_LIGHT_SUPPORT",support_adoption_rate=.55,monthly_support_revenue=500,routine_support_hours=2),
        replace(BASELINE,name="PROJECT_PLUS_MANAGED_SUPPORT",support_adoption_rate=.9,monthly_support_revenue=1100,routine_support_hours=5,incident_rate=.085),
        replace(BASELINE,name="MIXED_RELATIONSHIP_MODEL"),
    )
    return tuple(OperatingModelResult(c.name, compare_scenario(c)) for c in configs)


def capacity_mode_plausibility() -> dict[str, str]:
    output={}
    for name,hours in (("SIDE_BUSINESS",45),("PART_TIME",85),("FULL_TIME",128)):
        row=compare_scenario(replace(BASELINE,name=name,sustainable_owner_hours=hours,temporary_maximum_hours=hours*1.15))
        output[name] = "NOT_PLAUSIBLE" if row.overload_months > 6 else "PLAUSIBLE_WITH_LIMITS" if row.overload_months or row.funding_required else "PLAUSIBLE"
    return output


def lever_test() -> LeverTestResult:
    before_config=SCENARIOS["LOW_PRICE"]
    after_config=replace(before_config,name="LOW_PRICE_AFTER_LEVER",average_project_price=before_config.average_project_price*1.15)
    return LeverTestResult(BusinessDesignLever.RAISE_PRICE,compare_scenario(before_config),compare_scenario(after_config),
        ("average_project_price: +15%",),("lead volume", "conversion", "delivery cost", "support scope", "capacity"))


def bottleneck_evolution(config: BusinessSimulationConfig) -> tuple[tuple[str, ScenarioBottleneck], ...]:
    result=simulate(config); periods=(("Months 1-8",result.months[:8]),("Months 9-20",result.months[8:20]),("Months 21-36",result.months[20:]))
    rows=[]
    for label, months in periods:
        if min(m.cash.flow.minimum_cash_position for m in months)<0: b=ScenarioBottleneck.CASH
        elif sum(m.owner_workload.state is CapacityState.OVER_CAPACITY for m in months): b=ScenarioBottleneck.OWNER_CAPACITY
        elif max(m.portfolio.queued_projects for m in months)>config.max_concurrent_projects: b=ScenarioBottleneck.DELIVERY
        elif sum(m.paid_support_hours for m in months)/len(months)>config.support_reserve_hours*.7: b=ScenarioBottleneck.SUPPORT
        else: b=ScenarioBottleneck.DEMAND
        rows.append((label,b))
    return tuple(rows)
