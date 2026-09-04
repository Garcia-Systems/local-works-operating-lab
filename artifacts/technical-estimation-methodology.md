# Technical estimation methodology

## Keep commercial and delivery numbers separate

A **technical estimate** forecasts a delivery team's effort, cost, timeline, assumptions, and requirements. A **customer quote/customer price** is what Local Works charges. A **proposal price** is the commercial number shown to the customer. Chapter 15 owns customer pricing; Chapter 19 must not overwrite it.

## Request a common baseline

Send every Chapter 18 `QUALIFIED_FOR_ESTIMATE` candidate the same complete request linked to one scope version: problem and outcome, solution direction, workflow boundaries, capabilities, systems, constraints, acceptance, responsibilities, testing, documentation, deployment, continuity, assumptions, and unknowns. Record both baseline and estimated scope versions. An alternative is welcome only when labeled; it is not directly comparable until reconciled.

## Read the estimate, not merely the number

Use only the components a project needs—validation, configuration, frontend, backend, integration, automation, migration, testing, deployment, documentation, training/support, coordination, or other. Accept hourly effort and fixed delivery cost without assuming either is inherently more accurate. Prefer honest ranges over false precision.

Confidence—HIGH, MODERATE, LOW, VERY LOW, or UNKNOWN—should reflect scope clarity, access, documentation, rules, data, dependencies, and experience. Low confidence can be responsible. Preserve each assumption's importance, evidence/status, and impact if false. Preserve exclusions explicitly.

Separate partner cost from third-party implementation cost and recurring SaaS/licensing. Separately show customer effort and Local Works coordination effort. Those hours contribute to total project delivery burden without requiring an invented dollar value.

Effort hours are not elapsed time. Record duration, dependencies, earliest start, and expected completion independently. A short job with late availability can finish after a longer job that starts now. Record estimate validity because availability, rates, vendors, scope, and systems change.

## Conditional estimates and discovery

An estimate may depend on a capability. When evidence is unavailable, a small paid technical discovery can confirm API capability/authentication, document the path, and refine the estimate. Selecting discovery is not selecting implementation. Paying to reduce uncertainty can cost less than buying false certainty.

## Clarify, normalize, then compare

Record the question, why it matters, fictional response, impact, and status. Normalize scope, testing, documentation, deployment, third-party setup, support/handoff, customer effort, Local Works effort, assumptions, timeline, and risk. The normalized expected delivery cost can include partner cost, required discovery, attributable setup, and required specialist work. Keep recurring customer SaaS separate. If scope cannot be reconciled, mark **NOT COMPARABLE**.

Total project delivery burden considers partner cost, Local Works owner effort, customer internal effort, third-party implementation cost, and delivery risk. It is a decision perspective, not accounting profit, and not everything must be monetized.

## Judge estimate quality without a magic score

Review scope alignment, assumption/exclusion clarity, technical reasoning, risk disclosure, cost transparency, timeline realism, testing, documentation, handoff, and confidence calibration as STRONG, ADEQUATE, UNCERTAIN, or WEAK. Detail is useful but neither detail nor high price proves quality.

- **Low-bid bias:** omitted testing, deployment, documentation, or setup can make the lowest raw price costliest after normalization. Sometimes a complete low estimate really is best.
- **High-bid bias:** an expensive custom application can be unnecessary when configuration suffices.
- **Over-solution:** label added functionality `SCOPE DEVIATION` and request a bounded revision.
- **Under-solution:** label omitted required behavior `INCOMPLETE_SCOPE`; do not compare it as complete.
- **Risk ranges:** show plausible scenarios; do not apply a universal contingency percentage.
- **False precision:** 47.25 hours is not credible merely because it has decimals when API access, documents, or data complexity are unknown.

## Decide deliberately

Combine delivery fit carried from Chapter 18 with estimate quality, expected cost, timeline, risk, continuity, communication, availability, documentation, and handoff. Outcomes include delivery, technical discovery, revised estimate, clarification, backup, no selection, reopening search, or revisiting solution/scope. The lowest and highest prices are never automatic winners. Poor estimates may reveal an unstable solution or scope rather than poor candidates.

Future delivery chapters may compare estimated and actual cost, hours, and duration. Chapter 19 creates no actuals, kickoff, agreement, implementation, or customer commitment.
