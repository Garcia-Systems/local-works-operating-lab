from local_works.workflows import (
    DataMovement, DataMovementType, Duration, StepType, TimingBasis,
    ValidationStatus, Visibility, Workflow, WorkflowActor, WorkflowDecision,
    WorkflowException, WorkflowHandoff, WorkflowObservation, WorkflowStep,
    WorkflowSystem, WorkMode,
)


def sample() -> Workflow:
    member, staff = WorkflowActor("MEMBER"), WorkflowActor("STAFF")
    phone, records = WorkflowSystem("Phone", True), WorkflowSystem("Records")
    workflow = Workflow("Change", "request", "confirmation", ValidationStatus.PARTIALLY_VALIDATED)
    workflow.add_step(WorkflowStep(2, "Record request", staff, StepType.DATA_ENTRY, records,
        active_time=Duration(3, TimingBasis.ESTIMATED, "employee"), work_mode=WorkMode.MANUAL))
    workflow.add_step(WorkflowStep(1, "Make request", member, StepType.COMMUNICATION, phone,
        active_time=Duration(2, TimingBasis.MEASURED, "observation"), work_mode=WorkMode.MANUAL,
        visibility=Visibility.CUSTOMER_VISIBLE))
    workflow.add_step(WorkflowStep(3, "Send receipt", WorkflowActor("SYSTEM"), StepType.COMMUNICATION, records,
        active_time=Duration(None), work_mode=WorkMode.AUTOMATED))
    workflow.decisions.append(WorkflowDecision(2, "Eligible?", {"YES": "continue", "NO": "stop"}))
    workflow.handoffs.append(WorkflowHandoff(member, staff, 1, "request", phone))
    workflow.data_movements.append(DataMovement("request", DataMovementType.RE_ENTERED, "phone", "records", 2))
    workflow.exceptions.append(WorkflowException("Missing data", "request incomplete", (
        WorkflowStep(1, "Ask again", staff, StepType.COMMUNICATION, phone),
    )))
    workflow.observations.append(WorkflowObservation("Information is re-entered.", "interview"))
    return workflow


def test_order_actors_and_states_are_preserved() -> None:
    workflow = sample()
    assert [step.sequence for step in workflow.steps] == [1, 2, 3]
    assert workflow.steps[0].actor.role == "MEMBER"
    assert workflow.steps[1].work_mode is WorkMode.MANUAL
    assert workflow.steps[2].work_mode is WorkMode.AUTOMATED


def test_decisions_handoffs_data_and_exceptions_are_explicit() -> None:
    workflow = sample()
    assert workflow.decisions[0].branches["NO"] == "stop"
    assert workflow.handoffs[0].from_actor.role == "MEMBER"
    assert workflow.data_movements[0].movement_type is DataMovementType.RE_ENTERED
    assert len(workflow.exceptions[0].steps) != len(workflow.steps)


def test_time_unknowns_and_provenance_survive() -> None:
    workflow = sample()
    assert workflow.steps[0].active_time.basis is TimingBasis.MEASURED
    assert workflow.steps[1].active_time.basis is TimingBasis.ESTIMATED
    assert workflow.steps[2].active_time.minutes is None
    assert workflow.steps[2].active_time.minutes != 0
    assert workflow.steps[0].wait_time.minutes is None


def test_metrics_describe_without_scoring() -> None:
    metrics = sample().metrics()
    assert (metrics.steps, metrics.manual_steps, metrics.automated_steps) == (3, 2, 1)
    assert (metrics.systems_mechanisms, metrics.handoffs, metrics.decisions) == (2, 1, 1)
    assert metrics.data_reentries == 1
    assert metrics.estimated_active_minutes == 5
    assert metrics.estimated_customer_effort_minutes == 2
    assert metrics.known_wait_minutes is None
    assert metrics.unknown_timing_components == 1


def test_validation_and_observations_do_not_create_requirements() -> None:
    workflow = sample()
    assert workflow.validation_status is ValidationStatus.PARTIALLY_VALIDATED
    assert workflow.observations
    assert workflow.solution_requirements == ()
