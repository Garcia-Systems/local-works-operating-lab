# Chapter 22 — Business-to-Technical Translation

## 1. Why translation matters
Local Works stands between customer language and delivery language. Its job is to let the technical team implement intended business behavior without inventing policy or unnecessary technology. Translation unpacks intent, workflow, actors, rules, data, exceptions, constraints, and acceptance.

## 2. Customer language is not technical instruction
“Make it easier,” “automate this,” “we need a portal,” “connect these systems,” and “make it secure” express concerns or preferences. They are not complete implementation instructions.

## 3. Do not over-translate
“Authorized staff must identify pending exceptions” preserves a need. “Build React with Redis and WebSockets” prescribes an unsupported answer. Local Works clarifies the former and leaves proportional implementation choices to specialists.

## 4. Statement vs intent
Preserve exact wording, role, context, source, and interpretation. “We need a portal” may reveal a durable intent to reduce repetitive intervention, but that interpretation remains visibly distinct from what was said.

## 5. Requirements as the bridge
Reference the Chapter 21 baseline rather than rewriting it. Requirement IDs preserve provenance, scope, questions, tests, and acceptance as work moves downstream.

## 6. Business rules
A confirmed rule becomes implementable conditions: identify relevant status/type, evaluate confirmed criteria, branch, and record a decision. Unknown criteria create customer-owned clarification; developers may not invent policy.

## 7. Workflow behavior
Translate each approved future step into input, actor, normal path, exception path, state outcome, and response. Do not start with endpoints or tables.

## 8. Actors and authorization
Members initiate their own request, staff view appropriate status, and managers decide exceptions. These are business access behaviors, not OAuth scopes or permission schemas.

## 9. Data needs
Name member identifier, type, requested dates, eligibility, approval status, and decision time only when the behavior needs them. This is a business-data inventory, not a schema.

## 10. Data sources and destinations
Mark sources CUSTOMER_INPUT, EXISTING_PLATFORM, OTHER_SYSTEM, DERIVED, MANUAL_STAFF_INPUT, or UNKNOWN. Mark actions READ, CREATE, UPDATE, SEND, DISPLAY, STORE, TRANSFORM, VALIDATE, or UNKNOWN. Never assume access or a destination.

## 11. System interactions
“The workflow can communicate final status” is a need. Email, SMS, in-app status, or platform notification are options until evidence supports a choice.

## 12. Functional vs technical
“Manager can approve an exception” is functional. `POST /.../approve` is a possible design. Chapter 22 establishes the first before specialists decide the second.

## 13. Business questions vs technical questions
“Which membership types require approval?” belongs to the customer policy owner. “Can the platform expose membership type?” belongs to a specialist/vendor. Owners, evidence, and resolution paths differ.

## 14. Constraints
Record evidenced platform, API, authentication, hosting, rate, browser, budget, and timeline limits. A preference is not automatically a constraint.

## 15. Design options
Specialists can compare existing configuration, lightweight integration, automation, and custom service. Options trace to requirement, scope, and selected solution path. A changed path requires review, not casual reopening of Chapter 12.

## 16. Technical tasks
Use small VALIDATE_CAPABILITY, CONFIGURE, IMPLEMENT, INTEGRATE, AUTOMATE, TEST, DOCUMENT, DEPLOY, INVESTIGATE, or OTHER items. This is a translation aid, not a Jira clone.

## 17. Done conditions
“Build freeze feature” is unbounded. “Configuration supports the eligible test path and passes linked cases in the test environment” is observable.

## 18. Dependencies
A rule configuration depends on policy confirmation. Notification testing depends on validated capability. Explicit dependencies prevent unknowns from becoming assumptions.

## 19. Technical decisions
A lightweight record captures decision, context, options, selection, reason, requirements, risks, and status. It preserves reasoning without architecture bureaucracy.

