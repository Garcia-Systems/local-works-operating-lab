#!/usr/bin/env python3
"""Chapter 19: compare fictional technical estimates without starting delivery."""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_works.estimates import *

SCOPE = "HF-SCOPE-14-v1"
request = EstimateRequest(
    "HF-ER-19-v1", "Membership freeze workflow", "Harbor Fitness (fictional)",
    "Reduce manual, inconsistent membership-freeze handling",
    "Freeze requests cross channels and exceptions require manager judgment.",
    "A consistent, auditable freeze workflow with bounded staff work.",
    "Validate native capability, then configure; integrate only if configuration is inadequate", SCOPE,
    ("member request through recorded disposition", "manager approval of policy exceptions"),
    ("full member portal", "mobile app", "historical migration", "billing-platform replacement"),
    ("request capture", "policy validation", "exception approval", "audit trail"),
    ("standard request is recorded", "exception cannot complete without approval", "staff can reproduce test evidence"),
    ("fictional membership platform", "email notifications"),
    ("single location", "no production access during estimating"),
    ("customer provides test access",),
    ("native rules capability", "API write access and entitlement"),
    ("provide access", "confirm policy", "perform acceptance review"),
    ("scope control", "customer coordination", "acceptance coordination"),
    ("configuration/runbook and handoff notes",), ("happy path, exception, permissions, regression evidence",),
    ("documented, reversible deployment plan",),
    ("customer/Local Works administrative control; transition-ready records",),
)

def component(kind, text, lo, hi, clo, chi):
    return EstimateComponent(kind, text, EstimateRange(lo, hi, "hours"), EstimateRange(clo, chi))

northstar = TechnicalEstimate(
    "Northstar Configuration Specialist (fictional)", request.project, SCOPE, SCOPE,
    "Validate platform capability, then configure", [
        component(ComponentType.DISCOVERY_OR_TECHNICAL_VALIDATION, "Capability validation", 4, 6, 500, 700),
        component(ComponentType.CONFIGURATION, "Bounded workflow configuration", 8, 12, 1000, 1500),
        component(ComponentType.TESTING, "Testing and documentation", 4, 6, 500, 800)],
    date(2026, 9, 4), date(2026, 10, 4), EstimateStatus.CONDITIONAL_ESTIMATE,
    ScopeAlignment.ALIGNED, EstimateRange(16, 24, "hours"), EstimateRange(2000, 3000),
    TimelineEstimate(EstimateRange(1, 2, "weeks"), date(2026, 9, 14), date(2026, 9, 28), ("test access",)),
    EstimateConfidence.MODERATE, "Configuration path is clear; required native feature is not confirmed",
    [EstimateAssumption("Required platform rules exist", "CRITICAL", "UNKNOWN", "Stop and reassess integration"), EstimateAssumption("Customer supplies test access", "HIGH", "UNCONFIRMED", "Start slips")],
    [EstimateExclusion("Historical migration"), EstimateExclusion("Recurring licensing")],
    [EstimateRisk("Native feature may be inadequate", "$500 validation may lead to a revised path", "MEDIUM", "Validate before implementation")],
    technical_discovery_required=True, discovery_cost=EstimateRange(500, 700), customer_effort=EstimateRange(5, 8, "hours"), local_works_effort=EstimateRange(6, 9, "hours"),
    testing="Included: happy path, exception, permissions", documentation="Included: configuration and runbook", deployment="Included after approval", support_handoff="Transition-ready notes")
