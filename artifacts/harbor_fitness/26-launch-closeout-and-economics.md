# Harbor Fitness — launch, closeout, and economics

**FICTIONAL TRAINING RECORD**  
**Business:** Harbor Fitness  
**Project:** Membership-freeze configuration and technical validation  
**Scope version:** HF-SCOPE-14-v1 (cancellation excluded)  
**Requirements baseline:** HF-REQ-21-v1  
**Acceptance result:** ACCEPTED_WITH_KNOWN_ISSUES on fictional 2026-09-19; HF-D01 passed retest and HF-D02 cosmetic copy remained disclosed.

## LAUNCH

**Launch type:** CONFIGURE—controlled activation of accepted existing-platform settings, not custom infrastructure.  
**Planned launch:** 2026-09-22, during staffed operating hours.  
**Simulated actual launch:** 2026-09-22.  
**Launch owner:** Harbor authorizes; fictional delivery partner activates; Local Works communicates.  
**Verification owner:** Local Works with Harbor operations.  
**Rollback/reversal approach:** AVAILABLE/MANUAL—record previous settings, restore them, pause the configured path, and return staff to the prior manual process. Shared Harbor/Local Works rollback decision.  
**Launch readiness:** READY_WITH_MONITORED_RISKS. Acceptance, access, responsible people, configuration steps, prior-state record, vendor availability, verification, communication, and escalation path are ready. HF-D02 is documented and nonblocking.  
**Production verification:** PASS—fictional synthetic standard and exception paths route correctly; disposition/status is visible; unauthorized approval is refused; confirmation is delivered; no obvious duplicate processing; staff can see the next step. This is a critical production check, not a complete QA rerun.  
**Launch issues:** One fictional confirmation used the older awkward wording. LOW/cosmetic, no workflow or data impact; `CONTINUE_WITH_FIX`, correct copy and recheck, communicate known impact. No rollback. A hypothetical wrong-member update did **not** occur; it would justify PAUSE/ROLLBACK because of data integrity.  
**Stabilization result:** STABLE after the short fictional monitoring window and copy recheck; no QA escape or severe incident.

## COMMERCIAL CLOSEOUT

**Original customer price:** $6,000  
**Approved paid changes:** $0—cancellation was deferred and copy was absorbed.  
**Credits:** $0  
**Total customer charges:** $6,000  
**Deposit/payment already received:** $3,000 simulated deposit. This advances Chapter 17's then-unreceived state for the completed-project exercise.  
**Final balance:** $3,000 = $6,000 + $0 − $0 − $3,000.  
**Final payment status:** RECEIVED_SIMULATED on 2026-09-29. No money, invoice, or collection occurred. The cancellation question was clarified from HF-SCOPE-14-v1 and CH-001: it was excluded/deferred, so payment remains due as agreed in the simulation.

## DELIVERY ECONOMICS

**Original delivery estimate:** 18 hours / preliminary $2,800 partner cost from pricing (technical estimates later exposed a range).  
**Revised estimate:** 22 hours Chapter 23 forecast / $3,000 working partner-cost forecast (assumption for closeout).  
**Simulated actual:** 25 partner hours / **$3,200 delivery cost**, including correction/retest; this final cost is an explicit Chapter 26 assumption because prior artifacts did not contain completed actual cost.  
**Other direct costs:** $400 (retained Chapter 15 assumption).  
**Delivery variance:** +7h versus original, +3h versus forecast; +$400 versus original cost and +$200 versus revised cost.

## OWNER ECONOMICS

| Activity | Hours |
|---|---:|
| Acquisition | 2 |
| Audit | 2 |
| Discovery | 3 |
| Solution design | 2 |
| Sales/proposal | 3 |
| Closing | 2 |
| Delivery coordination | 5 |
| Requirements/translation | 4 |
| Project control | 3 |
| QA | 4 |
| Change control | 2 |
| Customer communication | 1 |
| Commercial closeout | 3 |
| **Total owner hours** | **36** |

Presales through closing is 14h; delivery-through-close is 22h. At the Chapter 15 internal assumption of $75/hour, **imputed owner-time value is $2,700**.  
**Project contribution:** $2,400 = $6,000 − $3,200 − $400.  
**Contribution margin:** 40.0%.  
**Contribution after owner-time value:** −$300. Owner time is subtracted once, not also included in direct cost.  
**Contribution per owner hour:** $66.67 ($2,400 ÷ 36); this is project business yield before owner-time imputation, not an hourly wage.

## CASH FLOW

**Cash received:** $3,000 simulated deposit on 2026-09-01; $3,000 simulated final receipt on 2026-09-29.  
**Cash paid:** $1,600 partner installment on 2026-09-08; $400 direct cost on 2026-09-15; $1,600 partner balance on 2026-09-24.  
**Maximum cash exposure:** $600 after the partner balance and before final receipt (cumulative cash reached −$600).  
**Outstanding cash:** $0 after simulated final receipt. Revenue/charges and cash timing remain separate.

