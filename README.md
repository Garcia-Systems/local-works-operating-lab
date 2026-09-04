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
- **Chapter 12 — Choose the Simplest Sensible Solution:** begins **Part IV — Design the Right Solution** by comparing configure, integrate, automate, custom-build, and leave-alone alternatives for adequacy, simplicity, relative cost, and risk while preserving capability unknowns.
- **Chapter 13 — Solution Economics:** connects current burden to evidence-backed recoverable value, adoption, realization, new operating work, one-time and recurring cost, payback, multi-year sensitivity, and incremental alternative economics without creating a proposal or approving a project.
- **Chapter 14 — Scope the Engagement:** turns a promising direction into an outcome-led workflow boundary with explicit inclusions, exclusions, responsibilities, dependencies, acceptance, change triggers, risks, and an estimate-readiness gate—without pricing or proposing the work.
- **Chapter 15 — Price the Engagement:** compares customer value and payback with direct cost, owner time, contribution, pricing windows, discounts, and cash exposure; it can phase, restructure, or find no healthy price without issuing a proposal.
- **Chapter 16 — Proposal and Negotiation:** completes **Part IV — Design the Right Solution** by assembling an evidence-linked decision document, preserving scope and proposal versions, and negotiating price, phases, payment, risk, and healthy exits without creating a contract or project.
- **Chapter 17 — Close Without Disaster:** begins **Part V — Assemble the Delivery System** by separating proposal acceptance, authority, agreement, payment, preconditions, cash coverage, and explicit authorization before any delivery commitment.
- **Chapter 18 — Find the Delivery Path:** derives delivery needs before comparing paths and fictional candidates, then gates estimate requests on fit, evidence, total risk, and transition-ready operational control without choosing a provider.
- **Chapter 19 — Request and Compare Technical Estimates:** sends qualified paths one scope-versioned fictional baseline, exposes ranges, assumptions, exclusions, confidence and total burden, then normalizes comparison and may choose paid validation rather than a low bid or implementation.
- **Chapter 20 — Delivery Risk and Ownership:** completes **Part V — Assemble the Delivery System** by separating legal ownership, operational control, and responsibility; testing assets, access, knowledge, dependencies, authority, and two-way continuity before kickoff.
- **Chapter 21 — Project Kickoff and Requirements:** begins **Part VI — Deliver the First Project** by transferring authorized context into role-aware kickoff, a provenance-rich requirements baseline, open questions, decision rules, and an implementation-readiness gate without restarting discovery or implementation.
- **Chapter 22 — Business-to-Technical Translation:** preserves customer wording and intent while linking requirements, rules, workflow, data, questions, bounded technical work, tests, and acceptance; it detects translation gaps and unjustified expansion without prescribing architecture.
- **Chapter 23 — Milestones and Project Control:** adds proportional milestones, owned and dependent tasks, blockers, decisions, baseline-safe forecasts, variance, health rationales, early customer communication, and corrective action without executing delivery or scope changes.
- **Chapter 24 — Scope Creep and Change Requests:** classifies changes against immutable baselines, analyzes incremental impact and economics, and records fair absorb, correct, trade, phase, reject, approval, baseline, and reforecast decisions without executing changed work.
- **Chapter 25 — QA and Customer Acceptance:** traces proportional tests to approved requirements and acceptance criteria, separates defects from changes, records fix/retest and known issues, and reaches evidence-based customer acceptance without treating acceptance as long-term business success.

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
python scripts/run_chapter_12.py
python scripts/run_chapter_13.py
python scripts/run_chapter_14.py
python scripts/run_chapter_15.py
python scripts/run_chapter_16.py
python scripts/run_chapter_17.py
python scripts/run_chapter_18.py
python scripts/run_chapter_19.py
python scripts/run_chapter_20.py
python scripts/run_chapter_21.py
python scripts/run_chapter_22.py
python scripts/run_chapter_23.py
python scripts/run_chapter_24.py
python scripts/run_chapter_25.py
python -m pytest
```

The exercises expose their reasoning: Chapters 0 and 1 distinguish hypotheses and service stages, while Chapter 2 compares fictional prospects and preserves unknowns rather than treating them as negative facts. Chapter 3 separates public observations from inferred problems, accounts for cash and owner time, and treats every channel as unvalidated. Chapter 4 distinguishes activity from commercial progress and labels all funnel arithmetic and simulations as hypothetical rather than evidence. Chapter 5 separates cash CAC from owner time and fully loaded CAC, retains prior-period failures, and leaves zero-denominator metrics undefined. Chapter 6 records customer and operational friction without turning incomplete evidence into low significance or an implementation recommendation. Chapter 7 decides whether that friction warrants more attention while exposing signals, uncertainty, fit, and non-project exits. Chapter 8 investigates the surviving hypothesis while preserving participant attribution, provenance, contradictions, policy, and unknowns. Chapter 9 reconstructs that evidence as current work, preserves exceptions and incomplete timing, and produces observations rather than solution requirements. Chapter 10 annualizes supported burden, preserves provenance and unknowns, and shows why current burden is neither recoverable value nor ROI. Chapter 11 completes **Part III — Sell the Right Problem** by asking whether the evidence, customer intent, feasibility, fit, risk, and remaining owner effort justify continuing; stopping is an acceptable result. Chapter 12 begins **Part IV — Design the Right Solution**, compares several technology-intervention paths without an opaque score, and requires capability evidence before preference becomes commitment. Chapter 13 models how much burden each alternative may actually recover after adoption and realization, then compares customer cost, new work, payback, multi-year value, and incremental economics without manufacturing precision or approval. Chapter 14 bounds the resulting direction around a business outcome, workflow, actors, systems, assumptions, three-party responsibilities, and acceptance, then refuses estimate readiness when a critical technical capability remains unknown. Chapter 15 keeps value, price, direct cost, owner time, contribution, and profit distinct while testing the two-sided pricing window, structure, discounts, and cash exposure; no healthy price is an acceptable result. Chapter 16 completes Part IV by turning Chapters 8–15 into a concise customer decision, preserving revisions, and using negotiation levers rather than reflexive discounting; acceptance in principle remains separate from contract, deposit, and project start. Chapter 17 begins **Part V — Assemble the Delivery System** with source-of-truth versions, authority, agreement and payment controls, staged preconditions, commitment/cash coverage, risks, and a deliberate authorize/hold/walk-away decision; it does not select a delivery partner or start work. Chapter 18 then derives delivery capabilities, compares self, specialist, agency, vendor, customer, and mixed paths, preserves candidate evidence provenance, tests continuity and control, and prequalifies an estimate-request set without collecting estimates or selecting a provider. Chapter 19 gives those qualified paths a common scope-versioned fictional request, keeps raw delivery estimates distinct from customer price, and compares assumptions, exclusions, effort, elapsed time, confidence, partner fit, and normalized burden; its Harbor Fitness exercise selects only technical validation, not implementation. Chapter 20 completes Part V by inventorying operational control, secret-free access metadata, knowledge, responsibility, authority, dependencies, and transition risk, then tests both partner and Local Works disappearance before an explicit readiness gate; it still does not start kickoff. Chapter 21 begins Part VI by carrying those decisions into a disciplined kickoff, linked context pack, requirements baseline, owned questions, acceptance traceability, and readiness decision while keeping validation distinct from implementation. Chapter 22 then translates preserved business meaning into functional technical needs, specialist-owned questions, bounded tasks, and testable traceability while exposing missing coverage, unsupported expansion, and constraints that require deliberate review. Chapter 23 controls that fictional work with outcome milestones, explicit ownership and dependencies, causal blockers, decision latency, baseline-safe forecasts, estimate-to-complete variance, owner effort, concise updates, and proportionate corrective action. Chapter 24 then distinguishes clarification, defects, corrections, discoveries, dependencies, enhancements, and true scope changes; compares immutable baselines; and selects fair incremental commercial and delivery treatments without executing changes. Chapter 25 adds delivery-team testing, Local Works workflow QA, traceable requirement and acceptance coverage, fair defect/change triage, fix/retest and regression, disclosed known issues, and explicit fictional customer acceptance. Deployment and commercial completion remain later work.

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
