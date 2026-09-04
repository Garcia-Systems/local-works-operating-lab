# Chapter 25 — QA and Customer Acceptance

> **PART VI — DELIVER THE FIRST PROJECT**  
> **Core question:** How does Local Works prove delivered work satisfies approved requirements, catch defects before the customer does, and define a fair path to acceptance?

**Approved requirements → test conditions → delivery-team testing → Local Works QA → defect classification → customer acceptance testing → acceptance decision → fix / retest / accept / reject.**

The governing rule is simple: **customer acceptance should not be the first time the project is tested.** The customer validates business fitness, rather than serving as the delivery team's unpaid test department.

## 1. Why QA exists
QA creates defensible confidence that delivery matches scope, requirements, business rules, acceptance criteria, expected quality, and handoff expectations. It protects customers from avoidable defects and Local Works from subjective disputes.

## 2. Testing vs QA
Testing is the act of checking behavior. QA is the broader process around planning, coverage, evidence, review, classification, correction, and readiness. Neither term needs enterprise ceremony on a tiny engagement.

## 3. Acceptance vs business success
Acceptance asks whether agreed behavior works, criteria pass, and known nonblockers are disclosed. Business success may require weeks of use, adoption, reduced staff time/support, or improved satisfaction. Do not turn these lagging outcomes into launch blockers unless explicitly contracted; an acceptance decision records `business_success_proven = false`.

## 4. Test planning
Use a proportional case: ID, title/type, requirement/rule/criterion links, preconditions, steps, expected and actual results, status, evidence, and notes. Select only applicable functional, rule, workflow, integration, data, security/access, usability, accessibility, error, regression, documentation, deployment, operations, or other checks.

## 5. Requirement coverage
Map every approved MUST requirement to meaningful tests and current results. `UNTESTED_REQUIREMENT` is a readiness problem. A blocked test is not a failed one, and `UNKNOWN` should not be disguised as success.

## 6. Acceptance coverage
Map each criterion to cases and evidence. Customer acceptance cannot rest on “looks good.” A failed criterion blocks acceptance even when individual implementation details appear impressive.

## 7. Delivery-team testing
Before handoff, the partner performs applicable unit/component checks, configuration validation, integration and error paths, a technical smoke test, and documentation completion. Chapter 25 does not prescribe a framework.

## 8. Local Works QA
Local Works checks business workflow, requirement/criterion coverage, scope fidelity, exceptions, obvious usability, known limitations, and handoff completeness. It decides whether the customer should see the work; it need not repeat every low-level technical check.

## 9. Customer acceptance testing
The customer validates business and policy correctness, representative real-world workflow fitness, staff/member experience, and criteria. Technical exhaustiveness stays with the delivery process.

## 10. Test environments
Record development, test, sandbox, staging, production-like, production, or unknown conceptually. If a vendor permits configuration only in production, flag risk and choose controls deliberately; this lab creates or changes no environment.

## 11. Test data
Prefer synthetic, fictional, or sanitized data. Track sensitivity, source, and appropriateness at a high level. Lab evidence contains neither PII nor credentials.

## 12. Happy path
Test the normal intended flow. For Harbor, an eligible standard freeze should follow the routine path without unnecessary staff re-entry.

## 13. Exception paths
Test meaningful risk: review-required membership, invalid date, duplicate, member not found, vendor unavailable, denial, or failed write where in scope. Do not enumerate every imaginable edge.

## 14. Business-rule tests
Every important rule deserves a demonstrating case. Harbor's BR-03 says a special membership reaches an authorized manager, while a standard eligible membership bypasses that review.

## 15. Security/access tests
At a high level, verify another member's request is not exposed, unauthorized staff cannot approve, normal customer use does not depend on temporary partner access, and customer-visible output contains no secret. This is neither penetration testing nor security certification.

## 16. Usability/accessibility
Check understandable labels and errors, visible outcomes, duplicate entry, dead ends, keyboard interaction, meaningful errors, and semantic clarity where applicable. These practical checks are not a UX research program or WCAG certification.

## 17. Integration/data/error testing
When integration is in scope, check record, field mapping, direction, duplicate behavior, failure, and recovery/retry. Preserve the right fictional member, dates, status, and required data. Above all, **a failed write must not look successful**: show failure, suppress false success, and permit follow-up.

## 18. Regression
A correction can break working behavior. After a routing fix, rerun the standard path, exception route, and confirmation. Keep the suite commensurate with risk.

## 19. Defects
A defect record links ID, summary, requirement/test, environment, expected/actual, business impact, finder, owner, severity, status, correction need, target retest, and notes. Evidence makes disagreement inspectable.

## 20. Severity and priority
Severity is impact; priority is when to act. Critical might expose another customer's data; high stops the core workflow; medium breaks an important exception; low has a workable minor impact; cosmetic changes no workflow. Context matters, and a low-severity launch-visible issue can be high priority.

## 21. Defect vs change
Failure to meet an approved requirement is a **defect**. New desired behavior is a **change request** under Chapter 24. QA cannot sneak expansion into defects, and defect correction is not customer-paid work by default.

