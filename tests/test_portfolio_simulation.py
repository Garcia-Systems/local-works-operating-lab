from datetime import date

from local_works.portfolio import CapacityState
from local_works.portfolio_simulation import *


def test_twelve_periods_and_deterministic_baseline():
    first, second = simulate(BASELINE), simulate(BASELINE)
    assert len(first.periods) == 12 and first == second


def test_revenue_mix_and_pipeline_stay_separate():
    period = simulate(BASELINE).periods[0]
    assert period.revenue.total == period.revenue.project + period.revenue.support + period.revenue.expansion
    assert period.leads and period.revenue.total != period.revenue.total + BASELINE.leads[0]


def test_contribution_is_not_revenue_or_cash():
    period = simulate(BASELINE).periods[0]
    assert period.contribution.total != period.revenue.total
    assert period.contribution.total != period.cash_flow.net_cash_flow


def test_positive_contribution_can_coexist_with_negative_cash():
    result = simulate(STRESS)
    period = next(p for p in result.periods if p.cash_flow.minimum_cash_position < 0)
    assert period.contribution.total > 0 and period.cash_flow.cash_state is CashState.NEGATIVE


def test_receivable_becomes_late_and_lateness_increases_exposure():
    ar = AccountReceivable("Fictional", 9000, date(2026, 1, 1))
    assert ar.update(date(2026, 1, 8)) is ReceivableStatus.LATE and ar.days_late(date(2026, 1, 8)) == 7
    late = PortfolioCashFlow("x", 10000, accounts_receivable=(ar,))
    normal = PortfolioCashFlow("x", 10000)
    assert late.maximum_cash_exposure > normal.maximum_cash_exposure


def test_partner_payment_timing_changes_minimum_cash_and_exposure():
    receipt = CashEvent("customer", CashEventType.PROJECT_DEPOSIT, 5000, 20)
    early = CashEvent("partner", CashEventType.PARTNER_DEPOSIT, 4000, 2)
    late = CashEvent("partner", CashEventType.PARTNER_DEPOSIT, 4000, 25)
    a = PortfolioCashFlow("a", 6000, (receipt,), (early,))
    b = PortfolioCashFlow("b", 6000, (receipt,), (late,))
    assert a.minimum_cash_position < b.minimum_cash_position and a.maximum_cash_exposure > b.maximum_cash_exposure


def test_maximum_cash_exposure_is_peak_prefunding():
    cash = PortfolioCashFlow("x", 5000, (CashEvent("c", CashEventType.PROJECT_DEPOSIT, 6000, 20),),
                             (CashEvent("p", CashEventType.PARTNER_DEPOSIT, 7000, 2),))
    assert cash.maximum_cash_exposure == 7000 and cash.minimum_cash_position == -2000


def test_start_can_queue_for_each_constraint():
    common = dict(owner_hours_needed=5, owner_hours_available=10, partner_hours_needed=5,
                  partner_hours_available=10, required_cash=2, cash_above_buffer=10)
    assert gate_project_start(**(common | {"required_cash": 20}))[1] == "cash constraint"
    assert gate_project_start(**(common | {"owner_hours_needed": 20}))[1] == "owner capacity"
    assert gate_project_start(**(common | {"partner_hours_needed": 20}))[1] == "partner capacity"


def test_support_load_accumulates_after_completions():
    periods = simulate(BASELINE).periods
    assert periods[-1].support_customers > periods[0].support_customers
    assert periods[-1].owner_hours.support > periods[0].owner_hours.support


def test_sales_reduction_produces_growth_pipeline_cliff():
    periods = simulate(GROWTH).periods
    assert periods[0].leads > periods[-1].leads and periods[-1].pipeline_state is PipelineState.WEAK


def test_high_demand_creates_queue_and_overload():
    result = simulate(GROWTH)
    assert max(p.queued_projects for p in result.periods) > 0 and result.overload_months > 0


def test_incident_collision_consumes_reserve_and_correlates():
    period = simulate(STRESS).periods[2]
    assert period.open_incidents == 2 and period.owner_hours.incidents > period.incident_reserve_hours
    assert any("correlated MemberCloud" in risk for risk in period.risks)


def test_customer_concentration_changes_and_dimensions_differ():
    periods = simulate(BASELINE).periods
    assert len({p.concentration.revenue for p in periods}) > 1
    assert any(p.concentration.owner_hours != p.concentration.revenue for p in periods)
    assert any(p.concentration.receivables != p.concentration.revenue for p in periods)


def test_owner_absence_affects_multiple_categories():
    risks = simulate(STRESS).periods[6].risks
    assert sum("owner absent" in r or "support triage" in r or "sales follow-up" in r or "customer communication" in r for r in risks) == 4


def test_scenario_verdicts_are_evidence_backed():
    assert simulate(BASELINE).verdict is PortfolioVerdict.HEALTHY
    assert simulate(GROWTH).verdict is PortfolioVerdict.CAPACITY_LIMITED
    assert simulate(CONSERVATIVE).verdict is PortfolioVerdict.PIPELINE_WEAK
    assert simulate(STRESS).verdict in {PortfolioVerdict.CASH_CONSTRAINED, PortfolioVerdict.FRAGILE}


def test_profitable_standalone_deal_is_deferred_by_portfolio():
    standalone, decision, lesson = marginal_deal_test()
    assert standalone == "PROMISING" and decision is StartDecision.QUEUE and "RIGHT NOW" in lesson


def test_support_overload_deal_is_not_silently_accepted():
    assert support_overload_deal_test() is StartDecision.DEFER_START


def test_reviews_can_be_generated():
    period = simulate(STRESS).periods[6]
    assert "WEEKLY OPERATING REVIEW" in weekly_review(period, stress=True)
    assert "MONTHLY BUSINESS REVIEW" in monthly_review(period)


def test_chapter_boundary_is_explicit_in_book():
    text = open("book/31-the-local-works-customer-portfolio.md").read().lower()
    assert "final owner-income" in text and "does not" in text
    assert "hire" in text and "database/api/site" in text
