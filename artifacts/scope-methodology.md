# Scope methodology

Scope exists to turn a promising solution direction into an understandable engagement boundary. A good idea can become a bad project when nobody can say where the workflow begins, where it ends, or what acceptance means. Scope is therefore not a feature list: it connects a qualified problem and a cautiously phrased **business outcome** (“designed to reduce…”) to bounded work.

## Define the boundary

1. Name the workflow **trigger** and **end condition**. This prevents “freeze requests” from becoming “the membership lifecycle.”
2. List meaningful **included** work and intentional **excluded** work. “Anything not listed” is not a substitute for exclusions.
3. Identify participating actors without silently adding every department.
4. Classify each system as `IN_SCOPE`, `DEPENDENCY_ONLY`, `OUT_OF_SCOPE`, or `UNKNOWN`. In scope does not imply that Local Works has permission or technical capability to modify it.
5. Minimize data: name what is required and what is unnecessary. Require approved, least-privilege, temporary/test access; never ask for emailed passwords or lab copies of secrets or customer records.

## Requirements, not premature design

Functional scope describes what people must accomplish. “A member can submit required information” is a requirement; “use a web form” is a design decision. Record a design constraint only when it is genuinely established. Add lightweight non-functional considerations—security, usability, reliability, accessibility, auditability, supportability, maintainability, performance, or compatibility—only when relevant.

Prioritize with `MUST`, `SHOULD`, `COULD`, and `NOT_IN_SCOPE`. These labels clarify the first engagement; they do not create a product backlog. A new request remains `REQUESTED` until explicitly made `INCLUDED`, `DEFERRED`, `REJECTED`, or `CHANGE_LATER`.

## Assumptions, dependencies, and responsibilities

A **dependency** is something required: vendor access, a customer administrator, test environment, documentation, or approved account. An **assumption** is what is believed about it: for example, that the subscription includes API access. Record why an assumption matters, evidence/status (`CONFIRMED`, `UNCONFIRMED`, `INVALIDATED`), and impact if false.

Divide responsibilities among the three parties. The customer supplies access, rules, decision makers, review, acceptance testing, policy decisions, and agreed third-party fees. Local Works translates discovery, clarifies requirements, coordinates delivery, communication, QA, acceptance, and documentation. An as-yet-unselected delivery team may configure or implement, support testing/deployment, and provide technical documentation. This conceptual division does not select a vendor or force customers to do specialist technical work.

## Acceptance and outcomes

Acceptance criteria are a small set of demonstrable given/when/then behaviors. A success metric measures the later business outcome, such as average handling time. Working software may be accepted before enough operating time exists to assess that metric; do not silently make long-term outcomes technical acceptance conditions.

Local Works can coordinate work inside the boundary, but cannot guarantee third-party uptime, approval, price, perpetual API behavior, or vendor changes. State those third-party limits.

## Change and risk

Potential change triggers include a new workflow, location, business unit, integration, policy, compliance duty, unexpected migration size, or vendor limitation requiring different architecture. They require an explicit scope decision rather than free absorption; execution of formal change requests comes later.

Use a lightweight risk record: category (`AMBIGUOUS_REQUIREMENT`, `UNVALIDATED_ASSUMPTION`, `THIRD_PARTY_DEPENDENCY`, `CUSTOMER_DEPENDENCY`, `DATA_COMPLEXITY`, `POLICY_COMPLEXITY`, `INTEGRATION_UNCERTAINTY`, `ACCEPTANCE_AMBIGUITY`, or `OTHER`), description, severity, mitigation, and status.

## Ready-for-estimate gate

Choose `READY_FOR_ESTIMATE`, `NEEDS_CUSTOMER_CLARIFICATION`, `NEEDS_TECHNICAL_VALIDATION`, `NEEDS_SCOPE_REDUCTION`, or `BLOCKED`. Perfect certainty is unnecessary, but an unclear outcome/boundary, undefined acceptance, unresolved customer duty, or unvalidated critical dependency prevents readiness. A technical capability unknown calls for bounded validation, not invented certainty. This gate creates neither price nor proposal.
