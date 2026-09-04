#!/usr/bin/env python3
"""Run the fictional Chapter 22 translation exercise."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.projects import OpenQuestion, QuestionCategory, QuestionStatus, Requirement, RequirementPriority, RequirementSource, RequirementStatus, RequirementType
from local_works.translation import *


def section(number: int, title: str) -> None:
    print(f"\nSECTION {number} — {title}")


requirements = [
    Requirement("R-001", "Determine whether confirmed Harbor freeze eligibility rules can be preserved.", RequirementType.BUSINESS_RULE, RequirementPriority.MUST, RequirementSource.SCOPE, "HF-SCOPE-14-v1", status=RequirementStatus.READY_FOR_IMPLEMENTATION),
    Requirement("R-002", "Determine whether routine requests avoid staff re-entry.", RequirementType.FUNCTIONAL, RequirementPriority.MUST, RequirementSource.ACCEPTANCE_CRITERIA, "HF-SCOPE-14-v1 acceptance", acceptance_linkage=("AC-01",), status=RequirementStatus.READY_FOR_IMPLEMENTATION),
    Requirement("R-003", "Exceptions route to an authorized staff decision and record status.", RequirementType.FUNCTIONAL, RequirementPriority.MUST, RequirementSource.WORKFLOW, "HF-WORKFLOW-09", acceptance_linkage=("AC-01",), status=RequirementStatus.NEEDS_CLARIFICATION),
    Requirement("R-004", "Use separate least-privilege access; do not share personal passwords.", RequirementType.ACCESS, RequirementPriority.MUST, RequirementSource.SCOPE, "HF-DELIVERY-CONTROL-20", status=RequirementStatus.READY_FOR_IMPLEMENTATION),
]
statements = [
    BusinessStatement("S-001", "We want members to stop having to call for routine freezes.", "Operations Manager", "Kickoff notes", evidence_reference="HF-KICKOFF-21", interpretation="Routine eligible requests should not require a phone call."),
    BusinessStatement("S-002", "Managers only need to review unusual freeze requests.", "Membership Lead", "Workflow review", evidence_reference="HF-WORKFLOW-09", interpretation="Confirmed exceptions require authorized review."),
    BusinessStatement("S-003", "Members should know whether the freeze worked.", "Membership Lead", "Kickoff notes", interpretation="Communicate accurate final or pending status."),
    BusinessStatement("S-004", "Could members cancel there too?", "Stakeholder", "Kickoff parking lot", interpretation="Adjacent outcome, excluded from current scope."),
]
intents = [
    BusinessIntent("S-001", "Reduce unnecessary staff intervention while preserving policy", "Members and staff", "WF-FUTURE-01", "HF-KICKOFF-21"),
    BusinessIntent("S-002", "Preserve accountable review only for exceptions", "Managers and members", "WF-FUTURE-02", "HF-WORKFLOW-09"),
    BusinessIntent("S-003", "Reduce uncertainty and repeat contact through accurate status", "Members", "WF-FUTURE-03"),
    BusinessIntent("S-004", "Reduce contact for an adjacent, unapproved workflow", "Members and staff", "OUT_OF_SCOPE"),
]
behaviors = [
    WorkflowBehavior("WB-01", "Member submits required information; routine/exception path follows confirmed rules", ("MEMBER", "STAFF"), "HF-WORKFLOW-09"),
    WorkflowBehavior("WB-02", "Authorized manager decides confirmed exceptions; standard cases avoid manager queue", ("MANAGER",), "HF-WORKFLOW-09"),
    WorkflowBehavior("WB-03", "Member receives accurate success, pending, or failure status", ("MEMBER", "STAFF"), "HF-WORKFLOW-09"),
]
needs = [
    TechnicalNeed("TN-001", "Determine whether existing capability collects required freeze information and applies or routes confirmed eligibility behavior", ("R-001", "R-002"), ("WB-01",), (DataNeed("membership type", "Evaluate confirmed policy", DataSource.EXISTING_PLATFORM, (DataAction.READ,)),)),
    TechnicalNeed("TN-002", "Distinguish standard and exception paths using confirmed policy and authorized review", ("R-003",), ("WB-02",)),
    TechnicalNeed("TN-003", "Communicate accurate request status and expose failed writes", ("R-002",), ("WB-03",)),
    TechnicalNeed("TN-004", "Validate business-level least-privilege behavior using available platform controls", ("R-004",)),
]
business_questions = [OpenQuestion("BQ-001", "Which membership types and conditions require manager approval?", QuestionCategory.BUSINESS_RULE, "Harbor Operations Manager", "Delivery must not invent policy", True)]
technical_questions = [
    TechnicalQuestion("TQ-001", "Can the platform expose membership type and record freeze status?", "Determines configuration viability", "R-001", "BR-03", "Delivery technical lead", True),
    TechnicalQuestion("TQ-002", "Can exceptions route to authorized manager review?", "Determines R-003 viability", "R-003", "BR-04", "Delivery technical lead", True),
    TechnicalQuestion("TQ-003", "Can existing capability communicate status?", "Determines truthful confirmation path", "R-002", owner="Delivery technical lead", blocking=True),
    TechnicalQuestion("TQ-004", "Is sandbox/test mode available?", "Safe validation access", "R-004", owner="Harbor technical contact", blocking=True),
]
constraints = [TechnicalConstraint("TC-01", "Configuration-first paid validation; custom portal is excluded", "HF-SCOPE-14-v1", "SCOPE", True), TechnicalConstraint("TC-02", "Platform write, routing, notification, and sandbox capability are UNKNOWN", "HF-EST-19-NORTHSTAR")]
tasks = [
    TechnicalTask("TT-001", "Validate platform freeze capability", "Test collection/read/write capability", TechnicalTaskCategory.VALIDATE_CAPABILITY, "Capability, evidence, limitations, and UNKNOWNs recorded", ("R-001", "R-002"), ("WB-01",), ("safe test access",)),
    TechnicalTask("TT-002", "Map confirmed business rules", "Compare confirmed rules with configurable behavior", TechnicalTaskCategory.CONFIGURE, "Every confirmed rule is supported, unsupported, or UNKNOWN with evidence", ("R-001",), dependencies=("BQ-001 answered",)),
    TechnicalTask("TT-003", "Validate exception routing", "Exercise standard and exception paths", TechnicalTaskCategory.VALIDATE_CAPABILITY, "Both path results and authorization behavior recorded", ("R-003",), ("WB-02",), ("BR-04 confirmed",)),
    TechnicalTask("TT-004", "Validate member notification behavior", "Observe success and failure status behavior", TechnicalTaskCategory.VALIDATE_CAPABILITY, "Available status behavior and truthful failure outcome evidenced", ("R-002",), ("WB-03",), ("notification capability validated",)),
    TechnicalTask("TT-005", "Document capability gaps", "Record requirement impact and escalation", TechnicalTaskCategory.DOCUMENT, "Every discovered gap has evidence and review destination", ("R-001", "R-002", "R-003", "R-004")),
    TechnicalTask("TT-006", "Prepare recommendation if configuration is insufficient", "Compare proportional paths without starting implementation", TechnicalTaskCategory.INVESTIGATE, "Options and scope/solution/estimate impacts are presented", ("R-001", "R-002", "R-003"), dependencies=("TT-001 through TT-005",)),
]
records = [TranslationRecord("TR-001", statements[0], intents[0], ("R-001", "R-002"), technical_needs=(needs[0],), technical_questions=(technical_questions[0],), technical_tasks=(tasks[0], tasks[1]), status=TranslationStatus.NEEDS_TECHNICAL_CLARIFICATION)]

print("FICTIONAL TRAINING SCENARIO\nNO REAL CUSTOMER SYSTEM IS BEING CHANGED")
section(1, "Project state"); print("Current phase: paid technical validation\nScope version: HF-SCOPE-14-v1\nRequirements baseline: HF-REQ-21-v0.1\nDelivery path: configuration-first; no custom portal")
section(2, "Customer statements"); [print(f"{s.statement_id}: {s.wording} — {s.speaker_role}") for s in statements]
section(3, "Business intent"); [print(f"{i.statement_id}: {i.desired_outcome}") for i in intents]
section(4, "Requirements linkage"); print("S-001 → R-001/R-002; S-002 → R-003/BR-04; S-003 → R-002; S-004 → OUT_OF_SCOPE")
section(5, "Workflow behaviors"); [print(f"{b.behavior_id}: {b.description}") for b in behaviors]
section(6, "Technical needs"); [print(f"{n.need_id}: {n.statement}") for n in needs]
section(7, "Business questions"); [print(f"{q.question_id}: {q.question} owner={q.owner} answer={q.answer}") for q in business_questions]
section(8, "Technical questions"); [print(f"{q.question_id}: {q.question} owner={q.owner} answer={q.answer}") for q in technical_questions]
section(9, "Technical constraints"); [print(f"{c.constraint_id}: {c.statement}") for c in constraints]
section(10, "Technical tasks"); [print(f"{t.task_id} {t.category.name}: {t.title}; DONE WHEN {t.done_condition}") for t in tasks]
section(11, "Traceability"); print("S-001 → R-002 → TN-001 → TT-001 → T-001/AC-01\nS-002 → R-003/BR-04 → TN-002 → TT-003 → T-002,T-003/AC-01\nS-003 → R-002 → TN-003 → TT-004 → T-004/AC-01")
section(12, "Translation gap"); print("Requirement: unresolved failed writes visible to staff; no linked task → TRANSLATION GAP")
section(13, "Gold-plating scenario"); extra = TechnicalTask("TT-X", "Add real-time analytics dashboard", "Add WebSockets and warehouse", TechnicalTaskCategory.IMPLEMENT, "Dashboard streams status", ()); print("Developer proposal:", extra.title, "→", "NO BUSINESS JUSTIFICATION" if unjustified_technical_work([extra]) else "JUSTIFIED"); print("Feature-as-requirement: 'We need an app' → 'Build mobile app' = INVALID TRANSLATION\nAutomatic processing of all freezes conflicts with manager exceptions = BUSINESS INTENT LOST\nMandating Laravel/Redis/PostgreSQL/React/AWS for configuration = UNJUSTIFIED TECHNICAL CONTROL")
section(14, "Nonfunctional translation"); print("reliable → failures visible; no false success, silent loss, or accidental duplicate\nsecure → own-record access, authorized approval, revocable access, no exposed secrets\neasy to use → labeled inputs, keyboard operation, understandable errors; no unsupported compliance claim")
section(15, "Vendor limitation scenario"); print("No exception routing and no adequate configuration alternative →", vendor_limitation_outcome(need_in_scope=True, alternate_within_solution=False, solution_still_viable=False).name, "(scope review/customer decision if requirement changes)")
section(16, "Translation readiness"); print(readiness(records, business_questions, technical_questions).name)
section(17, "Interpretation"); print("Translation succeeds when the technical team can implement the intended business behavior without inventing business policy or unnecessary technology. Current validation does not implement or modify a production system.")
