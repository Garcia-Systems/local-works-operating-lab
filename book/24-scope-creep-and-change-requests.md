# Chapter 24 — Scope Creep and Change Requests

> **Part VI — Deliver the First Project**  
> **Core question:** When delivery changes, how does Local Works distinguish clarification, correction, discovery, and true scope change—and protect project economics fairly?

## 1. Why change control exists
Change control protects customers from surprise charges and Local Works from unlimited unpriced work. It preserves a fair boundary; it is not a change-order revenue tactic.

## 2. Not every change is a change request
Use the sequence: new request/information → classification → baseline comparison → impact analysis → commercial/delivery decision → approve/defer/reject/absorb → baseline update → reforecast. Discuss money only after understanding cause.

## 3. Clarification
More detail about approved behavior, reasonably implied and not materially expansive, is CLARIFICATION. “Approve” including approve/deny and recording the result should not be reflexively monetized.

## 4. Defect
Behavior that fails an approved requirement or acceptance criterion is DEFECT. Fixing an eligible freeze case incorrectly routed to a manager is not customer-funded scope.

## 5. Delivery correction
Missing promised configuration, testing, documentation, or a correct integration mapping is DELIVERY_CORRECTION, not automatically a paid request.

## 6. Requirement correction
New policy evidence may prove an earlier business statement wrong. Ask what was known, unknowable, incorrectly supplied, or missed in discovery. Classify first; apportion impact fairly rather than blaming mechanically.

## 7. Technical discovery
Evidence that a vendor API cannot write or routing cannot be configured may force redesign, scope review, or re-estimation. It is not customer creep.

## 8. Dependency change
Record the dependency, what changed, who controls it, impact, and options when a vendor, platform, price, system, or access rule changes.

## 9. Customer enhancement
A customer-requested capability beyond the baseline is an enhancement. If cancellation is expressly excluded, adding it is the clear enhancement case.

## 10. True scope change
A material change may alter workflow, actors, systems, locations, capability, integration, migration, reports, acceptance, timeline, responsibility, or support. Feature count alone is inadequate.

## 11. Deferred ideas
DEFERRED_IDEA preserves a useful Phase 2, backlog, or post-launch opportunity without pretending it is active scope. Deferral is not rejection.

## 12. Scope baseline comparison
Compare every material request with the current approved scope and requirements versions, acceptance, proposal, decisions, statements, assumptions, and estimate. Record related items and YES, NO, AMBIGUOUS, or UNKNOWN inclusion.

## 13. Ambiguous scope
“Support membership changes” may mean freezes to Local Works and freeze/cancel/payment changes to the customer. This is SCOPE_AMBIGUITY: poor scope writing creates commercial risk and does not prove customer fault.

## 14. Materiality
TRIVIAL, SMALL, MATERIAL, MAJOR, and UNKNOWN describe judgment based on effort, cost, schedule, risk, complexity, dependencies, systems, business process, tests, and documentation. There is no universal numeric score.

## 15. Absorbing small changes
A ten-minute label change may be ABSORBED for goodwill when effort and schedule effects are negligible and no precedent is set. Record the exception and reason; “never free” is as crude as “always included.”

## 16. Cumulative small changes
Eight 30-minute favors equal four hours. Track cumulative delivery and owner burden so tomorrow's small request can receive an informed boundary review.

## 17. Impact analysis
Analyze scope, delivery/owner/customer effort, cost, schedule, quality, risk, tests, documentation, and dependencies. Estimates may remain UNKNOWN and should state confidence and assumptions.

## 18. Cost and price
Incremental delivery cost is not customer price. Local Works can absorb, charge, trade, or defer cost; any proposed price should reflect scope, direct cost, owner time, risk, and customer economics—not “contractor plus 20%.”

## 19. Schedule
Preserve baseline forecast, change effect, and revised forecast. A request can move launch, consume contingency, resequence work, add a dependency, or have no effect. An earlier customer deadline is itself a change: test feasibility, scope reduction, staffing, quality, and cost before promising.

## 20. Risk
Apparently small cancellation can create payment, retention, authorization, compliance, and acceptance paths. Risk can dominate feature size.

## 21. Incremental economics
Evaluate added customer value, price, delivery cost, owner time, contribution, schedule, and risk—not the whole project as though its original baseline never existed. A feature worth about $500 annually should not automatically incur $8,000 of cost.

