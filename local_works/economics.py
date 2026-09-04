"""Transparent current-problem economics for Chapter 10.

This module values supported current-state burden.  It intentionally does not
estimate a solution's recoverable value, ROI, price, or recommendation.
"""

from dataclasses import dataclass, field
from enum import Enum


class EvidenceStatus(Enum):
    MEASURED = "Measured"
    ESTIMATED = "Estimated"
    HYPOTHETICAL = "Hypothetical"
    UNKNOWN = "Unknown"


class FrequencyUnit(Enum):
    PER_DAY = "Per day"
    PER_WEEK = "Per week"
    PER_MONTH = "Per month"
    PER_YEAR = "Per year"


class BurdenCategory(Enum):
    LABOR = "Labor"
    REWORK = "Rework"
    ERROR = "Error"
    DELAY = "Delay"
    LOST_REVENUE = "Lost revenue"
    LOST_RETENTION = "Lost retention"
    REFUND_OR_CREDIT = "Refund or credit"
    THIRD_PARTY_COST = "Third-party cost"
    MANAGER_ESCALATION = "Manager escalation"
    OTHER = "Other"


class Scenario(Enum):
    LOW = "Low"
    BASELINE = "Baseline"
    HIGH = "High"


class EconomicSignificance(Enum):
    ECONOMICALLY_TRIVIAL = "Economically trivial"
    POTENTIALLY_MEANINGFUL = "Potentially meaningful"
    MORE_EVIDENCE_REQUIRED = "More evidence required"
    MEANINGFUL_BURDEN_ESTABLISHED = "Meaningful burden established"


@dataclass(frozen=True)
class EconomicInput:
    name: str
    value: float | None
    unit: str
    evidence: EvidenceStatus
    source: str
    notes: str = ""

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.source.strip():
            raise ValueError("Economic inputs require a name and source.")
        if self.value is None and self.evidence is not EvidenceStatus.UNKNOWN:
            raise ValueError("A missing value must remain UNKNOWN.")
        if self.value is not None and self.value < 0:
            raise ValueError("Economic inputs cannot be negative.")

    @property
    def is_known(self) -> bool:
        return self.value is not None


@dataclass(frozen=True)
class EconomicEstimate:
    annual_amount: float | None
    evidence: EvidenceStatus
    inputs: tuple[EconomicInput, ...]
    calculation: str

    @property
    def is_known(self) -> bool:
        return self.annual_amount is not None


def inherited_evidence(inputs: tuple[EconomicInput, ...]) -> EvidenceStatus:
    """Return the least certain input status; arithmetic cannot improve evidence."""
    if any(item.value is None or item.evidence is EvidenceStatus.UNKNOWN for item in inputs):
        return EvidenceStatus.UNKNOWN
    if any(item.evidence in (EvidenceStatus.HYPOTHETICAL, EvidenceStatus.ESTIMATED)
           for item in inputs):
        # A computed amount is an estimate; its inputs retain which assumptions
        # were merely hypothetical.
        return EvidenceStatus.ESTIMATED
    return EvidenceStatus.MEASURED


@dataclass(frozen=True)
class Frequency:
    amount: EconomicInput
    unit: FrequencyUnit
    operating_periods_per_year: EconomicInput | None = None

    def annualize(self) -> EconomicEstimate:
        default_periods = {
            FrequencyUnit.PER_DAY: 365.0,
            FrequencyUnit.PER_WEEK: 52.0,
            FrequencyUnit.PER_MONTH: 12.0,
            FrequencyUnit.PER_YEAR: 1.0,
        }[self.unit]
        periods = self.operating_periods_per_year or EconomicInput(
            "calendar periods/year", default_periods, "periods/year",
            EvidenceStatus.HYPOTHETICAL, "default calendar assumption",
            "Replace with explicit operating periods when known.",
        )
        inputs = (self.amount,) if self.unit is FrequencyUnit.PER_YEAR else (self.amount, periods)
        if any(item.value is None for item in inputs):
            return EconomicEstimate(None, EvidenceStatus.UNKNOWN, inputs, "Annual volume is UNKNOWN.")
        multiplier = 1.0 if self.unit is FrequencyUnit.PER_YEAR else periods.value
        assert self.amount.value is not None and multiplier is not None
        return EconomicEstimate(
            self.amount.value * multiplier, inherited_evidence(inputs), inputs,
            f"{self.amount.value:g} {self.unit.name} × {multiplier:g} operating periods/year",
        )


