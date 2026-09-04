# Chapter 31 — The Local Works Customer Portfolio

> **Fictional training chapter.** Every customer, amount, workload, incident, and result is simulated.

A portfolio must be tested through time. A healthy snapshot can hide tomorrow’s cash, capacity, support, dependency, or pipeline failure.

## 1. From one customer to a portfolio

Chapter 31A assembled fictional customers and all open work into one weekly operating view. Chapter 31B asks whether that same portfolio stays coherent through twelve months.

## 2. Why profitable deals can create a bad business

A deal can contribute positively yet collide with cash, starts, support, partner availability, or owner attention. Local optimization is not portfolio health.

## 3. Portfolio customer states

Lead, audit, qualified, discovery, proposal, signed, queued, active delivery, launch, support, expansion, and dormant states coexist. The simulation aggregates movement without inventing a CRM.

## 4. Unified work inventory

Sales, delivery, support, incidents, collection, relationship, and admin share one inventory. Customer size never determines urgency.

## 5. Urgency vs importance

Stopped operations and severe incidents lead; imminent commitments, dependencies, and cash risk follow. Important marketing and sales still need protected capacity.

## 6. Owner capacity

Owner time is finite and includes planned, unplanned, reserved, and switching hours. Required time over sustainable time is visible overload.

## 7. Non-delivery capacity

Marketing, qualification, commercial follow-up, administration, and relationships are real work. Treating them as free manufactures capacity.

## 8. Context switching

More concurrent customers and incidents create coordination overhead. The monthly total reports it rather than hiding it in delivery.

## 9. Delivery capacity

Partner hours and start slots differ from owner capacity. A free owner cannot authorize a start when the delivery partner is unavailable.

## 10. Support capacity

Routine support, partner effort, vendor coordination, and incident reserve share a finite plan.

## 11. Incident reserve

Reserve is protected capacity, not spare time. Incident collision can consume it and force honest resequencing.

## 12. Sales capacity

Lead follow-up, qualification, discovery, solution design, and proposals require owner hours now to create future work.

## 13. Pipeline vs delivery

Pipeline potential is never booked revenue. Delivery demand can be high while future pipeline is weak.

## 14. Pipeline coverage

Compare qualified and proposed opportunity volume with expected delivery slots. Labels are weak, adequate, strong, excessive for capacity, or unknown.

## 15. Project-start gating

Signed work moves through queued, scheduled, authorized, and active only when owner, partner, cash, support reserve, and commitments permit.

## 16. Capacity conflicts

Conflicts name required and available hours, affected commitments, and choices such as queue, defer, resequence, reduce scope, protect reserve, or refer out.

## 17. Portfolio revenue

Project, support, expansion, and other simulated revenue remain distinct. Pipeline is excluded.

## 18. Portfolio contribution

Direct delivery and support costs plus incident/warranty burden turn revenue into contribution. This remains distinct from cash.

## 19. Profit vs cash

A customer milestone due next week does not fund a partner deposit due today. The stress scenario has positive contribution and a negative intramonth balance.

## 20. Receivables

The planning record preserves customer, amount, due date, status, partial receipt, dispute, received date, days late, and risk without issuing an invoice.

## 21. Partner payment timing

Deposits, milestones, finals, and support cost can precede customer cash. Timing is compared event by event.

## 22. Maximum cash exposure

The peak negative cumulative event position is funding required before related receipts; uncovered future commitments also count. Opening cash is configurable and finite.

## 23. Customer concentration

Largest revenue, contribution, owner-hour, support, and receivable shares are calculated separately because different customers can dominate each.

## 24. Partner concentration

Primary delivery, specialist, and support dependence can make an apparently diverse customer base fragile.

## 25. Vendor concentration

Shared vendors create common failure paths across otherwise unrelated customers.

## 26. Correlated incidents

One MemberCloud event can produce two incidents. Diversified customer names do not diversify their shared dependency.

## 27. Support-tail accumulation

Every completion adds recurring routine time, incident probability, and coordination risk. Small obligations aggregate.

## 28. Owner dependency

The owner connects sales, delivery leadership, QA, relationships, collections, and escalation. That range makes absence systemic.

## 29. Owner absence

