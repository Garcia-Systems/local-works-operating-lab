"""Operational-control and delivery-responsibility records for Chapter 20.

The module does not decide legal ownership, provision access, or start a
project.  It makes continuity conditions explicit before kickoff.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class AssetType(Enum):
    SOURCE_REPOSITORY = "Source repository"
    DEPLOYMENT_CONFIGURATION = "Deployment configuration"
    HOSTING_ACCOUNT = "Hosting account"
    DOMAIN_ACCOUNT = "Domain account"
    CLOUD_ACCOUNT = "Cloud account"
    DATABASE_ACCESS = "Database access"
    API_CREDENTIAL = "API credential"
    VENDOR_ACCOUNT = "Vendor account"
    AUTOMATION_ACCOUNT = "Automation account"
    MONITORING_ACCOUNT = "Monitoring account"
    DOCUMENTATION = "Documentation"
    ARCHITECTURE_NOTES = "Architecture notes"
    DECISION_LOG = "Decision log"
    REQUIREMENTS = "Requirements"
    TEST_ASSETS = "Test assets"
    TEST_DATA = "Test data"
    ACCEPTANCE_CRITERIA = "Acceptance criteria"
    PROJECT_FILES = "Project files"
    DESIGN_FILES = "Design files"
    THIRD_PARTY_LICENSE = "Third-party license"
    OTHER = "Other"


class ControlParty(Enum):
    CUSTOMER = "Customer"
    LOCAL_WORKS = "Local Works"
    DELIVERY_PARTNER = "Delivery partner"
    THIRD_PARTY_VENDOR = "Third-party vendor"
    SHARED = "Shared"
    UNKNOWN = "Unknown"


class ControlStatus(Enum):
    CONTROLLED = "Controlled"
    NEEDS_ACTION = "Needs action"
    NOT_APPLICABLE = "Not applicable"
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class DeliveryAsset:
    name: str
    asset_type: AssetType
    legal_owner: str = "UNKNOWN"
    notes: str = ""


@dataclass(frozen=True)
class AssetControl:
    asset: DeliveryAsset
    primary_controller: ControlParty
    administrative_access: tuple[ControlParty, ...] = ()
    backup_access: tuple[ControlParty, ...] = ()
    recovery_path: str = "UNKNOWN"
    transferability: str = "UNKNOWN"
    status: ControlStatus = ControlStatus.UNKNOWN
    notes: str = ""

    @property
    def has_recovery_path(self) -> bool:
        return self.recovery_path.strip().upper() not in {"", "UNKNOWN", "NONE"}


class AccessStatus(Enum):
    PLANNED = "Planned"
    ACTIVE = "Active"
    REVOKED = "Revoked"
    NOT_APPLICABLE = "Not applicable"
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class AccessRecord:
    asset: str
    party: ControlParty
    access_level: str
    purpose: str
    granted_date: date | None = None
    expected_revocation: date | str | None = None
    revocation_path: str = "UNKNOWN"
    status: AccessStatus = AccessStatus.PLANNED


class ResponsibilityType(Enum):
    BUSINESS_DECISION = "Business decision"
    SCOPE_AUTHORITY = "Scope authority"
    CUSTOMER_COMMUNICATION = "Customer communication"
    TECHNICAL_IMPLEMENTATION = "Technical implementation"
    TECHNICAL_DESIGN = "Technical design"
    TECHNICAL_ESTIMATION = "Technical estimation"
    PROJECT_COORDINATION = "Project coordination"
    QA_COORDINATION = "QA coordination"
    TEST_EXECUTION = "Test execution"
    CUSTOMER_ACCEPTANCE = "Customer acceptance"
    DEPLOYMENT = "Deployment"
    DOCUMENTATION = "Documentation"
    SECURITY_ACCESS = "Security/access administration"
    VENDOR_ESCALATION = "Vendor escalation"
    SUPPORT_HANDOFF = "Support handoff"
    CHANGE_APPROVAL = "Change approval"
    PAYMENT_APPROVAL = "Payment approval"
    MONITORING = "Monitoring"
    OTHER = "Other"


@dataclass(frozen=True)
class ResponsibilityAssignment:
    responsibility: ResponsibilityType
    accountable: ControlParty | None
    performing: tuple[ControlParty, ...] = ()
    consulted: tuple[ControlParty, ...] = ()
    informed: tuple[ControlParty, ...] = ()
    status: str = "Assigned"
    notes: str = ""

    @property
    def has_gap(self) -> bool:
        return self.accountable in {None, ControlParty.UNKNOWN} or not self.performing

    @property
    def has_authority_overlap(self) -> bool:
        return len(set(self.performing)) > 1 and self.responsibility in {
            ResponsibilityType.CHANGE_APPROVAL,
            ResponsibilityType.DEPLOYMENT,
            ResponsibilityType.SECURITY_ACCESS,
        }


class KnowledgeCategory(Enum):
    BUSINESS_RULES = "Business rules"
    ARCHITECTURE = "Architecture"
    DEPLOYMENT = "Deployment"
    INTEGRATION = "Integration"
    CONFIGURATION = "Configuration"
    DATA_MAPPING = "Data mapping"
    TESTING = "Testing"
    TROUBLESHOOTING = "Troubleshooting"
    OPERATIONS = "Operations"
    DECISION_HISTORY = "Decision history"
    OTHER = "Other"


class ContinuityResult(Enum):
    RECOVERABLE = "Recoverable"
    RECOVERABLE_WITH_EFFORT = "Recoverable with effort"
    HIGH_RISK = "High risk"
    NOT_RECOVERABLE = "Not recoverable"
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class KnowledgeArtifact:
    name: str
    category: KnowledgeCategory
    required: bool
    current_holder: ControlParty
    documented: bool
    location: str = "UNKNOWN"
    transition_readiness: ContinuityResult = ContinuityResult.UNKNOWN


@dataclass(frozen=True)
class DecisionRecord:
    decision: str
    context: str
    rationale: str
    authority: ControlParty
    reference: str = ""


@dataclass(frozen=True)
class ThirdPartyDependency:
    name: str
    criticality: str
    owner: ControlParty
    access: str
    support_path: str
    known_limitation: str
    failure_impact: str
    fallback: str
    status: str


@dataclass(frozen=True)
class EscalationPath:
    issue_source: ControlParty
    triage: ControlParty
    investigation: tuple[ControlParty, ...]
    communication: ControlParty
    risky_change_approval: ControlParty


class RiskCategory(Enum):
    SOURCE_CONTROL = "Source control"
    ACCOUNT_CONTROL = "Account control"
    ACCESS_CONTROL = "Access control"
    KNOWLEDGE_CONCENTRATION = "Knowledge concentration"
    DOCUMENTATION_GAP = "Documentation gap"
    RESPONSIBILITY_GAP = "Responsibility gap"
    AUTHORITY_AMBIGUITY = "Authority ambiguity"
    THIRD_PARTY_DEPENDENCY = "Third-party dependency"
    VENDOR_LOCK_IN = "Vendor lock-in"
    KEY_PERSON_DEPENDENCY = "Key-person dependency"
    SECURITY_ACCESS = "Security access"
    DEPLOYMENT_RECOVERY = "Deployment recovery"
    SUPPORT_HANDOFF = "Support handoff"
    COMMUNICATION = "Communication"
    CHANGE_CONTROL = "Change control"
    OTHER = "Other"


class RiskSeverity(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class RiskStatus(Enum):
    OPEN = "Open"
    MITIGATING = "Mitigating"
    MONITORED = "Monitored"
    RESOLVED = "Resolved"
    ACCEPTED = "Accepted"


@dataclass(frozen=True)
class DeliveryRisk:
    description: str
    category: RiskCategory
    severity: RiskSeverity
    evidence: str
    mitigation: str
    owner: ControlParty
    blocking: bool = False
    status: RiskStatus = RiskStatus.OPEN
    likelihood: str = "UNKNOWN"


class DeliveryReadinessDecision(Enum):
    READY_FOR_KICKOFF = "Ready for kickoff"
    READY_WITH_MONITORED_RISKS = "Ready with monitored risks"
    NEEDS_CONTROL_REMEDIATION = "Needs control remediation"
    NEEDS_DOCUMENTATION_PLAN = "Needs documentation plan"
    NEEDS_ACCESS_PLAN = "Needs access plan"
    NEEDS_RESPONSIBILITY_CLARIFICATION = "Needs responsibility clarification"
    NEEDS_PARTNER_RENEGOTIATION = "Needs partner renegotiation"
    REOPEN_DELIVERY_SELECTION = "Reopen delivery selection"
    BLOCKED = "Blocked"


@dataclass(frozen=True)
class ContinuityRequirement:
    question: str
    result: ContinuityResult
    evidence: str = "UNKNOWN"
    required: bool = True


def evaluate_continuity(requirements: list[ContinuityRequirement]) -> ContinuityResult:
    relevant = [item.result for item in requirements if item.required]
    if not relevant or ContinuityResult.UNKNOWN in relevant:
        return ContinuityResult.UNKNOWN
    if ContinuityResult.NOT_RECOVERABLE in relevant:
        return ContinuityResult.NOT_RECOVERABLE
    if ContinuityResult.HIGH_RISK in relevant:
        return ContinuityResult.HIGH_RISK
    if ContinuityResult.RECOVERABLE_WITH_EFFORT in relevant:
        return ContinuityResult.RECOVERABLE_WITH_EFFORT
    return ContinuityResult.RECOVERABLE


def detect_control_risks(controls: list[AssetControl]) -> list[DeliveryRisk]:
    """Expose control facts without assuming partner control is always wrong."""
    risks: list[DeliveryRisk] = []
    for control in controls:
        if control.status is ControlStatus.NOT_APPLICABLE:
            continue
        partner_only = (control.primary_controller is ControlParty.DELIVERY_PARTNER
                        and not ({ControlParty.CUSTOMER, ControlParty.LOCAL_WORKS}
                                 & set(control.backup_access)))
        if control.asset.asset_type is AssetType.SOURCE_REPOSITORY and partner_only:
            category = RiskCategory.SOURCE_CONTROL
        elif control.asset.asset_type is AssetType.DEPLOYMENT_CONFIGURATION and not control.has_recovery_path:
            category = RiskCategory.DEPLOYMENT_RECOVERY
        elif control.asset.asset_type in {AssetType.HOSTING_ACCOUNT, AssetType.DOMAIN_ACCOUNT,
                                         AssetType.CLOUD_ACCOUNT, AssetType.VENDOR_ACCOUNT} and partner_only:
            category = RiskCategory.ACCOUNT_CONTROL
        else:
            category = RiskCategory.OTHER
        if category is not RiskCategory.OTHER:
            risks.append(DeliveryRisk(
                f"{control.asset.name} lacks transition-safe operational control",
                category, RiskSeverity.CRITICAL if not control.has_recovery_path else RiskSeverity.HIGH,
                f"Primary controller: {control.primary_controller.value}; recovery: {control.recovery_path}",
                "Add organizational backup access and a documented recovery path",
                ControlParty.LOCAL_WORKS, blocking=not control.has_recovery_path))
    return risks


@dataclass
class DeliveryReadiness:
    controls: list[AssetControl] = field(default_factory=list)
    responsibilities: list[ResponsibilityAssignment] = field(default_factory=list)
    knowledge: list[KnowledgeArtifact] = field(default_factory=list)
    risks: list[DeliveryRisk] = field(default_factory=list)
    partner_continuity: list[ContinuityRequirement] = field(default_factory=list)
    local_works_continuity: list[ContinuityRequirement] = field(default_factory=list)
    kickoff_started: bool = False

    def responsibility_gaps(self) -> list[ResponsibilityAssignment]:
        return [item for item in self.responsibilities if item.has_gap]

    def authority_overlaps(self) -> list[ResponsibilityAssignment]:
        return [item for item in self.responsibilities if item.has_authority_overlap]

    def assess(self) -> DeliveryReadinessDecision:
        all_risks = [*self.risks, *detect_control_risks(self.controls)]
        if any(r.blocking and r.status not in {RiskStatus.RESOLVED, RiskStatus.ACCEPTED} for r in all_risks):
            return DeliveryReadinessDecision.BLOCKED
        if self.responsibility_gaps():
            return DeliveryReadinessDecision.NEEDS_RESPONSIBILITY_CLARIFICATION
        unresolved = [r for r in all_risks if r.status is not RiskStatus.RESOLVED]
        if unresolved:
            return DeliveryReadinessDecision.READY_WITH_MONITORED_RISKS
        return DeliveryReadinessDecision.READY_FOR_KICKOFF
