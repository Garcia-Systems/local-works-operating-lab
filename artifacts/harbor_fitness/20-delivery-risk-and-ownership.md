# Chapter 20 — Delivery Risk and Ownership

**FICTIONAL TRAINING RECORD**

**Business:** Harbor Fitness  
**Current delivery stage:** Pre-kickoff planning for bounded technical/capability validation; implementation has not been selected.  
**Selected/preferred delivery path:** Northstar Configuration Specialist (fictional) performs platform validation; Bridge Integration Freelancer (fictional) remains a backup only.  
**Scope version:** HF-SCOPE-14-v1

> This is a fictional training record.  
> No real passwords, tokens, customer credentials, or production systems are included.  
> This is operational-control analysis, not legal ownership advice.

## Asset register

| Asset | Type | Primary control | Admin access | Backup/recovery | Transferability | Status | Notes |
|---|---|---|---|---|---|---|---|
| Membership platform admin | Vendor account | Customer | Customer; approved delegated access planned | Customer recovery with vendor; Local Works approved backup planned | Customer can replace delegate | CONTROLLED | Customer authorization governs access |
| Technical-discovery notes | Documentation | Local Works | Local Works | Customer receives project export | Portable files | CONTROLLED | Must include open questions and vendor references |
| Configuration record | Deployment configuration | Shared | Customer and specialist during validation | Local Works receives shared record | Common document format | NEEDS_ACTION | Completion condition, not yet delivered |
| API documentation references | Documentation | Third-party vendor | Vendor publishes; customer/partner use | Links and access requirements retained in project files | Depends on vendor availability | UNKNOWN | Native/API capability is the validation question |
| Test evidence | Test assets | Shared | Specialist creates; Local Works coordinates review | Customer receives evidence | Portable screenshots/notes, with sensitive data excluded | NEEDS_ACTION | No production data |
| Local Works project files | Project files | Local Works | Local Works | Current customer export | Portable files | CONTROLLED | Scope, estimate, risks and state |
| Customer policy rules | Requirements | Customer | Customer | Recorded in approved scope | Portable | CONTROLLED | Customer remains business authority |
| Decision log | Decision log | Local Works | Local Works | Customer receives current export | Portable | CONTROLLED | Includes decision context |
| Source repository | Source repository | N/A | N/A | N/A | N/A | NOT_APPLICABLE | No custom implementation has been selected or invented |

Legal ownership is deliberately not inferred from primary operational control.

## Responsibility matrix

| Responsibility | Accountable | Performs | Consulted | Informed | Status |
|---|---|---|---|---|---|
| Business policy | Customer | Customer | Local Works; Partner | Vendor as needed | ASSIGNED |
| Scope authority and interpretation | Local Works | Local Works | Customer | Partner | ASSIGNED |
| Customer communication | Local Works | Local Works | Customer | Partner | ASSIGNED |
| Technical validation/design within constraints | Delivery Partner | Delivery Partner | Local Works; Vendor | Customer | ASSIGNED |
| Project and QA coordination | Local Works | Local Works | Customer; Partner | Customer | ASSIGNED |
| Test execution/evidence | Local Works | Delivery Partner | Customer | Local Works | ASSIGNED |
| Customer acceptance | Customer | Customer | Local Works | Partner | ASSIGNED |
| Vendor escalation | Local Works | Local Works | Partner; Vendor | Customer | ASSIGNED |
| Billable scope/change approval | Local Works | Local Works | Customer decision maker | Partner | ASSIGNED; partner cannot self-authorize expansion |
| Post-launch integration monitoring | No owner | No owner | N/A | N/A | NOT_APPLICABLE to validation; GAP before any later launch |
| Payment approval | Customer | Customer | Local Works | Partner as applicable | ASSIGNED |

The customer controls required business behavior; the specialist chooses technical means within constraints. Local Works coordinates when a choice affects workflow, price, scope, risk, or maintainability.

## Knowledge artifacts

