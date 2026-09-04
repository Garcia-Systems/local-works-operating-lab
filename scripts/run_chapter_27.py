#!/usr/bin/env python3
"""Run Chapter 27's fictional post-launch boundary exercise."""
from datetime import date, timedelta
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_works.support import *


def main() -> None:
    print("FICTIONAL TRAINING SCENARIO")
    print("NO REAL CUSTOMER SUPPORT REQUESTS ARE BEING HANDLED")
    launch = date(2026, 9, 22)
    plan = SupportPlan("Harbor limited handoff", SupportEntitlement.LIMITED_SUPPORT,
        frozenset({SupportRequestType.HOW_TO, SupportRequestType.CONFIGURATION_ASSISTANCE}), 2,
        "Acknowledge and begin triage during ordinary working time; resolution is separate",
        ("new workflows", "extended training"), "Local Works coordinates when appropriate",
        "Not included", "Fictional 30-day handoff", SupportPlanStatus.ACTIVE_SIMULATED)
    print("\nSECTION 1 — Starting post-launch state")
    print("Launch:", launch, "| closeout: MEASUREMENT_PENDING")
    print("Warranty assumption: hypothetical, configurable 30 days; operational, not legal")
    print("Support entitlement:", plan.entitlement.name, "| capacity: 2 fictional hours")
    print("\nSECTION 2 — Support classification framework")
    print("Contact → triage → classify → check warranty/support/scope → responsibility → commercial treatment → action → learning")
    print("Types:", ", ".join(t.name for t in SupportRequestType))

    likely = WarrantyAssessment(WarrantyOutcome.LIKELY_WARRANTY, "HF-REQ-21-v1",
        "eligible freezes bypass manager review", "eligible freezes bypassed review at delivery",
        "eligible freezes bypass manager review", True, False, False, True,
        WarrantyClock(launch, launch, launch + timedelta(days=30), launch + timedelta(days=2)),
        ("accepted requirement", "no customer or vendor change identified"))
    cases = [
      ("SECTION 3 — Harbor defect request", SupportRequest("HF-SUP-01", date(2026,9,24), SupportSource.CUSTOMER,
       "Eligible freeze routed to manager", SupportClassification(SupportRequestType.DEFECT, responsibility=Responsibility.LOCAL_WORKS, warranty=likely), SupportPriority.HIGH, owner_hours=1.5),
       CommercialTreatment.NO_CHARGE_WARRANTY, SupportAction.HANDLE_AS_WARRANTY, "coordinate correction and communicate progress"),
      ("SECTION 4 — How-to/configuration request", SupportRequest("HF-SUP-02", date(2026,9,25), SupportSource.CUSTOMER,
       "How do I change confirmation wording?", SupportClassification(SupportRequestType.HOW_TO,(SupportRequestType.CONFIGURATION_ASSISTANCE,),Responsibility.SHARED), owner_hours=.25, documentation_improvement="add confirmation-text steps"),
       CommercialTreatment.INCLUDED_SUPPORT, SupportAction.HANDLE_AS_INCLUDED_SUPPORT, "answer and improve runbook"),
      ("SECTION 5 — Enhancement request", SupportRequest("HF-SUP-03", date(2026,9,26), SupportSource.CUSTOMER,
       "Can members cancel online too?", SupportClassification(SupportRequestType.NEW_PROJECT,(SupportRequestType.ENHANCEMENT,),Responsibility.LOCAL_WORKS), owner_hours=.5, expansion_signal="cancellation discovery"),
       CommercialTreatment.NEW_PROJECT_DISCOVERY, SupportAction.START_NEW_PROJECT_DISCOVERY, "investigate before pricing"),
      ("SECTION 6 — Vendor issue", SupportRequest("HF-SUP-04", date(2026,9,27), SupportSource.CUSTOMER,
       "Platform notification stopped", SupportClassification(SupportRequestType.THIRD_PARTY_ISSUE,responsibility=Responsibility.VENDOR,evidence=("no Local Works change",)), SupportPriority.HIGH, owner_hours=.75),
       CommercialTreatment.VENDOR_HANDLES, SupportAction.ESCALATE_TO_VENDOR, "Local Works coordinates; vendor owns platform correction"),
      ("SECTION 7 — Customer configuration issue", SupportRequest("HF-SUP-05", date(2026,9,28), SupportSource.CUSTOMER,
       "Workflow broke after a rule edit", SupportClassification(SupportRequestType.CUSTOMER_ENVIRONMENT_ISSUE,(SupportRequestType.CONFIGURATION_ASSISTANCE,),Responsibility.CUSTOMER,
       WarrantyAssessment(WarrantyOutcome.WARRANTY_DOES_NOT_APPLY, customer_changed_configuration=True,evidence=("configuration audit shows manager edit",))), owner_hours=.75),
       CommercialTreatment.BILLABLE_SUPPORT, SupportAction.HANDLE_AS_BILLABLE_SUPPORT, "confirm evidence and obtain approval for assistance"),
      ("SECTION 8 — Security-sensitive request", SupportRequest("HF-SUP-06", date(2026,9,29), SupportSource.CUSTOMER,
       "Staff can see data they should not see", SupportClassification(SupportRequestType.INCIDENT,(SupportRequestType.ACCESS_ISSUE,),Responsibility.UNDETERMINED), SupportPriority.URGENT, security_sensitive=True, owner_hours=.5),
       CommercialTreatment.INCLUDED_SUPPORT, SupportAction.ROUTE_TO_INCIDENT_RESPONSE, "route urgently to Chapter 28 process; do not diagnose here"),
      ("SECTION 9 — Goodwill support", SupportRequest("HF-SUP-07", date(2026,9,30), SupportSource.CUSTOMER,
       "Where is the harmless vendor display setting?", SupportClassification(SupportRequestType.CONFIGURATION_ASSISTANCE,responsibility=Responsibility.VENDOR), SupportPriority.LOW, owner_hours=1/6, estimated_internal_cost=15),
       CommercialTreatment.GOODWILL_NO_CHARGE, SupportAction.HANDLE_AS_INCLUDED_SUPPORT, "one-time goodwill; record rather than normalize"),
    ]
    history=SupportHistory()
    for heading, request, treatment, action, next_action in cases:
        print("\n"+heading); print(request.request_id, request.classification.primary_type.name, request.classification.responsibility.name, treatment.name, "→", action.name)
        history.add(request, SupportDecision(request.request_id, action,treatment,request.classification.responsibility,next_action))
    disputed = SupportRequest("HF-SUP-08", date(2026,10,1), SupportSource.CUSTOMER,
        "This broke after the project", SupportClassification(SupportRequestType.WARRANTY_CANDIDATE,
        responsibility=Responsibility.UNDETERMINED, warranty=WarrantyAssessment(
        WarrantyOutcome.MORE_EVIDENCE_REQUIRED, "HF-REQ-21-v1",
        evidence=("customer report", "partner vendor-change claim"), uncertainty="conflicting accounts")),
        SupportPriority.HIGH, owner_hours=.5)
    history.add(disputed, SupportDecision("HF-SUP-08", SupportAction.REQUEST_MORE_INFORMATION,
        CommercialTreatment.PENDING_CLASSIFICATION, Responsibility.UNDETERMINED,
        "collect timeline, changes, requirement, and reports"))
    print("\nSECTION 10 — Cumulative support effort")
    print(f"Local Works owner time: {history.total_owner_hours:.2f}h; goodwill: {len(history.goodwill_requests)} request / {history.cumulative_goodwill_owner_hours:.2f}h / $15 internal estimate")
    print("\nSECTION 11 — Repeated-request signal")
    print("A repeated confirmation how-to would trigger documentation/usability/training review—not endless replies.")
    print("\nSECTION 12 — Disputed responsibility")
    print("HF-SUP-08: vendor claims API change; customer says project broke → MORE_EVIDENCE_REQUIRED; collect timeline, changes, requirement and reports.")
    print("\nSECTION 13 — Support decision summary")
    for d in history.decisions: print(d.request_id, d.action.name, d.responsibility.name, d.commercial_treatment.name, "—", d.next_action)
    print("\nSECTION 14 — Interpretation")
    print("Good post-launch ownership means the customer knows where to go, while Local Works still protects its time, economics, and scope.")

if __name__ == "__main__": main()
