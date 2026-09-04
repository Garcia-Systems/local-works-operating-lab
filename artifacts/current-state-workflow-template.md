# Current-state workflow template

> Describe **AS-IS**, not TO-BE. Preserve unknowns; do not turn observations into requirements.

**Business:**  
**Opportunity:**  
**Workflow:**  
**Date:**  
**Validation status:** `DRAFT` / `PARTIALLY_VALIDATED` / `VALIDATED` / `CONFLICTING_EVIDENCE`  
**Trigger:**  
**End condition:**

## Actors

| Role (not merely a person's name) | Work performed | Evidence/unknowns |
|---|---|---|
| | | |

## Systems/mechanisms

Include software and practical mechanisms such as phone, email, spreadsheet, or paper without pretending they are architecturally equivalent.

| System/mechanism | Purpose in this workflow | Users | Unknowns |
|---|---|---|---|
| | | | |

## Steps

Repeat this block in sequence:

**Step:**  
**Actor:**  
**Action:**  
**Type:** `ACTION` / `DECISION` / `HANDOFF` / `WAIT` / `DATA_ENTRY` / `SYSTEM_LOOKUP` / `COMMUNICATION` / `APPROVAL` / `PAYMENT` / `OTHER`  
**System/mechanism:**  
**Input:**  
**Output:**  
**Manual/automated:** `MANUAL` / `AUTOMATED` / `MIXED` / `UNKNOWN`  
**Customer-visible/internal:**  
**Classification:** `VALUE_ADDING` / `NECESSARY` / `QUESTIONABLE` / `UNKNOWN`  
**Active time:** value, unit, `MEASURED` / `ESTIMATED` / `UNKNOWN`, source  
**Wait time:** value, unit, `MEASURED` / `ESTIMATED` / `UNKNOWN`, source  
**Evidence:** statement/observation/data, participant/source, status  
**Friction notes:**  
**Unknowns:**

## Decision points

| Step/question | Branch | Current result | Policy/evidence | Unknowns |
|---|---|---|---|---|
| | | | | |

## Handoffs

| After step | From → to | Information | Mechanism | Wait | Ownership/risks/unknowns |
|---:|---|---|---|---|---|
| | | | | | |

## Data movement

Use `DATA_CREATED`, `DATA_READ`, `DATA_COPIED`, `DATA_RE-ENTERED`, `DATA_TRANSFORMED`, or `DATA_SENT`.

| Step | Information | From → to | Movement | Duplicate/re-entry? | Evidence |
|---:|---|---|---|---|---|
| | | | | | |

## Exceptions

For each supported exception, record its trigger, divergent steps, decision owner, handoffs, active time, waiting, end condition, evidence, and assumptions. Clearly label fictional training assumptions.

## Workflow metrics

- Steps; manual steps; automated steps; systems/mechanisms; handoffs; decisions; known re-entry events.
- Estimated active labor; estimated customer effort; known wait; unknown timing components.
- Never substitute zero for unknown or create an efficiency score.

## Observations

Record current-state patterns and their evidence. Do not write a technical fix or solution requirement.

## Validation questions

1. 

## Playback summary

“Let me make sure I understand. … Is that accurate?”
