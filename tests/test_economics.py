import pytest

from local_works.economics import (
    BurdenCategory, BurdenComponent, EconomicEstimate, EconomicInput,
    EconomicSignificance, EvidenceStatus as E, Frequency, FrequencyUnit as U,
    LaborRole, ProblemEconomics, Scenario, rework_burden,
    scenario_labor_burdens, significance,
)


def inp(name, value, unit="units", evidence=E.MEASURED):
    return EconomicInput(name, value, unit, evidence, "test source")


def weekly(amount=20):
    return Frequency(inp("requests", amount), U.PER_WEEK, inp("weeks", 50))


def role(minutes=8, cost=24, involvement=1, evidence=E.MEASURED):
    return LaborRole("front desk", inp("minutes", minutes, evidence=evidence),
                     inp("cost", cost, evidence=evidence), inp("involvement", involvement))


def test_frequency_annualizes_configured_periods_and_common_units():
    assert weekly().annualize().annual_amount == 1000
    assert Frequency(inp("monthly", 10), U.PER_MONTH, inp("months", 11)).annualize().annual_amount == 110
    assert Frequency(inp("yearly", 7), U.PER_YEAR).annualize().annual_amount == 7


def test_labor_and_percentage_manager_and_multiple_roles():
    front = role().annual_burden(weekly())
    manager = role(3, 36, .25).annual_burden(weekly())
    assert front.annual_amount == pytest.approx(3200)
    assert manager.annual_amount == pytest.approx(450)
    assert front.annual_amount + manager.annual_amount == pytest.approx(3650)


def test_rework_calculation_and_unknown_stays_unknown():
    known = rework_burden(weekly(), inp("rate", .05), inp("minutes", 15), inp("cost", 24))
    assert known.annual_amount == pytest.approx(300)
    unknown = rework_burden(weekly(), inp("rate", None, evidence=E.UNKNOWN), inp("minutes", 15), inp("cost", 24))
    assert unknown.annual_amount is None and unknown.evidence is E.UNKNOWN


def test_zero_frequency_is_a_known_zero():
    assert role().annual_burden(weekly(0)).annual_amount == 0


def test_ranges_are_ordered_and_invalid_ranges_rejected():
    fs = {Scenario.LOW: weekly(10), Scenario.BASELINE: weekly(20), Scenario.HIGH: weekly(30)}
    roles = {scenario: (role(),) for scenario in Scenario}
    result = scenario_labor_burdens(fs, roles)
    assert result[Scenario.LOW] < result[Scenario.BASELINE] < result[Scenario.HIGH]
    with pytest.raises(ValueError):
        scenario_labor_burdens({Scenario.LOW: weekly(30), Scenario.BASELINE: weekly(20), Scenario.HIGH: weekly(10)}, roles)


def test_provenance_is_preserved_and_estimates_are_not_measured():
    estimate = role(evidence=E.ESTIMATED).annual_burden(weekly())
    assert estimate.evidence is E.ESTIMATED
    assert any(item.source == "test source" for item in estimate.inputs)
    hypothetical = role(evidence=E.HYPOTHETICAL).annual_burden(weekly())
    assert hypothetical.evidence is E.ESTIMATED
    assert any(item.evidence is E.HYPOTHETICAL for item in hypothetical.inputs)


def component(identifier="labor", group=None):
    estimate = role().annual_burden(weekly())
    return BurdenComponent(identifier, BurdenCategory.LABOR, "active work", estimate,
                           overlap_group=group, includes="the modeled active minutes")


def test_double_counting_safeguards_and_inclusion_metadata():
    economics = ProblemEconomics("test")
    economics.add_component(component(group="same-work"))
    with pytest.raises(ValueError): economics.add_component(component("duplicate", "same-work"))
    with pytest.raises(ValueError): economics.add_component(component())
    with pytest.raises(ValueError):
        BurdenComponent("bad", BurdenCategory.REWORK, "rework",
                        EconomicEstimate(10, E.MEASURED, (), "test"))


def test_wait_customer_time_and_unsupported_revenue_are_not_automatically_money():
    economics = ProblemEconomics("test", non_monetized_burdens=["2-day wait", "10 customer minutes"],
                                  unknown_potential_burdens=["lost revenue", "retention"])
    assert economics.annual_direct_burden.annual_amount == 0
    assert "2-day wait" in economics.non_monetized_burdens
    assert "lost revenue" in economics.unknown_potential_burdens


def test_unknown_included_component_makes_total_unknown_not_zero():
    economics = ProblemEconomics("test")
    economics.add_component(BurdenComponent("revenue", BurdenCategory.LOST_REVENUE,
        "unsupported impact", EconomicEstimate(None, E.UNKNOWN, (inp("revenue", None, evidence=E.UNKNOWN),), "UNKNOWN"),
        includes="potential revenue impact"))
    assert economics.annual_direct_burden.annual_amount is None


def test_significance_is_a_burden_gate_not_project_recommendation():
    estimate = role(evidence=E.ESTIMATED).annual_burden(weekly())
    assert significance(estimate, materiality_threshold=1000) is EconomicSignificance.POTENTIALLY_MEANINGFUL
    assert significance(estimate, materiality_threshold=10_000) is EconomicSignificance.ECONOMICALLY_TRIVIAL
    assert significance(estimate, materiality_threshold=1000, evidence_complete=False) is EconomicSignificance.MORE_EVIDENCE_REQUIRED


def test_current_burden_is_distinct_from_recoverable_value():
    economics = ProblemEconomics("test")
    economics.add_component(component())
    assert economics.annual_direct_burden.annual_amount == pytest.approx(3200)
    assert economics.recoverable_value is None
