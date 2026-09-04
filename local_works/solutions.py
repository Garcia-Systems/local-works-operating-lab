"""Transparent, qualitative solution selection for Chapter 12.

This module compares responses to a qualified problem.  It deliberately does
not estimate projects, calculate ROI, select technology, or create proposals.
"""

from dataclasses import dataclass, field
from enum import Enum

from local_works.hypothesis import SolutionPath


class RelativeCost(Enum):
    VERY_LOW = "Very low"
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    VERY_HIGH = "Very high"
    UNKNOWN = "Unknown"


class RelativeComplexity(Enum):
    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"
    VERY_HIGH = "Very high"
    UNKNOWN = "Unknown"


class TimeCategory(Enum):
    DAYS = "Days"
    WEEKS = "Weeks"
    MONTHS = "Months"
    UNKNOWN = "Unknown"


class CapabilityStatus(Enum):
    YES = "Yes"
    NO = "No"
    UNKNOWN = "Unknown"


class AlternativeStatus(Enum):
    PREFERRED = "Preferred"
    VIABLE_ALTERNATIVE = "Viable alternative"
    NEEDS_VALIDATION = "Needs validation"
    NOT_RECOMMENDED = "Not recommended"
    DISQUALIFIED = "Disqualified"


class SolutionDecision(Enum):
    PREFERRED_PATH_IDENTIFIED = "Preferred path identified"
    CAPABILITY_VALIDATION_REQUIRED = "Capability validation required"
    MORE_SOLUTION_RESEARCH_REQUIRED = "More solution research required"
    LEAVE_ALONE = "Leave alone"
    DECLINE = "Decline"


class SolutionCriterion(Enum):
    PROBLEM_COVERAGE = "Problem coverage"
    SIMPLICITY = "Simplicity"
    IMPLEMENTATION_COST = "Implementation cost"
    ONGOING_COST = "Ongoing cost"
    DELIVERY_RISK = "Delivery risk"
    OPERATING_RISK = "Operating risk"
    TIME_TO_VALUE = "Time to value"
    CUSTOMER_CHANGE_BURDEN = "Customer change burden"
    SYSTEM_DEPENDENCY = "System dependency"
    MAINTAINABILITY = "Maintainability"
    REVERSIBILITY = "Reversibility"
    MEASURABILITY = "Measurability"
    POLICY_FIT = "Policy fit"
    SCALABILITY = "Scalability"
    CUSTOM_BUILD_JUSTIFICATION = "Custom-build justification"


@dataclass(frozen=True)
class SolutionRisk:
    description: str
    hard_limitation: bool = False


@dataclass(frozen=True)
class SolutionAssumption:
    assumption: str
    why_it_matters: str
    evidence: str = "UNKNOWN"
    validation_needed: str = ""
    status: str = "OPEN"


@dataclass(frozen=True)
class CapabilityQuestion:
    system: str
    capability: str
    why_it_matters: str
    current_status: CapabilityStatus = CapabilityStatus.UNKNOWN
    evidence: tuple[str, ...] = ()
    validation_method: str = ""


@dataclass
class SolutionAlternative:
    name: str
    solution_path: SolutionPath
    description: str
    problem_addressed: str
    workflow_changes: tuple[str, ...] = ()
    systems_involved: tuple[str, ...] = ()
    capabilities_required: tuple[str, ...] = ()
    customer_behavior_changes_required: tuple[str, ...] = ()
    implementation_complexity: RelativeComplexity = RelativeComplexity.UNKNOWN
    operating_complexity: RelativeComplexity = RelativeComplexity.UNKNOWN
    delivery_dependency: str = "UNKNOWN"
    estimated_cost_category: RelativeCost = RelativeCost.UNKNOWN
    estimated_time_category: TimeCategory = TimeCategory.UNKNOWN
    problem_coverage: str = "UNKNOWN"
    policy_fit: str = "UNKNOWN"
    maintainability: str = "UNKNOWN"
    vendor_dependency: str = "UNKNOWN"
    risks: tuple[SolutionRisk, ...] = ()
    assumptions: tuple[SolutionAssumption, ...] = ()
    known_limitations: tuple[str, ...] = ()
    unresolved_questions: tuple[str, ...] = ()
    evidence: tuple[str, ...] = ()
    status: AlternativeStatus = AlternativeStatus.NEEDS_VALIDATION

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.problem_addressed.strip():
            raise ValueError("An alternative requires a name and problem addressed.")
        if any(risk.hard_limitation for risk in self.risks):
            self.status = AlternativeStatus.NOT_RECOMMENDED

    @property
    def requires_custom_build(self) -> bool:
        return self.solution_path is SolutionPath.CUSTOM_BUILD


@dataclass(frozen=True)
class CustomBuildJustification:
    problem_qualified: bool
    burden_meaningful: bool
    configuration_inadequate: bool
    integration_inadequate: bool
    automation_inadequate: bool
    policy_fit: bool
    ownership_capacity: bool
    value_may_justify_risk: bool
    delivery_plausible: bool

    @property
    def supported(self) -> bool:
        return all(self.__dict__.values())

    @property
    def simpler_alternatives_considered(self) -> bool:
        return self.configuration_inadequate and self.integration_inadequate and self.automation_inadequate


@dataclass
class SolutionAssessment:
    opportunity: str
    alternatives: list[SolutionAlternative]
    capability_questions: list[CapabilityQuestion] = field(default_factory=list)
    preferred_name: str | None = None
    custom_build_justification: CustomBuildJustification | None = None
    decline: bool = False

    def __post_init__(self) -> None:
        if not self.opportunity.strip():
            raise ValueError("An assessment requires an opportunity.")
        if len(self.alternatives) < 2:
            raise ValueError("Compare at least two plausible alternatives whenever practical.")
        if len({alternative.name for alternative in self.alternatives}) != len(self.alternatives):
            raise ValueError("Alternative names must be unique.")
        if self.preferred_name and self.preferred_name not in {a.name for a in self.alternatives}:
            raise ValueError("The preferred alternative must belong to this assessment.")

    @property
    def preferred(self) -> SolutionAlternative | None:
        return next((a for a in self.alternatives if a.name == self.preferred_name), None)

    @property
    def decision(self) -> SolutionDecision:
        if self.decline:
            return SolutionDecision.DECLINE
        preferred = self.preferred
        if preferred and preferred.solution_path is SolutionPath.LEAVE_ALONE:
            return SolutionDecision.LEAVE_ALONE
        if any(q.current_status is CapabilityStatus.UNKNOWN for q in self.capability_questions):
            return SolutionDecision.CAPABILITY_VALIDATION_REQUIRED
        if preferred and preferred.status is AlternativeStatus.PREFERRED:
            return SolutionDecision.PREFERRED_PATH_IDENTIFIED
        return SolutionDecision.MORE_SOLUTION_RESEARCH_REQUIRED

    @property
    def calculates_roi(self) -> bool:
        return False

    @property
    def creates_proposal(self) -> bool:
        return False


def custom_build_may_be_preferred(justification: CustomBuildJustification | None) -> bool:
    """Require every visible gate; unsupported assumptions do not become approval."""
    return justification is not None and justification.supported
