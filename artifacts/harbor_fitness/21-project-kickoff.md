# Chapter 21 — Project Kickoff

**FICTIONAL TRAINING RECORD**
**Business:** Harbor Fitness
**Project:** Membership-freeze platform capability validation
**Current phase:** Pre-kickoff remediation for bounded technical/configuration validation; implementation is not selected.
**Commercial source:** HF-CLOSE-17 authorized record
**Proposal version:** HF-PROP-16-v2
**Scope version:** HF-SCOPE-14-v1
**Estimate reference:** HF-EST-19-NORTHSTAR
**Kickoff readiness:** **BLOCKED** until Chapter 20's shared-output completion condition and separate access/revocation plan are confirmed. Unknown platform capability is an intended subject of validation, not by itself a kickoff failure.

> This is a fictional training record.
> No real project has been started.

## Participants
| Role | Organization | Responsibility | Decision authority |
|---|---|---|---|
| Fictional Operations Manager / customer decision maker | Harbor Fitness | Decide policy; accept validation findings | Business rules; customer acceptance; production authorization |
| Fictional Membership Lead / customer SME | Harbor Fitness | Explain current workflow and exceptions | Recommends policy; no commercial-change authority |
| Fictional Project Lead | Local Works | Coordinate context, scope, questions, evidence, and communication | Scope interpretation; commercial-change coordination; escalation |
| Fictional Platform Specialist | Northstar Configuration Specialist (fictional) | Validate native/configuration capability and document evidence | Technical design within the validation boundary only |
| Vendor support contact (identity UNKNOWN) | Fictional membership-platform vendor | Supply authoritative capability evidence when escalated | Vendor platform statements only |

## Project context pack
**Business problem:** Freeze handling relies on staff re-entry and policy review, creating avoidable work and delay.
**Business outcome:** Determine whether a simpler configuration-first path can support the bounded freeze workflow before any implementation commitment.
**Current workflow:** Member request → staff locates membership → eligibility/policy review → routine or exception decision → status recorded → member receives a result. See Chapters 8–10 records.
**Selected solution direction:** Paid platform/configuration validation first. A custom portal has not been selected.
**Included scope:** Validate one membership-freeze workflow, relevant eligibility data, exception routing, status recording, and member-result capability.
**Excluded scope:** Cancellation, reporting, referrals, payment updates, mobile app, custom portal build, production configuration, deployment, and support.

**Acceptance criteria:** Validation produces evidence sufficient to decide whether an eligible routine request can avoid staff re-entry while exceptions receive an authorized decision and status/result can be recorded. It must also deliver findings, limitations, evidence, and open questions into shared records.

**Known assumptions:** Customer policy remains authoritative; vendor capability is unconfirmed; validation uses fictional/test data and separate least-privilege access.
**Dependencies:** Harbor policy decisions and access authorization; platform test capability; vendor evidence where required.
**Delivery risks carried forward:** Shared findings/evidence and access/revocation controls require confirmation; vendor uncertainty and specialist concentration remain monitored. References: `14-project-scope.md`, `19-technical-estimates.md`, and `20-delivery-risk-and-ownership.md`.

## Kickoff agenda
1. Business problem
2. Desired business outcome
3. Approved scope
4. Excluded scope
5. Current workflow
6. Selected solution path
7. Major assumptions
8. Constraints
9. Responsibilities
10. Technical approach and estimate assumptions
11. Requirements baseline
12. Open technical questions
13. Testing and acceptance
14. Communication cadence
15. Decision and escalation path
16. Next milestone

## Coordination
**Communication cadence:** Weekly concise update for Harbor decision maker, SME, Local Works lead, and specialist; milestone review at validation findings; asynchronous question register; urgent blockers through Local Works. No daily meeting is assumed.
**Escalation path:** Specialist question → Local Works triage → Harbor SME for workflow facts → Harbor decision maker for policy/scope/acceptance → vendor for platform limitation. Local Works coordinates commercial implications; the specialist cannot self-authorize expansion.
**Next milestone:** Control remediation, then kickoff; after kickoff, approve the validation requirements baseline.
**Final kickoff status:** **BLOCKED — PREPARATION ONLY.** Kickoff must not begin until the small Chapter 20 control conditions are met.
