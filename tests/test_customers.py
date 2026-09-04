from local_works.customers import (
    CustomerProfile,
    FitRating,
    Signal,
    assess_customer,
    dimension,
    fictional_profiles,
    harbor_fitness_profile,
)


def profiles_by_name() -> dict[str, CustomerProfile]:
    return {profile.business: profile for profile in fictional_profiles()}


def test_hard_disqualifiers_are_preserved_and_control_the_action() -> None:
    profile = profiles_by_name()["Shadow Metrics Cooperative"]
    result = assess_customer(profile)
    assert profile.hard_disqualifiers == (
        "The prospect requires unlawful collection of private customer data.",
    )
    assert result.rating is FitRating.DISQUALIFY
    assert "Do not pursue" in result.next_action


def test_unknowns_remain_unknown_instead_of_becoming_negative() -> None:
    result = assess_customer(harbor_fitness_profile())
    unknown_names = {item.name for item in result.unknowns}
    negative_names = {item.name for item in result.negative_signals}
    assert "Economic capacity" in unknown_names
    assert "Friction severity" in unknown_names
    assert "Buying authority accessibility" in unknown_names
    assert "Economic capacity" not in negative_names
    assert "Friction severity" not in negative_names


def test_strong_problem_signals_do_not_erase_authority_problem() -> None:
    result = assess_customer(profiles_by_name()["MetroMotion Gym — Downtown"])
    assert result.rating is FitRating.WEAK
    assert "purchasing path" in result.rationale
    assert len(result.positive_signals) >= 3


def test_small_company_size_does_not_automatically_disqualify() -> None:
    result = assess_customer(profiles_by_name()["Pocket Stage Studio"])
    assert result.rating is FitRating.PROMISING
    assert not result.profile.hard_disqualifiers
    assert any(item.name == "Economic capacity" for item in result.unknowns)


def test_same_industry_profiles_can_have_different_assessments() -> None:
    independent_gym = CustomerProfile("Owner Gym", "gym", (
        dimension("Workflow frequency", Signal.POSITIVE, "Daily."),
        dimension("Friction severity", Signal.POSITIVE, "Meaningful."),
        dimension("Buying authority accessibility", Signal.POSITIVE, "Owner reachable."),
    ))
    corporate_gym = CustomerProfile("Chain Gym", "gym", (
        dimension("Workflow frequency", Signal.POSITIVE, "Daily."),
        dimension("Friction severity", Signal.POSITIVE, "Meaningful."),
        dimension("Buying authority accessibility", Signal.NEGATIVE, "No headquarters path."),
    ))
    assert assess_customer(independent_gym).rating is FitRating.PROMISING
    assert assess_customer(corporate_gym).rating is FitRating.WEAK


def test_harbor_fitness_is_promising_but_explicitly_unvalidated() -> None:
    result = assess_customer(harbor_fitness_profile())
    assert result.rating is FitRating.PROMISING
    assert "validation" in result.rationale
    assert result.unknowns
