# Chapter 19 — Request and Compare Technical Estimates

> **Part V — Assemble the Delivery System**
>
> **Core question:** How does Local Works obtain useful delivery estimates, compare them fairly, expose hidden assumptions, and choose a delivery approach without simply picking the lowest bid?

Chapter 18 ended with qualified delivery candidates. The next progression is estimate request → assumptions → cost/effort/timeline → exclusions → risk/confidence → comparison → clarification → decision. It does not authorize implementation.

## 1. An estimate is more than a number

A useful technical estimate identifies the work, assumptions, inclusions, exclusions, unknowns, effort, elapsed time, customer inputs, third-party costs, risks, and confidence. A $3,000 and a $6,000 estimate can describe different work. “$2,500, two weeks” is not enough to tell.

## 2. Estimate vs price

A **technical estimate** is a delivery team's forecast of technical effort, cost, timing, assumptions, and requirements. **Customer price** is what Local Works charges. **Proposal price** is the commercial number presented to the customer. Chapter 15 owns the latter two. A delivery estimate must never silently replace them.

## 3. Build a common estimate request

Qualified candidates need a problem and business outcome—not “How much for a portal?” Give them the selected direction, scope version, included/excluded workflow, capabilities, acceptance, systems, constraints, responsibilities, testing, documentation, continuity, assumptions, unknowns, and requested response format.

## 4. Same scope, same baseline

Every candidate receives the same immutable baseline. Record `BASELINE_SCOPE_VERSION` and `ESTIMATED_SCOPE_VERSION`. Alternatives can be insightful, but label their deviation and reconcile it before comparing costs. Otherwise mark the estimate `NOT_COMPARABLE`.

## 5. Estimate components

Use relevant categories, not mandatory bureaucracy: technical validation, configuration, frontend, backend, integration, automation, migration, testing, deployment, documentation, training/support, coordination, and other. A configuration job may need only two. Both hourly ranges and fixed delivery costs are valid; neither form guarantees accuracy.

## 6. Ranges and confidence

Ranges communicate uncertainty: 24–36 hours, $2,500–$3,500, two–four weeks. Decimals do not create evidence. Confidence is HIGH, MODERATE, LOW, VERY LOW, or UNKNOWN, supported by scope clarity, access, API documents, rules, data, dependencies, and experience. Low confidence may be honest and responsible.

## 7. Assumptions

Preserve each assumption's statement, importance, evidence/status, and impact if false. “API available,” “test access supplied,” “one location,” “no migration,” or “no custom mobile app” can define the estimate. Optimistic unknowns can make a cheap bid only appear cheap.

## 8. Exclusions

Make licensing, hosting, cleanup, mobile applications, migration, after-hours deployment, ongoing support, training, and vendor fees visible. An exclusion is not necessarily wrong; a hidden exclusion makes comparison unsafe.

## 9. Third-party costs

Separate delivery-partner cost from customer-paid SaaS, API plans, hosting, messages, vendor services, and licensing. Include attributable one-time setup in a normalized delivery view when appropriate; keep recurring operating costs explicitly separate.

## 10. Customer and Local Works effort

Customer access provisioning, policy clarification, testing, acceptance, cleanup, training, and review consume capacity even when not billed. Local Works communication, translation, scope control, QA, and acceptance coordination are also separate. Together they contribute to delivery burden; not every burden needs a fictional dollar value.

## 11. Effort vs elapsed time

Twenty work hours can span three weeks because of scheduling, vendor response, testing, and approvals. Store effort hours apart from elapsed duration and its dependencies.

## 12. Availability

Duration starts only when the candidate can. A two-week job starting in six weeks may finish alongside a four-week job starting next week. Record earliest start and expected completion where useful.

## 13. Conditional estimates

An estimate may be valid only if a vendor API supports write access. Mark the contingency instead of burying it. A conditional estimate is information, not a disqualification.

## 14. Paid technical discovery

A responsible candidate may decline to guess and propose four hours/$500 to verify API behavior, authentication, and the integration path, leaving technical notes and a refined estimate. **Paying for uncertainty reduction can be cheaper than paying for bad certainty.** Selecting discovery does not select delivery.

## 15. Clarification

Ask structured questions: Is testing included? Who deploys? Is API setup included? Who maps fields? What documentation remains? What happens without access? Preserve the question, reason, response, impact, and status. The chapter's responses are fictional; no outreach occurs.

## 16. Normalize the estimates

Before price, normalize scope, testing, documentation, deployment, setup, support/handoff, customer effort, Local Works effort, assumptions, timeline, and risk. A normalized expected delivery-cost range can show partner cost plus required discovery, one-time third-party setup, and specialist work. It must show every adjustment and exclude recurring SaaS unless explicitly presented separately. Irreconcilable scopes remain `NOT_COMPARABLE`.

The broader **total project delivery burden** considers partner cost + owner effort + customer effort + implementation setup + delivery risk. It is a comparison lens, not accounting profit.

## 17. Estimate quality

