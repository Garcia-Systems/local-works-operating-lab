import pytest
from local_works.pricing import ContributionAnalysis, PaymentEvent, PaymentStructure, PaymentTiming
from local_works.proposals import (NegotiationDecision, NegotiationHistory, NegotiationIssue,
 NegotiationRequest, discount_impact, no_deposit_cash_exposure, scope_reduction_analysis)
from test_proposals import proposal


def test_negotiation_can_express_scope_and_price_impacts():
 r=NegotiationRequest("add cancellation",NegotiationIssue.SCOPE,scope_impact="new workflow",price_impact=1000,
 response_options=(NegotiationDecision.DEFER,NegotiationDecision.COUNTER))
 r.decide(NegotiationDecision.DEFER,"Not in base scope")
 assert r.scope_impact=="new workflow" and r.price_impact==1000


def test_added_scope_requires_explicit_decision():
 p=proposal(); p.request_added_scope("cancellation")
 assert p.included==("freeze",) and p.scope.change_requests[0].request=="cancellation"


def test_discount_reduces_contribution_disproportionately():
 result=discount_impact(ContributionAnalysis(6000,2800,200,0,0),.20)
 assert result.discounted_price==4800 and result.contribution==1800
 assert result.contribution_change_rate==pytest.approx(.4)


def test_scope_reduction_is_independently_recosted():
 original=ContributionAnalysis(6000,3000,0,0,0); reduced=ContributionAnalysis(5400,2200,0,0,0)
 assert scope_reduction_analysis(original,reduced)["reduced_scope_contribution"]==3200


def test_no_deposit_exposes_cash():
 terms=PaymentStructure(PaymentTiming.ON_COMPLETION,(PaymentEvent(2,6000,"final"),),(PaymentEvent(0,2800,"startup"),PaymentEvent(1,400,"tools")))
 assert no_deposit_cash_exposure(terms)==3200


def test_roi_and_impossible_deadline_can_be_rejected():
 for issue in (NegotiationIssue.RISK_ALLOCATION,NegotiationIssue.TIMING):
  r=NegotiationRequest("request",issue,response_options=(NegotiationDecision.DECLINE_REQUEST,))
  assert r.decide(NegotiationDecision.DECLINE_REQUEST,"unsupported").decision is NegotiationDecision.DECLINE_REQUEST


def test_walkaway_after_interest_and_no_project_creation():
 p=proposal(); p.accept_in_principle()
 r=NegotiationRequest("no deposit",NegotiationIssue.PAYMENT_STRUCTURE)
 r.decide(NegotiationDecision.WALK_AWAY,"cannot finance",walk_away=True)
 history=NegotiationHistory(p,[r]); p.withdraw()
 assert history.requests[0].response.walk_away_condition_triggered
 assert not history.creates_project and not p.project_started