@dataclass(frozen=True)
class LaborRole:
    role: str
    minutes_per_event: EconomicInput
    loaded_cost_per_hour: EconomicInput
    involvement_rate: EconomicInput = EconomicInput(
        "involvement rate", 1.0, "proportion", EvidenceStatus.MEASURED,
        "role applies to every modeled event",
    )

    def annual_burden(self, frequency: Frequency) -> EconomicEstimate:
        annual = frequency.annualize()
        inputs = annual.inputs + (self.minutes_per_event, self.loaded_cost_per_hour,
                                  self.involvement_rate)
        if annual.annual_amount is None or any(item.value is None for item in inputs):
            return EconomicEstimate(None, EvidenceStatus.UNKNOWN, inputs,
                                    f"{self.role} labor is UNKNOWN because an input is unknown.")
        minutes = self.minutes_per_event.value
        rate = self.loaded_cost_per_hour.value
        involvement = self.involvement_rate.value
        assert minutes is not None and rate is not None and involvement is not None
        amount = annual.annual_amount * involvement * minutes / 60 * rate
        return EconomicEstimate(amount, inherited_evidence(inputs), inputs,
            f"{annual.annual_amount:g} events × {involvement:g} involvement × "
            f"{minutes:g} minutes ÷ 60 × ${rate:g}/hour")


def rework_burden(frequency: Frequency, error_rate: EconomicInput,
                  correction_minutes: EconomicInput,
                  loaded_cost_per_hour: EconomicInput) -> EconomicEstimate:
    annual = frequency.annualize()
    inputs = annual.inputs + (error_rate, correction_minutes, loaded_cost_per_hour)
    if annual.annual_amount is None or any(item.value is None for item in inputs):
        return EconomicEstimate(None, EvidenceStatus.UNKNOWN, inputs,
                                "Expected annual rework burden is UNKNOWN.")
    assert error_rate.value is not None and correction_minutes.value is not None
    assert loaded_cost_per_hour.value is not None
    amount = annual.annual_amount * error_rate.value * correction_minutes.value / 60 * loaded_cost_per_hour.value
    return EconomicEstimate(amount, inherited_evidence(inputs), inputs,
        f"{annual.annual_amount:g} events × {error_rate.value:g} correction rate × "
        f"{correction_minutes.value:g} minutes ÷ 60 × ${loaded_cost_per_hour.value:g}/hour")


@dataclass(frozen=True)
class BurdenComponent:
    component_id: str
    category: BurdenCategory
    description: str
    estimate: EconomicEstimate
    included: bool = True
    overlap_group: str | None = None
    includes: str = ""

    def __post_init__(self) -> None:
        if not self.component_id.strip() or not self.description.strip():
            raise ValueError("A burden component needs an id and description.")
        if self.included and self.estimate.is_known and not self.includes.strip():
            raise ValueError("Included monetary components must explain what they include.")


@dataclass
class ProblemEconomics:
    opportunity: str
    components: list[BurdenComponent] = field(default_factory=list)
    non_monetized_burdens: list[str] = field(default_factory=list)
    unknown_potential_burdens: list[str] = field(default_factory=list)

    def add_component(self, component: BurdenComponent) -> None:
        if any(item.component_id == component.component_id for item in self.components):
            raise ValueError("Component ids must be unique.")
        if component.included and component.overlap_group and any(
            item.included and item.overlap_group == component.overlap_group
            for item in self.components
        ):
            raise ValueError("Included components cannot share an overlap group (double count).")
        self.components.append(component)

    @property
    def annual_direct_burden(self) -> EconomicEstimate:
        included = [item for item in self.components if item.included]
        inputs = tuple(inp for item in included for inp in item.estimate.inputs)
        if any(not item.estimate.is_known for item in included):
            return EconomicEstimate(None, EvidenceStatus.UNKNOWN, inputs,
                                    "Included burden contains an UNKNOWN component.")
        total = sum(item.estimate.annual_amount or 0 for item in included)
        evidence = inherited_evidence(inputs) if inputs else EvidenceStatus.UNKNOWN
        return EconomicEstimate(total, evidence, inputs,
                                "Sum of included, non-overlapping annual components.")

    @property
    def recoverable_value(self) -> None:
        """Current burden is not a claim about what a future solution can recover."""
        return None


def scenario_labor_burdens(frequencies: dict[Scenario, Frequency],
                           roles: dict[Scenario, tuple[LaborRole, ...]]) -> dict[Scenario, float | None]:
    results: dict[Scenario, float | None] = {}
    for scenario in Scenario:
        estimates = [role.annual_burden(frequencies[scenario]) for role in roles[scenario]]
        results[scenario] = None if any(not estimate.is_known for estimate in estimates) else sum(
            estimate.annual_amount or 0 for estimate in estimates
        )
    known = [results[item] for item in Scenario]
    if all(value is not None for value in known) and not (known[0] <= known[1] <= known[2]):  # type: ignore[operator]
        raise ValueError("LOW, BASELINE, and HIGH scenario burdens must be ordered.")
    return results


def significance(total: EconomicEstimate, *, materiality_threshold: float,
                 evidence_complete: bool = True) -> EconomicSignificance:
    """Triage current burden only; never recommend or approve a project."""
    if not total.is_known or not evidence_complete:
        return EconomicSignificance.MORE_EVIDENCE_REQUIRED
    assert total.annual_amount is not None
    if total.annual_amount < materiality_threshold:
        return EconomicSignificance.ECONOMICALLY_TRIVIAL
    if total.evidence is EvidenceStatus.MEASURED:
        return EconomicSignificance.MEANINGFUL_BURDEN_ESTABLISHED
    return EconomicSignificance.POTENTIALLY_MEANINGFUL
