# Chapter 12 — Choose the Simplest Sensible Solution

> **Part IV — Design the Right Solution**
>
> **Core question:** Now that Local Works understands and has qualified the problem, what type of solution should be considered first?

The answer is not “software.” It is **the simplest economically sensible option that adequately solves the validated problem**. Do not build software just because you can.

## 1. Qualified problem, not blank canvas

Chapter 11 decides whether an opportunity deserves more effort. Chapter 12 begins design through a disciplined progression:

**Qualified Problem → Solution Alternatives → Compare Simplicity / Fit / Cost / Risk → Preferred Solution Path**

Carry forward the workflow, policies, constraints, systems, economics, customer goal, and evidence quality. “Opportunity qualified → custom application” is not valid reasoning. In Harbor Fitness, Chapter 11 actually remains at `MORE_EVIDENCE_REQUIRED`; its alternatives therefore demonstrate provisional thinking, not an approved project.

## 2. The Local Works solution hierarchy

**CONFIGURE → INTEGRATE → AUTOMATE → CUSTOM BUILD → LEAVE ALONE**

This is a decision hierarchy favoring simplicity when adequate, not a ladder every opportunity climbs. No option wins solely because of its position or price. A known platform limitation might make configuration irrelevant; a unique workflow might make custom work reasonable. The explanation must show why simpler options are insufficient.

## 3. Configure

Configure uses capabilities already present in a system: enable self-service, change permissions, configure notifications, or adjust vendor-supported forms/workflows. Ask: **Can capabilities the customer already owns adequately solve the problem?**

A fictional scheduling business believes it needs a replacement. Discovery demonstrates that its existing platform already supports automated reminders, waitlists, and cancellation rules, but they are disabled. `CONFIGURE` offers high coverage, low delivery complexity, low switching cost, no custom code, and fast time to value. Finding that answer is a Local Works success; value does not depend on maximizing development.

## 4. Integrate

Integrate connects existing systems so information moves effectively. A fictional home-services company re-enters completed-job details from scheduling into invoicing. Both products demonstrably support the required integration capabilities. The core capabilities exist; information movement is the problem. `INTEGRATE` is preferable to replacing both.

Integration is distinct from automation: its defining purpose is connection and movement across system boundaries, even if the connection runs automatically.

## 5. Automate

Automation reduces safely defined repetitive work without necessarily replacing core systems. A fictional professional office receives a form, creates an internal task, sends confirmation, and reminds an employee when unresolved. Its systems are otherwise adequate, while coordination is repetitive. A vendor-neutral workflow-automation path may be preferred.

Automation needs reliable triggers, rules, state, exceptions, permissions, and failure handling. Manual work is not automatically bad: judgment or relationship work may be intentional.

## 6. Custom build

Custom build creates a purpose-built portal, operational interface, workflow application, or unique orchestration/business logic. It is allowed—not the default.

Consider a fictional multi-location regulated operation with a validated high-frequency workflow, meaningful burden, unique location- and case-dependent rules, and cross-system coordination no existing tool supplies. Configuration has been demonstrated inadequate; integrations can move data but cannot supply the missing decision capability; task automation cannot model the workflow safely. The organization owns the policy, has support capacity, and evidence suggests recoverable value and plausible delivery. `CUSTOM_BUILD` can be justified there.

Contrast that evidence with “we need a member portal.” The latter merely names a desired artifact.

## 7. Leave alone

Leaving alone is a real design decision. The process may work adequately; frequency or recoverable value may be low; change cost/risk may be high; policy may intentionally require a person; or the customer may not be ready.

A fictional task occurring twice yearly with about $10 annual burden may technically be automatable. `LEAVE_ALONE` is economically sensible. Technical possibility does not create justification.

## 8. Cheapest is not always best

Suppose configuration is cheap but covers 10% of the problem, integration covers 85% at moderate relative cost, and custom software covers 100% while creating very high cost and long-term responsibility. The choice must compare:

**ADEQUACY + ECONOMICS + RISK + COMPLEXITY**

Low price cannot rescue inadequate coverage. Maximum coverage cannot erase disproportionate cost and risk. This chapter uses qualitative relative categories, never fabricated delivery estimates: cost from `VERY_LOW` to `VERY_HIGH` (or `UNKNOWN`), complexity from `LOW` to `VERY_HIGH` (or `UNKNOWN`), and time as `DAYS`, `WEEKS`, `MONTHS`, or `UNKNOWN`.

## 9. Capability validation

