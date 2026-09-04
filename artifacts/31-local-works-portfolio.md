# Chapter 31 — The Local Works customer portfolio

> **FICTIONAL BUSINESS SIMULATION.** All customers, financial results, workload, cash, incidents, and portfolio outcomes are fictional simulation data.

## PORTFOLIO STARTING STATE
Six fictional relationships span audit, discovery, signed/queued, active delivery, support, and expansion. Chapter 31B reuses Chapter 31A's single portfolio rather than copying customer or capacity models.

## CUSTOMERS
Harbor Fitness has support, a severe incident, and an expansion signal; James River Kitchen is in discovery; Tidewater Home Services is active; Colonial Professional Group is supported; Peninsula Events is in audit; Old Dominion Dental is signed but queued.

## WORK INVENTORY
One inventory includes sales, discovery, QA, launch, support, incident, collection, relationship, and administrative work. The Harbor severe incident outranks routine work because impact—not customer value—sets urgency.

## OWNER CAPACITY
The weekly foundation has 40 finite hours, protected incident reserve, non-delivery work, and context-switch overhead. Monthly scenarios use 128–140 hours and expose every overload rather than silently borrowing future time.

## PIPELINE
Potential pipeline never counts as revenue. Coverage compares qualified/proposal volume with two expected delivery slots. Baseline remains adequate; conservative and late growth months reveal a cliff after delivery crowds out selling.

## DELIVERY
Signed work follows **SIGNED → QUEUED → SCHEDULED → START_AUTHORIZED → ACTIVE**. Owner, partner, cash, support reserve, and existing commitments gate starts. Excess growth is queued; partner-unavailable months authorize no new start.

## SUPPORT
Every completion adds three routine owner hours per month before scenario multipliers. Baseline grows from 2 to 8 supported customers and 6 to 24 routine hours. Growth reaches a cumulative tail that exceeds the 36-hour plan even though no customer is individually extreme.

## REVENUE MIX
The baseline produces $72,000 project, $39,000 support, and $5,000 expansion revenue: $116,000 total. Pipeline is excluded.

## CONTRIBUTION MIX
Baseline simulated contribution is $56,300 after project/support/expansion direct burden and incident cost. Contribution is reported separately from revenue and cash.

## CASH FLOW
Opening: $18,000 baseline ($7,000 stress).  
Inflows: received project deposits and support receipts.  
Outflows: partner deposits, support-partner cost, and overhead.  
Net / ending: baseline ends $31,650; stress ends $8,450.  
Minimum: baseline $11,000; stress -$3,540.  
Receivables: late project cash remains outstanding in stress.  
Committed future outflows: queued partner work is explicit.  
Maximum cash exposure: baseline $6,625; stress $12,000 (the single late receivable).  
Cash state: baseline healthy; stress becomes negative before recovering. A profitable period can therefore run out of cash.

## CONCENTRATION
Revenue: a one-sale month can be 58% largest-customer.  
Contribution: up to 63%, and not assumed equal to revenue.  
Owner hours: incident months rise to 55%.  
Support burden: declines from one-half as the base diversifies.  
Receivables: a single late project can be 100%.  
Partner: Blue Heron dependence is approximately 78% during active delivery.  
Vendor: MemberCloud reaches 67%; a shared outage creates correlated incidents.

## 12-MONTH BASELINE
| Month | Customers | Active/queued | Support | Revenue | Contribution | Ending cash | Owner h/capacity | Pipeline | Risk |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| Jan | 7 | 2/0 | 2 | $13,300 | $6,215 | $17,160 | 118/140 busy | excessive | controlled start |
| Feb | 7 | 1/0 | 3 | $1,950 | $1,073 | $16,350 | 75/140 under | excessive | support begins |
| Mar | 8 | 2/0 | 3 | $13,950 | $5,873 | $16,765 | 129/140 busy | strong | incident reserve used |
| Apr | 8 | 1/0 | 4 | $2,600 | $1,430 | $16,485 | 80/140 under | excessive | support tail |
| May | 9 | 2/0 | 4 | $14,600 | $6,930 | $17,705 | 118/140 busy | strong | controlled start |
| Jun | 9 | 1/0 | 5 | $5,750 | $3,413 | $19,955 | 81/140 under | strong | expansion |
| Jul | 10 | 2/0 | 5 | $15,250 | $6,588 | $22,475 | 134/140 busy | excessive | incident reserve used |
| Aug | 10 | 1/0 | 6 | $3,900 | $2,145 | $23,255 | 86/140 healthy | strong | support rises |
| Sep | 11 | 2/0 | 6 | $15,900 | $7,290 | $27,045 | 127/140 busy | strong | finite buffer |
| Oct | 11 | 1/0 | 7 | $7,050 | $4,128 | $31,755 | 94/140 healthy | excessive | expansion |
| Nov | 12 | 2/0 | 7 | $16,550 | $7,648 | $36,815 | 132/140 busy | strong | controlled start |
| Dec | 12 | 1/0 | 8 | $5,200 | $2,860 | $31,650 | 95/140 healthy | adequate | sales maintained |

