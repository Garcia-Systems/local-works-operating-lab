"""Manual, evidence-first support for post-lab Validation Sprint 1.

This module models records and decisions only.  It deliberately has no network,
messaging, persistence, or production-application behavior.
"""

from dataclasses import dataclass, replace
from enum import Enum

from local_works.audit import JourneyStage


class Rating(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    UNKNOWN = "Unknown"


class TargetDimension(Enum):
    PUBLIC_JOURNEY_VISIBILITY = "Public journey visibility"
    FRICTION_OBSERVABILITY = "Friction observability"
    BUSINESS_VALUE_POTENTIAL = "Business value potential"
    DECISION_MAKER_REACHABILITY = "Decision-maker reachability"
    SOLUTION_FLEXIBILITY = "Solution flexibility"
    FIRST_PROJECT_SAFETY = "First-project safety"
    LEARNING_VALUE = "Learning value"


class TargetVerdict(Enum):
    HIGH_PRIORITY = "High priority"
    MEDIUM_PRIORITY = "Medium priority"
    LOW_PRIORITY = "Low priority"
    SKIP = "Skip"
    INSUFFICIENT_EVIDENCE = "Insufficient evidence"


class FrictionType(Enum):
    REQUIRES_PHONE_CALL = "Requires phone call"
    REQUIRES_EMAIL = "Requires email"
    REQUIRES_PRINTING = "Requires printing"
    REQUIRES_IN_PERSON = "Requires in person"
    DUPLICATE_DATA_ENTRY = "Duplicate data entry"
    UNCLEAR_NEXT_STEP = "Unclear next step"
    MANUAL_STAFF_HANDOFF = "Manual staff handoff"
    DISCONNECTED_SYSTEM = "Disconnected system"
    LIMITED_SELF_SERVICE = "Limited self-service"
    REPETITIVE_ADMIN = "Repetitive administration"
    UNNECESSARY_WAIT = "Unnecessary wait"
    UNCLEAR_STATUS = "Unclear status"
    PAYMENT_FRICTION = "Payment friction"
    SCHEDULING_FRICTION = "Scheduling friction"
    MEMBERSHIP_FRICTION = "Membership friction"
    OTHER = "Other"
    NO_MEANINGFUL_PUBLIC_FRICTION_FOUND = "No meaningful public friction found"


class AuditDecision(Enum):
    WORTH_DISCOVERY = "Worth discovery"
    MAYBE_DISCOVERY = "Maybe discovery"
    LOW_PRIORITY = "Low priority"
    NO_OBVIOUS_OPPORTUNITY = "No obvious opportunity"
    INSUFFICIENT_EVIDENCE = "Insufficient evidence"


class SolutionPath(Enum):
    CONFIGURE = "Configure"
    INTEGRATE = "Integrate"
    AUTOMATE = "Automate"
    CUSTOM_BUILD = "Custom build"
    LEAVE_ALONE = "Leave alone"
    UNKNOWN = "Unknown"


class ValidationStatus(Enum):
    NOT_CONTACTED = "Not contacted"
    OUTREACH_PREPARED = "Outreach prepared"
    CONTACTED = "Contacted"
    NO_RESPONSE = "No response"
    RESPONDED = "Responded"
    NOT_INTERESTED = "Not interested"
    INTERESTED = "Interested"
    DISCOVERY_SCHEDULED = "Discovery scheduled"
    DISCOVERY_COMPLETED = "Discovery completed"
    NOT_A_FIT = "Not a fit"
    OPPORTUNITY = "Opportunity"
    UNKNOWN = "Unknown"


class RejectionReason(Enum):
    NO_NEED = "No need"
    NO_BUDGET = "No budget"
    BAD_TIMING = "Bad timing"
    HAPPY_WITH_CURRENT_SYSTEM = "Happy with current system"
    CORPORATE_CONTROL = "Corporate control"
    ALREADY_SOLVED = "Already solved"
    NOT_PRIORITY = "Not priority"
    DO_NOT_CONTACT = "Do not contact"
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class ValidationTargetScore:
    ratings: dict[TargetDimension, Rating]

    def __post_init__(self) -> None:
        if set(self.ratings) != set(TargetDimension):
            raise ValueError("Every target dimension must be recorded, including UNKNOWN.")

    @property
    def verdict(self) -> TargetVerdict:
        values = tuple(self.ratings.values())
        if Rating.UNKNOWN in values:
            return TargetVerdict.INSUFFICIENT_EVIDENCE
        if values.count(Rating.LOW) >= 3:
            return TargetVerdict.SKIP
        if values.count(Rating.HIGH) >= 5:
            return TargetVerdict.HIGH_PRIORITY
        if values.count(Rating.HIGH) >= 2:
            return TargetVerdict.MEDIUM_PRIORITY
        return TargetVerdict.LOW_PRIORITY


@dataclass(frozen=True)
class ValidationTarget:
    name: str
    category: str
    public_url: str
    locations: str
    why_considered: str
    score: ValidationTargetScore
    is_fictional: bool = False


@dataclass(frozen=True)
class ValidationObservation:
    """One finding whose visible fact can never be confused with its meaning."""

    observation: str
    inference: str
    unknown: str
    discovery_question: str
    friction: FrictionType
    public_evidence: str

    def __post_init__(self) -> None:
        if not self.observation.strip() or not self.public_evidence.strip():
            raise ValueError("A public observation and its evidence are required.")
        if self.unknown.strip() and not self.discovery_question.strip():
            raise ValueError("An unknown needs a discovery question, not an answer.")


@dataclass(frozen=True)
class JourneyReview:
    stage: JourneyStage
    observed_experience: str
    friction: FrictionType
    evidence: str
    unknown: str = ""
    potential_business_effect: str = ""
    discovery_question: str = ""


@dataclass(frozen=True)
class ValidationHypothesis:
    statement: str
    status: str = "UNVALIDATED"

    def __post_init__(self) -> None:
        if self.status != "UNVALIDATED":
            raise ValueError("A public-audit value hypothesis must remain UNVALIDATED.")


@dataclass(frozen=True)
class DigitalFrictionAudit:
    target: ValidationTarget
    journey: tuple[JourneyReview, ...]
    observations: tuple[ValidationObservation, ...]
    decision: AuditDecision
    decision_reason: str
    value_hypotheses: tuple[ValidationHypothesis, ...] = ()
    solution_path: SolutionPath = SolutionPath.UNKNOWN

    @property
    def has_meaningful_public_friction(self) -> bool:
        return any(
            item.friction is not FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND
            for item in self.journey
        )


@dataclass(frozen=True)
class ValidationEvidence:
    assumption: str
    original_value: str
    original_evidence: str
    real_evidence: tuple[str, ...] = ()
    updated_estimate: str | None = None
    evidence_status: str = "SIMULATION_ONLY"

    def update(self, evidence: tuple[str, ...], estimate: str) -> "ValidationEvidence":
        if not evidence or not all(item.strip() for item in evidence):
            return self
        return replace(
            self,
            real_evidence=self.real_evidence + evidence,
            updated_estimate=estimate,
            evidence_status="REAL_EVIDENCE_COLLECTED",
        )


@dataclass(frozen=True)
class SprintCounts:
    researched: int = 0
    audited: int = 0
    contacted: int = 0
    responses: int = 0
    discoveries: int = 0
    opportunities: int = 0


@dataclass(frozen=True)
class SprintTime:
    target_research_minutes: int = 0
    audit_minutes: int = 0
    outreach_preparation_minutes: int = 0
    follow_up_minutes: int = 0
    discovery_minutes: int = 0

    @property
    def total_minutes(self) -> int:
        return sum((self.target_research_minutes, self.audit_minutes,
                    self.outreach_preparation_minutes, self.follow_up_minutes,
                    self.discovery_minutes))


@dataclass(frozen=True)
class ValidationExperiment:
    targets_to_research: int = 5
    audits_to_complete: int = 3
    outreach_limit: int = 3


def no_response_learning() -> tuple[str, tuple[str, ...]]:
    """Bound the conclusion from silence to the particular attempt."""
    return (
        "This outreach attempt received no response.",
        ("the business has no problem", "Local Works has no market",
         "the value proposition is invalid"),
    )


OUTREACH_TEMPLATES: dict[str, str] = {
    "EMAIL": ("Subject: A customer-workflow observation\n\nHi {name}, I was looking at "
              "{business}'s public customer experience and noticed {observation}. "
              "It may be creating unnecessary work, although I cannot know that "
              "from the outside. I put together a short observation and would be "
              "happy to share it. Would that be useful?"),
    "LINKEDIN": ("Hi {name} — I noticed one public {business} customer workflow "
                 "that may be creating unnecessary work. I wrote up the observation "
                 "and the questions it raised. Happy to share it if useful."),
    "IN_PERSON_NETWORKING_FOLLOW_UP": ("Good meeting you, {name}. I took another "
                 "look at the public {business} customer journey and noticed "
                 "{observation}. I cannot see the internal impact, but I would be "
                 "happy to share the short note and hear whether it matters."),
}


SPRINT_SUCCESS_SIGNALS = (
    "Genuine observable friction can be identified consistently.",
    "Findings lead to useful discovery questions.",
    "Some businesses respond to the bounded outreach attempts.",
    "Discovery reveals an economically meaningful problem.",
    "A simulation assumption becomes better informed by real evidence.",
)

SPRINT_FAILURE_SIGNALS = (
    "Targets show little observable friction.",
    "Public audits take too long.",
    "Outreach receives no engagement.",
    "Decision makers cannot be reached.",
    "Existing tools have already solved the issues.",
    "Problems appear too small economically or willingness to discuss is low.",
)
