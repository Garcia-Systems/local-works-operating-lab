# Customer Acquisition Economics

> **Status:** Chapter 5 training model. Every number below is a hypothetical assumption, not observed Local Works performance. Simulated customers and CAC are not real customers or CAC.

## 1. CAC definitions

There is no single universally correct CAC definition; different views answer different management questions.

- **Cash acquisition cost** is attributable cash spending: advertising, events, travel, tools, content production, or outsourced marketing as applicable.
- **Cash CAC** = total acquisition cash spending / customers acquired.
- **Owner hours** record acquisition work separately.
- **Owner time cost** = acquisition hours × an assumed owner-hour value.
- **Fully loaded acquisition cost** = cash acquisition spending + owner time cost + other attributable acquisition expenses. In the executable model, attributable expenses are recorded as cash cost items rather than silently added.
- **Fully loaded CAC** = fully loaded acquisition cost / customers acquired.
- **Owner hours per acquired customer** = acquisition owner hours / customers acquired.

These measures are analytical views, not audited accounting policy. Owner-hour value represents a hypothetical opportunity-cost lens, not an owner salary recommendation.

## 2. Cash versus fully loaded CAC

A hypothetical no-ad-spend channel using 40 owner hours to acquire one simulated customer has cash CAC of $0, but not zero acquisition cost. At $25, $50, $75, and $100 per owner hour, its hypothetical fully loaded CAC is respectively $1,000, $2,000, $3,000, and $4,000. A hypothetical paid channel spending $600 and using eight hours has fully loaded CAC of $800, $1,000, $1,200, and $1,400. Valuing time reverses the cash-only ranking, and the size of the difference changes substantially as the assumption changes. Other channel cost structures can cross at other assumed values. Neither result validates a channel.

## 3. Owner-time methodology

Record research, personalized outreach, networking, lead review, qualification, pre-engagement discovery, and attributable proposal preparation when they occur. Use activity count × minutes per activity, retain the evidence label, and avoid forcing irrelevant activities into a channel. Example-only assumptions include 15 minutes per prospect research, 10 per personalized outreach or lead review, 20 per qualification, 60 per discovery, and 90 per proposal. Actual time must eventually come from contemporaneous logs.

## 4. Zero-customer handling

If a hypothetical month consumes $500 and 20 owner hours but acquires zero customers, all costs remain real within the scenario while CAC, fully loaded CAC, and hours per customer are **undefined**, not $0. The model returns `None` and never divides by zero. Zero sales is an outcome requiring interpretation, not proof that every prospect or channel is bad.

## 5. Period versus cumulative economics

A second hypothetical month might consume another $250 and six hours and acquire one simulated customer. At an assumed $50/hour, that month alone shows $550 fully loaded CAC. The cumulative two-month view shows $750 cash plus $1,300 time cost: $2,050 fully loaded CAC. Failed attempts belong to acquisition economics; measuring only the interaction that bought understates investment.

## 6. Cost per funnel stage

Chapter 5 consumes Chapter 4 `FunnelResult` data. For exposure, visit, audit start/completion, lead, qualified lead, discovery, proposal, or sale, cost per outcome is total period cost divided by that stage's meaningful count. A zero count produces an undefined result. Simulated funnel provenance and its notice flow into every stage-cost row.

This arithmetic can show how low-cost traffic could become an expensive sale, or how costly leads could yield reasonable CAC when sufficiently qualified. Neither outcome is claimed typical.

## 7. Channel hypotheses

| Channel | Possible cash structure | Possible owner-time structure | Important unknown |
|---|---|---|---|
| Personalized public-friction outreach | Very low cash | Research and personalization | Reach and trust |
| Local networking | Events, membership, travel | Attendance and relationship delay | Attribution |
| LinkedIn relationship building | Low/moderate | Content and outreach | Attribution and response |
| Outbound email | Tools/data | Research and larger-volume outreach | Trust and qualification |
| Educational content / SEO | Production expense | Significant up-front creation | Lag and durable exposure |
| Paid social | Advertising and creative | Landing-page and review effort | Qualification |
| Paid search | Potentially costly clicks | Keyword/offer management | Intent and offer dependence |
| Referral | Low direct cash | Earlier relationship investment | Availability and scalability |

These are cost-structure hypotheses, not rankings. No winner is declared.

## 8. Owner-hour sensitivity

Recalculate each channel at multiple training assumptions, such as $25, $50, $75, and $100 per hour. Report cash and hours beside loaded cost so the assumed valuation never masquerades as measured cash. Sensitivity reveals which conclusions depend on owner-time valuation; it does not determine what the owner should earn.

## 9. Major uncertainties

Unknowns include actual response and conversion rates; acquisition attribution windows; time by activity; which expenses are attributable; click, event, tool, and creative costs; lead quality; customer quality; delayed content/referral effects; and contribution from an eventual engagement. UNKNOWN is not BAD, and simulated output is not evidence.

## 10. Measurements required from real activity

Local Works would eventually need dated channel/source, period and cohort, attributable cash by category, owner activity duration, stage counts and timestamps, qualification outcomes, sale status, attribution reasoning, and evidence provenance. Definitions and allocation rules should be stated consistently while allowing management views to differ.

## 11. CAC and customer contribution

CAC is necessary but insufficient. A hypothetical $1,000 fully loaded CAC paired later with $4,000 contribution before overhead may be plausible under those assumptions; paired with $500 it cannot be justified under those assumptions. This is only a conceptual payback preview. Chapter 5 neither models contribution nor invents Local Works lifetime value. The future dependency is:

**Acquisition Economics must eventually be compared against Customer Economic Contribution.**
