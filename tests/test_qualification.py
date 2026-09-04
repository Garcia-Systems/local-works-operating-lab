from local_works.economics import EconomicSignificance
from local_works.qualification import (
    BudgetStatus, DimensionAssessment, QualificationAssessment,
    QualificationDecision, QualificationDimension as D, QualificationGap,
    QualificationRating as R, QualificationRisk, RiskSeverity,
)


def assessment(**overrides: object) -> QualificationAssessment:
    ratings = {dimension: R.STRONG for dimension in D}
    ratings.update(overrides.pop("ratings", {}))  # type: ignore[arg-type]
    values = dict(
        opportunity="Fictional workflow",
        dimensions=[DimensionAssessment(dimension, rating, ("sourced evidence",))
                    for dimension, rating in ratings.items()],
        economic_significance=EconomicSignificance.MEANINGFUL_BURDEN_ESTABLISHED,
        budget_status=BudgetStatus.PLAUSIBLE_CAPACITY,
        rationale="The explicit evidence and gates support this result.",
    )
    values.update(overrides)
    return QualificationAssessment(**values)  # type: ignore[arg-type]


def test_dimensions_preserve_independent_ratings() -> None:
    item = assessment(ratings={D.URGENCY: R.UNCERTAIN, D.AUTHORITY: R.ACCEPTABLE})
    assert item.rating_for(D.URGENCY) is R.UNCERTAIN
    assert item.rating_for(D.AUTHORITY) is R.ACCEPTABLE


def test_unknown_budget_is_not_insufficient_and_can_advance() -> None:
    item = assessment(budget_status=BudgetStatus.UNKNOWN,
                      gaps=[QualificationGap("available budget", "Ask about budget cycle")])
    assert item.budget_status is BudgetStatus.UNKNOWN
    assert item.decision is QualificationDecision.ADVANCE_TO_SOLUTION_DESIGN


def test_meaningful_economics_do_not_override_no_priority() -> None:
    item = assessment(ratings={D.CUSTOMER_PRIORITY: R.WEAK})
    assert item.decision is QualificationDecision.NURTURE


def test_strong_problem_does_not_override_hard_disqualifier() -> None:
    item = assessment(risks=[QualificationRisk("Conceal work from corporate", RiskSeverity.DISQUALIFIER)])
    assert item.rating_for(D.PROBLEM_UNDERSTANDING) is R.STRONG
    assert item.decision is QualificationDecision.DISQUALIFY


def test_authority_does_not_compensate_for_trivial_economics() -> None:
    item = assessment(economic_significance=EconomicSignificance.ECONOMICALLY_TRIVIAL)
    assert item.rating_for(D.AUTHORITY) is R.STRONG
    assert item.decision is QualificationDecision.DECLINE


def test_wrong_fit_can_produce_referral() -> None:
    assert assessment(ratings={D.LOCAL_WORKS_FIT: R.WEAK}).decision is QualificationDecision.REFER_ELSEWHERE


def test_no_priority_can_produce_nurture() -> None:
    assert assessment(ratings={D.CUSTOMER_PRIORITY: R.WEAK}).decision is QualificationDecision.NURTURE


def test_hard_disqualifier_produces_disqualification() -> None:
    item = assessment(risks=[QualificationRisk("Illegal outcome", RiskSeverity.DISQUALIFIER)])
    assert item.hard_disqualifiers
    assert item.decision is QualificationDecision.DISQUALIFY


def test_presales_effort_and_rationale_are_preserved() -> None:
    item = assessment(expected_presales_hours=3.5, rationale="Proceed, while testing named unknowns.")
    assert item.expected_presales_hours == 3.5
    assert item.rationale == "Proceed, while testing named unknowns."


def test_qualification_does_not_select_approve_or_sell() -> None:
    item = assessment()
    assert item.selects_solution is False
    assert item.creates_proposal is False
    assert item.guarantees_sale is False


def test_unclear_authority_requires_more_evidence() -> None:
    item = assessment(ratings={D.AUTHORITY: R.UNCERTAIN})
    assert item.decision is QualificationDecision.MORE_EVIDENCE_REQUIRED
