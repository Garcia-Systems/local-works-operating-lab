from datetime import date
import pytest
from local_works.closing import *


def make_close(*, authority=AuthorityStatus.CONFIRMED, agreement=AgreementStatus.EXECUTED,
               received=50, assumption=False):
    risks = ([CloseRisk(RiskCategory.ASSUMPTION_RISK, "HIGH", "OPEN", "UNKNOWN", "validate", True)] if assumption else [])
    return CommercialClose("Example", CloseStatus.ACCEPTED_IN_PRINCIPLE,
        CommercialVersionReference("v2", "scope B", "price 1", 100, "50/50", exclusions=("cancellation",)),
        AgreementRecord("Example", None, "Local Works", "Garcia Systems", AgreementReadiness.READY_FOR_AGREEMENT, agreement),
        PaymentCommitment(True, 50, received, PaymentStatus.PAID if received >= 50 else PaymentStatus.PAYMENT_DUE),
        authorities=[AuthorityRecord(AuthorityRole.AUTHORIZED_SIGNER, "Signer", authority)], risks=risks)


def test_acceptance_versions_agreement_and_authorization_are_distinct():
    close = make_close(agreement=AgreementStatus.READY, received=0)
    assert close.customer_decision is CloseStatus.ACCEPTED_IN_PRINCIPLE
    assert close.commercial_version.proposal_version == "v2"
    assert close.commercial_version.scope_version == "scope B"
    assert close.agreement.status is AgreementStatus.READY
    assert close.status is CloseStatus.NOT_STARTED
    assert close.decide() is CloseDecision.HOLD_FOR_PAYMENT


def test_versions_are_mandatory():
    with pytest.raises(ValueError):
        CommercialVersionReference("", "scope", "price", 1, "upfront")


def test_unconfirmed_authority_blocks_authorization():
    close = make_close(authority=AuthorityStatus.UNCONFIRMED)
    assert "Authorized signer authority is not confirmed" in close.hard_blockers
    assert close.decide() is CloseDecision.HOLD_FOR_REQUIREMENT
    with pytest.raises(ValueError): close.record_authorization("Owner", "enthusiasm")


def test_deposit_and_cash_commitments_are_preserved():
    close = make_close(received=25)
    close.commitments += [CommitmentAuthorization("reservation", 80, False, "specialist", "capacity")]
    assert close.payment.deposit_required
    assert close.immediate_commitments == 80
    assert close.cash_exposure == 55
    assert close.available_cash_coverage == 0
    assert close.non_refundable_commitments[0].description == "reservation"
    assert close.decide() is CloseDecision.HOLD_FOR_PAYMENT


def test_preconditions_are_stage_specific_and_critical_can_block():
    close = make_close(assumption=True)
    close.preconditions += [
        Precondition("access", PreconditionStage.REQUIRED_BEFORE_IMPLEMENTATION, RequirementStatus.UNKNOWN),
        Precondition("authority input", PreconditionStage.REQUIRED_BEFORE_AUTHORIZATION, RequirementStatus.UNKNOWN, True)]
    assert {p.stage for p in close.preconditions} == {PreconditionStage.REQUIRED_BEFORE_IMPLEMENTATION, PreconditionStage.REQUIRED_BEFORE_AUTHORIZATION}
    assert close.decide() is CloseDecision.HOLD_FOR_TECHNICAL_VALIDATION


def test_scope_disagreement_and_ownership_question_have_no_fake_resolution():
    close = make_close()
    close.risks.append(CloseRisk(RiskCategory.SCOPE_DISAGREEMENT, "HIGH", "OPEN", "cancellation expected", "reconcile version", True))
    close.ownership_questions.append(OwnershipQuestion("Who owns source?"))
    assert close.decide() is CloseDecision.HOLD_FOR_REQUIREMENT
    assert close.ownership_questions[0].status == "NEEDS_REVIEW"


def test_target_and_committed_start_are_distinct_without_partner_selection():
    close = make_close()
    close.target_start_date = date(2030, 1, 1)
    assert close.committed_start_date is None
    assert not close.delivery_partner_selected
    assert not close.implementation_started
    close.record_authorization("Owner", "controls satisfied")
    assert close.status is CloseStatus.AUTHORIZED
    assert not close.implementation_started


def test_hold_decline_and_cancel_before_start_are_representable():
    close = make_close(); close.status = CloseStatus.ON_HOLD
    assert close.status is CloseStatus.ON_HOLD
    close.status = CloseStatus.DECLINED
    assert close.decide() is CloseDecision.DECLINE_BEFORE_START
    close.status = CloseStatus.CANCELLED_BEFORE_START
    assert close.decide() is CloseDecision.CANCEL_BEFORE_START


def test_model_is_training_not_legal_or_execution_system():
    close = make_close()
    assert "qualified counsel" in close.agreement.legal_note
    assert not hasattr(close, "select_delivery_partner")
    assert not hasattr(close, "start_implementation")
