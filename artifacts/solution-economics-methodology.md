# Solution Economics Methodology

## Purpose

Solution economics asks how much supported current burden a particular alternative can realistically recover, and whether that value justifies the customer's future costs. **Current burden is not recoverable value.** Fixed costs, legitimate review, exceptions, incomplete adoption, and imperfect realization all limit recovery.

## Value and work

For each burden component, state a recoverable fraction, adoption rate, and realization factor with provenance:

`realized gross value = current burden × recoverable fraction × adoption × realization`

This is a bounded burden-recovery calculation, not permission to invent revenue. Revenue, retention, or value beyond current burden needs separate causal evidence. Document work that disappears, becomes faster, remains necessary, and is newly introduced. New administration, monitoring, exception review, permissions, support, and vendor coordination reduce the net operating benefit.

Labor value needs careful classification. **Cash savings** requires evidence that spending or payroll falls. **Freed capacity** means employed people can redirect time; an indicative loaded-labor value can describe its scale, but is not guaranteed cash. Revenue value, risk reduction, and non-monetized benefits remain separate as well.

## Costs and calculations

One-time implementation cost is separate from annual recurring cost. Implementation can include services, integration, development, migration, training, testing, and defensibly monetized customer effort. Recurring costs can include subscriptions, hosting, support, maintenance, APIs, and monitoring. Track meaningful customer internal effort even when it cannot defensibly be monetized.

- `first-year cost = implementation + first-year recurring + other attributable first-year cost`
- `annual net benefit = annual gross recoverable value − annual recurring cost − annual new operating burden`
- `payback months = implementation ÷ annual net benefit × 12`, only when net benefit is positive
- `first-year net value = first-year recoverable value − first-year solution cost`
- `simple first-year ROI = first-year net value ÷ first-year solution cost`
- `N-year cumulative value = N × annual net benefit − implementation − other first-year cost`

ROI conventions vary; this lab's formula is a transparent decision-practice simplification, not universal accounting doctrine. One-time implementation is not subtracted every year. Use a defensible useful life—three years is the training default—and flag alternatives with differing useful lives. No discounted cash-flow model is needed here.

## Scenarios and comparison

LOW is less favorable to customer value, BASELINE is a reasonable working hypothesis, and HIGH is more favorable. Change genuine uncertain drivers—volume, recovery, adoption, realization, exception work, and cost—without engineering a desired answer. A used solution can still realize less than its theoretical gain.

Compare alternatives incrementally. If configuration creates $5,000 annual value and custom creates $7,000, custom's relevant increment is $2,000, weighed against its additional cost, ownership, useful life, and risk. Prior investigation spending is sunk: future decisions compare future expected value with future expected cost.

## Evidence and guardrails

Label measured, estimated, hypothetical, preliminary, and unknown inputs. Round decision outputs reasonably. Do not provide precise ROI when implementation cost or recoverable value is unknown. Do not report payback for zero or negative annual net benefit. Exclude unsupported revenue. Do not monetize customer time silently or call capacity cash. Preliminary costs are estimates, not quotes.

Economic decisions may be **economically attractive**, **economically plausible**, **marginal**, **more evidence required**, **economically unattractive**, or **leave alone**. None is project approval. Scope, price, delivery, risk, negotiation, and authorization gates still remain.
