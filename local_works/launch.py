"""Business records for proportional launch and project closeout.

Nothing in this module deploys software, changes access, sends communication,
or processes payment.  It records decisions in fictional exercises.
"""
from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class LaunchStatus(Enum):
    ACCEPTED = "Accepted"
    LAUNCH_PENDING = "Launch pending"
    LAUNCH_READY = "Launch ready"
    LAUNCHED = "Launched"
    STABILIZING = "Stabilizing"
    COMMERCIAL_CLOSEOUT = "Commercial closeout"
    CLOSED = "Closed"


class LaunchDecision(Enum):
    READY_TO_LAUNCH = "Ready to launch"
    READY_WITH_MONITORED_RISKS = "Ready with monitored risks"
    NEEDS_ACCESS = "Needs access"
    NEEDS_DEFECT_RESOLUTION = "Needs defect resolution"
    NEEDS_CUSTOMER_APPROVAL = "Needs customer approval"
    NEEDS_DEPLOYMENT_PLAN = "Needs deployment plan"
    NEEDS_ROLLBACK_PLAN = "Needs rollback plan"
    NEEDS_VENDOR_COORDINATION = "Needs vendor coordination"
    BLOCKED = "Blocked"


class SolutionLaunchType(Enum):
    CONFIGURE = "Configure"
    INTEGRATE = "Integrate"
    AUTOMATE = "Automate"
    CUSTOM_BUILD = "Custom build"


class CutoverApproach(Enum):
    IMMEDIATE = "Immediate"
    SCHEDULED = "Scheduled"
    PHASED = "Phased"
    PILOT = "Pilot"
    PARALLEL = "Parallel"
    FEATURE_TOGGLE = "Feature toggle"
    MANUAL_TRANSITION = "Manual transition"
    NOT_APPLICABLE = "Not applicable"


class RollbackReadiness(Enum):
    AVAILABLE = "Available"
    PARTIAL = "Partial"
    MANUAL = "Manual"
    NOT_AVAILABLE = "Not available"
    NOT_APPLICABLE = "Not applicable"
    UNKNOWN = "UNKNOWN"


class ResponsibleParty(Enum):
    CUSTOMER = "Customer"
    LOCAL_WORKS = "Local Works"
    DELIVERY_PARTNER = "Delivery partner"
    VENDOR = "Vendor"
    SHARED = "Shared"


@dataclass(frozen=True)
class LaunchRequirement:
    name: str
    satisfied: bool
    blocking: bool = True
    unmet_decision: LaunchDecision = LaunchDecision.BLOCKED
    evidence: str = "UNKNOWN"


@dataclass(frozen=True)
class LaunchReadiness:
    accepted: bool
    requirements: tuple[LaunchRequirement, ...]
    known_nonblocking_issues: tuple[str, ...] = ()

    def decide(self) -> LaunchDecision:
        if not self.accepted:
            return LaunchDecision.NEEDS_CUSTOMER_APPROVAL
        unmet = [r for r in self.requirements if r.blocking and not r.satisfied]
        if unmet:
            return unmet[0].unmet_decision
        if self.known_nonblocking_issues or any(not r.satisfied for r in self.requirements):
            return LaunchDecision.READY_WITH_MONITORED_RISKS
        return LaunchDecision.READY_TO_LAUNCH


@dataclass(frozen=True)
class RollbackPlan:
    readiness: RollbackReadiness
    reversal: str
    decision_owner: ResponsibleParty
    triggers: tuple[str, ...] = ()


@dataclass(frozen=True)
class LaunchPlan:
    launch_type: SolutionLaunchType
    cutover: CutoverApproach
    planned_launch: date | None
    authorizer: ResponsibleParty
    performer: ResponsibleParty
    verifier: ResponsibleParty
    communicator: ResponsibleParty
    rollback: RollbackPlan
    verification_steps: tuple[str, ...]
    constraints: tuple[str, ...] = ()


@dataclass(frozen=True)
class LaunchEvent:
    occurred_on: date
    plan: LaunchPlan
    authorized_by: ResponsibleParty
    fictional: bool = True


@dataclass(frozen=True)
class ProductionCheck:
    behavior: str
    passed: bool
    evidence: str


class StabilizationStatus(Enum):
    STABLE = "Stable"
    MONITORING = "Monitoring"
    ISSUES_FOUND = "Issues found"
    ROLLBACK_REQUIRED = "Rollback required"
    EXTENDED_STABILIZATION = "Extended stabilization"


@dataclass(frozen=True)
class StabilizationPeriod:
    start: date
    end: date | None
    status: StabilizationStatus
    observations: tuple[str, ...] = ()


class CloseoutStatus(Enum):
    READY_TO_CLOSE = "Ready to close"
    CLOSED = "Closed"
    CLOSED_WITH_OUTSTANDING_PAYMENT = "Closed with outstanding payment"
    CLOSED_WITH_KNOWN_ISSUES = "Closed with known issues"
    MEASUREMENT_PENDING = "Measurement pending"
    COMMERCIAL_DISPUTE = "Commercial dispute"
    STABILIZATION_REQUIRED = "Stabilization required"
    BLOCKED = "Blocked"


@dataclass(frozen=True)
class CloseoutChecklist:
    operational_items: dict[str, bool]

    @property
    def complete(self) -> bool:
        return bool(self.operational_items) and all(self.operational_items.values())


@dataclass(frozen=True)
class ProjectCloseout:
    checklist: CloseoutChecklist
    stabilization: StabilizationStatus
    payment_outstanding: bool = False
    commercial_dispute: bool = False
    known_issues: tuple[str, ...] = ()
    value_measurement_pending: bool = False

    def status(self) -> CloseoutStatus:
        if self.commercial_dispute:
            return CloseoutStatus.COMMERCIAL_DISPUTE
        if self.stabilization is not StabilizationStatus.STABLE:
            return CloseoutStatus.STABILIZATION_REQUIRED
        if not self.checklist.complete:
            return CloseoutStatus.BLOCKED
        if self.payment_outstanding:
            return CloseoutStatus.CLOSED_WITH_OUTSTANDING_PAYMENT
        if self.known_issues:
            return CloseoutStatus.CLOSED_WITH_KNOWN_ISSUES
        if self.value_measurement_pending:
            return CloseoutStatus.MEASUREMENT_PENDING
        return CloseoutStatus.CLOSED