## 22. Not-a-defect
A concern can match approved scope. Respectfully mark it `NOT_A_DEFECT`, explain evidence, then route it to clarification, training/documentation, or change control. “Can we add cancellation?” does not reveal a freeze-workflow bug.

## 23. Known issues
Never hide them. Record description, severity, workaround, impact, treatment, accepter, and a review/expiry point where relevant.

## 24. Acceptance blockers
Failed MUSTs, unresolved critical/high defects, failed criteria or important rules, unsafe access, material data-integrity failure, missing required documentation, and an unvalidated in-scope launch path can block. Cosmetic imperfections do not automatically block.

## 25. Acceptance with known issues
It is fair when issues are noncritical and disclosed, the customer understands impact, an acceptable workaround/treatment is recorded, criteria remain reasonably satisfied, and acceptance is explicit.

## 26. Customer acceptance session
Restate scope; demonstrate workflow; have the customer run representative cases; review exceptions, known issues, and handoff; record the result; separate defects and changes. This is not another discovery workshop. Conditional acceptance means materially acceptable subject to specifically named remaining items.

## 27. Rejection and disagreement
Rejection identifies the exact criterion/requirement, defects, evidence, next action, and retest plan—not “customer unhappy.” If partner and customer disagree, inspect scope, requirements, criteria, evidence, and decision history rather than personalities.

## 28. QA cycles and rework
Record TEST → DEFECT → FIX → RETEST → RESULT and cycle count. Many cycles can indicate unclear requirements, poor implementation, weak testing, or unstable dependencies; evidence should precede blame. Track defect-correction rework separately from customer-paid scope-change effort for later economics.

## 29. QA escapes
A customer-found defect Local Works reasonably should have caught is a QA escape: a broken core workflow, missing required confirmation, or failed standard case. First-pass acceptance and pre-customer requirement pass rate are learning signals, not metrics to game.

## 30. Harbor Fitness QA
Chapter 25 continues the approved **membership-freeze configuration and capability validation**, not a portal. Six proportional cases cover requirements R-001–R-005 and criteria AC-01/AC-02. HF-T01 initially finds a high-severity routing defect; the partner corrects it, Local Works retests it, and lightweight regression preserves the standard, exception, and confirmation paths. HF-D02's awkward but understandable confirmation is disclosed as cosmetic. Customer review then produces `ACCEPTED_WITH_KNOWN_ISSUES`, while long-term ROI remains unproven.

Dates remain causal: ready for acceptance, customer review, and acceptance are distinct. A prior review-window agreement should be operationally observed so work does not remain “almost accepted” indefinitely, without drafting contract language. Evidence is a conceptual checklist/report, not a real signature or email.

## 31. Failure: customer is QA
Local Works sends unchecked delivery to Harbor. The customer discovers broken standard routing, missing confirmation, and wrong eligibility. **The customer should not be the first QA pass.** These are QA escapes, not customer service.

## 32. Failure: happy path only
The standard request works but the exception fails after launch, leaving staff unable to handle reality. **The workflow includes exceptions.**

## 33. Failure: scope change called bug
Logging requested cancellation as “bug: cancellation missing” erases the baseline, converts expansion into free correction, and destroys scope discipline.

## 34. Failure: defect called change
R-002 clearly says the eligible request bypasses manager. Charging extra because it does not is wrong: this is **defect correction**.

## 35. Failure: hidden known issue
Launching while concealing a failing membership type transfers surprise to Harbor. **Undisclosed known issues destroy trust.**

## 36. Success: fair acceptance
The delivery team tests first. Local Works finds one defect and has it fixed before customer review. Harbor validates standard, exception, and confirmation behavior. A minor wording issue is disclosed and accepted. That is healthy acceptance, not forced perfection.

## 37. Executable exercise
Run `python scripts/run_chapter_25.py`. The fictional exercise prints all fifteen stages, traceability, first run, defect/change triage, correction/retest, regression, Local Works readiness, customer session, explicit decision, metrics, and failure lessons. It touches no customer system.

## 38. Chapter artifacts
Use `artifacts/qa-test-plan-template.md`, `artifacts/defect-template.md`, and `artifacts/customer-acceptance-template.md`. The operating method is in `artifacts/qa-acceptance-methodology.md`; the filled fictional record is `artifacts/harbor_fitness/25-qa-and-acceptance.md`.

## 39. Readiness checkpoint
The reader can now explain testing versus QA and acceptance versus business success; write proportional traceable cases; identify uncovered MUSTs; test normal and meaningful exception behavior; distinguish status, severity, priority, defects, changes, and not-a-defects; disclose known issues; determine blockers; run Local Works QA before customer review; coordinate evidence-based acceptance and rejection; preserve timing/evidence; track fixes, regression, rework, and escapes; and make a fair acceptance decision.

Chapter 25 performs no production deployment, signature, invoice, payment, project-economics calculation, warranty, support, CRM, database, Laravel, or production-site work. Those concerns remain intentionally deferred; do not proceed to Chapter 26 here.
