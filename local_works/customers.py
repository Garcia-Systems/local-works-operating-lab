"""Readable, evidence-cautious customer-fit models for Chapter 2.

The rules in this module are a working hypothesis, not a learned scoring model.
Each conclusion retains the observations and unknowns that produced it.
"""

from dataclasses import dataclass
from enum import Enum


class Signal(Enum):
    """The known direction of one fit observation."""

    POSITIVE = "positive"
    NEGATIVE = "negative"
    UNKNOWN = "unknown"


class FitRating(Enum):
    PROMISING = "PROMISING / REQUIRES VALIDATION"
    UNCERTAIN = "UNCERTAIN"
    WEAK = "WEAK"
    DISQUALIFY = "DISQUALIFY"


@dataclass(frozen=True)
class FitDimension:
    name: str
    signal: Signal
    reason: str


@dataclass(frozen=True)
class CustomerProfile:
    """Known facts and open questions about one explicitly fictional prospect."""

    business: str
    industry: str
    dimensions: tuple[FitDimension, ...]
    hard_disqualifiers: tuple[str, ...] = ()


@dataclass(frozen=True)
class CustomerFitAssessment:
    profile: CustomerProfile
    rating: FitRating
    rationale: str
    next_action: str

    @property
    def positive_signals(self) -> tuple[FitDimension, ...]:
        return self._with_signal(Signal.POSITIVE)

    @property
    def negative_signals(self) -> tuple[FitDimension, ...]:
        return self._with_signal(Signal.NEGATIVE)

    @property
    def unknowns(self) -> tuple[FitDimension, ...]:
        return self._with_signal(Signal.UNKNOWN)

    def _with_signal(self, signal: Signal) -> tuple[FitDimension, ...]:
        return tuple(item for item in self.profile.dimensions if item.signal is signal)


def dimension(name: str, signal: Signal, reason: str) -> FitDimension:
    return FitDimension(name, signal, reason)


def assess_customer(profile: CustomerProfile) -> CustomerFitAssessment:
    """Apply explicit prioritization rules without converting unknowns into negatives."""
    signals = {item.name: item.signal for item in profile.dimensions}
    if profile.hard_disqualifiers:
        return CustomerFitAssessment(
            profile, FitRating.DISQUALIFY,
            "A hard disqualifier overrides otherwise interesting fit signals.",
            "Do not pursue; refer elsewhere when appropriate.",
        )

    # Authority failure remains visible even when the operational problem is strong.
    if signals.get("Buying authority accessibility") is Signal.NEGATIVE:
        return CustomerFitAssessment(
            profile, FitRating.WEAK,
            "Problem fit may exist, but no reachable purchasing path is currently available.",
            "Maintain the relationship only if a path to an authorized decision maker emerges.",
        )

    severity = signals.get("Friction severity")
    burden = signals.get("Workaround burden")
    frequency = signals.get("Workflow frequency")
    if severity is Signal.NEGATIVE and burden is Signal.NEGATIVE:
        return CustomerFitAssessment(
            profile, FitRating.WEAK,
            "The known inconvenience is too slight to establish an economically meaningful problem.",
            "Problem currently too small; do not manufacture a project.",
        )

    if (
        frequency is Signal.POSITIVE
        and (severity is Signal.POSITIVE or burden is Signal.POSITIVE)
        and signals.get("Buying authority accessibility") is not Signal.NEGATIVE
    ):
        return CustomerFitAssessment(
            profile, FitRating.PROMISING,
            "Recurring friction and a plausible purchasing path justify validation; they do not prove a sale.",
            "Perform a Digital Friction Audit and validate the listed unknowns.",
        )

    return CustomerFitAssessment(
        profile, FitRating.UNCERTAIN,
        "The available evidence does not yet establish both meaningful recurring friction and a viable buying path.",
        "Gather more information before deciding whether discovery is warranted.",
    )


