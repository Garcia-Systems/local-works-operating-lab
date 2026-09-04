# Workflow reconstruction methodology

## Why reconstruct current state

“Customers call us” is a summary, not a workflow. Before economics or design, reconstruct what triggers work, who acts, what information moves, which rules apply, where ownership changes, where time passes, and how work ends. **Do not design the future until you can explain the present.**

## Practical reconstruction

1. **Bound the workflow.** Name the triggering event and an observable end condition. Avoid silently combining adjacent processes.
2. **Follow the work in order.** Record each actor role and action. Roles are enough; do not model an organization chart.
3. **Name systems and mechanisms.** Record software plus phone, email, spreadsheet, and paper as understandable mechanisms. Reuse discovery records and preserve unknown capabilities.
4. **Follow information.** Mark data created, read, copied, re-entered, transformed, and sent. The purpose is to expose transfers and duplication, not to build data lineage.
5. **Make decisions explicit.** Write the question, branches, current result, decision owner, policy, and evidence. Legitimate judgment need not be automatable.
6. **Mark handoffs.** Record from/to roles, information, mechanism, ownership, waiting, and unknowns. A handoff is not inherently bad.
7. **Separate active work from waiting.** Labor time and elapsed/customer time answer different questions. Attach `MEASURED`, `ESTIMATED`, or `UNKNOWN` and a source to each value. Unknown never means zero.
8. **Walk the happy path, then exceptions.** Reconstruct normal completion and supported variations such as approval, ineligibility, balance, or missing information. Label any new fictional training assumption.
9. **Classify carefully.** `VALUE_ADDING`, `NECESSARY`, `QUESTIONABLE`, and `UNKNOWN` invite discussion; manual does not mean waste. Business context can change a classification.
10. **Describe, do not prescribe.** System switching, repeated entry, policy decisions, contact loops, and approval waits are workflow observations. “Build an integration” is a solution requirement and does not belong here.

## Evidence provenance and conflicts

Build from discovery statements, observations, and records rather than inventing a tidy path. Attribute evidence. Keep measured time distinct from estimates, retain conflicting accounts, and ask what evidence would resolve each gap. A blank or `UNKNOWN` field is more honest than invented precision.

## Playback and validation

Read a concise reconstruction back to the people doing and owning the work: “First this happens; then this role does that; if this condition applies, it goes there and waits; finally this outcome is communicated. Is that accurate?” Ask participants to correct order, missing loops, rules, mechanisms, ownership, and exceptions.

Use `DRAFT`, `PARTIALLY_VALIDATED`, `VALIDATED`, or `CONFLICTING_EVIDENCE`. Partial validation is useful: it states that the model can support the next evidence-gathering step while estimates and gaps remain. Preserve status changes/history in any future operating practice rather than overwriting what was previously believed.

## Readiness

A useful reconstruction can explain trigger, end, roles, ordered actions, systems/mechanisms, information movement, decisions, handoffs, active/wait time, and exceptions without proposing software. Only then ask whether evidence is sufficient to quantify burden. “Yes with unknowns” may mean ready to design measurement—not ready to claim value.
