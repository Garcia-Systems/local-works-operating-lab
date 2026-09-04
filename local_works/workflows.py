"""Readable current-state workflow records for Chapter 9.

The records support analysis and customer playback.  They are deliberately not
an execution engine and they do not imply a future-state design.
"""

from dataclasses import dataclass, field
from enum import Enum


class StepType(Enum):
    ACTION = "Action"
    DECISION = "Decision"
    HANDOFF = "Handoff"
    WAIT = "Wait"
    DATA_ENTRY = "Data entry"
    SYSTEM_LOOKUP = "System lookup"
    COMMUNICATION = "Communication"
    APPROVAL = "Approval"
    PAYMENT = "Payment"
    OTHER = "Other"


class WorkMode(Enum):
    MANUAL = "Manual"
    AUTOMATED = "Automated"
    MIXED = "Mixed"
    UNKNOWN = "Unknown"


class Visibility(Enum):
    CUSTOMER_VISIBLE = "Customer-visible"
    INTERNAL = "Internal"
    UNKNOWN = "Unknown"


class TimingBasis(Enum):
    MEASURED = "Measured"
    ESTIMATED = "Estimated"
    UNKNOWN = "Unknown"


class ValidationStatus(Enum):
    DRAFT = "Draft"
    PARTIALLY_VALIDATED = "Partially validated"
    VALIDATED = "Validated"
    CONFLICTING_EVIDENCE = "Conflicting evidence"


class StepClassification(Enum):
    VALUE_ADDING = "Value adding"
    NECESSARY = "Necessary"
    QUESTIONABLE = "Questionable"
    UNKNOWN = "Unknown"


class DataMovementType(Enum):
    CREATED = "Data created"
    READ = "Data read"
    COPIED = "Data copied"
    RE_ENTERED = "Data re-entered"
    TRANSFORMED = "Data transformed"
    SENT = "Data sent"


@dataclass(frozen=True)
class WorkflowActor:
    role: str
    description: str = ""


@dataclass(frozen=True)
class WorkflowSystem:
    name: str
    mechanism: bool = False
    description: str = ""


@dataclass(frozen=True)
class Duration:
    minutes: float | None
    basis: TimingBasis = TimingBasis.UNKNOWN
    source: str = "UNKNOWN"

    def __post_init__(self) -> None:
        if self.minutes is not None and self.minutes < 0:
            raise ValueError("Duration cannot be negative.")
        if self.minutes is None and self.basis is not TimingBasis.UNKNOWN:
            raise ValueError("A missing duration must remain UNKNOWN.")

    @property
    def is_known(self) -> bool:
        return self.minutes is not None


UNKNOWN_DURATION = Duration(None)


@dataclass(frozen=True)
class WorkflowStep:
    sequence: int
    description: str
    actor: WorkflowActor
    step_type: StepType = StepType.ACTION
    system: WorkflowSystem | None = None
    input: str = "UNKNOWN"
    output: str = "UNKNOWN"
    active_time: Duration = UNKNOWN_DURATION
    wait_time: Duration = UNKNOWN_DURATION
    evidence_source: str = "UNKNOWN"
    evidence_status: str = "UNKNOWN"
    work_mode: WorkMode = WorkMode.UNKNOWN
    visibility: Visibility = Visibility.UNKNOWN
    classification: StepClassification = StepClassification.UNKNOWN
    friction_notes: tuple[str, ...] = ()
    unknowns: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.sequence < 1 or not self.description.strip():
            raise ValueError("A workflow step needs a positive sequence and description.")


@dataclass(frozen=True)
class WorkflowDecision:
    step_sequence: int
    question: str
    branches: dict[str, str]
    policy_source: str = "UNKNOWN"


@dataclass(frozen=True)
class WorkflowHandoff:
    from_actor: WorkflowActor
    to_actor: WorkflowActor
    after_step: int
    information: str
    mechanism: WorkflowSystem | None = None
    wait_time: Duration = UNKNOWN_DURATION


@dataclass(frozen=True)
class DataMovement:
    information: str
    movement_type: DataMovementType
    source: str
    destination: str
    step_sequence: int


@dataclass(frozen=True)
class WorkflowException:
    name: str
    trigger: str
    steps: tuple[WorkflowStep, ...]
    assumption: str = ""
    handoffs: tuple[WorkflowHandoff, ...] = ()


@dataclass(frozen=True)
class WorkflowObservation:
    description: str
    evidence: str


@dataclass(frozen=True)
class WorkflowMetrics:
    steps: int
    manual_steps: int
    automated_steps: int
    systems_mechanisms: int
    handoffs: int
    decisions: int
    data_reentries: int
    estimated_active_minutes: float | None
    estimated_customer_effort_minutes: float | None
    known_wait_minutes: float | None
    unknown_timing_components: int


@dataclass
class Workflow:
    name: str
    trigger: str
    end_condition: str
    validation_status: ValidationStatus = ValidationStatus.DRAFT
    steps: list[WorkflowStep] = field(default_factory=list)
    decisions: list[WorkflowDecision] = field(default_factory=list)
    handoffs: list[WorkflowHandoff] = field(default_factory=list)
    data_movements: list[DataMovement] = field(default_factory=list)
    exceptions: list[WorkflowException] = field(default_factory=list)
    observations: list[WorkflowObservation] = field(default_factory=list)
    validation_questions: list[str] = field(default_factory=list)

    def add_step(self, step: WorkflowStep) -> None:
        if any(existing.sequence == step.sequence for existing in self.steps):
            raise ValueError("Step sequences must be unique.")
        self.steps.append(step)
        self.steps.sort(key=lambda item: item.sequence)

    @property
    def solution_requirements(self) -> tuple[str, ...]:
        """Observations never silently become solution requirements."""
        return ()

    def metrics(self, steps: tuple[WorkflowStep, ...] | None = None) -> WorkflowMetrics:
        selected = list(steps) if steps is not None else self.steps
        systems = {step.system.name for step in selected if step.system}
        active = [step.active_time.minutes for step in selected if step.active_time.minutes is not None]
        customer = [step.active_time.minutes for step in selected
                    if step.visibility is Visibility.CUSTOMER_VISIBLE and step.active_time.minutes is not None]
        waits = [step.wait_time.minutes for step in selected if step.wait_time.minutes is not None]
        unknown = sum(step.active_time.minutes is None for step in selected)
        unknown += sum(step.wait_time.minutes is None for step in selected if step.step_type in (StepType.WAIT, StepType.HANDOFF, StepType.APPROVAL))
        selected_sequences = {step.sequence for step in selected}
        path_handoffs = self.handoffs
        if steps is not None:
            matching = next((exception for exception in self.exceptions if exception.steps == steps), None)
            if matching is not None:
                path_handoffs = list(matching.handoffs)
        return WorkflowMetrics(
            len(selected),
            sum(step.work_mode is WorkMode.MANUAL for step in selected),
            sum(step.work_mode is WorkMode.AUTOMATED for step in selected),
            len(systems),
            sum(handoff.after_step in selected_sequences for handoff in path_handoffs),
            sum(decision.step_sequence in selected_sequences for decision in self.decisions),
            sum(move.movement_type is DataMovementType.RE_ENTERED and move.step_sequence in selected_sequences for move in self.data_movements),
            sum(active) if active else None,
            sum(customer) if customer else None,
            sum(waits) if waits else None,
            unknown,
        )
