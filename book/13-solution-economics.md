# Chapter 13 — Solution Economics

## Part IV — Design the Right Solution

**Core question:** Does a proposed solution recover enough of the customer's current economic burden to justify its cost, risk, complexity, and ongoing ownership?

The chain is **current burden → solution alternative → recoverable value → implementation cost → ongoing cost → economic benefit → payback/ROI → economic decision**. It is an evidence chain, not a sales argument.

## 1. Burden is not recoverable value

Chapter 10 valued current-state burden. Chapter 12 compared intervention paths. Neither number nor alternative proves a benefit. A $20,000 burden may contain fixed cost, legitimate review, unavoidable exceptions, inconvenience, and uncertain consequences. A solution that removes $8,000 has $8,000 of potential recoverable value—not $20,000.

Link every claimed benefit to a supported burden component. Value beyond that bound, such as new revenue, requires its own defensible causal evidence. Never add revenue or retention merely to rescue ROI.

## 2. What can the solution actually change?

For each alternative ask which steps disappear, become faster, stay unchanged, and are introduced. A simple delta can compare eight current employee minutes with three proposed minutes: five minutes over 1,000 requests is 5,000 minutes, or 83.33 hours of potential capacity. Every input still needs provenance.

Value mechanisms can include labor capacity, rework, errors, fees, refunds, revenue, retention, delays, third-party cost, or another supported category. A category is not evidence.

## 3. Labor savings vs freed capacity

Two hundred hours at a $25 loaded rate has an indicative labor-capacity value of $5,000. If employees remain and redirect that time, report **200 hours freed capacity** and **$5,000 indicative capacity value**. Report **cash payroll savings: NOT ESTABLISHED**. Cash savings requires an actual spending reduction. Also keep revenue value, risk reduction, and non-monetized benefit distinct.

## 4. Remaining necessary work

Harbor Fitness cannot assume full automation. Identity verification, eligibility checks, exceptions, approvals, disputed billing, and unusual memberships may still require judgment. A recoverable fraction makes that limit visible:

`current component × recoverable fraction`

A hypothetical 50% recovery from $3,200 is a hypothetical $1,600—not a measured result.

## 5. New work created by solutions

Automation exceptions, configuration upkeep, integration monitoring, support questions, permissions, rule updates, and vendor coordination consume resources. Thus $4,000 gross capacity less $800 new administration is $3,200 before recurring technology cost. Gross benefit that ignores new work is incomplete.

## 6. Implementation cost

Implementation may include Local Works services, delivery resources, setup, integration, custom development, migration, training, testing, and customer internal effort. A preliminary estimate is not a quote. Meetings, cleanup, decisions, documentation, testing, training, and rollout matter even when no defensible rate exists; track but do not silently monetize them.

## 7. Recurring cost

Keep subscriptions, automation platforms, hosting, support, maintenance, API charges, and monitoring separate from setup. A low setup cost can conceal expensive ownership; a higher setup can sometimes have lower ongoing cost. These are scenario facts, not universal characteristics of solution paths.

## 8. First-year economics

`first-year cost = implementation + first-year recurring + other attributable first-year cost`

This is the customer's attributable economic cost, not customer price or Local Works delivery cost. Pricing belongs to a later chapter.

## 9. Annual net benefit

`annual net benefit = annual gross recoverable value − annual recurring solution cost − annual new operating burden`

Do not subtract implementation every year. Keep one-time and operating economics visible.

## 10. Payback

`payback months = implementation cost ÷ annual net benefit × 12`

Calculate only when implementation and recoverable value are known and annual net benefit is positive. Zero or negative benefit means **NONE / NOT ACHIEVED**, never division by zero.

## 11. Simple ROI

This lab uses `(first-year recoverable value − first-year solution cost) ÷ first-year solution cost`. ROI conventions vary; this transparent simplification supports decision practice and is not universal accounting doctrine. Unknown cost or benefit means no precise ROI. Round reasonable outputs rather than displaying false precision.

## 12. Multi-year economics

`N-year cumulative value = N × annual net benefit − implementation − other first-year cost`

