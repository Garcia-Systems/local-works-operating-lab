"""Behavior tests for Chapter 15's internal pricing decision model."""
import pytest

from local_works.pricing import (
    ContributionAnalysis, CustomerEconomicsView, LocalWorksEconomicsView,
    PaymentEvent, PaymentStructure, PaymentTiming, PriceScenario, PricingEstimate,
    PricingModel, PricingWindow, PricingDecision, customer_ceiling_for_payback,
    discount_sensitivity,
)


def views(price: float = 5_000):
    customer = CustomerEconomicsView(20_000, 8_000, 2_000, price)
    local = LocalWorksEconomicsView(2_000, 300, 20, 75, 500)
    return customer, local


def test_customer_price_value_and_delivery_cost_remain_distinct():
    customer, local = views()
    assert customer.customer_price == 5_000
    assert customer.recoverable_annual_value == 8_000
    assert customer.current_annual_burden == 20_000
    assert local.delivery_partner_cost == 2_000


def test_contribution_margin_and_owner_adjustment():
    result = ContributionAnalysis(5_000, 2_000, 300, 20, 75)
    assert result.contribution == 2_700
    assert result.contribution_margin == pytest.approx(.54)
    assert result.imputed_owner_time_cost == 1_500
    assert result.contribution_after_owner_time == 1_200
    assert result.contribution_after_owner_time_margin == pytest.approx(.24)


def test_zero_price_margin_is_unknown_not_division_error():
    result = ContributionAnalysis(0, 100, 0, 0, 0)
    assert result.contribution == -100
    assert result.contribution_margin is None
    assert result.contribution_after_owner_time_margin is None


def test_customer_payback_uses_candidate_price_and_recurring_cost():
    customer, _ = views()
    assert customer.annual_net_benefit == 6_000
    assert customer.payback_months == pytest.approx(10)
    assert customer.cumulative_customer_result(1) == 1_000
    assert customer.cumulative_customer_result(3) == 13_000


def test_floor_ceiling_window_and_no_overlap_decision():
    _, local = views()
    assert local.economic_floor == 4_300
    ceiling = customer_ceiling_for_payback(6_000, 12)
    assert ceiling == 6_000
    assert PricingWindow(local.economic_floor, ceiling).decision is PricingDecision.HEALTHY_PRICE_IDENTIFIED
    failed = PricingWindow(6_000, 4_000)
    assert failed.has_overlap is False
    assert failed.decision is PricingDecision.NO_HEALTHY_PRICE


def test_unknown_window_inputs_request_evidence():
    assert PricingWindow(None, 4_000).decision is PricingDecision.NEED_BETTER_COST_ESTIMATE
    assert PricingWindow(4_000, None).decision is PricingDecision.NEED_BETTER_VALUE_EVIDENCE


def test_discount_reduces_contribution_disproportionately():
    base = ContributionAnalysis(6_000, 3_000, 0, 0, 0)
    result = discount_sensitivity(base, .10)
    assert result.discounted_price == 5_400
    assert result.contribution == 2_400
    assert result.contribution_change_rate == pytest.approx(.20)


def test_deposit_reduces_cash_exposure():
    costs = (PaymentEvent(0, 4_000, "partner"), PaymentEvent(1, 500, "tools"))
    no_deposit = PaymentStructure(PaymentTiming.ON_COMPLETION,
        (PaymentEvent(2, 8_000, "completion"),), costs)
    deposit = PaymentStructure(PaymentTiming.DEPOSIT_PLUS_FINAL,
        (PaymentEvent(0, 4_000, "deposit"), PaymentEvent(2, 4_000, "final")), costs)
    assert no_deposit.maximum_cash_exposure == 4_500
    assert deposit.maximum_cash_exposure == 500


def test_fixed_fee_t_and_m_and_phases_are_distinct_structures():
    customer, local = views()
    fixed = PriceScenario("fixed", PricingModel.FIXED_FEE, customer, local, "bounded")
    tm = PriceScenario("investigate", PricingModel.TIME_AND_MATERIALS, customer, local,
                       "evolving", budget_guardrail=6_000)
    phased = PriceScenario("validate", PricingModel.PHASED, customer, local, "bounded",
                           phases=(("validation", 750), ("implementation", 2_500)))
    assert fixed.model is not tm.model
    assert tm.budget_guardrail == 6_000
    assert phased.phases[0] == ("validation", 750)


def test_price_reduction_does_not_change_scope():
    customer, local = views()
    original = PriceScenario("base", PricingModel.FIXED_FEE, customer, local, "MUST + SHOULD")
    discounted = original.reduce_price(4_500)
    assert discounted.scope == original.scope
    assert discounted.customer.customer_price == 4_500
    assert original.customer.customer_price == 5_000


def test_scope_reduction_can_change_cost_and_value_separately():
    customer, local = views()
    original = PriceScenario("full", PricingModel.FIXED_FEE, customer, local, "MUST + SHOULD")
    smaller_customer = CustomerEconomicsView(20_000, 7_000, 1_500, 4_500)
    smaller_local = LocalWorksEconomicsView(1_600, 200, 16, 75, 400)
    smaller = PriceScenario("reduced", PricingModel.FIXED_FEE, smaller_customer, smaller_local, "MUST")
    assert smaller.scope != original.scope
    assert smaller.customer.recoverable_annual_value != original.customer.recoverable_annual_value
    assert smaller.local_works.delivery_partner_cost != original.local_works.delivery_partner_cost


def test_pricing_neither_creates_proposal_nor_guarantees_sale():
    customer, local = views()
    estimate = PricingEstimate(
        PriceScenario("base", PricingModel.FIXED_FEE, customer, local, "bounded"),
        PricingWindow(4_300, 6_000),
    )
    assert estimate.creates_proposal is False
    assert estimate.guarantees_sale is False
