import pytest

from local_works.partners import (
    CandidateStatus, DeliveryAssessment, DeliveryCandidate, DeliveryCapability,
    DeliveryDecision, DeliveryNeed, DeliveryPath, DeliveryPathType, DeliveryRisk,
    EvidenceType, FitRating, PartnerEvidence, QualificationDecision,
    RequirementLevel, RiskCategory, RiskSeverity, SubcontractingStatus,
)


def candidate(name="Candidate", cost=3000):
    return DeliveryCandidate(
        name, DeliveryPathType.SPECIALIST_FREELANCER,
        [DeliveryCapability("API integration", FitRating.STRONG,
            (PartnerEvidence("Built integrations", EvidenceType.SELF_REPORTED),)),
         DeliveryCapability("Support handoff", FitRating.ADEQUATE)],
        availability="AVAILABLE FROM OCTOBER", capacity_hours_per_week=5,
        documentation=FitRating.ADEQUATE, support_handoff=FitRating.ADEQUATE,
        cost=cost, subcontracting=SubcontractingStatus.POSSIBLE,
        status=CandidateStatus.UNDER_REVIEW,
    )


def assessment(*candidates):
    return DeliveryAssessment("Harbor Fitness", "CONFIGURE_FIRST", "Validation only",
        [DeliveryNeed("Platform configuration", "HIGH", RequirementLevel.REQUIRED,
                      "Chapter 17 capability precondition")], candidates=list(candidates))


def test_needs_remain_distinct_from_candidate_capabilities():
    item = candidate()
    record = assessment(item)
    assert record.needs[0].capability == "Platform configuration"
    assert item.capabilities[0].capability == "API integration"


def test_path_and_evidence_types_are_preserved():
    item = candidate()
    path = DeliveryPath(DeliveryPathType.MIXED_TEAM, ("combined context",), ("coordination",))
    assert item.path_type is DeliveryPathType.SPECIALIST_FREELANCER
    assert path.path_type is DeliveryPathType.MIXED_TEAM
    assert item.capabilities[0].evidence[0].evidence_type is EvidenceType.SELF_REPORTED


def test_strong_technician_can_be_wrong_delivery_fit():
    item = candidate()
    record = assessment(item)
    record.qualify(item.name, QualificationDecision.WRONG_DELIVERY_MODEL)
    assert item.capabilities[0].rating is FitRating.STRONG
    assert item.status is CandidateStatus.NOT_QUALIFIED


def test_availability_is_distinct_from_capacity():
    item = candidate()
    assert item.availability.startswith("AVAILABLE")
    assert item.capacity_hours_per_week == 5


def test_cheapest_is_not_automatically_preferred():
    cheap, higher = candidate("Cheap", 1500), candidate("Higher", 3000)
    record = assessment(cheap, higher)
    record.qualify("Cheap", QualificationDecision.NEEDS_MORE_INFORMATION)
    record.qualify("Higher", QualificationDecision.QUALIFIED_FOR_ESTIMATE)
    assert record.qualified_for_estimate == ("Higher",)


@pytest.mark.parametrize("category", [
    RiskCategory.SOURCE_CONTROL, RiskCategory.CREDENTIAL_CONTROL,
    RiskCategory.KEY_PERSON_DEPENDENCY,
])
def test_continuity_risks_can_be_represented(category):
    risk = DeliveryRisk(category, "Critical asset held by one provider", RiskSeverity.HIGH,
                        "Proposed operating setup", "Shared control and handoff")
    assert risk.category is category
    assert risk.mitigation


def test_open_critical_risk_prevents_qualification():
    item = candidate()
    item.risks.append(DeliveryRisk(RiskCategory.SOURCE_CONTROL, "Personal repository only",
        RiskSeverity.CRITICAL, "Candidate proposal", "Require shared repository", disqualifying=True))
    record = assessment(item)
    with pytest.raises(ValueError):
        record.qualify(item.name, QualificationDecision.QUALIFIED_FOR_ESTIMATE)
    record.qualify(item.name, QualificationDecision.TOO_RISKY)
    assert item.status is CandidateStatus.NOT_QUALIFIED


def test_subcontracting_documentation_and_handoff_are_explicit():
    item = candidate()
    assert item.subcontracting is SubcontractingStatus.POSSIBLE
    assert item.documentation is FitRating.ADEQUATE
    assert item.capability("Support handoff").rating is FitRating.ADEQUATE


@pytest.mark.parametrize("decision,status", [
    (QualificationDecision.QUALIFIED_FOR_ESTIMATE, CandidateStatus.QUALIFIED),
    (QualificationDecision.NEEDS_MORE_INFORMATION, CandidateStatus.UNDER_REVIEW),
    (QualificationDecision.NOT_QUALIFIED, CandidateStatus.NOT_QUALIFIED),
])
def test_qualification_states(decision, status):
    item = candidate()
    record = assessment(item)
    record.qualify(item.name, decision)
    assert item.status is status


def test_assessment_stops_before_estimate_selection_and_work():
    record = assessment(candidate())
    assert not record.technical_estimate_created
    assert not record.final_provider_selected
    assert not record.implementation_started


def test_delivery_decision_is_an_estimate_request_not_final_selection():
    decision = DeliveryDecision(("Candidate",), "Fit warrants comparable estimate",
        DeliveryPathType.SPECIALIST_FREELANCER, "Transition-ready documentation")
    assert decision.estimate_request_set == ("Candidate",)
    assert not decision.final_provider_selected
    with pytest.raises(ValueError):
        DeliveryDecision(("Candidate",), "winner", DeliveryPathType.SPECIALIST_FREELANCER,
                         "none", final_provider_selected=True)