def fictional_profiles() -> tuple[CustomerProfile, ...]:
    """Return Chapter 2 cases. Every organization and observation is fictional."""
    p, n, u = Signal.POSITIVE, Signal.NEGATIVE, Signal.UNKNOWN
    return (
        CustomerProfile("Harbor Fitness", "Fictional two-location gym", (
            dimension("Workflow frequency", p, "Memberships and member interactions recur."),
            dimension("Affected people", p, "Members and staff participate in account-management workflows."),
            dimension("Friction severity", u, "Actual disruption and member complaints have not been measured."),
            dimension("Workaround burden", p, "Staff involvement in membership/account management is visible, but its amount is unknown."),
            dimension("Economic capacity", u, "No budget or economic evidence has been gathered."),
            dimension("Buying authority accessibility", u, "Management appears reachable, but actual approval authority is unknown."),
            dimension("Decision complexity", u, "Stakeholders, approval steps, and vendor rules are unknown."),
            dimension("Technology environment", n, "Existing membership software may constrain changes or already contain useful capabilities."),
            dimension("Urgency", u, "Management urgency has not been established."),
            dimension("Measurability", u, "No baseline for time, complaints, completion, or impact exists."),
            dimension("Repeat opportunity", u, "No additional worthwhile workflows have been validated."),
            dimension("Delivery feasibility", u, "Capabilities, integrations, restrictions, and safe delivery options are unknown."),
            dimension("Sales accessibility", p, "A local management conversation appears plausible."),
        )),
        CustomerProfile("Cadence Music Lessons", "Fictional solo music teacher with 18 students", (
            dimension("Workflow frequency", n, "Scheduling texts occur only occasionally."),
            dimension("Friction severity", n, "The teacher describes no meaningful economic or customer problem."),
            dimension("Workaround burden", n, "The texts consume very little time."),
            dimension("Economic capacity", u, "Capacity to purchase professional help is unknown."),
            dimension("Buying authority accessibility", p, "The owner can make a decision directly."),
            dimension("Delivery feasibility", p, "A simple response would likely be feasible if one became worthwhile."),
        )),
        CustomerProfile("Rapid Home Care", "Fictional multi-trade home services company", (
            dimension("Workflow frequency", p, "Incoming calls, scheduling, dispatch, estimates, and updates recur daily."),
            dimension("Affected people", p, "Several employees and customers encounter the workflows."),
            dimension("Friction severity", u, "Operational and customer impact have not been measured."),
            dimension("Workaround burden", p, "Coordination crosses several software tools."),
            dimension("Economic capacity", u, "Purchasing capacity is plausible but unverified."),
            dimension("Buying authority accessibility", u, "The decision maker and approval path are unknown."),
            dimension("Decision complexity", u, "Stakeholders and vendor constraints are unknown."),
            dimension("Technology environment", n, "Multiple tools increase both opportunity and delivery risk."),
            dimension("Urgency", u, "No commitment to act has been observed."),
            dimension("Measurability", p, "Response time, rework, and missed appointments may be measurable."),
            dimension("Delivery feasibility", u, "Integration access and partner capability require validation."),
            dimension("Sales accessibility", p, "Local outreach and referrals appear plausible."),
        )),
        CustomerProfile("MetroMotion Gym — Downtown", "Fictional corporate gym-chain location", (
            dimension("Workflow frequency", p, "Account friction occurs throughout recurring member interactions."),
            dimension("Friction severity", p, "Staff report a meaningful local customer problem."),
            dimension("Workaround burden", p, "Branch staff repeatedly handle the issue manually."),
            dimension("Economic capacity", p, "The chain plausibly has resources, though no project budget is known."),
            dimension("Buying authority accessibility", n, "Headquarters controls all technology and the local manager cannot authorize or introduce Local Works."),
            dimension("Decision complexity", n, "Corporate procurement, security, and legal review would be required."),
            dimension("Technology environment", n, "Corporate-controlled systems cannot be changed locally."),
            dimension("Measurability", p, "Local handling time and complaints could be measured."),
        )),
        CustomerProfile("Pocket Stage Studio", "Fictional tiny performing-arts studio", (
            dimension("Workflow frequency", p, "The owner re-enters registrations, waivers, payments, and rosters every day."),
            dimension("Affected people", n, "Only the owner and a small customer base are affected."),
            dimension("Friction severity", p, "Administration regularly displaces paid teaching time."),
            dimension("Workaround burden", p, "The tiny organization performs unusually heavy manual administration."),
            dimension("Economic capacity", u, "Small size does not answer whether an affordable improvement has sound economics."),
            dimension("Buying authority accessibility", p, "The owner is directly reachable and can decide."),
            dimension("Technology environment", p, "Mostly manual work may permit a simple response."),
            dimension("Urgency", p, "The owner wants to reclaim teaching time."),
            dimension("Measurability", p, "Administrative hours and re-entry errors can be baselined."),
            dimension("Delivery feasibility", u, "The simplest safe response has not been investigated."),
        )),
        CustomerProfile("Shadow Metrics Cooperative", "Fictional data-services prospect", (
            dimension("Workflow frequency", p, "The requested data collection would be recurring."),
            dimension("Friction severity", p, "The prospect says its current restriction is commercially significant."),
            dimension("Buying authority accessibility", p, "An owner is directly involved."),
        ), ("The prospect requires unlawful collection of private customer data.",)),
    )


def harbor_fitness_profile() -> CustomerProfile:
    return fictional_profiles()[0]
