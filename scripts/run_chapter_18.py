#!/usr/bin/env python3
"""Chapter 18: deterministic fictional delivery-path exercise."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.partners import *

needs = [
    DeliveryNeed("Membership-platform configuration", "HIGH", RequirementLevel.REQUIRED, "Configuration-first solution direction", "Exact capability remains UNKNOWN"),
    DeliveryNeed("Workflow analysis", "HIGH", RequirementLevel.REQUIRED, "Scoped check-in workflow"),
    DeliveryNeed("Testing and reproducibility", "HIGH", RequirementLevel.REQUIRED, "Acceptance requires demonstrated behavior"),
    DeliveryNeed("Documentation and support handoff", "HIGH", RequirementLevel.REQUIRED, "Continuity requirement"),
    DeliveryNeed("API/integration investigation", "MEDIUM", RequirementLevel.OPTIONAL, "Needed only if configuration is insufficient"),
    DeliveryNeed("Customer-facing coordination", "HIGH", RequirementLevel.REQUIRED, "Local Works retains relationship leadership"),
]

def cap(name, rating, evidence=EvidenceType.UNKNOWN):
    return DeliveryCapability(name, rating, (PartnerEvidence(name, evidence, "fictional prequalification record"),))

candidates = [
    DeliveryCandidate("Northstar Configuration Specialist (fictional)", DeliveryPathType.SPECIALIST_FREELANCER,
        [cap("Membership-platform configuration", FitRating.STRONG, EvidenceType.DIRECT_EVALUATION), cap("API integration", FitRating.WEAK, EvidenceType.SELF_REPORTED)],
        "AVAILABLE", 20, FitRating.STRONG, FitRating.ADEQUATE, FitRating.STRONG, FitRating.ADEQUATE, FitRating.ADEQUATE, FitRating.STRONG, 3000, FitRating.ADEQUATE, SubcontractingStatus.NONE),
    DeliveryCandidate("Bridge Integration Freelancer (fictional)", DeliveryPathType.INDEPENDENT_CONTRACTOR,
        [cap("API integration", FitRating.STRONG, EvidenceType.PUBLIC_PORTFOLIO), cap("Membership-platform configuration", FitRating.UNCERTAIN)],
        "AVAILABLE", 12, FitRating.STRONG, FitRating.UNCERTAIN, FitRating.STRONG, FitRating.ADEQUATE, FitRating.ADEQUATE, FitRating.STRONG, 4000, FitRating.ADEQUATE, SubcontractingStatus.NONE),
    DeliveryCandidate("Cedar Small Software Agency (fictional)", DeliveryPathType.SMALL_AGENCY,
        [cap("Full-stack custom build", FitRating.STRONG, EvidenceType.PUBLIC_PORTFOLIO), cap("QA", FitRating.STRONG, EvidenceType.SELF_REPORTED)],
        "AVAILABLE", 60, FitRating.ADEQUATE, FitRating.UNCERTAIN, FitRating.ADEQUATE, FitRating.STRONG, FitRating.ADEQUATE, FitRating.ADEQUATE, 9000, FitRating.WEAK, SubcontractingStatus.POSSIBLE),
    DeliveryCandidate("Local Works self delivery (fictional exercise)", DeliveryPathType.LOCAL_WORKS_SELF_DELIVERY,
        [cap("Customer context", FitRating.STRONG, EvidenceType.DIRECT_EVALUATION), cap("Platform expertise", FitRating.UNCERTAIN)],
        "AVAILABLE", 6, FitRating.STRONG, FitRating.STRONG, FitRating.STRONG, FitRating.ADEQUATE, FitRating.ADEQUATE, FitRating.STRONG, 0, FitRating.UNCERTAIN, SubcontractingStatus.NONE),
    DeliveryCandidate("Harbor Fitness internal IT (fictional)", DeliveryPathType.CUSTOMER_INTERNAL_TEAM,
        [cap("Internal access", FitRating.STRONG, EvidenceType.DIRECT_EVALUATION), cap("Platform configuration", FitRating.UNCERTAIN)],
        "AVAILABLE", 3, FitRating.ADEQUATE, FitRating.UNCERTAIN, FitRating.UNCERTAIN, FitRating.UNCERTAIN, FitRating.ADEQUATE, FitRating.UNCERTAIN, None, FitRating.UNCERTAIN, SubcontractingStatus.UNKNOWN),
]
candidates[4].risks.append(DeliveryRisk(RiskCategory.CAPACITY, "Only three hours per week", RiskSeverity.HIGH, "Fictional availability statement", "Use as access adviser, not primary delivery", disqualifying=True))
record = DeliveryAssessment("Harbor Fitness", "Capability validation / configuration first", "Validate and configure the check-in workflow; custom build excluded", needs, candidates=candidates,
    continuity_plan="Shared repository when code exists; customer/Local Works administrative control; decision log, tests, and milestone documentation",
    backup_path="Keep transition-ready records so another qualified provider can continue")
for name, decision in zip((c.name for c in candidates), (QualificationDecision.QUALIFIED_FOR_ESTIMATE, QualificationDecision.QUALIFIED_FOR_ESTIMATE, QualificationDecision.WRONG_DELIVERY_MODEL, QualificationDecision.NEEDS_MORE_INFORMATION, QualificationDecision.NOT_AVAILABLE)):
    record.qualify(name, decision)

print("CHAPTER 18 — FIND THE DELIVERY PATH\nPART V — ASSEMBLE THE DELIVERY SYSTEM")
print("FICTIONAL TRAINING SCENARIO\nNO REAL CONTRACTOR OR AGENCY IS BEING EVALUATED")
print("\nSECTION 1 — Starting project state\nCommercial close: HOLD_FOR_REQUIREMENT / not implementation-authorized\nSolution: capability validation / CONFIGURE FIRST\nScope: validate and configure check-in workflow; custom build excluded\nUnresolved: platform capability, API entitlement, test access")
print("\nSECTION 2 — Delivery needs")
for n in needs: print(f"{n.requirement.name}: {n.capability} — {n.importance}; evidence: {n.evidence}")
print("\nSECTION 3 — Delivery path options\nSELF: control / capacity risk\nCONTRACTOR: flexibility / continuity risk\nSPECIALIST: focused fit / narrow skills\nAGENCY: backup team / cost and layers\nCUSTOMER TEAM: internal knowledge / competing priorities\nMIXED: combined strengths / coordination")
print("\nSECTION 4 — Fictional candidates")
for c in candidates: print(f"{c.name}: {c.path_type.value}; availability={c.availability}; capacity={c.capacity_hours_per_week} hours/week")
print("\nSECTION 5 — Capability fit")
for c in candidates:
    print(c.name + ": " + ", ".join(f"{x.capability}={x.rating.name}" for x in c.capabilities))
print("GOOD TECHNICIAN ≠ RIGHT DELIVERY FIT: strong custom skills do not establish fit for platform configuration.")
print("\nSECTION 6 — Evidence quality\nSELF_REPORTED is a claim, PUBLIC_PORTFOLIO is public evidence, DIRECT_EVALUATION is observed in an exercise, PAST_PERFORMANCE requires real prior work, and UNKNOWN stays unknown. No fictional past Local Works performance is claimed.")
print("\nSECTION 7 — Risk assessment\nNorthstar: narrow integration depth and solo key-person risk. Bridge: platform fit uncertain. Cedar: wrong-sized/cost and custom-build incentive. Local Works: capacity and skill uncertainty. Internal IT: critical capacity constraint.")
print("\nSECTION 8 — Continuity test")
for c in candidates: print(f"If {c.name} disappears: requirements, decisions, account administration, tests, and documentation must remain with customer/Local Works; provider-only assets are unacceptable.")
print("\nSECTION 9 — Repository/account control\nUse customer/Local Works-controlled shared source as agreed; record ACCOUNT_OWNER, ADMINISTRATIVE_ACCESS, and RECOVERY_PATH; use separate least-privilege identities, revocable access, and appropriate secret management—never real credentials in this record.")
print("\nSECTION 10 — Cost vs fit\nA $1,500 provider using a personal repository, personal accounts, inconsistent communication, and no handoff is not automatically preferred to a $3,000 transition-ready provider. Neither automatically wins: compare fit, evidence, rework, and total delivery risk.")
print("\nSECTION 11 — Partner conflict-of-interest scenario\nCedar recommends a custom build, which better matches its business model. Configuration remains plausible, so Local Works preserves Chapter 12's independent solution hierarchy.")
print("\nSECTION 12 — Prequalification")
for c in candidates: print(f"{c.name}: {record.decisions[c.name].name}")
print("\nSECTION 13 — Preferred delivery path\nRequest comparable Chapter 19 estimates from: " + "; ".join(record.qualified_for_estimate) + ". This is not a final winner or assignment.")
print("\nSECTION 14 — Backup strategy\n" + record.continuity_plan + ". Backup: " + record.backup_path + ". A disappearing provider makes recovery painful but manageable, unlike provider-only code, credentials, deployment knowledge, and decisions.")
print("\nSECTION 15 — Interpretation\nLocal Works is assembling a delivery system, not shopping for the cheapest coder. Customer owns business decisions; Local Works owns relationship, translation, coordination, and commercial accountability; delivery supplies technical capability. No estimate, provider selection, kickoff, or implementation occurs.")
print("\nSUCCESS — RIGHT-SIZED DELIVERY\nFor a simple configuration issue, six hours from a qualified platform specialist can solve the problem without custom development while Local Works retains documentation and the relationship.")