“Does the membership platform support conditional self-service freezes?” can be `YES`, `NO`, or `UNKNOWN`. Preserve `UNKNOWN`. Record the system, capability, consequence, current evidence, and a bounded validation method such as official documentation, an admin demonstration, vendor support, sandbox/test, or implementation-partner input.

Unknown capability means `CAPABILITY_VALIDATION_REQUIRED`, not custom build. This lab does not contact vendors and does not invent their functionality.

## 10. Policy and process changes

Technology intervention is only part of design. If policy requires manager approval for exceptions but the current habit sends every request to a manager, routine eligible requests might move to front desk staff. Represent this operational change within `CONFIGURE`, `LEAVE_ALONE`, or another relevant alternative rather than inventing a sixth technology path. Confirm policy ownership first.

## 11. Compare alternatives

Generate at least two plausible alternatives whenever practical. For each, expose problem coverage, simplicity, relative implementation and ongoing cost, delivery and operating risk, time to value, customer change, system dependency, maintainability, reversibility, measurability, policy fit, scalability, assumptions, and evidence. Never hide judgment in one score.

An alternative can be `PREFERRED`, `VIABLE_ALTERNATIVE`, `NEEDS_VALIDATION`, `NOT_RECOMMENDED`, or `DISQUALIFIED`. The opportunity may result in `PREFERRED_PATH_IDENTIFIED`, `CAPABILITY_VALIDATION_REQUIRED`, `MORE_SOLUTION_RESEARCH_REQUIRED`, `LEAVE_ALONE`, or `DECLINE`. None is a proposal.

## 12. Why customers ask for custom software too early

“Our website looks old,” “we want an app,” “we need AI,” “our competitor has one,” “we hate our vendor,” “it would be cool,” “we want everything in one system,” and “custom gives us control” may lead to valid inquiry. None establishes problem coverage, feasibility, economics, ownership, or the inadequacy of simpler paths.

## 13. The custom-build justification test

A confident custom direction normally needs evidence that the problem is qualified and meaningful; configuration is inadequate; integration cannot provide the capability; automation alone is insufficient; policy/constraints can be met; the organization can own/support the result; expected value may justify cost/risk; and delivery is plausible. Not every fact must be certain yet, but major unsupported assumptions block confidence.

## 14. Harbor Fitness alternatives

The fictional comparison includes configuring its membership platform, integrating a lightweight request interface, automating staff coordination, building a custom account-management experience, and leaving the workflow alone. Native capability, APIs, events, complete rules, access restrictions, ownership, and change readiness remain unknown.

The current direction is `CAPABILITY_VALIDATION_REQUIRED`: investigate configuration and supported integration/automation possibilities before custom work. Custom is not currently justified because simpler paths have not been shown inadequate, economics remain estimated and modest, and ownership/support capacity is unresolved. Leave-alone remains viable.

## 15. What would change the recommendation?

Demonstrated native support strengthens `CONFIGURE`. Missing native support but suitable APIs/events strengthens `INTEGRATE` or `AUTOMATE`. Demonstrated absence of critical capability and viable interfaces—plus all custom-build gate evidence—makes `CUSTOM_BUILD` plausible. Insufficient recoverable value strengthens `LEAVE_ALONE`. Evidence changes the direction; preference does not rewrite evidence.

## 16. Executable exercise

Run:

```bash
python scripts/run_chapter_12.py
```

It prints the qualified-problem caveat, hierarchy, five Harbor alternatives, capability questions, transparent comparison, premature-custom rejection, current direction, and evidence that would change it. Qualitative categories are not bids or project estimates.

## 17. Chapter artifacts

- `artifacts/solution-selection-methodology.md` explains the reusable method.
- `artifacts/solution-alternatives-template.md` supports future comparisons.
- `artifacts/harbor_fitness/12-solution-alternatives.md` records the fictional case.
- `artifacts/harbor_fitness/12-solution-assumptions.md` preserves open assumptions.
- `local_works/solutions.py` makes the visible gates executable.

No project is priced; no detailed cost, recoverable value, ROI, implementation estimate, scope, proposal, vendor choice, partner sourcing, contract, delivery, or support design is produced.

## 18. Readiness checkpoint

The reader should now be able to explain all five paths; generate multiple alternatives; distinguish configuration, integration, and automation; explain justified custom work and valid leave-alone decisions; compare coverage with complexity; identify capability assumptions without inventing functionality; reject “we need an app” as justification; and explain why new evidence can change the preferred path.

Next—not here—Chapter 13 asks whether a proposed solution creates enough recoverable value to justify its cost and risk.
