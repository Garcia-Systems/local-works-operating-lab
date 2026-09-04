# Chapter 27 — Warranty vs Support vs New Work

## Part VII — Own the Relationship After Launch

> **Core question:** When a customer contacts Local Works after launch, how do we decide whether the request is a defect we owe, included support, billable support, a new feature, or a new project?

The operating path is **contact → triage → classify → check warranty, entitlement, and scope history → determine responsibility → determine commercial treatment → resolve, support, quote, escalate, or decline → record learning**. Every post-launch request must not become free support; every problem must not become a sales pitch. The aim is **fair continuity**.

## 1. The post-launch boundary problem
“That’s extra” for every problem abandons a customer. “No problem” forever makes the owner an unpaid help desk. A fair boundary acknowledges first, investigates evidence, and explains the path.

## 2. Warranty vs support
Warranty is a limited operational obligation to correct delivered work that fails approved scope, requirements, or acceptance criteria under modeled assumptions. Support is ongoing help operating, maintaining, troubleshooting, coordinating, or adjusting it. This chapter does not draft legal language.

## 3. Support vs new work
“Where is the confirmation setting?” concerns existing operation. “Add cancellation and payment-plan changes” adds capability. Effort is not the test: a ten-minute capability can be new work and a three-hour defect diagnosis can be warranty.

## 4. Triage
Ask only questions that resolve uncertainty: what happened and when, who is affected, impact and usability, expected versus actual behavior, approved scope, whether it worked, recent changes, vendor involvement, workaround, data/security, and whether different behavior is requested. Keep source provenance and `UNKNOWN` until justified.

## 5. Warranty assessment
Trace requirement, acceptance criterion, delivered/expected behavior, acceptance history, intended workflow, timing, customer/vendor/environment changes, and evidence. Preserve applies, likely, does-not-apply, more-evidence-required, disputed, and not-applicable outcomes.

## 6. Defects after launch
If eligible freezes should bypass review but route incorrectly two days later with no external/customer change, classify defect and likely warranty. Local Works coordinates no-charge correction rather than automatically invoicing.

## 7. Customer changes
A verified administrator rule change may be customer-environment trouble plus configuration assistance, not warranty. Investigate before assigning blame.

## 8. Third-party changes
A changed vendor behavior remains a third-party issue. Entitlement, complexity, expectations, and vendor ownership shape Local Works coordination; Local Works does not claim vendor control.

## 9. How-to requests
A disable-workflow question might be how-to, documentation, or routine support. Answering a missing documented fact can be paired with improving the guide.

## 10. Training
A new manager's walkthrough is not a defect. It may be included onboarding, billable support, or separate training according to the arrangement.

## 11. Configuration assistance
Copy, recipient, and non-policy settings adjust existing capability. A new workflow rule is enhancement work even if quick.

## 12. Incidents
An incident is unexpected operational interruption or degradation needing coordinated response. Chapter 27 captures type, severity, priority, and route only; Chapter 28 owns response mechanics.

## 13. Enhancements
Pause-reason analytics changes capability. Record it as an enhancement rather than hiding testing and future support inside support.

## 14. New projects
Cancellation, a second materially different location/system, reporting suite, or platform replacement returns to discovery, economics, and design. Do not quote with insufficient evidence.

## 15. Support entitlement
Entitlement can be none, warranty-only, limited, monthly, prepaid, incident-only, or custom. None still permits sufficient triage to explain a fair path.

## 16. Support plans
A simple plan records included types/capacity, response expectation, exclusions, third-party coordination, after-hours assumption, term, and hypothetical/simulated status. It does not invent a contract or SLA.

## 17. Warranty timing
A configurable 30-day period is a fictional training assumption, not adopted policy. Timing informs but cannot alone determine responsibility; review possible latent defects after expiration.

## 18. Commercial treatment
Treatment can be no-charge warranty, included/prepaid/billable support, quote, discovery, customer/vendor handling, goodwill, or decline. Classification, responsibility, and money remain separate decisions.

## 19. Goodwill support
A ten-minute vendor-setting answer may be intentional no-charge goodwill for clarity and relationship. State the reason and record it.

## 20. Cumulative goodwill
Count requests, owner and partner time, and estimated internal cost. Otherwise kindness silently becomes a recurring obligation.

