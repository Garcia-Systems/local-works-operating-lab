# Local Works Operating Lab

An executable business laboratory for testing how Local Works might operate before a production application is built.

Local Works is a customer-facing technology-services initiative by Garcia Systems. Its promise is simple: **Make your business easier to use.** The lab tests whether that promise can become a repeatable, economically sound operating practice. It does not claim that the business model works.

> The website concept shows what Local Works might look like.
>
> The operating lab determines what Local Works actually needs to do.

## Why the lab comes first

A website can describe an imagined service, but it cannot establish whether customers have costly friction, will buy help, or can be served profitably. This repository makes assumptions visible and turns the operating lifecycle into small exercises. Observations from those exercises belong in `artifacts/production-system-discovery.md`; only repeated, supported needs should influence a later production system.

This is an executable business textbook—not the production Local Works website, a prototype SaaS product, or evidence that Local Works has customers or results.

## The three-party model

1. **Customer** — the business experiencing customer or employee workflow friction.
2. **Local Works / Garcia Systems** — Local Works is the customer-facing initiative; Garcia Systems is the business behind it. Local Works leads marketing, qualification, Digital Friction Audits, discovery, economics, solution design, sales, project leadership, QA, the customer relationship, and support coordination.
3. **Delivery partner** — a generic implementation resource, such as an independent specialist, agency, vendor, customer team, or larger services firm. No real delivery company is assumed.

Local Works can own the outcome and relationship without personally performing every implementation task.

## The five tests

- **Demand:** do businesses experience important digital workflow friction?
- **Value:** can an audit reveal a problem worth addressing?
- **Sale:** will customers pay enough for a sensible engagement?
- **Delivery:** can partners implement reliably while Local Works leads the relationship?
- **Sustainability:** can the work, including appropriate recurring support, produce sustainable owner income?

All five begin as unproven hypotheses.

## Solution hierarchy

Every problem should be considered in this order:

**Configure → Integrate → Automate → Custom Build → Leave Alone**

This is a decision set, not a promise to progress from left to right. “Leave alone” can be the best economic answer, and custom software is never the default.

## Implemented chapters

- **Chapter 0 — The Local Works Experiment:** establishes the unproven business hypotheses and evidence language.
- **Chapter 1 — What Are We Actually Selling?:** separates customer requests, validated problems, service stages, technical solutions, delivery, and ongoing support.
- **Chapter 2 — The Ideal Customer Hypothesis:** uses explicit positive, negative, unknown, and disqualifying signals to prioritize fictional prospects without claiming a validated market.
- **Chapter 3 — The First Market Experiment:** compares qualitative acquisition hypotheses and designs a bounded, ethical, observation-led learning experiment without running it or selecting a winning channel.
- **Chapter 4 — The Acquisition Funnel:** models hypothetical, channel-specific progression, expected versus simulated outcomes, bottlenecks, sensitivity, quality, and owner effort without claiming sales evidence.
- **Chapter 5 — Customer Acquisition Economics:** connects attributable cash, owner effort, and Chapter 4 funnel outcomes; safely handles zero-customer periods and compares hypothetical channel economics without selecting a winner.
- **Chapter 6 — The Digital Friction Audit:** maps adaptable customer and employee workflows, separates observed facts from friction hypotheses, preserves unknowns, and recommends whether further investigation is warranted without selecting a solution.
- **Chapter 7 — From Audit to Opportunity:** applies a transparent opportunity gate, separates problem potential from commercial fit, groups only plausibly related findings, and permits discovery, simple, referral, leave-alone, and disqualification exits without approving a project.
- **Chapter 8 — Discovery:** uses open workflow questions, sourced evidence, multiple perspectives, conflicts, systems, policies, exceptions, and evidence requests to revise a problem hypothesis without choosing a solution or approving a project.
- **Chapter 9 — Reconstruct the Current Workflow:** turns discovery evidence into an ordered current-state workflow with actors, mechanisms, data movement, decisions, handoffs, exceptions, separate active/wait time, and explicit unknowns—without designing a solution.
- **Chapter 10 — The Economics Behind the Pain:** converts supported current workflow activity into evidence-preserving direct-burden estimates, separates hard, soft, and unknown impacts, and tests low/base/high sensitivity without claiming recoverable value or ROI.
- **Chapter 11 — Qualify the Opportunity:** completes Part III by applying independent, evidence-backed commercial gates, explicit hard disqualifiers, and owner-time discipline to advance, investigate, nurture, refer, decline, or disqualify without selecting a solution.

## Run the chapters

Python 3.11 or newer is required.

```bash
python scripts/run_chapter_00.py
python scripts/run_chapter_01.py
python scripts/run_chapter_02.py
python scripts/run_chapter_03.py
python scripts/run_chapter_04.py
python scripts/run_chapter_05.py
python scripts/run_chapter_06.py
python scripts/run_chapter_07.py
python scripts/run_chapter_08.py
python scripts/run_chapter_09.py
python scripts/run_chapter_10.py
python scripts/run_chapter_11.py
python -m pytest
```

The exercises expose their reasoning: Chapters 0 and 1 distinguish hypotheses and service stages, while Chapter 2 compares fictional prospects and preserves unknowns rather than treating them as negative facts. Chapter 3 separates public observations from inferred problems, accounts for cash and owner time, and treats every channel as unvalidated. Chapter 4 distinguishes activity from commercial progress and labels all funnel arithmetic and simulations as hypothetical rather than evidence. Chapter 5 separates cash CAC from owner time and fully loaded CAC, retains prior-period failures, and leaves zero-denominator metrics undefined. Chapter 6 records customer and operational friction without turning incomplete evidence into low significance or an implementation recommendation. Chapter 7 decides whether that friction warrants more attention while exposing signals, uncertainty, fit, and non-project exits. Chapter 8 investigates the surviving hypothesis while preserving participant attribution, provenance, contradictions, policy, and unknowns. Chapter 9 reconstructs that evidence as current work, preserves exceptions and incomplete timing, and produces observations rather than solution requirements. Chapter 10 annualizes supported burden, preserves provenance and unknowns, and shows why current burden is neither recoverable value nor ROI. Chapter 11 completes **Part III — Sell the Right Problem** by asking whether the evidence, customer intent, feasibility, fit, risk, and remaining owner effort justify continuing; stopping is an acceptable result.

## Repository map

- `book/` — instructional chapters
- `local_works/` — deliberately small executable business models
- `scripts/` — chapter exercises
- `artifacts/` — operating documents produced and refined by the lab
- `scenarios/` — future, explicitly fictional operating scenarios
- `tests/` — checks that protect the meaning of the models

## Repository philosophy

- Every executable element must answer a business operating question.
- Prefer readable Python and the standard library over generalized architecture.
- Label uncertain assumptions as hypotheses and fictional businesses as fictional.
- Separate what is believed, observed, and measured.
- Let operating evidence—not a concept mockup—create production requirements.

## Intentionally absent

There is no web application, API, authentication, CRM, dashboard, portal, database, ORM, customer CRUD, pricing engine, proposal engine, or speculative production feature list. Harbor Fitness is a fictional running case; its artifacts and audit do not select or design a solution.
