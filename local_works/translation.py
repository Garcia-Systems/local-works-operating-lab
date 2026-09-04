"""Business-to-technical translation controls for Chapter 22.

The module records *what* delivery must accomplish and why.  It deliberately
does not prescribe production architecture, APIs, database tables, or vendor
workarounds.
"""

from dataclasses import dataclass
from enum import Enum

from local_works.projects import OpenQuestion, QuestionCategory, Requirement


class TranslationStatus(Enum):
    DRAFT = "Draft"
    NEEDS_BUSINESS_CLARIFICATION = "Needs business clarification"
    NEEDS_TECHNICAL_CLARIFICATION = "Needs technical clarification"
    READY_FOR_TECHNICAL_DESIGN = "Ready for technical design"
    READY_FOR_IMPLEMENTATION = "Ready for implementation"
    BLOCKED = "Blocked"
    SUPERSEDED = "Superseded"
    OUT_OF_SCOPE = "Out of scope"


class TranslationReadiness(Enum):
    READY_FOR_IMPLEMENTATION = "Ready for implementation"
    READY_WITH_OPEN_NONBLOCKERS = "Ready with open nonblockers"
    NEEDS_BUSINESS_CLARIFICATION = "Needs business clarification"
    NEEDS_TECHNICAL_VALIDATION = "Needs technical validation"
    NEEDS_SCOPE_REVIEW = "Needs scope review"
    NEEDS_SOLUTION_REVIEW = "Needs solution review"
    BLOCKED = "Blocked"


class DataSource(Enum):
    CUSTOMER_INPUT = "Customer input"
    EXISTING_PLATFORM = "Existing platform"
    OTHER_SYSTEM = "Other system"
    DERIVED = "Derived"
    MANUAL_STAFF_INPUT = "Manual staff input"
    UNKNOWN = "UNKNOWN"


class DataAction(Enum):
    READ = "Read"
    CREATE = "Create"
    UPDATE = "Update"
    SEND = "Send"
    DISPLAY = "Display"
    STORE = "Store"
    TRANSFORM = "Transform"
    VALIDATE = "Validate"
    UNKNOWN = "UNKNOWN"


class TechnicalTaskCategory(Enum):
    VALIDATE_CAPABILITY = "Validate capability"
    CONFIGURE = "Configure"
    IMPLEMENT = "Implement"
    INTEGRATE = "Integrate"
    AUTOMATE = "Automate"
    TEST = "Test"
    DOCUMENT = "Document"
    DEPLOY = "Deploy"
    INVESTIGATE = "Investigate"
    OTHER = "Other"


class VendorLimitationOutcome(Enum):
    REVISE_TECHNICAL_DESIGN = "Revise technical design"
    REVISIT_SCOPE = "Revisit scope"
    REVISIT_SOLUTION = "Revisit solution"
    CUSTOMER_DECISION_REQUIRED = "Customer decision required"


@dataclass(frozen=True)
class BusinessStatement:
    statement_id: str
    wording: str
    speaker_role: str
    source: str
    context: str = ""
    evidence_reference: str = "UNKNOWN"
    interpretation: str = "UNKNOWN"


@dataclass(frozen=True)
class BusinessIntent:
    statement_id: str
    desired_outcome: str
    affected_party: str
    workflow_reference: str
    evidence: str = "UNKNOWN"
    status: str = "DRAFT"


@dataclass(frozen=True)
class BusinessRuleReference:
    rule_id: str
    statement: str
    evidence_reference: str = "UNKNOWN"
    confirmed: bool = False


@dataclass(frozen=True)
class WorkflowBehavior:
    behavior_id: str
    description: str
    actors: tuple[str, ...]
    workflow_reference: str


@dataclass(frozen=True)
class DataNeed:
    name: str
    purpose: str
    source: DataSource = DataSource.UNKNOWN
    actions: tuple[DataAction, ...] = (DataAction.UNKNOWN,)
    destination: str = "UNKNOWN"


@dataclass(frozen=True)
class TechnicalNeed:
    need_id: str
    statement: str
    related_requirement_ids: tuple[str, ...]
    related_workflow_behavior_ids: tuple[str, ...] = ()
    data_needs: tuple[DataNeed, ...] = ()
    system_interactions: tuple[str, ...] = ()


@dataclass(frozen=True)
class TechnicalQuestion:
    question_id: str
    question: str
    why_it_matters: str
    related_requirement: str
    related_business_rule: str = "NONE"
    owner: str = "UNASSIGNED"
    blocking: bool = False
    status: str = "OPEN"
    answer: str = "UNKNOWN"
    evidence: str = "UNKNOWN"

    @property
    def unresolved(self) -> bool:
        return self.status.upper() in {"OPEN", "BLOCKED_EXTERNAL"} or self.answer == "UNKNOWN"


@dataclass(frozen=True)
class TechnicalConstraint:
    constraint_id: str
    statement: str
    source_reference: str = "UNKNOWN"
    constraint_type: str = "PLATFORM_LIMITATION"
    confirmed: bool = False


@dataclass(frozen=True)
class TranslationRisk:
    risk_id: str
    statement: str
    impact: str
    response: str = "UNKNOWN"


