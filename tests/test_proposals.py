from datetime import date
import pytest
from local_works.economics import EvidenceStatus
from local_works.pricing import CustomerEconomicsView, LocalWorksEconomicsView, PriceScenario, PricingModel
from local_works.proposals import EconomicClaim, Proposal, ProposalDecision, ProposalStatus
from local_works.scope import ProjectScope, ScopeBoundary, ScopeExclusion, ScopeItem


def proposal():
 scope=ProjectScope("Harbor","Freeze","Reduce handling","Repeated handling","CONFIGURE",ScopeBoundary("request","confirmation"),[ScopeItem("freeze")],[ScopeExclusion("cancellation")])
 customer=CustomerEconomicsView(10000,None,None,6000,evidence_quality="UNKNOWN")
 pricing=PriceScenario("base",PricingModel.FIXED_FEE,customer,LocalWorksEconomicsView(2800,400,10,50,500),"Freeze")
 return Proposal("Harbor","Freeze",scope.problem_statement,"PAID VALIDATION",scope,pricing,
   economic_claims=[EconomicClaim("Retention impact",None,EvidenceStatus.UNKNOWN,"Chapter 13")],valid_through=date(2026,10,4))


def test_proposal_preserves_problem_scope_exclusions_and_price():
 p=proposal(); p.assert_consistent()
 assert p.problem_statement==p.scope.problem_statement
 assert p.included==("freeze",) and p.excluded==("cancellation",)
 assert p.customer_price==6000
 assert p.economic_claims[0].evidence is EvidenceStatus.UNKNOWN


def test_proposal_cannot_construct_contradictory_scope():
 with pytest.raises(ValueError):
  ProjectScope("B","O","Outcome","Problem","Configure",ScopeBoundary("a","b"),[ScopeItem("same")],[ScopeExclusion("SAME")])


def test_missing_claim_stays_unknown():
 with pytest.raises(ValueError): EconomicClaim("ROI",None,EvidenceStatus.ESTIMATED,"guess")


def test_revisions_preserve_history():
 p=proposal(); old=p.version_history[0]
 p.revise(reason="phase",pricing=p.pricing.reduce_price(900),payment_description="100% for validation")
 assert [x.version for x in p.version_history]==[1,2]
 assert old.customer_price==6000 and p.version_history[1].customer_price==900


def test_acceptance_is_not_contract_deposit_or_project():
 p=proposal(); p.accept_in_principle()
 assert p.decision is ProposalDecision.ACCEPTED_IN_PRINCIPLE
 assert not p.contract_executed and not p.deposit_received and not p.project_started


def test_decline_and_withdraw_are_explicit():
 p=proposal(); p.decline(); assert p.status is ProposalStatus.DECLINED
 p=proposal(); p.withdraw(); assert p.status is ProposalStatus.WITHDRAWN and p.decision is ProposalDecision.NO_HEALTHY_DEAL
