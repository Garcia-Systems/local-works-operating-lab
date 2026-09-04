# Chapter 7 — From Audit to Opportunity

## 1. Friction is everywhere

A five-minute call, a confusing sentence, and an error-prone handoff can all be
real friction. Their existence says nothing yet about whether professional time is
justified. Chapter 6 asked, “What friction appears to exist?” Chapter 7 asks, “Is
this worth Local Works investigating further?”

## 2. Local Works cannot pursue everything

Treating every inconvenience as a lead manufactures demand, wastes the business's
attention, and biases Local Works toward projects. Responsible practice permits
seven outcomes: investigate, ask for information, make a simple improvement,
monitor, leave alone, refer, or disqualify.

## 3. The opportunity gate

**Audit Finding → Opportunity Assessment → Decision**

The finding supplies evidence and uncertainty. The assessment examines significance
and engagement conditions. The decision governs whether more time is warranted.
None of those transitions approves implementation.

The assessment exposes frequency, impact, affected parties, workaround burden,
business importance, urgency, authority, measurability, technical plausibility,
economic plausibility, and evidence strength. Economic plausibility means only
“potentially worth measuring”; quantified economics comes later.

## 4. Problem potential

Problem potential asks whether the possible workflow condition could matter. Does it
repeat? What happens? Who is affected? Does it touch revenue, acquisition, retention,
service, productivity, compliance, experience, or reliability? Is the workaround
burdensome? Could an outcome eventually be measured? A strong answer remains a
reason to investigate, not proof of value.

## 5. Commercial fit

Commercial or engagement fit asks whether Local Works is positioned to investigate
responsibly. Does the organization care now? Is an authorized sponsor accessible?
Is the work plausibly within scope and economically capable of supporting
professional help? A corporate location can have severe friction but no local path
to authority. An owner can be accessible while the problem is trivial. Never average
these distinct judgments into one flattering conclusion.

## 6. UNKNOWN is not BAD

Unknown request frequency is not low. Unknown budget is not no budget. Unknown
feasibility is not impossible. Label the gap and ask what would resolve it. When
frequency, impact, or authority is critical and missing, choose
`MORE_INFORMATION_NEEDED` rather than pretending the candidate is qualified or bad.

## 7. Why a magic score is dangerous

“73/100: qualified” substitutes arithmetic for judgment and hides decisive facts.
Show positive signals, negative signals, unknowns, hard disqualifiers, separate
problem and commercial judgments, the decision, and its rationale. A reader should
be able to disagree with the reasoning rather than reverse-engineer a score.

## 8. Symptoms versus workflow problems

“Customers call constantly” is a symptom; “routine membership changes require staff
intervention” is a candidate workflow condition. “We get lots of emails” might mean
customers cannot determine appointment status. “Employees hate this system” might
mean staff re-enter the same data three times. Complaints point toward questions;
they are not adequate opportunity definitions.

## 9. Grouping related findings

Several findings can be manifestations of one process. Freezes, cancellations,
manual account changes, and separate billing checks might belong to Membership
Account Management—or might be independent annoyances. Group only when actors,
handoffs, systems, or workflow purpose plausibly connect them, and record why. Never
automatically combine everything from one business.

## 10. Simple fixes

If public instructions demand a call while already-enabled SaaS self-service works,
correct the instructions or configuration and verify it. `SIMPLE_IMPROVEMENT` keeps
Local Works from turning obvious, bounded, low-risk corrections into consulting
engagements.

## 11. Problems worth leaving alone

Suppose a membership transfer really requires a five-minute call and occurs twice a
year. The friction is real and the established burden negligible. `LEAVE_ALONE` says
intervention is unjustified; it does not deny the observation.

## 12. When to refer

A valid need may chiefly require legal interpretation, accounting, managed IT,
cybersecurity incident response, or creative expertise. `REFER_ELSEWHERE` recognizes
the problem while putting it with a better-suited professional. Local Works should
not try to capture every dollar.

## 13. When to disqualify

`DISQUALIFY` concerns unacceptable engagement conditions: an unethical outcome,
unsafe expectation, demanded misrepresentation, insistence on a predetermined risky
solution, no viable authority path, or work clearly beyond capability. This differs
from `LEAVE_ALONE`: the latter concerns insignificant intervention value; the former
concerns whether pursuit is appropriate even if the problem is significant.

## 14. Harbor Fitness opportunity assessment

The fictional audit supports a provisional **Membership Account Management**
candidate. It groups routine freezes/cancellations requiring front-desk contact with
corroborated join-form re-entry because both may touch the operational membership
account workflow. It explicitly excludes membership comparison because no shared
process is established.

The decision is `DISCOVERY_WARRANTED`: corroborated manual re-entry and a potentially
related member/staff path justify bounded investigation. Volumes, effort, errors,
member impact, policy and billing constraints, shared workflow boundaries, authority,
urgency, system capability, economics, and baselines remain unknown. The detailed
assessment does not propose a portal or any other solution.

## 15. Executable exercise

Run:

```bash
python scripts/run_chapter_07.py
```

The exercise prints the gate, six distinct exit examples, explicit grouping and
exclusion, problem-versus-commercial comparisons, and a decision change caused by
critical unknowns. Its fictional outputs are teaching inputs, not market evidence.

## 16. What discovery must establish next

Discovery must test workflow boundaries and root conditions; establish volume,
handling time, consequences, exceptions, and affected parties; understand intentional
human value, policy, billing, and system constraints; confirm sponsor authority and
urgency; and find measurable baselines. It must not begin with a predetermined build.

## 17. Chapter artifacts

- `artifacts/opportunity-gate-methodology.md` defines the decision method.
- `artifacts/opportunity-assessment-template.md` supports repeatable assessments.
- `artifacts/harbor_fitness/07-opportunity-assessment.md` applies the gate cautiously.
- `local_works/opportunities.py` preserves explicit reasoning in executable objects.

## 18. Readiness checkpoint

Before continuing, explain:

- why friction does not automatically become an opportunity;
- problem potential versus commercial fit;
- why related findings may represent one workflow, without automatic grouping;
- why unknowns remain visible;
- leave alone versus disqualify, and when referral is appropriate;
- why an obvious simple fix may bypass discovery;
- why `DISCOVERY_WARRANTED` means only “worth investigating”; and
- why qualification does not select a technical solution.

