# Chapter 9 — Reconstruct the Current Workflow

## 1. “Members call us” is not a workflow

That sentence hides finding instructions, initiating contact, identity checks, account lookup, eligibility rules, record changes, billing checks, notes, confirmation, and exceptions. Chapter 8 gathered evidence. Chapter 9 turns it into a precise **current-state (AS-IS)** account.

> **Do not design the future until you can explain the present.**

Reconstruction does not prove that a workflow is inefficient and does not authorize software. It gives later economic analysis an honest unit of work.

## 2. Start with the trigger

A workflow needs boundaries. “A member asks the front desk to freeze a membership” is a trigger. “The member receives the recorded outcome” is an end condition. Without both, interviews drift into related enrollment, billing, and cancellation processes and step counts become meaningless.

## 3. Follow the work

Ask the participant to narrate a recent instance, one action at a time. For each action capture sequence, description, input, output, evidence, visibility, friction, and unknowns. Do not force every field to be known. An explicit unknown—such as whether updating status also updates billing—is a useful result.

## 4. Actors

Model roles that perform work: member, front-desk employee, membership manager, accounting, system, or external vendor. Names may support evidence attribution, but an organization chart is not the objective. The question is “who does the work or owns the decision?”

## 5. Systems and mechanisms

Record the membership platform and payment processor, but also phone, email, spreadsheet, and paper. The latter may be mechanisms rather than architectural systems. That distinction should not make them invisible: they still receive information, create handoffs, and consume attention.

## 6. Information movement

Follow important data across the steps. Mark when it is created, read, copied, re-entered, transformed, or sent. A member's identity, dates, and reason may move from speech or email to an employee, platform, spreadsheet, and confirmation. This is a compact transfer record—not a data-lineage platform. Re-entry is an observation, not automatic proof of waste.

## 7. Decisions

Write decisions as questions with branches. “Is this membership eligible?” might produce **yes**, **no**, or **requires approval**. Capture the policy and decision owner. A later design must preserve legitimate policy, and neither manual judgment nor approval is presumed automatable.

## 8. Handoffs

Identify who or what passes information to whom, by which mechanism, and who owns the work afterward. Handoffs can introduce waiting, information loss, ambiguity, duplication, or errors, but they can also be necessary. Record before judging.

## 9. Active work vs waiting

Eight minutes of labor can coexist with two days of customer elapsed time. Track active and wait time separately. A manager review may add little hands-on work but substantial inbox waiting. If discovery did not establish a duration, write **UNKNOWN**; never treat it as zero.

Descriptive metrics include step, manual/automated, mechanism, handoff, decision, and re-entry counts; estimated active labor; customer effort; known waiting; and unknown timing components. They are not a magic efficiency score.

## 10. The happy path is not enough

A normal eligible freeze offers the cleanest sequence and often understates reality. Reconstruct it first so everyone shares a baseline, then ask what happens when the next condition fails. Ensure the normal path reaches a specific end rather than stopping at “system updated.”

## 11. Exceptions

Chapter 8 supports overdue balances, medical-freeze review, unclear notes, and correction after wrong entry. The manager-approval exception adds a handoff, decision work, and waiting. Missing-information and ineligible branches remain less fully understood. Only use supported exceptions or explicitly mark new fictional training assumptions.

## 12. Estimated vs measured timing

Harbor Fitness participants estimated about five minutes for a normal request and 15–20 for an overdue-balance exception; they said the work had never been timed. Preserve `EMPLOYEE_ESTIMATE`, source, value, and unit. A per-step allocation added for an exercise is also an assumption and may expose a conflict rather than resolve it. Measurement comes later.

## 13. Play the workflow back

Say: “Let me make sure I understand. A member calls or emails. Front desk gathers the request, finds the account, applies eligibility policy, changes the record, adds the supplemental note, checks status, and confirms the outcome. Exceptions go to the manager and wait for review. Is that accurate?”

Playback lets the people doing the work correct missing steps, ownership, order, systems, branches, and timing. Use `DRAFT`, `PARTIALLY_VALIDATED`, `VALIDATED`, or `CONFLICTING_EVIDENCE`. A simulation with unresolved estimates should remain partially validated.

## 14. Workflow observations without solution design

“Information appears to be entered in two locations” is an observation. “Build API synchronization” is a proposed requirement. This chapter stops at the former. Likewise, system switching, manual policy determination, repeated customer contact, and approval waiting are patterns to validate—not technical recommendations.

Classifying steps as `VALUE_ADDING`, `NECESSARY`, `QUESTIONABLE`, or `UNKNOWN` makes judgment visible. Identity verification and policy application may be necessary. Spreadsheet re-entry may be questionable. Manual work is not automatically bad.

## 15. Harbor Fitness current-state workflow

The fictional happy path is request → gather details → account lookup → eligibility decision → platform update → spreadsheet note → status check → confirmation. The exception replaces normal continuation with a manager handoff, unknown wait, review, outcome entry, supplemental note, and communication.

Its actors are member, front desk, and membership manager. Its mechanisms are phone/email, the membership platform, and spreadsheet. It has an explicit eligibility decision and tracks request data into two entry points. Platform/billing behavior, precise rules, spreadsheet purpose, active time, waiting, correction behavior, and ownership during approval remain unknown.

The artifact is `PARTIALLY_VALIDATED`. Its playback is suitable for correction; its numbers are not results from a real customer.

## 16. Executable exercise

Run:

```bash
python scripts/run_chapter_09.py
```

Read starting evidence, happy path, transfers, handoffs, decision branches, the approval exception, incomplete timing, observations, playback, and readiness. Notice that unknown time does not disappear into zero and that no future-state recommendation is printed.

## 17. Chapter artifacts

- `artifacts/harbor_fitness/09-current-state-workflow.md` — fictional reconstruction and validation questions.
- `artifacts/current-state-workflow-template.md` — reusable field guide.
- `artifacts/workflow-reconstruction-methodology.md` — reconstruction and playback method.
- `local_works/workflows.py` — deliberately small analytical records, not an engine.

## 18. Readiness checkpoint

The reader should now be able to reconstruct from discovery evidence; bound a workflow; name actors and mechanisms; expose information transfers, decisions, handoffs, waiting, and exceptions; distinguish active from elapsed time and estimated from measured; preserve unknowns; separate observations from requirements; and play the account back for validation.

For Harbor Fitness the answer to “Do we understand the current process well enough to quantify its economic burden?” is **YES WITH UNKNOWNS**: enough to plan measurement, not enough to claim annual burden, recoverable value, ROI, or select a solution. Those topics are intentionally deferred. Stop here; do not design the future state.
