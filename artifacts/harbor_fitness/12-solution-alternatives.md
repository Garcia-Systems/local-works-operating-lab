# Harbor Fitness — solution alternatives

> **Fictional training scenario. Not a real customer recommendation.**

**Qualified problem:** Certain membership freezes require policy-dependent staff review and several manual administrative steps across systems. Frequency, total burden, errors, and customer impact remain unmeasured. Chapter 11's actual gate remains `MORE_EVIDENCE_REQUIRED`, so this is a provisional design comparison rather than a claim that qualification is complete.

**Current workflow summary:** A member contacts the front desk; staff gather details, inspect membership/billing context, apply eligibility policy, update the membership platform, record a spreadsheet note, verify the result, and confirm it. Exceptions go to a manager and wait for review.

**Current burden summary:** Chapter 10's estimated/hypothetical direct-labor range is $1,335–$4,312.50 annually ($2,450 baseline). Volume and time are not measured. Rework, customer burden, revenue, retention, and delay impacts remain unknown. Current burden is not future recoverable value.

**Relevant policies:** Eligibility depends on membership type; exceptions may legitimately require manager approval.  
**Relevant constraints:** Platform features, supported integrations, access/contract restrictions, priority, authority, budget/capacity, policy ownership, and change readiness remain unknown.

## Alternative 1 — Configure existing membership platform

- **Path:** `CONFIGURE`
- **Description:** Enable/configure supported member self-service or a better staff workflow, if it exists; a policy/process adjustment may be included.
- **Potential coverage:** `UNKNOWN / potentially high`
- **Complexity / cost / time:** `LOW` / `LOW` / `DAYS` (qualitative directions, not estimates)
- **Strengths:** No custom code, low switching cost, potentially fast value, potentially strong policy fit.
- **Critical assumption:** The platform supports conditional freeze workflows.
- **Status:** `NEEDS_VALIDATION`.

## Alternative 2 — Integrate a lightweight request interface

- **Path:** `INTEGRATE`
- **Description:** Move request information into the existing platform while preserving approval rules.
- **Potential coverage:** `UNKNOWN / potentially high`
- **Complexity / cost / time:** `MODERATE` / `MODERATE` / `WEEKS`
- **Dependencies:** Supported interfaces, permissions, identifiers, error handling, and vendor terms.
- **Critical assumption:** A suitable supported API/integration mechanism exists.
- **Status:** `NEEDS_VALIDATION`.

## Alternative 3 — Automate staff coordination

- **Path:** `AUTOMATE`
- **Description:** Route requests and approvals, send confirmations/reminders, or synchronize safe repetitive steps while retaining core systems.
- **Potential coverage:** Partial to potentially high; automation must not erase legitimate judgment.
- **Complexity / cost / time:** `MODERATE` / `MODERATE` / `WEEKS`
- **Critical assumption:** Stable triggers, states, and documented rules can safely drive automation.
- **Status:** `NEEDS_VALIDATION`.

## Alternative 4 — Custom account-management experience

- **Path:** `CUSTOM_BUILD`
- **Description:** Purpose-built customer/staff workflow coordinating membership changes and review.
- **Potential coverage:** Potentially high.
- **Complexity / cost / time:** `VERY_HIGH` / `VERY_HIGH` / `MONTHS`
- **Risks:** Highest delivery, security, integration, adoption, and long-term support responsibility.
- **Critical assumption:** Configuration, integration, and automation cannot adequately supply the capability.
- **Status:** `NOT_RECOMMENDED` now—not disqualified forever, but not currently justified.

## Alternative 5 — Leave alone

- **Path:** `LEAVE_ALONE`
- **Description:** Retain the current policy-dependent manual workflow.
- **Potential:** No project cost or added system risk.
- **Tradeoff:** Current burden and friction remain.
- **Status:** `VIABLE_ALTERNATIVE`, especially if measurement confirms limited recoverable value.

## Comparison

| Alternative | Coverage | Complexity | Relative cost | Time to value | Policy fit | Dependency / maintenance | Customer change |
|---|---|---|---|---|---|---|---|
| Configure | Unknown, potentially high | Low | Low | Days | Potentially strong | Existing vendor / low if supported | Unknown |
| Integrate | Unknown, potentially high | Moderate | Moderate | Weeks | Potentially strong | Vendor interface / moderate | Unknown |
| Automate | Partial–potentially high | Moderate | Moderate | Weeks | Must preserve review | Existing tools/interfaces / moderate | Staff coordination changes |
| Custom build | Potentially high | Very high | Very high | Months | Must be designed and proven | Highest ownership responsibility | Material and unknown |
| Leave alone | No improvement | Low | Very low | Immediate/no change | Strong | No added dependency | None |

These are qualitative comparison categories, not factual project estimates. Cheapest does not win: a low-cost option must adequately cover the validated problem.

## Critical capability questions

1. Does the membership platform support conditional self-service or staff-managed freezes? `UNKNOWN`—review vendor documentation and an admin demonstration.
2. Does it expose supported APIs/integration mechanisms for requests, eligibility context, approval, and status? `UNKNOWN`—review official documentation and, if available, a sandbox.
3. Does it emit reliable events or notifications for safe automation? `UNKNOWN`—inspect admin capabilities/documentation and conduct a bounded test.
4. What access, contract, pricing, security, and vendor restrictions apply? `UNKNOWN`—review customer/vendor materials; do not infer permission from technical possibility.

## Open assumptions

See `12-solution-assumptions.md`. Platform capability, interface access, complete policy rules, reliable automation triggers, authority, and adoption readiness remain open.

## Current preferred direction and decision

**Direction:** Validate `CONFIGURE` first and the supported `INTEGRATE`/`AUTOMATE` paths next where relevant. This preference does not assert any vendor capability or final recommendation.  
**Current decision:** `CAPABILITY_VALIDATION_REQUIRED`, nested within Chapter 11's still-open qualification gaps.

“We need a member portal” is requested solution language, not evidence. Custom build is not currently justified because platform capabilities are unknown, simpler paths have not been shown inadequate, economics are estimated and modest, and organizational ownership/support capacity is unresolved.

## What would change the decision

- Demonstrated native conditional workflow would make `CONFIGURE` strong.
- Absent native capability plus suitable supported interfaces/events would strengthen `INTEGRATE` and/or `AUTOMATE`.
- Evidence that critical capabilities and usable interfaces are absent, coupled with qualified burden, authority/capacity, policy fit, support ownership, plausible delivery, and value proportional to risk, would make `CUSTOM_BUILD` plausible.
- Evidence that recoverable value remains too small would strengthen `LEAVE_ALONE`.
- A hard legal, ethical, authority, security, or feasibility limitation could lead to `DECLINE` or disqualify an alternative.

**No project has been priced.**  
**No ROI has been calculated.**  
**No proposal has been issued.**  
**No implementation technology has been selected.**
