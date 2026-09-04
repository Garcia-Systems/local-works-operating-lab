# Harbor Fitness — Chapter 23 project control

> **FICTIONAL TRAINING RECORD**  
> **Business:** Harbor Fitness  
> **Project:** Membership-freeze configuration and technical validation  
> **Scope version:** HF-SCOPE-14-v1  
> **Requirements baseline:** HF-REQ-21-v1  
> **Technical estimate reference:** HF-EST-19-NORTHSTAR (paid validation)  
> **All work, dates, effort, and project events are fictional training data.**

## Project baseline

| Milestone ID | Name | Planned date | Owner | Status |
|---|---|---|---|---|
| M1 | Kickoff Complete | 2026-09-01 | Local Works | Complete |
| M2 | Platform Capability Validated | 2026-09-07 | Delivery Partner | At risk |
| M3 | Configuration Path Confirmed | 2026-09-09 | Delivery Partner | Not started |
| M4 | Test Workflow Ready | 2026-09-11 | Local Works | At risk |
| M5 | Customer Review | 2026-09-14 | Shared; Local Works coordinates | Not started |
| M6 | Delivery Recommendation / Acceptance Ready | 2026-09-16 | Local Works | Not started |

These are proportional outcome checkpoints, not a milestone for every task. No acceptance is performed here.

## Tasks

| Task ID | Title | Owner | Milestone | Dependencies | Estimated effort | Actual simulated effort | Remaining estimate | Status | Done condition |
|---|---|---|---|---|---:|---:|---:|---|---|
| T1 | Validate freeze capability | Delivery Partner | M2 | Safe test access | 4h | 4h | 0h | Done | Capability evidence recorded |
| T2 | Confirm eligibility fields | Harbor Operations Manager | M3 | D1 decided | 2h | 0h | 2h | Blocked | Required fields confirmed |
| T3 | Prepare standard-case test | Delivery Partner | M4 | T1 | 2h | 2h | 0h | Done | Reproducible case documented |
| T4 | Prepare exception-route test | Delivery Partner | M4 | T2; B1 resolved | 4h | 3h | 4h | Blocked | Expected route and evidence plan recorded |
| T5 | Validate confirmation behavior | Delivery Partner | M2 | T1 | 2h | 2h | 1h | In progress | Available outcomes documented |
| T6 | Document limitations | Local Works | M4 | T1 | 2h | 1h | 1h | Ready | Known, unsupported, and UNKNOWN behavior summarized |
| T7 | Prepare customer review | Local Works | M5 | T3; T4; T5; T6 | 2h | 0h | 2h | Not started | Factual review pack ready |

## Blockers

- **Blocker ID:** B1
- **Description:** Available fictional vendor documentation does not clarify whether exception routing is configurable.
- **Category:** Vendor
- **Owner:** Vendor for clarification; Delivery Partner coordinates the question
- **Impact:** Exception-route preparation cannot finish; M2 and M4 are at risk, but documentation and standard-case work continue.
- **Affected task/milestone:** T4; M2 and M4
- **Status:** Waiting
- **Next action:** Seek fictional support clarification; record `UNKNOWN` until evidence exists.
- **Escalation:** Escalate if no answer by 2026-09-08 because M4 forecast is threatened.

## Decisions

- **Decision ID:** D1
- **Question:** Which membership types require exception approval?
- **Owner:** Harbor Operations Manager
- **Needed by:** 2026-09-02, before configuration test
- **Impact if delayed:** T2 and T4 wait and M4 forecast moves.
- **Status:** Decided after a two-fictional-day delay
- **Decision:** Use only the confirmed membership-type list supplied in the training scenario; do not invent policy.

Latency explains impact; it is not blame or a customer score.

## Forecast

- **Milestone:** M4 — Test Workflow Ready
- **Baseline date:** Friday, 2026-09-11
- **Forecast date:** Tuesday, 2026-09-15
- **Confidence:** Moderate
- **Reason:** Vendor clarification remains open and discovered platform behavior requires an additional exception case.
- **Assumptions:** Clarification arrives by 2026-09-08; no production testing occurs.

## Variance

- **Estimated effort:** 18h
- **Actual so far:** 12h simulated
- **Estimate to complete:** 10h
- **Forecast total:** 22h
- **Variance:** +4h / +22.2% (scenario precision only)

The remaining estimate was reconsidered after platform behavior emerged; it was not calculated as the unused portion of 18 hours.

## Project health

- **Scope:** Watch — cancellation request is a potential change, not work.
- **Schedule:** At risk — M4 forecasts four calendar days later.
- **Cost:** Watch — effort forecast is four hours above baseline; customer change pricing is deferred.
- **Quality:** On track — preparation, documentation, and security controls were not removed.
- **Dependencies:** At risk — vendor routing answer remains unresolved.
- **Customer decisions:** Watch — D1 arrived after a two-day fictional delay and is now decided.
- **Delivery capacity:** On track — no simulated capacity reduction.
- **Overall:** At risk
- **Rationale:** Available work continues, but unresolved dependency and variance require early reforecasting.

## Local Works owner effort

- **Customer communication:** 1.0h
- **Partner coordination:** 1.5h
- **Decision management:** 0.75h
- **QA/project review:** 1.25h (coordination/review only; no QA execution)
- **Other:** 0.5h documentation review
- **Total:** 5.0h simulated

## Scope-change signal

“Could members cancel there too?” is recorded as **POTENTIAL_SCOPE_CHANGE**. It is not a task and is not implemented. Chapter 24 is intentionally required for evaluation.

## Corrective action

**RESEQUENCE_WORK + REFORECAST:** while T4 waits, finish confirmation-behavior evidence, the limitations document, and the review skeleton. Defer optional embellishment. Do not add developers, remove quality work, or silently absorb cancellation.

## Customer update

Configuration capability and the standard-case test preparation are complete. Exception routing remains blocked on fictional vendor clarification, and Harbor's membership-type decision arrived two fictional days after needed. We are continuing confirmation evidence and limitations documentation. Test Workflow Ready was planned for Friday 11 September and is now forecast for Tuesday 15 September with moderate confidence, assuming the vendor clarification arrives by 8 September. Current effort forecasts 22 hours against the 18-hour baseline. Cancellation is logged for later scope review and is not being implemented. Harbor has no immediate action now that D1 is decided; Local Works will coordinate the vendor question and send the next factual update.

**Final project-control decision:** `CONTINUE_WITH_REFORECAST`
