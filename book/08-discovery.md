# Chapter 8 — Discovery

## 1. Discovery is not a sales pitch

Chapter 7 allowed a promising hypothesis through a gate; it did not approve work. Discovery learns whether a problem is real, matters, is understood, has interest and authority behind it, faces meaningful constraints, and merits more analysis. It is not a performance designed to make a customer agree. A rigorous discovery can succeed by concluding **no project**.

Discovery must not design a technical solution or calculate value. Its progression is:

> Audit observation → Opportunity hypothesis → Discovery questions → Customer evidence → Revised understanding

## 2. Begin with a hypothesis

“Routine membership-account changes appear to require staff intervention, potentially creating member inconvenience and repetitive administrative work” is a useful starting hypothesis. It identifies a workflow and possible consequences while admitting uncertainty. “Customers have to call, therefore build a member portal” skips the learning process, turns an observation into an unsupported conclusion, and chooses a solution prematurely.

Keep observation, inference, hypothesis, simulated evidence, and measured evidence visibly distinct. Discovery progressively replaces assumptions; it does not disguise them.

## 3. Ask about work, not features

Begin with “Walk me through what happens.” Learn who initiates the work, who touches it, which manual workarounds compensate, how it ends, and what changes when it goes wrong. Feature requests are prompts to investigate work:

- “We need an app.” → “What would someone need to accomplish?”
- “Members need to freeze accounts, update payment methods, and see billing status.” → investigate those workflows, without accepting an app as necessary.
- “We need AI.” → “What work are you hoping AI would improve?”

A requested feature remains a stated preference until evidence establishes the underlying problem. Even then, the feature is not automatically the solution.

## 4. The discovery question categories

A useful interview covers:

- **Current state:** What actually happens, including workarounds?
- **Frequency/volume:** How often, and how many cases?
- **People:** Who performs, experiences, manages, and decides?
- **Time/burden:** What employee, customer, and manager time is involved?
- **Errors/exceptions:** What fails, and what happens off the happy path?
- **Customer impact:** What delay, confusion, inconvenience, dissatisfaction, or abandonment occurs?
- **Business impact:** What effect on revenue, retention, acquisition, service, workload, errors, cost, compliance, reliability, or visibility is known?
- **Systems:** What participates, and what is known versus unknown?
- **Policy:** Which steps are intentional business choices?
- **Constraints:** What cannot easily change?
- **Urgency:** Why now, and is the deadline real?
- **Authority:** Who may approve further work?
- **Budget:** Is funding plausibly available—not approved?
- **Success criteria:** In business/workflow terms, what would “better” mean?

The goal is coverage, not a robotic questionnaire. Follow useful answers while retaining gaps.

## 5. Open questions vs leading questions

“Wouldn't it be easier if members could cancel online?” advertises an answer. “Walk me through what happens when a member wants to cancel” invites a description. “How much time does your broken system waste?” embeds both blame and waste; ask “How often does this happen, and what does a staff member do?”

The five-whys technique can help, but repetition is not understanding. “They call because the website does not support it” might be wrong: a platform may support self-service while management intentionally disables it. Test whether the cause is a technical limitation, business policy, process habit, configuration, integration gap, or knowledge/training issue. Do not choose a solution while categorizing the cause.

## 6. Estimates are not measurements

“We get calls constantly” establishes the manager's perception. “Probably 20 per week” is a sourced estimate. A call log showing 18, 22, 19, and 21 in four stated weeks is measured data. All can be evidence, but they are not interchangeable.

Record an evidence value's value, unit, source, provenance, and notes. An employee's “eight minutes/request” must never silently become measured labor time. `UNKNOWN` is not bad, zero, rare, or impossible. This discipline matters when a later chapter—not this one—examines economics.

## 7. Talk to the people doing the work

Owners understand objectives and authority. Employees often understand interruptions and exceptions. Managers may understand policies; customers may understand effort and confusion. No single role automatically owns truth.

If a manager says a call takes five minutes while an employee says simple calls take five but disputes take twenty, retain both. The second statement adds variation rather than merely defeating the first. Missing perspectives should be named.

## 8. Contradictory evidence is useful

If management says a request is rare and the front desk says it occurs daily, do not average testimony into a fictional fact. Preserve each participant and source, identify a conflict, state the unresolved question, and request evidence capable of resolving it. Contradiction points to definitions, seasons, exceptions, or visibility that discovery needs to understand.

