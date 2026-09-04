from dataclasses import replace

from local_works.capstone import *
from local_works.portfolio import CapacityState
from local_works.portfolio_simulation import OwnerHours, PipelineState


def test_baseline_is_36_months_repeatable_and_starts_empty():
    a, b = simulate(), simulate()
    assert len(a.months) == 36 and a == b
    assert a.months[0].portfolio.customers == 0


def test_sales_cycle_prevents_instant_close():
    result = simulate(replace(BASELINE, horizon_months=2, monthly_lead_volume=20, close_rate=1))
    assert result.months[0].sales == 0


def test_sales_capacity_constrains_progression_and_can_defer():
    result = simulate(replace(BASELINE, sustainable_owner_hours=20, temporary_maximum_hours=25,
                              monthly_lead_volume=20, opening_cash=50000))
    assert any(m.qualified < m.leads or m.owner_workload.deferred_sales for m in result.months)


def test_project_queue_and_concurrency_are_visible():
    result = simulate(replace(BASELINE, monthly_lead_volume=15, qualified_lead_rate=1,
                              discovery_progression_rate=1, proposal_rate=1, close_rate=1,
                              max_concurrent_projects=1))
    assert max(m.portfolio.queued_projects for m in result.months) > 0
    assert max(m.portfolio.active_projects for m in result.months) <= 1


def test_support_accumulates_and_warranty_is_distinct():
    rows = simulate().months
    assert rows[-1].paid_support_hours > rows[0].paid_support_hours
    assert any(m.warranty_hours >= 0 and m.warranty_hours != m.paid_support_hours for m in rows)


def test_incidents_consume_owner_capacity_and_vendor_event_correlates():
    rows = simulate().months
    assert any(m.incidents and m.owner_workload.hours.incidents > 0 for m in rows)
    assert rows[BASELINE.correlated_vendor_incident_month-1].correlated_vendor_incident


def test_expansion_referral_churn_and_quiet_health_are_possible():
    rows = simulate().months
    assert sum(m.expansions for m in rows) > 0
    assert sum(m.referral_leads for m in rows) > 0
    assert sum(m.churn for m in rows) > 0
    assert any(m.portfolio.quiet_customers > 0 for m in rows)
    # Referral counts are included as leads, not qualified automatically.
    assert all(m.qualified <= m.leads + 20 for m in rows)


def test_revenue_contribution_and_cash_are_distinct():
    result = simulate(); m = next(x for x in result.months if x.revenue.total)
    assert m.revenue.total != m.contribution.total
    assert m.contribution.total != m.cash.flow.net_cash_flow
    assert result.total_contribution > 0 and result.minimum_cash < 0
    assert result.working_capital_required and FailureReason.WORKING_CAPITAL_REQUIRED in result.failure_reasons


def test_capacity_can_overload_and_overload_defers_work():
    workload = evaluate_capacity(OwnerHours(admin=40), 20, 20, 30)
    assert workload.state is CapacityState.OVER_CAPACITY
    rows = simulate(replace(BASELINE, sustainable_owner_hours=28, temporary_maximum_hours=35,
                            monthly_lead_volume=12, opening_cash=50000)).months
    assert any(m.capacity_state is CapacityState.OVER_CAPACITY for m in rows)
    assert any(m.owner_workload.deferred_project_work > 0 for m in rows)


def test_delivery_heavy_pipeline_can_weaken():
    rows = simulate(replace(BASELINE, sustainable_owner_hours=35, monthly_lead_volume=2,
                            opening_cash=50000)).months
    assert any(m.pipeline_state is PipelineState.WEAK for m in rows)


def test_customer_partner_and_vendor_concentration_calculate():
    rows = simulate().months
    assert any(m.concentration.revenue > 0 for m in rows)
    assert any(m.concentration.partner == 1 for m in rows)
    assert any(m.concentration.vendor == 1 for m in rows)


def test_owner_absence_reduces_available_hours():
    rows = simulate().months
    absence = rows[BASELINE.absence_month-1]
    assert absence.owner_workload.available_hours == BASELINE.sustainable_owner_hours-BASELINE.absence_hours
    assert any("absence" in r.description for r in absence.risks)


def test_three_year_summaries_health_and_bottleneck():
    result = simulate()
    assert [y.year for y in result.years] == [1, 2, 3]
    assert all(y.revenue >= 0 and y.owner_hours > 0 for y in result.years)
    assert set(result.health) == {"DEMAND", "SALES", "PROJECT_ECONOMICS", "DELIVERY", "SUPPORT", "CASH", "OWNER_CAPACITY", "PIPELINE", "CONCENTRATION", "PARTNER_RESILIENCE"}
    assert result.primary_bottleneck.bottleneck is not Bottleneck.UNKNOWN


def test_part_a_boundaries_are_explicit_and_no_production_app_exists():
    result = simulate()
    assert not hasattr(result, "owner_income_target_verdict")
    assert not hasattr(result, "monte_carlo")
    assert not __import__("pathlib").Path("artisan").exists()
    text = open("book/32-owner-income-and-final-examination.md").read()
    assert "COMPLETE" in text and "Part A result itself does not calculate owner income" in text
