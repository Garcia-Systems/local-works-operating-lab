# Harbor Fitness current-state workflow

> **FICTIONAL TRAINING SCENARIO — NOT A REAL CUSTOMER WORKFLOW**
>
> **This document describes the CURRENT STATE. It does not prescribe a future-state solution.**

**Workflow:** Membership Account Management — Membership Freeze  
**Status:** `PARTIALLY_VALIDATED`  
**Trigger:** A member asks the front desk by phone or email to freeze a membership.  
**End condition:** The member receives confirmation of the recorded outcome (approved or declined).

## Actors

- **MEMBER** — initiates the request and receives the outcome.
- **FRONT_DESK_EMPLOYEE** — gathers information, checks the account and policy, records the change, and communicates.
- **MEMBERSHIP_MANAGER** — reviews unclear eligibility, medical-freeze, or overdue-balance exceptions.

## Systems/mechanisms

- Membership Management Platform — membership record, notes, eligibility context, and status.
- Spreadsheet — supplemental manual tracking; purpose and completeness require validation.
- Phone and Staff Email — communication mechanisms, not necessarily architectural systems.

## Happy path

| # | Actor | Current action | Type | Mechanism | Active time | Evidence |
|---:|---|---|---|---|---|---|
| 1 | Member | Requests freeze; provides identity | Communication | Phone/email | 2 min, estimate | Reconstructed from Ch. 8 |
| 2 | Front desk | Gathers dates and reason | Communication | Phone/email | 1 min, estimate | Employee statement |
| 3 | Front desk | Looks up account and notes | System lookup | Membership platform | 1 min, estimate | Employee statement |
| 4 | Front desk | Determines type and applies eligibility policy | Decision | Membership platform | 1 min, estimate | Manager + employee statements |
| 5 | Front desk | Records freeze and updates status | Data entry | Membership platform | **UNKNOWN** | Duration and billing behavior unknown |
| 6 | Front desk | Re-enters supplemental note | Data entry | Spreadsheet | 1 min, estimate | Employee statement |
| 7 | Front desk | Checks membership and billing status | System lookup | Membership platform | **UNKNOWN** | Integration behavior unknown |
| 8 | Front desk | Sends confirmation | Communication | Email | 1 min, estimate | Employee statement |

These allocations are fictional training assumptions used to expose incomplete arithmetic. Chapter 8 only supported an overall simple-request estimate near five minutes; it did not measure per-step time.

## Decision points

**Is the membership eligible for a freeze?**

- **YES** → record the normal change.
- **NO** → explain the policy and record/confirm the outcome; exact recordkeeping is unknown.
- **REQUIRES_APPROVAL** → send the request to the membership manager.

The decision enforces a stated business policy. Its being manual does not establish waste or suitability for automation.

## Data movement

- Identity, dates, and reason: **Member → Front desk** (`DATA_CREATED`).
- Account and notes: **Membership platform → Front desk** (`DATA_READ`).
- Request details: **Phone/email → Membership platform** (`DATA_RE-ENTERED`).
- Freeze details/status: **Membership platform/request → Spreadsheet** (`DATA_RE-ENTERED`; apparent duplicate requiring validation).
- Outcome: **Front desk → Member** (`DATA_SENT`).

## Handoffs

1. Member → front desk: request details by phone/email.
2. Front desk → member: outcome by email on the happy path.
3. Front desk → membership manager: exception context by email when approval is required.
4. Membership manager → front desk: decision; exact mechanism and ownership are unknown.

## Exception path: manager approval

**Supported triggers:** unclear eligibility, medical-freeze review, or overdue balance. After the eligibility check, front desk sends account/request context to the manager; the request waits; the manager reviews and decides; front desk records the outcome, adds the spreadsheet note, and contacts the member.

This path has **10 modeled steps rather than 8**, adds manager work and at least one handoff, and introduces an approval wait. Chapter 8 supports the existence of these exceptions and an employee estimate of **15–20 minutes** total handling, but does not support a measured step allocation or wait duration. Missing-information follow-up and ineligible membership are known possible branches but are not yet reconstructed sufficiently.

## Timing

### Known

- No workflow duration is measured.
- Approval waiting exists, but its duration is unknown.

### Estimated

- Chapter 8 manager: a normal request takes about 5 minutes.
- Chapter 8 employee: a simple request may take 5 minutes; an overdue-balance exception may take 15–20 minutes.
- The executable exercise represents 7 minutes of partial step estimates on the happy path, intentionally revealing that the new training allocation conflicts with the earlier overall estimate and needs playback/measurement.

### Unknown

- Update and billing-verification duration; approval waiting; correction/rework time; measured customer effort; whether billing updates automatically; and whether the spreadsheet is always used.
- Unknown time is not zero and is not included in a complete-total claim.

## Current workflow metrics

- Happy-path steps: 8; manual: 8; automated: 0.
- Systems/mechanisms represented: 4.
- Happy-path decision points: 1; direct happy-path handoffs: 2.
- Known data re-entry events: 2.
- Represented active time: 7 estimated minutes plus 2 unknown components; therefore no complete active-time total.
- Represented customer-visible effort: 4 estimated minutes; total customer elapsed time remains unknown.
- Known wait time: none quantified; exception wait: unknown.

Metrics describe this reconstruction; they are not an efficiency score or proof the process is bad.

## Workflow observations

- Staff manually enter request information and switch mechanisms.
- Eligibility is policy-dependent and manager approval creates an unmeasured wait.
- A spreadsheet entry appears to repeat freeze information; its business purpose remains unclear.
- Customer confirmation occurs after internal record work.

These are **workflow observations**, not solution requirements or automation recommendations.

## Questions requiring validation

1. Does platform status automatically update billing, and what verification is actually performed?
2. What exact rules produce yes, no, and manager-review branches?
3. Is the spreadsheet always used, authoritative, or required for another purpose?
4. How long does active work and approval waiting take when observed?
5. Who owns a request while it waits, and how is the manager decision returned?
6. What steps close declined, missing-information, and corrected-charge cases?

## Playback summary

“Let me make sure I understand. A member calls or emails; front desk staff gather the request, look up the account, apply eligibility policy, update the membership platform, add a spreadsheet note, verify status, and confirm the outcome. If eligibility is unclear or an exception applies, staff send it to a manager and wait for review. Is that accurate?”

**Readiness:** `YES WITH UNKNOWNS` for beginning burden measurement—not for claiming quantified economics or selecting a solution.
