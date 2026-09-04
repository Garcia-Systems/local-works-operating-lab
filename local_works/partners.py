"""Readable delivery-path and partner prequalification records for Chapter 18.

The model stops at qualification for an estimate.  It does not request an
estimate, appoint a provider, authorize implementation, or manage credentials.
"""

from dataclasses import dataclass, field
from enum import Enum


class DeliveryPathType(Enum):
    LOCAL_WORKS_SELF_DELIVERY = "Local Works self delivery"
    INDEPENDENT_CONTRACTOR = "Independent contractor"
    SPECIALIST_FREELANCER = "Specialist freelancer"
    SMALL_AGENCY = "Small agency"
    LARGER_AGENCY = "Larger agency"
    PLATFORM_IMPLEMENTATION_PARTNER = "Platform implementation partner"
    VENDOR_PROFESSIONAL_SERVICES = "Vendor professional services"
    CUSTOMER_INTERNAL_TEAM = "Customer internal team"
    MIXED_TEAM = "Mixed team"
    NO_EXTERNAL_DELIVERY_REQUIRED = "No external delivery required"


class RequirementLevel(Enum):
    REQUIRED = "Required"
    OPTIONAL = "Optional"


class FitRating(Enum):
    STRONG = "Strong"
    ADEQUATE = "Adequate"
    UNCERTAIN = "Uncertain"
    WEAK = "Weak"
    NO_FIT = "No fit"


class FitDimension(Enum):
    TECHNICAL_FIT = "Technical fit"
    PLATFORM_EXPERIENCE = "Platform experience"
    INTEGRATION_EXPERIENCE = "Integration experience"
    SECURITY_AWARENESS = "Security awareness"
    TESTING_QUALITY = "Testing quality"
    DOCUMENTATION = "Documentation"
    COMMUNICATION = "Communication"
    AVAILABILITY = "Availability"
    CAPACITY = "Capacity"
    RELIABILITY = "Reliability"
    SUPPORT_HANDOFF = "Support handoff"
    COST_FIT = "Cost fit"


class EvidenceType(Enum):
    SELF_REPORTED = "Self reported"
    PUBLIC_PORTFOLIO = "Public portfolio"
    REFERENCE = "Reference"
    DIRECT_EVALUATION = "Direct evaluation"
    PAST_PERFORMANCE = "Past performance"
    CERTIFICATION = "Certification"
    UNKNOWN = "Unknown"


class CandidateStatus(Enum):
    UNRESEARCHED = "Unresearched"
    POTENTIAL = "Potential"
    UNDER_REVIEW = "Under review"
    QUALIFIED = "Qualified"
    NOT_QUALIFIED = "Not qualified"
    UNAVAILABLE = "Unavailable"
    DECLINED = "Declined"


class QualificationDecision(Enum):
    QUALIFIED_FOR_ESTIMATE = "Qualified for estimate"
    NEEDS_MORE_INFORMATION = "Needs more information"
    NOT_QUALIFIED = "Not qualified"
    NOT_AVAILABLE = "Not available"
    WRONG_DELIVERY_MODEL = "Wrong delivery model"
    TOO_RISKY = "Too risky"


class RiskCategory(Enum):
    SKILL_GAP = "Skill gap"
    AVAILABILITY = "Availability"
    CAPACITY = "Capacity"
    COMMUNICATION = "Communication"
    RELIABILITY = "Reliability"
    DOCUMENTATION = "Documentation"
    QUALITY = "Quality"
    SECURITY = "Security"
    CREDENTIAL_CONTROL = "Credential control"
    SOURCE_CONTROL = "Source control"
    SUBCONTRACTING = "Subcontracting"
    SUPPORT_HANDOFF = "Support handoff"
    COST = "Cost"
    VENDOR_LOCK_IN = "Vendor lock-in"
    KEY_PERSON_DEPENDENCY = "Key-person dependency"
    CUSTOMER_DEPENDENCY = "Customer dependency"
    OTHER = "Other"


