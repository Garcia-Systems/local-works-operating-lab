"""Proportional QA and customer-acceptance records for Chapter 25.

The module records fictional checks and decisions.  It neither operates a
customer environment nor proves that a project will create long-term ROI.
"""
from dataclasses import dataclass, field
from datetime import date
from enum import Enum

from .projects import Requirement, RequirementPriority, RequirementStatus


class TestType(Enum):
    FUNCTIONAL="Functional"; BUSINESS_RULE="Business rule"; WORKFLOW="Workflow"
    INTEGRATION="Integration"; DATA="Data"; SECURITY_ACCESS="Security/access"
    USABILITY="Usability"; ACCESSIBILITY="Accessibility"; ERROR_HANDLING="Error handling"
    REGRESSION="Regression"; DOCUMENTATION="Documentation"; DEPLOYMENT="Deployment"
    OPERATIONS="Operations"; OTHER="Other"


class TestStatus(Enum):
    NOT_RUN="Not run"; PASS="Pass"; FAIL="Fail"; BLOCKED="Blocked"
    NOT_APPLICABLE="Not applicable"; DEFERRED="Deferred"


class TestEnvironment(Enum):
    DEVELOPMENT="Development"; TEST="Test"; SANDBOX="Sandbox"; STAGING="Staging"
    PRODUCTION_LIKE="Production-like"; PRODUCTION="Production"; UNKNOWN="Unknown"


@dataclass(frozen=True)
class TestEvidence:
    kind: str
    reference: str
    notes: str = ""


@dataclass
class TestCase:
    test_id: str
    title: str
    test_type: TestType
    related_requirement: str | None = None
    related_business_rule: str | None = None
    related_acceptance_criterion: str | None = None
    preconditions: tuple[str, ...] = ()
    steps: tuple[str, ...] = ()
    expected_result: str = ""
    actual_result: str = "NOT_RUN"
    status: TestStatus = TestStatus.NOT_RUN
    evidence: tuple[TestEvidence, ...] = ()
    notes: str = ""
    environment: TestEnvironment = TestEnvironment.UNKNOWN

    @property
    def failed(self) -> bool:
        """A blocked case is deliberately not a failed case."""
        return self.status is TestStatus.FAIL

    def record(self, status: TestStatus, actual: str,
               evidence: tuple[TestEvidence, ...] = ()) -> None:
        self.status, self.actual_result, self.evidence = status, actual, evidence


TestResult = TestCase


class DefectSeverity(Enum):
    CRITICAL="Critical"; HIGH="High"; MEDIUM="Medium"; LOW="Low"; COSMETIC="Cosmetic"


class DefectStatus(Enum):
    OPEN="Open"; TRIAGED="Triaged"; IN_FIX="In fix"; READY_FOR_RETEST="Ready for retest"
    PASSED_RETEST="Passed retest"; DEFERRED="Deferred"
    ACCEPTED_AS_KNOWN_ISSUE="Accepted as known issue"; CLOSED="Closed"
    NOT_A_DEFECT="Not a defect"


@dataclass(frozen=True)
class RetestRecord:
    test_id: str
    result: TestStatus
    tested_on: date | None = None
    evidence: str = ""


@dataclass
class Defect:
    defect_id: str
    summary: str
    related_requirement: str | None
    related_test: str
    severity: DefectSeverity
    status: DefectStatus
    found_by: str
    environment: TestEnvironment
    expected: str
    actual: str
    business_impact: str
    owner: str = "UNASSIGNED"
    fix_required: bool = True
    target_retest: date | None = None
    priority: str = "UNKNOWN"
    notes: str = ""
    retests: list[RetestRecord] = field(default_factory=list)
    customer_found: bool = False
    reasonably_preventable: bool = False

    @property
    def blocks_acceptance(self) -> bool:
        return (self.severity in {DefectSeverity.CRITICAL, DefectSeverity.HIGH}
                and self.status not in {DefectStatus.CLOSED, DefectStatus.PASSED_RETEST,
                                        DefectStatus.NOT_A_DEFECT})

    @property
    def qa_escape(self) -> bool:
        return self.customer_found and self.reasonably_preventable

    def record_retest(self, record: RetestRecord) -> None:
        self.retests.append(record)
        if record.result is TestStatus.PASS:
            self.status = DefectStatus.PASSED_RETEST
            self.fix_required = False
        elif record.result is TestStatus.FAIL:
            self.status = DefectStatus.OPEN

    def close(self) -> None:
        if self.status is not DefectStatus.PASSED_RETEST:
            raise ValueError("A defect requiring correction must pass retest before closing.")
        self.status = DefectStatus.CLOSED


@dataclass(frozen=True)
class KnownIssue:
    description: str
    severity: DefectSeverity
    workaround: str
    business_impact: str
    planned_treatment: str
    accepted_by: str
    review_point: str = "UNKNOWN"
    blocking: bool = False


