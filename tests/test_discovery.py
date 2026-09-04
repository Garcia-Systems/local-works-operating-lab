import pytest

from local_works.discovery import (
    CauseType, DiscoveredSystem, DiscoveryAnswer, DiscoveryFinding,
    DiscoveryOutcome, DiscoveryQuestion, DiscoveryQuestionCategory as Category,
    DiscoverySession, EvidenceConflict, EvidenceKind, EvidenceValue,
)


def question(text="How often does this happen?", category=Category.FREQUENCY_VOLUME):
    return DiscoveryQuestion(text, category)


def answer(participant, statement, value, kind):
    return DiscoveryAnswer(question(), participant, statement,
                           EvidenceValue(value, "requests/week", participant, kind))


def test_discovery_questions_retain_categories():
    item = question(category=Category.CURRENT_STATE)
    assert item.category is Category.CURRENT_STATE


def test_answers_retain_participant_and_evidence_source():
    item = answer("Front-desk employee", "About four.", 4, EvidenceKind.ESTIMATE)
    assert item.participant == "Front-desk employee"
    assert item.evidence.source == "Front-desk employee"


def test_estimates_remain_distinguishable_from_measurements():
    estimate = EvidenceValue(20, "requests/week", "Manager", EvidenceKind.ESTIMATE)
    measured = EvidenceValue(20, "requests/week", "Change log", EvidenceKind.MEASURED_DATA)
    assert estimate.kind is not measured.kind
    assert not estimate.is_measured
    assert measured.is_measured


def test_conflicting_evidence_is_preserved_not_reconciled():
    session = DiscoverySession("Requests may create repetitive work.")
    manager = session.add_answer(answer("Manager", "About eight.", 8, EvidenceKind.ESTIMATE))
    employee = session.add_answer(answer("Employee", "About four.", 4, EvidenceKind.ESTIMATE))
    session.record_conflict(EvidenceConflict(
        "frequency", (manager, employee), "What is representative volume?", "Change logs"))
    assert [a.evidence.value for a in session.answers] == [8, 4]
    assert session.conflicts[0].answer_indexes == (0, 1)
    assert session.conflicts[0].evidence_needed == "Change logs"


def test_unknown_values_remain_unknown():
    unknown = EvidenceValue(None, "requests/month", "Manager", EvidenceKind.UNKNOWN)
    assert unknown.value is None
    assert unknown.kind is EvidenceKind.UNKNOWN
    with pytest.raises(ValueError, match="cannot contain"):
        EvidenceValue(0, "requests/month", "Manager", EvidenceKind.UNKNOWN)


def test_feature_request_does_not_automatically_become_validated_problem():
    finding = DiscoveryFinding("Requested app", "Participant asked for an app.", ())
    assert finding.validated_problem is False
    assert finding.cause_type is CauseType.UNKNOWN


def test_systems_retain_unknown_capabilities():
    system = DiscoveredSystem(
        "Membership platform", "Store memberships", ("Staff",), "Status update",
        unknown_capabilities=("Self-service eligibility rules",))
    assert system.unknown_capabilities == ("Self-service eligibility rules",)
    assert system.owner_vendor == "UNKNOWN"


def test_policy_can_change_interpretation_of_friction():
    finding = DiscoveryFinding(
        "Staff approval", "Approval enforces membership-type eligibility.", (0,),
        CauseType.BUSINESS_POLICY)
    assert finding.cause_type is CauseType.BUSINESS_POLICY
    assert "eligibility" in finding.understanding


def test_evidence_requests_are_generated_for_unresolved_questions():
    session = DiscoverySession("Frequency may matter.")
    request = session.request_evidence(
        "Monthly volume", "Membership change logs", "How often does it happen?")
    assert request in session.evidence_requests
    assert request.possible_evidence == "Membership change logs"


@pytest.mark.parametrize("outcome", [DiscoveryOutcome.STOP, DiscoveryOutcome.MORE_EVIDENCE_REQUIRED])
def test_discovery_supports_non_project_outcomes(outcome):
    session = DiscoverySession("A provisional hypothesis.", outcome=outcome)
    assert session.outcome is outcome
    assert session.project_approved is False
    assert session.selected_solution is None


def test_discovery_cannot_select_custom_build():
    with pytest.raises(ValueError):
        DiscoveryOutcome("CUSTOM_BUILD")
    assert "CUSTOM_BUILD" not in DiscoveryOutcome.__members__


def test_discovery_cannot_mark_a_project_approved():
    session = DiscoverySession("A provisional hypothesis.")
    assert session.project_approved is False
    with pytest.raises(AttributeError):
        session.project_approved = True
