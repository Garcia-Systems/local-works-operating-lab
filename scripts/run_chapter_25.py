#!/usr/bin/env python3
"""Run Chapter 25's fictional QA and customer-acceptance exercise."""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.projects import (Requirement, RequirementPriority, RequirementSource,
                                  RequirementStatus, RequirementType)
from local_works.qa import *

def section(n: int, title: str) -> None: print(f"\nSECTION {n} — {title}")
def req(i: str, statement: str, link: str) -> Requirement:
    return Requirement(i, statement, RequirementType.FUNCTIONAL, RequirementPriority.MUST,
                       RequirementSource.ACCEPTANCE_CRITERIA, "HF-REQ-21-v1", acceptance_linkage=(link,),
                       status=RequirementStatus.READY_FOR_IMPLEMENTATION)

print("FICTIONAL TRAINING SCENARIO")
print("NO REAL CUSTOMER SYSTEM IS BEING TESTED")
requirements=[req("R-001","Preserve confirmed eligibility policy","AC-01"),
              req("R-002","Routine eligible request avoids staff re-entry","AC-01"),
              req("R-003","Exceptions reach authorized manager and record status","AC-01"),
              req("R-004","Use safe least-privilege access","AC-02"),
              req("R-005","Document findings and limitations","AC-02")]
tests=[
 TestCase("HF-T01","Standard eligible freeze",TestType.WORKFLOW,"R-002","BR-01","AC-01",("Synthetic standard membership",),("Submit eligible freeze",),"Accepted without manager re-entry"),
 TestCase("HF-T02","Special membership review",TestType.BUSINESS_RULE,"R-003","BR-03","AC-01",("Synthetic special membership",),("Submit freeze",),"Routes to authorized manager"),
 TestCase("HF-T03","Denied request status",TestType.DATA,"R-001","BR-02","AC-01",(),("Deny fictional request",),"Denied status recorded"),
 TestCase("HF-T04","Confirmation behavior",TestType.USABILITY,"R-005",None,"AC-02",(),("Complete request",),"Clear result and next step"),
 TestCase("HF-T05","Unauthorized approval",TestType.SECURITY_ACCESS,"R-004",None,"AC-02",(),("Attempt approval as ordinary staff",),"Approval denied"),
 TestCase("HF-T07","Failed platform write",TestType.ERROR_HANDLING,"R-001",None,"AC-01",(),("Simulate unavailable fictional vendor",),"Failure visible; no false success")]