An $8,000 implementation with $6,000 annual net operating benefit yields -$2,000 after year one, +$4,000 after year two, and +$10,000 after year three. Use a defensible useful life. Three years is enough for training; vendor, API, process, replacement, growth, maintenance, and deprecation risks make automatic ten-year benefits misleading. Flag comparisons with different useful lives.

## 13. Adoption and realization

Eligibility is not usage. If 60% of 1,000 requests use the improvement, only 600 are exposed to benefit. Usage is not full impact either: five theoretical minutes at 80% realization becomes four realized minutes.

`realized value = burden × recoverable fraction × adoption × realization`

Do not default either factor to 100%.

## 14. Low/base/high scenarios

LOW is less favorable realization for the customer, BASELINE is a reasonable working hypothesis, and HIGH is more favorable. Vary uncertain volume, time, recovery, adoption, exception work, implementation, and recurring cost honestly. Sensitivity shows what matters; it does not prove an outcome.

## 15. Incremental economics

If configuration recovers $5,000 and custom recovers $7,000, custom adds $2,000—not $7,000—over configuration. Compare that increment with additional implementation, recurring burden, risk, and ownership. “We already spent $15,000” is sunk-cost thinking; future decisions compare future expected value with future expected cost.

## 16. Big problem, bad solution

A fictional $100,000 annual problem does not justify a $300,000 custom system that costs $60,000 annually and recovers only $40,000. Its annual net benefit is negative before implementation recovery. **BIG PROBLEM ≠ GOOD PROJECT.**

## 17. Smaller problem, excellent solution

A fictional $8,000 burden with a $1,000 configuration and $5,000 recoverable annual value can have excellent economics. **SMALLER PROJECT can be BETTER BUSINESS.** Let the scenario decide; do not force configuration to win or custom to lose.

## 18. Harbor Fitness solution economics

The exercise reconstructs Chapter 10's $2,450 baseline direct labor burden. Under explicitly hypothetical inputs, configuration grosses $809 capacity value and nets $659 annually; integration/automation grosses $1,103 but nets $203; custom grosses $1,499 but nets negative $1,501. Leave alone costs and recovers zero while the burden continues. No cash payroll, revenue, or retention benefit is established.

Configuration's baseline payback is 18.2 months and cumulative values are -$342, +$317, and +$976 over years one through three. Integration remains negative after three years; custom has no payback. Configuration sensitivity ranges from $184 net and 84.6-month payback to $1,162 net and 8.3-month payback. These results are hypotheses, not customer ROI.

## 19. Evidence before precision

Measured, estimated, hypothetical, preliminary, and unknown inputs must remain visible. Guardrails exclude unsupported revenue, preserve non-monetized customer time, label capacity correctly, prevent payback on nonpositive benefits, and suppress ROI when key inputs are unknown. An economic state—attractive, plausible, marginal, more evidence required, unattractive, or leave alone—is not project approval.

## 20. Executable exercise

Run:

```bash
python scripts/run_chapter_13.py
```

Inspect the current burden, alternatives, recoverable components, costs, payback, cumulative results, increments, sensitivity, evidence, and decision. Then replace one hypothetical input with real evidence and explain whether the conclusion changes.

## 21. Chapter artifacts

- `artifacts/harbor_fitness/13-solution-economics.md` — completed fictional analysis
- `artifacts/solution-economics-template.md` — reusable evidence-first worksheet
- `artifacts/solution-economics-methodology.md` — formulas and guardrails
- `artifacts/production-system-discovery.md` — only capabilities revealed by operating practice

## 22. Readiness checkpoint

The reader can explain burden versus recovery; calculate recoverable labor value; distinguish capacity from cash; preserve remaining and new work; separate implementation and recurring cost; calculate annual net benefit, conditional payback, simplified ROI, and one/two/three-year value; model adoption and realization; order low/base/high scenarios; compare increments; reject unsupported revenue; and explain why attractive economics still creates neither a proposal nor project approval.

Chapter 14—not this chapter—will define what is included, excluded, assumed, and required for a manageable scope.
