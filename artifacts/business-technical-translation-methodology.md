# Business-to-technical translation methodology

Local Works translates between customer language and delivery language. Translation preserves what was said, identifies the durable intent, and links that intent through existing requirements to testable delivery work. It is not an architecture exercise and does not turn requests such as “we need a portal” into technical orders.

## From meaning to an implementable need

1. **Preserve statement and intent separately.** Record wording, speaker, context, and evidence. State the desired outcome, affected party, and workflow without silently rewriting the request.
2. **Reference requirements; do not duplicate them.** Preserve baseline version, provenance, scope, business-rule, test, and acceptance links.
3. **Translate workflow behavior.** Identify actors, initiation, authorization, normal and exception branches, input, outcome, and failure behavior. Actor permissions stay at the business level; do not prematurely invent roles, scopes, or permission tables.
4. **Identify data and interaction needs.** Name business data, its source (including UNKNOWN), and whether it must be read, validated, created, transformed, sent, displayed, stored, or updated. Describe the interaction outcome without choosing an email, endpoint, table, or other design absent evidence.
5. **Separate functional meaning from design.** “A manager can approve an exception” is a functional need. An endpoint is one possible later design. Specialists may compare configuration, a lightweight integration, automation, a custom service, or no change, but each option remains linked to the approved scope and solution path.

## Rules, questions, and constraints

Developers implement confirmed policy; they do not create it. Unknown eligibility or approval policy becomes a **business question** owned by the customer. Whether a platform exposes membership type is a **technical question** owned by the specialist or vendor. Their evidence and resolution paths remain separate.

Constraints are evidenced limitations—not preferences—including no/read-only API access, vendor control, authentication, hosting, rates, legacy browser support, budget, or timeline. A lightweight technical decision records context, options, selection, reason, affected requirements, and risks. If an option changes the configuration-first solution path, it triggers review rather than silently reopening Chapter 12.

## Tasks, decisions, and traceability

A task is bounded, categorized, dependent on known decisions, and has an observable done condition. “Build freeze feature” is insufficient; “record configuration capability and linked test evidence in the test environment” is observable. Dependencies such as confirmed BR-03 or available notification capability are explicit.

The intended chain is: source statement → intent → requirement → business rule/workflow → technical need → task/design question → test → acceptance. Missing coverage for an in-scope requirement is a **translation gap**. Technical work with no requirement, acceptance, scope outcome, or delivery/operational-risk justification is **unjustified technical work**. Real-time dashboards, microservices, or custom identity are not inherently wrong; without proportional justification they are gold-plating.

Invisible work—tests, logging, error handling, dependency maintenance, or deployment repeatability—can reduce reliability, maintainability, security, supportability, or delivery risk. Such a risk link is valid justification even when the customer cannot see the work.

## Nonfunctional and exception translation

- **Reliable:** failed requests are visible, outages do not silently lose work, duplicate outcomes are avoided, and unresolved failures can be followed up. No invented SLA.
- **Fast:** normal response is reasonable in workflow context; a numeric target remains UNKNOWN until agreed.
- **Secure:** members cannot see others' information, approval is limited to authorized staff, access can be revoked, secrets are not exposed, and only needed data is handled. No unsupported compliance claim.
- **Accessible/easy:** labels, keyboard operation, understandable errors, and semantic structure are considered; formal conformance is not claimed without agreement and validation.
- **Vendor write failure:** do not report success; expose accurate status and an appropriate repair path without prematurely prescribing retry architecture.

## Limitations, impacts, and readiness

A missing vendor capability can yield REVISE_TECHNICAL_DESIGN, REVISIT_SCOPE, REVISIT_SOLUTION, or CUSTOMER_DECISION_REQUIRED. Major new work is classified as estimate clarification, delivery risk, potential scope change, or technical discovery; it is not silently absorbed. Formal change execution belongs to Chapter 24.

The readiness gate can return READY_FOR_IMPLEMENTATION, READY_WITH_OPEN_NONBLOCKERS, NEEDS_BUSINESS_CLARIFICATION, NEEDS_TECHNICAL_VALIDATION, NEEDS_SCOPE_REVIEW, NEEDS_SOLUTION_REVIEW, or BLOCKED. Translation succeeds when specialists can implement intended behavior without inventing customer policy or unnecessary technology.
