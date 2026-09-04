# Chapter 2 — The Ideal Customer Hypothesis

## 1. Why “any local business” is not a strategy

Local Works cannot economically investigate every inconvenient workflow. “Local business” describes geography, not a coherent customer profile. A useful Ideal Customer Profile (ICP) helps decide where scarce sales and discovery attention should go while leaving room to learn.

> **INITIAL HYPOTHESIS — NOT VALIDATED**
>
> Local Works has no real customer evidence. This chapter forms a testable starting belief, not a market declaration.

An ICP is a prioritization tool, not a machine that automatically accepts or rejects customers. It should focus inquiry, preserve reasons, and change when evidence disagrees.

## 2. Friction does not automatically create an opportunity

A workflow can be awkward yet harmless. Occasional texts may be mildly annoying, but if they consume almost no time, cause no customer loss, and create no economic consequence, professional intervention may cost more than the problem. Conversely, mundane re-entry repeated hundreds of times can accumulate into a meaningful burden.

We are not trying to find businesses that “need software.” We are trying to find businesses where meaningful friction may create an economically sensible opportunity for improvement. The eventual response could be configuration, integration, automation, a custom build, a process change, or leaving the workflow alone.

## 3. What might make a customer attractive?

The initial hypothesis is that promising customers may combine recurring customer or employee workflows; visible friction; meaningful manual work; enough volume for inefficiency to accumulate; reachable decision makers; some capacity to pay; manageable procurement; a technically feasible response; accessible sales channels; and measurable outcomes.

No single trait decides fit. Thirteen useful lenses are workflow frequency, affected people, severity, workaround burden, economic capacity, buying-authority accessibility, decision complexity, technology environment, urgency, measurability, responsible repeat opportunity, delivery feasibility, and sales accessibility. The Python exercise records each lens independently so its conclusion can be inspected.

## 4. Workflow frequency

Frequency changes the possible accumulated cost. Annual, monthly, weekly, daily, and many-times-daily work deserve different questions. High frequency is a useful signal, not proof: a near-effortless action repeated often can remain cheap, while an infrequent failure can be severe. Ask for observed counts rather than adjectives such as “always.”

The number of affected people also provides context—one employee, a whole staff, dozens or thousands of customers—but headcount must not masquerade as economics. One owner losing many paid hours may have a better opportunity than hundreds of users encountering a negligible annoyance.

## 5. Severity and workaround burden

Severity ranges conceptually from minor annoyance, through noticeable inconvenience and operational burden, to a meaningful customer problem or serious business constraint. Existing workarounds reveal the actual system: manual entry, phone calls, spreadsheets, repeated email, copying between systems, and paper re-entry can all be evidence.

But a workaround is not inherently bad. A harmless spreadsheet can be cheaper and safer than replacement. Establish time, error, delay, customer, risk, or opportunity effects before prescribing technology.

## 6. Economics and ability to pay

A worthwhile problem must support a proportionate response. Economic capacity is qualitative at this stage; Chapter 2 invents no revenue cutoff and has no pricing engine. Investigate whether the business plausibly can and will fund professional help and whether improvement could justify its total cost.

Large does not automatically mean good: a large company can impose expensive procurement and block access. Small does not automatically mean bad: a tiny organization can have severe repeated work, direct authority, and a simple measurable response. “Budget unknown” is a question, not “no budget.”

## 7. Authority and procurement

Local Works needs a plausible path to someone capable of approving work. An owner may decide directly; a manager may have a limit; regional, corporate, government, or committee structures may require introductions and formal cycles.

Decision complexity includes stakeholders, budget timing, procurement, security, legal review, and corporate approval. Strong problem fit cannot erase an inaccessible buyer. Equally, authority that has not yet been identified is not proof that authority is absent.

## 8. Technology environment

A prospect might be mostly manual, rely on one SaaS platform, use disconnected SaaS tools, run legacy or custom systems, or be controlled by corporate technology. Complexity can contain opportunity and substantial delivery risk at the same time. Existing software is not an automatic negative: configuration may solve the problem. Access restrictions, contracts, data, integration support, safety, and delivery-partner capacity require discovery.

## 9. Measurability

A credible engagement should identify what improvement would look like. Possible measures include handling time, re-entry, errors, completion, response delay, missed appointments, complaints, or customer outcomes. Choose a measure connected to the actual problem and establish a baseline before claiming change. A merely countable metric is not necessarily valuable.

## 10. Sales accessibility

Even a suitable operational problem may be an impractical market if Local Works cannot reach comparable organizations. Networking, referrals, targeted outreach, audits, and partnerships are possible channels to test—not assumed funnels. Track whether conversations reach appropriate decision makers and whether the cost and effort of access are sustainable.

Urgency matters here too. A prospect can agree that a problem exists but not care enough to act now. Maintain a relationship when appropriate without turning politeness into qualification.

## 11. Hard disqualifiers vs weak signals

