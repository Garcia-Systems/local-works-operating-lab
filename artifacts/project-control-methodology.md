# Chapter 23 — Project-control methodology

> This is a training method, not evidence of real project activity.

## Use proportional control

Use **just enough structure to see risk early**. A six-hour configuration may need a few outcomes, owned tasks, and one concise update—not a 50-line Gantt chart or daily meetings. A multi-month integration warrants more detail and perhaps optional weekly burn rate. One project is simpler than five; portfolio capacity belongs to later scaling work.

## Outcomes and work

A **milestone** is a meaningful checkpoint or outcome; a **task** is work contributing to it. “Configuration validated in test” is a milestone; confirmation, configuration, standard/exception test preparation, and documentation are tasks. Every active task has one accountable owner. `SHARED` must name a coordinator in notes. Dependencies are explicit, and an incomplete dependency prevents readiness.

A **blocker** means affected work cannot proceed. **At risk** means work can proceed while schedule, cost, or outcome is threatened. A task blocker can put its milestone at risk without blocking the whole project. Each blocker records causal owner, impact, affected work, next action, and escalation need. Customer, delivery-partner, vendor, and Local Works delays remain distinct to explain causality, never to assign mechanical blame.

## Health without a magic score

Assess scope, schedule, cost, quality, dependencies, customer decisions, delivery capacity, and technical risk as `ON_TRACK`, `WATCH`, `AT_RISK`, or `BLOCKED`, each with a rationale. Overall status reflects evidence rather than percent complete. Reduced partner or owner capacity changes the forecast; impossible dates are not retained for appearances.

## Baseline, forecast, and variance

Protect the approved requirements baseline, original estimate, and original milestone date. A forecast is today's evidence-based expectation, not a rewritten plan; actual completion is a third field. Forecast confidence is high, moderate, low, or `UNKNOWN`, with reasons and assumptions.

`actual so far + estimate to complete = forecast total`. Re-estimate remaining work rather than subtracting actual hours from the original estimate. Variance is forecast total minus baseline (and percent only when the baseline is nonzero), so negative as well as positive variance remains visible. Larger projects may optionally track weekly owner hours, delivery hours, and cost burn; tiny work need not.

## Decisions and communication

A decision request keeps the question, owner, needed-by date, delay impact, options, recommendation, status, decision, and date out of inbox limbo. Decision latency explains forecast effects; it is not a punitive customer metric. A concise update covers completed, in progress, next, decisions, blockers, risks, changes, actions, and forecast.

Report early warning signals—fast estimate burn, unresolved vendor questions, late decisions, failed tests, reduced capacity, or scope ambiguity—before the deadline. Say what is known, likely impact, next action, and uncertainty. “Everything is going well” is not acceptable when a material unknown exists.

Escalation thresholds are proportional and hypothetical: a critical blocker aging beyond an agreed threshold, customer commitment threatened, forecast outside approved tolerance, scope or acceptance disagreement, partner failure, or security issue. Not every delay needs executive attention.

## Corrective action

Choose the response that addresses the cause: resequence work, clarify, escalate a decision, reassign, defer optional work, request change review, reforecast, pause, or reopen design. Adding people cannot resolve an unanswered business rule. While API validation waits, prepare test cases, documentation structure, or validate rules. A blocked task need not block the project.

Protect `MUST` work: `COULD` work is deferred before it silently consumes essential capacity. New “tiny” requests are `POTENTIAL_SCOPE_CHANGE`, not executable tasks; Chapter 24 will evaluate them. Schedule pressure does not silently remove testing, documentation, or security. **The deadline does not make risk disappear.**

Track Local Works time for customer communication, partner coordination, decision management, QA/project review, and other control work. PM time is not free. Keep a lightweight event log for meaningful task, blocker, decision, forecast, escalation, and customer-update events—not a full audit log.