## 20. Traceability
The visible chain is statement → intent → requirement → business rule/workflow → technical need → task/question → test → acceptance. Simple identifiers are sufficient.

## 21. Translation gaps
An in-scope requirement with no technical need/task is a serious gap. It prompts coverage or deliberate review, not silent omission.

## 22. Gold-plating
A dashboard, event bus, microservice, warehouse, or custom identity system is not inherently bad. It is expansion when no requirement, acceptance outcome, or risk justifies it.

## 23. Invisible technical work
Tests, logging, error handling, dependency work, and deployment automation may reduce reliability, maintainability, security, supportability, or delivery risk. A clear risk link can justify them without customer-visible functionality.

## 24. Reliability, performance, security, and accessibility
“Reliable” can mean visible failures, no silent loss, and no duplicate outcome. “Fast” needs workflow context, not an invented 200 ms SLA. “Secure” means isolation, authorized approval, revocable access, secret protection, and necessary-data handling—not unsupported certification. “Works for everyone” can imply labels, keyboard operation, understandable errors, and semantic structure—not an unvalidated compliance claim.

## 25. Error behavior
A failed vendor write must not look successful. Appropriate people see the failure, the member receives accurate status, and a proportional repair path can be considered without prematurely designing retries.

## 26. Vendor limitations
A missing capability may cause REVISE_TECHNICAL_DESIGN, REVISIT_SCOPE, REVISIT_SOLUTION, or CUSTOMER_DECISION_REQUIRED. Major custom development is never a silent workaround.

## 27. Cost and timeline impacts
Extra integrations, vendors, security needs, or task clusters become ESTIMATE_CLARIFICATION, DELIVERY_RISK, POTENTIAL_SCOPE_CHANGE, or TECHNICAL_DISCOVERY. Chapter 24, not this chapter, executes formal changes.

## 28. Harbor Fitness translation
The phase remains paid, configuration-first capability validation. “Members stop having to call” links to R-002 and validation of collection, eligibility/routing, and staff re-entry—not to a custom portal. Exceptions, confirmation, and least-privilege access retain their Chapter 21 provenance and UNKNOWNs.

## 29. Failure: feature as requirement
“We need an app” becoming “Build a mobile app” without an underlying behavior is **INVALID TRANSLATION**. Explore the outcome first.

## 30. Failure: business rule lost
If R-003 requires manager review for exceptions but a task automatically processes all freezes, **BUSINESS INTENT LOST**. The design conflicts with policy.

## 31. Failure: gold-plating
A simple status need does not independently justify an event bus, real-time dashboard, microservice, and warehouse. **TECHNICAL EXPANSION REQUIRES JUSTIFICATION.**

## 32. Failure: Local Works over-specifies
Ordering Laravel, Redis, PostgreSQL, React, and AWS during a platform-configuration validation turns translation into **UNJUSTIFIED TECHNICAL CONTROL**.

## 33. Success: clean translation
“Managers only review unusual requests” becomes: standard confirmed cases avoid the queue; confirmed exceptions route for authorized review. Specialists choose design. Tests exercise both paths, and the customer confirms both. **BUSINESS INTENT SURVIVES THE TRANSLATION.**

## 34. Executable exercise
Run `python scripts/run_chapter_22.py`. The fictional exercise prints project inheritance, statements, intents, links, questions, constraints, bounded tasks, gaps, unjustified expansion, nonfunctional behavior, limitation escalation, and readiness. It changes no customer system.

## 35. Readiness checkpoint
The reader should now distinguish statement from intent; link requirements, rules, workflow, actors, data, and interactions; separate functional needs from design and business questions from technical questions; record constraints, tasks, done conditions, dependencies, and decisions; preserve traceability; detect gaps and unjustified expansion; translate quality language; and route vendor limitations backward when needed. Readiness is not implementation authorization when business policy or capability validation remains unresolved.

Chapter 23 will address milestones and project control. It is intentionally not implemented here.
