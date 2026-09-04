# Chapter 14 — Scope the Engagement

## Core question

**What exactly is Local Works proposing to change, and what is explicitly not included?**

Qualified problem → solution alternative → solution economics → **project scope**. Chapter 13 found a potentially sensible direction; it did not authorize a project. **A good solution idea can still become a bad project if the scope is vague.**

## 1. A good idea can become a bad project

“Improve membership freezes” can expand into cancellation, billing, family accounts, and an app before work begins. Each addition might be useful, but each is a separate decision. Scope makes the intended outcome, workflow, responsibilities, dependencies, evidence, and stopping point understandable. It is not price, proposal, contract, architecture, or implementation.

## 2. Scope is not a feature list

“Portal, admin panel, notifications, integration, reporting” names objects but not the problem or boundary. A useful engagement scope says that eligible freeze requests cause repeated handling; work is designed to reduce that handling; defined freeze requests are included; cancellation, refunds, disputes, and family-account changes are excluded; relevant systems are classified; and successful workflow behavior can be demonstrated.

## 3. Start with the business outcome

Start with “designed to reduce duplicate entry,” “improve self-service,” or “shorten approval turnaround,” not a technology. Do not promise “will reduce handling by 50%” without evidence. The outcome guides design without pretending a result is validated.

## 4. Define the workflow boundary

Every scoped workflow has a **trigger** and **end condition**. Harbor begins when a member submits a freeze request for a defined membership type. It ends when the request is approved or rejected, its status is recorded, and confirmation is sent. The boundary prevents one request process from becoming the entire membership lifecycle.

## 5. Included and excluded

Explicitly list both. Harbor includes request capture, approved eligibility rules, exception routing, decision status, and confirmation. It intentionally excludes cancellation, disputes, refunds, membership changes, full account management, a native app, and platform replacement. “Anything not listed” hides rather than teaches boundary decisions.

## 6. Actors and systems

Include only participating actors: member, front-desk employee, and membership manager. Accounting, marketing, and HR do not enter merely because they exist. Classify systems as `IN_SCOPE`, `DEPENDENCY_ONLY`, `OUT_OF_SCOPE`, or `UNKNOWN`. Unknown preserves evidence; “in scope” never grants permission or proves modifiability.

## 7. Functional scope

Say what people must accomplish: submit information, evaluate eligibility, route an exception, record a decision, and communicate status. Add only relevant non-functional considerations, such as least-privilege access, usability, auditability, and compatibility. Avoid an enterprise requirements inventory.

Data receives a boundary too. Harbor needs an identifier, membership type, dates, and status—not full payment-card data, passwords, or unrelated profile data. Use sanitized test data and approved temporary accounts; never email credentials.

## 8. Requirements vs design

A requirement states **what must be true**: members can submit required information. “Use a web form” is a design decision. Staff approval for exceptions is a requirement; sending a task through a particular automation service is design. Recording status is a requirement; choosing a database is design. Chapter 14 stays primarily at requirement level.

## 9. Must, should, could

`MUST` protects necessary behavior, `SHOULD` names important but negotiable behavior, `COULD` names optional value, and `NOT_IN_SCOPE` reinforces a boundary. This controls the first engagement without becoming backlog software. For Harbor, eligibility and decision recording are musts, automatic confirmation is a should, a manager view is a could, and a native app is not in scope.

## 10. Assumptions and dependencies

A dependency is something required, such as vendor capability or a customer administrator. An assumption is the current belief about it, such as “the subscription includes configuration access.” Record statement, importance, evidence/status, and impact if false. `UNCONFIRMED` does not mean false; `INVALIDATED` does. A critical unconfirmed technical assumption can stop estimate readiness.

## 11. Customer responsibilities

The customer provides business rules, a decision maker, approved access, sanitized test data, timely reviews, policy decisions, acceptance testing, and agreed third-party fees. Local Works must not assign specialist implementation work to a customer who was not expected to perform it.

## 12. Local Works responsibilities

Local Works translates discovery, clarifies requirements, coordinates validation and delivery, communicates status, and coordinates QA, acceptance, and documentation. Owning the customer relationship does not mean personally coding everything.