bridge = TechnicalEstimate(
    "Bridge Integration Freelancer (fictional)", request.project, SCOPE, SCOPE, "API discovery and integration", [
        component(ComponentType.DISCOVERY_OR_TECHNICAL_VALIDATION, "API discovery", 6, 10, 800, 1200), component(ComponentType.INTEGRATION, "Integration/workflow logic", 24, 36, 3200, 4800), component(ComponentType.TESTING, "Tests", 8, 12, 1000, 1500), component(ComponentType.DOCUMENTATION, "Technical handoff", 4, 6, 500, 800)],
    date(2026, 9, 4), date(2026, 10, 4), EstimateStatus.RECEIVED, ScopeAlignment.ALIGNED,
    EstimateRange(42, 64, "hours"), EstimateRange(5500, 8300), TimelineEstimate(EstimateRange(3, 5, "weeks"), date(2026, 9, 9), date(2026, 10, 14), ("API entitlement", "vendor response")),
    EstimateConfidence.LOW, "No API access or documentation reviewed", [EstimateAssumption("Write API and suitable authentication exist", "CRITICAL", "UNKNOWN", "Integration may be impossible" )],
    [EstimateExclusion("Vendor professional-services fees"), EstimateExclusion("Recurring API plan")], [EstimateRisk("Integration may be unnecessary", "Higher complexity than configuration", "MEDIUM", "Use only after native validation")],
    customer_effort=EstimateRange(7, 12, "hours"), local_works_effort=EstimateRange(10, 16, "hours"), testing="Included", documentation="Included", deployment="Included; vendor setup excluded", support_handoff="Source and runbook included")
cedar = TechnicalEstimate(
    "Cedar Small Software Agency (fictional)", request.project, SCOPE, "HF-PORTAL-v1", "Custom member portal", [component(ComponentType.FRONTEND, "Member portal", 60, 90, 9000, 13500), component(ComponentType.BACKEND, "Portal services", 60, 100, 9000, 15000)],
    status=EstimateStatus.NOT_COMPARABLE, scope_alignment=ScopeAlignment.SCOPE_DEVIATION, effort=EstimateRange(120, 190, "hours"), partner_cost=EstimateRange(18000, 28500), timeline=TimelineEstimate(EstimateRange(8, 12, "weeks"), date(2026, 10, 19), date(2027, 1, 11)), confidence=EstimateConfidence.MODERATE, confidence_reason="Custom approach known, platform boundary unknown", assumptions=[EstimateAssumption("A new portal is desired", "CRITICAL", "CONTRADICTED BY SCOPE", "Remove most proposed work")], exclusions=[EstimateExclusion("Platform licensing")], risks=[EstimateRisk("Over-solves bounded workflow", "Cost and operational burden", "HIGH", "Re-estimate approved scope")], customer_effort=EstimateRange(20, 35, "hours"), local_works_effort=EstimateRange(25, 40, "hours"), testing="Portal testing included", documentation="Technical documentation included", deployment="Included", support_handoff="Agency support option")
self_delivery = TechnicalEstimate(
    "Local Works self delivery (fictional exercise)", request.project, SCOPE, SCOPE, "Learn, validate, and configure internally", [component(ComponentType.DISCOVERY_OR_TECHNICAL_VALIDATION, "Learning/validation", 10, 18, 0, 0), component(ComponentType.CONFIGURATION, "Configuration and evidence", 18, 30, 0, 0)], scope_alignment=ScopeAlignment.ALIGNED, effort=EstimateRange(28, 48, "hours"), partner_cost=EstimateRange(0, 0), timeline=TimelineEstimate(EstimateRange(6, 10, "weeks"), date(2026, 9, 7), date(2026, 11, 16), ("six owner hours/week",)), confidence=EstimateConfidence.LOW, confidence_reason="Platform skill and calendar capacity are uncertain", assumptions=[EstimateAssumption("Owner can sustain six hours/week", "HIGH", "UNKNOWN", "Customer work and sales are displaced")], exclusions=[EstimateExclusion("Owner opportunity cost is not a cash partner cost")], risks=[EstimateRisk("Owner bottleneck", "Displaces sales, coordination, and other customer work", "HIGH")], customer_effort=EstimateRange(6, 10, "hours"), local_works_effort=EstimateRange(34, 57, "hours"), testing="Owner performs", documentation="Owner performs", deployment="UNKNOWN pending validation", support_handoff="Low external dependency; owner concentration remains")
