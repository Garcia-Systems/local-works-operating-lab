# Chapter 23 — Milestones and Project Control

## 1. Project control without bureaucracy

Project control is not more status meetings. It is knowing what should and does happen, what is blocked, which decisions are needed, what changed, what threatens scope/cost/time, what the customer needs to know, and what action follows. Control should match project size: **just enough to see risk early**.

## 2. Milestones vs tasks

A milestone is a meaningful outcome; a task is a unit of work contributing to one. “Configuration validated in test” is an outcome. Confirm capability, configure the rule, prepare standard and exception tests, and document results are tasks. Do not promote every task into a milestone.

## 3. Ownership

Every active task has an accountable customer, Local Works, delivery-partner, vendor, or shared owner. Shared work must identify its coordinator. “Everybody” is not ownership.

## 4. Dependencies

Configuration waits for the business rule; API validation waits for sandbox access; review waits for completed preparation. Dependencies are recorded, and blocked prerequisites propagate risk.

## 5. Blockers vs risks

Blocked means work cannot proceed. At risk means it can proceed but an outcome is threatened. Missing credentials blocks an API test; a slowly approaching vendor response threshold first creates risk. A blocked task does not necessarily block the project.

## 6. Project health

Scope, schedule, cost, quality, dependencies, customer decisions, delivery capacity, and technical risk each receive a state and plain-language rationale. There is no magic score and percentage complete is not the only truth.

## 7. Plan vs forecast

The baseline date records the plan. The forecast records the current expectation. Actual completion records what happened. Reforecasting never overwrites history, and confidence stays `UNKNOWN` when evidence is absent.

## 8. Estimate vs actual

Chapter 19's estimate remains the baseline. Chapter 23 can record explicitly simulated actual effort and current projected delivery cost, but final economics wait for Chapter 26.

## 9. Estimate to complete

**Actual so far + a newly considered estimate to complete = forecast total.** Original remaining effort is not assumed unchanged after learning.

## 10. Variance

Forecast total minus baseline exposes positive or negative effort variance. Percent variance is useful only where inputs support it; it is a scenario result, not false precision.

## 11–14. Preserve delay causality

Customer access or policy decisions, partner availability or rework, vendor approval or outages, and Local Works coordination or review can each cause delay. Record the responsible source without blame and avoid the content-free label “project delay.” Local Works is not assumed perfect.

## 15. Decision requests

Keep question, owner, deadline, impact, options, recommendation, state, and answer together. Decisions should not disappear in chat.

## 16. Decision latency

Elapsed time from request to answer can explain a forecast move. It is not a punitive customer performance metric.

## 17. Status updates

Prefer a short factual set: completed, in progress, next, decisions, blockers, risks, changes, party actions, and forecast. Report material uncertainty rather than “everything is going well.”

## 18. Early warning

Fast estimate burn, unanswered vendor questions, late decisions, test problems, reduced capacity, and ambiguous additions are visible before a commitment is missed. A known problem today should not surprise the customer in two weeks.

## 19. Escalation

Configurable thresholds can include blocker age, threatened commitment, forecast outside tolerance, scope/acceptance disagreement, partner failure, and security. Not every delay is an executive escalation.

## 20. Corrective actions

Resequence, clarify, escalate the decision, reassign, reduce or defer optional scope, request change review, reforecast, pause, or reopen design. Do not reflexively add developers.

## 21. Resequencing

If exception validation waits on a vendor, prepare test cases and documentation or validate known rules. Partial progress is honest when the blocked path remains visible.

## 22. Protecting MUST work

When time tightens, defer `COULD` work before it consumes `MUST` capacity. Urgency follows business impact, not whoever asked most recently.

## 23. Scope-creep signals

A small adjacent request is marked `POTENTIAL_SCOPE_CHANGE`; it is not silently converted to delivery work. Chapter 24 will classify and evaluate change.

## 24. Deadline pressure and quality

Testing, documentation, and security do not disappear when dates tighten. Removing a control requires an explicit decision. **The deadline does not make risk disappear.**

## 25. Capacity

A change from 20 to 8 partner hours per week changes the forecast. Local Works also tracks communication, coordination, decisions, QA/project review, and documentation review; owner time is not free. Weekly burn rate is optional for larger work. Multiple-project capacity belongs to Part VIII.

## 26. Baseline protection

Never overwrite the original estimate, planned milestone, or approved requirements baseline. Keep baseline, forecast, and actual separate, supported by a lightweight major-event log.

## 27. Customer communication

State evidence, impact, next action, and uncertainty. Better than “developer is behind”: “Validation is complete; exception routing awaits vendor clarification. Without an answer by Thursday, test readiness likely moves about one week.”

## 28. Harbor Fitness project control

The fictional paid validation stays small: six outcomes from kickoff through recommendation, seven owned tasks, an ambiguous vendor capability, and a customer policy decision. An 18-hour estimate becomes a 22-hour forecast after observed simulated validation behavior. M4 moves from Friday 11 September to Tuesday 15 September without erasing the plan.

## 29. Failure: green until red

Weeks 1–3 say “on track”; week 4 announces a three-week miss. Ignored vendor uncertainty, overrun, failed tests, and decision delay show why **status reporting without forecasting is not project control**.

## 30. Failure: everything urgent

Every request becomes urgent, causing context switching and late MUST work. Urgency must connect to business impact.

## 31. Failure: hidden bad news

A Monday critical API issue disclosed only at Friday's deadline creates customer surprise. Disclose Monday or Tuesday with likely impact and action.

## 32. Failure: adding people to the wrong problem

A second developer cannot decide an unresolved customer business rule. Correct the constraint rather than adding capacity reflexively.

## 33. Success: early reforecast

On Tuesday, record vendor risk, identify unaffected work, update the Friday forecast, inform the customer, request the decision, and keep moving. On Friday the date may have moved, but the customer is not surprised: control succeeded.

## 34. Executable exercise

Run `python scripts/run_chapter_23.py`. It is fictional training and performs no customer work, QA, change, acceptance, or deployment.

## 35. Chapter artifacts

Use the project-control, milestone, blocker, and concise update templates; the Harbor record demonstrates them. The methodology explains proportional use.

## 36. Readiness checkpoint

The reader can right-size milestones; distinguish and own tasks; identify dependencies, blockers, risks, and causal delay; protect baselines; forecast and calculate remaining effort/variance; request decisions; communicate early warning; choose corrective action and resequence; protect MUST work and quality; flag—not execute—scope additions; track owner effort; and explain health with rationales.
