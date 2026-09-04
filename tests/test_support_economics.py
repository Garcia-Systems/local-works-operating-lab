"""Meaningful checks for Chapter 29's planning model."""
from local_works.support_economics import *


def case(name="normal", revenue=600, owner=2, partner=1, available=20,
         buffer=5, partner_available=True, after_hours=0):
    return SupportScenario(name, SupportUsage(owner, partner, .5, 1, after_hours), revenue,
        100, 50, 75, SupportCapacity(available, owner, buffer), partner_available,
        InterruptionRisk.HIGH if after_hours else InterruptionRisk.LOW)


def test_unknown_demand_is_preserved():
    profile = SupportDemandProfile()
    assert profile.requests_per_month == UNKNOWN
    assert profile.uncertainty == UNKNOWN


def test_request_mix_is_distinct_from_count():
    a = SupportDemandProfile(10, request_mix={SupportWorkCategory.HOW_TO: 10 / 12})
    b = SupportDemandProfile(10, request_mix={SupportWorkCategory.VENDOR_COORDINATION: 15})
    assert a.requests_per_month == b.requests_per_month
    assert a.request_mix != b.request_mix


def test_warranty_goodwill_and_paid_usage_remain_separate():
    usage = SupportUsage(2, 1, goodwill_owner_hours=.5, goodwill_partner_hours=.25,
                         warranty_owner_hours=3, warranty_partner_hours=2)
    assert usage.paid_support_owner_hours == 2
    assert usage.goodwill_owner_hours == .5
    assert usage.warranty_owner_hours == 3
    assert usage.partner_hours == 1


def test_vendor_coordination_and_owner_hours_are_visible():
    usage = SupportUsage(2, vendor_coordination_hours=1.25)
    assert (usage.owner_hours, usage.vendor_coordination_hours) == (2, 1.25)


def test_contribution_metrics():
    result = SupportContribution(600, 100, 50, 4, 75)
    assert result.contribution == 450
    assert result.margin == .75
    assert result.after_owner_time == 150
    assert result.contribution_per_owner_hour == 112.5


def test_ratios_handle_zero_safely():
    result = SupportContribution(0, 0, 0, 0, 75)
    assert result.margin is None
    assert result.contribution_per_owner_hour is None


def test_break_even_owner_and_partner_hours():
    result = SupportBreakEven(600, 150, 75, 100)
    assert result.owner_hours == 6
    assert result.partner_hours == 4.5


def test_incident_reserve_reduces_usable_capacity():
    assert SupportCapacity(20, 10, 5).usable_planned_capacity == 15


def test_capacity_can_be_strained_and_over():
    assert SupportCapacity(20, 17, 5).state is CapacityState.STRAINED
    assert SupportCapacity(20, 21, 5).state is CapacityState.OVER_CAPACITY


def test_after_hours_increases_risk_and_boundaries():
    result = case(after_hours=1)
    assert result.interruption_risk is InterruptionRisk.HIGH
    assert result.verdict() is SupportPlanVerdict.VIABLE_WITH_BOUNDARIES


def test_all_revenue_models_can_be_represented():
    models = {RevenueModel.PAY_AS_YOU_GO, RevenueModel.PREPAID_HOURS,
              RevenueModel.MONTHLY_FLAT_FEE, RevenueModel.HYBRID}
    assert {SupportRevenue(model, 1).model for model in models} == models


def test_unlimited_high_usage_can_fail_stress_test():
    unlimited = case("unlimited", revenue=199, owner=12, partner=4)
    assert unlimited.economics.after_owner_time < 0
    assert assess_plan([unlimited]) is SupportPlanVerdict.NOT_ECONOMICALLY_SENSIBLE


def test_high_usage_can_reverse_expected_profit():
    expected = case(owner=2, partner=.5)
    busy = case(owner=10, partner=2)
    assert expected.economics.after_owner_time > 0
    assert busy.economics.after_owner_time < 0


def test_partner_unavailability_changes_verdict():
    assert case(partner_available=False).verdict() is SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE


def test_double_demand_can_break_capacity():
    doubled = case(owner=22, available=20)
    assert doubled.capacity.state is CapacityState.OVER_CAPACITY
    assert doubled.verdict() is SupportPlanVerdict.NOT_OPERATIONALLY_SUSTAINABLE


def test_customer_value_is_not_margin():
    value = SupportCustomerValue(("known contact",), value_state="WEAK")
    margin = SupportContribution(1000, 0, 0, 0, 75)
    assert margin.contribution == 1000
    assert value.value_state == "WEAK"


def test_annual_simulation_aggregates_months():
    annual = aggregate_annual([case(), case(owner=4, partner=2)])
    assert annual.revenue == 1200
    assert annual.owner_hours == 6
    assert annual.incidents == 2
    assert annual.contribution == 800


def test_burden_concentration():
    concentration = burden_concentration({"Harbor": 6, "Other": 4})
    assert concentration == {"Harbor": .6, "Other": .4}
    assert burden_concentration({"Harbor": 0}) == {"Harbor": None}


def test_monthly_plan_can_be_not_economic():
    assert case(revenue=100, owner=4).verdict() is SupportPlanVerdict.NOT_ECONOMICALLY_SENSIBLE


def test_payg_can_win_comparison():
    assert compare_monthly_with_payg([case(revenue=100, owner=4)], [case(revenue=600)]) is SupportPlanVerdict.PAY_AS_YOU_GO_BETTER


def test_empty_evidence_stays_insufficient():
    assert assess_plan([]) is SupportPlanVerdict.INSUFFICIENT_EVIDENCE


def test_chapter_does_not_implement_deferred_systems():
    import local_works.support_economics as module
    names = {name.lower() for name in vars(module)}
    assert not ({"invoice", "subscriptionpayment", "retention", "churn", "expansionsale"} & names)
