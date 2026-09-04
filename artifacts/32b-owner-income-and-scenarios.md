# Chapter 32B — Owner income and scenarios

> **FICTIONAL SIMULATION ONLY.** These are fictional simulation outputs and not
> real-world probabilities or financial results. No final Chapter 32 verdict is made.

## Baseline owner economics

| | Revenue | Contribution | Owner draw | Owner hours | Draw/hour | Minimum cash after draw | Overload months |
|---|---:|---:|---:|---:|---:|---:|---:|
| Year 1 | $144,623 | $58,623 | $21,865 | 373 | $59 | $1,542 | 0 |
| Year 2 | $153,838 | $71,768 | $99,773 | 628 | $159 | $17,736 | 0 |
| Year 3 | $186,235 | $83,028 | $71,868 | 733 | $98 | $15,849 | 0 |

Revenue, contribution, engine cash, reserve-preserving draw, and contribution
per owner hour are different measures. Draw/hour is not economic profit/hour.

## Owner-income targets and stability

The Year 3 states are: $50,000 `ACHIEVED_BUT_UNSTABLE`; $75,000, $100,000,
and $125,000 `NOT_ACHIEVED`. There are 8 zero-draw months and 19 months below
the $75,000/12 equivalent. Monthly draws range from $0 to $10,000; simulated
standard deviation is $3,933 and stability is `VOLATILE`.

Reserve-first preserves a $12,000 minimum plus the next $2,850 overhead before
making 50% of eligible cash available, capped at $10,000 per month. It does not
transfer all excess cash. This is not tax, accounting, legal, or financial advice.

## Scenarios

| Scenario | 36-month revenue | Contribution | Y1 / Y2 / Y3 draw | Minimum post-draw cash | Average hours/week | Overload | Primary bottleneck |
|---|---:|---:|---:|---:|---:|---:|---|
| Baseline | $484,696 | $213,418 | $21,865 / $99,773 / $71,868 | $1,542 | 11.1 | 0 | Cash |
| Conservative | $288,918 | $118,923 | $0 / $40,074 / $46,381 | -$7,792 | 9.2 | 0 | Cash |
| Optimistic | $866,835 | $381,517 | $36,858 / $119,098 / $120,000 | $4,537 | 14.3 | 0 | Cash |
| Stress | $250,138 | $81,838 | $0 / $15,566 / $34,243 | -$15,276 | 6.0 | 0 | Cash |
| Rapid growth | $1,618,560 | $695,663 | $55,199 / $120,000 / $120,000 | $5,950 | 21.0 | 1 | Owner capacity |
| Low demand | $208,013 | $92,040 | $0 / $6,872 / $20,853 | -$8,425 | 6.1 | 0 | Demand |
| Low price | $387,861 | $93,288 | $2,955 / $34,466 / $68,607 | -$6,800 | 10.6 | 0 | Economics |
| High support burden | $598,595 | $254,166 | $21,865 / $99,338 / $105,835 | $1,542 | 13.2 | 0 | Support |
| Cash stress | $448,329 | $177,642 | $0 / $35,948 / $72,324 | -$33,958 | 10.5 | 0 | Cash |
| Partner failure | $490,309 | $206,509 | $21,570 / $83,420 / $104,654 | $1,542 | 7.5 | 0 | Partner capacity |
| Customer concentration | $435,905 | $263,255 | $23,096 / $103,923 / $85,717 | $1,695 | 8.9 | 0 | Concentration |
| Owner absence | $534,373 | $234,024 | $21,865 / $101,589 / $120,000 | $1,542 | 11.7 | 1 | Owner capacity |

Each scenario still uses finite 32A acquisition, project-start, delivery,
support, incident, expansion, churn, cash, and workload behavior.

## Break even

- Qualified opportunities: **6.23/month** at current downstream rates.
- Sales: **15.38/year** for a selected $75,000 draw target plus fixed overhead.
- Average project contribution: **$18,439** at modeled expected sales.
- Maximum owner effort: **83.5 hours/project** at the configured owner-time threshold.
- Maximum support burden: **6.1 owner hours/customer/month** before support margin is consumed.
- Cash requirement: approximately **$26,130 opening cash**, holding timing constant.

These thresholds are conditional arithmetic, not recommended commercial terms.

## Sensitivity

Year 3 draw range ranks: (1) close rate $66,103; (2) project price $51,116;
(3) delivery cost $50,268; (4) qualified rate $14,224; and (5) monthly lead
volume $8,496. Other tested assumptions are support price, payment delay,
expansion rate, incident rate, project owner hours, and routine support hours.
The ordering is calculated, not hardcoded, and indicates validation priority.

## Monte Carlo

Runs: **500**. Seed: **3202**. Year 3 draw P10 / P50 / P90:
**$66,010 / $109,213 / $120,000**. Simulation-frequency cash remains
nonnegative: **65.4%**; selected $75,000 target achieved: **83.2%**; overload:
**0.0%**; working capital required: **34.6%**; concentration threshold exceeded:
**95.0%**.

These are **SIMULATION FREQUENCIES UNDER ASSUMPTIONS**. They describe these 500
configured draws; they do not mean Local Works has those real-world chances.

## Operating models and capacity modes

- Project only: $201,693 contribution; $95,947 Year 3 draw; 10.3 hours/week.
- Pay as you go: $239,525; $118,272; 11.2 hours/week.
- Light support: $256,926; $118,061; 11.7 hours/week.
- Managed support: $282,741; $113,900; 12.6 hours/week.
- Mixed model: $213,418; $71,868; 11.1 hours/week.

Side business is `NOT_PLAUSIBLE`, part time is `PLAUSIBLE_WITH_LIMITS`, and full
time is `PLAUSIBLE` under configured capacity checks. These are model
classifications, not personal recommendations; no model is declared the winner.

## Business-design lever

Before: low price produces $93,288 contribution and $68,607 Year 3 draw. Change:
raise average project price 15%. After: contribution becomes $152,303, while Year
3 draw becomes $49,194 because start/cash timing also changes. Lead volume,
conversion, delivery cost, support scope, and capacity do not magically change.
The lever improves contribution, but plainly does not improve every outcome.

## Bottlenecks and evolution

Scenario-specific bottlenecks appear in the table. Baseline evolves from cash
(months 1–20) to delivery (months 21–36). Rapid growth evolves from cash
(months 1–8), to delivery (months 9–20), to owner capacity (months 21–36).
These results are evidence inputs for 32C—not a final verdict.