estimates = [northstar, bridge, cedar, self_delivery]
questions = {
 northstar.candidate: ("Is documentation included?", "Confirm handoff baseline", "Yes: configuration record and runbook are included.", "No adjustment."),
 bridge.candidate: ("Does this include vendor API setup?", "Expose third-party setup", "No; allow fictional $500–$900 if required.", "Add setup range in normalization."),
 cedar.candidate: ("Which features are outside approved scope?", "Reconcile scope", "Portal accounts, dashboard, profile, and mobile-responsive self-service are additions.", "Still NOT_COMPARABLE; request a bounded revision."),
 self_delivery.candidate: ("What owner work would be displaced?", "Expose non-cash burden", "Sales, customer coordination, and method development.", "Keep owner effort visible; do not call it free."),
}
for e in estimates:
    q = questions[e.candidate]
    e.add_clarification(EstimateClarification(q[0], q[1], q[2], q[3], ClarificationStatus.ANSWERED))
comparison = EstimateComparison(request, estimates)
normal = {
 northstar.candidate: comparison.normalize(northstar.candidate),
 bridge.candidate: comparison.normalize(bridge.candidate, (NormalizationAdjustment("Vendor API setup", EstimateRange(500, 900), "Excluded implementation setup"),)),
 cedar.candidate: comparison.normalize(cedar.candidate),
 self_delivery.candidate: comparison.normalize(self_delivery.candidate),
}
decisions = [
 EstimateDecision(northstar.candidate, EstimateDecisionType.SELECT_FOR_TECHNICAL_DISCOVERY, "A bounded $500–$700 validation reduces the decisive native-capability uncertainty."),
 EstimateDecision(bridge.candidate, EstimateDecisionType.KEEP_AS_BACKUP, "Use the integration path only if native capability is inadequate."),
 EstimateDecision(cedar.candidate, EstimateDecisionType.REQUEST_REVISED_ESTIMATE, "The portal changes scope and cannot be directly compared."),
 EstimateDecision(self_delivery.candidate, EstimateDecisionType.DO_NOT_SELECT, "Low cash price does not outweigh 34–57 owner hours and capacity risk."),
]
print("CHAPTER 19 — REQUEST AND COMPARE TECHNICAL ESTIMATES\nPART V — ASSEMBLE THE DELIVERY SYSTEM")
print("FICTIONAL TRAINING SCENARIO\nNO REAL DELIVERY ESTIMATES WERE REQUESTED OR RECEIVED")
print(f"\nSECTION 1 — Common estimate request\n{request.request_version}; BASELINE_SCOPE_VERSION={request.scope_version}\nProblem: {request.problem_summary}\nSolution: {request.selected_solution_path}\nIncluded: {'; '.join(request.included_workflow)}\nExcluded: {'; '.join(request.excluded_workflow)}\nAcceptance: {'; '.join(request.acceptance_criteria)}\nUnknowns: {'; '.join(request.unresolved_technical_questions)}\nTesting: {'; '.join(request.expected_testing)}\nDocumentation: {'; '.join(request.expected_documentation)}\nContinuity: {'; '.join(request.continuity_expectations)}")
print("\nSECTION 2 — Estimates received")
for e in estimates: print(f"{e.candidate}: {e.approach}; raw partner cost ${e.partner_cost.lower:,.0f}–${e.partner_cost.upper:,.0f}; status={e.status.name}")
print("\nSECTION 3 — Scope alignment")
for e in estimates: print(f"{e.candidate}: baseline={e.baseline_scope_version}; estimated={e.estimated_scope_version}; {e.scope_alignment.name}")
print("\nSECTION 4 — Assumptions")
for e in estimates: print(e.candidate + ": " + "; ".join(f"{a.statement} [{a.evidence_status}] → {a.impact_if_false}" for a in e.assumptions))
print("\nSECTION 5 — Exclusions")
for e in estimates: print(e.candidate + ": " + "; ".join(x.statement for x in e.exclusions))
print("\nSECTION 6 — Cost components")
for e in estimates: print(f"{e.candidate}: partner={e.partner_cost}; discovery={e.discovery_cost or 'none separate'}; third-party setup={e.third_party_implementation_cost or 'UNKNOWN/none stated'}; customer={e.customer_effort}; Local Works={e.local_works_effort}")
print("\nSECTION 7 — Effort and timeline")
for e in estimates: print(f"{e.candidate}: effort={e.effort.lower}–{e.effort.upper} hours; elapsed={e.timeline.duration.lower}–{e.timeline.duration.upper} weeks; earliest={e.timeline.earliest_start}; completion={e.timeline.expected_completion}")
print("\nSECTION 8 — Estimate confidence")
for e in estimates: print(f"{e.candidate}: {e.confidence.name} — {e.confidence_reason}")
print("\nSECTION 9 — Estimate quality\nNorthstar: STRONG scope/assumption clarity, ADEQUATE confidence. Bridge: STRONG technical reasoning, UNCERTAIN API basis. Cedar: STRONG custom detail, WEAK scope alignment. Self: STRONG burden disclosure, LOW technical confidence. No magic score or price proxy is used.")
print("\nSECTION 10 — Clarification round")
for e in estimates:
    c=e.clarifications[-1]; print(f"{e.candidate}: Q {c.question} A {c.response} Impact: {c.impact}; {c.status.name}")
