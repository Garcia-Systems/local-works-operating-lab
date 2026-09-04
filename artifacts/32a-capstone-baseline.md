# Chapter 32A — capstone baseline

> **FICTIONAL SIMULATION ONLY**  
> All financial, customer, conversion, workload, and operating results are fictional simulation data.

## Core question

Can Local Works operate through a complete customer lifecycle over multiple years while maintaining coherent demand, sales, delivery, support, cash, and owner-capacity behavior?

This baseline exercises the engine; it is not an owner-income target result or final business verdict.

## Baseline assumptions

- **Acquisition:** 5 monthly leads at maturity; 48% qualification; 72% discovery progression; 68% proposal progression; 42% close; two-month minimum sales cycle; referral leads still qualify.
- **Projects:** $15,000 average price with 12% variation; $7,200 partner cost; $700 other direct cost; 46 owner delivery hours; three months; 40% deposit; simple delays.
- **Support:** 62% adoption; $625 monthly revenue; 2.4 routine owner hours; $105 partner cost; separate warranty, goodwill, and incident burden.
- **Expansion:** signals, qualification, proposal effort, and sale remain separate; a simulated sale is $4,800 with $1,900 direct cost.
- **Retention:** support can churn; project-complete customers may remain quiet and healthy.
- **Capacity:** 128 sustainable and 150 temporary owner hours; two concurrent projects; support and incident reserves; 100 partner hours.
- **Cash:** $14,500 opening cash; $2,850 monthly overhead; delayed final receipts; early partner deposits; $12,000 reserve target; no free financing.
- **Evidence status:** assumptions are `SIMULATION_ASSUMPTION` (or hypotheses where replaced by a future researcher). Running the model does not make them observed or measured.

## Starting state

- **Cash:** $14,500
- **Owner capacity:** 128 hours/month
- **Partner capacity:** 100 hours/month
- **Pipeline:** small startup ramp
- **Customers:** zero

## Year 1

54 leads; 25 newly qualified; 10 sales; 0 projects delivered; 0 support customers at year end; $144,623 revenue; $58,623 contribution; -$11,630 minimum cash; $49,069 ending cash; 373.2 owner hours; 0 overload months; pipeline `EXCESSIVE_FOR_CAPACITY`.

## Year 2

63 leads; 28 newly qualified; 9 sales; 4 projects delivered; 2 support customers at year end; $153,838 revenue; $71,768 contribution; $42,154 minimum cash; $153,023 ending cash; 627.6 owner hours; 0 overload months; pipeline `EXCESSIVE_FOR_CAPACITY`.

## Year 3

61 leads; 28 newly qualified; 11 sales; 4 projects delivered; 3 support customers at year end; $186,235 revenue; $83,028 contribution; $134,238 minimum cash; $216,644 ending cash; 732.9 owner hours; 0 overload months; pipeline `EXCESSIVE_FOR_CAPACITY`.

## 36-month totals

- **Revenue:** $484,696
- **Contribution:** $213,418
- **Projects:** 30 sales; 8 delivered; 1 active and 21 queued at month 36
- **Support customers:** 3 at month 36
- **Incidents:** 3
- **Expansions:** 2 sales
- **Churn:** 2 support relationships
- **Minimum cash:** -$11,630
- **Ending cash:** $216,644
- **Owner hours:** 1,733.7
- **Overload months:** 0

## Pipeline

The startup begins with no customers and a gradual lead ramp. Sales cannot close
inside the two-month minimum cycle. The final pipeline is excessive relative to
available starts: deposits and accounting contribution must not disguise the
21-project queue. Delivery-heavy work limits progression when capacity is scarce.

## Support tail

Routine paid support grows only after completions. Warranty, paid support,
goodwill, and incident hours remain distinct. The tail is bounded in this run,
but grows in later years and competes for the same finite owner capacity.

## Concentration

Month 36's largest simulated revenue/contribution/owner-hour/support shares are
approximately 4%/4%/3%/33%. Active delivery depends entirely on one primary
partner; supported customers share FictionalFlow, enabling one correlated event.

## Owner absence

Month 20 removes 32 hours for a planned one-week absence. The engine does not
assign those hours back to the owner; available capacity drops and queue/deferral
logic remains active. The month remains below capacity, which is not proof of
operational independence.

## Baseline health

- **Demand:** ACCEPTABLE
- **Sales:** ACCEPTABLE
- **Project economics:** ACCEPTABLE
- **Delivery:** MIXED
- **Support:** MIXED
- **Cash:** WEAK
- **Owner capacity:** ACCEPTABLE
- **Pipeline:** ACCEPTABLE (coverage), while volume is excessive for start capacity
- **Concentration:** ACCEPTABLE at customer level
- **Partner resilience:** WEAK

## Primary bottleneck

**CASH.** The minimum simulated position is -$11,630, so the engine raises
`WORKING_CAPITAL_REQUIRED` rather than silently treating financing as free.

Chapter 32 remains **IN PROGRESS**. Scenario analysis, owner income, break-even,
sensitivity, Monte Carlo, the final verdict, real-world validation, and production
requirements remain for 32B/32C.

