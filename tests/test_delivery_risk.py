from dataclasses import fields
from local_works.delivery_risk import *


def control(kind=AssetType.SOURCE_REPOSITORY, party=ControlParty.CUSTOMER,
            recovery="organizational recovery", backup=(ControlParty.LOCAL_WORKS,)):
    return AssetControl(DeliveryAsset("asset", kind, "Customer under fictional agreement"),
                        party, (party,), backup, recovery, "Portable", ControlStatus.CONTROLLED)


def test_legal_ownership_is_distinct_from_operational_control_and_preserved():
    item = control(party=ControlParty.LOCAL_WORKS)
    assert item.asset.legal_owner == "Customer under fictional agreement"
    assert item.primary_controller is ControlParty.LOCAL_WORKS


def test_asset_control_backup_and_recovery_are_represented():
    item = control()
    assert item.primary_controller is ControlParty.CUSTOMER
    assert item.backup_access == (ControlParty.LOCAL_WORKS,)
    assert item.has_recovery_path


def test_access_metadata_neither_requires_nor_offers_a_secret_field():
    access = AccessRecord("platform", ControlParty.DELIVERY_PARTNER, "test editor", "validation")
    assert access.expected_revocation is None
    assert "secret" not in {f.name for f in fields(AccessRecord)}
    assert "password" not in {f.name for f in fields(AccessRecord)}


def test_source_control_deployment_and_partner_account_risks():
    source = control(party=ControlParty.DELIVERY_PARTNER, recovery="UNKNOWN", backup=())
    deployment = control(AssetType.DEPLOYMENT_CONFIGURATION, ControlParty.SHARED, "UNKNOWN")
    account = control(AssetType.HOSTING_ACCOUNT, ControlParty.DELIVERY_PARTNER, "partner transfer process", ())
    risks = detect_control_risks([source, deployment, account])
    assert {r.category for r in risks} == {RiskCategory.SOURCE_CONTROL, RiskCategory.DEPLOYMENT_RECOVERY, RiskCategory.ACCOUNT_CONTROL}
    assert any(r.blocking for r in risks)


def test_responsibility_assignment_gap_and_overlap():
    assigned = ResponsibilityAssignment(ResponsibilityType.TECHNICAL_DESIGN, ControlParty.DELIVERY_PARTNER, (ControlParty.DELIVERY_PARTNER,), (ControlParty.LOCAL_WORKS,), (ControlParty.CUSTOMER,))
    gap = ResponsibilityAssignment(ResponsibilityType.MONITORING, None)
    overlap = ResponsibilityAssignment(ResponsibilityType.DEPLOYMENT, ControlParty.LOCAL_WORKS, (ControlParty.CUSTOMER, ControlParty.LOCAL_WORKS, ControlParty.DELIVERY_PARTNER))
    readiness = DeliveryReadiness(responsibilities=[assigned, gap, overlap])
    assert assigned.performing == (ControlParty.DELIVERY_PARTNER,)
    assert readiness.responsibility_gaps() == [gap]
    assert readiness.authority_overlaps() == [overlap]


def test_knowledge_may_be_required_but_undocumented():
    artifact = KnowledgeArtifact("rules", KnowledgeCategory.BUSINESS_RULES, True, ControlParty.CUSTOMER, False)
    assert artifact.required and not artifact.documented
    assert artifact.transition_readiness is ContinuityResult.UNKNOWN


def test_third_party_dependency_is_explicit_not_assumed_controlled():
    dep = ThirdPartyDependency("vendor API", "Critical", ControlParty.CUSTOMER, "delegated",
                               "vendor support", "rate limit unknown", "sync stops", "manual entry", "OPEN")
    assert dep.owner is ControlParty.CUSTOMER
    assert dep.known_limitation == "rate limit unknown"


def test_partner_and_local_works_disappearance_can_be_evaluated():
    partner = [ContinuityRequirement("source", ContinuityResult.RECOVERABLE),
               ContinuityRequirement("deployment", ContinuityResult.RECOVERABLE_WITH_EFFORT)]
    local_works = [ContinuityRequirement("customer record", ContinuityResult.RECOVERABLE)]
    assert evaluate_continuity(partner) is ContinuityResult.RECOVERABLE_WITH_EFFORT
    assert evaluate_continuity(local_works) is ContinuityResult.RECOVERABLE
    assert evaluate_continuity([ContinuityRequirement("unknown", ContinuityResult.UNKNOWN)]) is ContinuityResult.UNKNOWN


def test_key_asset_without_recovery_blocks_readiness():
    assessment = DeliveryReadiness(controls=[control(party=ControlParty.DELIVERY_PARTNER, recovery="UNKNOWN", backup=())])
    assert assessment.assess() is DeliveryReadinessDecision.BLOCKED
    assert not assessment.kickoff_started


def test_noncritical_documentation_gap_can_be_monitored():
    risk = DeliveryRisk("minor note absent", RiskCategory.DOCUMENTATION_GAP, RiskSeverity.LOW,
                        "note pending", "complete at handoff", ControlParty.DELIVERY_PARTNER,
                        False, RiskStatus.MONITORED)
    assert DeliveryReadiness(risks=[risk]).assess() is DeliveryReadinessDecision.READY_WITH_MONITORED_RISKS


def test_readiness_can_be_ready_or_blocked_and_never_starts_kickoff():
    ready = DeliveryReadiness(controls=[control()])
    assert ready.assess() is DeliveryReadinessDecision.READY_FOR_KICKOFF
    blocking = DeliveryRisk("no recovery", RiskCategory.ACCOUNT_CONTROL, RiskSeverity.CRITICAL,
                            "external-only", "add recovery", ControlParty.LOCAL_WORKS, True)
    stopped = DeliveryReadiness(risks=[blocking])
    assert stopped.assess() is DeliveryReadinessDecision.BLOCKED
    assert not ready.kickoff_started and not stopped.kickoff_started


def test_not_applicable_source_does_not_create_fictional_risk():
    source = AssetControl(DeliveryAsset("source", AssetType.SOURCE_REPOSITORY), ControlParty.UNKNOWN,
                          status=ControlStatus.NOT_APPLICABLE)
    assert detect_control_risks([source]) == []
