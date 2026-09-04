"""Meaningful boundary and readiness checks for Chapter 14."""
import pytest

from local_works.scope import (AcceptanceCriterion, AssumptionStatus, CustomerResponsibility,
    DeliveryResponsibility, EstimateReadiness, LocalWorksResponsibility, Priority, ProjectScope,
    RequestDisposition, ScopeAssumption, ScopeBoundary, ScopeDependency, ScopeExclusion,
    ScopeItem, ScopedSystem, SystemClassification)


def scope(**changes: object) -> ProjectScope:
    values: dict[str, object] = dict(
        business="Example", opportunity="Reduce duplicate entry",
        business_outcome="Designed to reduce duplicate data entry",
        problem_statement="Staff enter completed-job data twice",
        solution_direction="Copy completed-job details into an invoice draft",
        boundary=ScopeBoundary("Job is marked complete", "Invoice draft is created"),
        included=[ScopeItem("Completed-job to invoice-draft workflow")],
        excluded=[ScopeExclusion("Replace accounting platform")],
        actors=["Dispatcher", "Bookkeeper"],
        systems=[ScopedSystem("Scheduling", SystemClassification.IN_SCOPE),
                 ScopedSystem("Accounting", SystemClassification.DEPENDENCY_ONLY)],
        functional_requirements=[ScopeItem("Copy required job details", Priority.MUST),
                                 ScopeItem("Notify bookkeeper", Priority.SHOULD),
                                 ScopeItem("Show copy history", Priority.COULD)],
        assumptions=[], dependencies=[],
        customer_responsibilities=[CustomerResponsibility("Provide test access")],
        local_works_responsibilities=[LocalWorksResponsibility("Coordinate requirements")],
        delivery_responsibilities=[DeliveryResponsibility("Configure integration")],
        acceptance_criteria=[AcceptanceCriterion("a completed job", "copy runs", "an invoice draft contains required fields")],
        business_success_metrics=["Duplicate-entry time decreases"])
    values.update(changes)
    return ProjectScope(**values)  # type: ignore[arg-type]


def test_scope_preserves_outcome_workflow_actors_and_system_classification() -> None:
    item = scope()
    assert item.business_outcome == "Designed to reduce duplicate data entry"
    assert item.boundary.trigger == "Job is marked complete"
    assert item.boundary.end_condition == "Invoice draft is created"
    assert item.actors == ["Dispatcher", "Bookkeeper"]
    assert item.systems[1].classification is SystemClassification.DEPENDENCY_ONLY


def test_included_and_excluded_are_distinct_and_overlap_is_rejected() -> None:
    item = scope()
    assert item.included[0].statement != item.excluded[0].statement
    with pytest.raises(ValueError, match="both included and excluded"):
        scope(excluded=[ScopeExclusion("Completed-job to invoice-draft workflow")])


def test_priorities_and_requirement_design_are_preserved() -> None:
    item = scope()
    assert [x.statement for x in item.requirements_by_priority[Priority.MUST]] == ["Copy required job details"]
    assert item.requirements_by_priority[Priority.SHOULD]
    assert item.requirements_by_priority[Priority.COULD]
    requirement = ScopeItem("Staff can approve exceptions", Priority.MUST, "Send an automation-platform task")
    assert requirement.statement != requirement.design_decision


def test_assumption_dependency_and_three_party_roles_remain_distinct() -> None:
    assumption = ScopeAssumption("Plan includes API", "Enables integration", AssumptionStatus.UNCONFIRMED, "Validate another path")
    dependency = ScopeDependency("API access", "Vendor", AssumptionStatus.UNCONFIRMED, "Integration unavailable")
    item = scope(assumptions=[assumption], dependencies=[dependency])
    assert item.assumptions[0].status is AssumptionStatus.UNCONFIRMED
    assert item.dependencies[0].owner == "Vendor"
    assert type(item.customer_responsibilities[0]) is CustomerResponsibility
    assert type(item.local_works_responsibilities[0]) is LocalWorksResponsibility
    assert type(item.delivery_responsibilities[0]) is DeliveryResponsibility


def test_acceptance_and_business_metric_are_distinct() -> None:
    item = scope()
    assert item.acceptance_criteria[0].then.startswith("an invoice draft")
    assert item.business_success_metrics == ["Duplicate-entry time decreases"]


def test_unconfirmed_critical_business_assumption_blocks_ready_gate() -> None:
    item = scope(assumptions=[ScopeAssumption("Rules are complete", "Defines acceptance", AssumptionStatus.UNCONFIRMED, "Clarify rules", critical=True)])
    assert item.estimate_readiness is EstimateReadiness.NEEDS_CUSTOMER_CLARIFICATION


def test_technical_unknown_requires_validation() -> None:
    item = scope(dependencies=[ScopeDependency("Vendor API", "Vendor", AssumptionStatus.UNCONFIRMED, "Change direction", technical=True, critical=True)])
    assert item.estimate_readiness is EstimateReadiness.NEEDS_TECHNICAL_VALIDATION


def test_broad_scope_requires_reduction_and_vague_scope_needs_clarification() -> None:
    assert scope(overloaded=True).estimate_readiness is EstimateReadiness.NEEDS_SCOPE_REDUCTION
    assert scope(vague=True).estimate_readiness is EstimateReadiness.NEEDS_CUSTOMER_CLARIFICATION


def test_deferred_request_does_not_change_included_scope() -> None:
    item = scope()
    before = list(item.included)
    request = item.classify_request("Add cancellations", RequestDisposition.DEFERRED)
    assert request.disposition is RequestDisposition.DEFERRED
    assert item.included == before


def test_scoping_creates_no_commercial_or_partner_commitment() -> None:
    item = scope()
    assert item.estimate_readiness is EstimateReadiness.READY_FOR_ESTIMATE
    assert not item.creates_price
    assert not item.creates_proposal
    assert not item.selects_delivery_partner
