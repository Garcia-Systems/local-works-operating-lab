from dataclasses import replace
from pathlib import Path

from local_works.capstone import BASELINE, simulate
from local_works.capstone_scenarios import (
    BusinessDesignLever, OwnerCompensationPolicy, OwnerIncomeModel, OwnerIncomeTarget,
    OwnerIncomeTargetState, ScenarioBottleneck, SCENARIOS, break_even,
    compare_scenario, lever_test, monte_carlo, operating_models,
    ranked_sensitivities, scenario_suite, target_result,
)


def test_reserve_first_preserves_reserve_when_a_draw_is_made():
    result=simulate(replace(BASELINE,opening_cash=100_000,name="CASH_RICH"))
    income=OwnerIncomeModel().calculate(result,replace(BASELINE,opening_cash=100_000))
    assert any(income.monthly_draws)
    assert all(cash >= income.reserve_minimum for draw,cash in zip(income.monthly_draws,income.monthly_post_draw_cash) if draw)


def test_draw_can_be_zero_with_revenue_and_positive_with_available_cash():
    no_draw=OwnerIncomeModel(OwnerCompensationPolicy.NO_DRAW).calculate(simulate(),BASELINE)
    normal=OwnerIncomeModel().calculate(simulate(),BASELINE)
    assert simulate().total_revenue > 0 and sum(no_draw.monthly_draws)==0
    assert sum(normal.monthly_draws)>0


def test_revenue_contribution_cash_and_draw_remain_distinct():
    result=simulate(); income=OwnerIncomeModel().calculate(result)
    assert result.total_revenue != result.total_contribution
    assert result.total_contribution != result.ending_cash
    assert result.ending_cash != sum(income.monthly_draws)


def test_all_three_years_and_safe_per_hour_calculate():
    income=OwnerIncomeModel().calculate(simulate())
    assert [x.year for x in income.years]==[1,2,3]
    assert all(x.owner_draw >= 0 and x.owner_draw_per_hour >= 0 for x in income.years)


def test_target_states_cover_achievement_instability_overload_and_failure():
    income=OwnerIncomeModel().calculate(simulate())
    assert target_result(income,OwnerIncomeTarget(50_000)).state is OwnerIncomeTargetState.ACHIEVED_BUT_UNSTABLE
    assert target_result(income,OwnerIncomeTarget(500_000)).state is OwnerIncomeTargetState.NOT_ACHIEVED
    stable=OwnerIncomeModel(minimum_reserve=0,draw_fraction=1,monthly_draw_cap=1_000_000).calculate(simulate(replace(BASELINE,opening_cash=2_000_000)),replace(BASELINE,opening_cash=2_000_000))
    assert target_result(stable,OwnerIncomeTarget(1)).state in {OwnerIncomeTargetState.ACHIEVED,OwnerIncomeTargetState.ACHIEVED_BUT_UNSTABLE}
    growth=OwnerIncomeModel().calculate(simulate(SCENARIOS["RAPID_GROWTH"]),SCENARIOS["RAPID_GROWTH"])
    assert target_result(growth,OwnerIncomeTarget(75_000)).state is OwnerIncomeTargetState.ACHIEVED_WITH_OVERLOAD


def test_scenarios_differ_preserve_capacity_and_expose_expected_bottlenecks():
    rows={x.scenario:x for x in scenario_suite()}
    assert rows["CONSERVATIVE"] != rows["BASELINE"]
    assert rows["OPTIMISTIC"].peak_owner_hours_week <= SCENARIOS["OPTIMISTIC"].temporary_maximum_hours/4.33
    assert rows["RAPID_GROWTH"].overload_months > rows["BASELINE"].overload_months
    assert rows["LOW_DEMAND"].primary_bottleneck is ScenarioBottleneck.DEMAND
    assert rows["LOW_PRICE"].primary_bottleneck is ScenarioBottleneck.ECONOMICS and rows["LOW_PRICE"].customers_acquired > 0
    assert rows["HIGH_SUPPORT_BURDEN"].primary_bottleneck is ScenarioBottleneck.SUPPORT
    assert rows["CASH_STRESS"].funding_required > 0


def test_scenario_comparison_is_deterministic():
    assert compare_scenario(BASELINE)==compare_scenario(BASELINE)


def test_break_even_calculations_are_supported_and_positive():
    result=break_even()
    assert result.sales_per_year>0 and result.project_contribution>0
    assert result.maximum_owner_hours_per_project>0
    assert result.maximum_support_hours_per_customer_month>0
    assert result.minimum_opening_cash>=BASELINE.opening_cash


def test_sensitivity_changes_and_ranking_is_deterministic():
    first=ranked_sensitivities(); second=ranked_sensitivities()
    assert first==second and any(x.absolute_impact>0 for x in first)
    assert first[0].absolute_impact>=first[-1].absolute_impact


def test_monte_carlo_reproducible_ordered_and_bounded():
    a=monte_carlo(25,77); b=monte_carlo(25,77)
    assert a==b and a.p10_year3_draw<=a.p50_year3_draw<=a.p90_year3_draw
    for value in (a.cash_nonnegative_frequency,a.target_achieved_frequency,a.overload_frequency,a.working_capital_frequency,a.concentration_frequency): assert 0<=value<=1


def test_operating_models_differ_and_lever_is_bounded():
    models={x.model:x.comparison for x in operating_models()}
    assert models["PROJECT_ONLY"] != models["PROJECT_PLUS_MANAGED_SUPPORT"]
    lever=lever_test()
    assert lever.lever is BusinessDesignLever.RAISE_PRICE
    assert lever.after.contribution_36_months>lever.before.contribution_36_months
    assert "conversion" in lever.unchanged_assumptions


def test_32b_boundaries_remain_explicit():
    text=Path("book/32-owner-income-and-final-examination.md").read_text()
    script=Path("scripts/run_chapter_32b.py").read_text()
    assert "IN PROGRESS" in text and "32C" in text
    assert "No final verdict" in script
    assert not Path("artisan").exists()
    assert "production requirements are produced" in script
