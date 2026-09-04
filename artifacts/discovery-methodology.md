# Discovery methodology

## Purpose

Discovery turns an opportunity hypothesis into an evidence-based understanding of the business problem. Its progression is:

**Audit observation → opportunity hypothesis → discovery questions → customer evidence → revised understanding**

It tests whether the problem is real and important, the workflow is understood, people care about change, authority and plausible funding exist, constraints matter, and more analysis is justified. **Discovery is not a sales presentation.** `STOP`—no project—is a valid, successful learning result.

## Questions reveal work

Ask open questions before closed ones. “Walk me through what happens when a member wants to cancel” reveals the current state; “Wouldn't online cancellation be easier?” leads the participant toward a solution. Likewise, replace “How much time does your broken system waste?” with “How often does this happen, and what does a staff member do?”

Cover current state, frequency/volume, people, time/burden, errors/exceptions, customer impact, business impact, systems, policy, constraints, urgency, authority, budget, and success criteria. Ask what a requested app or AI must help someone accomplish. A feature request is evidence of a preference, not a validated problem or selected solution.

Repeated “why?” can help but becomes misleading when mechanical. Apparent technical friction may instead be a **technical limitation, business policy, process habit, configuration, integration gap, or knowledge/training issue**. Record the supported cause and leave the rest unknown.

## Evidence discipline

A statement is evidence of that participant's account, not perfect truth. Preserve source, participant, value, unit, notes, and provenance:

- **MEASURED_DATA:** produced by a stated measurement or record review.
- **ESTIMATE:** a numeric judgment such as “about 20 per week.”
- **CUSTOMER_STATEMENT:** a participant's qualitative account.
- **OBSERVATION:** directly seen in a bounded context.
- **UNKNOWN:** not established; never silently zero, low, or bad.

Interview managers and people doing the work. If a manager says five minutes while an employee says exceptions take twenty, keep both accounts. Do not average contradictory testimony. Record the conflict, unresolved question, and evidence needed.

## Context and complexity

Inventory participating systems without designing architecture: purpose, users, workflow part, known limitations/integrations, unknown capabilities, owner/vendor, and access constraints. Never invent vendor capability. Record policies and constraints separately from system limitations.

Ask “what happens when it doesn't go normally?” Exceptions often reveal approvals, rework, disputed status, or missing information hidden by the happy path. Examples are prompts, not assumed customer facts.

## Evidence requests and exits

Missing information should create a practical request: the need, possible evidence, and unresolved question. Logs might test volume, sampled observation might test handling time, an inbox review might test complaints, and correction records might test errors. Discovery does not access those sources merely by requesting them.

Valid exits are:

- `CONTINUE_ANALYSIS` — enough evidence supports the next analytical step.
- `MORE_EVIDENCE_REQUIRED` — specified evidence blocks interpretation.
- `OPPORTUNITY_WEAKENED` — evidence reduces the apparent importance.
- `STOP` — no further Local Works work is justified.

None means custom build, project approved, or proposal ready. Discovery selects no technical solution and establishes no financial value.
