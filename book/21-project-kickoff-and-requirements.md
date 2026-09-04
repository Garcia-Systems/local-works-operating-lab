# Chapter 21 — Project Kickoff and Requirements

## Part VI — Deliver the First Project

**Core question:** How does Local Works turn the sold, controlled engagement into a working project without reopening everything already decided?

Authorized engagement → kickoff readiness → shared understanding → requirements baseline → open questions → decision rules → delivery plan → requirements ready for implementation.

## 1. Kickoff is a transition
Kickoff moves context from sales and solution design to delivery. The delivery team needs the reason, workflow, constraints, prior tradeoffs, and deliberate exclusions—not merely “build this feature.” Its central rule is **kickoff is not a second discovery project**.

## 2. Do not restart discovery
Chapters 17–20 supplied authorization, delivery path, estimate, and operational control. Those records are inputs. Do not casually reopen qualification, direction, commercial scope, or price. New implementers may challenge a decision with new evidence; their normal preference is not evidence.

## 3. Kickoff readiness
Verify authorization, known proposal/scope versions, selected-enough path and estimate, controlled/monitored major risks, responsibilities, participant groups, access-request plan, and available files. Return a visible outcome: ready, commercial/delivery/access/participant clarification, or blocked. Technical unknowns intended for validation do not automatically prevent the meeting.

## 4. Who needs to participate
Use roles rather than names alone: customer sponsor/decision maker/SME/technical contact; Local Works project/solution lead; technical lead/implementer/QA; and vendor contact only when useful. Record organization, responsibility, authority, communication, and availability. A small project needs few people, not many personas.

## 5. The project context pack
Link the problem, current workflow, economic rationale, selected direction, approved and excluded scope, acceptance, responsibility matrix, estimate, risks, systems, assumptions, dependencies, technical questions, and decision history. The pack is an index and summary, not a duplicate archive. A disciplined agenda reviews that context before requirements, questions, testing, cadence, escalation, and next milestone.

## 6. Scope vs requirements
Scope is the boundary: “membership-freeze workflow.” Requirements state what that included workflow must do: collect necessary information, evaluate supported rules, route exceptions, record decisions, and communicate status. A cancellation workflow is another scope item, not a requirement that can slip in unnoticed.

## 7. Requirement types
Use relevant types only: BUSINESS_RULE, FUNCTIONAL, DATA, INTEGRATION, SECURITY, ACCESS, USABILITY, ACCESSIBILITY, PERFORMANCE, RELIABILITY, AUDITABILITY, OPERATIONS, DOCUMENTATION, TESTING, DEPLOYMENT, or OTHER. Priority remains Chapter 14's MUST, SHOULD, COULD, and NOT_IN_SCOPE.

## 8. Requirement quality
A useful statement is clear, bounded, testable, traceable, necessary, understandable, and not prematurely technical. Replace “make it user friendly” with “a member can submit required freeze information without staff data entry.” Preserve an uncertainty instead of hiding it in confident prose.

## 9. Requirement provenance
Record source, evidence/reference, related scope, acceptance linkage, status, and open questions. Customer policy is stronger evidence of policy than a developer suggestion. A vendor claim and technical validation are different sources. UNKNOWN remains UNKNOWN.

## 10. Business requirements vs technical design
“Eligible members must be able to request a freeze” states business behavior. “Webhook + API + queue worker” chooses a design. Requirements should not lock technology unless a supported constraint genuinely requires it. Chapter 22 will deepen the translation without losing intent.

## 11. Business rules
Eligibility, balance conditions, duration, self-service cases, and review cases are policy. Only rules supported by prior Harbor records may be treated as known. Customer authority owns unknown policy; a specialist cannot fill the blank with a convenient guess.

## 12. Open questions
Keep a useful register: question, category, owner, reason, blocking flag, needed-by point, status, answer, and evidence. Categories include business rule, technical, vendor, data, access, security, scope, acceptance, and other. Blocking questions stop affected work; nonblockers can remain open.

## 13. Requirement traceability
Use lightweight references backward to problem, workflow, scope, rule, and acceptance, and later forward to implementation, test, and acceptance. The purpose is to explain why a requirement exists, not to construct an enterprise bureaucracy.

## 14. Requirements baseline
Implementation eventually works against a named version in DRAFT, REVIEWED, APPROVED_FOR_IMPLEMENTATION, or SUPERSEDED state. A baseline does not freeze reality. It makes later information visible and protects the meaning of approval.

## 15. Clarification vs change
“Which manager role performs the already-required exception approval?” may clarify. “Also add cancellation” expands scope. Classify later information as clarification, correction, new requirement, scope change, technical discovery, or defect discovery. Chapter 24 will handle formal change execution.

## 16. Data requirements
Identify necessary business information—fictional member identifier, membership type, dates, reason category if required, eligibility, decision, status, and timestamps. This is not permission to design a production schema or use personal data.

## 17. System interaction requirements
Describe business interactions: read eligibility information, submit or update status, notify the member, and record approval. Do not invent endpoints where validation has not established them.

