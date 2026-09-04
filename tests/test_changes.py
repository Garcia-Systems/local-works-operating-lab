"""Meaning-level checks for Chapter 24 change control."""
from datetime import date
from local_works.changes import *

BASE = BaselineReference("scope-v1", "req-v1", date(2026, 9, 15), 18)

def change(types=(ChangeType.UNKNOWN,), inclusion=Inclusion.UNKNOWN,
           materiality=Materiality.UNKNOWN, source=ChangeSource.CUSTOMER,
           estimate=ChangeEstimate(), commercial=ChangeCommercialImpact()):
    comparison = ScopeComparison(BASE,"request",("S-1",),inclusion,materiality=materiality)
    return ChangeItem("C-1","request",source,date(2026,9,4),types,comparison,
                      ChangeImpact(estimate,commercial))

def test_classifications_remain_distinct():
    assert ChangeType.CLARIFICATION is not ChangeType.SCOPE_CHANGE
    assert ChangeType.DEFECT is not ChangeType.CUSTOMER_ENHANCEMENT
    assert len({ChangeType.DELIVERY_CORRECTION, ChangeType.TECHNICAL_DISCOVERY,
                ChangeType.DEPENDENCY_CHANGE}) == 3

def test_dependency_and_technical_discovery_are_not_customer_creep():
    c=change((ChangeType.TECHNICAL_DISCOVERY,ChangeType.DEPENDENCY_CHANGE),source=ChangeSource.VENDOR)
    assert ChangeType.SCOPE_CHANGE not in c.change_types
    assert c.source is ChangeSource.VENDOR

def test_baseline_comparison_and_explicit_exclusion():
    c=change(inclusion=Inclusion.NO)
    assert c.comparison.baseline.scope_version == "scope-v1"
    assert classify_from_baseline(c.comparison) == (ChangeType.CUSTOMER_ENHANCEMENT,ChangeType.SCOPE_CHANGE)

def test_ambiguous_and_unknown_are_preserved():
    c=change(inclusion=Inclusion.AMBIGUOUS,materiality=Materiality.UNKNOWN)
    assert c.comparison.is_ambiguous
    assert classify_from_baseline(c.comparison)==(ChangeType.REQUIREMENT_CORRECTION,)
    assert c.comparison.materiality is Materiality.UNKNOWN

def test_trivial_change_can_be_absorbed_and_effort_accumulates():
    history=ChangeHistory([BASE])
    for i in range(8):
        c=change((ChangeType.CLARIFICATION,),Inclusion.YES,Materiality.TRIVIAL,
                 estimate=ChangeEstimate(.25,.25,0,"HIGH"))
        c.change_id=str(i); c.decide(ChangeDecision.ABSORB,"tiny tracked goodwill"); history.record(c)
    assert history.cumulative_absorbed_hours == 4
    assert all(c.status is ChangeStatus.ABSORBED for c in history.changes)

def test_delivery_cost_price_and_incremental_contribution_are_distinct():
    commercial=ChangeCommercialImpact(delivery_cost=800,customer_price=1250)
    c=change(commercial=commercial)
    assert c.impact.commercial.delivery_cost != c.impact.commercial.customer_price
    assert c.impact.commercial.incremental_contribution == 450

def test_phase_reject_and_trade_are_available_decisions():
    outcomes=[]
    for decision in (ChangeDecision.PHASE_LATER,ChangeDecision.REJECT,ChangeDecision.TRADE_SCOPE):
        c=change(); c.decide(decision,"recorded option"); outcomes.append((c.decision,c.status))
    assert outcomes == [(ChangeDecision.PHASE_LATER,ChangeStatus.DEFERRED),
                        (ChangeDecision.REJECT,ChangeStatus.REJECTED),
                        (ChangeDecision.TRADE_SCOPE,ChangeStatus.APPROVED)]

def test_approved_change_adds_baseline_without_destroying_original():
    history=ChangeHistory([BASE]); c=change((ChangeType.SCOPE_CHANGE,),Inclusion.NO)
    new=history.approve_new_baseline(c,"scope-v2","req-v2",date(2026,9,29))
    assert history.baselines == [BASE,new]
    assert new.predecessor_scope_version == "scope-v1"
    assert history.baselines[0].scope_version == "scope-v1"

def test_defect_never_automatically_charges_customer():
    c=change((ChangeType.DEFECT,),Inclusion.YES,
             commercial=ChangeCommercialImpact(500,900))
    assert c.customer_charge is None

def test_partner_overrun_is_not_automatically_customer_change():
    assert partner_overrun_type(False,False) is ChangeType.DELIVERY_CORRECTION
    assert partner_overrun_type(False,True) is ChangeType.TECHNICAL_DISCOVERY

def test_project_can_reforecast_after_approved_change():
    history=ChangeHistory([BASE]); c=change((ChangeType.SCOPE_CHANGE,),Inclusion.NO)
    history.approve_new_baseline(c,"scope-v2",forecast=date(2026,9,29))
    assert history.current_baseline.forecast == date(2026,9,29)
    assert BASE.forecast == date(2026,9,15)

def test_records_do_not_execute_change_implementation():
    c=change(); c.decide(ChangeDecision.APPROVE_WITH_PRICE_CHANGE,"approved record")
    assert c.status is ChangeStatus.APPROVED
    assert c.implementation_executed is False
