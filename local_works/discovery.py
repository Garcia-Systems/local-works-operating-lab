"""Small, evidence-preserving models for Chapter 8 discovery.

Discovery records what people say and what remains unknown.  It deliberately
does not validate a feature request, select a solution, or approve a project.
"""

from dataclasses import dataclass, field
from enum import Enum


class DiscoveryQuestionCategory(Enum):
    CURRENT_STATE = "Current state"
    FREQUENCY_VOLUME = "Frequency and volume"
    PEOPLE = "People"
    TIME_BURDEN = "Time and burden"
    ERRORS_EXCEPTIONS = "Errors and exceptions"
    CUSTOMER_IMPACT = "Customer impact"
    BUSINESS_IMPACT = "Business impact"
    SYSTEMS = "Systems"
    POLICY = "Policy"
    CONSTRAINTS = "Constraints"
    URGENCY = "Urgency"
    AUTHORITY = "Authority"
    BUDGET = "Budget"
    SUCCESS_CRITERIA = "Success criteria"


class EvidenceKind(Enum):
    CUSTOMER_STATEMENT = "Customer statement"
    ESTIMATE = "Estimate"
    MEASURED_DATA = "Measured data"
    OBSERVATION = "Observation"
    UNKNOWN = "Unknown"


class CauseType(Enum):
    TECHNICAL_LIMITATION = "Technical limitation"
    BUSINESS_POLICY = "Business policy"
    PROCESS_HABIT = "Process habit"
    CONFIGURATION = "Configuration"
    INTEGRATION_GAP = "Integration gap"
    KNOWLEDGE_TRAINING = "Knowledge/training issue"
    UNKNOWN = "Unknown"


class DiscoveryOutcome(Enum):
    CONTINUE_ANALYSIS = "Continue analysis"
    MORE_EVIDENCE_REQUIRED = "More evidence required"
    OPPORTUNITY_WEAKENED = "Opportunity weakened"
    STOP = "Stop"


@dataclass(frozen=True)
class DiscoveryQuestion:
    text: str
    category: DiscoveryQuestionCategory

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("A discovery question needs text.")


@dataclass(frozen=True)
class EvidenceValue:
    value: object | None
    unit: str
    source: str
    kind: EvidenceKind
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.source.strip():
            raise ValueError("Evidence needs a source.")
        if self.kind is EvidenceKind.UNKNOWN and self.value is not None:
            raise ValueError("Unknown evidence cannot contain a known value.")

    @property
    def is_measured(self) -> bool:
        return self.kind is EvidenceKind.MEASURED_DATA


@dataclass(frozen=True)
class DiscoveryAnswer:
    question: DiscoveryQuestion
    participant: str
    statement: str
    evidence: EvidenceValue | None = None


@dataclass(frozen=True)
class DiscoveryFinding:
    topic: str
    understanding: str
    answer_indexes: tuple[int, ...]
    cause_type: CauseType = CauseType.UNKNOWN
    validated_problem: bool = False


@dataclass(frozen=True)
class EvidenceConflict:
    topic: str
    answer_indexes: tuple[int, ...]
    unresolved_question: str
    evidence_needed: str

    def __post_init__(self) -> None:
        if len(self.answer_indexes) < 2:
            raise ValueError("A conflict requires at least two preserved answers.")


@dataclass(frozen=True)
class EvidenceRequest:
    need: str
    possible_evidence: str
    unresolved_question: str


@dataclass(frozen=True)
class DiscoveredSystem:
    name: str
    purpose: str
    users: tuple[str, ...]
    workflow_part: str
    known_limitations: tuple[str, ...] = ()
    known_integrations: tuple[str, ...] = ()
    unknown_capabilities: tuple[str, ...] = ()
    owner_vendor: str = "UNKNOWN"
    access_constraints: tuple[str, ...] = ()


@dataclass
class DiscoverySession:
    opportunity_hypothesis: str
    participants: list[str] = field(default_factory=list)
    answers: list[DiscoveryAnswer] = field(default_factory=list)
    findings: list[DiscoveryFinding] = field(default_factory=list)
    conflicts: list[EvidenceConflict] = field(default_factory=list)
    evidence_requests: list[EvidenceRequest] = field(default_factory=list)
    systems: list[DiscoveredSystem] = field(default_factory=list)
    revised_understanding: str = ""
    outcome: DiscoveryOutcome | None = None

    def add_answer(self, answer: DiscoveryAnswer) -> int:
        if answer.participant not in self.participants:
            self.participants.append(answer.participant)
        self.answers.append(answer)
        return len(self.answers) - 1

    def record_conflict(self, conflict: EvidenceConflict) -> None:
        if any(index >= len(self.answers) or index < 0 for index in conflict.answer_indexes):
            raise ValueError("Conflict indexes must refer to recorded answers.")
        self.conflicts.append(conflict)

    def request_evidence(self, need: str, possible_evidence: str,
                         unresolved_question: str) -> EvidenceRequest:
        request = EvidenceRequest(need, possible_evidence, unresolved_question)
        self.evidence_requests.append(request)
        return request

    @property
    def project_approved(self) -> bool:
        return False

    @property
    def selected_solution(self) -> None:
        return None
