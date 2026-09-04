"""Meaningful Chapter 30 relationship-model checks."""
import inspect
import local_works.relationships as module
from local_works.relationships import *


def econ(**kw): return RelationshipEconomics(project_revenue=1000, project_direct_cost=400, owner_hour_value=50, **kw)

def test_retention_is_not_lock_in():
    assert CustomerRelationship("A", RelationshipStatus.HEALTHY).retained_ethically
    assert not CustomerRelationship("A", RelationshipStatus.HEALTHY, locked_in=True).retained_ethically

def test_quiet_can_be_healthy_and_not_automatic_risk():
    r=CustomerRelationship("A", RelationshipStatus.QUIET, RelationshipHealth(overall=HealthRating.HEALTHY), RetentionRisk.LOW)
    assert r.health.overall is HealthRating.HEALTHY and not r.quiet_is_risk

def test_health_and_profitability_are_independent():
    assert CustomerRelationship("A", RelationshipStatus.AT_RISK, RelationshipHealth(overall=HealthRating.AT_RISK), economics=econ()).economics.cumulative_contribution > 0
    assert CustomerRelationship("B", RelationshipStatus.HEALTHY, RelationshipHealth(overall=HealthRating.HEALTHY), economics=econ(other_direct_cost=700)).economics.cumulative_contribution < 0

def test_evidence_preserves_expected_vs_measured():
    expected=CustomerOutcomeEvidence("time", evidence_type=EvidenceType.EXPECTED_ONLY)
    measured=CustomerOutcomeEvidence("time", 10, 8, evidence_type=EvidenceType.MEASURED)
    assert not expected.is_measured and measured.is_measured and expected.current_value == UNKNOWN

def test_signal_is_not_automatically_opportunity():
    s=ExpansionSignal("idea")
    assert not s.qualified and s.pipeline_state is ExpansionPipelineState.SIGNAL

def test_discovery_and_leave_alone_are_legitimate():
    s=ExpansionSignal("request")
    assert ExpansionOpportunity(s,"problem").decision is ExpansionDecision.DISCOVERY_REQUIRED
    assert ExpansionOpportunity(s,"tiny",decision=ExpansionDecision.LEAVE_ALONE).decision is ExpansionDecision.LEAVE_ALONE

def test_deferred_and_support_sources_can_be_signals_without_sales():
    for source in (SignalSource.DEFERRED_CHANGE, SignalSource.SUPPORT):
        assert ExpansionSignal("friction",source).pipeline_state is ExpansionPipelineState.SIGNAL

def test_expansion_contribution_and_owner_hours():
    o=ExpansionOpportunity(ExpansionSignal("x"),"x",delivery_cost=1200,customer_price=2000,owner_hours=10)
    assert o.contribution == 800 and o.contribution_per_owner_hour == 80

def test_churn_can_be_healthy_or_unhealthy_and_unknown_risk():
    assert ChurnEvent(ChurnReason.PROJECT_COMPLETE_NO_SUPPORT_NEEDED,True).healthy
    assert not ChurnEvent(ChurnReason.SUPPORT_QUALITY,False).healthy
    assert CustomerRelationship("x").retention_risk is RetentionRisk.UNKNOWN

def test_graceful_offboarding_is_representable():
    p=OffboardingPlan(True,True,True,True,True,"settled","2026-10-01")
    assert p.ownership_confirmed and p.support_termination_date == "2026-10-01"

def test_referral_readiness_waits_then_can_be_ready():
    assert assess_referral(stable=True,health=HealthRating.HEALTHY,measured_value=False,unresolved_dispute=False) is ReferralReadiness.WAIT_FOR_MEASUREMENT
    assert assess_referral(stable=True,health=HealthRating.HEALTHY,measured_value=True,unresolved_dispute=False,willing=True) is ReferralReadiness.READY

def test_referral_request_is_optional_unsent_simulation():
    r=ReferralRequest(ReferralReadiness.READY,"No pressure")
    assert r.optional and r.simulated_only and not r.sent

def test_public_case_requires_reality_evidence_permission_review():
    assert assess_case_study(real_customer=False,permission=True,measured_evidence=True,confidentiality_reviewed=True) is CaseStudyReadiness.READY_FOR_INTERNAL_TRAINING_SUMMARY
    assert assess_case_study(real_customer=True,permission=None,measured_evidence=True,confidentiality_reviewed=True) is CaseStudyReadiness.PERMISSION_REQUIRED
    assert assess_case_study(real_customer=True,permission=True,measured_evidence=True,confidentiality_reviewed=True) is CaseStudyReadiness.READY_FOR_PUBLIC_CASE

def test_relationship_economics_preserve_components_and_calculate():
    e=RelationshipEconomics(1000,400,300,100,50,500,200,25,1,5,2,1,1,3,1,50)
    assert (e.project_contribution,e.support_contribution,e.expansion_contribution)==(600,200,300)
    assert e.cumulative_contribution==1025 and e.total_owner_hours==14
    assert e.owner_time_adjusted_contribution==325
    assert e.expansion_contribution_per_owner_hour==100

def test_relationship_can_receive_leave_alone_action():
    assert CustomerRelationship("x", action=RelationshipAction.LEAVE_ALONE).action is RelationshipAction.LEAVE_ALONE

def test_chapter_has_no_outreach_testimonial_or_portfolio_automation():
    source=inspect.getsource(module).lower()
    assert "requests.post" not in source and "smtplib" not in source
    assert not ({"testimonial", "customerportfolio", "portfolioscaling"} & {n.lower() for n in vars(module)})