@dataclass(frozen=True)
class TechnicalTask:
    task_id: str
    title: str
    description: str
    category: TechnicalTaskCategory
    done_condition: str
    related_requirement_ids: tuple[str, ...] = ()
    related_workflow_behavior_ids: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = ()
    risk_justifications: tuple[str, ...] = ()
    acceptance_linkage: tuple[str, ...] = ()
    status: str = "PLANNED"

    def __post_init__(self) -> None:
        if not self.done_condition.strip():
            raise ValueError("A technical task requires an observable done condition")

    @property
    def justified(self) -> bool:
        return bool(self.related_requirement_ids or self.acceptance_linkage or self.risk_justifications)


@dataclass(frozen=True)
class TechnicalDecision:
    decision: str
    context: str
    options: tuple[str, ...]
    selected_option: str
    reason: str
    affected_requirements: tuple[str, ...] = ()
    affected_risks: tuple[str, ...] = ()
    status: str = "PROPOSED"


@dataclass(frozen=True)
class TraceabilityLink:
    statement_id: str
    intent: str
    requirement_id: str
    business_rule_id: str
    workflow_behavior_id: str
    technical_need_id: str
    technical_task_id: str
    test_id: str
    acceptance_criterion_id: str


@dataclass
class TranslationRecord:
    translation_id: str
    source_statement: BusinessStatement
    business_intent: BusinessIntent
    requirement_ids: tuple[str, ...]
    business_rule_references: tuple[BusinessRuleReference, ...] = ()
    workflow_behaviors: tuple[WorkflowBehavior, ...] = ()
    technical_needs: tuple[TechnicalNeed, ...] = ()
    technical_questions: tuple[TechnicalQuestion, ...] = ()
    technical_constraints: tuple[TechnicalConstraint, ...] = ()
    technical_tasks: tuple[TechnicalTask, ...] = ()
    traceability_links: tuple[TraceabilityLink, ...] = ()
    status: TranslationStatus = TranslationStatus.DRAFT
    risks: tuple[TranslationRisk, ...] = ()

    def references_known_requirements(self, requirements: list[Requirement]) -> bool:
        known = {requirement.requirement_id for requirement in requirements}
        return bool(self.requirement_ids) and set(self.requirement_ids) <= known


def business_question(question: OpenQuestion) -> bool:
    """Keep policy ownership separate from delivery/vendor investigation."""
    return question.category in {QuestionCategory.BUSINESS_RULE, QuestionCategory.SCOPE, QuestionCategory.ACCEPTANCE}


def missing_technical_coverage(requirements: list[Requirement], needs: list[TechnicalNeed], tasks: list[TechnicalTask]) -> tuple[str, ...]:
    covered = {item for need in needs for item in need.related_requirement_ids}
    covered.update(item for task in tasks for item in task.related_requirement_ids)
    return tuple(r.requirement_id for r in requirements if r.status.name != "OUT_OF_SCOPE" and r.requirement_id not in covered)


def unjustified_technical_work(tasks: list[TechnicalTask]) -> tuple[str, ...]:
    return tuple(task.task_id for task in tasks if not task.justified)


def gold_plated_work(tasks: list[TechnicalTask]) -> tuple[str, ...]:
    """Flag expansion by absent justification, not by declaring technologies bad."""
    expansion = ("real-time", "websocket", "microservice", "data warehouse", "analytics dashboard", "custom identity")
    return tuple(task.task_id for task in tasks if not task.justified and any(term in f"{task.title} {task.description}".lower() for term in expansion))


def readiness(records: list[TranslationRecord], business_questions: list[OpenQuestion] | None = None,
              technical_questions: list[TechnicalQuestion] | None = None) -> TranslationReadiness:
    if any(record.status is TranslationStatus.BLOCKED for record in records):
        return TranslationReadiness.BLOCKED
    if any(q.blocking and q.unresolved for q in business_questions or []):
        return TranslationReadiness.NEEDS_BUSINESS_CLARIFICATION
    if any(q.blocking and q.unresolved for q in technical_questions or []):
        return TranslationReadiness.NEEDS_TECHNICAL_VALIDATION
    if any(record.status is TranslationStatus.NEEDS_BUSINESS_CLARIFICATION for record in records):
        return TranslationReadiness.NEEDS_BUSINESS_CLARIFICATION
    if any(record.status is TranslationStatus.NEEDS_TECHNICAL_CLARIFICATION for record in records):
        return TranslationReadiness.NEEDS_TECHNICAL_VALIDATION
    if any(q.unresolved for q in (business_questions or [])) or any(q.unresolved for q in (technical_questions or [])):
        return TranslationReadiness.READY_WITH_OPEN_NONBLOCKERS
    return TranslationReadiness.READY_FOR_IMPLEMENTATION


def vendor_limitation_outcome(*, need_in_scope: bool, alternate_within_solution: bool, solution_still_viable: bool) -> VendorLimitationOutcome:
    if alternate_within_solution:
        return VendorLimitationOutcome.REVISE_TECHNICAL_DESIGN
    if not need_in_scope:
        return VendorLimitationOutcome.REVISIT_SCOPE
    if not solution_still_viable:
        return VendorLimitationOutcome.REVISIT_SOLUTION
    return VendorLimitationOutcome.CUSTOMER_DECISION_REQUIRED
