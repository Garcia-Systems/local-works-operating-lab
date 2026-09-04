"""Run Chapter 9's deterministic, fictional current-state reconstruction."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.workflows import (  # noqa: E402
    DataMovement, DataMovementType as Move, Duration, StepClassification as Class,
    StepType, TimingBasis, ValidationStatus, Visibility, Workflow, WorkflowActor,
    WorkflowDecision, WorkflowException, WorkflowHandoff, WorkflowObservation,
    WorkflowStep, WorkflowSystem, WorkMode,
)


MEMBER = WorkflowActor("MEMBER")
FRONT_DESK = WorkflowActor("FRONT_DESK_EMPLOYEE")
MANAGER = WorkflowActor("MEMBERSHIP_MANAGER")
PHONE = WorkflowSystem("Phone", mechanism=True)
EMAIL = WorkflowSystem("Staff Email", mechanism=True)
PLATFORM = WorkflowSystem("Membership Management Platform")
SHEET = WorkflowSystem("Spreadsheet")
EST = TimingBasis.ESTIMATED


def step(number: int, description: str, actor: WorkflowActor, kind: StepType,
         system: WorkflowSystem | None, minutes: float | None,
         visibility: Visibility = Visibility.INTERNAL, **kwargs: object) -> WorkflowStep:
    duration = Duration(minutes, EST, "Chapter 8 participant estimate") if minutes is not None else Duration(None)
    return WorkflowStep(number, description, actor, kind, system,
        active_time=duration, evidence_source="Chapter 8 discovery interviews",
        evidence_status="CUSTOMER_STATEMENT / EMPLOYEE_ESTIMATE",
        work_mode=WorkMode.MANUAL, visibility=visibility, **kwargs)


def build_workflow() -> Workflow:
    workflow = Workflow(
        "Membership Account Management — Membership Freeze",
        "A member asks the front desk to freeze a membership by phone or email.",
        "The member receives confirmation of the recorded outcome.",
        ValidationStatus.PARTIALLY_VALIDATED,
    )
    steps = [
        step(1, "Requests a membership freeze and provides account identity.", MEMBER, StepType.COMMUNICATION, PHONE, 2, Visibility.CUSTOMER_VISIBLE, classification=Class.VALUE_ADDING),
        step(2, "Reads the request or takes the call and gathers dates and reason.", FRONT_DESK, StepType.COMMUNICATION, PHONE, 1, Visibility.CUSTOMER_VISIBLE, classification=Class.NECESSARY),
        step(3, "Looks up the member account and notes.", FRONT_DESK, StepType.SYSTEM_LOOKUP, PLATFORM, 1, classification=Class.NECESSARY),
        step(4, "Determines membership type and applies freeze eligibility policy.", FRONT_DESK, StepType.DECISION, PLATFORM, 1, classification=Class.NECESSARY),
        step(5, "Records the requested freeze and updates membership status.", FRONT_DESK, StepType.DATA_ENTRY, PLATFORM, None, classification=Class.NECESSARY, unknowns=("Does the status change automatically update billing?",)),
        step(6, "Re-enters a supplemental freeze note for tracking.", FRONT_DESK, StepType.DATA_ENTRY, SHEET, 1, classification=Class.QUESTIONABLE),
        step(7, "Checks the resulting membership and billing status.", FRONT_DESK, StepType.SYSTEM_LOOKUP, PLATFORM, None, classification=Class.NECESSARY, unknowns=("How billing status is updated is unknown.",)),
        step(8, "Sends the member confirmation.", FRONT_DESK, StepType.COMMUNICATION, EMAIL, 1, Visibility.CUSTOMER_VISIBLE, classification=Class.VALUE_ADDING),
    ]
    for item in steps:
        workflow.add_step(item)
    workflow.decisions.append(WorkflowDecision(4, "Is this membership eligible for a freeze?", {
        "YES": "Continue with the normal update.", "NO": "Explain that policy does not permit the freeze.",
        "REQUIRES_APPROVAL": "Hand the request to the membership manager.",
    }, "Eligibility depends on membership type; Chapter 8 manager statement."))
    workflow.handoffs.extend([
        WorkflowHandoff(MEMBER, FRONT_DESK, 1, "Identity, requested dates, and reason", PHONE),
        WorkflowHandoff(FRONT_DESK, MEMBER, 8, "Freeze outcome and status", EMAIL),
    ])
    workflow.data_movements.extend([
        DataMovement("Identity, freeze dates, reason", Move.CREATED, "Member", "Front desk", 1),
        DataMovement("Account and membership notes", Move.READ, "Membership platform", "Front desk", 3),
        DataMovement("Freeze dates and status", Move.RE_ENTERED, "Member request", "Membership platform", 5),
        DataMovement("Freeze dates and status", Move.RE_ENTERED, "Membership platform", "Spreadsheet", 6),
        DataMovement("Freeze outcome", Move.SENT, "Front desk", "Member", 8),
    ])
    exception_steps = tuple(steps[:4] + [
        step(5, "Sends unclear eligibility or overdue-balance details to manager.", FRONT_DESK, StepType.HANDOFF, EMAIL, 2, classification=Class.NECESSARY),
        WorkflowStep(6, "Waits for manager review.", FRONT_DESK, StepType.WAIT, EMAIL,
            active_time=Duration(0, EST, "Training arithmetic only"), wait_time=Duration(None),
            evidence_source="Chapter 8 employee statement", evidence_status="WAIT EXISTS; DURATION UNKNOWN",
            work_mode=WorkMode.MANUAL, visibility=Visibility.INTERNAL, classification=Class.UNKNOWN),
        step(7, "Reviews the exception and decides whether to approve.", MANAGER, StepType.APPROVAL, PLATFORM, None, classification=Class.NECESSARY),
        step(8, "Records the approved outcome in the membership platform.", FRONT_DESK, StepType.DATA_ENTRY, PLATFORM, None, classification=Class.NECESSARY),
        step(9, "Re-enters a supplemental note in the spreadsheet.", FRONT_DESK, StepType.DATA_ENTRY, SHEET, 1, classification=Class.QUESTIONABLE),
        step(10, "Sends the member the decision.", FRONT_DESK, StepType.COMMUNICATION, EMAIL, 1, Visibility.CUSTOMER_VISIBLE, classification=Class.VALUE_ADDING),
    ])
    workflow.exceptions.append(WorkflowException(
        "Manager approval",
        "Eligibility is unclear, a medical freeze needs review, or a balance is overdue.",
        exception_steps,
        handoffs=(
            WorkflowHandoff(MEMBER, FRONT_DESK, 1, "Identity, requested dates, and reason", PHONE),
            WorkflowHandoff(FRONT_DESK, MANAGER, 5, "Account, request, and exception details", EMAIL, Duration(None)),
            WorkflowHandoff(FRONT_DESK, MEMBER, 10, "Approval outcome", EMAIL),
        ),
    ))
    workflow.observations.extend([
        WorkflowObservation("Staff manually enter request information.", "Chapter 8 employee account."),
        WorkflowObservation("Eligibility is a policy-dependent decision; manual review is not automatically waste.", "Chapter 8 manager account."),
        WorkflowObservation("Normal work switches among intake, platform, spreadsheet, and confirmation mechanisms.", "Reconstructed steps."),
        WorkflowObservation("The spreadsheet appears to repeat information already recorded elsewhere.", "Chapter 8 employee account; completeness remains unvalidated."),
        WorkflowObservation("Exception approval introduces waiting whose duration is unknown.", "Chapter 8 interviews."),
    ])
    workflow.validation_questions.extend([
        "Does a platform status update automatically change billing?",
        "Is the spreadsheet always used, and what purpose makes it necessary?",
        "How long do approval requests wait, and who owns them while waiting?",
        "What are the precise eligibility branches and end states?",
    ])
    return workflow


def duration_text(duration: Duration) -> str:
    return f"{duration.minutes:g} min ({duration.basis.name})" if duration.minutes is not None else "UNKNOWN"


def main() -> None:
    workflow = build_workflow()
    print("CHAPTER 9 — RECONSTRUCT THE CURRENT WORKFLOW\nFICTIONAL TRAINING SCENARIO\nNOT A REAL CUSTOMER WORKFLOW")
    print("\nSECTION 1 — Starting evidence")
    print("Chapter 8 says front desk staff receive calls/emails, look up accounts and notes, apply policy, update the platform, note a spreadsheet, and reply. Normal handling was estimated near five minutes; exceptions were estimated at 15–20 minutes. Nothing was measured.")
    print("\nSECTION 2 — Happy path")
    for item in workflow.steps:
        print(f"{item.sequence:02} {item.actor.role}\n   {item.description}\n   Mechanism: {item.system.name if item.system else 'UNKNOWN'} | Type: {item.step_type.name} | Active: {duration_text(item.active_time)} | Evidence: {item.evidence_status} | {item.work_mode.name} | Unknowns: {', '.join(item.unknowns) or 'none recorded'}")
    print("\nSECTION 3 — Data movement")
    for move in workflow.data_movements:
        print(f"- {move.information}: {move.source} → {move.destination} [{move.movement_type.name}, step {move.step_sequence}]")
    print("\nSECTION 4 — Handoffs")
    for handoff in workflow.handoffs:
        print(f"- {handoff.from_actor.role} → {handoff.to_actor.role}: {handoff.information} via {handoff.mechanism.name if handoff.mechanism else 'UNKNOWN'}; wait {duration_text(handoff.wait_time)}")
    print("\nSECTION 5 — Decisions")
    for decision in workflow.decisions:
        print(f"- Step {decision.step_sequence}: {decision.question}")
        for branch, result in decision.branches.items(): print(f"  {branch} → {result}")
    exception = workflow.exceptions[0]
    normal = workflow.metrics()
    unusual = workflow.metrics(exception.steps)
    print("\nSECTION 6 — Exception path")
    print(f"{exception.name}: {exception.trigger}")
    for item in exception.steps: print(f"{item.sequence:02} {item.actor.role}: {item.description} [active {duration_text(item.active_time)}; wait {duration_text(item.wait_time)}]")
    print(f"Change: {normal.steps} → {unusual.steps} steps; active known/estimated {normal.estimated_active_minutes} → {unusual.estimated_active_minutes} min; handoffs {normal.handoffs} → {unusual.handoffs}; approval wait remains UNKNOWN.")
    print("\nSECTION 7 — Timing")
    print(f"Known/estimated active labor represented: {normal.estimated_active_minutes} minutes (partial, not a complete total). Customer effort represented: {normal.estimated_customer_effort_minutes} minutes. Known wait: {normal.known_wait_minutes if normal.known_wait_minutes is not None else 'UNKNOWN'}. Unknown timing components: {normal.unknown_timing_components}.")
    print("Unknown values are not counted as zero; all supplied values are estimates, not measurements.")
    print("\nSECTION 8 — Workflow observations")
    for observation in workflow.observations: print(f"- {observation.description} Evidence: {observation.evidence}")
    print("These are observations, not solution requirements.")
    print("\nSECTION 9 — Playback")
    print("Let me make sure I understand. A member calls or emails; front desk staff gather the request, look up the account, apply eligibility policy, update the membership platform, add a spreadsheet note, verify status, and confirm the outcome. If eligibility is unclear or an exception applies, staff send the request to a manager and wait for review. Is that accurate?")
    print("\nSECTION 10 — Readiness")
    print("Do we understand the current process well enough to quantify its economic burden?\nYES WITH UNKNOWNS — the path is reconstructable, but volume, measured work time, approval wait, correction rate, and platform/billing behavior still require validation.")


if __name__ == "__main__":
    main()
