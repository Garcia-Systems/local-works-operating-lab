"""Small, evidence-conscious models for a Digital Friction Audit.

An audit organizes observations and questions.  It does not select software or
promise that an implementation project should exist.
"""

from dataclasses import dataclass, replace
from enum import Enum

from local_works.hypothesis import EvidenceType


class JourneyStage(Enum):
    FIND = "Find"
    UNDERSTAND = "Understand"
    CONTACT = "Contact"
    BOOK_OR_JOIN = "Book or join"
    PAY = "Pay"
    RECEIVE_SERVICE = "Receive service"
    MANAGE = "Manage"
    RETURN = "Return"


class FrictionType(Enum):
    UNNECESSARY_CALL = "Unnecessarily required call"
    UNNECESSARY_EMAIL = "Unnecessarily required email"
    PAPER_PROCESS = "Paper process"
    REPEATED_INFORMATION = "Repeated information"
    MANUAL_DATA_ENTRY = "Manual data entry"
    SYSTEM_SWITCHING = "System switching"
    WAITING = "Waiting"
    IN_PERSON_REQUIREMENT = "In-person requirement"
    UNCLEAR_INFORMATION = "Unclear information"
    DUPLICATE_WORK = "Duplicate work"
    MANUAL_HANDOFF = "Manual handoff"
    STATUS_UNCERTAINTY = "Status uncertainty"
    ERROR_PRONE_STEP = "Error-prone step"
    REPETITIVE_ADMINISTRATION = "Repetitive administration"
    DISCONNECTED_SYSTEMS = "Disconnected systems"
    OTHER = "Other"


class AffectedParty(Enum):
    CUSTOMER = "Customer"
    EMPLOYEE = "Employee"
    MANAGER = "Manager"


class EvidenceSource(Enum):
    PUBLIC_WEBSITE = "Public website"
    PUBLIC_BOOKING_FLOW = "Public booking flow"
    PUBLIC_MEMBERSHIP_FLOW = "Public membership flow"
    PUBLIC_DOCUMENT = "Public document"
    CUSTOMER_STATEMENT = "Customer statement"
    EMPLOYEE_STATEMENT = "Employee statement"
    MANAGER_STATEMENT = "Manager statement"
    DIRECT_WORKFLOW_OBSERVATION = "Direct workflow observation"
    SYSTEM_DEMONSTRATION = "System demonstration"
    PROCESS_DOCUMENTATION = "Process documentation"
    MEASURED_DATA = "Measured data"


class Frequency(Enum):
    UNKNOWN = "Unknown"
    RARE = "Rare"
    OCCASIONAL = "Occasional"
    FREQUENT = "Frequent"


class Severity(Enum):
    UNKNOWN = "Unknown"
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"


class Confidence(Enum):
    UNKNOWN = "Unknown"
    LIMITED = "Limited evidence"
    CORROBORATED = "Corroborated"
    MEASURED = "Measured"


class FindingDisposition(Enum):
    WORTH_INVESTIGATING = "Observed friction worth investigating"
    NEEDS_MORE_EVIDENCE = "Possible friction requiring more evidence"
    LOW_SIGNIFICANCE = "Low-significance friction"
    WORKING_ADEQUATELY = "No meaningful friction / working adequately"
    UNKNOWN_INTERNAL = "Unknown internal workflow area"


class AuditRecommendation(Enum):
    NO_MEANINGFUL_FRICTION = "No meaningful friction"
    MONITOR = "Monitor"
    SIMPLE_IMPROVEMENT = "Simple improvement"
    DISCOVERY_RECOMMENDED = "Discovery recommended"
    INSUFFICIENT_INFORMATION = "Insufficient information"


@dataclass(frozen=True)
class FrictionObservation:
    journey_stage: JourneyStage
    affected_parties: tuple[AffectedParty, ...]
    observed_fact: str
    friction_hypothesis: str | None
    evidence_sources: tuple[EvidenceSource, ...]
    frequency: Frequency = Frequency.UNKNOWN
    severity: Severity = Severity.UNKNOWN
    workaround: str | None = None
    unknowns: tuple[str, ...] = ()
    follow_up_questions: tuple[str, ...] = ()
    confidence: Confidence = Confidence.UNKNOWN
    evidence_status: EvidenceType = EvidenceType.OBSERVED
    business_objective: str | None = None
    policy_or_regulatory_reason: str | None = None
    potential_tradeoff: str | None = None

    def __post_init__(self) -> None:
        if not self.observed_fact.strip():
            raise ValueError("An observed fact is required.")
        if not self.affected_parties:
            raise ValueError("At least one affected party is required.")
        if not self.evidence_sources:
            raise ValueError("At least one evidence source is required.")


@dataclass(frozen=True)
class AuditFinding:
    title: str
    observation: FrictionObservation
    friction_types: tuple[FrictionType, ...]
    disposition: FindingDisposition
    significance_reasoning: tuple[str, ...]
    known_facts: tuple[str, ...] = ()

    def revised(
        self,
        *,
        observation: FrictionObservation | None = None,
        disposition: FindingDisposition | None = None,
        significance_reasoning: tuple[str, ...] | None = None,
    ) -> "AuditFinding":
        """Return a traceable reassessment when additional evidence arrives."""
        return replace(
            self,
            observation=observation or self.observation,
            disposition=disposition or self.disposition,
            significance_reasoning=significance_reasoning or self.significance_reasoning,
        )


@dataclass(frozen=True)
class DigitalFrictionAudit:
    business: str
    journey_stages: tuple[JourneyStage, ...]
    findings: tuple[AuditFinding, ...]
    recommendation: AuditRecommendation
    recommendation_reasoning: tuple[str, ...]
    is_fictional: bool = False

    def __post_init__(self) -> None:
        if not self.journey_stages:
            raise ValueError("Select the journey stages relevant to this business.")
        if len(set(self.journey_stages)) != len(self.journey_stages):
            raise ValueError("Journey stages cannot be duplicated.")
        outside_scope = [
            finding.observation.journey_stage
            for finding in self.findings
            if finding.observation.journey_stage not in self.journey_stages
        ]
        if outside_scope:
            raise ValueError("Every finding must belong to an included journey stage.")

    @property
    def implementation_recommended(self) -> bool:
        """Discovery is permission to learn, never an implementation decision."""
        return False

    def findings_by_disposition(
        self, disposition: FindingDisposition
    ) -> tuple[AuditFinding, ...]:
        return tuple(item for item in self.findings if item.disposition is disposition)


AUDIT_QUESTIONS: dict[JourneyStage, tuple[str, ...]] = {
    JourneyStage.FIND: ("Can customers find the business and correct location/service?", "Is important information discoverable?"),
    JourneyStage.UNDERSTAND: ("Are pricing, eligibility, requirements, and options understandable?", "What repeatedly needs staff explanation?"),
    JourneyStage.CONTACT: ("Is contact necessary and is the right channel obvious?", "Will information be repeated later?"),
    JourneyStage.BOOK_OR_JOIN: ("Can the customer finish, and where is staff intervention required?", "Is information entered more than once?"),
    JourneyStage.PAY: ("How is payment handled and are failures visible?", "Does staff reconcile anything manually?"),
    JourneyStage.RECEIVE_SERVICE: ("How does intake reach delivery staff?", "Are handoffs manual and is status understandable?"),
    JourneyStage.MANAGE: ("What can customers update, pause, cancel, or reschedule?", "Which changes require staff, and why?"),
    JourneyStage.RETURN: ("Can a customer resume without re-entering information?", "Is relevant history available?"),
}
