"""Lightweight, fictional delivery-control records for Chapter 23.

These types make delivery facts visible.  They do not execute implementation,
quality assurance, deployment, acceptance, or a prospective scope change.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class MilestoneType(Enum):
    KICKOFF = "Kickoff"
    REQUIREMENTS_BASELINE = "Requirements baseline"
    TECHNICAL_VALIDATION = "Technical validation"
    CONFIGURATION_COMPLETE = "Configuration complete"
    IMPLEMENTATION_COMPLETE = "Implementation complete"
    INTEGRATION_COMPLETE = "Integration complete"
    QA_READY = "QA ready"
    CUSTOMER_REVIEW = "Customer review"
    ACCEPTANCE_READY = "Acceptance ready"
    LAUNCH_READY = "Launch ready"
    LAUNCH = "Launch"
    HANDOFF = "Handoff"
    OTHER = "Other"


class MilestoneStatus(Enum):
    NOT_STARTED = "Not started"
    IN_PROGRESS = "In progress"
    BLOCKED = "Blocked"
    AT_RISK = "At risk"
    COMPLETE = "Complete"
    CANCELLED = "Cancelled"
    DEFERRED = "Deferred"


class TaskStatus(Enum):
    NOT_STARTED = "Not started"
    READY = "Ready"
    IN_PROGRESS = "In progress"
    BLOCKED = "Blocked"
    DONE = "Done"
    DEFERRED = "Deferred"
    CANCELLED = "Cancelled"


class TaskCategory(Enum):
    VALIDATION = "Validation"
    CONFIGURATION = "Configuration"
    TEST_PREPARATION = "Test preparation"
    DOCUMENTATION = "Documentation"
    CUSTOMER_REVIEW = "Customer review"
    COORDINATION = "Coordination"
    OTHER = "Other"


class WorkOwner(Enum):
    CUSTOMER = "Customer"
    LOCAL_WORKS = "Local Works"
    DELIVERY_PARTNER = "Delivery partner"
    VENDOR = "Vendor"
    SHARED = "Shared"
    UNKNOWN = "UNKNOWN"


@dataclass
class Milestone:
    milestone_id: str
    name: str
    milestone_type: MilestoneType
    owner: WorkOwner
    baseline_date: date | None
    status: MilestoneStatus = MilestoneStatus.NOT_STARTED
    forecast_date: date | None = None
    actual_date: date | None = None
    related_requirements: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    done_condition: str = ""

    def reforecast(self, new_date: date) -> None:
        """Change current expectations while retaining the historical plan."""
        self.forecast_date = new_date


@dataclass
class ProjectTask:
    task_id: str
    title: str
    category: TaskCategory
    owner: WorkOwner
    related_milestone: str
    related_requirements: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    estimated_effort: float = 0.0
    actual_effort: float = 0.0
    remaining_estimate: float = 0.0
    status: TaskStatus = TaskStatus.NOT_STARTED
    blocker_id: str | None = None
    done_condition: str = ""
    notes: str = ""
    priority: str = "MUST"

    def ready(self, tasks: list["ProjectTask"]) -> bool:
        completed = {task.task_id for task in tasks if task.status is TaskStatus.DONE}
        return self.status not in {TaskStatus.BLOCKED, TaskStatus.DEFERRED, TaskStatus.CANCELLED, TaskStatus.DONE} and set(self.dependencies) <= completed

    def defer_optional(self) -> bool:
        if self.priority.upper() != "COULD":
            return False
        self.status = TaskStatus.DEFERRED
        return True


class BlockerCategory(Enum):
    CUSTOMER_DECISION = "Customer decision"
    CUSTOMER_ACCESS = "Customer access"
    DELIVERY_CAPACITY = "Delivery capacity"
    TECHNICAL_UNKNOWN = "Technical unknown"
    VENDOR = "Vendor"
    SECURITY = "Security"
    DATA = "Data"
    SCOPE = "Scope"
    PAYMENT = "Payment"
    ENVIRONMENT = "Environment"
    OTHER = "Other"


class BlockerStatus(Enum):
    OPEN = "Open"
    WAITING = "Waiting"
    ESCALATED = "Escalated"
    RESOLVED = "Resolved"
    ACCEPTED_RISK = "Accepted risk"
    CLOSED = "Closed"


class DelaySource(Enum):
    CUSTOMER = "Customer"
    DELIVERY_PARTNER = "Delivery partner"
    VENDOR = "Vendor"
    LOCAL_WORKS = "Local Works"
    SHARED = "Shared"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class DeliveryDelay:
    source: DelaySource
    reason: str
    days: int = 0


@dataclass
class Blocker:
    blocker_id: str
    description: str
    category: BlockerCategory
    owner: WorkOwner
    opened_at: date
    impact: str
    blocking_tasks: tuple[str, ...] = ()
    blocking_milestones: tuple[str, ...] = ()
    status: BlockerStatus = BlockerStatus.OPEN
    next_action: str = "UNKNOWN"
    escalation_needed: bool = False

    @property
    def active(self) -> bool:
        return self.status in {BlockerStatus.OPEN, BlockerStatus.WAITING, BlockerStatus.ESCALATED}


class ForecastConfidence(Enum):
    HIGH = "High"
    MODERATE = "Moderate"
    LOW = "Low"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class ProjectForecast:
    milestone: str
    planned_date: date | None
    forecast_date: date | None
    confidence: ForecastConfidence
    reason: str
    assumptions: tuple[str, ...] = ()


class VarianceType(Enum):
    EFFORT_VARIANCE = "Effort variance"
    SCHEDULE_VARIANCE = "Schedule variance"
    COST_VARIANCE = "Cost variance"


@dataclass(frozen=True)
class DeliveryVariance:
    estimated: float
    actual_so_far: float
    estimate_to_complete: float
    variance_type: VarianceType = VarianceType.EFFORT_VARIANCE

    @property
    def forecast_total(self) -> float:
        return self.actual_so_far + self.estimate_to_complete

    @property
    def amount(self) -> float:
        return self.forecast_total - self.estimated

    @property
    def percent(self) -> float | None:
        return None if self.estimated == 0 else self.amount / self.estimated * 100


class DecisionRequestStatus(Enum):
    OPEN = "Open"
    DECIDED = "Decided"
    DEFERRED = "Deferred"
    ESCALATED = "Escalated"


@dataclass
class ProjectDecisionRequest:
    decision_id: str
    question: str
    decision_owner: str
    requested_at: date
    needed_by: date
    impact_if_delayed: str
    options: tuple[str, ...]
    recommendation: str = "UNKNOWN"
    status: DecisionRequestStatus = DecisionRequestStatus.OPEN
    decision: str = "UNKNOWN"
    decision_date: date | None = None

    def latency_days(self, as_of: date) -> int:
        end = self.decision_date or as_of
        return max(0, (end - self.requested_at).days)

    def threatens_forecast(self, as_of: date) -> bool:
        return self.status in {DecisionRequestStatus.OPEN, DecisionRequestStatus.ESCALATED} and as_of > self.needed_by


class HealthDimension(Enum):
    SCOPE = "Scope"
    SCHEDULE = "Schedule"
    COST = "Cost"
    QUALITY = "Quality"
    DEPENDENCIES = "Dependencies"
    CUSTOMER_DECISIONS = "Customer decisions"
    DELIVERY_CAPACITY = "Delivery capacity"
    TECHNICAL_RISK = "Technical risk"


class HealthState(Enum):
    ON_TRACK = "On track"
    WATCH = "Watch"
    AT_RISK = "At risk"
    BLOCKED = "Blocked"


@dataclass(frozen=True)
class HealthAssessment:
    state: HealthState
    rationale: str


@dataclass(frozen=True)
class ProjectHealth:
    dimensions: dict[HealthDimension, HealthAssessment]

    @property
    def overall(self) -> HealthState:
        order = {HealthState.ON_TRACK: 0, HealthState.WATCH: 1, HealthState.AT_RISK: 2, HealthState.BLOCKED: 3}
        return max((item.state for item in self.dimensions.values()), key=order.get, default=HealthState.ON_TRACK)


class CorrectiveAction(Enum):
    RESEQUENCE_WORK = "Resequence work"
    ADD_CLARIFICATION = "Add clarification"
    ESCALATE_DECISION = "Escalate decision"
    REASSIGN_TASK = "Reassign task"
    REDUCE_SCOPE = "Reduce scope"
    DEFER_OPTIONAL_WORK = "Defer optional work"
    REQUEST_CHANGE_REVIEW = "Request change review"
    REFORECAST = "Reforecast"
    PAUSE = "Pause"
    REOPEN_TECHNICAL_DESIGN = "Reopen technical design"


class ProjectControlDecision(Enum):
    CONTINUE = "Continue"
    CONTINUE_WITH_REFORECAST = "Continue with reforecast"
    CONTINUE_WITH_ESCALATION = "Continue with escalation"
    NEEDS_CUSTOMER_DECISION = "Needs customer decision"
    NEEDS_SCOPE_REVIEW = "Needs scope review"
    NEEDS_DELIVERY_RECOVERY = "Needs delivery recovery"
    PAUSE = "Pause"
    BLOCKED = "Blocked"


@dataclass(frozen=True)
class ScopeChangeSignal:
    description: str
    status: str = "POTENTIAL_SCOPE_CHANGE"
    executed: bool = False


@dataclass(frozen=True)
class OwnerEffort:
    customer_communication: float = 0
    partner_coordination: float = 0
    decision_management: float = 0
    qa_project_review: float = 0
    other: float = 0

    @property
    def total(self) -> float:
        return sum((self.customer_communication, self.partner_coordination, self.decision_management, self.qa_project_review, self.other))


@dataclass(frozen=True)
class ProjectUpdate:
    completed: tuple[str, ...] = ()
    in_progress: tuple[str, ...] = ()
    next: tuple[str, ...] = ()
    decisions_needed: tuple[str, ...] = ()
    blockers: tuple[str, ...] = ()
    risks: tuple[str, ...] = ()
    changes: tuple[str, ...] = ()
    customer_actions: tuple[str, ...] = ()
    local_works_actions: tuple[str, ...] = ()
    delivery_partner_actions: tuple[str, ...] = ()
    forecast: str = "UNKNOWN"


class ProjectEventType(Enum):
    TASK_STARTED = "Task started"
    TASK_COMPLETED = "Task completed"
    BLOCKER_OPENED = "Blocker opened"
    BLOCKER_RESOLVED = "Blocker resolved"
    DECISION_REQUESTED = "Decision requested"
    DECISION_MADE = "Decision made"
    MILESTONE_CHANGED = "Milestone changed"
    FORECAST_CHANGED = "Forecast changed"
    RISK_ESCALATED = "Risk escalated"
    CUSTOMER_UPDATE_SENT = "Customer update sent"
    OTHER = "Other"


@dataclass(frozen=True)
class ProjectLogEntry:
    occurred_at: date
    event_type: ProjectEventType
    summary: str


@dataclass
class ProjectControl:
    milestones: list[Milestone] = field(default_factory=list)
    tasks: list[ProjectTask] = field(default_factory=list)
    blockers: list[Blocker] = field(default_factory=list)
    scope_signals: list[ScopeChangeSignal] = field(default_factory=list)
    log: list[ProjectLogEntry] = field(default_factory=list)

    def add_scope_signal(self, description: str) -> ScopeChangeSignal:
        signal = ScopeChangeSignal(description)
        self.scope_signals.append(signal)
        return signal  # deliberately not converted into a task

    def apply_blocker(self, blocker: Blocker) -> None:
        self.blockers.append(blocker)
        for task in self.tasks:
            if task.task_id in blocker.blocking_tasks:
                task.status, task.blocker_id = TaskStatus.BLOCKED, blocker.blocker_id
        for milestone in self.milestones:
            if milestone.milestone_id in blocker.blocking_milestones and milestone.status is not MilestoneStatus.COMPLETE:
                milestone.status = MilestoneStatus.AT_RISK

    def available_tasks(self) -> tuple[ProjectTask, ...]:
        return tuple(task for task in self.tasks if task.ready(self.tasks))

    def decide(self, *, pause: bool = False, reforecast: bool = False) -> ProjectControlDecision:
        if pause:
            return ProjectControlDecision.PAUSE
        if reforecast:
            return ProjectControlDecision.CONTINUE_WITH_REFORECAST
        if self.tasks and all(task.status is TaskStatus.BLOCKED for task in self.tasks if task.status not in {TaskStatus.DONE, TaskStatus.DEFERRED, TaskStatus.CANCELLED}):
            return ProjectControlDecision.BLOCKED
        return ProjectControlDecision.CONTINUE
