# Chapter 5 — Customer Acquisition Economics

> All numerical scenarios in this chapter are **hypothetical training assumptions**. Local Works has no real acquisition data. Simulated customers are not customers, simulated CAC is not Local Works CAC, and assumed costs, time values, and conversion rates are not evidence.

## 1. Leads are not free

Chapter 3 introduced possible channels and Chapter 4 followed people through channel-specific funnels. Neither lead volume nor a simulated sale answers the economic question: **what did Local Works spend, in money and owner effort, to acquire the customer?** Acquisition includes attempts that fail. This chapter connects cost inputs to the existing funnel without validating a channel or recommending a marketing budget.

## 2. Cash CAC

The simplest view is:

```text
Cash CAC = total attributable acquisition cash spending / customers acquired
```

Cash may include advertising, networking fees, attributable travel or mileage, prospecting tools, content production, and outsourced marketing. Not every channel needs every category. Clear attribution rules matter. Cash CAC answers a useful liquidity question, but it can badly understate the burden on an owner-operated professional-services business.

There is no universally correct CAC definition for every management purpose. The important practice is to name the view, state its boundary, and compare like with like.

## 3. The hidden cost of owner time

Research, outreach, networking, lead review, qualification, pre-engagement discovery, and proposal work consume capacity. Record them as hours even when no money changes hands:

```text
Owner time cost = owner acquisition hours × assumed owner-hour value
```

The value is an opportunity-cost hypothesis—not a declaration of salary or what the owner should earn. The exercise uses $25, $50, $75, and $100 per hour only to expose sensitivity.

## 4. Fully loaded CAC

```text
Fully loaded acquisition cost = cash acquisition spending
                              + owner time cost
                              + other attributable acquisition expenses

Fully loaded CAC = fully loaded acquisition cost / customers acquired
Owner hours per customer = owner acquisition hours / customers acquired
```

The model records other attributable expenses as categorized cash items, avoiding an invisible plug. Chapter 5 keeps three views visible: cash CAC, owner hours per customer, and fully loaded CAC.

## 5. What happens when nobody buys?

Suppose a hypothetical Month 1 spends $500 and 20 owner hours but acquires nobody. Cash CAC is not $0. Its denominator is zero, so CAC and hours per customer are undefined—not meaningfully calculable. The investment still exists. Python represents these ratios as `None`, never divides by zero, and reports the reason.

This preserves a related principle from earlier chapters: zero sales needs investigation. It is not automatic proof that a prospect, channel, or business is bad.

## 6. Period versus cumulative economics

Now suppose Month 2 adds $250 and six hours and produces one simulated customer. At a hypothetical $50/hour, Month 2 alone appears to cost $550 fully loaded. Across both months, cash is $750 and time cost is $1,300, for cumulative fully loaded CAC of $2,050. Looking only at the prospect who bought erases the unsuccessful work that made up acquisition economics.

Period views help locate changes; cumulative/cohort views answer what the acquisition effort has cost so far. Both need explicit boundaries and attribution.

## 7. Cost through the funnel

Chapter 5 uses Chapter 4's `FunnelResult`, rather than inventing an incompatible funnel. It divides cash and fully loaded cost by a meaningful count at each available stage: exposure, website visit, audit completion, lead, qualified lead, discovery, proposal, and sale. A zero stage count returns undefined.

A hypothetical $500 campaign could yield 1,000 visits, 100 starts, 40 completions, 10 qualified leads, four discoveries, two proposals, and one simulated sale. Cost looks small per visit and large per sale. Conversely, expensive leads could still yield reasonable CAC if qualification and progression were strong. These are possibilities, not typical outcomes. When the funnel is simulated, every derived stage-cost record preserves `is_simulated`, the hypothesis evidence type, and “SIMULATED OUTPUT IS NOT OBSERVED EVIDENCE.”

## 8. Comparing acquisition channels

Potential structures differ:

