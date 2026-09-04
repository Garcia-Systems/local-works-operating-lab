from local_works.projects import *

def req(**kw):
    values=dict(requirement_id="R-001",statement="Record the result",requirement_type=RequirementType.FUNCTIONAL,priority=RequirementPriority.MUST,source=RequirementSource.SCOPE,evidence_reference="S-v1")
    values.update(kw); return Requirement(**values)

def kickoff(**kw):
    values=dict(commercial_authorized=True,delivery_path_selected=True,scope_version="S-v1",commercial_version="P-v2",estimate_reference="E-1",control_risks_ready=True,responsibilities_known=True,customer_participants_identified=True,local_works_participants_identified=True,delivery_participants_identified=True,access_requests_identified=True,context_available=True)
    values.update(kw); return Kickoff(**values)

def question(blocking=False, category=QuestionCategory.TECHNICAL): return OpenQuestion("Q-1","Question?",category,"Owner","Matters",blocking)

def test_project_preserves_sources_and_does_not_start_implementation():
    p=Project("P","Business","close-1","proposal-2","scope-3","estimate-4",("freeze",),("cancellation",))
    assert (p.commercial_source,p.scope_version)==("close-1","scope-3")
    assert p.status is ProjectStatus.AUTHORIZED

def test_kickoff_readiness_gates():
    assert kickoff(commercial_authorized=False).readiness() is KickoffStatus.NEEDS_COMMERCIAL_CLARIFICATION
    assert kickoff().readiness() is KickoffStatus.READY_FOR_KICKOFF

def test_participant_preserves_role_and_authority():
    p=ProjectParticipant(ParticipantRole.CUSTOMER_DECISION_MAKER,"Customer",("Decide",),("BUSINESS_RULES",))
    assert p.role is ParticipantRole.CUSTOMER_DECISION_MAKER and p.decision_authority==("BUSINESS_RULES",)

def test_requirement_preserves_type_priority_provenance_and_acceptance():
    r=req(requirement_type=RequirementType.DATA,acceptance_linkage=("AC-1",))
    assert r.requirement_type is RequirementType.DATA and r.priority is RequirementPriority.MUST
    assert r.source is RequirementSource.SCOPE and r.evidence_reference=="S-v1" and r.acceptance_linkage==("AC-1",)
    assert not hasattr(r,"database_schema")

def test_scope_stays_distinct_and_feature_dump_is_out_of_scope():
    p=Project("P","B","C","P","S","E",("freeze",),("cancellation",))
    r=p.request_feature("Add cancellation")
    assert p.approved_scope==("freeze",) and r.status is RequirementStatus.OUT_OF_SCOPE and r.priority is RequirementPriority.NOT_IN_SCOPE

def test_requirement_can_preserve_uncertainty_and_business_rule_type():
    r=req(requirement_type=RequirementType.BUSINESS_RULE,status=RequirementStatus.NEEDS_CLARIFICATION)
    assert r.requirement_type is RequirementType.BUSINESS_RULE and r.status is RequirementStatus.NEEDS_CLARIFICATION
    design=TechnicalDesign("Use a queue worker",(r.requirement_id,))
    assert design.statement not in r.statement

def test_questions_can_block_or_not_block():
    assert question(True).blocking and not question(False).blocking

def test_baseline_versions_and_change_classification():
    b=RequirementBaseline("2",[req()],prior_version="1")
    assert b.prior_version=="1"
    assert b.classify_new_information("Which manager approves exceptions?",("freeze",)) is RequirementDecision.CLARIFICATION
    assert b.classify_new_information("Add cancellation",("freeze",)) is RequirementDecision.SCOPE_CHANGE

def test_readiness_results():
    b=RequirementBaseline("1",[req(status=RequirementStatus.READY_FOR_IMPLEMENTATION)])
    assert b.readiness([question(True)]) is ImplementationReadiness.NEEDS_TECHNICAL_VALIDATION
    assert b.readiness([question(False)]) is ImplementationReadiness.READY_WITH_OPEN_NONBLOCKERS
    assert b.readiness([]) is ImplementationReadiness.READY_FOR_IMPLEMENTATION
    blocked=RequirementBaseline("1",[req(status=RequirementStatus.BLOCKED)])
    assert blocked.readiness([]) is ImplementationReadiness.BLOCKED
