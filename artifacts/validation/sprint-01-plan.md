# VALIDATION SPRINT 1 — Find and Test a Real Business Friction Hypothesis

## Objective

Replace part of the fictional funnel model with bounded real evidence: manually identify suitable businesses, inspect only public customer journeys, determine whether genuine observable friction deserves discovery, prepare and (manually) attempt appropriate outreach, and record progression without building software.

> **Governing principle: THE NEXT STEP SHOULD PRODUCE EVIDENCE, NOT MORE SOFTWARE.** This is post-lab validation, not Chapter 33.

## Primary evidence gap

- **Evidence gap:** Will qualified strangers progress and buy?
- **Current assumption:** The simulation assumes a 48% qualified-lead rate and 42% close rate; neither is a real operating observation.
- **Evidence status:** SIMULATION_ONLY / qualified demand unvalidated.
- **Sensitivity:** `close_rate` is the most sensitive modeled assumption (a $66,103 range in simulated Year 3 owner draw); `qualified_lead_rate` is fourth ($14,224 range).
- **Risk if wrong:** Demand, cash, capacity, and owner income may be materially worse; the final verdict is **FRAGILE**, and the software gate is **MORE_BUSINESS_VALIDATION_FIRST**.
- **Why this should be tested now:** Chapter 32 explicitly marks it **CRITICAL_NEXT** and prescribes bounded public audits with funnel progression. It precedes price, delivery, and production-software validation because those tests require a qualified conversation first.

## Validation type and target profile

**PUBLIC DIGITAL FRICTION AUDIT VALIDATION.** Prefer independent/local businesses or small groups with a visible and meaningful customer workflow, observable friction, a reachable decision maker, potentially material value, solution flexibility, first-project safety, and learning value. Compare candidate categories rather than presuming they are equal. Never access private systems, impersonate customers, submit transactions/forms, or create disruption.

## Sprint scope (configurable)

- 5 target businesses researched
- 3 detailed public audits
- Up to 3 personalized outreach attempts

This small batch seeks learning, not statistical certainty. Change these limits before beginning only with a written reason and time bound.

## Steps

1. Identify targets manually and record provenance.
2. Score all seven dimensions, preserving UNKNOWN.
3. Select audit candidates based on visible evidence, safety, and learning value.
4. Perform public audits across FIND → UNDERSTAND → CONTACT → BOOK/JOIN → PAY → RECEIVE SERVICE → MANAGE → RETURN; do not force findings.
5. Separate every direct observation from inference and unknown.
6. Produce discovery questions only for facts unavailable publicly.
7. Choose WORTH_DISCOVERY, MAYBE_DISCOVERY, LOW_PRIORITY, NO_OBVIOUS_OPPORTUNITY, or INSUFFICIENT_EVIDENCE.
8. Prepare personalized, specific, non-salesy outreach only where warranted; a human decides whether to send it.
9. Record response and any voluntarily supplied rejection reason without arguing.
10. Update the evidence ledger only with actual evidence, sample size, and provenance.
11. Compare eligible counts, outcomes, and actual minutes with the simulation assumptions.
12. Decide the next evidence-producing experiment.

## Response and rejection records

Record the response stage without collapsing the funnel: **NOT_CONTACTED, OUTREACH_PREPARED, CONTACTED, NO_RESPONSE, RESPONDED, NOT_INTERESTED, INTERESTED, DISCOVERY_SCHEDULED, DISCOVERY_COMPLETED, NOT_A_FIT, OPPORTUNITY,** or **UNKNOWN**. If a business voluntarily explains a rejection, record **NO_NEED, NO_BUDGET, BAD_TIMING, HAPPY_WITH_CURRENT_SYSTEM, CORPORATE_CONTROL, ALREADY_SOLVED, NOT_PRIORITY, DO_NOT_CONTACT,** or **UNKNOWN**. Respect the answer and do not argue.

No response is evidence only about that particular outreach attempt. It does not establish that the business lacks a problem, that Local Works lacks a market, or that the value proposition is invalid.

## Success signals

- Genuine observable friction can consistently be identified.
- Findings generate useful discovery questions.
- At least some businesses respond.
- Discoveries reveal economically meaningful problems.
- Assumptions become better informed.

Closing a sale is not required for sprint success.

## Failure signals (also valuable evidence)

- Targets show little observable friction, or audits take too long.
- Outreach gets no engagement or decision makers cannot be reached.
- Existing tools have solved the issue.
- Problems are economically small or willingness to discuss is low.

## Time budget and tracking

Predeclare the calendar window and maximum total owner time before research begins. For every target record actual **target research, audit, outreach preparation, follow-up, and discovery minutes**; blank/zero means not done, never estimated completion. These observations will eventually test owner presales-hours assumptions.

## Stop conditions

- Stop immediately for a request not to contact, a privacy/access boundary, or any need to impersonate, submit, scrape, or disrupt.
- Stop auditing a target when public evidence is insufficient; record that verdict.
- Do not exceed 5 researched, 3 audits, 3 attempts, or the predeclared time budget without reviewing the experiment.
- Do not propose a solution, alter a simulation assumption, or authorize production software from fictional or unsupported evidence.

## Outreach templates (prepare; never automate)

### Email
**Subject: A customer-workflow observation**

Hi [name], I was looking at [business]'s public customer experience and noticed [specific observation]. It may be creating unnecessary work, although I cannot know that from the outside. I put together a short observation and would be happy to share it. Would that be useful?

### LinkedIn
Hi [name] — I noticed one public [business] customer workflow that may be creating unnecessary work. I wrote up the observation and questions it raised. Happy to share it if useful.

### In-person / networking follow-up
Good meeting you, [name]. I took another look at the public [business] customer journey and noticed [specific observation]. I cannot see the internal impact, but I would be happy to share the short note and hear whether it matters.

Do not claim customers, results, savings, benchmarks, partners, or authority that do not exist.
