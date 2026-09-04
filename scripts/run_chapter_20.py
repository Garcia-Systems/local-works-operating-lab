#!/usr/bin/env python3
"""Chapter 20: test fictional delivery control without starting kickoff."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_works.delivery_risk import *

controls = [
 AssetControl(DeliveryAsset("Membership platform admin", AssetType.VENDOR_ACCOUNT, "Harbor Fitness"), ControlParty.CUSTOMER, (ControlParty.CUSTOMER,), (ControlParty.LOCAL_WORKS,), "Customer account recovery with vendor", "Customer can replace delegated administrators", ControlStatus.CONTROLLED),
 AssetControl(DeliveryAsset("Technical-discovery notes", AssetType.DOCUMENTATION, "Not assessed; legal advice excluded"), ControlParty.LOCAL_WORKS, (ControlParty.LOCAL_WORKS,), (ControlParty.CUSTOMER,), "Customer copy in project handoff", "Portable files", ControlStatus.CONTROLLED),
 AssetControl(DeliveryAsset("Configuration record", AssetType.DEPLOYMENT_CONFIGURATION), ControlParty.SHARED, (ControlParty.CUSTOMER, ControlParty.DELIVERY_PARTNER), (ControlParty.LOCAL_WORKS,), "Partner records observations before validation closes", "Common document format", ControlStatus.NEEDS_ACTION),
 AssetControl(DeliveryAsset("Source repository", AssetType.SOURCE_REPOSITORY), ControlParty.UNKNOWN, status=ControlStatus.NOT_APPLICABLE, notes="No custom implementation selected"),
 AssetControl(DeliveryAsset("Decision log", AssetType.DECISION_LOG), ControlParty.LOCAL_WORKS, (ControlParty.LOCAL_WORKS,), (ControlParty.CUSTOMER,), "Customer receives current export", "Portable file", ControlStatus.CONTROLLED),
]
responsibilities = [
 ResponsibilityAssignment(ResponsibilityType.BUSINESS_DECISION, ControlParty.CUSTOMER, (ControlParty.CUSTOMER,), (ControlParty.LOCAL_WORKS, ControlParty.DELIVERY_PARTNER)),
 ResponsibilityAssignment(ResponsibilityType.SCOPE_AUTHORITY, ControlParty.LOCAL_WORKS, (ControlParty.LOCAL_WORKS,), (ControlParty.CUSTOMER,)),
 ResponsibilityAssignment(ResponsibilityType.TECHNICAL_DESIGN, ControlParty.DELIVERY_PARTNER, (ControlParty.DELIVERY_PARTNER,), (ControlParty.LOCAL_WORKS, ControlParty.THIRD_PARTY_VENDOR)),
 ResponsibilityAssignment(ResponsibilityType.CUSTOMER_COMMUNICATION, ControlParty.LOCAL_WORKS, (ControlParty.LOCAL_WORKS,), informed=(ControlParty.CUSTOMER,)),
 ResponsibilityAssignment(ResponsibilityType.TEST_EXECUTION, ControlParty.LOCAL_WORKS, (ControlParty.DELIVERY_PARTNER,), (ControlParty.CUSTOMER,)),
 ResponsibilityAssignment(ResponsibilityType.CUSTOMER_ACCEPTANCE, ControlParty.CUSTOMER, (ControlParty.CUSTOMER,), (ControlParty.LOCAL_WORKS,)),
 ResponsibilityAssignment(ResponsibilityType.VENDOR_ESCALATION, ControlParty.LOCAL_WORKS, (ControlParty.LOCAL_WORKS,), (ControlParty.DELIVERY_PARTNER, ControlParty.THIRD_PARTY_VENDOR)),
 ResponsibilityAssignment(ResponsibilityType.MONITORING, None, (), notes="Not needed for validation; must be assigned before any later integration launch"),
]
knowledge = [
 KnowledgeArtifact("Customer policy rules", KnowledgeCategory.BUSINESS_RULES, True, ControlParty.CUSTOMER, True, "HF scope/project files", ContinuityResult.RECOVERABLE),
 KnowledgeArtifact("Capability findings and configuration observations", KnowledgeCategory.CONFIGURATION, True, ControlParty.DELIVERY_PARTNER, False, "Planned validation report", ContinuityResult.RECOVERABLE_WITH_EFFORT),
 KnowledgeArtifact("Test evidence", KnowledgeCategory.TESTING, True, ControlParty.DELIVERY_PARTNER, False, "Planned shared project files", ContinuityResult.RECOVERABLE_WITH_EFFORT),
 KnowledgeArtifact("Decision context", KnowledgeCategory.DECISION_HISTORY, True, ControlParty.LOCAL_WORKS, True, "Decision log", ContinuityResult.RECOVERABLE),
]
access = [
 AccessRecord("Membership platform test environment", ControlParty.CUSTOMER, "Administrator", "Authorize and recover access", revocation_path="Customer/vendor account recovery", status=AccessStatus.ACTIVE),
 AccessRecord("Membership platform test environment", ControlParty.DELIVERY_PARTNER, "Least privilege, temporary", "Capability validation", expected_revocation="End of validation", revocation_path="Customer administrator removes identity"),
 AccessRecord("Project files", ControlParty.LOCAL_WORKS, "Editor", "Coordinate scope, evidence, and decisions", revocation_path="Organizational administrator"),
]
dependencies = [ThirdPartyDependency("Fictional membership platform", "Critical", ControlParty.CUSTOMER, "Customer-authorized test access", "Customer support channel; Local Works coordinates", "Native rule and API capability remain unverified", "Validation cannot conclude", "Pause and obtain vendor answer; integration remains a backup, not an assumed fallback", "OPEN")]
decisions = [
 DecisionRecord("Buy bounded technical validation", "Chapter 19 estimates depend on unknown native capability", "A $500–$700 validation reduces the decisive uncertainty before implementation", ControlParty.LOCAL_WORKS, "HF-ER-19-v1"),
 DecisionRecord("Keep integration specialist as backup", "Native configuration may be inadequate", "Do not buy integration complexity unless validation supports the need", ControlParty.LOCAL_WORKS, "HF-SCOPE-14-v1"),
 DecisionRecord("Exclude cancellation and full portal", "The sold scope concerns membership freezes", "Preserve the approved workflow boundary", ControlParty.CUSTOMER, "HF-SCOPE-14-v1"),
]
partner_check = [ContinuityRequirement("Findings retained?", ContinuityResult.RECOVERABLE_WITH_EFFORT, "Required validation report is planned, not delivered"), ContinuityRequirement("Requirements and decisions retained?", ContinuityResult.RECOVERABLE, "Local Works project record"), ContinuityRequirement("Vendor references and open questions retained?", ContinuityResult.RECOVERABLE_WITH_EFFORT, "Shared notes required")]
lw_check = [ContinuityRequirement("Customer can identify account and provider?", ContinuityResult.RECOVERABLE, "Customer controls platform account"), ContinuityRequirement("Customer receives findings, decisions, and support path?", ContinuityResult.RECOVERABLE_WITH_EFFORT, "Handoff/export required")]
risks = [
 DeliveryRisk("Validation findings could remain with one specialist", RiskCategory.KNOWLEDGE_CONCENTRATION, RiskSeverity.HIGH, "Report and evidence not yet delivered", "Make shared report, evidence, open questions, and vendor references a completion condition", ControlParty.LOCAL_WORKS, True),
 DeliveryRisk("Vendor capability and support response are uncertain", RiskCategory.THIRD_PARTY_DEPENDENCY, RiskSeverity.MEDIUM, "No platform evidence reviewed", "Use bounded validation and retain integration path", ControlParty.LOCAL_WORKS, False, RiskStatus.MONITORED),
 DeliveryRisk("Post-launch monitoring is unowned", RiskCategory.RESPONSIBILITY_GAP, RiskSeverity.LOW, "No implementation or launch selected", "Assign if a later integration reaches launch", ControlParty.LOCAL_WORKS, False, RiskStatus.MONITORED),
]
assessment = DeliveryReadiness(controls, responsibilities, knowledge, risks, partner_check, lw_check)

def heading(n, name): print(f"\nSECTION {n} — {name}")
print("CHAPTER 20 — DELIVERY RISK AND OWNERSHIP\nPART V — ASSEMBLE THE DELIVERY SYSTEM")
print("FICTIONAL TRAINING SCENARIO\nNO REAL CUSTOMER ACCESS OR CREDENTIALS ARE USED")
heading(1,"Starting delivery decision"); print("Path: Northstar platform specialist (fictional) for technical/capability validation; Bridge integration specialist (fictional) remains backup.\nScope: HF-SCOPE-14-v1 membership-freeze workflow. Stage: pre-kickoff validation planning.\nKnown partner risks: key-person concentration and platform capability uncertainty.")
heading(2,"Asset register")
for c in controls: print(f"{c.asset.name} | {c.asset.asset_type.name} | control={c.primary_controller.name} | backup={','.join(x.name for x in c.backup_access) or 'N/A'} | recovery={c.recovery_path} | {c.status.name}")
heading(3,"Responsibility matrix")
for x in responsibilities: print(f"{x.responsibility.name}: accountable={x.accountable.name if x.accountable else 'NO OWNER'}; performs={','.join(p.name for p in x.performing) or 'NO OWNER'}; consulted={','.join(p.name for p in x.consulted) or 'N/A'}; informed={','.join(p.name for p in x.informed) or 'N/A'}")
heading(4,"Access model")
for a in access: print(f"{a.asset}: {a.party.name}; {a.access_level}; purpose={a.purpose}; revoke={a.revocation_path}; NO SECRET STORED")
heading(5,"Knowledge register")
for k in knowledge: print(f"{k.name}: required={k.required}; holder={k.current_holder.name}; documented={k.documented}; location={k.location}; transition={k.transition_readiness.name}")
heading(6,"Decision history")
for d in decisions: print(f"{d.decision}: {d.rationale} [context: {d.context}; authority={d.authority.name}]")
heading(7,"Third-party dependencies")
for d in dependencies: print(f"{d.name}: {d.criticality}; owner={d.owner.name}; support={d.support_path}; failure={d.failure_impact}; fallback={d.fallback}; {d.status}")
heading(8,"Delivery-partner disappearance test"); print(evaluate_continuity(partner_check).name, "— findings/evidence must be delivered to shared records")
heading(9,"Local Works disappearance test"); print(evaluate_continuity(lw_check).name, "— customer controls its account; current project export/handoff remains required")
heading(10,"Responsibility-gap detector")
for x in assessment.responsibility_gaps(): print(x.responsibility.name, "—", x.notes)
heading(11,"Authority ambiguity"); overlap=ResponsibilityAssignment(ResponsibilityType.DEPLOYMENT, ControlParty.UNKNOWN,(ControlParty.CUSTOMER,ControlParty.LOCAL_WORKS,ControlParty.DELIVERY_PARTNER,ControlParty.THIRD_PARTY_VENDOR)); print("Example only:", ', '.join(p.name for p in overlap.performing), "all have production admin; overlap=", overlap.has_authority_overlap, "MORE ACCESS ≠ MORE CONTROL. Harbor validation has no production deployment.")
heading(12,"Risk register")
for r in risks: print(f"{'BLOCKING' if r.blocking else 'MONITORED'} {r.category.name}/{r.severity.name}: {r.description}; evidence={r.evidence}")
heading(13,"Control remediation"); print("Require shared validation findings, screenshots/notes, capability results, configuration observations, open questions, and vendor references; confirm separate least-privilege identity and revocation; export decision/current-state record to customer. No external action is performed.")
heading(14,"Final delivery readiness"); print(assessment.assess().name, "— readiness assessment does not start kickoff")
heading(15,"Interpretation"); print("Resolve the validation-record blocker before work is handed off. Local Works should be able to change technical providers without losing the customer or the project; the customer should also be able to continue without Local Works.")