- **Personalized public-friction outreach:** little cash, intensive research/personalization, limited reachable volume.
- **Local networking:** event, membership, and travel cash; substantial time and relationship delay.
- **LinkedIn relationship building:** low/moderate cash, content/outreach time, uncertain attribution.
- **Outbound email:** tools/data and research time; more volume but a trust challenge.
- **Educational content / SEO:** substantial up-front creation, low immediate volume, potentially durable exposure.
- **Paid social:** advertising, creative, and landing-page work; fast feedback is possible while qualification is uncertain.
- **Paid search:** potentially strong intent and expensive clicks, dependent on keywords and offer.
- **Referral:** little direct cash, but relationship cost occurred earlier and supply may be hard to scale.

The executable comparison returns parallel measurements and deliberately has no “winner” field. Customer quality, uncertainty, attribution, and eventual contribution prevent responsible selection from these inputs alone.

## 9. Why “free marketing” can be expensive

Compare hypothetical Channel A at $0 cash, 40 hours, and one simulated customer with Channel B at $600 cash, eight hours, and one simulated customer. At $25/hour their fully loaded costs are $1,000 and $800; at $100/hour they are $4,000 and $1,400. Zero ad spend plainly does not mean zero acquisition cost.

## 10. Why paid marketing can sometimes be economically sensible

Paid activity buys reach or learning speed while potentially conserving owner time. Under some assumptions that trade can be sensible; under others, weak qualification can compound cash and time waste. This chapter makes no claim that paid media works for Local Works and recommends no budget.

## 11. Lead quality and owner workload

Example-only assumptions—15 minutes of prospect research, 10 minutes of personalized outreach, 10 minutes of lead review, 20 minutes of qualification, 60 minutes of discovery, and 90 minutes of proposal preparation—make hidden capacity visible. Many weak leads may impose more qualification and discovery time than fewer stronger leads. Cheap traffic can therefore create costly downstream work. Real activity timing is required before acting on the result.

## 12. CAC is not enough

A $300 CAC tied to a tiny, difficult engagement is not automatically better than $900 tied to a healthy, profitable account. Chapter 5 does not implement lifetime value or contribution. It only names the dependency:

> **Acquisition Economics must eventually be compared against Customer Economic Contribution.**

For conceptual payback only, hypothetical $1,000 fully loaded CAC against future $4,000 contribution before overhead might be plausible. Against $500 contribution it cannot be justified under those assumptions. Neither example predicts Local Works results.

## 13. Harbor Fitness acquisition investment

Harbor Fitness is fictional and has not reached sale. The case records $5 hypothetical cash and 5.75 hypothetical owner hours across public research, observation preparation, outreach, response handling, audit review, and qualification. These are **acquisition investment to date**, not CAC. Customer acquired: no. CAC: not applicable.

## 14. Executable exercise

Run `python scripts/run_chapter_05.py`. Nine sections define vocabulary, expose the cost of “free” acquisition, test owner-hour sensitivity, handle a zero-customer month, compare period and cumulative results, calculate cost through a simulated funnel, compare channel structures without selecting a winner, show lead-quality workload, and ask interpretation questions.

## 15. What Local Works eventually needs to measure

Real activity must supply dated source/channel and cohort, attributable cash by category, owner minutes by activity and stage, funnel counts and timing, qualification outcomes, acquired customers, attribution choices, and evidence provenance. Later engagement economics must supply customer contribution. Until then, costs, conversions, time values, delayed effects, and customer quality remain hypotheses or unknowns—not bad facts.

## 16. Chapter artifacts

- `artifacts/customer-acquisition-economics.md` — definitions, methodology, sensitivities, channel hypotheses, and measurement needs.
- `artifacts/harbor_fitness/05-acquisition-economics.md` — fictional investment-to-date record without premature CAC.
- `artifacts/production-system-discovery.md` — restrained operational needs surfaced by the exercise.

## 17. Readiness checkpoint

The reader should be able to explain:

- why $0 ad spend does not mean $0 acquisition cost;
- cash CAC versus fully loaded CAC;
- why zero customers must not produce CAC of $0;
- why unsuccessful attempts belong in acquisition economics;
- why owner-hour assumptions can alter channel comparisons;
- why cheap leads can create expensive downstream work;
- why CAC cannot be judged without eventual customer contribution; and
- why simulation results are not evidence.

Chapter 5 ends here. Customer lifetime value, pricing, contribution, proposals, negotiation, delivery-partner economics, recurring/support revenue, owner salary, and full profitability remain intentionally deferred.
