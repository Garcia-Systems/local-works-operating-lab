# Problem economics methodology

## Purpose and transition

Move from **audit finding → opportunity → discovery → current-state workflow → economic burden**. Start with steps, actors, frequency, active time, exceptions, and sources. Friction is not value: a dated or annoying process can be too cheap to change.

## Annualizing frequency

Record a value, unit, operating periods, evidence status, and source. A weekly model is `events/week × operating weeks/year`; use 50 when the business says 50 rather than silently using 52. Day, month, and year units work similarly.

## Labor burden and multiple roles

`annual events × active minutes/event ÷ 60 × loaded cost/hour`. Loaded cost is not merely wage; it may include payroll taxes, benefits, and other employer costs. Ask for a suitable direct assumption rather than applying a universal payroll formula. Calculate each role separately. For intermittent manager work, multiply by the manager-involvement proportion.

## Rework and errors

Expected rework is `annual events × correction rate × correction minutes ÷ 60 × loaded cost/hour`. Direct error costs can be separate only when they do not duplicate that correction labor. If rate or consequence is not established, retain `UNKNOWN`.

## Waiting, customer time, and soft burden

Elapsed waiting is not active labor: two days does not become 48 paid hours. Establish delayed service, abandonment, delayed revenue, or an SLA cost separately. Customer minutes, repeat contacts, repeated information, and physical visits describe experience burden but receive no automatic dollar value.

Hard burden includes supported labor, rework, fees, refunds, and measurable revenue loss. Soft burden includes frustration, complexity, annoyance, poor experience, and reduced flexibility. Soft does not mean unreal; it means non-monetized here.

## Revenue and retention claims

Use measured abandonment, documented missed bookings/cancellations, known uncollected charges, or a credible comparison before monetizing revenue. Dislike does not establish churn. Without evidence, revenue and retention are `UNKNOWN`, not zero and not an invented estimate.

## Evidence provenance and ranges

Every input records `MEASURED`, `ESTIMATED`, `HYPOTHETICAL`, or `UNKNOWN`, plus source and notes. Arithmetic cannot upgrade evidence: estimated inputs cannot yield a measured result. Use low/base/high inputs when uncertainty warrants it. These scenarios are transparent sensitivity analysis, not probability or proof.

## Avoiding double counting

Give each burden component a unique identity, say exactly what it includes, and mark overlapping economic events. Correction labor counted as rework is not counted again as routine labor. A $50 refund and $50 lost-revenue claim may describe one event. The executable model rejects simultaneously included components with the same overlap group.

## Economic significance gate

- `ECONOMICALLY_TRIVIAL`: supported direct burden is below the analysis's stated materiality threshold.
- `POTENTIALLY_MEANINGFUL`: magnitude warrants attention but relies on estimates/hypotheses.
- `MORE_EVIDENCE_REQUIRED`: an important amount or classification cannot yet be supported.
- `MEANINGFUL_BURDEN_ESTABLISHED`: a material burden has sufficiently strong measured evidence.

This gate does not approve work, select software, or recommend a project.

## Current burden is not recoverable value

A current burden of $10,000/year does not mean a solution recovers $10,000. Necessary work remains, costs may not be removable cash costs, freed time may only create capacity, and experience may stay non-monetized. A later analysis might support $4,000 of recoverable value—but Chapter 10 does not calculate it, solution economics, or ROI.
