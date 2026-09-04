"""Commercial close controls for Chapter 17.

These records support operational training.  They do not create contracts,
legal advice, payments, purchases, delivery-partner selections, or project work.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class CloseStatus(Enum):
    NOT_STARTED = "Not started"
    CUSTOMER_INTEREST = "Customer interest"
    ACCEPTED_IN_PRINCIPLE = "Accepted in principle"
    AWAITING_AGREEMENT = "Awaiting agreement"
    AWAITING_PAYMENT = "Awaiting payment"
    AWAITING_PRECONDITIONS = "Awaiting preconditions"
    READY_TO_AUTHORIZE = "Ready to authorize"
    AUTHORIZED = "Authorized for delivery preparation"
    ON_HOLD = "On hold"
    DECLINED = "Declined"
    WITHDRAWN = "Withdrawn"
    CANCELLED_BEFORE_START = "Cancelled before start"


class CloseDecision(Enum):
    AUTHORIZE_NEXT_STAGE = "Authorize next stage"
    HOLD_FOR_REQUIREMENT = "Hold for requirement"
    HOLD_FOR_PAYMENT = "Hold for payment"
    HOLD_FOR_TECHNICAL_VALIDATION = "Hold for technical validation"
    HOLD_FOR_CUSTOMER_ACTION = "Hold for customer action"
    RESTRUCTURE_DEAL = "Restructure deal"
    DECLINE_BEFORE_START = "Decline before start"
    CANCEL_BEFORE_START = "Cancel before start"


class RequirementStatus(Enum):
    SATISFIED = "Satisfied"
    NOT_SATISFIED = "Not satisfied"
    NOT_APPLICABLE = "Not applicable"
    UNKNOWN = "Unknown"


class AuthorityStatus(Enum):
    CONFIRMED = "Confirmed"
    UNCONFIRMED = "Unconfirmed"
    INSUFFICIENT = "Insufficient"


class AuthorityRole(Enum):
    DECISION_MAKER = "Decision maker"
    BUDGET_OWNER = "Budget owner"
    AUTHORIZED_SIGNER = "Authorized signer"
    TECHNICAL_APPROVER = "Technical approver"
    PROCUREMENT_CONTACT = "Procurement contact"


class AgreementStatus(Enum):
    NOT_STARTED = "Not started"
    READY = "Ready"
    SENT = "Sent"
    EXECUTED = "Executed"
    NEEDS_REVISION = "Needs revision"


class AgreementReadiness(Enum):
    READY_FOR_AGREEMENT = "Ready for agreement"
    NEEDS_COMMERCIAL_CLARIFICATION = "Needs commercial clarification"
    NEEDS_SCOPE_REVISION = "Needs scope revision"
    NEEDS_RISK_REVIEW = "Needs risk review"


class PaymentStatus(Enum):
    NOT_REQUIRED = "Not required"
    INVOICE_READY = "Invoice ready"
    INVOICE_SENT = "Invoice sent"
    PAYMENT_DUE = "Payment due"
    PARTIALLY_PAID = "Partially paid"
    PAID = "Paid"
    OVERDUE = "Overdue"
    WAIVED = "Waived"


class PreconditionStage(Enum):
    REQUIRED_BEFORE_AUTHORIZATION = "Before authorization"
    REQUIRED_BEFORE_IMPLEMENTATION = "Before implementation"
    REQUIRED_BEFORE_LAUNCH = "Before launch"


class DeliveryCapacity(Enum):
    AVAILABLE = "Available"
    TENTATIVE = "Tentative"
    UNAVAILABLE = "Unavailable"
    UNKNOWN = "Unknown"


class SubcontractorUse(Enum):
    ALLOWED = "Allowed"
    REQUIRES_NOTICE = "Requires notice"
    REQUIRES_APPROVAL = "Requires approval"
    UNKNOWN = "Unknown"


class RiskCategory(Enum):
    AUTHORITY_RISK = "Authority risk"
    VERSION_MISMATCH = "Version mismatch"
    PAYMENT_RISK = "Payment risk"
    CASH_EXPOSURE = "Cash exposure"
    SCOPE_DISAGREEMENT = "Scope disagreement"
    ASSUMPTION_RISK = "Assumption risk"
    ACCESS_RISK = "Access risk"
    DELIVERY_CAPACITY_RISK = "Delivery capacity risk"
    THIRD_PARTY_RISK = "Third-party risk"
    OWNERSHIP_RISK = "Ownership risk"
    SECURITY_ACCESS_RISK = "Security/access risk"
    CUSTOMER_DELAY_RISK = "Customer delay risk"
    OTHER = "Other"


@dataclass(frozen=True)
class CommercialVersionReference:
    proposal_version: str
    scope_version: str
    pricing_version: str
    price: float
    payment_structure: str
    assumptions: tuple[str, ...] = ()
    exclusions: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.proposal_version.strip() or not self.scope_version.strip():
            raise ValueError("Accepted proposal and scope versions are required.")
        if self.price < 0:
            raise ValueError("Price cannot be negative.")


@dataclass(frozen=True)
class AuthorityRecord:
    role: AuthorityRole
    person: str
    status: AuthorityStatus
    evidence: str = "UNKNOWN"


@dataclass(frozen=True)
class AgreementRecord:
    customer_display_name: str
    customer_contracting_entity: str | None
    local_works_brand: str
    local_works_contracting_entity: str | None
    readiness: AgreementReadiness
    status: AgreementStatus
    topics_reviewed: tuple[str, ...] = ()
    legal_note: str = "Agreement topics should be reviewed with qualified counsel."


@dataclass(frozen=True)
class PaymentCommitment:
    deposit_required: bool
    deposit_amount: float
    funds_received: float
    status: PaymentStatus

    def __post_init__(self) -> None:
        if min(self.deposit_amount, self.funds_received) < 0:
            raise ValueError("Payment amounts cannot be negative.")

    @property
    def required_deposit_received(self) -> bool:
        return not self.deposit_required or self.funds_received >= self.deposit_amount


@dataclass(frozen=True)
class CommitmentAuthorization:
    description: str
    amount: float
    refundable: bool
    party_being_paid: str
    reason: str
    customer_funds_received: float = 0.0
    approved_by: str | None = None
    status: RequirementStatus = RequirementStatus.NOT_SATISFIED

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Commitment amount cannot be negative.")


@dataclass(frozen=True)
class Precondition:
    description: str
    stage: PreconditionStage
    status: RequirementStatus
    critical: bool = False


@dataclass(frozen=True)
class CloseRequirement:
    description: str
    status: RequirementStatus
    blocking: bool = False


@dataclass(frozen=True)
class CloseRisk:
    category: RiskCategory
    severity: str
    status: str
    evidence: str
    mitigation: str
    blocking: bool = False


@dataclass(frozen=True)
class OwnershipQuestion:
    question: str
    status: str = "NEEDS_REVIEW"


@dataclass(frozen=True)
class AuthorizationRecord:
    decision: CloseDecision
    authorized_by: str | None
    reason: str
    recorded_on: date | None = None
    implementation_started: bool = False


@dataclass
class CommercialClose:
    business_display_name: str
    customer_decision: CloseStatus
    commercial_version: CommercialVersionReference
    agreement: AgreementRecord
    payment: PaymentCommitment
    authorities: list[AuthorityRecord] = field(default_factory=list)
    commitments: list[CommitmentAuthorization] = field(default_factory=list)
    preconditions: list[Precondition] = field(default_factory=list)
    requirements: list[CloseRequirement] = field(default_factory=list)
    risks: list[CloseRisk] = field(default_factory=list)
    ownership_questions: list[OwnershipQuestion] = field(default_factory=list)
    subcontractor_use: SubcontractorUse = SubcontractorUse.UNKNOWN
    delivery_capacity: DeliveryCapacity = DeliveryCapacity.UNKNOWN
    target_start_date: date | None = None
    committed_start_date: date | None = None
    status: CloseStatus = CloseStatus.NOT_STARTED
    authorization: AuthorizationRecord | None = None
    delivery_partner_selected: bool = False
    implementation_started: bool = False

    @property
    def immediate_commitments(self) -> float:
        return sum(item.amount for item in self.commitments)

    @property
    def non_refundable_commitments(self) -> tuple[CommitmentAuthorization, ...]:
        return tuple(item for item in self.commitments if not item.refundable)

    @property
    def available_cash_coverage(self) -> float:
        return max(0.0, self.payment.funds_received - self.immediate_commitments)

    @property
    def cash_exposure(self) -> float:
        return max(0.0, self.immediate_commitments - self.payment.funds_received)

    @property
    def hard_blockers(self) -> tuple[str, ...]:
        blockers = [item.description for item in self.requirements
                    if item.blocking and item.status is not RequirementStatus.SATISFIED]
        blockers.extend(risk.category.value for risk in self.risks if risk.blocking and risk.status != "RESOLVED")
        required_roles = {AuthorityRole.AUTHORIZED_SIGNER}
        for role in required_roles:
            if not any(a.role is role and a.status is AuthorityStatus.CONFIRMED for a in self.authorities):
                blockers.append(f"{role.value} authority is not confirmed")
        if self.agreement.status is not AgreementStatus.EXECUTED:
            blockers.append("Required agreement is not executed")
        if not self.payment.required_deposit_received:
            blockers.append("Required deposit is not received")
        blockers.extend(p.description for p in self.preconditions
                        if p.stage is PreconditionStage.REQUIRED_BEFORE_AUTHORIZATION
                        and p.status is not RequirementStatus.SATISFIED)
        return tuple(dict.fromkeys(blockers))

    def decide(self) -> CloseDecision:
        """Make a conservative next-stage decision; never start implementation."""
        if self.status is CloseStatus.CANCELLED_BEFORE_START:
            return CloseDecision.CANCEL_BEFORE_START
        if self.status is CloseStatus.DECLINED:
            return CloseDecision.DECLINE_BEFORE_START
        if not self.payment.required_deposit_received:
            return CloseDecision.HOLD_FOR_PAYMENT
        if any(r.blocking and r.category is RiskCategory.ASSUMPTION_RISK and r.status != "RESOLVED"
               for r in self.risks):
            return CloseDecision.HOLD_FOR_TECHNICAL_VALIDATION
        if self.hard_blockers:
            return CloseDecision.HOLD_FOR_REQUIREMENT
        return CloseDecision.AUTHORIZE_NEXT_STAGE

    def record_authorization(self, authorized_by: str, reason: str) -> AuthorizationRecord:
        decision = self.decide()
        if decision is not CloseDecision.AUTHORIZE_NEXT_STAGE:
            raise ValueError(f"Cannot authorize: {decision.name}")
        self.status = CloseStatus.AUTHORIZED
        self.authorization = AuthorizationRecord(decision, authorized_by, reason)
        return self.authorization
