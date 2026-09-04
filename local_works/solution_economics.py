"""Evidence-preserving solution economics for Chapter 13.

The model deliberately stops before scope, price, proposal, or approval.  It
compares the customer's supported future costs with value a solution may
actually realize from an existing burden.
"""

from dataclasses import dataclass, field
from enum import Enum

from local_works.economics import BurdenComponent, EvidenceStatus, inherited_evidence


class ValueCategory(Enum):
    LABOR_CAPACITY = "Labor capacity"
    REWORK_REDUCTION = "Rework reduction"
    ERROR_REDUCTION = "Error reduction"
    FEE_REDUCTION = "Fee reduction"
    REFUND_REDUCTION = "Refund reduction"
    REVENUE_RECOVERY = "Revenue recovery"
    RETENTION_IMPROVEMENT = "Retention improvement"
    DELAY_REDUCTION = "Delay reduction"
    THIRD_PARTY_COST_REDUCTION = "Third-party cost reduction"
    OTHER = "Other"


class BenefitType(Enum):
    CASH_SAVINGS = "Cash savings"
    FREED_CAPACITY = "Freed capacity"
    REVENUE_VALUE = "Revenue value"
    RISK_REDUCTION = "Risk reduction"
    NON_MONETIZED_BENEFIT = "Non-monetized benefit"


class CostCategory(Enum):
    LOCAL_WORKS_SERVICES = "Local Works services"
    DELIVERY_PARTNER = "Delivery partner"
    SOFTWARE_SETUP = "Software setup"
    INTEGRATION = "Integration"
    CUSTOM_DEVELOPMENT = "Custom development"
    DATA_MIGRATION = "Data migration"
    TRAINING = "Training"
    TESTING = "Testing"
    CUSTOMER_INTERNAL_TIME = "Customer internal time"
    SUBSCRIPTION = "Subscription"
    SUPPORT_MAINTENANCE = "Support and maintenance"
    OTHER = "Other"


class ScenarioLevel(Enum):
    LOW = "Low"
    BASELINE = "Baseline"
    HIGH = "High"


class EconomicDecision(Enum):
    ECONOMICALLY_ATTRACTIVE = "Economically attractive"
    ECONOMICALLY_PLAUSIBLE = "Economically plausible"
    MARGINAL = "Marginal"
    MORE_EVIDENCE_REQUIRED = "More evidence required"
    ECONOMICALLY_UNATTRACTIVE = "Economically unattractive"
    LEAVE_ALONE = "Leave alone"


@dataclass(frozen=True)
class EconomicAssumption:
    name: str
    value: float | None
    evidence: EvidenceStatus
    source: str

    def __post_init__(self) -> None:
        if not self.name.strip() or not self.source.strip():
            raise ValueError("An assumption requires a name and source.")
        if self.value is None and self.evidence is not EvidenceStatus.UNKNOWN:
            raise ValueError("A missing assumption must remain UNKNOWN.")


@dataclass(frozen=True)
class RecoverableValueComponent:
    burden: BurdenComponent
    category: ValueCategory
    benefit_type: BenefitType
    recoverable_fraction: EconomicAssumption
    adoption_rate: EconomicAssumption
    realization_factor: EconomicAssumption
    remaining_work: str
    separately_justified_value: bool = False
    supported: bool = True
    freed_hours: float | None = None

    def __post_init__(self) -> None:
        for assumption in (self.recoverable_fraction, self.adoption_rate, self.realization_factor):
            if assumption.value is not None and not 0 <= assumption.value <= 1:
                raise ValueError("Fractions, adoption, and realization must be between 0 and 1.")
        if not self.remaining_work.strip():
            raise ValueError("Remaining necessary work must be explicit.")
        if self.category in (ValueCategory.REVENUE_RECOVERY, ValueCategory.RETENTION_IMPROVEMENT) and not self.supported:
            return
        if self.separately_justified_value:
            raise ValueError("Value above current burden needs a separate value model, not a burden fraction.")

    @property
    def annual_value(self) -> float | None:
        if not self.supported or self.benefit_type is BenefitType.NON_MONETIZED_BENEFIT:
            return None
        values = (self.burden.estimate.annual_amount, self.recoverable_fraction.value,
                  self.adoption_rate.value, self.realization_factor.value)
        if any(value is None for value in values):
            return None
        burden, recoverable, adoption, realization = values
        assert burden is not None and recoverable is not None and adoption is not None and realization is not None
        return burden * recoverable * adoption * realization

    @property
    def evidence(self) -> EvidenceStatus:
        assumptions = (self.recoverable_fraction, self.adoption_rate, self.realization_factor)
        if self.annual_value is None:
            return EvidenceStatus.UNKNOWN
        # Preserve hypothetical provenance prominently rather than upgrading it.
        if any(item.evidence is EvidenceStatus.HYPOTHETICAL for item in assumptions):
            return EvidenceStatus.HYPOTHETICAL
        return inherited_evidence(self.burden.estimate.inputs)

    @property
    def cash_savings(self) -> float | None:
        return self.annual_value if self.benefit_type is BenefitType.CASH_SAVINGS else None