class RiskSeverity(Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class SubcontractingStatus(Enum):
    NONE = "None"
    POSSIBLE = "Possible"
    EXPECTED = "Expected"
    UNKNOWN = "Unknown"


@dataclass(frozen=True)
class PartnerEvidence:
    claim: str
    evidence_type: EvidenceType
    source: str = "UNKNOWN"
    notes: str = ""


@dataclass(frozen=True)
class DeliveryNeed:
    capability: str
    importance: str
    requirement: RequirementLevel
    evidence: str
    notes: str = ""


@dataclass(frozen=True)
class DeliveryCapability:
    capability: str
    rating: FitRating
    evidence: tuple[PartnerEvidence, ...] = ()
    notes: str = ""


@dataclass(frozen=True)
class DeliveryPath:
    path_type: DeliveryPathType
    benefits: tuple[str, ...]
    risks: tuple[str, ...]
    fit: FitRating = FitRating.UNCERTAIN
    status: str = "UNDER_REVIEW"


@dataclass(frozen=True)
class DeliveryRisk:
    category: RiskCategory
    description: str
    severity: RiskSeverity
    evidence: str
    mitigation: str
    status: str = "OPEN"
    disqualifying: bool = False


@dataclass
class DeliveryCandidate:
    name: str
    path_type: DeliveryPathType
    capabilities: list[DeliveryCapability] = field(default_factory=list)
    availability: str = "UNKNOWN"
    capacity_hours_per_week: float | None = None
    communication: FitRating = FitRating.UNCERTAIN
    reliability: FitRating = FitRating.UNCERTAIN
    documentation: FitRating = FitRating.UNCERTAIN
    qa: FitRating = FitRating.UNCERTAIN
    security_access: FitRating = FitRating.UNCERTAIN
    support_handoff: FitRating = FitRating.UNCERTAIN
    cost: float | None = None
    cost_fit: FitRating = FitRating.UNCERTAIN
    subcontracting: SubcontractingStatus = SubcontractingStatus.UNKNOWN
    risks: list[DeliveryRisk] = field(default_factory=list)
    status: CandidateStatus = CandidateStatus.UNRESEARCHED

    def capability(self, name: str) -> DeliveryCapability | None:
        """Return a named capability without conflating it with a project need."""
        return next((item for item in self.capabilities if item.capability == name), None)


@dataclass(frozen=True)
class FitAssessment:
    dimension: FitDimension
    rating: FitRating
    evidence: str
    notes: str = ""


@dataclass
class DeliveryAssessment:
    opportunity: str
    solution_direction: str
    scope: str
    needs: list[DeliveryNeed]
    paths: list[DeliveryPath] = field(default_factory=list)
    candidates: list[DeliveryCandidate] = field(default_factory=list)
    assessments: dict[str, list[FitAssessment]] = field(default_factory=dict)
    decisions: dict[str, QualificationDecision] = field(default_factory=dict)
    continuity_plan: str = "UNKNOWN"
    backup_path: str = "UNKNOWN"
    technical_estimate_created: bool = False
    final_provider_selected: bool = False
    implementation_started: bool = False

    def qualify(self, candidate_name: str, decision: QualificationDecision) -> None:
        """Record an explicit gate decision; never infer it from cost or a score."""
        candidate = next((c for c in self.candidates if c.name == candidate_name), None)
        if candidate is None:
            raise ValueError(f"Unknown candidate: {candidate_name}")
        if any(r.disqualifying and r.status == "OPEN" for r in candidate.risks) and decision is QualificationDecision.QUALIFIED_FOR_ESTIMATE:
            raise ValueError("A candidate with an open disqualifying risk cannot qualify.")
        self.decisions[candidate_name] = decision
        if decision is QualificationDecision.QUALIFIED_FOR_ESTIMATE:
            candidate.status = CandidateStatus.QUALIFIED
        elif decision in {QualificationDecision.NOT_QUALIFIED, QualificationDecision.TOO_RISKY, QualificationDecision.WRONG_DELIVERY_MODEL}:
            candidate.status = CandidateStatus.NOT_QUALIFIED
        elif decision is QualificationDecision.NOT_AVAILABLE:
            candidate.status = CandidateStatus.UNAVAILABLE
        else:
            candidate.status = CandidateStatus.UNDER_REVIEW

    @property
    def qualified_for_estimate(self) -> tuple[str, ...]:
        return tuple(name for name, decision in self.decisions.items() if decision is QualificationDecision.QUALIFIED_FOR_ESTIMATE)


@dataclass(frozen=True)
class DeliveryDecision:
    estimate_request_set: tuple[str, ...]
    rationale: str
    primary_path: DeliveryPathType
    backup_strategy: str
    final_provider_selected: bool = False

    def __post_init__(self) -> None:
        if self.final_provider_selected:
            raise ValueError("Chapter 18 cannot select a final delivery provider.")
