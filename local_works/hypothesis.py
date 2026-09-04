"""The minimum model needed to state and inspect the Chapter 0 hypotheses."""

from collections.abc import Iterable
from dataclasses import dataclass
from enum import Enum


class BusinessTest(Enum):
    DEMAND = "Demand"
    VALUE = "Value"
    SALE = "Sale"
    DELIVERY = "Delivery"
    SUSTAINABILITY = "Sustainability"


class SolutionPath(Enum):
    CONFIGURE = "Configure"
    INTEGRATE = "Integrate"
    AUTOMATE = "Automate"
    CUSTOM_BUILD = "Custom Build"
    LEAVE_ALONE = "Leave Alone"


class EvidenceType(Enum):
    HYPOTHESIS = "Hypothesis — believed, not yet observed"
    OBSERVED = "Observed — seen in a specific instance"
    MEASURED = "Measured — quantified using a stated method"


@dataclass(frozen=True)
class BusinessHypothesis:
    statement: str
    business_test: BusinessTest
    evidence_type: EvidenceType
    confidence: str
    notes: str = ""

    @classmethod
    def initial(
        cls, statement: str, business_test: BusinessTest, notes: str = ""
    ) -> "BusinessHypothesis":
        """Create a claim that cannot accidentally be labeled observed or measured."""
        return cls(
            statement=statement,
            business_test=business_test,
            evidence_type=EvidenceType.HYPOTHESIS,
            confidence="Unproven",
            notes=notes,
        )

    @property
    def evidence_label(self) -> str:
        return self.evidence_type.value

    @property
    def is_proven(self) -> bool:
        """Avoid treating any evidence label as proof of a general business claim."""
        return False


def initial_hypotheses() -> tuple[BusinessHypothesis, ...]:
    return (
        BusinessHypothesis.initial(
            "Businesses experience meaningful digital workflow friction.",
            BusinessTest.DEMAND,
        ),
        BusinessHypothesis.initial(
            "A Digital Friction Audit can create qualified sales conversations.",
            BusinessTest.VALUE,
        ),
        BusinessHypothesis.initial(
            "Customers will pay Local Works enough for viable margins.",
            BusinessTest.SALE,
        ),
        BusinessHypothesis.initial(
            "Delivery partners can implement work reliably while Local Works preserves the customer relationship.",
            BusinessTest.DELIVERY,
        ),
        BusinessHypothesis.initial(
            "Recurring support can contribute to sustainable owner income.",
            BusinessTest.SUSTAINABILITY,
        ),
    )


def group_by_business_test(
    hypotheses: Iterable[BusinessHypothesis],
) -> dict[BusinessTest, list[BusinessHypothesis]]:
    grouped = {business_test: [] for business_test in BusinessTest}
    for hypothesis in hypotheses:
        grouped[hypothesis.business_test].append(hypothesis)
    return grouped
