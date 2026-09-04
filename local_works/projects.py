"""Project kickoff and requirements controls for Chapter 21.

The records in this module coordinate an authorized engagement.  They do not
authorize commercial work, change scope, select architecture, or start
implementation.
"""

from dataclasses import dataclass, field
from enum import Enum


class ProjectStatus(Enum):
    AUTHORIZED = "Authorized"
    KICKOFF_PREPARING = "Kickoff preparing"
    KICKOFF_COMPLETE = "Kickoff complete"
    REQUIREMENTS_IN_PROGRESS = "Requirements in progress"
    READY_FOR_IMPLEMENTATION = "Ready for implementation"
    IMPLEMENTATION_IN_PROGRESS = "Implementation in progress"
    BLOCKED = "Blocked"
    ON_HOLD = "On hold"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class KickoffStatus(Enum):
    READY_FOR_KICKOFF = "Ready for kickoff"
    NEEDS_COMMERCIAL_CLARIFICATION = "Needs commercial clarification"
    NEEDS_DELIVERY_CLARIFICATION = "Needs delivery clarification"
    NEEDS_ACCESS_PREPARATION = "Needs access preparation"
    NEEDS_PARTICIPANT_CONFIRMATION = "Needs participant confirmation"
    BLOCKED = "Blocked"


class ParticipantRole(Enum):
    CUSTOMER_SPONSOR = "Customer sponsor"
    CUSTOMER_DECISION_MAKER = "Customer decision maker"
    CUSTOMER_SUBJECT_MATTER_EXPERT = "Customer subject-matter expert"
    CUSTOMER_TECHNICAL_CONTACT = "Customer technical contact"
    LOCAL_WORKS_PROJECT_LEAD = "Local Works project lead"
    LOCAL_WORKS_SOLUTION_LEAD = "Local Works solution lead"
    DELIVERY_TECHNICAL_LEAD = "Delivery technical lead"
    DELIVERY_IMPLEMENTER = "Delivery implementer"
    QA = "QA"
    THIRD_PARTY_VENDOR_CONTACT = "Third-party vendor contact"
    OTHER = "Other"


@dataclass(frozen=True)
class ProjectParticipant:
    role: ParticipantRole
    organization: str
    responsibilities: tuple[str, ...]
    decision_authority: tuple[str, ...] = ()
    name: str = "UNASSIGNED"
    communication_needs: str = ""
    availability_notes: str = ""


class RequirementType(Enum):
    BUSINESS_RULE = "Business rule"
    FUNCTIONAL = "Functional"
    DATA = "Data"
    INTEGRATION = "Integration"
    SECURITY = "Security"
    ACCESS = "Access"
    USABILITY = "Usability"
    ACCESSIBILITY = "Accessibility"
    PERFORMANCE = "Performance"
    RELIABILITY = "Reliability"
    AUDITABILITY = "Auditability"
    OPERATIONS = "Operations"
    DOCUMENTATION = "Documentation"
    TESTING = "Testing"
    DEPLOYMENT = "Deployment"
    OTHER = "Other"


class RequirementPriority(Enum):
    MUST = "Must"
    SHOULD = "Should"
    COULD = "Could"
    NOT_IN_SCOPE = "Not in scope"


class RequirementStatus(Enum):
    DRAFT = "Draft"
    CONFIRMED = "Confirmed"
    NEEDS_CLARIFICATION = "Needs clarification"
    BLOCKED = "Blocked"
    DEFERRED = "Deferred"
    OUT_OF_SCOPE = "Out of scope"
    READY_FOR_IMPLEMENTATION = "Ready for implementation"
    INVALIDATED = "Invalidated"


class RequirementSource(Enum):
    DISCOVERY = "Discovery"
    WORKFLOW = "Workflow"
    SCOPE = "Scope"
    CUSTOMER_POLICY = "Customer policy"
    CUSTOMER_STATEMENT = "Customer statement"
    TECHNICAL_VALIDATION = "Technical validation"
    DELIVERY_PARTNER = "Delivery partner"
    VENDOR_DOCUMENTATION = "Vendor documentation"
    ACCEPTANCE_CRITERIA = "Acceptance criteria"
    OTHER = "Other"


