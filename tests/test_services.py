from local_works.services import (
    SERVICE_DEFINITIONS,
    ServiceStage,
    chapter_examples,
    service_definition,
)


def test_all_expected_service_stages_exist() -> None:
    assert list(ServiceStage) == [
        ServiceStage.AUDIT,
        ServiceStage.DISCOVERY,
        ServiceStage.SOLUTION_DESIGN,
        ServiceStage.IMPLEMENTATION,
        ServiceStage.SUPPORT,
        ServiceStage.CONTINUOUS_IMPROVEMENT,
    ]
    assert set(SERVICE_DEFINITIONS) == set(ServiceStage)


def test_audit_does_not_require_implementation() -> None:
    audit = service_definition(ServiceStage.AUDIT)
    assert not audit.implementation_required
    assert "simple configuration or process fix" in audit.exit_conditions


def test_discovery_does_not_guarantee_a_project() -> None:
    discovery = service_definition(ServiceStage.DISCOVERY)
    assert not discovery.project_must_result
    assert "no project" in discovery.exit_conditions


def test_implementation_is_distinguishable_from_solution_design() -> None:
    design = service_definition(ServiceStage.SOLUTION_DESIGN)
    implementation = service_definition(ServiceStage.IMPLEMENTATION)
    assert not design.implementation_required
    assert implementation.implementation_required
    assert design.primary_purpose != implementation.primary_purpose


def test_support_is_distinguishable_from_continuous_improvement() -> None:
    support = service_definition(ServiceStage.SUPPORT)
    improvement = service_definition(ServiceStage.CONTINUOUS_IMPROVEMENT)
    assert support.outputs != improvement.outputs
    assert "new project identified" in support.exit_conditions
    assert "value assessment" in improvement.outputs


def test_every_service_definition_has_useful_outputs_and_exits() -> None:
    for stage in ServiceStage:
        definition = service_definition(stage)
        assert definition.stage is stage
        assert definition.inputs
        assert definition.outputs
        assert definition.exit_conditions


def test_examples_are_explicit_and_never_select_a_technical_solution() -> None:
    examples = chapter_examples()
    assert len(examples) >= 6
    assert all(not example.technical_solution_selected for example in examples)
    assert any("configuration fix" in example.reason for example in examples)
    assert any("checklist" in example.reason for example in examples)