@dataclass(frozen=True)
class AcceptanceCriterionResult:
    criterion_id: str
    result: TestStatus
    related_tests: tuple[str, ...] = ()
    evidence: str = ""

    @property
    def blocks_acceptance(self) -> bool:
        return self.result is TestStatus.FAIL


class QAReadiness(Enum):
    READY="Ready"; READY_WITH_NONBLOCKERS="Ready with nonblockers"
    NOT_READY="Not ready"; BLOCKED="Blocked"


class AcceptanceStatus(Enum):
    ACCEPTED="Accepted"; ACCEPTED_WITH_KNOWN_ISSUES="Accepted with known issues"
    CONDITIONAL_ACCEPTANCE="Conditional acceptance"; REJECTED_FOR_DEFECTS="Rejected for defects"
    NEEDS_RETEST="Needs retest"; BLOCKED="Blocked"; CANCELLED="Cancelled"


@dataclass(frozen=True)
class AcceptanceDecision:
    status: AcceptanceStatus
    rationale: str
    evidence: tuple[str, ...] = ()
    business_success_proven: bool = False


@dataclass
class CustomerAcceptanceSession:
    session_date: date
    scope_version: str
    requirements_baseline: str
    representative_cases: tuple[str, ...]
    criterion_results: tuple[AcceptanceCriterionResult, ...]
    known_issues: tuple[KnownIssue, ...] = ()
    open_defects: tuple[Defect, ...] = ()
    evidence: tuple[str, ...] = ()

    def decide(self) -> AcceptanceDecision:
        if any(d.blocks_acceptance for d in self.open_defects):
            return AcceptanceDecision(AcceptanceStatus.REJECTED_FOR_DEFECTS,
                                      "A critical/high unresolved defect blocks acceptance.", self.evidence)
        if any(r.blocks_acceptance for r in self.criterion_results):
            return AcceptanceDecision(AcceptanceStatus.REJECTED_FOR_DEFECTS,
                                      "An acceptance criterion failed.", self.evidence)
        if any(r.result is TestStatus.BLOCKED for r in self.criterion_results):
            return AcceptanceDecision(AcceptanceStatus.BLOCKED,
                                      "Acceptance evidence is blocked.", self.evidence)
        if self.known_issues:
            return AcceptanceDecision(AcceptanceStatus.ACCEPTED_WITH_KNOWN_ISSUES,
                                      "Criteria pass; disclosed nonblocking issues were accepted.", self.evidence)
        return AcceptanceDecision(AcceptanceStatus.ACCEPTED,
                                  "The agreed scope and acceptance criteria passed.", self.evidence)


@dataclass
class QACycle:
    cycle_number: int
    tests: list[TestCase]
    defects: list[Defect] = field(default_factory=list)
    defect_rework_hours: float = 0
    scope_change_hours: float = 0

    @property
    def qa_escapes(self) -> int:
        return sum(d.qa_escape for d in self.defects)


def requirement_coverage(requirements: list[Requirement], tests: list[TestCase]) -> dict[str, str]:
    """Return lightweight coverage, explicitly flagging uncovered approved MUSTs."""
    covered = {t.related_requirement for t in tests if t.related_requirement
               and t.status is not TestStatus.NOT_APPLICABLE}
    output: dict[str, str] = {}
    for requirement in requirements:
        approved = requirement.status in {RequirementStatus.CONFIRMED,
                                          RequirementStatus.READY_FOR_IMPLEMENTATION}
        if approved and requirement.priority is RequirementPriority.MUST \
                and requirement.requirement_id not in covered:
            output[requirement.requirement_id] = "UNTESTED_REQUIREMENT"
        else:
            results = [t.status.name for t in tests
                       if t.related_requirement == requirement.requirement_id]
            output[requirement.requirement_id] = ", ".join(results) or "NO_MEANINGFUL_COVERAGE"
    return output


def qa_readiness(requirements: list[Requirement], tests: list[TestCase],
                 defects: list[Defect] | None = None) -> QAReadiness:
    coverage = requirement_coverage(requirements, tests)
    if "UNTESTED_REQUIREMENT" in coverage.values():
        return QAReadiness.NOT_READY
    if any(t.status is TestStatus.BLOCKED for t in tests):
        return QAReadiness.BLOCKED
    if any(d.blocks_acceptance for d in (defects or [])):
        return QAReadiness.NOT_READY
    return QAReadiness.READY


# These domain names intentionally begin with ``Test``.  Tell pytest that they
# are records imported by tests, rather than test containers of their own.
for _domain_type in (TestType, TestStatus, TestEnvironment, TestEvidence, TestCase):
    _domain_type.__test__ = False
