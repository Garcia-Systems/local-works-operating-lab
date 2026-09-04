# Harbor Fitness Requirements Baseline

**FICTIONAL TRAINING RECORD**
**Project:** Membership-freeze platform capability validation
**Baseline version:** HF-REQ-21-v0.1
**Status:** DRAFT
**Phase boundary:** Capability/configuration validation only; no implementation is authorized.

> This is not a technical design specification. It contains no API endpoints, architecture, database schema, credentials, or production work.

## Requirements
| ID | Type | Priority | Statement | Source | Evidence/reference | Related scope item | Related acceptance criterion | Status | Open questions / notes |
|---|---|---|---|---|---|---|---|---|---|
| R-001 | BUSINESS_RULE | MUST | Validation must determine whether the platform can preserve Harbor's confirmed freeze eligibility rules without inventing policy. | SCOPE | HF-SCOPE-14-v1 | Freeze-workflow validation | AC-01 | READY_FOR_IMPLEMENTATION | Unknown policy remains customer-owned |
| R-002 | FUNCTIONAL | MUST | Validation must determine whether a routine eligible request can avoid staff re-entry of member-submitted information. | ACCEPTANCE_CRITERIA | HF-SCOPE-14-v1 acceptance | Freeze-workflow validation | AC-01 | READY_FOR_IMPLEMENTATION | Q-01, Q-02 |
| R-003 | FUNCTIONAL | MUST | Validation must determine whether exception cases can route to an authorized staff decision and the decision/status can be recorded. | WORKFLOW | HF-WORKFLOW-09 / HF-SCOPE-14-v1 | Exception path | AC-01 | NEEDS_CLARIFICATION | Q-02, Q-04 |
| R-004 | ACCESS | MUST | Validation must use separate, least-privilege, temporary access; Harbor staff must not share personal passwords. | DELIVERY_CONTROL | HF-DELIVERY-CONTROL-20 | Validation access | Evidence delivered safely | BLOCKED | Q-03; access plan must be confirmed |
| R-005 | DOCUMENTATION | MUST | The specialist must place capability findings, test evidence, limitations, configuration observations, vendor references, and open questions in shared records. | DELIVERY_CONTROL | HF-DELIVERY-CONTROL-20 | Validation output | Findings support path decision | BLOCKED | Chapter 20 completion condition |
| R-006 | FUNCTIONAL | NOT_IN_SCOPE | Add a membership-cancellation workflow. | CUSTOMER_STATEMENT example | Kickoff feature-dump simulation | None | None | OUT_OF_SCOPE | Potential change/future discovery; not baseline scope |

## Business rules
**Known:** Harbor owns eligibility policy; routine and exception cases are distinct; exception decisions require authorized Harbor staff.
**UNKNOWN:** Exact exception categories, maximum duration, treatment of special/promotional memberships, and which manager role approves each exception. Delivery must not guess “90 days” or any other rule.

## Open questions
| ID | Question | Category | Owner | Blocking | Status | Why it matters / evidence |
|---|---|---|---|---|---|---|
| Q-01 | Does the platform support a configurable freeze workflow? | VENDOR | Fictional Platform Specialist | YES | OPEN | Determines configuration viability; HF-EST-19-NORTHSTAR |
| Q-02 | Can required eligibility data be read and decision/status written using existing capability? | TECHNICAL | Fictional Platform Specialist | YES | OPEN | Determines bounded workflow viability; HF-EST-19-NORTHSTAR |
| Q-03 | What test environment and separate temporary role are available? | ACCESS | Harbor decision owner | YES | OPEN | Blocks safe validation; HF-DELIVERY-CONTROL-20 |
| Q-04 | Which exception cases and manager roles require approval? | BUSINESS_RULE | Harbor Operations Manager | YES | OPEN | Blocks exception-rule validation; evidence UNKNOWN |
| Q-05 | Who is the vendor support contact? | VENDOR | Local Works Project Lead | NO | OPEN | Useful escalation detail; does not block kickoff once support route exists |

## Data requirements
Required business data categories are member identifier, membership type, requested dates, reason category if policy requires it, eligibility result, approval decision, status, and timestamps. Use fictional/test data. These categories do not prescribe tables or a production database schema.

## System interaction requirements
At a business-capability level, validation asks whether the platform can read eligibility information, accept/request status, record an approval decision, and provide a clear member result. No endpoint or integration mechanism is assumed.

## Exception requirements
Validate or document expected business behavior for member not found, review-required membership, duplicate request, invalid date range, approval denied, vendor unavailable, and failed status write. This baseline does not over-design technical recovery.

## Security/access requirements
A member must not gain access to another member's request; only authorized staff may decide exceptions; specialist access must be role-appropriate, separate, temporary, and revocable; credentials must not be exposed. Authorization architecture is deferred.

## Usability/accessibility and operations
If a customer-facing configurable workflow is viable, instructions, labels, keyboard use, and errors must be understandable. Determine whether staff need a way to identify pending exceptions and failed requests; do not assume an admin panel.

## Documentation requirements
Produce a compact configuration/capability summary, evidence, business-rule mapping, open questions, known limitations, support/escalation notes, and access-revocation confirmation. No giant manual is required.

## Test requirements and acceptance traceability
- **AC-01:** An eligible routine freeze request can avoid staff re-entry, while exceptions reach an authorized decision and status/result can be recorded → **R-001, R-002, R-003**.
- Evidence and limitations are transition-ready enough to support the next path decision → **R-004, R-005**.
Detailed QA execution belongs to Chapter 25.

## Out-of-scope requests
Cancellation, reporting, referral program, payment updates, mobile app, custom portal, and production implementation are **OUT_OF_SCOPE**. They may be future discovery or potential change, but are not requirements merely because someone mentioned them at kickoff.

## Requirements readiness decision
**NEEDS_BUSINESS_DECISIONS** and, independently, **NEEDS_TECHNICAL_VALIDATION** and **NEEDS_ACCESS**. The single gate result is **NEEDS_BUSINESS_DECISIONS** because Q-04 prevents a valid exception-rule baseline; Q-01–Q-03 are explicit subsequent blockers. Chapter 20 remediation also keeps kickoff blocked. Implementation has not started and cannot start from this draft.