## 9. Systems, policies, and constraints

Discovery inventories systems; it does not produce architecture. For each system, record its name/generic role, purpose, users, workflow part, known limitations, known integrations, unknown capabilities, owner/vendor, and access constraints. If a vendor capability was not checked, write `UNKNOWN` rather than inventing it.

The Harbor Fitness audit suggested members contact staff to freeze memberships. Fictional management explains that eligibility depends on membership type and approval is intentional. That materially revises interpretation. The question may be how eligible requests can require less administration while preserving policy—but even that is an analytical question, not a selected solution.

## 10. Exceptions reveal complexity

The normal path is often deceptively easy. Ask, “What happens when it doesn't go normally?” An overdue balance, medical freeze, or missing note may change roles and time. These are fictional Harbor examples, not universal facts. Discovery records only exceptions participants identify and leaves their frequency unknown. Designing only for the happy path would erase the real work.

## 11. When “we need an app” is not the problem

An app is a container. AI is a technology. Neither describes work, impact, policy, or success. Translate a request into accomplishments and current workflows, then investigate. Discovery can validate meaningful work while weakening the proposed feature—or weaken the opportunity altogether.

## 12. Harbor Fitness discovery session

The executable fictional scenario interviews an owner/general manager and a front-desk employee. Management estimates eight freezes/week and five minutes normally. The employee estimates three or four/week, says simple work may take five minutes, and describes an overdue-balance exception taking 15–20. Neither has measured it.

The emerging outline is contact, lookup, eligibility/notes check, exception approval, platform update, supplemental note, and confirmation. This is orientation, **not Chapter 9's formal workflow reconstruction**. The identified systems are a generic Membership Management Platform, Staff Email, and a Spreadsheet; important capabilities remain unknown.

## 13. Evidence requests

A gap should become a bounded request, not an invented answer:

- monthly change logs for representative volume and seasonality;
- observation/a sample of 20 requests for handling time and variation;
- categorized inbox review for complaints;
- correction/billing-exception records for error and rework rate.

Requesting evidence does not mean Local Works accessed it. It creates a measurement plan and explains what decision the evidence could inform.

## 14. Revising the problem statement

Before: “Members cannot self-manage account changes.”

After: “Certain membership freezes require policy-dependent staff review, and staff appear to perform several manual administrative steps across systems. Frequency, total handling burden, errors, and customer impact remain unmeasured.”

The revised statement is narrower, more useful, and less certain where evidence is missing. It preserves the policy rather than assuming staff must be removed.

## 15. Valid discovery outcomes

- `CONTINUE_ANALYSIS`: evidence supports the next analytical step.
- `MORE_EVIDENCE_REQUIRED`: named missing evidence blocks interpretation.
- `OPPORTUNITY_WEAKENED`: discovery reduced apparent importance.
- `STOP`: no further work is warranted.

There is no `CUSTOM_BUILD`, `PROJECT_APPROVED`, or `PROPOSAL_READY` discovery outcome. Harbor Fitness ends at `MORE_EVIDENCE_REQUIRED`, not a recommendation. A later answer can still be stop.

## 16. Executable exercise

Run:

```bash
python scripts/run_chapter_08.py
```

Read its provenance labels, compare participants, inspect the contradiction and unknowns, and verify that its final output contains neither a solution nor approval.

## 17. Chapter artifacts

- `artifacts/discovery-methodology.md` — operating method and exits.
- `artifacts/discovery-template.md` — practical reusable interview record.
- `artifacts/harbor_fitness/08-discovery-notes.md` — explicitly fictional session notes.
- `artifacts/production-system-discovery.md` — only production needs exposed by this exercise.

## 18. Readiness checkpoint

The reader should be able to explain:

- why discovery is learning rather than a sales presentation;
- why a requested feature is not necessarily the problem;
- why estimates and measurements remain separate;
- why multiple roles and preserved contradictions improve understanding;
- why business policy can explain apparent technical friction;
- why exceptions expose complexity;
- why missing facts produce evidence requests; and
- why a successful discovery can still end with no project.

If any answer depends on picking a technology, calculating ROI, or drawing the formal workflow, stop. Those activities are intentionally deferred. Chapter 8 ends with evidence discipline and a decision about learning—not Chapter 9.