## 22. Change options
Options include ABSORB, approve with/without price, TRADE_SCOPE, PHASE_LATER, DEFER, REJECT, clarification, solution/scope revisit, and project pause. A price increase is one option, not the default.

## 23. Trade scope
Exchange a new reporting view for an optional notification of equivalent effort only by shared agreement. Explicitly version both addition and removal so price and timeline do not conceal a changed baseline.

## 24. Phase later
A separately discovered Phase 2 protects launch, prevents rushed expansion, and keeps a valuable idea alive.

## 25. Rejection
Reject professionally when a change is unsafe, infeasible, irrational, conflicts with the goal, violates dependencies, lacks funding, destroys timing, or is not a Local Works fit.

## 26. Approval authority
Customer decision makers approve their commitments; Local Works controls commercial offers and technical corrections; shared approval governs relevant scope, price, and schedule changes. A partner alone cannot authorize a commercial change.

## 27. Baseline updates
A material decision record preserves request, classification, baseline, evidence, impact, options, decision, approver, treatment, and successor reference. Approved work creates scope/requirement/acceptance/estimate/forecast lineage. Never silently edit v1; deferred work creates no baseline.

## 28. Defect vs change disputes
When the customer says “included” and the partner says “extra,” inspect scope, requirement, acceptance, and decision history rather than picking a side. Original intent and evidence decide—not volume.

## 29. Partner overruns
“We underestimated by 20 hours” is not automatically customer scope. Determine whether scope changed, an assumption was reasonably invalidated, customer information was wrong, discovery was unavoidable, or estimation/delivery failed.

## 30. Harbor Fitness changes
The fictional baseline remains `HF-SCOPE-14-v1`, `HF-REQ-21-v1`, an 18-hour estimate, and Chapter 23's 2026-09-15 forecast. Cancellation is excluded and phased later after a 24h/5h/4h delivery/Local Works/customer estimate, $3,600 delivery cost, illustrative $6,000 price and $500 annual value expose poor current economics. A copy clarification is absorbed. Wrong eligible routing is a no-charge defect/correction. Missing configurable routing is technical discovery/dependency change. Family-membership wording is ambiguous and returned for evidence.

## 31. Failure: everything out of scope
Charging for every clarification, defect, and missing detail angers the customer. **Change control is not a weapon.**

## 32. Failure: everything included
Saying yes to reports, notifications, cancellations, another location, and payment changes makes delivery late, confused, and unprofitable. **Goodwill without boundaries becomes unlimited scope.**

## 33. Failure: partner expands project
“We must rebuild the portal” without evidence warrants technical questions and alternative comparison—not an automatic $20,000 customer message.

## 34. Failure: no baseline
Editing a requirement in place destroys proof of original approval and makes later dispute resolution impossible. Immutable versions preserve institutional memory.

## 35. Success: fair change control
Local Works hears a useful request, compares and classifies it, estimates incremental impact, presents choices, recommends Phase 2, preserves launch, and retains the opportunity. The customer feels heard and delivery stays controlled.

## 36. Executable exercise
Run `python scripts/run_chapter_24.py`. It prints a fictional classification, impact and economics exercise; it does not implement changes, amend a contract, invoice, perform QA, accept, or deploy work.

## 37. Chapter artifacts
Use `artifacts/change-request-template.md`, `artifacts/change-classification-template.md`, and `artifacts/change-control-methodology.md`. The fictional worked record is `artifacts/harbor_fitness/24-change-log.md`.

## 38. Readiness checkpoint
The reader can explain fairness; distinguish clarification, defect, delivery/requirement correction, discovery, dependency, enhancement, and scope; compare evidence with a baseline; preserve ambiguity and UNKNOWN; assess materiality and cumulative absorbed effort; separate delivery cost from price; analyze incremental economics, schedule, and risk; trade, phase, reject, and approve with proper authority; version a new baseline without erasing history; and resolve defect/overrun disputes fairly.

Chapter 25—not this chapter—will address QA and customer acceptance. Actual amendments, signatures, invoicing, payment, negotiation, implementation, QA, acceptance, deployment, final payment, support, CRM, databases, Laravel, and a production website remain intentionally deferred.
