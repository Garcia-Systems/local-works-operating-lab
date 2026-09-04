import pytest

from local_works.audit import (
    AffectedParty, AuditFinding, EvidenceSource, FindingDisposition,
    FrictionObservation, FrictionType, JourneyStage,
)
from local_works.opportunities import (
    DimensionRating, OpportunityAssessment, OpportunityCandidate,
    OpportunityDecision, OpportunityDimension, signal,
)


def finding(title="Membership change", stage=JourneyStage.MANAGE):
    return AuditFinding(
        title,
        FrictionObservation(
            stage, (AffectedParty.CUSTOMER, AffectedParty.EMPLOYEE),
            "Instructions require staff contact.", "The contact may create burden.",
            (EvidenceSource.PUBLIC_WEBSITE,), unknowns=("frequency",),
        ),
        (FrictionType.UNNECESSARY_CALL,), FindingDisposition.NEEDS_MORE_EVIDENCE,
        ("The rule is visible; burden is not.",),
    )


def assessment(decision=OpportunityDecision.MORE_INFORMATION_NEEDED, **changes):
    candidate = OpportunityCandidate.from_finding(
        "Account management", "Membership Account Management", finding(),
        "Routine account changes appear to require staff intervention.",
    )
    values = dict(
        candidate=candidate,
        dimensions={
            OpportunityDimension.FREQUENCY: signal(
                OpportunityDimension.FREQUENCY, "Request frequency has not been measured."
            )
        },
        problem_potential=DimensionRating.MODERATE,
        commercial_fit=DimensionRating.MODERATE,
        positive_signals=("Multiple parties may be affected.",), negative_signals=(),
        unknowns=("request frequency",), hard_disqualifiers=(), decision=decision,
        rationale=("The visible rule merits a bounded decision.",),
    )
    values.update(changes)
    return OpportunityAssessment(**values)


def test_unknowns_remain_unknown():
    item = assessment()
    assert item.dimensions[OpportunityDimension.FREQUENCY].rating is DimensionRating.UNKNOWN
    assert item.unknown_dimensions == (OpportunityDimension.FREQUENCY,)
    assert "request frequency" in item.unknowns


def test_multiple_findings_can_be_explicitly_grouped_into_one_opportunity():
    grouped = OpportunityCandidate.group(
        "Membership Account Management", "Membership Account Management",
        (finding("Freeze"), finding("Cancellation")),
        "Routine changes appear to share staff handling.",
        "Both findings concern changes to an existing membership account.",
    )
    assert len(grouped.source_findings) == 2


def test_unrelated_findings_are_not_automatically_grouped():
    standalone = OpportunityCandidate.from_finding(
        "Membership change", "Membership Account Management", finding(), "Staff contact is required."
    )
    assert len(standalone.source_findings) == 1
    with pytest.raises(ValueError, match="explicit rationale"):
        OpportunityCandidate("Mixed", "Unclear", (finding(), finding(stage=JourneyStage.PAY)),
                             "Two complaints.", "")


def test_strong_problem_does_not_erase_weak_commercial_fit():
    item = assessment(problem_potential=DimensionRating.STRONG,
                      commercial_fit=DimensionRating.WEAK,
                      decision=OpportunityDecision.MORE_INFORMATION_NEEDED)
    assert item.problem_potential is DimensionRating.STRONG
    assert item.commercial_fit is DimensionRating.WEAK


def test_strong_commercial_fit_does_not_create_a_meaningful_problem():
    item = assessment(problem_potential=DimensionRating.WEAK,
                      commercial_fit=DimensionRating.STRONG,
                      decision=OpportunityDecision.LEAVE_ALONE)
    assert item.decision is OpportunityDecision.LEAVE_ALONE


@pytest.mark.parametrize("decision", [
    OpportunityDecision.SIMPLE_IMPROVEMENT,
    OpportunityDecision.LEAVE_ALONE,
    OpportunityDecision.REFER_ELSEWHERE,
])
def test_non_discovery_exit_paths_remain_distinct(decision):
    assert assessment(decision=decision).decision is decision


def test_disqualification_preserves_the_reason():
    item = assessment(decision=OpportunityDecision.DISQUALIFY,
                      hard_disqualifiers=("Requested misrepresentation.",))
    assert item.hard_disqualifiers == ("Requested misrepresentation.",)
    assert item.decision is not OpportunityDecision.REFER_ELSEWHERE


def test_disqualification_without_reason_is_invalid():
    with pytest.raises(ValueError, match="hard disqualifier"):
        assessment(decision=OpportunityDecision.DISQUALIFY)


def test_discovery_warranted_is_not_implementation_or_custom_build():
    item = assessment(decision=OpportunityDecision.DISCOVERY_WARRANTED)
    assert item.implementation_approved is False
    assert item.custom_build_selected is False


def test_decisions_preserve_rationale():
    item = assessment(rationale=("Evidence supports asking focused questions.",))
    assert item.rationale == ("Evidence supports asking focused questions.",)

