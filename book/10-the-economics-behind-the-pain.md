# Chapter 10 — The Economics Behind the Pain

## 1. Annoying does not mean valuable

**Friction is not value.** Manual, repetitive, and old-fashioned work can be genuinely unpleasant yet cost too little to justify changing. Chapter 10 asks what the *current* business problem costs. It does not inflate annoyance into a sales argument.

The operating progression is now:

> Audit finding → Opportunity → Discovery → Current-state workflow → Economic burden

## 2. Start with the current workflow

For each relevant Chapter 9 step, ask how often it occurs, who actively works, for how long, and at what loaded cost. Then investigate errors, correction, manager intervention, fees, refunds, delays, abandonment, revenue, and retention. Record only supported effects; unknowns remain visible.

## 3. Annualize frequency

Normalize `PER_DAY`, `PER_WEEK`, `PER_MONTH`, or `PER_YEAR` explicitly. Twenty requests per week across 50 operating weeks means 1,000 requests/year. Do not silently substitute 52. Preserve the value, unit, operating-period assumption, status, and source.

## 4. Direct labor burden

The simplest component is:

`annual events × active minutes/event ÷ 60 × loaded labor cost/hour`

Thus `1,000 × 8 ÷ 60 × $24 = $3,200/year`. Loaded labor cost differs from wage: it may conceptually include wages, payroll taxes, benefits, and other employer labor costs. There is no universal formula in this lab; the simulation's direct cost assumption must be labeled hypothetical.

## 5. Multiple people doing work

Roles remain separate. If front desk work takes eight minutes every time and a manager spends three minutes on 25% of requests, calculate each burden, then sum non-overlapping components. Do not erase different costs and involvement by inventing an average employee.

## 6. Rework and errors

Expected rework is:

`annual events × correction rate × correction minutes ÷ 60 × loaded cost/hour`

For 1,000 events, 5%, 15 minutes, and $24, the answer is $300/year. But that answer is only hypothetical when the rate is hypothetical. Without an established rate, the answer is `UNKNOWN`, not zero.

## 7. Waiting is not labor

A two-day approval wait does not create 48 employee labor hours. Waiting may delay service or revenue, contribute to abandonment, dissatisfy customers, or violate an SLA. Each consequence needs separate evidence. Otherwise it remains operational friction, not monetary loss.

## 8. Customer inconvenience

Track customer minutes, contacts, elapsed days, repeated information, and required visits. These reveal experience burden. Do not assign a dollar rate to customer time merely to enlarge the case; keep it separate from direct business burden unless a supported financial connection exists.

## 9. The danger of invented lost revenue

A frustrating form does not prove $50,000 of loss. A revenue calculation needs evidence such as measured abandonment, known conversion differences, documented missed bookings or uncollected charges, cancellations, or a credible historical comparison. Unsupported lost revenue and retention impact are `UNKNOWN`. “Customers dislike it” does not establish “it causes 5% churn.”

## 10. Hard burden vs soft burden

Hard/quantifiable burden can include active labor, rework, known third-party fees, refunds, and measurable revenue loss. Soft/non-monetized burden includes customer or employee frustration, complexity, annoyance, poor experience, and reduced flexibility. Soft burden is real; refusing fake dollars makes the analysis more credible.

## 11. Evidence provenance

Each economic input has a name, value, unit, evidence status, source, and notes. Status is `MEASURED`, `ESTIMATED`, `HYPOTHETICAL`, or `UNKNOWN`. A result inherits uncertainty: arithmetic on estimates cannot produce a measured result. An unknown required input produces an unknown estimate rather than a convenient zero.

## 12. Low/base/high scenarios

Ranges expose sensitivity without false precision. Calculate `LOW`, `BASELINE`, and `HIGH` from explicit combinations such as 15–25 weekly requests and 4–6 minutes. Ensure results are ordered when inputs justify that order. This is sensitivity analysis, not proof and not Monte Carlo analysis.

## 13. Avoid double counting

Say what every component includes. If ten correction minutes are in `REWORK`, do not repeat them in routine `LABOR`. A $50 refund and $50 lost-revenue entry may be the same event. Unique component identities and overlap groups in the model stop simultaneously included duplicates; human explanation remains essential.

## 14. The economically trivial problem

A task performed twice per year for ten minutes at $30/hour costs `2 × 10 ÷ 60 × $30 = $10/year`. Automation is possible. Economically, **leave it alone**. This conclusion is useful, not a failed sale.

## 15. The high-frequency problem

A fictional home-services company re-enters information 500 times/month. At six minutes and a hypothetical $28 loaded cost, direct annual burden is `500 × 12 × 6 ÷ 60 × $28 = $16,800`. Frequency makes small events material. This deserves more analysis, but does not automatically justify custom software—or any solution.

## 16. Harbor Fitness economics

Harbor Fitness remains fictional. Chapter 9 describes a partially validated membership-freeze workflow and unknown timing. Chapter 10 uses estimated 15/20/25 weekly requests, 50 hypothetical operating weeks, estimated front-desk time of 4/5/6 minutes at a hypothetical $24/hour, and estimated manager involvement of 15%/25%/35% for 2/3/5 minutes at a hypothetical $36/hour.

Direct labor is $1,335 low, $2,450 baseline, and $4,312.50 high. Customer effort and waiting remain non-monetized. Rework, errors, refunds, revenue, retention, and delay consequences remain unknown and excluded. The gate is `MORE_EVIDENCE_REQUIRED`: these numbers are neither measured results nor a project recommendation. The surprisingly modest baseline is a valid finding.

## 17. Burden is not recoverable value

**Current burden is not recoverable value.** If current burden is $10,000/year, a later solution might recover only $4,000: necessary work remains, costs cannot always be eliminated, freed capacity is not automatically cash savings, and inconvenience may not be monetizable. Chapter 10 does not calculate recoverable value, future state, solution value, ROI, price, or delivery economics.

## 18. Executable exercise

Run:

```bash
python scripts/run_chapter_10.py
```

The eleven sections explain vocabulary, arithmetic, roles, rework, waiting, unknown revenue, scenarios, tiny and larger examples, Harbor Fitness, and interpretation.

## 19. Chapter artifacts

- `artifacts/problem-economics-template.md` — reusable customer worksheet.
- `artifacts/problem-economics-methodology.md` — calculation and evidence rules.
- `artifacts/harbor_fitness/10-problem-economics.md` — fictional worked analysis.
- `artifacts/production-system-discovery.md` — only production needs observed through this exercise.

## 20. Readiness checkpoint

The reader should now be able to:

- convert workflow frequency into annual volume;
- calculate labor burden by multiple roles and percentage involvement;
- calculate supported rework burden;
- distinguish active labor from waiting and customer time;
- preserve measured, estimated, hypothetical, and unknown inputs;
- leave unsupported revenue and retention unknown;
- separate hard from soft burden;
- detect and prevent double counting;
- interpret low/base/high sensitivity;
- identify economically trivial friction; and
- explain why current burden is not recoverable value.

Proceed only when the current burden is represented honestly. Do not proceed to solution economics merely because a workflow is annoying.