@dataclass(frozen=True)
class Requirement:
    requirement_id: str
    statement: str
    requirement_type: RequirementType
    priority: RequirementPriority
    source: RequirementSource
    evidence_reference: str
    related_scope: tuple[str, ...] = ()
    acceptance_linkage: tuple[str, ...] = ()
    status: RequirementStatus = RequirementStatus.DRAFT
    open_question_ids: tuple[str, ...] = ()
    notes: str = ""



@dataclass(frozen=True)
class TechnicalDesign:
    """A proposed implementation choice, deliberately separate from a requirement."""

    statement: str
    related_requirement_ids: tuple[str, ...]
    evidence_reference: str = "UNKNOWN"
    status: str = "PROPOSED"


class QuestionCategory(Enum):
    BUSINESS_RULE = "Business rule"
    TECHNICAL = "Technical"
    VENDOR = "Vendor"
    DATA = "Data"
    ACCESS = "Access"
    SECURITY = "Security"
    SCOPE = "Scope"
    ACCEPTANCE = "Acceptance"
    OTHER = "Other"


class QuestionStatus(Enum):
    OPEN = "Open"
    ANSWERED = "Answered"
    DEFERRED = "Deferred"
    NOT_NEEDED = "Not needed"
    BLOCKED_EXTERNAL = "Blocked externally"


@dataclass(frozen=True)
class OpenQuestion:
    question_id: str
    question: str
    category: QuestionCategory
    owner: str
    why_it_matters: str
    blocking: bool
    due_or_needed_by: str = "Before affected work begins"
    status: QuestionStatus = QuestionStatus.OPEN
    answer: str = "UNKNOWN"
    evidence_reference: str = "UNKNOWN"

    @property
    def unresolved(self) -> bool:
        return self.status in {QuestionStatus.OPEN, QuestionStatus.BLOCKED_EXTERNAL}


class BaselineStatus(Enum):
    DRAFT = "Draft"
    REVIEWED = "Reviewed"
    APPROVED_FOR_IMPLEMENTATION = "Approved for implementation"
    SUPERSEDED = "Superseded"


class RequirementDecision(Enum):
    CLARIFICATION = "Clarification"
    CORRECTION = "Correction"
    NEW_REQUIREMENT = "New requirement"
    SCOPE_CHANGE = "Scope change"
    TECHNICAL_DISCOVERY = "Technical discovery"
    DEFECT_DISCOVERY = "Defect discovery"


class ImplementationReadiness(Enum):
    READY_FOR_IMPLEMENTATION = "Ready for implementation"
    READY_WITH_OPEN_NONBLOCKERS = "Ready with open nonblockers"
    NEEDS_BUSINESS_DECISIONS = "Needs business decisions"
    NEEDS_TECHNICAL_VALIDATION = "Needs technical validation"
    NEEDS_ACCESS = "Needs access"
    NEEDS_SCOPE_CLARIFICATION = "Needs scope clarification"
    BLOCKED = "Blocked"


@dataclass(frozen=True)
class ProjectConstraint:
    statement: str
    source_reference: str = "UNKNOWN"


@dataclass(frozen=True)
class ProjectDependency:
    statement: str
    owner: str
    status: str = "UNKNOWN"


@dataclass(frozen=True)
class ProjectDecision:
    subject: str
    decision: str
    authority: str
    evidence_reference: str


@dataclass(frozen=True)
class ProjectContextPack:
    problem_statement: str
    current_workflow: str
    economic_rationale: str
    selected_solution: str
    approved_scope: tuple[str, ...]
    excluded_scope: tuple[str, ...]
    acceptance_criteria: tuple[str, ...]
    source_references: tuple[str, ...]
    responsibility_summary: tuple[str, ...] = ()
    technical_estimate_reference: str = "UNKNOWN"
    delivery_risks: tuple[str, ...] = ()
    known_systems: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = ()
    dependencies: tuple[str, ...] = ()
    open_technical_questions: tuple[str, ...] = ()
    decision_history: tuple[str, ...] = ()


