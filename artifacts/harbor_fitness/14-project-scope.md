# Chapter 14 — Project scope

> **This is a fictional training scope.**
> **This is not a proposal.**
> **This is not a contract.**
> **No customer price has been established.**
> **No delivery partner has been selected.**

**Business:** Harbor Fitness
**Opportunity:** Reduce repeated handling of membership-freeze requests.
**Scope status:** NEEDS_VALIDATION
**Business outcome:** Designed to reduce administrative work in the membership-freeze workflow while preserving eligibility rules and manager approval for exceptions.
**Problem statement:** Eligible membership-freeze requests currently require repeated front-desk and manager handling. Chapter 13's $2,450 annual labor-capacity burden was estimated; cash savings were not established.
**Solution direction:** Phase 1 validates whether bounded configuration of the existing platform is viable; implementation remains conditional.
**Trigger:** A member submits a freeze request for a defined membership type.
**End condition:** The request is approved or rejected, the decision is recorded, and confirmation is sent.

## Included workflows
- Membership-freeze request and required-data capture
- Eligibility determination using customer-approved rules
- Manager routing for exceptions
- Decision recording and confirmation communication

## Excluded workflows
- Membership cancellation; payment disputes; refunds
- Upgrades or downgrades; full account management
- Native mobile application; replacement membership platform

## Actors
Member; front desk employee; membership manager. Accounting, marketing, and corporate HR are not participants in this scope.

## Systems and classifications
- Existing membership platform — **UNKNOWN** as a configuration target pending capability validation
- Approved request mechanism — **IN_SCOPE**
- Payment processor — **DEPENDENCY_ONLY**; no modification
- Accounting platform — **OUT_OF_SCOPE**

## Functional requirements
**MUST:** Capture required information; preserve eligibility rules; route exceptions to an authorized manager; record the approval outcome.
**SHOULD:** Send confirmation automatically.
**COULD:** Provide a manager status view.
**NOT IN SCOPE:** Native mobile application and other excluded workflows.

**Non-functional considerations:** Least-privilege temporary test access; usable request entry; auditable decisions; compatibility with validated vendor capabilities.

## Assumptions
- **CONFIRMED (fictional discovery):** Harbor can document eligibility and exception rules. If false, requirements require clarification.
- **UNCONFIRMED / CRITICAL:** The current subscription supports required configuration. If false, validate another direction rather than inventing capability.

## Dependencies
- Customer decision maker and approved rules — owner: Harbor Fitness — **CONFIRMED**.
- Vendor capability, documentation, and approved test access — owner: Harbor Fitness/platform vendor — **UNCONFIRMED**; if unavailable, scope or solution direction changes.

## Responsibilities
**Customer responsibilities:** Supply approved rules and a decision maker; provide least-privilege test/admin access without emailing passwords; provide sanitized test data; review requirements; conduct acceptance testing; make policy decisions; pay approved third-party fees.
**Local Works responsibilities:** Translate discovery; clarify requirements; coordinate validation and delivery; communicate status; coordinate QA, acceptance, and documentation.
**Delivery responsibilities:** The unselected delivery team is expected to perform validated configuration/implementation, support testing/deployment, and provide technical documentation.

**Data required:** Member identifier, membership type, requested dates, eligibility and approval status.
**Data not required:** Full payment-card data, passwords, and unrelated member-profile data. No secrets or real customer data belong in this lab.

## Third-party boundaries
Local Works may coordinate a supported configuration but cannot guarantee vendor uptime, approval, pricing, perpetual API behavior, permissions, or future service changes.

## Acceptance criteria
1. Given an eligible membership, when a request is submitted, then required information and the eligibility result are recorded.
2. Given an exception, when validation completes, then it is routed to an authorized manager.
3. Given a manager decision, when the request is approved or rejected, then status is recorded and agreed confirmation is produced.

**Business success metrics:** Average staff handling time and share of routine requests completed without repeated handling, measured after an agreed observation period. These are distinct from delivery acceptance.

## Scope risks
- **INTEGRATION_UNCERTAINTY / HIGH / OPEN:** capability unknown; mitigate with bounded validation.
- **POLICY_COMPLEXITY / MEDIUM / OPEN:** exception rules may be incomplete; customer reviews the rule set.
- **THIRD_PARTY_DEPENDENCY / MEDIUM / OPEN:** vendor behavior can change; document supported boundaries.

**Potential change triggers:** Another workflow, location, membership type, integration, policy/compliance requirement, unexpectedly large migration, or vendor limitation requiring new architecture. Cancellations and family-account management are **DEFERRED**; credit-card updates are **CHANGE_LATER**, not silently included.

**Estimate-readiness decision:** **NEEDS_TECHNICAL_VALIDATION**. The preferred configuration capability and safe test access are critical and unconfirmed.
**Remaining questions:** Which native rules and notifications exist? Which membership types qualify? Can a test environment be provided? What exception evidence and review window will Harbor approve?