@dataclass(frozen=True)
class SolutionCost:
    name: str
    category: CostCategory
    amount: float | None
    evidence: EvidenceStatus
    source: str
    recurring: bool = False
    monetized: bool = True

    def __post_init__(self) -> None:
        if self.amount is None and self.evidence is not EvidenceStatus.UNKNOWN:
            raise ValueError("A missing cost must remain UNKNOWN.")
        if self.amount is not None and self.amount < 0:
            raise ValueError("Costs cannot be negative.")


@dataclass
class SolutionEconomics:
    alternative: str
    current_annual_burden: float | None
    components: list[RecoverableValueComponent]
    costs: list[SolutionCost]
    annual_new_operating_burden: float | None = 0.0
    other_first_year_cost: float | None = 0.0
    useful_life_years: int = 3
    decision: EconomicDecision = EconomicDecision.MORE_EVIDENCE_REQUIRED
    major_unknowns: list[str] = field(default_factory=list)

    @staticmethod
    def _sum_known(values: list[float | None]) -> float | None:
        return None if any(value is None for value in values) else sum(value or 0 for value in values)

    @property
    def annual_gross_value(self) -> float | None:
        return self._sum_known([component.annual_value for component in self.components if component.supported])

    @property
    def implementation_cost(self) -> float | None:
        return self._sum_known([cost.amount for cost in self.costs if not cost.recurring and cost.monetized])

    @property
    def annual_recurring_cost(self) -> float | None:
        return self._sum_known([cost.amount for cost in self.costs if cost.recurring and cost.monetized])

    @property
    def first_year_cost(self) -> float | None:
        return self._sum_known([self.implementation_cost, self.annual_recurring_cost, self.other_first_year_cost])

    @property
    def annual_net_benefit(self) -> float | None:
        values = [self.annual_gross_value, self.annual_recurring_cost, self.annual_new_operating_burden]
        if any(value is None for value in values):
            return None
        return values[0] - values[1] - values[2]  # type: ignore[operator]

    @property
    def payback_months(self) -> float | None:
        if self.implementation_cost is None or self.annual_net_benefit is None or self.annual_net_benefit <= 0:
            return None
        return self.implementation_cost / self.annual_net_benefit * 12

    @property
    def first_year_roi(self) -> float | None:
        if self.first_year_cost in (None, 0) or self.annual_gross_value is None:
            return None
        assert self.first_year_cost is not None
        return (self.annual_gross_value - self.first_year_cost) / self.first_year_cost

    def cumulative_value(self, years: int) -> float | None:
        if years < 1 or years > self.useful_life_years or self.implementation_cost is None or self.annual_net_benefit is None:
            return None
        return self.annual_net_benefit * years - self.implementation_cost - (self.other_first_year_cost or 0)

    @property
    def creates_proposal(self) -> bool:
        return False

    @property
    def approves_project(self) -> bool:
        return False


@dataclass(frozen=True)
class EconomicScenario:
    level: ScenarioLevel
    economics: SolutionEconomics


@dataclass(frozen=True)
class IncrementalComparison:
    simpler: str
    more_complex: str
    additional_implementation_cost: float | None
    additional_annual_net_benefit: float | None


def compare_incrementally(simpler: SolutionEconomics, more_complex: SolutionEconomics) -> IncrementalComparison:
    implementation = None if simpler.implementation_cost is None or more_complex.implementation_cost is None else more_complex.implementation_cost - simpler.implementation_cost
    benefit = None if simpler.annual_net_benefit is None or more_complex.annual_net_benefit is None else more_complex.annual_net_benefit - simpler.annual_net_benefit
    return IncrementalComparison(simpler.alternative, more_complex.alternative, implementation, benefit)


def validate_scenarios(scenarios: list[EconomicScenario]) -> None:
    if [item.level for item in scenarios] != list(ScenarioLevel):
        raise ValueError("Scenarios must be LOW, BASELINE, HIGH.")
    values = [item.economics.annual_net_benefit for item in scenarios]
    if any(value is None for value in values) or not values[0] <= values[1] <= values[2]:  # type: ignore[operator]
        raise ValueError("Scenario net benefits must be known and ordered LOW to HIGH.")
