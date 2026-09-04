import pytest

from local_works.acquisition import FunnelScenario, FunnelStage, FunnelTransition
from local_works.acquisition_economics import (
    AcquisitionCost, AcquisitionPeriod, ChannelEconomics, OwnerTimeActivity,
    compare_channels, cumulative_economics,
)
from local_works.hypothesis import EvidenceType


def channel(customers=1, funnel=None):
    return ChannelEconomics("test", (
        AcquisitionCost("ads", 500, 2),
        AcquisitionCost("travel", 40, 3),
    ), customers, funnel)


def test_cash_costs_and_owner_hours_sum_correctly():
    item = channel()
    assert item.total_cash_cost == 540
    assert item.total_owner_hours == 5


def test_activity_time_is_included():
    item = ChannelEconomics("activity", (), 1, activities=(OwnerTimeActivity("review", 6, 10),))
    assert item.total_owner_hours == 1


def test_owner_value_and_fully_loaded_cost_respond_to_assumption():
    low = channel().calculate(25)
    high = channel().calculate(100)
    assert low.owner_time_cost == 125
    assert low.fully_loaded_acquisition_cost == 665
    assert high.fully_loaded_acquisition_cost == 1040
    assert high.fully_loaded_cac > low.fully_loaded_cac


def test_cac_views_are_calculated():
    result = channel(2).calculate(50)
    assert result.cash_cac == 270
    assert result.owner_hours_per_customer == 2.5
    assert result.fully_loaded_cac == 395


def test_zero_customers_have_undefined_not_zero_cac():
    result = channel(0).calculate(50)
    assert result.cash_cac is None
    assert result.owner_hours_per_customer is None
    assert result.fully_loaded_cac is None
    assert result.fully_loaded_acquisition_cost == 790


def test_cumulative_periods_include_unsuccessful_period():
    month_one = AcquisitionPeriod("one", ChannelEconomics("one", (AcquisitionCost("ads", 500, 20),), 0))
    month_two = AcquisitionPeriod("two", ChannelEconomics("two", (AcquisitionCost("ads", 200, 4),), 1))
    result = cumulative_economics("two months", (month_one, month_two)).calculate(50)
    assert result.total_cash_cost == 700
    assert result.total_owner_hours == 24
    assert result.fully_loaded_cac == 1900


def test_cost_per_stage_handles_zero_and_preserves_simulation_status():
    S = FunnelStage
    scenario = FunnelScenario("zero", 2, S.EXPOSURE, (
        FunnelTransition(S.EXPOSURE, S.LEAD, 0, EvidenceType.HYPOTHESIS),
        FunnelTransition(S.LEAD, S.SALE, 1, EvidenceType.HYPOTHESIS),
    ))
    funnel = scenario.simulate(7)
    costs = ChannelEconomics("zero", (AcquisitionCost("ads", 10),), 0, funnel).cost_per_stage(50)
    assert costs[0].cash_cost_per_outcome == 5
    assert costs[1].cash_cost_per_outcome is None
    assert costs[2].fully_loaded_cost_per_outcome is None
    assert all(item.is_simulated for item in costs)
    assert all(item.evidence_type is EvidenceType.HYPOTHESIS for item in costs)


def test_comparison_reports_views_but_does_not_declare_a_winner():
    free_cash = ChannelEconomics("owner-heavy", (AcquisitionCost("outreach", 0, 40),), 1)
    paid = ChannelEconomics("paid", (AcquisitionCost("ads", 600, 8),), 1)
    low_value = compare_channels((free_cash, paid), 25)
    high_value = compare_channels((free_cash, paid), 100)
    # Cash alone ranks owner-heavy first, while either loaded view reverses it.
    assert low_value[0].cash_cac < low_value[1].cash_cac
    assert low_value[0].fully_loaded_cac > low_value[1].fully_loaded_cac
    assert high_value[0].fully_loaded_cac - high_value[1].fully_loaded_cac > 2000
    assert not hasattr(low_value, "winner")


@pytest.mark.parametrize("cash,hours", [(-1, 0), (0, -1)])
def test_costs_cannot_be_negative(cash, hours):
    with pytest.raises(ValueError):
        AcquisitionCost("bad", cash, hours)
