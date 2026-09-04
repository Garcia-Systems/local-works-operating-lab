from local_works.hypothesis import SolutionPath
from local_works.solutions import (
    AlternativeStatus, CapabilityQuestion, CapabilityStatus,
    CustomBuildJustification, RelativeCost, SolutionAlternative,
    SolutionAssessment, SolutionAssumption, SolutionDecision, SolutionRisk,
    custom_build_may_be_preferred,
)


def alternative(name: str, path: SolutionPath, **kwargs: object) -> SolutionAlternative:
    return SolutionAlternative(name, path, "A bounded response", "Validated workflow", **kwargs)


def test_alternatives_preserve_distinct_paths_and_can_share_opportunity() -> None:
    configure = alternative("Configure", SolutionPath.CONFIGURE)
    integrate = alternative("Integrate", SolutionPath.INTEGRATE)
    automate = alternative("Automate", SolutionPath.AUTOMATE)
    assessment = SolutionAssessment("One opportunity", [configure, integrate, automate])
    assert configure.solution_path is SolutionPath.CONFIGURE
    assert [item.solution_path for item in assessment.alternatives] == [
        SolutionPath.CONFIGURE, SolutionPath.INTEGRATE, SolutionPath.AUTOMATE]
    assert not configure.requires_custom_build


def test_unknown_capability_stays_unknown_and_blocks_final_decision() -> None:
    question = CapabilityQuestion("Current platform", "Conditional freezes", "Could avoid code")
    assessment = SolutionAssessment(
        "Freeze workflow",
        [alternative("Configure", SolutionPath.CONFIGURE), alternative("Leave", SolutionPath.LEAVE_ALONE)],
        [question],
    )
    assert question.current_status is CapabilityStatus.UNKNOWN
    assert assessment.decision is SolutionDecision.CAPABILITY_VALIDATION_REQUIRED


def test_custom_build_is_representable_but_not_automatically_preferred() -> None:
    custom = alternative("Portal", SolutionPath.CUSTOM_BUILD)
    assessment = SolutionAssessment(
        "Workflow", [custom, alternative("Configure", SolutionPath.CONFIGURE)])
    assert custom.requires_custom_build
    assert custom.status is AlternativeStatus.NEEDS_VALIDATION
    assert assessment.preferred is None


def test_leave_alone_can_be_preferred() -> None:
    leave = alternative("Leave", SolutionPath.LEAVE_ALONE, status=AlternativeStatus.PREFERRED)
    assessment = SolutionAssessment(
        "Twice yearly task", [leave, alternative("Automate", SolutionPath.AUTOMATE)],
        preferred_name="Leave",
    )
    assert assessment.decision is SolutionDecision.LEAVE_ALONE


def test_hard_limitation_makes_alternative_not_recommended() -> None:
    item = alternative(
        "Integration", SolutionPath.INTEGRATE,
        risks=(SolutionRisk("Required API is unavailable", hard_limitation=True),),
        status=AlternativeStatus.VIABLE_ALTERNATIVE,
    )
    assert item.status is AlternativeStatus.NOT_RECOMMENDED


def test_assumptions_are_preserved() -> None:
    assumption = SolutionAssumption("API may exist", "Controls feasibility")
    item = alternative("Integration", SolutionPath.INTEGRATE, assumptions=(assumption,))
    assert item.assumptions == (assumption,)
    assert item.assumptions[0].evidence == "UNKNOWN"


def test_low_cost_does_not_make_inadequate_option_preferred() -> None:
    cheap = alternative(
        "Cheap configuration", SolutionPath.CONFIGURE,
        estimated_cost_category=RelativeCost.VERY_LOW,
        problem_coverage="10% / inadequate",
        status=AlternativeStatus.NOT_RECOMMENDED,
    )
    useful = alternative("Useful integration", SolutionPath.INTEGRATE, problem_coverage="85%")
    assessment = SolutionAssessment("Workflow", [cheap, useful])
    assert assessment.preferred is None
    assert assessment.decision is SolutionDecision.MORE_SOLUTION_RESEARCH_REQUIRED


def test_custom_build_gate_requires_simpler_paths_and_every_other_gate() -> None:
    unsupported = CustomBuildJustification(True, True, True, False, True, True, True, True, True)
    supported = CustomBuildJustification(True, True, True, True, True, True, True, True, True)
    assert not unsupported.simpler_alternatives_considered
    assert not custom_build_may_be_preferred(unsupported)
    assert supported.simpler_alternatives_considered
    assert custom_build_may_be_preferred(supported)


def test_solution_selection_neither_calculates_roi_nor_creates_proposal() -> None:
    assessment = SolutionAssessment(
        "Workflow", [alternative("Configure", SolutionPath.CONFIGURE), alternative("Leave", SolutionPath.LEAVE_ALONE)])
    assert not assessment.calculates_roi
    assert not assessment.creates_proposal