print("\nSECTION 11 — Normalization")
for name,n in normal.items(): print(f"{name}: ${n.normalized_delivery_cost.lower:,.0f}–${n.normalized_delivery_cost.upper:,.0f}; comparable={n.comparable}; adjustments={'; '.join(a.category for a in n.adjustments) or 'none'}")
print("\nSECTION 12 — Low-bid trap\nRaw A=$2,000, excluding testing, deployment, documentation, vendor setup. Add $1,000+$700+$600+$500: normalized A=$4,800. Complete B=$4,000. RAW BID PRICE CAN BE MISLEADING; the lowest bid can still win when truly comparable.")
print("\nSECTION 13 — Over-solution trap\nCedar's custom portal adds accounts, dashboards, profile, and self-service beyond Chapter 14. High cost is not proof of quality or safety; it is NOT COMPARABLE until scope is revised.")
print("\nSECTION 14 — Self-delivery burden\n$0 partner cash does not mean free: 28–48 technical hours plus coordination, 34–57 Local Works hours total, six-to-ten elapsed weeks, skill uncertainty, and displaced sales/customer work.")
print("\nSECTION 15 — Partner fit carry-forward\nNorthstar: strong platform/documentation fit, narrow integration depth/key-person risk. Bridge: strong integration, platform fit uncertain. Cedar: capable custom team, wrong-sized and continuity/subcontracting concerns. Self: strong context, uncertain expertise and capacity.")
print("\nSECTION 16 — Final estimate comparison")
for e in estimates: print(f"{e.candidate}: fit={e.scope_alignment.name}; normalized={normal[e.candidate].normalized_delivery_cost}; timeline={e.timeline.duration}; confidence={e.confidence.name}; risk={e.risks[0].description}; docs={e.documentation}; continuity={e.support_handoff}")
print("\nSECTION 17 — Decision")
for d in decisions: print(f"{d.decision.name}: {d.candidate} — {d.rationale}")
print("No delivery is selected or started. Scope and solution remain intact pending validation; an adverse result may trigger REVISIT_SOLUTION or REVISIT_SCOPE.")
print("\nSECTION 18 — Interpretation\nThe cheapest estimate is only useful if it estimates the work Local Works actually intends to buy. PAYING FOR UNCERTAINTY REDUCTION CAN BE CHEAPER THAN PAYING FOR BAD CERTAINTY. 47.25 hours without API access, documentation, or migration knowledge is false precision, not confidence. Equal $5,000 bids with HIGH versus LOW confidence are not equal estimates.")