## SCENARIOS
- **Baseline:** $116,000 revenue; $56,300 contribution; $31,650 ending cash; no overload; 6 starts/completions; 8 supported; `HEALTHY`.
- **Conservative:** $69,600 revenue; $34,080 contribution; $11,845 ending and $2,695 minimum cash; no overload; final pipeline `WEAK`; verdict `PIPELINE_WEAK`.
- **Growth:** $206,850 revenue; $90,356 contribution; $57,670 ending cash; 11 overload months and a five-project peak queue; final pipeline `WEAK`; verdict `CAPACITY_LIMITED`.
- **Stress:** $88,750 revenue; $40,521 contribution; $8,450 ending but -$3,540 minimum cash; 2 overload months; shared-vendor incidents, late receipts, partner constraint, and absence; verdict `FRAGILE`.

## COLLISION TESTS
- **Harbor incident:** severe impact consumes reserve and precedes routine support/launch work.
- **Marginal deal:** standalone `PROMISING`; portfolio decision `QUEUE` because only 10 owner hours remain. **GOOD DEAL ≠ GOOD DEAL RIGHT NOW.**
- **Cash-constrained deal:** $6,500 positive contribution, but a $9,000 partner deposit exceeds $4,000 above buffer; `DELAY_START` and conceptually restructure timing.
- **Support-overload deal:** strong price does not replace support capacity; `DEFER_START`, reprice/limit support, or decline.
- **Concentration:** sound economics may proceed with boundaries, while the increased largest-customer share remains flagged.
- **Owner absence:** three business days delay project coordination, degrade triage, defer sales follow-up, and require delegated customer communication.

## PORTFOLIO HEALTH
Pipeline: acceptable baseline, weak conservative/stress and late growth.  
Sales: acceptable baseline; mixed when delivery displaces it.  
Delivery: controlled baseline; weak growth/stress overload.  
Support: acceptable baseline; weak when the accumulated tail exceeds plan.  
Incidents: mixed because reserve is finite.  
Cash: acceptable baseline; weak stress timing.  
Concentration: mixed and measured across five distinct customer dimensions.  
Partner resilience: mixed baseline, weak during unavailability.  
Vendor risk: mixed baseline, weak under MemberCloud correlation.  
Owner capacity: acceptable baseline, weak growth.  
Quality: mixed during overload.  
Relationships: acceptable when delays and boundaries are communicated; mixed under stress.

## WEEKLY OPERATING REVIEW EXAMPLES
Normal: maintain one controlled start, preserve reserve, and keep selling. Stress: triage two correlated incidents, communicate the delayed start, delegate updates, protect cash, and do not consume reserve for routine work.

## MONTHLY BUSINESS REVIEW EXAMPLES
Normal March reports project/support separately, positive cash, 129/140 owner hours, one incident, and no queue. Overloaded growth July reports a five-project queue, cumulative support, 156/128 owner hours, incident collision, and explicit deferred work.

## FINAL VERDICT
The controlled baseline is **HEALTHY**. The same book of individually profitable work becomes **CAPACITY_LIMITED** under growth and **FRAGILE** under correlated stress. Qualifiers are finite owner/support capacity, primary-partner dependence, shared-vendor risk, cash timing, and the delayed pipeline cliff. This is the final **Chapter 31 portfolio verdict**, not the Chapter 32 owner-income or final business-viability verdict.

A portfolio must be tested through time. Maximum revenue is not the objective; coordinated sales, delivery, support, cash, quality, partners, and owner capacity are.
