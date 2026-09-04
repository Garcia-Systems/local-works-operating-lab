# Harbor Fitness — business-to-technical translation

**FICTIONAL TRAINING RECORD**

Business: Harbor Fitness  
Project phase: paid technical validation / configuration-first  
Scope version: HF-SCOPE-14-v1  
Requirements baseline: HF-REQ-21-v0.1

This is a fictional training record. It is not a technical architecture specification. No real customer system is being modified.

## Translation records

### TR-001 — routine freeze request
**Source statement:** “We want members to stop having to call for routine freezes.” — fictional Operations Manager, kickoff notes.  
**Business intent:** Reduce unnecessary staff intervention while preserving Harbor membership policy.  
**Related requirement:** R-002, sourced from HF-SCOPE-14-v1 acceptance: validate whether routine requests avoid staff re-entry.  
**Related business rule:** BR-03, standard eligibility policy; exact criteria remain customer-controlled and partly UNKNOWN.  
**Workflow behavior:** Member supplies a request; confirmed rules distinguish routine and exception paths; routine information is not re-entered by staff.  
**Data needs:** member identifier (CUSTOMER_INPUT/existing-platform match); membership type/status (EXISTING_PLATFORM, access unconfirmed); dates (CUSTOMER_INPUT); eligibility (DERIVED only from confirmed rules).  
**System interaction needs:** Collect and associate required information, evaluate or route it, and record an accurate result.  
**Technical need:** TN-001 determine whether existing capability can collect required freeze information and apply or route eligibility behavior.  
**Technical questions:** TQ-001 platform freeze workflow? TQ-002 can eligibility data be read and status written?  
**Technical constraints:** configuration-first scope; platform capability and test access UNKNOWN.  
**Technical task(s):** TT-001 validate platform freeze capability; TT-002 map confirmed rules to configurable behavior.  
**Test linkage:** T-001 routine eligible case avoids staff re-entry.  
**Acceptance linkage:** AC-01.  
**Status:** NEEDS_TECHNICAL_CLARIFICATION.  
**Risks:** Delivery must not convert unknown policy into configuration.

### TR-002 — exception approval
**Source statement:** “Managers only need to review unusual freeze requests.” — fictional Membership Lead.  
**Business intent:** Preserve accountable human decisions for exceptions without burdening routine work.  
**Related requirement:** R-003, from HF-WORKFLOW-09.  
**Related business rule:** BR-04 exceptions require authorized review; exact exception categories remain UNKNOWN under BQ-001.  
**Workflow behavior:** Standard eligible case bypasses manager review; confirmed exception enters an authorized decision path and records status.  
**Data needs:** eligibility result (DERIVED); approval status and decision timestamp (source/destination UNKNOWN until capability validation).  
**System interaction needs:** Authorized staff can identify, decide, and record exception status.  
**Technical need:** TN-002 distinguish standard/exception behavior using confirmed policy and validate authorized routing.  
**Technical questions:** TQ-003 can exception requests route to manager review and record status?  
**Technical constraints:** vendor-controlled workflow may limit routing.  
**Technical task(s):** TT-003 validate exception routing; depends on BQ-001/BR-04 confirmation.  
**Test linkage:** T-002 standard case avoids queue; T-003 exception enters manager queue.  
**Acceptance linkage:** AC-01 customer confirms both behaviors.  
**Status:** NEEDS_BUSINESS_CLARIFICATION.  
**Risks:** Automatically processing all freezes would lose business intent.

### TR-003 — member confirmation
**Source statement:** “Members should know whether the freeze worked.” — fictional Membership Lead.  
**Business intent:** Give members an accurate outcome and avoid uncertainty or repeat contact.  
**Related requirement:** R-002 and R-005.  
**Related business rule:** A failed platform write is not a successful freeze.  
**Workflow behavior:** Communicate final or pending status accurately; surface failures for follow-up.  
**Data needs:** request status and decision time (source/destination UNKNOWN).  
**System interaction needs:** Workflow can communicate status; email, SMS, in-platform notice, or another design is not selected.  
**Technical need:** TN-003 validate status/notification capability and truthful failure behavior.  
**Technical questions:** TQ-004 can the platform send confirmation?  
**Technical constraints:** existing notification capability UNKNOWN.  
**Technical task(s):** TT-004 validate member notification behavior; TT-005 document gaps.  
**Test linkage:** T-004 successful and failed writes produce accurate, distinguishable outcomes.  
**Acceptance linkage:** AC-01 and documented-findings acceptance.  
**Status:** NEEDS_TECHNICAL_CLARIFICATION.  
**Risks:** False success or silently lost request.