Inspect scope alignment, assumption/exclusion clarity, technical reasoning, risk disclosure, cost transparency, timeline realism, testing, documentation, handoff, and confidence calibration. Qualitative STRONG/ADEQUATE/UNCERTAIN/WEAK judgments expose reasoning without a magic score. A detailed estimate is not automatically expensive, and expense is not proof of detail.

## 18. The low-bid trap

A $2,000 bid excluding $1,000 testing, $700 deployment, $600 documentation, and $500 vendor setup normalizes to $4,800. A complete $4,000 bid is then cheaper. **Raw bid price can be misleading.** This does not mean the low bid always loses; a complete aligned low bid can be best.

## 19. The high-bid trap

The highest price is not automatically highest quality. An agency may propose a data warehouse, application, and mobile client where configuration meets the bounded outcome. Chapter 12's simplest-sensible-solution discipline still applies.

## 20. Over-solution

A full member portal for a membership-freeze workflow is `SCOPE_DEVIATION`. Explain the added work and ask for a baseline revision rather than comparing its number directly or rejecting it solely for cost.

## 21. Under-solution

Request submission without required manager approval is `INCOMPLETE_SCOPE`. A low number for omitted required behavior is not an estimate of the validated scope.

## 22. Estimate uncertainty

Do not add a universal 25 percent. Show scenarios: $2,500 expected but $2,500–$5,000 under high uncertainty versus $3,500 expected and $3,500–$4,200 under moderate uncertainty. Equal $5,000 estimates with different assumptions, confidence, and documentation are not the same. “47.25 hours” with no API access, documentation, or migration evidence is false precision.

Future chapters may compare estimated with actual cost, hours, and duration. This chapter creates no actual history.

## 23. Partner fit still matters

Combine Chapter 18 delivery fit with estimate quality, expected cost, timeline, risk, continuity, communication, availability, documentation, and handoff. A polished estimate does not erase security, reliability, or continuity risk. Neither low nor high price is selected automatically.

## 24. Harbor Fitness comparison

The fictional common request `HF-ER-19-v1` references `HF-SCOPE-14-v1`, a configuration-first membership-freeze workflow with exception approval. Only Northstar and Bridge were externally qualified for estimates in Chapter 18; Cedar is retained solely as the explicit over-solution exercise and Local Works as a burden alternative, not as real solicitation.

Northstar forecasts 16–24 hours and $2,000–$3,000, but conditions delivery on native feature validation. Bridge forecasts 42–64 hours and $5,500–$8,300 for a flexible integration, assuming API access. Cedar's $18,000–$28,500 portal uses a different scope and is not comparable. Self-delivery has $0 partner cash but 34–57 Local Works hours, low skill confidence, and six–ten elapsed weeks.

Clarification confirms Northstar documentation, adds $500–$900 vendor setup to Bridge, identifies Cedar's extra portal features, and exposes the work displaced by self-delivery. The fictional decision selects Northstar for $500–$700 technical discovery only, keeps Bridge as backup, requests a Cedar revision, and does not choose self-delivery. No implementation begins. Scope and solution are not yet reopened, although failed validation may require either.

## 25. When not to select anyone

Outcomes include `SELECT_FOR_DELIVERY`, `SELECT_FOR_TECHNICAL_DISCOVERY`, `REQUEST_REVISED_ESTIMATE`, `REQUEST_CLARIFICATION`, `KEEP_AS_BACKUP`, `DO_NOT_SELECT`, `REOPEN_DELIVERY_SEARCH`, `REVISIT_SCOPE`, and `REVISIT_SOLUTION`. A collection of weak or divergent estimates can reveal a bad baseline rather than bad partners.

## 26. Executable exercise

Run:

```bash
python scripts/run_chapter_19.py
```

The output prints the common baseline, four explicitly fictional perspectives, assumptions, exclusions, separate costs and efforts, confidence, clarifications, normalization, bias traps, partner fit, and a discovery-only decision.

## 27. Chapter artifacts

- `artifacts/technical-estimate-request-template.md`
- `artifacts/technical-estimate-template.md`
- `artifacts/estimate-comparison-template.md`
- `artifacts/technical-estimation-methodology.md`
- `artifacts/harbor_fitness/19-technical-estimates.md`

## 28. Readiness checkpoint

The reader can now:

- distinguish technical estimate from customer/proposal price;
- issue a complete common request against one scope version;
- preserve assumptions, exclusions, ranges, confidence, validity, and contingencies;
- separate partner/third-party cost and partner/customer/Local Works effort;
- distinguish effort, elapsed duration, availability, and completion;
- clarify and normalize estimates without hiding scope differences;
- recognize low-bid, high-bid, over-solution, under-solution, and false-precision traps;
- treat paid discovery as responsible uncertainty reduction;
- combine estimate quality with partner fit; and
- select delivery, discovery, revision, clarification, backup, search, or scope/solution reconsideration without starting implementation.

Chapter 20 will examine delivery risk and ownership before kickoff. Do not begin it here.
