# Chapter 29 — Harbor Fitness Support Economics

**FICTIONAL TRAINING RECORD**  
Customer: **Harbor Fitness**

> All support usage, prices, costs, and economics are fictional simulation assumptions.

## Current support evidence

Chapter 27 recorded eight post-launch contacts: a likely 1.5-owner-hour warranty defect; one how-to/configuration question; a new-work request; customer configuration assistance; vendor coordination; a security-sensitive incident routed onward; 0.17 owner hour/$15 of goodwill; and a disputed warranty candidate. Total owner effort was about 4.92 hours. Chapter 28 evidence is not present in this checkout, so partner effort, detailed incident effort, recurrence, and monthly/after-hours patterns below are assumptions—not observations.

## SUPPORT DEMAND PROFILE

Routine requests/month: 3 (assumption)  
Incidents/month: 0.25  
Owner hours/month: 2.5 paid/included support hours  
Partner hours/month: 0.5  
Vendor coordination: 0.5 owner hour  
After-hours: none promised; occurrence uncertain  
Goodwill: Chapter 27 recorded 0.17 owner hour and $15 internal estimate  
Warranty burden: likely defect recorded separately at 1.5 owner hours  
Uncertainty: high; short launch-period history may not represent steady state.

Work mix assumes 1.0 how-to, 0.5 configuration, 0.5 vendor coordination, 0.25 incident coordination, and 0.25 documentation owner hour. Ticket count is not used as a cost proxy.

## PLAN A

Name: Pay As You Go  
Revenue model: PAY_AS_YOU_GO  
Price: no recurring fee; expected-month illustration bills $500 after approval  
Included work: none without approval; warranty remains no-charge where applicable  
Exclusions: new workflows/integrations, redesign, large reports/training, third-party fees, discovery  
Owner capacity: not reserved; scheduled against availability  
Partner assumptions: $100/hour illustration, available with confirmation  
Incident treatment: approval unless warranty/vendor responsibility  
After-hours: not included  
Overage: not applicable; work is usage-based

### EXPECTED ECONOMICS
Monthly revenue: $500  
Partner cost: $50  
Direct cost: $25 other / $75 total  
Owner hours: 2.5  
Imputed owner-time value: $187.50 at $75/hour  
Contribution: $425  
Contribution margin: 85.0%  
Contribution after owner-time: $237.50  
Contribution per owner hour: $170

Customer advantage: low commitment. Weakness: approval friction and unpredictable spend. Local Works advantage: demand is billed; weakness: revenue and availability are less predictable.

## PLAN B

Name: Light Support  
Revenue model: MONTHLY_FLAT_FEE  
Price: $600/month, hypothetical  
Included work: how-to, limited configuration, documentation, and reasonable vendor coordination  
Exclusions: new work/integrations, redesign, large reporting/training, third-party fees, after-hours  
Owner capacity: 3 hours/month; no rollover  
Partner assumptions: 0.5 hour expected at $100/hour; excess billed with approval  
Incident treatment: business-hours triage and limited coordination  
After-hours: not included  
Overage: billable hourly with approval

### EXPECTED ECONOMICS
Monthly revenue: $600  
Partner cost: $50  
Direct cost: $50 other / $100 total  
Owner hours: 2.5  
Imputed owner-time value: $187.50  
Contribution: $500  
Contribution margin: 83.3%  
Contribution after owner-time: $312.50  
Contribution per owner hour: $200

## PLAN C

Name: Managed Support  
Revenue model: HYBRID  
Price: $1,050/month, hypothetical; material partner/new work quoted separately  
Included work: broader routine support, business-hours incident coordination, documentation, limited configuration, and periodic review  
Exclusions: new workflows/integrations, redesign, large reports/training, third-party fees, 24/7 coverage  
Owner capacity: 6 hours/month; no rollover  
Partner assumptions: 1 hour expected at $100/hour; availability must be confirmed  
Incident treatment: prioritized business-hours coordination, not guaranteed resolution  
After-hours: separately approved, not promised  
Overage: quote required

