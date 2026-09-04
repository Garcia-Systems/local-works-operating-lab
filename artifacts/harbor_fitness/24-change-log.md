# Harbor Fitness — Chapter 24 Change Log

**FICTIONAL TRAINING RECORD**  
**Business:** Harbor Fitness  
**Project:** membership-freeze configuration validation  
**Current scope version:** HF-SCOPE-14-v1 (Chapter 14 revision B; cancellation excluded)  
**Current requirements baseline:** HF-REQ-21-v1  
**Current forecast:** 2026-09-15; **delivery estimate:** 18h baseline / 22h Chapter 23 forecast

All changes are fictional training events. No real customer change orders are being issued and no changed work is executed.

## CHANGE ITEM — CH-001
**Change ID:** CH-001  
**Requested by/source:** Harbor/customer  
**Request:** Let members cancel through the freeze workflow.  
**Date:** 2026-09-04  
**Related scope item:** membership cancellation exclusion  
**Related requirement:** R-006 (NOT_IN_SCOPE)  
**Classification:** CUSTOMER_ENHANCEMENT + SCOPE_CHANGE  
**Baseline comparison:** Adds policy, workflow, payment/retention analysis, testing, and acceptance.  
**Was included before:** NO  
**Materiality:** MAJOR  
**Delivery effort impact:** 24h, LOW confidence  
**Local Works effort impact:** 5h  
**Customer effort impact:** 4h policy/review  
**Cost impact:** $3,600 incremental delivery cost; illustrative $6,000 price; $500 recurring cost; separate figures  
**Schedule impact:** approximately +14 days if inserted; baseline forecast retained because phased  
**Risk impact:** authorization, payment, retention, additional acceptance paths  
**Customer-value impact:** illustrative $500/year—insufficient for current insertion  
**Options considered:** paid approval; scope trade; PHASE_LATER; defer; reject  
**Decision:** PHASE_LATER  
**Commercial treatment:** no current price; separately discover and price only if later pursued  
**Approver:** fictional shared customer decision maker / Local Works recommendation  
**New scope version if applicable:** none  
**New requirements baseline if applicable:** none  
**Forecast impact:** none  
**Status:** DEFERRED  
**Rationale:** preserve the freeze-validation launch and retain a potentially useful idea.

## CHANGE ITEM — CH-002
**Change ID:** CH-002 | **Requested by/source:** Harbor/customer | **Date:** 2026-09-04  
**Request:** Adjust confirmation wording. | **Related scope item:** confirmation | **Related requirement:** R-004  
**Classification:** CLARIFICATION | **Was included before:** YES | **Materiality:** TRIVIAL  
**Baseline comparison:** wording only; meaning and acceptance unchanged.  
**Delivery effort impact:** 0.17h | **Local Works effort impact:** 0.08h | **Customer effort impact:** 0h  
**Cost impact:** absorbed; customer price $0 | **Schedule impact:** none | **Risk impact:** negligible  
**Customer-value impact:** clearer copy | **Options considered:** absorb; batch; defer  
**Decision:** ABSORB | **Commercial treatment:** goodwill, under 30 minutes, no precedent | **Approver:** Local Works  
**New scope version if applicable:** none | **New requirements baseline if applicable:** none | **Forecast impact:** none  
**Status:** ABSORBED | **Rationale:** negligible effort and no boundary expansion.

