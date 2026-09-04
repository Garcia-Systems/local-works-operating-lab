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

## Run Chapter 0

Python 3.11 or newer is required.

```bash
python scripts/run_chapter_00.py
python -m pytest
```

The exercise prints the initial hypotheses grouped by business test and distinguishes beliefs from observations and measurements.

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

There is no web application, API, authentication, CRM, dashboard, portal, database, ORM, customer CRUD, or speculative production feature list. Harbor Fitness, the first planned fictional customer, is not analyzed here. Chapter 0 establishes the experiment only; it does not begin Chapter 1 or decide on any solution.