### EXPECTED ECONOMICS
Monthly revenue: $1,050  
Partner cost: $100  
Direct cost: $50 other / $150 total  
Owner hours: 4.5  
Imputed owner-time value: $337.50  
Contribution: $900  
Contribution margin: 85.7%  
Contribution after owner-time: $562.50  
Contribution per owner hour: $200

## BREAK-EVEN ANALYSIS

| Plan | Owner-hour break-even | Partner-cost break-even | Usage break-even |
|---|---:|---:|---|
| PAYG illustration | 5.67 h | 4.25 h at $100/h | Depends on request mix |
| Light | 6.67 h | 5.00 h at $100/h | Depends on owner/partner mix |
| Managed | 12.00 h | 9.00 h at $100/h | Depends on owner/partner mix |

These are sensitivities, not promised allowances or precision forecasts.

## STRESS TESTS — LIGHT PLAN

| Case | Revenue | Direct cost | Owner hours | Contribution | Capacity | Verdict |
|---|---:|---:|---:|---:|---|---|
| Normal | $600 | $100 | 2.5 | $500 | HEALTHY | VIABLE |
| Busy | $600 | $150 | 5 | $450 | HEALTHY | VIABLE |
| Vendor incident | $600 | $200 | 6 | $400 | HEALTHY | NOT_ECONOMICALLY_SENSIBLE after owner time |
| After-hours | $600 | $275 | 7 | $325 | HEALTHY but no after-hours promise | NOT_ECONOMICALLY_SENSIBLE / boundary failure |
| Partner unavailable | $600 | planned $150 | 4 | $450 apparent | HEALTHY | NOT_OPERATIONALLY_SUSTAINABLE |
| Double demand | $600 | $250 | 10 | $350 | HEALTHY portfolio signal | NOT_ECONOMICALLY_SENSIBLE |

Portfolio capacity assumption: 20 owner hours/month with 5 reserved for incidents. Expected Light demand uses 12.5% of total and leaves reserve intact. A full portfolio—not Harbor alone—must survive concurrency.

## CUSTOMER VALUE

Potential value: a known point of contact, quicker business-hours routing, less internal diagnosis, vendor help, documentation continuity, and predictable base cost. A light documentation check can be preventive if it reflects real changes. Harbor has not validated willingness to pay or the value of availability. Low usage alone would create a weak “what am I paying for?” plan.

Weaknesses: limited history, vendor/partner dependence, no proven recurring preventive need, and possible approval/value mismatch. No fear-based or 24/7 claim is justified.

## GOODWILL, WARRANTY, AND VENDOR BURDEN

Goodwill remains occasional at 0.17 hour in Chapter 27, but recurrence would indicate an unpaid plan. The 1.5-hour likely warranty defect remains outside support revenue and may be a quality signal if repeated. Vendor coordination is assumed at 0.5 owner hour/month and is real cost even if the vendor fixes its platform without charge.

Illustrative concentration across a future portfolio must compare both revenue and burden: a customer with 20% of revenue but 60% of owner hours needs review before averages hide it.

## ANNUAL SIMULATION

Twelve lumpy Light-plan months use owner hours `[2,3,7,1,4,2,5,2,3,8,1,4]`, partner hours `[.25,.5,1.5,.25,.75,.5,1,.25,.5,2,.25,.75]`, and six incidents. Results: $7,200 revenue; $1,450 direct cost; 42 owner hours; $5,750 contribution; and $2,600 contribution after owner time. This simulation does not turn short history into a forecast.

## SUPPORT VERDICT

**PAY_AS_YOU_GO_BETTER**, for now. PAYG best matches sparse evidence and avoids manufacturing MRR. A bounded Light plan is the next candidate if Harbor validates continuity value and demand stabilizes. Managed support appears premature.

## ASSUMPTIONS THAT WOULD CHANGE VERDICT

Light could become **VIABLE_WITH_BOUNDARIES** if demand remains at or below roughly three owner hours, partner coverage is reliable, after-hours remains excluded, Harbor values predictable continuity, and preventive work is demonstrably useful. Higher incident/vendor effort, unavailable partners, concurrent customer incidents, repeated goodwill, or 24/7 expectations favor PAYG, vendor-led support, lower scope, higher fair pricing, or no ongoing plan.
