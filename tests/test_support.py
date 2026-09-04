from datetime import date, timedelta
import local_works.support as support
from local_works.support import *

def test_request_types_remain_distinct_and_unknown_survives():
    assert SupportRequestType.DEFECT is not SupportRequestType.ENHANCEMENT
    assert SupportClassification().primary_type is SupportRequestType.UNKNOWN

def test_warranty_links_requirement_and_can_apply_or_remain_uncertain():
    applies=WarrantyAssessment(WarrantyOutcome.WARRANTY_APPLIES,"REQ-1")
    uncertain=WarrantyAssessment(WarrantyOutcome.MORE_EVIDENCE_REQUIRED,uncertainty="change history missing")
    assert applies.related_requirement == "REQ-1"
    assert uncertain.outcome is WarrantyOutcome.MORE_EVIDENCE_REQUIRED

def test_warranty_clock_is_input_not_automatic_decision():
    launch=date(2026,1,1); clock=WarrantyClock(launch,launch,launch+timedelta(days=30),launch+timedelta(days=40))
    assessment=WarrantyAssessment(WarrantyOutcome.LIKELY_WARRANTY,warranty_clock=clock,rationale="possible latent defect")
    assert not clock.within_assumed_period and assessment.outcome is WarrantyOutcome.LIKELY_WARRANTY

def test_customer_and_vendor_issues_are_not_local_works_defects():
    customer=SupportClassification(SupportRequestType.CUSTOMER_ENVIRONMENT_ISSUE,responsibility=Responsibility.CUSTOMER,warranty=WarrantyAssessment(WarrantyOutcome.WARRANTY_DOES_NOT_APPLY,customer_changed_configuration=True))
    vendor=SupportClassification(SupportRequestType.THIRD_PARTY_ISSUE,responsibility=Responsibility.VENDOR)
    assert customer.warranty.outcome is WarrantyOutcome.WARRANTY_DOES_NOT_APPLY
    assert vendor.primary_type is not SupportRequestType.DEFECT

def test_how_to_training_and_configuration_can_be_classified():
    kinds={SupportRequestType.HOW_TO,SupportRequestType.TRAINING,SupportRequestType.CONFIGURATION_ASSISTANCE}
    assert len(kinds)==3

def test_incident_enhancement_and_project_routes():
    def req(kind, security=False): return SupportRequest("x",date.today(),SupportSource.CUSTOMER,"x",SupportClassification(kind),security_sensitive=security)
    assert recommended_action(req(SupportRequestType.INCIDENT)) is SupportAction.ROUTE_TO_INCIDENT_RESPONSE
    assert recommended_action(req(SupportRequestType.ENHANCEMENT)) is SupportAction.QUOTE_ENHANCEMENT
    assert recommended_action(req(SupportRequestType.NEW_PROJECT)) is SupportAction.START_NEW_PROJECT_DISCOVERY
    assert recommended_action(req(SupportRequestType.ACCESS_ISSUE,True)) is SupportAction.ROUTE_TO_INCIDENT_RESPONSE

def test_entitlement_and_commercial_treatments():
    p=SupportPlan("limited",SupportEntitlement.LIMITED_SUPPORT,frozenset({SupportRequestType.ROUTINE_SUPPORT}))
    assert p.includes(SupportRequestType.ROUTINE_SUPPORT) and not p.includes(SupportRequestType.TRAINING)
    assert SupportEntitlement.NONE is not SupportEntitlement.LIMITED_SUPPORT
    assert {CommercialTreatment.NO_CHARGE_WARRANTY,CommercialTreatment.INCLUDED_SUPPORT,CommercialTreatment.BILLABLE_SUPPORT}

def test_effort_goodwill_and_repeated_signal_are_visible():
    h=SupportHistory()
    for i in range(2):
      r=SupportRequest(str(i),date.today(),SupportSource.CUSTOMER,"help",SupportClassification(SupportRequestType.HOW_TO),owner_hours=.25,delivery_partner_hours=.1,estimated_internal_cost=10,documentation_improvement="improve guide")
      h.add(r,SupportDecision(str(i),SupportAction.HANDLE_AS_INCLUDED_SUPPORT,CommercialTreatment.GOODWILL_NO_CHARGE,Responsibility.LOCAL_WORKS,"answer"))
    assert h.total_owner_hours==.5 and h.cumulative_goodwill_owner_hours==.5
    assert h.cumulative_goodwill_partner_hours==.2 and h.cumulative_goodwill_internal_cost==20
    assert h.repeated_request_signal() and h.requests[0].documentation_improvement

def test_dispute_preserves_uncertainty():
    a=WarrantyAssessment(WarrantyOutcome.DISPUTED,uncertainty="vendor/customer accounts conflict")
    r=SupportRequest("d",date.today(),SupportSource.CUSTOMER,"broke",SupportClassification(SupportRequestType.WARRANTY_CANDIDATE,warranty=a))
    assert recommended_action(r) is SupportAction.REQUEST_MORE_INFORMATION

def test_chapter_does_not_implement_incident_execution_or_profitability():
    assert not hasattr(support,"IncidentCommand")
    assert not hasattr(support,"RecurringSupportProfitability")
