"""Meaning-level checks for Chapter 25 QA and acceptance."""
from datetime import date
from local_works.projects import (Requirement, RequirementPriority, RequirementSource,
                                  RequirementStatus, RequirementType)
from local_works.qa import *

def requirement(i="R-1", priority=RequirementPriority.MUST):
    return Requirement(i,"agreed behavior",RequirementType.FUNCTIONAL,priority,
                       RequirementSource.SCOPE,"baseline",acceptance_linkage=("AC-1",),
                       status=RequirementStatus.READY_FOR_IMPLEMENTATION)

def case(status=TestStatus.NOT_RUN, kind=TestType.FUNCTIONAL):
    return TestCase("T-1","behavior",kind,"R-1","BR-1","AC-1",expected_result="works",status=status)

def defect(severity=DefectSeverity.MEDIUM,status=DefectStatus.OPEN,**kw):
    return Defect("D-1","does not work","R-1","T-1",severity,status,"Local Works",
                  TestEnvironment.SANDBOX,"works","does not","workflow impact",**kw)

def session(defects=(), issues=(), result=TestStatus.PASS):
    return CustomerAcceptanceSession(date.today(),"scope-v1","req-v1",("T-1",),
        (AcceptanceCriterionResult("AC-1",result,("T-1",)),),issues,defects,("checklist",))

def test_case_references_requirement_and_acceptance_criterion():
    t=case(); assert t.related_requirement == "R-1"; assert t.related_acceptance_criterion == "AC-1"

def test_pass_fail_and_blocked_are_distinct_and_blocked_is_not_failed():
    assert len({TestStatus.PASS,TestStatus.FAIL,TestStatus.BLOCKED}) == 3
    assert case(TestStatus.FAIL).failed and not case(TestStatus.BLOCKED).failed

def test_uncovered_approved_must_is_detected():
    assert requirement_coverage([requirement()],[])["R-1"] == "UNTESTED_REQUIREMENT"
    assert qa_readiness([requirement()],[]) is QAReadiness.NOT_READY

def test_defect_links_to_failed_test_and_preserves_severity():
    t=case(TestStatus.FAIL); d=defect(DefectSeverity.HIGH)
    assert d.related_test == t.test_id and d.severity is DefectSeverity.HIGH

def test_defect_and_change_request_remain_distinct():
    d=defect(); change=defect(status=DefectStatus.NOT_A_DEFECT,fix_required=False)
    assert d.status is DefectStatus.OPEN and change.status is DefectStatus.NOT_A_DEFECT
    assert not change.fix_required

def test_known_cosmetic_issue_can_be_nonblocking_and_accepted():
    issue=KnownIssue("copy",DefectSeverity.COSMETIC,"understandable","none","revise","Sponsor")
    assert not issue.blocking
    assert session(issues=(issue,)).decide().status is AcceptanceStatus.ACCEPTED_WITH_KNOWN_ISSUES

def test_critical_open_defect_blocks_and_rejects_acceptance():
    d=defect(DefectSeverity.CRITICAL)
    assert d.blocks_acceptance
    assert session(defects=(d,)).decide().status is AcceptanceStatus.REJECTED_FOR_DEFECTS

def test_failed_acceptance_criterion_rejects_acceptance():
    assert session(result=TestStatus.FAIL).decide().status is AcceptanceStatus.REJECTED_FOR_DEFECTS

def test_fix_requires_retest_and_passing_retest_can_close_defect():
    d=defect(status=DefectStatus.READY_FOR_RETEST)
    try: d.close(); assert False
    except ValueError: pass
    d.record_retest(RetestRecord("T-1",TestStatus.PASS)); assert not d.fix_required
    d.close(); assert d.status is DefectStatus.CLOSED

def test_regression_test_is_representable():
    assert case(TestStatus.PASS,TestType.REGRESSION).test_type is TestType.REGRESSION

def test_customer_found_preventable_defect_counts_as_escape():
    d=defect(customer_found=True,reasonably_preventable=True)
    assert d.qa_escape and QACycle(1,[case()],[d]).qa_escapes == 1

def test_acceptance_can_be_accepted_or_accepted_with_issues_or_rejected():
    assert session().decide().status is AcceptanceStatus.ACCEPTED
    issue=KnownIssue("copy",DefectSeverity.LOW,"workaround","small","later","Sponsor")
    assert session(issues=(issue,)).decide().status is AcceptanceStatus.ACCEPTED_WITH_KNOWN_ISSUES
    assert session(defects=(defect(DefectSeverity.HIGH),)).decide().status is AcceptanceStatus.REJECTED_FOR_DEFECTS

def test_acceptance_does_not_prove_roi():
    assert session().decide().business_success_proven is False

def test_qa_cycle_separates_defect_rework_from_scope_change_work():
    q=QACycle(1,[case()],defect_rework_hours=3,scope_change_hours=8)
    assert q.defect_rework_hours != q.scope_change_hours

def test_chapter_does_not_deploy_or_collect_payment():
    decision=session().decide()
    assert not hasattr(decision,"deploy") and not hasattr(decision,"collect_payment")
