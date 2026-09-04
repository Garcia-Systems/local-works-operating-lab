import pytest

from local_works.projects import *
from local_works.translation import *


def requirement(requirement_id="R-001", status=RequirementStatus.READY_FOR_IMPLEMENTATION):
    return Requirement(requirement_id, "Exceptions require manager approval", RequirementType.FUNCTIONAL,
                       RequirementPriority.MUST, RequirementSource.WORKFLOW, "HF-WORKFLOW-09", status=status)


def statement(wording="We need a portal"):
    return BusinessStatement("S-001", wording, "Operations manager", "Kickoff notes", interpretation="Reduce staff intervention")


def intent():
    return BusinessIntent("S-001", "Reduce repetitive staff intervention", "Members and staff", "WF-FUTURE-01")


def task(task_id="TT-001", requirements=("R-001",), risks=(), title="Validate platform"):
    return TechnicalTask(task_id, title, "Test available capability", TechnicalTaskCategory.VALIDATE_CAPABILITY,
                         "Capability result and evidence are recorded", requirements, risk_justifications=risks)


def record(status=TranslationStatus.READY_FOR_IMPLEMENTATION, tasks=None):
    return TranslationRecord("TR-001", statement(), intent(), ("R-001",), technical_tasks=tuple(tasks or [task()]), status=status)


def test_source_statement_is_preserved_and_intent_is_distinct():
    source = statement()
    assert source.wording == "We need a portal"
    assert intent().desired_outcome != source.wording


def test_translation_references_existing_requirement_and_preserves_provenance():
    r = requirement()
    assert record().references_known_requirements([r])
    assert r.source is RequirementSource.WORKFLOW and r.evidence_reference == "HF-WORKFLOW-09"


def test_business_rule_is_not_technical_design():
    rule = BusinessRuleReference("BR-03", "Exceptions require manager approval", "Policy notes", True)
    need = TechnicalNeed("TN-1", "Distinguish routine and exception paths", ("R-001",))
    assert rule.statement != need.statement


def test_data_need_preserves_unknown_source():
    assert DataNeed("approval status", "Record decision").source is DataSource.UNKNOWN


def test_technical_question_is_distinct_from_business_question():
    business = OpenQuestion("BQ-1", "Which types need approval?", QuestionCategory.BUSINESS_RULE, "Harbor", "Policy", True)
    technical = TechnicalQuestion("TQ-1", "Can the platform expose type?", "Evaluation", "R-001", owner="Specialist")
    assert business_question(business) and not isinstance(technical, OpenQuestion)


def test_task_links_multiple_requirements_and_requires_done_condition():
    assert task(requirements=("R-001", "R-002")).related_requirement_ids == ("R-001", "R-002")
    with pytest.raises(ValueError):
        TechnicalTask("TT-X", "Build freeze feature", "Too broad", TechnicalTaskCategory.IMPLEMENT, "")


def test_out_of_scope_cancellation_needs_no_task_or_gap():
    cancellation = requirement("R-CANCEL", RequirementStatus.OUT_OF_SCOPE)
    assert missing_technical_coverage([cancellation], [], []) == ()
    assert TranslationRecord("TR-X", statement("Add cancellation"), intent(), ("R-CANCEL",), status=TranslationStatus.OUT_OF_SCOPE).technical_tasks == ()


def test_missing_coverage_and_unjustified_work_are_detected():
    assert missing_technical_coverage([requirement()], [], []) == ("R-001",)
    extra = task("TT-X", requirements=(), title="Add analytics dashboard")
    assert unjustified_technical_work([extra]) == ("TT-X",)
    assert gold_plated_work([extra]) == ("TT-X",)


def test_invisible_work_can_be_justified_by_operational_or_security_risk():
    logging = task("TT-LOG", requirements=(), risks=("Reliability: failed writes must be visible",), title="Add bounded failure logging")
    assert logging.justified and unjustified_technical_work([logging]) == ()


def test_vendor_questions_and_limitations_route_deliberately():
    q = TechnicalQuestion("TQ-1", "Can status be written?", "Viability", "R-001", blocking=True)
    assert readiness([record()], technical_questions=[q]) is TranslationReadiness.NEEDS_TECHNICAL_VALIDATION
    assert vendor_limitation_outcome(need_in_scope=False, alternate_within_solution=False, solution_still_viable=True) is VendorLimitationOutcome.REVISIT_SCOPE
    assert vendor_limitation_outcome(need_in_scope=True, alternate_within_solution=False, solution_still_viable=False) is VendorLimitationOutcome.REVISIT_SOLUTION


def test_traceability_chain_is_preserved():
    link = TraceabilityLink("S-1", "Reduce calls", "R-002", "BR-03", "WB-1", "TN-1", "TT-1", "T-1", "AC-1")
    translated = record()
    translated.traceability_links = (link,)
    assert translated.traceability_links[0].acceptance_criterion_id == "AC-1"


def test_readiness_outcomes():
    assert readiness([record()]) is TranslationReadiness.READY_FOR_IMPLEMENTATION
    bq = OpenQuestion("BQ", "Which types?", QuestionCategory.BUSINESS_RULE, "Customer", "Policy", True)
    assert readiness([record()], [bq]) is TranslationReadiness.NEEDS_BUSINESS_CLARIFICATION
    assert readiness([record(TranslationStatus.NEEDS_TECHNICAL_CLARIFICATION)]) is TranslationReadiness.NEEDS_TECHNICAL_VALIDATION


def test_chapter_22_does_not_implement_production_code():
    translated = record()
    assert not hasattr(translated, "deploy") and not hasattr(translated, "database_schema")
