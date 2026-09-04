# Solution-selection methodology

## Governing principle

Start with the qualified problem, current workflow, evidence, current burden, policy, constraints, systems, and desired outcome—not a blank canvas. Generate alternatives, compare adequacy/simplicity/cost/risk, then identify a provisional direction. Choose **the simplest economically sensible option that adequately solves the validated problem**. Do not build software merely because you can.

## Decision hierarchy

1. **Configure:** use capabilities the customer already owns—settings, permissions, notifications, forms, or supported workflows. Ask whether current capabilities can adequately solve the problem.
2. **Integrate:** connect systems whose core capabilities already exist. Ask whether information, rather than capability, is missing.
3. **Automate:** make a defined repetitive process execute or coordinate reliably using existing tools/interfaces. Ask whether rules, triggers, exceptions, and failure handling are safe and known.
4. **Custom build:** create purpose-built software only when simpler paths cannot adequately supply critical capability and ownership/economics/risk are plausible.
5. **Leave alone:** accept the current process when burden is small, intervention disproportionate, risk high, manual judgment intentional, readiness absent, or the current process is adequate.

This order expresses a preference, not mandatory progression. A demonstrated hard limitation can eliminate an option. Configuration does not win merely by being cheap, and custom build is allowed when justified.

## Adequacy before cheapness

`CHEAPEST ≠ BEST`. A configuration addressing 10% of the validated workflow may be inferior to an integration addressing 85%. A custom system might cover 100% but add disproportionate cost, delivery risk, and maintenance. Compare problem coverage, simplicity, relative implementation/ongoing cost, delivery/operating risk, time to value, behavior change, dependencies, maintainability, reversibility, measurability, policy fit, and scalability. Keep the dimensions visible; do not collapse them into an opaque score.

Chapter 12 uses only qualitative cost (`VERY_LOW` through `VERY_HIGH` or `UNKNOWN`), complexity (`LOW` through `VERY_HIGH` or `UNKNOWN`), and time (`DAYS`, `WEEKS`, `MONTHS`, `UNKNOWN`). These are comparative directions, not delivery estimates.

## Capability validation and assumptions

For each unknown product ability, record the system, capability, why it matters, `YES`/`NO`/`UNKNOWN` status, evidence, and validation method. Suitable methods include official vendor documentation, a customer admin demonstration, a bounded support question, a sandbox/test, or implementation-partner input. `UNKNOWN` never means `NO`; it means **capability validation required**, not “build custom.” Do not contact a vendor merely to complete this exercise.

Keep assumptions explicit with consequence, evidence, validation, and status. The option with the most consequential untested assumptions is usually not ready for commitment.

## Process and policy are design inputs

Not every improvement is technical. A legitimate rule may require manual intervention; removing it is not automatically improvement. Conversely, if policy only requires managers for exceptions, a routine path might change operationally. Include that change within configure, leave-alone, or another alternative. The hierarchy classifies technology intervention, so it needs no sixth process-only path.

## Alternatives before recommendation

Compare at least two plausible alternatives whenever practical. Alternatives need not all be viable. Record path, coverage, workflow/system/behavior change, relative complexity/cost/time, operating burden, dependencies, risks, assumptions, limitations, questions, evidence, and status. Statuses are `PREFERRED`, `VIABLE_ALTERNATIVE`, `NEEDS_VALIDATION`, `NOT_RECOMMENDED`, and `DISQUALIFIED`. Opportunity outcomes are `PREFERRED_PATH_IDENTIFIED`, `CAPABILITY_VALIDATION_REQUIRED`, `MORE_SOLUTION_RESEARCH_REQUIRED`, `LEAVE_ALONE`, and `DECLINE`.

## Custom-build justification gate

A confident custom-build direction normally requires evidence that:

1. the problem is qualified;
2. burden is meaningful;
3. configuration is inadequate;
4. integration cannot reasonably supply the capability;
5. automation alone is inadequate;
6. legitimate policy and constraints can be met;
7. the organization can own and support the result;
8. expected value may justify cost and risk; and
9. delivery is plausible.

Incomplete certainty is acceptable during research, but major unsupported assumptions block confident recommendation. “We want an app/AI/control,” “our competitor has one,” “our website looks old,” “we hate our vendor,” “it would be cool,” or “everything should be in one system” may begin inquiry but do not pass this gate.

## Why this precedes deeper economics

Selection first identifies plausible forms of response without pretending to know technical scope or price. Chapter 13 can then ask whether a proposed solution creates enough recoverable value for its cost and risk. Chapter 12 calculates no ROI, produces no proposal, and makes no detailed implementation estimate.