### TR-004 — access and security
**Source statement:** “Make sure member information is secure.” — fictional Operations Manager.  
**Business intent:** Limit personal-data access and approval to appropriate people during validation.  
**Related requirement:** R-004, from HF-DELIVERY-CONTROL-20.  
**Related business rule:** Members access only their own request; approval is restricted to authorized staff.  
**Workflow behavior:** Specialist uses separate least-privilege, revocable test/admin access; passwords are not shared.  
**Data needs:** only necessary member and request information; no credentials in project records.  
**System interaction needs:** Enforce business-level access behavior using available platform controls.  
**Technical need:** TN-004 validate least-privilege access and role behavior without inventing an identity architecture.  
**Technical questions:** TQ-005 what sandbox/test mode and roles are available?  
**Technical constraints:** safe test access is not yet confirmed.  
**Technical task(s):** Covered by validation access precondition; no custom identity task.  
**Test linkage:** T-005 unauthorized member/staff behavior is denied in available test mode.  
**Acceptance linkage:** R-004 evidence review.  
**Status:** NEEDS_TECHNICAL_CLARIFICATION.  
**Risks:** Shared access or excessive privileges.

### TR-005 — cancellation request
**Source statement:** “Could members cancel there too?” — fictional stakeholder.  
**Business intent:** Reduce calls for an adjacent workflow; it has not been discovered or approved.  
**Related requirement:** R-CANCEL-01, OUT_OF_SCOPE, provenance HF-SCOPE-14-v1 exclusion.  
**Related business rule:** UNKNOWN; none may be invented.  
**Workflow behavior:** Not part of this validation.  
**Data needs:** Not analyzed.  
**System interaction needs:** None in current scope.  
**Technical need:** None.  
**Technical questions:** None until separately authorized.  
**Technical constraints:** Explicit scope exclusion.  
**Technical task(s):** None.  
**Test linkage:** None.  
**Acceptance linkage:** None.  
**Status:** OUT_OF_SCOPE.  
**Risks:** Silent scope expansion if converted into a task.

## Business questions

- **BQ-001 (blocking, Harbor Operations Manager):** Which membership types and conditions require manager approval? Answer/evidence: UNKNOWN.
- **BQ-002 (nonblocking until notification design):** What member wording accurately distinguishes pending, successful, and failed outcomes? Answer/evidence: UNKNOWN.

## Technical questions

- **TQ-001:** Does the platform support configurable freeze workflow? OPEN; delivery technical lead; blocking.
- **TQ-002:** Can membership type/status be exposed and freeze status recorded? OPEN; delivery technical lead; blocking.
- **TQ-003:** Can exceptions route to authorized manager review? OPEN; delivery technical lead; blocking.
- **TQ-004:** Can existing capability communicate member status? OPEN; delivery technical lead; blocking.
- **TQ-005:** Is a safe sandbox/test mode available? OPEN; Harbor technical contact/vendor; blocking.

## Technical tasks

- **TT-001 VALIDATE_CAPABILITY:** Validate platform freeze capability. Done when capability, evidence, limitations, and UNKNOWNs are recorded; depends on safe access.
- **TT-002 CONFIGURE/VALIDATE:** Map only confirmed Harbor rules to configurable behavior. Done when each confirmed rule is supported, unsupported, or UNKNOWN with evidence; depends on BQ-001.
- **TT-003 VALIDATE_CAPABILITY:** Validate exception routing. Done when standard and exception test results and authorization observations are recorded; depends on TT-001 and BR-04.
- **TT-004 VALIDATE_CAPABILITY:** Validate member notification behavior. Done when available status behavior and truthful failure result are evidenced; depends on notification capability.
- **TT-005 DOCUMENT:** Document capability gaps. Done when each gap has requirement impact and redesign/scope/solution escalation.
- **TT-006 INVESTIGATE:** Prepare recommendation if configuration is insufficient. Done when proportional options and impacts are presented without starting custom work; depends on TT-001–TT-005.

## Traceability examples

1. “stop having to call” → reduce staff intervention → R-002 → WB-routine → TN-001 → TT-001 → T-001 → AC-01.
2. “Managers only…unusual” → accountable exception review → R-003/BR-04 → WB-exception → TN-002 → TT-003 → T-002/T-003 → AC-01.
3. “know whether…worked” → accurate outcome → R-002/R-005 → WB-confirmation → TN-003 → TT-004 → T-004 → documented acceptance.

## Translation gaps

A deliberate demonstration requirement—“staff can identify unresolved failed writes”—has no assigned technical task. **TRANSLATION GAP:** it must be covered before implementation readiness; it is not permission to invent a dashboard.

## Unjustified technical work

A proposed real-time analytics dashboard has no requirement, acceptance, scope outcome, or operational-risk link: **NO BUSINESS JUSTIFICATION / TECHNICAL EXPANSION REQUIRES JUSTIFICATION.** Logging failed writes could be legitimate invisible work when linked to reliability risk.

## Open constraints

The platform interface, writable status, routing, notification, and sandbox remain UNKNOWN. If required routing is absent, first consider an evidenced design alternative within configuration. If none meets R-003, **REVISIT_SOLUTION**; if Harbor elects to remove approval behavior, **REVISIT_SCOPE / CUSTOMER_DECISION_REQUIRED**. No major custom workaround is silently authorized.

## Final translation readiness

**NEEDS_BUSINESS_CLARIFICATION**, with technical validation also required. BQ-001 blocks safe rule mapping, and vendor capability questions block implementation selection. Current work remains the approved paid validation phase—not implementation.