## CHANGE ITEM — CH-003
**Change ID:** CH-003 | **Requested by/source:** testing | **Date:** 2026-09-04  
**Request:** Correct eligible standard case routed to manager. | **Related scope item:** eligible freeze route | **Related requirement:** R-002 / AC-01  
**Classification:** DEFECT + DELIVERY_CORRECTION | **Was included before:** YES | **Materiality:** MATERIAL  
**Baseline comparison:** approved behavior explicitly bypasses staff re-entry/review.  
**Delivery effort impact:** 3h | **Local Works effort impact:** 1h | **Customer effort impact:** 0.5h validation  
**Cost impact:** delivery correction; customer price $0 | **Schedule impact:** assess within current forecast  
**Risk impact:** acceptance fails until corrected | **Customer-value impact:** restores approved outcome  
**Options considered:** correct/retest; investigate evidence | **Decision:** APPROVE_WITHOUT_PRICE_CHANGE  
**Commercial treatment:** Local Works/delivery responsibility | **Approver:** Local Works technical-correction authority  
**New scope version if applicable:** none | **New requirements baseline if applicable:** none | **Forecast impact:** monitored, not yet changed  
**Status:** APPROVED CORRECTION, NOT EXECUTED | **Rationale:** customers are not charged for failure to meet R-002.

## CHANGE ITEM — CH-004
**Change ID:** CH-004 | **Requested by/source:** vendor evidence | **Date:** 2026-09-04  
**Request:** Respond to lack of expected configurable routing. | **Related scope item:** configuration-first validation | **Related requirement:** R-001/R-003  
**Classification:** TECHNICAL_DISCOVERY + DEPENDENCY_CHANGE | **Was included before:** UNKNOWN | **Materiality:** MAJOR  
**Baseline comparison:** invalidates a capability assumption, not evidence of customer expansion.  
**Delivery effort impact:** UNKNOWN | **Local Works effort impact:** UNKNOWN | **Customer effort impact:** UNKNOWN  
**Cost impact:** UNKNOWN; no customer price | **Schedule impact:** solution review may affect forecast | **Risk impact:** configuration path may be infeasible  
**Customer-value impact:** unchanged outcome need | **Options considered:** alternative configuration; integration; reduce scope; leave alone  
**Decision:** REVISIT_SOLUTION | **Commercial treatment:** decide after causality/evidence | **Approver:** shared if scope/commercial effect follows  
**New scope version if applicable:** none | **New requirements baseline if applicable:** none | **Forecast impact:** pending evidence  
**Status:** IMPACT_ANALYSIS | **Rationale:** do not blame Harbor for vendor capability.

## CHANGE ITEM — CH-005
**Change ID:** CH-005 | **Requested by/source:** Harbor/customer | **Date:** 2026-09-04  
**Request:** Include family memberships. | **Related scope item:** membership types | **Related requirement:** open decision D1  
**Classification:** REQUIREMENT_CORRECTION / SCOPE_AMBIGUITY | **Was included before:** AMBIGUOUS | **Materiality:** UNKNOWN  
**Baseline comparison:** prior wording does not establish either party's interpretation.  
**Delivery effort impact:** UNKNOWN | **Local Works effort impact:** review required | **Customer effort impact:** policy evidence required  
**Cost impact:** UNKNOWN/no price proposed | **Schedule impact:** UNKNOWN | **Risk impact:** eligibility and authorization  
**Customer-value impact:** UNKNOWN | **Options considered:** clarify; review history/policy; revise requirement fairly  
**Decision:** RETURN_FOR_CLARIFICATION | **Commercial treatment:** undecided | **Approver:** SHARED after evidence  
**New scope version if applicable:** none | **New requirements baseline if applicable:** none | **Forecast impact:** pending  
**Status:** CLASSIFYING | **Rationale:** bad scope wording creates shared commercial risk, not automatic customer fault.

## Register summary
- **ACTIVE CHANGES:** CH-004, CH-005
- **APPROVED CHANGES:** no scope expansions; CH-003 correction authorized but not executed
- **ABSORBED CHANGES:** CH-002 plus seven fictional 0.5h combined copy adjustments
- **DEFERRED IDEAS:** CH-001 cancellation / Phase 2
- **REJECTED CHANGES:** none; irrational current insertion was not approved
- **DEFECTS / CORRECTIONS:** CH-003
- **CUMULATIVE ABSORBED EFFORT:** 4.0 combined delivery/Local Works hours; future freebies require formal review
- **Baseline lineage:** HF-SCOPE-14-v1 and HF-REQ-21-v1 remain immutable/current; no successor baseline is created for a deferred request.