Three unplanned business days delay a launch, degrade triage, defer sales, and require delegated communication. A planned week can be prepared only with queues, coverage, and expectations.

## 30. Portfolio prioritization

Protect stopped operations, explicit commitments, cash, and reserve while deliberately preserving enough future sales work.

## 31. Multi-month capacity

Monthly snapshots expose planned and incident time, context switching, remaining buffer, deferred work, and commitments affected.

## 32. Sales pipeline cliff

In growth, delivery consumes sales time. Lead flow falls from nine to zero, and several months later the pipeline is empty.

## 33. Too much demand

More closes create a visible queue. Local Works must delay, decline, refer, or conceptually add qualified delivery capacity—never hide overload.

## 34. Growth overload

Growth earns more revenue but produces eleven overload months, a five-project queue, quality risk, support accumulation, and a later weak pipeline.

## 35. Marginal-deal decisions

The exercise says PROMISING standalone and QUEUE at portfolio level. GOOD DEAL does not mean GOOD DEAL RIGHT NOW.

## 36. Portfolio health

Pipeline, sales, delivery, support, incidents, cash, concentration, partner resilience, vendor risk, owner capacity, quality, and relationships receive separate evidence states, not a magic score.

## 37. Weekly operating review

A normal review preserves controlled starts and selling. A stress review triages incidents, communicates delays, delegates updates, and protects cash and reserve.

## 38. Monthly business review

The monthly template combines customer movement, funnel, delivery, support, financial timing, owner hours, concentration, risks, decisions, and next-month action.

## 39. Baseline simulation

Moderate leads, ordinary timing and partners, one controlled start at a time, and explicit reserve yield $116,000 revenue, $56,300 contribution, no overload, and a HEALTHY verdict.

## 40. Conservative simulation

Fewer leads, a late payment, higher support, delay, and partner constraint yield $69,600 revenue and a PIPELINE_WEAK verdict.

## 41. Growth simulation

Stronger early demand yields $206,850 revenue but eleven overload months, queueing, support risk, and CAPACITY_LIMITED health.

## 42. Stress simulation

Two incident collisions, late receipts, unavailable partner, deadline, waiting work, support spike, and owner absence create a -$3,540 minimum cash position and FRAGILE verdict.

## 43. Failure: profitable but out of cash

Positive contribution coexists with negative cash because partner outflows precede customer receipt. PROFIT DOES NOT EQUAL LIQUIDITY.

## 44. Failure: pipeline cliff

Busy delivery suppresses selling now and revenue later. The delay makes a snapshot misleading.

## 45. Failure: support tail

No supported customer is extreme; cumulative routine time crosses the plan and consumes future sales capacity.

## 46. Failure: partner bottleneck

One unavailable primary partner blocks starts and expands the queue despite owner willingness and signed demand.

## 47. Failure: correlated vendor incident

One shared-vendor event affects multiple customers and consumes reserve faster than independent incident assumptions.

## 48. Failure: customer concentration

A customer can dominate receivables or owner work without dominating revenue. Each concentration type is named.

## 49. Success: controlled portfolio

Health means adequate pipeline, controlled starts, finite support, reserve, contribution, cash buffer, manageable concentration, and explicit queueing—not maximum revenue.

## 50. Final portfolio verdict

Baseline is HEALTHY; growth is CAPACITY_LIMITED; stress is FRAGILE. These verdicts concern portfolio operations, not final owner income or business viability.

## 51. Executable exercise

Run `python scripts/run_chapter_31a.py` for the weekly foundation and `python scripts/run_chapter_31b.py` for cash timing and twelve-month scenarios.

## 52. Chapter artifacts

Use `31-local-works-portfolio.md`, `portfolio-methodology.md`, the cash-flow template, monthly-review template, and Chapter 31A weekly-review template.

## 53. Readiness checkpoint

The reader can distinguish revenue, contribution and cash; model receivables and exposure; simulate twelve periods; gate starts; see support and pipeline trends; compare scenarios; review operations; and issue a qualified portfolio verdict.

## What Chapter 31 does not decide

Chapter 31 does not calculate a final owner-income target, run a 36-month or Monte Carlo examination, hire, process payroll or taxes, keep books, invoice customers, build a CRM/database/API/site, or issue the final Local Works business-viability verdict. Chapter 32 remains unimplemented.
