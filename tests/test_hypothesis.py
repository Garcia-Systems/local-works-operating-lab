import pytest

from local_works.hypothesis import (
    BusinessHypothesis,
    BusinessTest,
    EvidenceType,
    SolutionPath,
    group_by_business_test,
    initial_hypotheses,
)


def test_enum_values_are_business_language() -> None:
    assert [item.value for item in BusinessTest] == [
        "Demand", "Value", "Sale", "Delivery", "Sustainability"
    ]
    assert [item.value for item in SolutionPath] == [
        "Configure", "Integrate", "Automate", "Custom Build", "Leave Alone"
    ]


def test_hypotheses_are_grouped_under_each_business_test() -> None:
    grouped = group_by_business_test(initial_hypotheses())
    assert list(grouped) == list(BusinessTest)
    assert all(len(grouped[business_test]) == 1 for business_test in BusinessTest)
    assert grouped[BusinessTest.DEMAND][0].statement.startswith("Businesses")


@pytest.mark.parametrize(
    ("evidence_type", "expected"),
    [
        (EvidenceType.HYPOTHESIS, "Hypothesis — believed, not yet observed"),
        (EvidenceType.OBSERVED, "Observed — seen in a specific instance"),
        (EvidenceType.MEASURED, "Measured — quantified using a stated method"),
    ],
)
def test_evidence_labels_explain_their_meaning(evidence_type, expected) -> None:
    item = BusinessHypothesis("A claim", BusinessTest.DEMAND, evidence_type, "Unknown")
    assert item.evidence_label == expected


def test_initial_hypotheses_cannot_be_accidentally_presented_as_proven() -> None:
    hypotheses = initial_hypotheses()
    assert all(item.evidence_type is EvidenceType.HYPOTHESIS for item in hypotheses)
    assert all(item.confidence == "Unproven" for item in hypotheses)
    assert not any(item.is_proven for item in hypotheses)