## 21. Owner time
Triage, email, diagnosis, coordination, resolution, and documentation all consume Local Works capacity. “Just an email” is not zero cost.

## 22. Delivery partner responsibility
Record partner warranty, defect response, support charges, handoff period, and contact owner. Never assume partner support is free.

## 23. Owning customer communication
Own the relationship under the chosen model without pretending to own every system. A customer should know one clear next step rather than be passed around.

## 24. Escalation paths
Customer → Local Works → partner → vendor is one path, not a ritual. Direct vendor support may reduce middleman delay while Local Works keeps the customer informed.

## 25. Security/data-sensitive requests
Potential compromise, exposure, suspicious access, leaked credentials, missing data, or excessive visibility receives urgent/high incident routing. Do not perform deep incident troubleshooting here.

## 26. Priority
Use impact, affected users, security/data, workaround, and time sensitivity—not an “URGENT!!!” subject alone. Severe/high/moderate/low incident metadata should remain proportionate.

## 27. Response vs resolution
Response is acknowledgment and start of triage. Resolution is restoration or correction. A quick response cannot promise same-day resolution.

## 28. Documentation
Each answer asks whether the runbook should cover confirmation text, pending exceptions, or disablement. Documentation reduces repeated owner work.

## 29. Repeated requests
Recurrence can expose poor usability, weak documentation/training, defect, missing feature, or process mismatch. Investigate the pattern instead of endlessly replying.

## 30. Support as discovery
History reveals needs, assumptions, and failure patterns. Link genuine expansion signals to discovery without turning every customer problem into upselling.

## 31. Disputed responsibility
When customer and partner explanations conflict, gather timeline, scope, requirements, changes, and conceptual logs/reports. Preserve `DISPUTED` or `MORE_EVIDENCE_REQUIRED` rather than manufacturing certainty.

## 32. Customers without support plans
Do not ignore a three-month-later contact and do not work without limit. Triage enough to classify, review warranty facts and policy, then offer the appropriate route plainly.

## 33. Harbor Fitness support triage
The fictional limited handoff includes two hours of how-to/configuration support. HF-SUP-01 is likely warranty; HF-SUP-02 included help; cancellation returns to discovery; the vendor issue escalates; an evidenced customer edit is billable assistance; inappropriate visibility routes urgently; a ten-minute setting answer is tracked goodwill.

## 34. Failure: everything free
Weekly copy, training, report, vendor, workflow, and troubleshooting work reaches 20 owner hours monthly. **Undefined support becomes an unpriced job.**

## 35. Failure: everything billable
Quoting a core defect two days after launch destroys trust. **Warranty responsibility matters.**

## 36. Failure: blame vendor
Immediate blame precedes evidence; later the Local Works configuration proves wrong. **Classification requires evidence.**

## 37. Failure: hidden enhancement
A “small” support change adds a rule, tests, and future burden. **Effort size does not define scope.**

## 38. Failure: no support owner
Customer, developer, vendor, and several staff communicate separately. No one owns response, so status and trust fragment.

## 39. Success: fair triage
Local Works acknowledges, checks history, identifies warranty, coordinates correction, communicates, records time, closes, and improves documentation. Later it recognizes cancellation value and routes it to discovery—not support or an instant quote.

## 40. Executable exercise
Run `python scripts/run_chapter_27.py`. It processes only fictional records, displays decisions and cumulative owner effort, and stops at incident routing and support economics boundaries.

## 41. Chapter artifacts
Use `support-triage-template.md`, `warranty-assessment-template.md`, and `support-boundary-template.md`; consult the methodology and fictional Harbor record. Production discoveries remain capability observations, not a system design.

## 42. Readiness checkpoint
The reader can distinguish warranty/support/enhancement; triage and assess evidence; identify customer, vendor, training, configuration, incident, and new-project cases; apply entitlement and commercial treatment; track goodwill/owner time; coordinate partners; prioritize impact; distinguish response/resolution; learn from recurrence; improve documentation; preserve disputes; fairly route no-plan customers; and return opportunities to discovery.

Chapter 28—incident response and support escalation—is intentionally not implemented here. Also deferred: real monitoring/tickets/messages/inbox, SLA enforcement, recurring support profitability or MRR, expansion selling, referrals, case studies, scaling, CRM, database, Laravel, and a production website.