| Artifact | Required | Current holder | Documented | Location/reference | Transition readiness |
|---|---|---|---|---|---|
| Customer policy rules | Yes | Customer/shared with Local Works | Yes | HF-SCOPE-14-v1 | RECOVERABLE |
| Capability findings/configuration observations | Yes | Partner will create | No—not yet delivered | Planned validation report | RECOVERABLE_WITH_EFFORT |
| Screenshots/notes and test evidence | Yes | Partner will create | No—not yet delivered | Planned shared project files | RECOVERABLE_WITH_EFFORT |
| Open technical questions/vendor references | Yes | Shared during validation | Partial | Project issue list | RECOVERABLE_WITH_EFFORT |
| Decision context | Yes | Local Works | Yes | Decision log | RECOVERABLE |
| Architecture/deployment runbook | No for validation | N/A | N/A | N/A | NOT_APPLICABLE; reassess if implementation is selected |

Documentation is proportional to the small validation engagement. It records evidence and rationale, not an invented full-system runbook.

## Access register

| Asset | Party | Access level | Purpose | Revocation path | Status |
|---|---|---|---|---|---|
| Membership platform test environment | Customer | Administrator | Authorize and recover access | Customer/vendor recovery | ACTIVE (fictional) |
| Membership platform test environment | Delivery Partner | Least-privilege, separate, temporary | Capability validation | Customer admin removes identity at validation close | PLANNED |
| Project files | Local Works | Editor | Coordinate scope, evidence and decisions | Organizational administrator | ACTIVE (fictional) |
| Project export | Customer | Readable copy | Continuity without Local Works | Customer-controlled copy | REQUIRED REMEDIATION |

The register stores metadata only. It contains no password, token, secret, or credential value.

## Third-party dependencies

**Dependency:** Fictional membership platform  
**Criticality:** Critical to validation  
**Owner:** Customer owns the subscription/relationship; the vendor owns platform behavior  
**Support path:** Customer issue → Local Works triage → specialist/vendor investigation → Local Works customer communication  
**Failure impact:** Validation cannot confirm configuration or API capability  
**Fallback:** Pause for vendor evidence; retain integration specialist as a possible later path, not a guaranteed technical fallback  
**Status:** OPEN/MONITORED

## Continuity results

**Delivery partner disappearance result:** **RECOVERABLE_WITH_EFFORT.** Scope, policy, estimate and decisions remain available, but findings, screenshots, configuration observations, capability results, open questions, and vendor references must be placed in shared records before validation closes.

**Local Works disappearance result:** **RECOVERABLE_WITH_EFFORT.** Harbor controls its SaaS account and can identify the delivery specialist; it still needs a current export describing scope, project state, findings, decisions, subscriptions, unresolved issues, and the support path. Service value must not be hostage dependency.

## Gaps and risks

**Responsibility gaps:** Post-launch monitoring is intentionally unassigned because no implementation or launch exists. It becomes a hard gap if an integration is later authorized without an owner. Customer inactivity for policy, access, testing, or acceptance must be recorded as a customer dependency rather than silently becoming Local Works failure.

**Authority conflicts:** None accepted for Harbor validation. Customer authorizes business requirements and access; Local Works controls scope/change coordination; partner controls technical design within constraints. The failure example where customer, Local Works, two contractors and vendor support all hold unrestricted production admin is prohibited pending explicit authority and least privilege.

**Blocking risks:** The validation engagement must require delivery of findings/evidence into shared, transitionable records. Until that completion condition and the access/revocation plan are confirmed, readiness is blocked.

**Monitored risks:** Vendor response/capability uncertainty; specialist key-person concentration during the short validation; future monitoring ownership if an integration is later chosen.

**Required remediation:**
1. Make the validation report, screenshots/notes, observations, capability results, open questions and vendor references contractual completion outputs (without writing an agreement here).
2. Confirm customer-controlled, separate least-privilege test identity and documented revocation.
3. Give Harbor a current portable project/decision export and support contacts.
4. Assign deployment, monitoring and recovery only if later implementation makes them applicable.
5. Reassess source and deployment control if custom code is selected; do not invent a repository now.

**Final delivery readiness:** **BLOCKED** pending the small control remediation above. This assessment neither authorizes nor starts kickoff.
