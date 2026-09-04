#!/usr/bin/env python3
"""Run the fictional Chapter 21 kickoff exercise."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.projects import *

project = Project("HF-VALIDATION-01", "Harbor Fitness", "HF-CLOSE-17", "HF-PROP-16-v2", "HF-SCOPE-14-v1", "HF-EST-19-NORTHSTAR", ("Validate configuration-first membership-freeze workflow",), ("Cancellation workflow", "Custom portal implementation"))
participants = [
 ProjectParticipant(ParticipantRole.CUSTOMER_DECISION_MAKER,"Harbor Fitness",("Decide policy and accept findings",),("BUSINESS_RULES","CUSTOMER_ACCEPTANCE"),"Fictional Operations Manager"),
 ProjectParticipant(ParticipantRole.CUSTOMER_SUBJECT_MATTER_EXPERT,"Harbor Fitness",("Explain current freeze workflow",),(),"Fictional Membership Lead"),
 ProjectParticipant(ParticipantRole.LOCAL_WORKS_PROJECT_LEAD,"Local Works",("Coordinate scope, questions, evidence",),("SCOPE","COMMERCIAL_CHANGES"),"Fictional Project Lead"),
 ProjectParticipant(ParticipantRole.DELIVERY_TECHNICAL_LEAD,"Northstar Configuration Specialist (fictional)",("Validate platform capability",),("TECHNICAL_DESIGN_WITHIN_SCOPE",),"Fictional Platform Specialist"),
]
project.participants.extend(participants)
requirements = [
 Requirement("R-001","Validation must determine whether the platform can preserve Harbor's confirmed freeze eligibility rules.",RequirementType.BUSINESS_RULE,RequirementPriority.MUST,RequirementSource.SCOPE,"HF-SCOPE-14-v1",("Freeze workflow validation",),status=RequirementStatus.READY_FOR_IMPLEMENTATION),
 Requirement("R-002","Validation must determine whether routine requests can avoid staff re-entry of member-submitted information.",RequirementType.FUNCTIONAL,RequirementPriority.MUST,RequirementSource.ACCEPTANCE_CRITERIA,"HF-SCOPE-14-v1 acceptance",("Freeze workflow validation",),("AC-01",),RequirementStatus.READY_FOR_IMPLEMENTATION),
 Requirement("R-003","Validation must determine whether exceptions can route to an authorized staff decision and record status.",RequirementType.FUNCTIONAL,RequirementPriority.MUST,RequirementSource.WORKFLOW,"HF-WORKFLOW-09",("Freeze workflow validation",),("AC-01",),RequirementStatus.NEEDS_CLARIFICATION,("Q-04",)),
 Requirement("R-004","The specialist must use separate least-privilege access; Harbor staff must not share personal passwords.",RequirementType.ACCESS,RequirementPriority.MUST,RequirementSource.SCOPE,"HF-DELIVERY-CONTROL-20",status=RequirementStatus.READY_FOR_IMPLEMENTATION),
 Requirement("R-005","Findings, test evidence, known limitations, and open questions must be delivered in shared project records.",RequirementType.DOCUMENTATION,RequirementPriority.MUST,RequirementSource.SCOPE,"HF-DELIVERY-CONTROL-20",status=RequirementStatus.READY_FOR_IMPLEMENTATION),
]
project.requirements.extend(requirements)
questions = [
 OpenQuestion("Q-01","Does the platform support a configurable freeze workflow?",QuestionCategory.VENDOR,"Delivery technical lead","Determines configuration viability",True,evidence_reference="HF-EST-19-NORTHSTAR"),
 OpenQuestion("Q-02","Can eligibility data be read and status written using existing capability?",QuestionCategory.TECHNICAL,"Delivery technical lead","Determines workflow viability",True,evidence_reference="HF-EST-19-NORTHSTAR"),
 OpenQuestion("Q-03","What test environment is available?",QuestionCategory.ACCESS,"Harbor technical contact","Needed before validation execution",True,evidence_reference="HF-DELIVERY-CONTROL-20"),
 OpenQuestion("Q-04","Which exception cases require manager approval?",QuestionCategory.BUSINESS_RULE,"Harbor Operations Manager","Delivery must not invent policy",True,evidence_reference="UNKNOWN"),
 OpenQuestion("Q-05","Who is the vendor support contact?",QuestionCategory.VENDOR,"Local Works project lead","Useful escalation detail",False,evidence_reference="UNKNOWN"),
]
baseline = RequirementBaseline("HF-REQ-21-v0.1", requirements)
kickoff = Kickoff(True,True,"HF-SCOPE-14-v1","HF-PROP-16-v2","HF-EST-19-NORTHSTAR",False,True,True,True,True,True,True)
agenda=("Business problem","Desired business outcome","Approved scope","Excluded scope","Current workflow","Selected solution path","Major assumptions","Constraints","Responsibilities","Technical approach / estimate assumptions","Requirements baseline","Open technical questions","Testing / acceptance","Communication cadence","Decision / escalation path","Next milestone")

def section(n,title): print(f"\nSECTION {n} — {title}")
print("FICTIONAL TRAINING SCENARIO\nNO REAL CUSTOMER PROJECT IS BEING STARTED")
section(1,"Starting authorized project state"); print("Commercial authorization: AUTHORIZED\nDelivery path: configuration-first capability validation\nScope version: HF-SCOPE-14-v1\nEstimate decision: paid validation selected; implementation not selected\nDelivery readiness: BLOCKED pending Chapter 20 control remediation")
section(2,"Kickoff readiness"); print(kickoff.readiness().name,"— shared outputs/access remediation remains required; technical unknowns alone would not prevent kickoff")
section(3,"Participants"); [print(f"{p.role.name}: {p.organization}; authority={', '.join(p.decision_authority) or 'none'}") for p in participants]
section(4,"Project context pack"); print("Problem: manual freeze handling creates staff re-entry and delay\nWorkflow: member request → eligibility review → routine/exception decision → record and response\nSolution: validate configuration first; no custom portal\nScope: one freeze-workflow capability validation\nEconomics: preserve prior rationale; validation limits downside\nAcceptance: determine evidence-backed viable path\nRisks: vendor capability, access, shared evidence")
section(5,"Kickoff agenda"); [print(f"{i}. {a}") for i,a in enumerate(agenda,1)]
section(6,"Requirements baseline draft"); [print(r.requirement_id,r.status.name,"—",r.statement) for r in requirements]
section(7,"Requirement provenance"); [print(r.requirement_id,r.source.name,r.evidence_reference) for r in requirements]
section(8,"Business rules"); print("KNOWN: eligibility policy remains Harbor-controlled; exceptions require authorized decision\nUNKNOWN: exact exception categories and duration policy; customer must decide")
section(9,"Open questions"); [print(q.question_id,q.owner,"blocking="+str(q.blocking),q.question) for q in questions]
section(10,"Clarification vs change"); print('A. “Which manager approves exceptions?” →',baseline.classify_new_information("Which manager approves exceptions?",project.approved_scope).name); print('B. “Can we add cancellation too?” →',baseline.classify_new_information("Can we add cancellation too?",project.approved_scope).name)
section(11,"Data requirements"); print("Business data only: member identifier; membership type; requested dates; eligibility result; approval decision; status; timestamps. No database schema.")
section(12,"Exceptions"); print("Happy path: validate routine eligible request. Exceptions: member not found, review-required type, duplicate/invalid dates, vendor unavailable, denied approval, failed status write — capture expected business result, not architecture.")
section(13,"Acceptance traceability"); print("AC-01 Eligible routine request avoids staff re-entry → R-002, R-003")
section(14,"Communication / escalation"); print("Weekly concise update; milestone review; asynchronous question log; urgent blockers via Local Works. Partner → Local Works triage → Harbor SME/decision maker for policy or vendor for limitation.")
section(15,"Requirements readiness"); print(baseline.readiness(questions).name)
section(16,"Interpretation"); print("Kickoff turns commercial intent into coordinated execution without erasing earlier decisions. This validation baseline does not start implementation.")
