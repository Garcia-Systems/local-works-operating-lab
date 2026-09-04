from datetime import date

from local_works.portfolio import *
from scripts.run_chapter_31a import build_portfolio


def test_multiple_lifecycle_states_coexist():
    assert len({c.lifecycle_stage for c in build_portfolio().customers}) >= 5


def test_inventory_combines_sales_project_support_and_incident_work():
    p = build_portfolio(); categories = {w.category for w in p.work_items}
    assert {WorkCategory.DISCOVERY, WorkCategory.QA, WorkCategory.SUPPORT, WorkCategory.INCIDENT} <= categories


def test_critical_incident_outranks_large_customer_routine_work():
    assert build_portfolio().prioritized_work()[0].work_id == "HF-INC"
    assert WorkPriority.assess(incident_severity="SEVERE") is WorkPriority.CRITICAL


def test_owner_total_differs_from_delivery_capacity():
    c = build_portfolio().owner_capacity
    assert c.total_working_hours != c.customer_delivery_hours


def test_incident_reserve_reduces_schedulable_capacity():
    c = OwnerCapacity(40, {}, 5, 0)
    assert c.schedulable_hours == 35


def test_context_switching_overhead_is_represented():
    c = OwnerCapacity(40, {}, 5, 3)
    assert c.schedulable_hours == 32 and c.context_switch_hours == 3


def test_delivery_capacity_can_be_constrained():
    assert build_portfolio().delivery_capacity.constrained


def test_support_capacity_can_be_overloaded():
    assert build_portfolio().support_capacity.overloaded


def test_pipeline_is_distinct_from_booked_revenue():
    p = build_portfolio()
    assert p.potential_revenue == p.pipeline.potential_revenue and p.potential_revenue != p.booked_revenue


def test_two_project_starts_create_conflict():
    p = build_portfolio(); starts = [w for w in p.work_items if w.work_id in {"THS-QA", "ODD-START"}]
    assert capacity_conflict("starts", starts, 10, (PortfolioDecision.DELAY_KICKOFF,), "one slot").exists


def test_signed_work_can_remain_queued():
    customer = next(c for c in build_portfolio().customers if c.name == "Old Dominion Dental")
    assert customer.lifecycle_stage is LifecycleStage.SIGNED
    assert customer.project_start_state is ProjectStartState.QUEUED and not customer.start_authorized


def test_profitable_deal_can_be_deferred_for_portfolio_reasons():
    customer = next(c for c in build_portfolio().customers if c.name == "Old Dominion Dental")
    decision = PortfolioDecision.DELAY_KICKOFF
    assert customer.contribution > 0 and decision is PortfolioDecision.DELAY_KICKOFF


def test_revenue_concentration_differs_from_owner_hour_concentration():
    c = build_portfolio().concentration()
    assert c.largest_share(c.revenue) != c.largest_share(c.owner_hours)


def test_support_concentration_differs_from_revenue_concentration():
    c = build_portfolio().concentration()
    assert c.largest_share(c.support_burden) != c.largest_share(c.revenue)


def test_partner_concentration_is_represented():
    assert build_portfolio().concentration().partners["Blue Heron"] == 3


def test_vendor_concentration_creates_correlated_risk():
    assert "MemberCloud" in build_portfolio().concentration().vendor_correlated_risks


def test_owner_absence_creates_continuity_risk():
    assert build_portfolio().owner_absence(3) in {ResilienceResult.SERIOUS_RISK, ResilienceResult.BUSINESS_STOPS}
