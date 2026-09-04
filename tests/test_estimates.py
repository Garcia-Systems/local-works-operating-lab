from datetime import date
import pytest
from local_works.estimates import *


def request():
    return EstimateRequest("ER-v1", "Workflow", "Fictional Co", "OPP", "Problem", "Outcome", "Configure", "SCOPE-v1", ("approval",), ("portal",), ("rules",), ("approval tested",), ("platform",))


def estimate(name="Candidate", cost=(2000, 2000), scope="SCOPE-v1", alignment=ScopeAlignment.ALIGNED):
    return TechnicalEstimate(name, "Workflow", "SCOPE-v1", scope, "Configure", [
        EstimateComponent(ComponentType.CONFIGURATION, "Configure", EstimateRange(8, 12, "hours"), EstimateRange(*cost)),
        EstimateComponent(ComponentType.TESTING, "Test", EstimateRange(2, 4, "hours"), fixed_cost=500),
    ], status=EstimateStatus.RECEIVED, scope_alignment=alignment,
       effort=EstimateRange(10, 16, "hours"), partner_cost=EstimateRange(cost[0] + 500, cost[1] + 500),
       timeline=TimelineEstimate(EstimateRange(2, 3, "weeks"), date(2026, 9, 20)),
       confidence=EstimateConfidence.MODERATE,
       assumptions=[EstimateAssumption("Access exists", "HIGH", "UNKNOWN", "Delay")],
       exclusions=[EstimateExclusion("Migration")], customer_effort=EstimateRange(3, 5, "hours"),
       local_works_effort=EstimateRange(4, 6, "hours"), third_party_implementation_cost=EstimateRange(100, 200))


def test_scope_reference_and_estimate_is_not_customer_price():
    e = estimate()
    assert e.baseline_scope_version == "SCOPE-v1"
    assert not hasattr(e, "customer_price")
    assert request().scope_version == e.estimated_scope_version


def test_ranges_components_confidence_assumptions_and_exclusions():
    e = estimate()
    assert e.component_cost_total() == EstimateRange(2500, 2500)
    assert e.component_effort_total() == EstimateRange(10, 16, "hours")
    assert (e.effort.lower, e.effort.upper) == (10, 16)
    assert e.confidence is EstimateConfidence.MODERATE
    assert e.assumptions[0].evidence_status == "UNKNOWN"
    assert e.exclusions[0].statement == "Migration"
    with pytest.raises(ValueError):
        EstimateRange(4, 2)


def test_cost_and_effort_categories_stay_distinct():
    e = estimate()
    assert e.partner_cost == EstimateRange(2500, 2500)
    assert e.third_party_implementation_cost == EstimateRange(100, 200)
    assert e.customer_effort == EstimateRange(3, 5, "hours")
    assert e.local_works_effort == EstimateRange(4, 6, "hours")
    assert e.effort != e.customer_effort != e.local_works_effort
    assert e.timeline.duration == EstimateRange(2, 3, "weeks")
    assert e.timeline.earliest_start == date(2026, 9, 20)


def test_conditional_discovery_and_clarification_status():
    e = estimate()
    e.status = EstimateStatus.CONDITIONAL_ESTIMATE
    e.technical_discovery_required = True
    e.discovery_cost = EstimateRange(500, 500)
    assert e.technical_discovery_required and e.discovery_cost.lower == 500
    e.add_clarification(EstimateClarification("Testing?", "Compare"))
    assert e.status is EstimateStatus.NEEDS_CLARIFICATION
    e.add_clarification(EstimateClarification("Testing?", "Compare", "Included", "None", ClarificationStatus.ANSWERED))
    assert e.status is EstimateStatus.REVISED


def test_scope_mismatch_is_not_comparable():
    e = estimate(scope="PORTAL-v1", alignment=ScopeAlignment.SCOPE_DEVIATION)
    result = EstimateComparison(request(), [e]).normalize(e.candidate)
    assert not result.comparable
    assert e.status is EstimateStatus.NOT_COMPARABLE


def test_normalization_exposes_missing_cost_and_keeps_recurring_separate():
    e = estimate()
    e.recurring_third_party_cost = EstimateRange(50, 50, "USD/month")
    adjustment = NormalizationAdjustment("Missing documentation", EstimateRange(600, 600), "Excluded")
    result = EstimateComparison(request(), [e]).normalize(e.candidate, (adjustment,))
    # partner 2500 + third-party setup 100–200 + missing documentation 600
    assert result.normalized_delivery_cost == EstimateRange(3200, 3300)
    assert e.recurring_third_party_cost == EstimateRange(50, 50, "USD/month")


def test_raw_low_and_high_prices_do_not_drive_decision():
    low = estimate("Low", (1500, 1500))
    high = estimate("High", (4000, 4000))
    comparison = EstimateComparison(request(), [low, high])
    normalized_low = comparison.normalize("Low", (
        NormalizationAdjustment("Testing", EstimateRange(1000, 1000), "missing"),
        NormalizationAdjustment("Deployment", EstimateRange(700, 700), "missing"),
        NormalizationAdjustment("Documentation", EstimateRange(600, 600), "missing"),
        NormalizationAdjustment("Vendor setup", EstimateRange(500, 500), "missing"),
    ))
    normalized_high = comparison.normalize("High")
    assert normalized_low.normalized_delivery_cost.lower > normalized_high.normalized_delivery_cost.lower
    # Decision is explicit, not an automatic min/max operation.
    decision = EstimateDecision("High", EstimateDecisionType.SELECT_FOR_DELIVERY, "Complete comparable scope")
    assert decision.candidate == "High"


def test_over_and_under_scope_can_be_revised_or_rejected():
    over = estimate("Over", scope="PORTAL", alignment=ScopeAlignment.SCOPE_DEVIATION)
    under = estimate("Under", alignment=ScopeAlignment.INCOMPLETE_SCOPE)
    assert not EstimateComparison(request(), [over]).normalize("Over").comparable
    assert not EstimateComparison(request(), [under]).normalize("Under").comparable
    assert EstimateDecision("Over", EstimateDecisionType.REQUEST_REVISED_ESTIMATE, "Return to baseline").decision is EstimateDecisionType.REQUEST_REVISED_ESTIMATE
    assert EstimateDecision("Under", EstimateDecisionType.DO_NOT_SELECT, "Required approval omitted").decision is EstimateDecisionType.DO_NOT_SELECT


def test_discovery_and_backward_decisions_do_not_start_delivery():
    for kind in (EstimateDecisionType.SELECT_FOR_TECHNICAL_DISCOVERY,
                 EstimateDecisionType.REVISIT_SCOPE,
                 EstimateDecisionType.REVISIT_SOLUTION):
        decision = EstimateDecision(None, kind, "Evidence requires another gate")
        assert not decision.starts_implementation
    with pytest.raises(ValueError):
        EstimateDecision("Candidate", EstimateDecisionType.SELECT_FOR_DELIVERY, "Not kickoff", starts_implementation=True)
    comparison = EstimateComparison(request(), [estimate()])
    assert not comparison.implementation_started
