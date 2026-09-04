"""Evidence-linked proposal and negotiation decisions for Chapter 16.

The objects in this module are decision records, not contracts, invoices,
signatures, project authorizations, or a proposal-delivery system.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from local_works.economics import EvidenceStatus
from local_works.pricing import (
    ContributionAnalysis,
    DiscountResult,
    PaymentStructure,
    PriceScenario,
    discount_sensitivity,
)
from local_works.scope import ProjectScope, RequestDisposition


class ProposalStatus(Enum):
    DRAFT = "Draft"
    INTERNAL_REVIEW = "Internal review"
    READY_TO_PRESENT = "Ready to present"
    PRESENTED = "Presented"
    REVISION_REQUESTED = "Revision requested"
    ACCEPTED = "Accepted"
    DECLINED = "Declined"
    EXPIRED = "Expired"
    WITHDRAWN = "Withdrawn"


class ProposalDecision(Enum):
    ACCEPTED_IN_PRINCIPLE = "Accepted in principle"
    REVISION_REQUESTED = "Revision requested"
    POSTPONED = "Postponed"
    DECLINED = "Declined"
    WITHDRAWN_BY_LOCAL_WORKS = "Withdrawn by Local Works"
    NO_HEALTHY_DEAL = "No healthy deal"
    EXPIRED = "Expired"


class OptionStatus(Enum):
    OPTIONAL = "Optional"
    DEFERRED = "Deferred"
    FUTURE_DISCOVERY = "Future discovery"


class NegotiationIssue(Enum):
    PRICE = "Price"
    SCOPE = "Scope"
    TIMING = "Timing"
    PHASING = "Phasing"
    PAYMENT_STRUCTURE = "Payment structure"
    OPTIONAL_ITEMS = "Optional items"
    DELIVERY_APPROACH = "Delivery approach"
    RISK_ALLOCATION = "Risk allocation"
    START_DATE = "Start date"
    SUPPORT = "Support"
    OTHER = "Other"


class NegotiationDecision(Enum):
    ACCEPT = "Accept"
    COUNTER = "Counter"
    REDUCE_SCOPE = "Reduce scope"
    PHASE = "Phase"
    CHANGE_PAYMENT_STRUCTURE = "Change payment structure"
    DEFER = "Defer"
    REQUIRE_VALIDATION = "Require validation"
    DECLINE_REQUEST = "Decline request"
    WALK_AWAY = "Walk away"


@dataclass(frozen=True)
class ProposalSection:
    heading: str
    content: str


@dataclass(frozen=True)
class ProposalAssumption:
    statement: str
    evidence: str = "UNKNOWN"
    critical: bool = False
    consequence_if_false: str = "Scope, cost, or timing may require revision."


@dataclass(frozen=True)
class ProposalRisk:
    description: str
    consequence: str
    mitigation: str


@dataclass(frozen=True)
class ProposalTerm:
    name: str
    value: str


@dataclass(frozen=True)
class ProposalOption:
    description: str
    status: OptionStatus
    price: float | None = None


@dataclass(frozen=True)
class EconomicClaim:
    statement: str
    amount: float | None
    evidence: EvidenceStatus
    source: str

    def __post_init__(self) -> None:
        if self.amount is None and self.evidence is not EvidenceStatus.UNKNOWN:
            raise ValueError("A claim without an amount must remain UNKNOWN.")


@dataclass(frozen=True)
class ProposalRevision:
    version: int
    reason: str
    included: tuple[str, ...]
    excluded: tuple[str, ...]
    customer_price: float
    payment_description: str
    assumptions: tuple[ProposalAssumption, ...] = ()


@dataclass
class Proposal:
    business: str
    opportunity: str
    problem_statement: str
    recommended_approach: str
    scope: ProjectScope
    pricing: PriceScenario
    executive_summary: str = ""
    why_it_matters: str = ""
    why_this_approach: str = ""
    sections: list[ProposalSection] = field(default_factory=list)
    assumptions: list[ProposalAssumption] = field(default_factory=list)
    risks: list[ProposalRisk] = field(default_factory=list)
    options: list[ProposalOption] = field(default_factory=list)
    economic_claims: list[EconomicClaim] = field(default_factory=list)
    payment: PaymentStructure | None = None
    payment_description: str = "Not specified"
    valid_through: date | None = None
    status: ProposalStatus = ProposalStatus.DRAFT
    decision: ProposalDecision | None = None
    version_history: list[ProposalRevision] = field(default_factory=list)
    contract_executed: bool = False
    deposit_received: bool = False
    project_started: bool = False

    def __post_init__(self) -> None:
        if self.problem_statement != self.scope.problem_statement:
            raise ValueError("Proposal problem must match the linked scope problem.")
        if not self.pricing.scope.strip():
            raise ValueError("Pricing must identify its scope.")
        self._record_revision("Initial proposal")

    @property
    def customer_price(self) -> float:
        return self.pricing.customer.customer_price

    @property
    def included(self) -> tuple[str, ...]:
        return tuple(item.statement for item in self.scope.included)

    @property
    def excluded(self) -> tuple[str, ...]:
        return tuple(item.statement for item in self.scope.excluded)

    def assert_consistent(self) -> None:
        overlap = {x.casefold() for x in self.included} & {x.casefold() for x in self.excluded}
        if overlap:
            raise ValueError(f"Proposal silently includes excluded work: {sorted(overlap)}")
        if self.customer_price != self.pricing.customer.customer_price:
            raise ValueError("Proposal price differs from linked pricing analysis.")
        for claim in self.economic_claims:
            if claim.amount is None and claim.evidence is not EvidenceStatus.UNKNOWN:
                raise ValueError("Unknown economic claims cannot be upgraded.")

    def request_added_scope(self, request: str,
                            disposition: RequestDisposition = RequestDisposition.REQUESTED) -> None:
        """Record an addition for decision; never mutate the base scope."""
        self.scope.classify_request(request, disposition, "Proposal negotiation requires explicit decision")

    def revise(self, *, reason: str, pricing: PriceScenario | None = None,
               payment_description: str | None = None,
               assumptions: list[ProposalAssumption] | None = None) -> ProposalRevision:
        if not reason.strip():
            raise ValueError("A revision requires a reason.")
        if pricing is not None:
            self.pricing = pricing
        if payment_description is not None:
            self.payment_description = payment_description
        if assumptions is not None:
            self.assumptions = list(assumptions)
        return self._record_revision(reason)

    def _record_revision(self, reason: str) -> ProposalRevision:
        revision = ProposalRevision(len(self.version_history) + 1, reason, self.included,
            self.excluded, self.customer_price, self.payment_description, tuple(self.assumptions))
        self.version_history.append(revision)
        return revision

    def accept_in_principle(self) -> None:
        self.status = ProposalStatus.ACCEPTED
        self.decision = ProposalDecision.ACCEPTED_IN_PRINCIPLE
        # Deliberately does not alter contract, payment, or project states.

    def decline(self) -> None:
        self.status, self.decision = ProposalStatus.DECLINED, ProposalDecision.DECLINED

    def withdraw(self, healthy_deal: bool = False) -> None:
        self.status = ProposalStatus.WITHDRAWN
        self.decision = (ProposalDecision.WITHDRAWN_BY_LOCAL_WORKS if healthy_deal
                         else ProposalDecision.NO_HEALTHY_DEAL)


@dataclass(frozen=True)
class NegotiationResponse:
    decision: NegotiationDecision
    rationale: str
    proposal_revision_required: bool = False
    walk_away_condition_triggered: bool = False


@dataclass
class NegotiationRequest:
    request: str
    category: NegotiationIssue
    customer_rationale: str = ""
    scope_impact: str = "NONE IDENTIFIED"
    price_impact: float = 0.0
    delivery_cost_impact: float = 0.0
    owner_time_impact: str = "UNKNOWN"
    customer_economics_impact: str = "UNKNOWN"
    local_works_economics_impact: str = "UNKNOWN"
    cash_flow_impact: float = 0.0
    risk_introduced: str = "NONE IDENTIFIED"
    response_options: tuple[NegotiationDecision, ...] = ()
    response: NegotiationResponse | None = None

    def decide(self, decision: NegotiationDecision, rationale: str,
               *, revision_required: bool = False, walk_away: bool = False) -> NegotiationResponse:
        if self.response_options and decision not in self.response_options:
            raise ValueError("Selected response was not one of the evaluated options.")
        self.response = NegotiationResponse(decision, rationale, revision_required, walk_away)
        return self.response


@dataclass
class NegotiationHistory:
    proposal: Proposal
    requests: list[NegotiationRequest] = field(default_factory=list)

    def add(self, request: NegotiationRequest) -> None:
        self.requests.append(request)

    @property
    def creates_project(self) -> bool:
        return False


def discount_impact(analysis: ContributionAnalysis, rate: float) -> DiscountResult:
    """Expose Chapter 15 discount math in the negotiation vocabulary."""
    return discount_sensitivity(analysis, rate)


def no_deposit_cash_exposure(payment: PaymentStructure) -> float:
    return payment.maximum_cash_exposure


def scope_reduction_analysis(
    original: ContributionAnalysis, reduced: ContributionAnalysis
) -> dict[str, float]:
    """Compare an explicitly re-costed scope with a price-only concession."""
    return {"original_contribution": original.contribution,
            "reduced_scope_contribution": reduced.contribution,
            "difference": reduced.contribution - original.contribution}
