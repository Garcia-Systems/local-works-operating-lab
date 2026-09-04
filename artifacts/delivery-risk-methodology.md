# Delivery Risk and Ownership Methodology

## Three separate questions

**Legal ownership** asks who owns intellectual property or contractual rights. It depends on agreements and applicable law; this lab gives no jurisdiction-specific conclusion. **Operational control** asks who can access, administer, recover, deploy, and transition an asset. **Responsibility** asks who is accountable and who performs, consults, or is informed. Chapter 20 models the latter two and records legal ownership only as separate evidence.

## Asset, source, account, and deployment control

Inventory only assets applicable to the chosen stage. Record the primary controller, administrative and backup access, recovery, transferability, and uncertainty. Custom source in one contractor's personal repository is a continuity warning; an organizational repository or documented mirror can reduce it, but no single legal-ownership pattern fits every engagement. Source alone is insufficient: another provider must be able to identify environments, dependencies, configuration, deployment, and rollback. Customer-facing domains, hosting, payments, booking, automation, and SaaS accounts should not be unnecessarily trapped in a personal account. Partner control is not automatically wrong; its transition cost must be visible.

## Access control

Track identity/access metadata—not secret values. Use separate identities and minimum necessary, preferably temporary, privileges; record purpose, current status, expected revocation, and who can revoke or recover. Shared personal passwords obscure accountability. Conversely, giving everyone production administration increases exposure, conflicting-change risk, and revocation difficulty: more access is not more control.

## Knowledge continuity and decision history

Accessible code cannot replace undocumented business rules, mappings, schedules, manual procedures, vendor quirks, exception logic, configuration rationale, tests, or deployment knowledge. Record required artifacts, holder, documentation location, and transition readiness. Preserve concise decision context: what was decided, why, under which scope, and by whose authority. Local Works retains enough discovery, scope, rationale, estimate, questions, acceptance, deployment summary, and contacts to coordinate; it need not duplicate every technical detail.

Documentation is proportional. A tiny configuration may need what changed, where, rollback, and where authorized access is managed. A large integration may need architecture, data flow, authentication, deployment, monitoring, failure modes, dependencies, runbook, and troubleshooting.

## Responsibility and authority

For each applicable activity record an accountable party, performers, consulted parties, and informed parties. Customers normally decide policy, authorize access/subscriptions, participate in tests, administer their systems, and accept. Local Works normally interprets scope, translates requirements, coordinates customer communication, project and QA work, escalation, acceptance, and commercial changes. A partner may design and implement within constraints, configure, integrate, test, document, support deployment, and correct agreed defects. These defaults are not unlimited obligations.

A required responsibility without an accountable or performing party is a gap. Monitoring failures is a classic gap that can break a technically correct integration. Multiple performers are useful for some work, but multiple independent production or change authorities are ambiguous. The customer determines required business behavior; technical specialists determine implementation within agreed constraints. The partner cannot turn preference into billable expansion. Local Works coordinates design choices affecting scope, price, risk, workflow, or maintainability, preserving Chapter 16 controls.

## Dependencies, escalation, and incident ownership

For each vendor/API/SaaS/hosting/identity/messaging/payment dependency, record criticality, relationship owner, access, support route, known limitation, failure effect, fallback, and status. Local Works does not control a vendor. Plan a single coordination path: customer issue → Local Works triage → delivery partner/vendor investigation → Local Works customer communication. Before launch, surface who would detect, triage, investigate, communicate, fix, and approve risky production changes; this is planning, not incident-management software.

## Two disappearance tests and portability

Ask whether customer/Local Works can recover source, deployment, accounts, documentation, current state, issues, requirements, tests, vendor contacts, architecture, and access recovery if the partner vanishes. Then ask whether the customer can understand what exists, who delivered it, accounts/subscriptions, source, and support if Local Works vanishes. Outcomes are RECOVERABLE, RECOVERABLE_WITH_EFFORT, HIGH_RISK, NOT_RECOVERABLE, or UNKNOWN.

Portability is the effort of changing providers. Common technology, source/deployment access, exportability, documentation, and distributed knowledge lower effort; partner-only tooling, vendor lock-in, and knowledge concentration may increase it. Proprietary tooling is not inherently bad—its transition consequences must be explicit. Controls exist for continuity, not suspicion, and customer service value must not rely on hostage dependency.

## Risk register and readiness gate

Record category, severity, evidence, mitigation, owner, blocking status, and state; avoid an opaque score. Hard blockers can include unrecoverable critical assets, single-external-person credentials, unowned major work, refused reasonable documentation, unsafe customer access, unknown deployment ownership, unacceptable partner-only lock-in, unsupported critical dependencies, or unresolved scope/change authority. Smaller or noncritical documentation/dependency risks may be monitored.

The explicit gate is READY_FOR_KICKOFF, READY_WITH_MONITORED_RISKS, NEEDS_CONTROL_REMEDIATION, NEEDS_DOCUMENTATION_PLAN, NEEDS_ACCESS_PLAN, NEEDS_RESPONSIBILITY_CLARIFICATION, NEEDS_PARTNER_RENEGOTIATION, REOPEN_DELIVERY_SELECTION, or BLOCKED. Provider preference does not imply kickoff readiness, and the assessment never starts work.
