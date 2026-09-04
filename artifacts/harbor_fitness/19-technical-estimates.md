# Harbor Fitness — technical estimates

> **FICTIONAL TRAINING RECORD**
> **All estimates are fictional. No real delivery company provided these estimates. No real estimates were requested or received. No final technical commitment has been made.**

- **Business:** Harbor Fitness (fictional)
- **Estimate request version:** HF-ER-19-v1
- **Scope version:** HF-SCOPE-14-v1
- **Solution direction:** Validate native platform capability, then configure; integrate only if configuration is inadequate.
- **Delivery needs:** platform validation/configuration, bounded workflow analysis, testing, reproducible documentation, handoff; integration investigation only if needed.
- **Included:** request through recorded disposition, including manager approval for policy exceptions.
- **Excluded:** full portal, mobile app, historical migration, billing replacement.
- **Acceptance:** normal and exception behavior demonstrated with permission/test evidence.
- **Known unknowns:** native rule support and API write entitlement.

## Candidate estimates

### CANDIDATE: Northstar Configuration Specialist (fictional)

- **Estimate status:** CONDITIONAL / REVISED AFTER FICTIONAL CLARIFICATION
- **Scope alignment:** ALIGNED; baseline and estimate are HF-SCOPE-14-v1.
- **Components:** validation 4–6 hours; configuration 8–12; testing/documentation 4–6.
- **Estimated hours:** 16–24
- **Cost / range:** fictional raw partner cost $2,000–$3,000; validation identified as $500–$700.
- **Timeline / earliest start:** 1–2 weeks after access / 2026-09-14; expected 2026-09-28.
- **Assumptions:** native features exist (UNKNOWN, critical); customer supplies test access (UNCONFIRMED).
- **Exclusions / third-party costs:** historical migration and recurring licensing; setup not stated.
- **Customer effort / Local Works effort:** 5–8 / 6–9 hours.
- **Testing / documentation / deployment:** happy path, exception, permissions / configuration record and runbook / included after approval.
- **Confidence / risks:** MODERATE; capability unconfirmed and implementation must stop/reassess if absent.
- **Clarification:** “Is documentation included?” Fictional answer: configuration record and runbook are included; no adjustment.
- **Normalized expected cost:** $2,500–$3,700 including separately visible validation (conservative comparison; confirm whether raw total already includes it before commitment).
- **Partner-fit considerations:** strong platform/documentation fit; narrow integration depth and solo continuity risk.
- **Decision:** **SELECT_FOR_TECHNICAL_DISCOVERY**, not delivery.

### CANDIDATE: Bridge Integration Freelancer (fictional)

- **Estimate status:** REVISED / COMPARABLE AFTER FICTIONAL CLARIFICATION
- **Scope alignment:** ALIGNED, although the approach is more complex than configuration.
- **Components:** API discovery 6–10 hours; integration 24–36; testing 8–12; documentation 4–6.
- **Estimated hours:** 42–64
- **Cost / range:** fictional raw partner cost $5,500–$8,300.
- **Timeline / earliest start:** 3–5 weeks / 2026-09-09; expected 2026-10-14.
- **Assumptions:** write API and authentication exist (UNKNOWN, critical).
- **Exclusions / third-party costs:** vendor services and recurring API plan; fictional vendor setup $500–$900 after clarification.
- **Customer effort / Local Works effort:** 7–12 / 10–16 hours.
- **Testing / documentation / deployment:** included / source and runbook / included except vendor setup.
- **Confidence / risks:** LOW; no API access or documents reviewed, and integration may be unnecessary.
- **Clarification:** “Does this include vendor API setup?” Fictional answer: no; add $500–$900 if required.
- **Normalized expected cost:** $6,000–$9,200; recurring API fees remain separate.
- **Partner-fit considerations:** strong integration and communication; platform fit and reliability evidence uncertain.
- **Decision:** **KEEP_AS_BACKUP** if configuration is inadequate.

### CANDIDATE: Cedar Small Software Agency (fictional)

