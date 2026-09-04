import pytest

from local_works.audit import (
    AffectedParty, AuditFinding, AuditRecommendation, Confidence,
    DigitalFrictionAudit, EvidenceSource, FindingDisposition, Frequency,
    FrictionObservation, FrictionType, JourneyStage, Severity,
)
from local_works.hypothesis import EvidenceType


def observation(**changes):
    values = dict(
        journey_stage=JourneyStage.MANAGE,
        affected_parties=(AffectedParty.CUSTOMER, AffectedParty.EMPLOYEE),
        observed_fact="The instructions require a call.",
        friction_hypothesis="The call may create avoidable work.",
        evidence_sources=(EvidenceSource.PUBLIC_WEBSITE,),
    )
    values.update(changes)
    return FrictionObservation(**values)


def finding(**changes):
    values = dict(
        title="Account change",
        observation=observation(),
        friction_types=(FrictionType.UNNECESSARY_CALL,),
        disposition=FindingDisposition.NEEDS_MORE_EVIDENCE,
        significance_reasoning=("Public evidence establishes the rule, not its burden.",),
    )
    values.update(changes)
    return AuditFinding(**values)


def test_journey_framework_has_all_expected_stages():
    assert [stage.name for stage in JourneyStage] == [
        "FIND", "UNDERSTAND", "CONTACT", "BOOK_OR_JOIN", "PAY",
        "RECEIVE_SERVICE", "MANAGE", "RETURN",
    ]


def test_irrelevant_stages_can_be_omitted():
    audit = DigitalFrictionAudit("Restaurant", (JourneyStage.FIND, JourneyStage.PAY), (),
                                 AuditRecommendation.NO_MEANINGFUL_FRICTION, ("No issue found.",))
    assert JourneyStage.MANAGE not in audit.journey_stages


def test_unknown_is_preserved_and_not_silently_low():
    item = observation()
    assert item.frequency is Frequency.UNKNOWN
    assert item.severity is Severity.UNKNOWN
    assert item.frequency is not Frequency.RARE
    assert item.severity is not Severity.LOW


def test_observation_and_hypothesis_are_distinct_fields():
    item = observation()
    assert item.observed_fact == "The instructions require a call."
    assert item.friction_hypothesis == "The call may create avoidable work."


def test_evidence_sources_status_and_affected_parties_are_preserved():
    item = observation(
        evidence_sources=(EvidenceSource.PUBLIC_WEBSITE, EvidenceSource.MEASURED_DATA),
        evidence_status=EvidenceType.MEASURED,
        confidence=Confidence.MEASURED,
    )
    assert item.evidence_sources == (EvidenceSource.PUBLIC_WEBSITE, EvidenceSource.MEASURED_DATA)
    assert item.affected_parties == (AffectedParty.CUSTOMER, AffectedParty.EMPLOYEE)
    assert item.evidence_status is EvidenceType.MEASURED


@pytest.mark.parametrize("disposition", [
    FindingDisposition.WORKING_ADEQUATELY,
    FindingDisposition.LOW_SIGNIFICANCE,
])
def test_audit_can_contain_non_problem_and_positive_findings(disposition):
    item = finding(disposition=disposition)
    audit = DigitalFrictionAudit("Gym", (JourneyStage.MANAGE,), (item,),
                                 AuditRecommendation.MONITOR, ("No urgent action.",))
    assert audit.findings_by_disposition(disposition) == (item,)


def test_false_positive_can_be_downgraded_with_new_evidence():
    initial = finding(disposition=FindingDisposition.WORTH_INVESTIGATING)
    updated_observation = observation(
        evidence_sources=(EvidenceSource.PUBLIC_WEBSITE, EvidenceSource.MANAGER_STATEMENT),
        frequency=Frequency.RARE,
        severity=Severity.LOW,
        policy_or_regulatory_reason="Identity verification is required.",
    )
    revised = initial.revised(
        observation=updated_observation,
        disposition=FindingDisposition.LOW_SIGNIFICANCE,
        significance_reasoning=("Rare and required verification.",),
    )
    assert revised.disposition is FindingDisposition.LOW_SIGNIFICANCE
    assert initial.disposition is FindingDisposition.WORTH_INVESTIGATING


def test_recommendations_cannot_name_or_automatically_recommend_custom_build():
    assert "CUSTOM_BUILD_RECOMMENDED" not in AuditRecommendation.__members__
    audit = DigitalFrictionAudit("Gym", (JourneyStage.MANAGE,), (finding(),),
                                 AuditRecommendation.DISCOVERY_RECOMMENDED,
                                 ("Investigate burden.",))
    assert audit.implementation_recommended is False
    assert audit.recommendation is AuditRecommendation.DISCOVERY_RECOMMENDED


def test_findings_outside_selected_journey_are_rejected():
    with pytest.raises(ValueError):
        DigitalFrictionAudit("Gym", (JourneyStage.FIND,), (finding(),),
                             AuditRecommendation.INSUFFICIENT_INFORMATION, ("Ask questions.",))
