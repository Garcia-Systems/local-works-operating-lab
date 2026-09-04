from pathlib import Path

from local_works.capstone import (
    BusinessHealth, FinalBusinessScorecard, FinalBusinessVerdict,
    FinalEvidenceAssessment, ProductionApproach, ProductionCapabilityPriority,
    ProductionSoftwareVerdict, ScorecardDimension, assess_final_business,
    classify_final_verdict,
)


def test_assessment_consumes_prior_objects_and_preserves_simulation_evidence():
    exam=assess_final_business()
    assert exam.owner_income.simulation is exam.baseline
    assert exam.scenarios and exam.sensitivities and exam.operating_models
    assert exam.evidence_quality is FinalEvidenceAssessment.SIMULATION_ONLY
    assert exam.evidence_quality is not FinalEvidenceAssessment.STRONGLY_VALIDATED
    assert exam.primary_bottleneck == exam.baseline.primary_bottleneck
    assert exam.sensitivities[0].assumption


def test_transparent_policy_supports_required_primary_outcomes():
    common=dict(full_time_target=75_000, side_business_floor=15_000)
    assert classify_final_verdict(annual_owner_income=90_000, **common) is FinalBusinessVerdict.VIABLE
    assert classify_final_verdict(annual_owner_income=90_000, minimum_cash=-1, **common) is FinalBusinessVerdict.VIABLE_WITH_CHANGES
    assert classify_final_verdict(annual_owner_income=30_000, **common) is FinalBusinessVerdict.VIABLE_AS_SIDE_BUSINESS
    assert classify_final_verdict(annual_owner_income=90_000, adverse_income_ratio=.2, **common) is FinalBusinessVerdict.FRAGILE
    assert classify_final_verdict(annual_owner_income=0, **common) is FinalBusinessVerdict.NOT_CURRENTLY_VIABLE
    assert classify_final_verdict(annual_owner_income=90_000, evidence=FinalEvidenceAssessment.UNKNOWN, **common) is FinalBusinessVerdict.INSUFFICIENT_EVIDENCE


def test_unknown_and_multiple_qualifiers_are_preserved():
    card=FinalBusinessScorecard((ScorecardDimension('QUALITY',BusinessHealth.UNKNOWN,'none','unknown','observe'),))
    assert card.get('QUALITY').status is BusinessHealth.UNKNOWN
    assert len(assess_final_business().qualifiers) > 1


def test_conditions_income_quality_gaps_and_experiments_are_multidimensional():
    exam=assess_final_business()
    assert exam.success_conditions and exam.failure_conditions
    assert exam.owner_income_quality.name == 'MIXED'  # volatile and cash-exposed despite amount
    assert exam.operating_model_verdict.name == 'SIDE_BUSINESS_PREFERRED'
    assert exam.evidence_gaps[0].validation_priority.name == 'CRITICAL_NEXT'
    assert exam.experiments[0].assumption == exam.evidence_gaps[0].current_assumption


def test_software_gate_manual_tools_and_public_portal_split():
    exam=assess_final_business()
    assert exam.software_verdict is ProductionSoftwareVerdict.MORE_BUSINESS_VALIDATION_FIRST
    approaches={c.capability:c.approach for c in exam.capabilities}
    priorities={c.capability:c.priority for c in exam.capabilities}
    assert approaches['CRM'] is ProductionApproach.CONFIGURE
    assert approaches['customer portal'] is ProductionApproach.LEAVE_ALONE
    assert priorities['customer portal'] is ProductionCapabilityPriority.DO_NOT_BUILD_YET
    assert exam.primary_verdict.name != exam.software_verdict.name


def test_artifacts_never_turn_harbor_or_simulation_into_real_proof():
    root=Path(__file__).parents[1]
    exam=(root/'artifacts/32-final-local-works-examination.md').read_text()
    requirements=(root/'artifacts/production-application-requirements-summary.md').read_text()
    assert 'FICTIONAL SIMULATION ONLY' in exam
    assert 'Harbor Fitness is fictional' in exam
    assert 'No production application is authorized' in requirements
    assert not (root/'book/33').exists()
    assert not (root/'artisan').exists()