- **Estimate status:** NOT_COMPARABLE
- **Scope alignment:** **SCOPE DEVIATION**; estimated HF-PORTAL-v1, not HF-SCOPE-14-v1.
- **Components / hours / cost:** custom frontend and backend, 120–190 hours, fictional $18,000–$28,500.
- **Timeline / earliest start:** 8–12 weeks / 2026-10-19; expected 2027-01-11.
- **Assumptions:** a new portal is desired, contradicted by approved scope.
- **Exclusions / third-party costs:** platform licensing excluded.
- **Customer effort / Local Works effort:** 20–35 / 25–40 hours.
- **Testing / documentation / deployment:** portal testing, technical docs, and deployment included.
- **Confidence / risks:** MODERATE about a custom build; HIGH over-solution/operating-burden risk.
- **Clarification:** “Which proposed features are outside approved scope?” Fictional answer: accounts, dashboard, profile, and responsive self-service.
- **Normalized expected cost:** NOT COMPARABLE while scope differs.
- **Partner-fit considerations:** custom capability, but wrong-sized approach plus subcontracting/continuity uncertainty.
- **Decision:** **REQUEST_REVISED_ESTIMATE** against the baseline; not rejected merely for price.

### CANDIDATE: Local Works self delivery (fictional exercise)

- **Estimate status:** COMPARABLE as a burden scenario; not a provider assignment.
- **Scope alignment:** ALIGNED.
- **Components / hours:** learning/validation 10–18; configuration/evidence 18–30; technical effort 28–48.
- **Cost / range:** $0 partner cash, but owner work is not free.
- **Timeline / earliest start:** 6–10 weeks at six hours/week / 2026-09-07; expected 2026-11-16.
- **Assumptions / exclusions:** owner capacity is available (UNKNOWN); owner opportunity cost is excluded from cash cost.
- **Third-party costs:** UNKNOWN.
- **Customer effort / Local Works effort:** 6–10 / 34–57 hours including coordination.
- **Testing / documentation / deployment:** owner performs / owner performs / UNKNOWN pending validation.
- **Confidence / risks:** LOW; uncertain platform skill, calendar capacity, and displaced selling/customer work.
- **Clarification:** “What owner work would be displaced?” Fictional answer: sales, customer coordination, and method development.
- **Normalized expected cost:** $0 cash; high non-monetized owner burden remains explicit.
- **Partner-fit considerations:** strong context and control, but key-person/capacity concentration.
- **Decision:** **DO_NOT_SELECT** for this exercise.

## Comparison summary

| Candidate | Scope | Raw/normalized implementation cost | Effort / elapsed | Confidence | Decision |
|---|---|---:|---|---|---|
| Northstar | Aligned, conditional | $2,000–$3,000 / $2,500–$3,700 conservative | 16–24h / 1–2w | Moderate | Technical discovery |
| Bridge | Aligned, integration fallback | $5,500–$8,300 / $6,000–$9,200 | 42–64h / 3–5w | Low | Backup |
| Cedar | Scope deviation | $18,000–$28,500 / NOT COMPARABLE | 120–190h / 8–12w | Moderate | Revise |
| Local Works | Aligned | $0 cash / $0 cash plus 34–57 owner hours | 28–48h / 6–10w | Low | Do not select |

Customer effort, Local Works effort, recurring customer SaaS, risk, continuity, and partner fit remain separate rather than being hidden in a total.

### Failure checks

- A fictional $2,000 bid excluding $1,000 testing, $700 deployment, $600 documentation, and $500 setup normalizes to **$4,800**; a complete $4,000 bid is then cheaper. Raw bid price can be misleading.
- Equal $5,000 bids with HIGH/clear versus LOW/unknown confidence are not equivalent.
- A claim of 47.25 hours despite no API access, documentation, or migration knowledge is false precision.
- The agency's expensive portal is not safer merely because it costs more; it solves work outside the approved boundary.

## Final delivery decision

Select Northstar only for a fictional $500–$700 technical-validation phase whose outputs are confirmed native capability, technical notes, and a refined implementation estimate. Keep Bridge as the integration backup. Ask Cedar for a baseline-scope revision. Do not self-deliver merely to minimize cash.

**No provider is selected for implementation and implementation has not started.** The current evidence does not require `REVISIT_SCOPE` or `REVISIT_SOLUTION`; failed validation may trigger one later. Paying for uncertainty reduction can be cheaper than paying for bad certainty.
