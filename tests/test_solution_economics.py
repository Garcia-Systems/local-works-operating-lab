from local_works.economics import (BurdenCategory, BurdenComponent, EconomicEstimate,
                                  EconomicInput, EvidenceStatus)
from local_works.solution_economics import (
    BenefitType, CostCategory, EconomicAssumption, EconomicDecision,
    EconomicScenario, RecoverableValueComponent, ScenarioLevel, SolutionCost,
    SolutionEconomics, ValueCategory, compare_incrementally, validate_scenarios,
)
import pytest


def assumption(name: str, value: float | None, evidence=EvidenceStatus.HYPOTHETICAL):
    return EconomicAssumption(name, value, evidence, "test evidence")


def burden(amount: float | None = 10_000) -> BurdenComponent:
    source = EconomicInput("burden", amount, "dollars/year",
                           EvidenceStatus.ESTIMATED if amount is not None else EvidenceStatus.UNKNOWN,
                           "Chapter 10")
    return BurdenComponent("labor", BurdenCategory.LABOR, "Current labor", EconomicEstimate(
        amount, source.evidence, (source,), "supported current burden"), includes="labor")


def component(*, amount=10_000, fraction=.5, adoption=.8, realization=.75,
              benefit_type=BenefitType.FREED_CAPACITY, supported=True):
    return RecoverableValueComponent(
        burden(amount), ValueCategory.LABOR_CAPACITY, benefit_type,
        assumption("recoverable", fraction), assumption("adoption", adoption),
        assumption("realization", realization), "Verification and exceptions remain",
        supported=supported, freed_hours=200,
    )


def economics(value_component=None, implementation=1_000, recurring=100, new_work=200):
    costs = [
        SolutionCost("setup", CostCategory.SOFTWARE_SETUP, implementation,
                     EvidenceStatus.HYPOTHETICAL if implementation is not None else EvidenceStatus.UNKNOWN,
                     "preliminary estimate"),
        SolutionCost("subscription", CostCategory.SUBSCRIPTION, recurring,
                     EvidenceStatus.ESTIMATED, "vendor information", recurring=True),
    ]
    return SolutionEconomics("Configure", 10_000, [value_component or component()], costs,
                             annual_new_operating_burden=new_work,
                             decision=EconomicDecision.ECONOMICALLY_ATTRACTIVE)


def test_burden_recovery_adoption_realization_and_remaining_work_are_distinct():
    value = component()
    assert value.burden.estimate.annual_amount == 10_000
    assert value.annual_value == 3_000
    assert value.annual_value != value.burden.estimate.annual_amount
    assert value.remaining_work == "Verification and exceptions remain"


def test_fraction_cannot_exceed_burden_or_be_silently_separately_justified():
    with pytest.raises(ValueError):
        component(fraction=1.01)
    with pytest.raises(ValueError):
        RecoverableValueComponent(burden(), ValueCategory.OTHER, BenefitType.CASH_SAVINGS,
            assumption("fraction", .5), assumption("adoption", .8), assumption("realization", .8),
            "work remains", separately_justified_value=True)


def test_freed_capacity_is_not_cash_savings():
    value = component()
    assert value.annual_value == 3_000
    assert value.freed_hours == 200
    assert value.cash_savings is None


def test_adoption_and_realization_each_reduce_theoretical_value():
    full = component(adoption=1, realization=1).annual_value
    assert component(adoption=.5, realization=1).annual_value == full / 2
    assert component(adoption=1, realization=.5).annual_value == full / 2


def test_costs_net_benefit_first_year_payback_and_cumulative_value():
    model = economics()
    assert model.implementation_cost == 1_000
    assert model.annual_recurring_cost == 100
    assert model.first_year_cost == 1_100
    assert model.annual_net_benefit == 2_700
    assert model.payback_months == pytest.approx(40 / 9)
    assert model.cumulative_value(1) == 1_700
    assert model.cumulative_value(3) == 7_100


@pytest.mark.parametrize("new_work", [2_900, 4_000])
def test_zero_or_negative_net_benefit_has_no_payback(new_work):
    assert economics(new_work=new_work).payback_months is None


def test_unknown_cost_or_value_prevents_precise_roi():
    assert economics(implementation=None).first_year_roi is None
    assert economics(component(amount=None)).first_year_roi is None


def test_unsupported_revenue_is_excluded():
    revenue = RecoverableValueComponent(
        burden(), ValueCategory.REVENUE_RECOVERY, BenefitType.REVENUE_VALUE,
        assumption("fraction", .5), assumption("adoption", .8), assumption("realization", .8),
        "No revenue causal evidence", supported=False)
    assert revenue.annual_value is None


def test_scenarios_are_ordered_and_incremental_comparison_works():
    scenarios = [EconomicScenario(level, economics(component(fraction=fraction)))
                 for level, fraction in zip(ScenarioLevel, (.3, .5, .7))]
    validate_scenarios(scenarios)
    richer = economics(component(fraction=.8), implementation=5_000)
    comparison = compare_incrementally(scenarios[1].economics, richer)
    assert comparison.additional_implementation_cost == 4_000
    assert comparison.additional_annual_net_benefit == 1_800


def test_attractiveness_neither_proposes_nor_approves():
    model = economics()
    assert model.decision is EconomicDecision.ECONOMICALLY_ATTRACTIVE
    assert model.creates_proposal is False
    assert model.approves_project is False