## 13. Delivery responsibilities

An unselected delivery team may perform configuration or technical implementation, support testing and deployment, and produce technical documentation. Describing the role preserves the Customer / Local Works / Delivery Team model without selecting a real vendor.

## 14. Acceptance criteria

Scope and acceptance belong together. A few given/when/then statements demonstrate the boundary: an eligible submission captures required information; an exception reaches an authorized reviewer; and a decision produces recorded status and agreed confirmation. Hundreds of test cases are unnecessary here.

## 15. Acceptance vs business outcomes

Acceptance proves the agreed workflow functions. A success metric, such as average handling time, usually needs operating time after delivery. Unless deliberately contracted otherwise, a later business result is not a condition of technical acceptance. Keep these lists separate.

## 16. Third-party boundaries

Local Works may configure an integration but cannot guarantee vendor uptime, pricing, approval, permissions, permanent API behavior, or future changes. Make control and dependency explicit. The current membership platform's configuration capability remains unknown, so Harbor needs validation rather than invented certainty.

## 17. Scope creep before kickoff

“Can we add cancellations too?” stays `REQUESTED` until explicitly classified `INCLUDED`, `DEFERRED`, `REJECTED`, or `CHANGE_LATER`. A new location, business unit, workflow, policy, compliance duty, integration, unexpectedly large migration, or architecture forced by a vendor limitation can trigger a scope change. These do not become free additions. Chapter 24 will address change-request execution.

## 18. Scope risks

Use a small register: category, description, severity, mitigation, and status. Useful categories are ambiguous requirement, unvalidated assumption, third-party dependency, customer dependency, data complexity, policy complexity, integration uncertainty, acceptance ambiguity, and other. This exposes uncertainty without building an enterprise risk system.

## 19. Harbor Fitness project scope

Harbor's outcome is designed to reduce administrative work while preserving eligibility rules and manager approval for exceptions. A bounded configuration direction was economically plausible in Chapter 13, but capability evidence remains missing. The engagement therefore begins with validation of configuration, rules, access, and the bounded implementation option. It does not pretend the whole implementation is ready.

The full fictional record is in `artifacts/harbor_fitness/14-project-scope.md`. It is neither proposal nor contract, establishes no price, and selects no partner.

## 20. Ready for estimate?

The gate returns `READY_FOR_ESTIMATE`, `NEEDS_CUSTOMER_CLARIFICATION`, `NEEDS_TECHNICAL_VALIDATION`, `NEEDS_SCOPE_REDUCTION`, or `BLOCKED`. An unclear outcome or workflow, undefined acceptance, unresolved customer responsibility, or critical unvalidated dependency prevents readiness. Perfect certainty is not required—sufficient clarity is.

Harbor returns **NEEDS_TECHNICAL_VALIDATION** because the existing platform's critical capability and test access remain unconfirmed. A broad seven-system first project would need scope reduction; “fix operations” needs customer clarification; a small known completed-job-to-invoice-draft workflow may be ready.

## 21. Executable exercise

Run:

```bash
python scripts/run_chapter_14.py
```

Read why the script preserves included/excluded work, separates three parties, keeps requirements apart from design, records deferred requests, and refuses to estimate around a technical unknown.

## 22. Chapter artifacts

- `artifacts/harbor_fitness/14-project-scope.md` — fictional applied scope
- `artifacts/project-scope-template.md` — reusable boundary-first template
- `artifacts/scope-methodology.md` — operating method
- `local_works/scope.py` — readable scope and readiness model

## 23. Readiness checkpoint

The reader should now be able to:

- define a project around a cautious business outcome and distinguish scope from features;
- name its trigger/end condition, included/excluded work, actors, systems, and minimized data;
- distinguish requirements from design and classify must/should/could/not-in-scope;
- separate assumptions from dependencies and assign customer, Local Works, and delivery duties;
- write acceptance criteria distinct from longer-term success metrics;
- classify early scope creep and record scope risks; and
- decide whether clarity is sufficient to estimate.

Stop here. Chapter 15 will ask what Local Works should charge given customer value, delivery cost, risk, owner time, and a healthy deal. Chapter 14 creates no price.
