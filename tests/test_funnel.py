import pytest

from local_works.acquisition import (
    FunnelScenario, FunnelStage, FunnelTransition, OwnerEffort,
    analyze_bottlenecks, baseline_website_funnel, referral_funnel,
)
from local_works.hypothesis import EvidenceType


def transition(a, b, rate):
    return FunnelTransition(a, b, rate, EvidenceType.HYPOTHESIS)


def test_expected_counts_compound():
    result = baseline_website_funnel().expected()
    assert [s.advanced for s in result.steps[:3]] == [200, 30, 7.5]
    assert result.final_count == pytest.approx(0.27)


@pytest.mark.parametrize("rate", [-0.01, 1.01])
def test_conversion_rate_bounds(rate):
    with pytest.raises(ValueError):
        transition(FunnelStage.EXPOSURE, FunnelStage.SALE, rate)


def test_channels_can_enter_at_different_stages():
    assert baseline_website_funnel().entry_stage is FunnelStage.EXPOSURE
    assert referral_funnel().entry_stage is FunnelStage.REFERRAL


def test_seeded_simulation_is_reproducible_and_marked_simulated():
    first = baseline_website_funnel().simulate(42)
    assert first == baseline_website_funnel().simulate(42)
    assert first.is_simulated
    assert first.evidence_type is EvidenceType.HYPOTHESIS
    assert "NOT OBSERVED EVIDENCE" in first.notice


def test_assumption_retains_evidence_status():
    assert all(t.evidence_type is EvidenceType.HYPOTHESIS
               for t in baseline_website_funnel().transitions)


def test_zero_conversion_stops_downstream_and_full_conversion_preserves_count():
    S = FunnelStage
    scenario = FunnelScenario("bounds", 10, S.EXPOSURE, (
        transition(S.EXPOSURE, S.LEAD, 1), transition(S.LEAD, S.SALE, 0)))
    assert [step.advanced for step in scenario.expected().steps] == [10, 0]
    assert scenario.simulate(1).final_count == 0


def test_owner_time_uses_stage_activity_volume():
    S = FunnelStage
    scenario = FunnelScenario("effort", 10, S.LEAD,
        (transition(S.LEAD, S.DISCOVERY, .5),),
        (OwnerEffort(S.LEAD, 6), OwnerEffort(S.DISCOVERY, 60)))
    assert scenario.estimated_owner_hours() == 6


def test_qualification_dropoff_is_not_automatically_a_failure():
    findings = analyze_bottlenecks(baseline_website_funnel())
    assert all(not finding.is_business_failure for finding in findings.values())
    assert "protect" in baseline_website_funnel().transitions[3].notes.lower()