A **hard disqualifier** justifies stopping: illegal or unethical expectations; no plausible business problem; refusal of necessary discovery paired with a demanded fixed solution; work that clearly cannot be delivered safely; or a contact who can neither authorize a purchase nor connect Local Works to someone who can.

A **weak or negative signal** changes priority or calls for evidence. Very small size, limited technology, uncertain budget, initial skepticism, existing software, and an apparently simple problem do not automatically disqualify anyone. Premature rejection can be as misleading as premature enthusiasm.

Most importantly, **UNKNOWN is different from BAD**:

- Budget unknown ≠ no budget.
- Authority unknown ≠ no authority.
- Workflow burden unknown ≠ low burden.

The model preserves unknowns in their own collection. It never silently converts missing evidence into a negative observation.

## 12. Why industry is only one variable

Industry can make outreach and workflow learning more focused, but it does not determine purchasing structure, burden, urgency, economics, or feasibility.

### Same industry, different fit exercise

| Fictional prospect | Workflow/problem | Authority | Current implication |
| --- | --- | --- | --- |
| Gym A | Recurring manual member problems | Owner controls decisions and is reachable | Audit may be warranted |
| Gym B | Similar recurring member problems | Corporate controls technology; local manager has no approval or introduction path | Strong problem fit, weak authority/sales fit |

Both are gyms. Their Local Works potential differs. **Industry ≠ ICP.** Fitness, restaurants, studios/classes, shops/services, recreation, membership organizations, trades, professional services, and community organizations are merely test markets—not proven verticals or claims of expertise.

## 13. Harbor Fitness assessment

Harbor Fitness is a fictional two-location gym and a running case, not evidence that gyms are the target market. Recurring memberships, recurring customer interactions, staff involvement, account-management workflows, existing membership software, and apparently reachable management make it interesting enough to investigate.

Actual volume, staff time, complaints, business impact, urgency, authority, budget, system capabilities, vendor restrictions, feasibility, and measurement remain unknown. Existing software is both context and a possible constraint. Current assessment: **PROMISING / REQUIRES VALIDATION**. A Digital Friction Audit is warranted; a purchase, project, custom build, and vertical conclusion are not.

## 14. Comparing fictional prospects

The exercise compares six explicitly fictional organizations:

- **Harbor Fitness:** promising enough for an audit, with substantial unknowns.
- **Cadence Music Lessons:** 18 students and occasional low-cost scheduling texts; friction exists, but the known problem is currently too small.
- **Rapid Home Care:** frequent calls, scheduling, dispatch, estimates, communications, staff, and multiple tools create plausible signals plus delivery and authority uncertainty.
- **MetroMotion Gym—Downtown:** strong local workflow signals cannot overcome a known absence of local authority or a headquarters path.
- **Pocket Stage Studio:** tiny size does not erase exceptionally heavy administration, measurable lost teaching time, and direct authority; economics remain unknown.
- **Shadow Metrics Cooperative:** the demanded unlawful data collection is a hard disqualifier regardless of commercial interest.

The comparisons resist two shortcuts: “friction means sale” and “large means attractive.”

## 15. Executable exercise

Run:

```bash
python scripts/run_chapter_02.py
```

For every prospect, the script prints business and type, positive signals, negative signals, unknowns, hard disqualifiers, current assessment, rationale, and next action. There is no numerical score or machine learning. The few decision rules are readable: disqualifiers stop pursuit; known authority failure remains decisive; known trivial severity and burden remain weak; recurring friction plus plausible authority may warrant validation; everything else stays uncertain.

## 16. Revising the ICP with evidence

Real audits and discovery should test workflow volume, impact, authority access, buying behavior, procurement effort, sales-channel response, feasibility, delivery effort, measurable improvement, and responsible repeat work. Record counterexamples, referrals, declines, and “leave alone” decisions—not only sales. Look for repeated patterns before narrowing a vertical or creating thresholds.

A revision should state what evidence changed, how often it appeared, and which belief it challenges. Fictional cases can test logic; they cannot validate demand.

## 17. Chapter artifacts

- `artifacts/ideal-customer-hypothesis.md` holds the working ICP, test markets, disqualifiers, unknowns, and revision evidence.
- `artifacts/harbor_fitness/02-customer-fit-hypothesis.md` keeps the cautious case assessment.
- `artifacts/production-system-discovery.md` records only system needs observed in this exercise.
- `local_works/customers.py` contains the readable model and fictional profiles.

## 18. Readiness checkpoint

Before moving beyond this chapter, Local Works should be able to:

- explain the initial ICP as an unvalidated hypothesis;
- distinguish meaningful friction from any inconvenience;
- discuss all thirteen fit characteristics without using company size as a shortcut;
- preserve positive, negative, unknown, and disqualifying evidence separately;
- explain why Harbor Fitness warrants an audit but not a project conclusion;
- compare same-industry prospects with different authority and operating conditions;
- name the real evidence that would revise the ICP.

Chapter 2 stops at customer-fit hypothesis and audit prioritization. Qualification processes, funnels, advertising, proposals, pricing, production software, and partner engines remain deferred.
