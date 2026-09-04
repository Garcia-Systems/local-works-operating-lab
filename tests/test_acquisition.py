import pytest

from local_works.acquisition import (
    AcquisitionChannel,
    ExperimentResult,
    PublicFrictionObservation,
    channel_hypotheses,
    first_market_experiment,
)


def observation() -> PublicFrictionObservation:
    return PublicFrictionObservation(
        "Fictional public membership page",
        "The page directs freeze requests to the front desk by telephone.",
        "Requests may take staff time or inconvenience members.",
        ("Request frequency", "Reason for the policy", "Existing software capability"),
        "How are requests handled, and do they create meaningful work or complaints?",
    )


def test_experiment_keeps_cash_and_owner_time_limits_distinct() -> None:
    experiment = first_market_experiment()
    assert experiment.cash_limit != experiment.owner_time_limit
    assert "spending" in experiment.cash_limit
    assert "time" in experiment.owner_time_limit


def test_public_fact_hypothesis_and_unknowns_remain_separate() -> None:
    item = observation()
    assert item.observed_fact != item.possible_friction_hypothesis
    assert item.unknowns == ("Request frequency", "Reason for the policy", "Existing software capability")


def test_public_observation_cannot_validate_a_problem_automatically() -> None:
    with pytest.raises(ValueError, match="cannot by itself"):
        PublicFrictionObservation("page", "fact", "hypothesis", ("impact",), "question", True)


def test_discouraging_outcome_can_preserve_learning() -> None:
    result = first_market_experiment().record_result(
        ExperimentResult.DISCOURAGING,
        ("Respondents said the workflow was not meaningful.",),
    )
    assert result.has_been_run
    assert result.learning


def test_unrun_experiment_is_clearly_labeled() -> None:
    experiment = first_market_experiment()
    assert not experiment.has_been_run
    assert experiment.result.value == "NOT YET RUN IN THE REAL WORLD"


def test_channels_preserve_distinct_cash_and_time_characteristics() -> None:
    channels = {item.channel: item for item in channel_hypotheses()}
    assert set(channels) == set(AcquisitionChannel)
    assert channels[AcquisitionChannel.PERSONALIZED_OUTREACH].cash_cost == "Low"
    assert channels[AcquisitionChannel.PERSONALIZED_OUTREACH].owner_time_cost == "High"
    assert channels[AcquisitionChannel.PAID_SOCIAL].cash_cost == "Higher"
    assert channels[AcquisitionChannel.REFERRAL].primary_purpose.value == "relationship development"