## 18. Exceptions
Cover more than the happy path. Ask what the business expects for member not found, review-required type, duplicate request, invalid dates, vendor outage, denial, or failed write. Avoid prematurely prescribing retries, queues, or architecture.

## 19. Security/access
State high-level outcomes: one member cannot see another's request, only authorized staff decide exceptions, access is role-appropriate, and credentials are not exposed. Full authorization architecture is later work.

## 20. Operations
Ask what staff must do after launch: see pending exceptions, recognize failures, understand status, correct allowed data, and know escalation. Include only evidenced needs. “Build an admin panel” is not a default requirement.

## 21. Documentation
Scale configuration summary, support/handoff notes, deployment notes, limitations, and rule mapping to the project. A small validation needs compact, shared evidence—not a giant manual.

## 22. Testing
State testable outcomes: routine eligible path, exception routing, denied status, and understandable invalid response. Chapter 25 handles detailed QA execution.

## 23. Acceptance traceability
Link Chapter 14 criteria to requirement IDs. A criterion that an eligible member avoids staff re-entry might link to rules, collection, and workflow-routing requirements. Keep the map small enough to use.

## 24. Communication cadence
Agree on participants, purpose, and cadence: perhaps a weekly update, milestone review, asynchronous question log, and urgent escalation route. Daily meetings are not assumed.

## 25. Decision authority
Name authority for business rules, scope, technical design within constraints, customer acceptance, commercial changes, production access, and vendor escalation. Authority and performance are separate.

## 26. Escalation
A partner question goes to Local Works triage, the customer SME for facts, the decision maker for policy/scope, or vendor for platform limitations. Local Works coordinates customer and commercial effects. A contractor should not independently promise a scope or price change.

## 27. Harbor Fitness kickoff
Harbor remains a configuration-first **capability validation**, not a portal implementation. Chapter 20 left readiness blocked pending shared-output and access/revocation controls. Participants are a Harbor decision maker and SME, Local Works lead, fictional specialist, and vendor support when needed. Requirements therefore ask validation questions and demand transition-ready evidence rather than pretending the eventual implementation exists.

## 28. Failure: reopen everything
“We usually build custom portals, so let us start over” reopens direction, scope, features, architecture, and price without evidence. The result is **PROJECT DRIFT**. A new implementer does not invalidate prior business analysis merely by arriving.

## 29. Failure: feature dump
Cancellation, reporting, referrals, payment updates, and a mobile app mentioned during kickoff are not automatically requirements. Record them as OUT_OF_SCOPE, FUTURE_DISCOVERY, or POTENTIAL_CHANGE; do not edit approved scope silently.

## 30. Failure: developer invents policy
Asked for maximum freeze duration, the customer has no current answer. The developer guesses 90 days. That is an **UNAUTHORIZED BUSINESS RULE**. Assign the question to customer authority and block the affected requirement.

## 31. Success: small clear kickoff
A configuration-first kickoff confirms one workflow, two supported rules, one platform, one exception route, one acceptance criterion, and two technical questions. The baseline is small and testable. **Good project control often looks boring.**

## 32. Requirements readiness gate
Choose READY_FOR_IMPLEMENTATION, READY_WITH_OPEN_NONBLOCKERS, NEEDS_BUSINESS_DECISIONS, NEEDS_TECHNICAL_VALIDATION, NEEDS_ACCESS, NEEDS_SCOPE_CLARIFICATION, or BLOCKED. Not every question must close; every blocker must. Readiness does not itself start implementation.

Preview only these future milestones: KICKOFF, REQUIREMENTS_BASELINE, TECHNICAL_VALIDATION, IMPLEMENTATION_COMPLETE, QA_READY, CUSTOMER_ACCEPTANCE, and LAUNCH. Chapter 23 will add milestone control.

## 33. Executable exercise
Run `python scripts/run_chapter_21.py`. The fictional exercise assembles prior state, evaluates blocked kickoff readiness, prints roles and context, drafts a provenance-rich validation baseline, preserves policy unknowns, classifies clarification/change, and returns a readiness decision. It starts no customer or implementation activity.

## 34. Chapter artifacts
- `artifacts/project-kickoff-template.md`
- `artifacts/requirements-baseline-template.md`
- `artifacts/open-questions-template.md`
- `artifacts/kickoff-requirements-methodology.md`
- `artifacts/harbor_fitness/21-project-kickoff.md`
- `artifacts/harbor_fitness/21-requirements-baseline.md`

## 35. Readiness checkpoint
The reader can explain kickoff, verify readiness, transfer context, identify participants, distinguish scope/requirements and requirement/design, write sourced requirements, capture rules/questions, classify clarification/change, version a baseline, cover data/interactions/exceptions, link acceptance, establish cadence/authority/escalation, and decide whether implementation may begin.

Chapter 22—not this chapter—will translate customer language, workflow rules, and business requirements into implementable technical work without losing business intent.
