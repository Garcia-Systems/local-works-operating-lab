# Harbor Fitness — QA and acceptance

**FICTIONAL TRAINING RECORD**  
**Business:** Harbor Fitness  
**Project:** Membership-freeze configuration and technical validation  
**Scope version:** HF-SCOPE-14-v1  
**Requirements baseline:** HF-REQ-21-v1  
**Acceptance criteria:** AC-01 routine requests avoid re-entry while exceptions reach an authorized decision and status is recorded; AC-02 safe access and transition-ready findings.  
**QA readiness:** Initially ready for Local Works QA after fictional delivery-team checks; not ready for customer review until HF-D01 passes retest.

All testing and acceptance activity is fictional. **No real customer system or personal data is used.** Synthetic memberships contain no PII or credentials. The scenario validates bounded platform capability/configuration; it does not invent a custom portal or execute production deployment.

## TEST CASES

| Test ID | Title | Type | Requirement | Business rule | Criterion | Preconditions | Expected result | First actual result | Final status | Evidence/reference | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| HF-T01 | Standard eligible freeze | WORKFLOW | R-002 | BR-01 standard eligible bypasses review | AC-01 | Synthetic standard membership | No manager re-entry | Incorrectly routed to manager | PASS after retest | QA-C1/HF-T01; QA-C2/HF-T01 | Real defect caught before customer |
| HF-T02 | Exception membership | BUSINESS_RULE | R-003 | BR-03 special membership requires manager | AC-01 | Synthetic special membership | Authorized manager route | Correct route | PASS | QA-C1/HF-T02 | Meaningful exception |
| HF-T03 | Denied status | DATA | R-001 | BR-02 decisions retain status | AC-01 | Synthetic review case | Denied status recorded | Recorded | PASS | QA-C1/HF-T03 | No real record |
| HF-T04 | Confirmation | USABILITY | R-005 | — | AC-02 | Completed fictional request | Clear outcome | Understandable but awkward | PASS | QA-C1/HF-T04 | Cosmetic known issue |
| HF-T05 | Unauthorized approval | SECURITY_ACCESS | R-004 | Only authorized manager decides | AC-02 | Ordinary fictional staff role | Approval refused | Refused | PASS | QA-C1/HF-T05 | Not penetration testing/certification |
| HF-T07 | Failed platform update | ERROR_HANDLING | R-001 | Failed write is not success | AC-01 | Simulated vendor failure | Visible failure; follow-up possible | Visible; no false success | PASS | QA-C1/HF-T07 | Conceptual sandbox |
| HF-TR01 | Routing regression | REGRESSION | R-002/R-003 | BR-01/BR-03 | AC-01/AC-02 | HF-D01 fix | Standard, exception, confirmation remain correct | All pass | PASS | QA-C2/HF-TR01 | Lightweight regression |

## DEFECTS

**Defect ID:** HF-D01  
**Summary:** Standard eligible membership incorrectly routes to manager.  
**Related requirement/test:** R-002 / HF-T01  
**Severity / priority:** HIGH / HIGH (impact and timing are distinct)  
**Expected:** Eligible routine request bypasses manager.  
**Actual:** Manager review required.  
**Business impact:** The agreed core routine workflow cannot complete without avoidable re-entry.  
**Owner:** Fictional delivery partner  
**Status:** CLOSED after PASSED_RETEST  
**Retest result:** PASS; three fictional defect-correction hours, no customer charge.

**Defect ID:** HF-D02  
**Summary:** Confirmation wording is awkward.  
**Related requirement/test:** R-005 / HF-T04  
**Severity / priority:** COSMETIC / LOW  
**Expected/actual:** Natural wording / understandable awkward wording.  
**Business impact:** No workflow impact.  
**Owner/status:** Fictional delivery partner / ACCEPTED_AS_KNOWN_ISSUE  
**Retest result:** Not required for acceptance.

**Defect ID:** HF-D03  
**Summary:** Customer requests cancellation during UAT.  
**Status:** NOT_A_DEFECT. Chapter 24 classification is CUSTOMER_ENHANCEMENT / SCOPE_CHANGE because R-006 excludes it. It is not smuggled into defect correction.

## KNOWN ISSUES

**Issue:** Awkward confirmation wording  
**Severity:** COSMETIC  
**Workaround:** Outcome and next step remain understandable.  
**Impact:** No workflow impact.  
**Treatment:** Revise copy after acceptance; track explicitly.  
**Accepted by:** Fictional Harbor sponsor  
**Status:** Accepted, nonblocking; review at next planned review.

## REQUIREMENT COVERAGE

| Requirement | Test coverage | Current result |
|---|---|---|
| R-001 | HF-T03, HF-T07 | PASS |
| R-002 | HF-T01, HF-TR01 | PASS after fix/retest |
| R-003 | HF-T02, HF-TR01 | PASS |
| R-004 | HF-T05 | PASS |
| R-005 | HF-T04 | PASS with disclosed cosmetic issue |

No approved MUST is `UNTESTED_REQUIREMENT`. AC-01 and AC-02 have explicit passing evidence; acceptance is not “looks good.”

## ACCEPTANCE

**Customer acceptance session:** 2026-09-19 fictional session: scope restated; workflow demonstrated; customer ran standard and exception cases and observed confirmation; exceptions, known issue, and handoff were reviewed.  
**Ready for acceptance date:** 2026-09-18  
**Customer review / acceptance date:** 2026-09-19 / 2026-09-19 (kept separate so delay causality can be preserved).  
**Acceptance blockers:** None after HF-D01 passed retest.  
**Open defects:** HF-D02 only, explicitly nonblocking known issue.  
**Known issues:** Awkward confirmation wording.  
**Customer change requests:** Cancellation, routed to Chapter 24 and not included.  
**Acceptance decision:** **ACCEPTED_WITH_KNOWN_ISSUES**.  
**Acceptance evidence:** Fictional acceptance checklist HF-UAT-01 and fictional QA report; no signature or email was actually produced.

Metrics: 7 final tests passed, 0 failed, 1 HIGH defect corrected, 1 COSMETIC known issue, 1 fix/retest cycle, 5/5 MUST requirements covered, and **0 QA escapes** because Local Works caught the avoidable core defect before customer review. This acceptance says the agreed validation is fit; it does not prove adoption, saved time, support reduction, satisfaction, or long-term ROI.
