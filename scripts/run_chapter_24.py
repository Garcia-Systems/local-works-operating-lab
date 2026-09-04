#!/usr/bin/env python3
"""Run Chapter 24's fictional, non-executing change-control exercise."""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_works.changes import *

def section(number: int, title: str) -> None: print(f"\nSECTION {number} — {title}")

print("FICTIONAL TRAINING SCENARIO")
print("NO REAL CUSTOMER CHANGE ORDERS ARE BEING ISSUED")
base = BaselineReference("HF-SCOPE-14-v1", "HF-REQ-21-v1", date(2026, 9, 15), 18)
history = ChangeHistory([base])
section(1, "Starting project baseline")
print("Scope", base.scope_version, "| requirements", base.requirements_version, "| forecast", base.forecast, "| delivery estimate 18h")
section(2, "Change classification framework")
print(", ".join(kind.name for kind in ChangeType)); print("UNKNOWN is retained until evidence supports a fair classification.")

def item(cid, request, source, types, inclusion, materiality, rationale, effort=ChangeEstimate()):
    comparison=ScopeComparison(base, request, ("membership-freeze workflow",), inclusion, new_workflow=inclusion is Inclusion.NO, new_acceptance=inclusion is Inclusion.NO, materiality=materiality, classification_rationale=rationale)
    change=ChangeItem(cid, request, source, date(2026,9,4), types, comparison, ChangeImpact(effort))
    history.record(change); return change

section(3, "Cancellation request")
cancel=item("CH-001", "Members cancel through the same workflow", ChangeSource.CUSTOMER, (ChangeType.CUSTOMER_ENHANCEMENT, ChangeType.SCOPE_CHANGE), Inclusion.NO, Materiality.MAJOR, "Cancellation is explicitly excluded by scope and R-006; it adds policy, workflow and acceptance.", ChangeEstimate(24,5,4,"LOW",("Payment and retention review required",)))
cancel.impact=ChangeImpact(cancel.impact.estimate, ChangeCommercialImpact(3600,6000,500,500), ChangeScheduleImpact(base.forecast,date(2026,9,29),"About two weeks if inserted"), "More acceptance paths", "Authorization, payment and retention policy", "New cancellation cases", "Policy/runbook updates", ("membership platform",))
print(cancel.change_id, [x.name for x in cancel.change_types], "included before", cancel.comparison.included_before.value)
section(4, "Small copy change")
copy=item("CH-002", "Change confirmation wording", ChangeSource.CUSTOMER, (ChangeType.CLARIFICATION,), Inclusion.YES, Materiality.TRIVIAL, "Meaning is unchanged.", ChangeEstimate(.17,.08,0,"HIGH")); copy.decide(ChangeDecision.ABSORB,"Under 30 minutes, no schedule or scope precedent."); print(copy.decision.name, "0.25h tracked, no charge")
section(5, "Defect scenario")
defect=item("CH-003", "Eligible standard case incorrectly enters manager review", ChangeSource.TESTING, (ChangeType.DEFECT,ChangeType.DELIVERY_CORRECTION), Inclusion.YES, Materiality.MATERIAL, "R-002 and AC-01 require bypass.", ChangeEstimate(3,1,.5,"MODERATE")); defect.decide(ChangeDecision.APPROVE_WITHOUT_PRICE_CHANGE,"Correct agreed behavior"); print("DEFECT → DELIVERY_CORRECTION | customer price",defect.customer_charge,"| implementation not executed")
section(6, "Vendor limitation")
vendor=item("CH-004", "Configurable routing unavailable", ChangeSource.VENDOR, (ChangeType.TECHNICAL_DISCOVERY,ChangeType.DEPENDENCY_CHANGE), Inclusion.UNKNOWN, Materiality.MAJOR, "Vendor capability differs from the validation assumption."); vendor.decide(ChangeDecision.REVISIT_SOLUTION,"Compare configuration alternatives before estimate revision"); print([x.name for x in vendor.change_types], "→",vendor.decision.name,"| not customer blame")
section(7, "Ambiguous requirement")
family=item("CH-005", "Family memberships are included", ChangeSource.CUSTOMER, (ChangeType.REQUIREMENT_CORRECTION,), Inclusion.AMBIGUOUS, Materiality.UNKNOWN, "Membership-type wording is unclear; review scope history and policy evidence."); family.decide(ChangeDecision.RETURN_FOR_CLARIFICATION,"Shared evidence review before commercial treatment"); print("included before",family.comparison.included_before.value,"→ fair/shared investigation")
section(8, "Impact analysis")
print("Cancellation: delivery 24h; Local Works 5h; customer 4h; cost $3,600; schedule +14 days; risk: payment/retention/authorization; confidence LOW")
section(9, "Incremental economics")
print("Incremental annual value $500; price $6,000; delivery cost $3,600; contribution $2,400. Value does not justify current insertion.")
section(10, "Options")
print("APPROVE_WITH_PRICE_CHANGE | TRADE_SCOPE | PHASE_LATER | DEFER | REJECT")
section(11, "Customer decision")
cancel.decide(ChangeDecision.PHASE_LATER,"Preserve launch; retain cancellation for a separately discovered Phase 2."); print("Fictional choice:",cancel.decision.name)
section(12, "Baseline update")
print("Deferred: no new baseline. Original remains",history.current_baseline.scope_version,"/",history.current_baseline.requirements_version)
section(13, "Project reforecast")
print("Cancellation causes no reforecast; Chapter 23 forecast remains",history.current_baseline.forecast,". Defect correction is assessed within existing correction responsibility.")
section(14, "Cumulative absorbed changes")
for n in range(3,10):
    c=item(f"CH-{n+3:03}",f"Tiny copy adjustment {n-2}",ChangeSource.CUSTOMER,(ChangeType.CLARIFICATION,),Inclusion.YES,Materiality.TRIVIAL,"Goodwill without precedent",ChangeEstimate(.25,.25,0,"HIGH")); c.decide(ChangeDecision.ABSORB,"Small, tracked exception")
print("Eight changes × 0.5 combined hours =",history.cumulative_absorbed_hours,"hours; review future freebies formally.")
section(15, "Final project state")
print("Current",history.current_baseline.scope_version,"| deferred CH-001 | correction CH-003 | solution review CH-004 | clarification CH-005")
section(16, "Interpretation")
print("Good change control distinguishes legitimate correction from new work before discussing money.")
print("\nFAILURE — EVERYTHING OUT OF SCOPE: monetizing clarification and defects makes change control a weapon.")
print("FAILURE — EVERYTHING INCLUDED: reports, notifications, cancellation, locations and payments make goodwill unlimited scope.")
print("FAILURE — PARTNER EXPANDS PROJECT: demand evidence and alternatives before accepting a portal rebuild or $20k claim.")
print("FAILURE — NO BASELINE: silent requirement edits erase what was approved.")
print("SUCCESS — FAIR CHANGE CONTROL: compare, classify, estimate options, phase a useful idea, and preserve launch.")
print("No implementation, QA, acceptance, deployment, amendment, invoice, signature, or payment was executed.")