## CHANGE / REWORK IMPACT

- CH-001 cancellation: deferred, $0 current charge and $0 current delivery cost.
- CH-002 plus small copy adjustments: 4.0 combined absorbed hours in Chapter 24; $0 customer charge, but owner/delivery burden is reflected in actuals.
- CH-003 / HF-D01: three correction hours plus retest; $0 customer charge because it restored agreed behavior.
- HF-D02 launch copy issue: small internal correction/recheck, no automatic customer charge.
- Technical-discovery variance and rework help explain 25 actual hours against 18 original; history is not rewritten.

## CUSTOMER ECONOMICS

**Baseline:** Chapter 10's $18,600 annual current-burden estimate and Chapter 13/15's $9,600 recoverable-value hypothesis remain hypotheses; preserve underlying request volume/time evidence rather than editing it after launch.  
**Expected recoverable value:** reduced routine staff re-entry and waiting, subject to adoption, platform behavior, exceptions, and measurement.  
**Measured value:** **NOT YET ESTABLISHED**. No savings or percentage improvement is claimed.  
**Measurement plan:** baseline then 30 days (sample staff interventions and minutes/request), 60 days (compare member calls/emails and exception rate), 90 days (compare processing time and error/rework; assess persistence). Preserve convenience, clearer workflow, less frustration, and reduced uncertainty without invented dollars.  
**Current evidence status:** MEASUREMENT_PENDING.

## PROJECT SUCCESS DIMENSIONS

| Dimension | Rating | Basis |
|---|---|---|
| Scope delivery | STRONG | Accepted baseline delivered; cancellation deferred |
| Quality | ACCEPTABLE | Core defect corrected; cosmetic issue corrected after launch |
| Schedule | MIXED | Actual exceeded original and revised effort |
| Customer acceptance | STRONG | Explicit fictional acceptance evidence |
| Commercial collection | STRONG | Final receipt simulated |
| Local Works contribution | ACCEPTABLE | $2,400 / 40%, before owner time |
| Owner time | WEAK | Owner-adjusted contribution is −$300 |
| Customer value plausibility | ACCEPTABLE | Supported hypothesis, measurement pending |
| Delivery partner | ACCEPTABLE | Good correction/communication; estimate low |
| Continuity | ACCEPTABLE | Configuration record, reversal, handoff |
| Relationship | ACCEPTABLE | Clear scope resolution; no invented testimonial |

No overall magic score hides the weak owner economics.

## PARTNER PERFORMANCE

Fictional private evidence: configuration judgment and defect response were good; communication and handoff were clear; documentation enabled reversal; quality improved after HF-D01; estimate accuracy was mixed because actual reached 25h versus the 18h baseline/22h forecast. Retain this as future selection evidence, not a public rating.

## POSTMORTEM

**What worked:** configuration-first scope, traceable requirements/tests, explicit cancellation exclusion, prior-settings record, proportionate verification, and partner response to HF-D01.  
**What did not:** delivery and owner effort exceeded the economic plan; copy-version control allowed minor launch rework.  
**Estimate lessons:** preserve 18h original, 22h forecast, and 25h actual; add explicit correction/retest allowance without hiding uncertainty.  
**Scope lessons:** cancellation exclusion and objective acceptance helped; ambiguous membership-type wording caused avoidable review.  
**Partner lessons:** reward documentation and defect response; calibrate future estimates with actual configuration/retest evidence.  
**Owner-time lessons:** 14 presales hours and coordination/QA materially changed an apparently healthy 40% margin.  
**Reusable assets:** sanitized configuration checklist, routing test pattern, verification checklist, estimate lesson, and change classification. Exclude Harbor data, credentials, proprietary settings/code, and confidential policy rules.

## CASE STUDY READINESS

**MEASUREMENT_PENDING / CUSTOMER_PERMISSION_REQUIRED.** An internal summary may retain sanitized operating lessons. A public case study needs measured results, Harbor's fictional equivalent of permission, accurate attribution, and confidentiality review. No testimonial exists.

## CLOSEOUT

Launch and stabilization complete; acceptance recorded; blocker corrected; known issue disposition transferred; documentation/configuration control recorded; temporary fictional partner access marked **REVIEWED → REVOKED after handoff** (metadata only); final customer and partner payments known; actual economics recorded; 30/60/90-day value plan scheduled; warranty-versus-support boundary flagged for Chapter 27; lessons captured. Operational ownership returns to Harbor with Local Works as the stated contact path; vendor dependency remains documented.

**CLOSEOUT STATUS: MEASUREMENT_PENDING.** Operational and commercial closeout are complete while customer value awaits evidence.

**All launch, payment, cost, and outcome information is fictional simulation data. No real customer result is being claimed.**