@dataclass
class RequirementBaseline:
    version: str
    requirements: list[Requirement]
    status: BaselineStatus = BaselineStatus.DRAFT
    prior_version: str | None = None

    def classify_new_information(self, statement: str, approved_scope: tuple[str, ...]) -> RequirementDecision:
        text = statement.lower()
        if "which" in text and any(word in text for word in ("manager", "role", "owner")):
            return RequirementDecision.CLARIFICATION
        expansion_terms = ("cancellation", "mobile app", "referral", "payment update")
        requested_expansions = tuple(term for term in expansion_terms if term in text)
        if requested_expansions and not all(
            any(term in scope.lower() for scope in approved_scope)
            for term in requested_expansions
        ):
            return RequirementDecision.SCOPE_CHANGE
        return RequirementDecision.NEW_REQUIREMENT

    def readiness(self, questions: list[OpenQuestion]) -> ImplementationReadiness:
        active = [q for q in questions if q.unresolved]
        blockers = [q for q in active if q.blocking]
        if blockers:
            categories = {q.category for q in blockers}
            if QuestionCategory.SCOPE in categories:
                return ImplementationReadiness.NEEDS_SCOPE_CLARIFICATION
            if QuestionCategory.BUSINESS_RULE in categories:
                return ImplementationReadiness.NEEDS_BUSINESS_DECISIONS
            if QuestionCategory.ACCESS in categories:
                return ImplementationReadiness.NEEDS_ACCESS
            if categories & {QuestionCategory.TECHNICAL, QuestionCategory.VENDOR, QuestionCategory.DATA, QuestionCategory.SECURITY}:
                return ImplementationReadiness.NEEDS_TECHNICAL_VALIDATION
            return ImplementationReadiness.BLOCKED
        if any(r.status in {RequirementStatus.BLOCKED, RequirementStatus.NEEDS_CLARIFICATION} for r in self.requirements):
            return ImplementationReadiness.BLOCKED
        if active:
            return ImplementationReadiness.READY_WITH_OPEN_NONBLOCKERS
        return ImplementationReadiness.READY_FOR_IMPLEMENTATION


@dataclass(frozen=True)
class Kickoff:
    commercial_authorized: bool
    delivery_path_selected: bool
    scope_version: str
    commercial_version: str
    estimate_reference: str
    control_risks_ready: bool
    responsibilities_known: bool
    customer_participants_identified: bool
    local_works_participants_identified: bool
    delivery_participants_identified: bool
    access_requests_identified: bool
    context_available: bool

    def readiness(self) -> KickoffStatus:
        if not self.commercial_authorized or not self.scope_version or not self.commercial_version:
            return KickoffStatus.NEEDS_COMMERCIAL_CLARIFICATION
        if not self.delivery_path_selected or not self.estimate_reference or not self.responsibilities_known:
            return KickoffStatus.NEEDS_DELIVERY_CLARIFICATION
        if not all((self.customer_participants_identified, self.local_works_participants_identified, self.delivery_participants_identified)):
            return KickoffStatus.NEEDS_PARTICIPANT_CONFIRMATION
        if not self.access_requests_identified:
            return KickoffStatus.NEEDS_ACCESS_PREPARATION
        if not self.control_risks_ready or not self.context_available:
            return KickoffStatus.BLOCKED
        return KickoffStatus.READY_FOR_KICKOFF


@dataclass
class Project:
    project_id: str
    business: str
    commercial_source: str
    commercial_version: str
    scope_version: str
    estimate_reference: str
    approved_scope: tuple[str, ...]
    excluded_scope: tuple[str, ...]
    status: ProjectStatus = ProjectStatus.AUTHORIZED
    participants: list[ProjectParticipant] = field(default_factory=list)
    requirements: list[Requirement] = field(default_factory=list)

    def add_requirement(self, requirement: Requirement) -> None:
        """Add a requirement without changing the approved scope or starting work."""
        self.requirements.append(requirement)

    def request_feature(self, statement: str) -> Requirement:
        """Record an unsolicited feature visibly outside the approved boundary."""
        requirement = Requirement(
            requirement_id=f"R-{len(self.requirements) + 1:03d}",
            statement=statement,
            requirement_type=RequirementType.FUNCTIONAL,
            priority=RequirementPriority.NOT_IN_SCOPE,
            source=RequirementSource.CUSTOMER_STATEMENT,
            evidence_reference="Kickoff request",
            status=RequirementStatus.OUT_OF_SCOPE,
        )
        self.requirements.append(requirement)
        return requirement
