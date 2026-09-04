# Kickoff and requirements methodology

## Kickoff is a controlled transition
Kickoff transfers an authorized engagement from sales/solution design to delivery. It aligns the people who will deliver; it is not a second discovery project or a marketing presentation. Prior problem qualification, solution direction, commercial scope, and customer price remain decisions unless new evidence demonstrates that one is invalid.

## Readiness and participants
Before kickoff, verify commercial authorization; proposal, scope, and estimate references; a sufficiently selected delivery path; monitored or resolved control risks; responsibilities; customer, Local Works, and delivery participants; planned access requests; and available context. Unknown technical details are normal and belong in the question register rather than automatically preventing kickoff. Identify people by role, organization, work, authority, communication needs, and availability. Explicit authority should cover business rules, scope, technical design within scope, acceptance, commercial changes, production access, and vendor escalation.

## Context pack and agenda
Assemble a compact pack that links—not copies—the problem, workflow, economics, solution choice, included/excluded scope, acceptance, responsibilities, estimate, systems, assumptions, dependencies, risks, questions, and decision history. Review these in that order, then confirm testing, communication, escalation, and the next milestone. Context lets an implementer understand why, constraints, prior tradeoffs, and stopping points rather than merely hearing “build this feature.”

## Scope and requirements
Scope says what the engagement includes; requirements say what the included solution must do. A membership-freeze workflow can be scope, while collecting required information and routing exceptions are requirements. A new cancellation workflow is not silently a requirement. Use only relevant types: business rule, functional, data, integration, security, access, usability, accessibility, performance, reliability, auditability, operations, documentation, testing, deployment, or other. Reuse MUST, SHOULD, COULD, and NOT_IN_SCOPE.

A useful requirement is clear, bounded, testable, traceable, necessary, understandable, and not prematurely technical. “A member can provide required freeze information without staff re-entry” is testable; “user friendly” is not. “Eligible members can request a freeze” is a business requirement. “Use a webhook, endpoint, and queue” is technical design and stays elsewhere unless the technology itself is a supported constraint.

## Provenance, rules, and questions
Each requirement records its source and evidence reference, related scope, acceptance linkage, state, and open questions. Discovery evidence, workflow, approved scope, customer policy or statement, technical validation, partner input, vendor documentation, and acceptance criteria are not interchangeable sources. Preserve UNKNOWN.

Business policy belongs to the customer. Never invent a maximum duration, eligibility rule, or exception policy. Put an unknown in the lightweight open-question register with category, owner, consequence, blocking flag, needed-by point, status, answer, and evidence. A blocking policy question goes to the customer decision owner; a capability question goes to technical validation/vendor evidence. Nonblocking questions need not stop all work.

## Traceability and baseline
Trace backward from a requirement to problem, workflow, scope, rule, and acceptance where applicable, and later forward to implementation, test, and acceptance. Simple identifiers are sufficient. A DRAFT, REVIEWED, or APPROVED_FOR_IMPLEMENTATION baseline makes the set and version visible; SUPERSEDED preserves history. It does not pretend change is impossible.

After baseline classify information as CLARIFICATION, CORRECTION, NEW_REQUIREMENT, SCOPE_CHANGE, TECHNICAL_DISCOVERY, or DEFECT_DISCOVERY. “Which manager role approves the already-required exception?” can clarify. “Also build cancellation” changes scope. Chapter 24, not this chapter, will execute formal changes.

## Requirement coverage
Record business data—identifiers, categories, decisions, statuses, and timestamps—without designing a database schema. Record business-level system interactions such as reading eligibility, recording approval, and notifying a member without inventing endpoints. Include expected business behavior for invalid input, duplicates, missing member, review-required types, vendor outage, denial, or failed write.

For customer-facing work, use understandable instructions, labels, keyboard access, and clear errors where relevant without claiming compliance certification. State role-appropriate access, separation between members, authorized approval, and safe credential handling without designing authorization architecture. Include only operations actually required after launch; do not default to an admin panel. Scale configuration, handoff, deployment, known-limitations, and rule-mapping documentation to the project. Make happy paths and significant exceptions testable; Chapter 25 handles QA execution.

## Acceptance and coordination
Link each acceptance criterion to a few requirements rather than constructing an enterprise matrix. Establish a proportionate cadence such as weekly status, milestone review, an asynchronous question log, and an urgent escalation route. Delivery questions go through Local Works triage, then to the customer SME/decision maker for policy or scope and to the vendor for platform limits. A contractor should not independently turn a technical issue into a commercial customer commitment.

## Readiness gate
Return READY_FOR_IMPLEMENTATION, READY_WITH_OPEN_NONBLOCKERS, NEEDS_BUSINESS_DECISIONS, NEEDS_TECHNICAL_VALIDATION, NEEDS_ACCESS, NEEDS_SCOPE_CLARIFICATION, or BLOCKED. Every noncritical question need not be answered. Kickoff and baseline readiness coordinate future work; neither automatically starts implementation.