section(1,"Starting delivery state")
print("Scope HF-SCOPE-14-v1 | requirements HF-REQ-21-v1 | status READY_FOR_QA")
print("AC-01 workflow/routing/status; AC-02 safe access and transition-ready evidence")
section(2,"QA readiness"); print("Delivery-team smoke/configuration/error checks complete;",qa_readiness(requirements,tests).name)
section(3,"Test plan")
for t in tests: print(t.test_id,t.test_type.name,"→",t.related_requirement,"/",t.related_acceptance_criterion)
section(4,"First test run")
results=[TestStatus.FAIL,TestStatus.PASS,TestStatus.PASS,TestStatus.PASS,TestStatus.PASS,TestStatus.PASS]
actual=["Incorrectly routed to manager","Correct manager route","Denied recorded","Understandable but awkward wording","Approval denied","Failure shown; follow-up retained"]
for t,s,a in zip(tests,results,actual): t.record(s,a,(TestEvidence("test notes",f"QA-C1-{t.test_id}"),)); print(t.test_id,s.name,a)
section(5,"Requirement coverage")
for k,v in requirement_coverage(requirements,tests).items(): print(k,v)
section(6,"Defect triage")
defect=Defect("HF-D01","Eligible standard request routes to manager","R-002","HF-T01",DefectSeverity.HIGH,DefectStatus.TRIAGED,"Local Works",TestEnvironment.SANDBOX,"Bypass manager","Manager review","Core routine workflow cannot complete as agreed","Delivery partner",priority="HIGH")
cosmetic=Defect("HF-D02","Confirmation wording is awkward","R-005","HF-T04",DefectSeverity.COSMETIC,DefectStatus.ACCEPTED_AS_KNOWN_ISSUE,"Local Works",TestEnvironment.SANDBOX,"Clear natural wording","Understandable awkward wording","No workflow impact","Delivery partner",False,priority="LOW")
change=Defect("HF-D03","Cancellation is absent",None,"UAT-request",DefectSeverity.LOW,DefectStatus.NOT_A_DEFECT,"Customer",TestEnvironment.SANDBOX,"Outside approved scope","Freeze only","None in accepted scope",fix_required=False,notes="CUSTOMER_ENHANCEMENT / SCOPE_CHANGE under Chapter 24")
for d in (defect,cosmetic,change): print(d.defect_id,d.severity.name,d.status.name,"—",d.notes or d.summary)
section(7,"Fix and retest")
defect.status=DefectStatus.READY_FOR_RETEST; tests[0].record(TestStatus.PASS,"Eligible request now bypasses manager")
defect.record_retest(RetestRecord("HF-T01",TestStatus.PASS,date(2026,9,18),"QA-C2-HF-T01")); defect.close(); print(defect.status.name,"— defect correction rework 3h; customer charge $0")
section(8,"Regression test")
regression=TestCase("HF-TR01","Routing regression",TestType.REGRESSION,"R-002","BR-01","AC-01",steps=("Repeat standard, exception, confirmation",),expected_result="All remain correct",status=TestStatus.PASS,actual_result="Standard, exception, confirmation pass")
print(regression.test_id,regression.status.name,regression.actual_result)
section(9,"Local Works QA"); print("READY_WITH_NONBLOCKERS — customer should now see the work; HF-D02 is disclosed.")
section(10,"Customer acceptance session"); print("Scope restated; customer ran standard and exception paths and observed confirmation; handoff reviewed.")
section(11,"Out-of-scope UAT request"); print("Add cancellation → NOT_A_DEFECT; CUSTOMER_ENHANCEMENT / SCOPE_CHANGE; phase separately via Chapter 24.")
section(12,"Known issues")
issue=KnownIssue("Awkward confirmation wording",DefectSeverity.COSMETIC,"Outcome remains understandable","No workflow impact","Copy revision after acceptance","Fictional Harbor sponsor","Next review",False)
print(issue.description,"| disclosed | nonblocking | accepted by",issue.accepted_by)
section(13,"Acceptance decision")
session=CustomerAcceptanceSession(date(2026,9,19),"HF-SCOPE-14-v1","HF-REQ-21-v1",("HF-T01","HF-T02","HF-T04"),(AcceptanceCriterionResult("AC-01",TestStatus.PASS,("HF-T01","HF-T02")),AcceptanceCriterionResult("AC-02",TestStatus.PASS,("HF-T04","HF-T05"))), (issue,), evidence=("fictional acceptance checklist HF-UAT-01",))
decision=session.decide(); print(decision.status.name,"—",decision.rationale,"Long-term business success proven:",decision.business_success_proven)
section(14,"QA metrics")
all_tests=tests+[regression]; print("tests passed",sum(t.status is TestStatus.PASS for t in all_tests),"| failed",sum(t.status is TestStatus.FAIL for t in all_tests),"| defects HIGH 1, COSMETIC 1 | retest cycles 1 | QA escapes 0 | requirements covered 5/5")
section(15,"Interpretation")
print("QA protects the customer from avoidable defects and protects Local Works from subjective acceptance disputes.")
print("Acceptance proves agreed fitness now, not weeks-later ROI. Customer acceptance was not the first test pass.")
print("FAILURE — CUSTOMER IS QA: broken standard flow, missing confirmation, and wrong eligibility escape. THE CUSTOMER SHOULD NOT BE THE FIRST QA PASS.")
print("FAILURE — HAPPY PATH ONLY: exceptions fail after launch. THE WORKFLOW INCLUDES EXCEPTIONS.")
print("FAILURE — CHANGE CALLED DEFECT: cancellation as a bug destroys scope discipline.")
print("FAILURE — DEFECT CALLED CHANGE: R-002 failure is correction, not customer-paid extra work.")
print("FAILURE — HIDDEN ISSUE: undisclosed membership failure destroys trust.")
print("SUCCESS — FAIR ACCEPTANCE: partner tests, Local Works finds/fixes the defect, customer validates fitness, and a disclosed minor issue remains.")
print("No production deployment, signature, invoice, payment, customer data, or real system activity occurred.")
