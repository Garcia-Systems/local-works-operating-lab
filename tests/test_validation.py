from pathlib import Path

from local_works.audit import JourneyStage
from local_works.validation import (
    AuditDecision, DigitalFrictionAudit, FrictionType, JourneyReview, Rating,
    RejectionReason, SolutionPath, SprintCounts, TargetDimension,
    ValidationEvidence, ValidationHypothesis, ValidationObservation,
    ValidationStatus, ValidationTarget, ValidationTargetScore,
    no_response_learning,
)


def score(**overrides: Rating) -> ValidationTargetScore:
    values = {dimension: Rating.MEDIUM for dimension in TargetDimension}
    for name, value in overrides.items():
        values[TargetDimension[name]] = value
    return ValidationTargetScore(values)


def target() -> ValidationTarget:
    return ValidationTarget("Example", "Example", "https://example.invalid", "One", "Test", score(), True)


def audit(decision: AuditDecision, friction: FrictionType) -> DigitalFrictionAudit:
    review = JourneyReview(JourneyStage.FIND, "Visible statement", friction, "Public page")
    return DigitalFrictionAudit(target(), (review,), (), decision, "Explicit manual judgment")


def test_target_score_preserves_unknown():
    result = score(BUSINESS_VALUE_POTENTIAL=Rating.UNKNOWN)
    assert result.ratings[TargetDimension.BUSINESS_VALUE_POTENTIAL] is Rating.UNKNOWN
    assert result.verdict.name == "INSUFFICIENT_EVIDENCE"


def test_no_observable_friction_is_valid():
    result = audit(AuditDecision.NO_OBVIOUS_OPPORTUNITY, FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND)
    assert not result.has_meaningful_public_friction


def test_observation_remains_distinct_from_inference_and_unknown_creates_question():
    finding = ValidationObservation("Page requires a call", "May create work", "Call volume", "How many calls?", FrictionType.REQUIRES_PHONE_CALL, "Public page")
    assert finding.observation != finding.inference
    assert finding.unknown and finding.discovery_question.endswith("?")


def test_unknown_without_discovery_question_is_rejected():
    try:
        ValidationObservation("Visible", "Possible", "Unknown fact", "", FrictionType.OTHER, "Page")
    except ValueError as error:
        assert "discovery question" in str(error)
    else:
        raise AssertionError("Unknown facts must produce a question")


def test_supported_audit_verdicts_and_unknown_solution_path():
    worth = audit(AuditDecision.WORTH_DISCOVERY, FrictionType.REQUIRES_PHONE_CALL)
    none = audit(AuditDecision.NO_OBVIOUS_OPPORTUNITY, FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND)
    assert worth.decision is AuditDecision.WORTH_DISCOVERY
    assert none.decision is AuditDecision.NO_OBVIOUS_OPPORTUNITY
    assert worth.solution_path is SolutionPath.UNKNOWN


def test_value_hypothesis_remains_unvalidated():
    assert ValidationHypothesis("Possible effect").status == "UNVALIDATED"


def test_response_states_and_unknown_rejection_work():
    assert ValidationStatus.NO_RESPONSE.name == "NO_RESPONSE"
    assert ValidationStatus.OPPORTUNITY.name == "OPPORTUNITY"
    assert RejectionReason.UNKNOWN.name == "UNKNOWN"


def test_no_response_does_not_invalidate_the_business():
    learned, unsupported = no_response_learning()
    assert "attempt" in learned
    assert "Local Works has no market" in unsupported


def test_sprint_counts_actual_stages_separately():
    counts = SprintCounts(researched=5, audited=3, contacted=2, responses=1)
    assert (counts.researched, counts.audited, counts.contacted, counts.responses) == (5, 3, 2, 1)


def test_evidence_ledger_does_not_upgrade_without_evidence():
    entry = ValidationEvidence("close rate", "42%", "simulation")
    assert entry.update((), "1 of 3") is entry
    assert entry.evidence_status == "SIMULATION_ONLY"
    updated = entry.update(("Dated outcome VAL-001",), "1 of 3 eligible attempts")
    assert updated.evidence_status == "REAL_EVIDENCE_COLLECTED"


def test_fictional_demonstration_is_unmistakably_marked():
    script = (Path(__file__).parents[1] / "scripts/run_validation_sprint_01.py").read_text()
    assert "FICTIONAL DEMONSTRATION" in script
    assert "THE DEMONSTRATION DATA BELOW IS FICTIONAL" in script
    assert "REAL VALIDATION DATA MUST BE ENTERED ONLY AFTER ACTUAL RESEARCH" in script


def test_validation_code_has_no_external_or_production_behavior():
    root = Path(__file__).parents[1]
    source = (root / "local_works/validation.py").read_text()
    script = (root / "scripts/run_validation_sprint_01.py").read_text()
    forbidden = ("requests", "urllib", "http.client", "smtplib", "selenium", "playwright", "subprocess", "Laravel", "artisan")
    assert not any(term in source for term in forbidden)
    assert not any(f"import {term}" in script for term in forbidden)
    assert not (root / "book/33").exists()
