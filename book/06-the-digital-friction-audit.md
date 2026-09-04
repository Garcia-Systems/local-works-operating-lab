# Chapter 6 — The Digital Friction Audit

## 1. Looking for friction without looking for software

The Digital Friction Audit asks one bounded question: **is there enough evidence of
meaningful customer or employee workflow friction to justify further investigation?**
It does not ask what software to build. It is allowed to find no problem, recommend
monitoring, or stop. This makes the audit a diagnostic offer rather than a mechanism
for manufacturing implementation work.

## 2. The customer journey

Local Works begins with **Find → Understand → Contact → Book or Join → Pay → Receive
Service → Manage → Return**. This is a prompt, not a mandatory pipeline. A restaurant
might use Find, Understand, Reserve, Visit, Pay, Return; a gym might use Join and Use;
home services might use Contact, Schedule, and Receive Service. Name the business's
actual path and omit irrelevant stages.

The compact questions in `AUDIT_QUESTIONS` ask whether key information is
discoverable, whether a customer can complete a step, where information repeats,
what requires staff intervention, how payment exceptions work, how status and
handoffs work, what can be self-managed, and whether a returning customer can resume.

## 3. The employee workflow behind the journey

Customer and operational journeys are connected. A required phone call can create
verification, system switching, data entry, confirmation, and a manager billing
exception. Conversely, a seamless form can hide employee re-entry. Follow the work
after each customer action and label whether customers, employees, managers, or
several parties are affected.

## 4. What counts as friction?

The model names potentially unnecessary calls and emails, paper, repeated data,
manual entry, switching systems, waiting, in-person requirements, unclear information,
duplicate work, manual handoffs, uncertain status, error-prone steps, repetitive
administration, and disconnected systems. The taxonomy helps observers use consistent
language; the label alone does not establish significance.

## 5. Phone calls and human interaction are not automatically bad

A tour, sensitive conversation, or welcoming check-in can be valuable service. Ask
whether the interaction is **unnecessarily required**, whether a customer wants the
human help, and whether it advances a legitimate operational goal. “Uses the phone”
is an observation; “bad process” requires more evidence.

## 6. Observation vs inference

Keep two fields. **Observed fact:** the public page directs membership freezes to the
front desk. **Friction hypothesis:** this may inconvenience members and consume staff
time. That observation does not establish dislike, frequency, lost revenue, cause,
or that a portal would solve anything. Chapter 3's evidence discipline still applies.

## 7. Evidence sources

Public websites, booking/membership flows, and documents support bounded public
observations and useful questions. Customer, employee, and manager statements add
perspectives. Direct workflow observation, system demonstrations, process documents,
and measured data can support stronger operational, frequency, or burden claims.
Evidence labels matter, but no elaborate point system substitutes for source scope.

## 8. Frequency, severity, and significance

Consider frequency and severity alongside affected parties, manual effort, customer
inconvenience, error potential, business criticality, and evidence strength. Print
the dimensions and reasoning instead of hiding them in a magic score. A severe rare
exception and a mild daily task invite different questions; neither automatically
requires software.

## 9. UNKNOWN is legitimate

`UNKNOWN` means evidence has not established a value. `LOW` is an affirmative,
supported assessment. Turning missing frequency, satisfaction, or effort into low
would create false confidence. An audit can recommend gathering information precisely
because frequency and severity remain unknown.

## 10. Customer convenience vs business objectives

One-click cancellation may help a member while a gym values a retention conversation.
Record customer friction, the business objective, policy rationale, contractual or
regulatory reason, and the tradeoff. Do not automatically declare either party right.
Later work can evaluate a balanced response after the facts are known.

## 11. False positives

Harbor Fitness's fictional legal-name correction requires a call. That initially
resembles friction. Additional fictional manager context says the request is extremely
rare and requires identity verification. The finding is downgraded to low significance:
probably leave it alone unless errors or complaints emerge. Visible inconvenience is
not synonymous with worthwhile opportunity.

## 12. Hidden employee friction

The fictional online join form looks clean to customers. A permitted internal system
demonstration then shows employees copying submissions to a membership system. That
is stronger evidence of a manual step, but volume, time, errors, constraints, and
economics still require measurement. Public-only audits have important limits.

## 13. Harbor Fitness audit

The exercise records adequate location discovery, optional human tours, a working
observed payment path, friendly check-in, and easy return visits. It also records
unclear membership terms as a question; manual join-form re-entry as observed internal
friction; and staff-required freezes/cancellations as a cross-party hypothesis with
a business-policy tradeoff. This neutral inventory avoids selling by diagnosis.

## 14. Audit recommendations

The available endpoints are **No meaningful friction, Monitor, Simple improvement,
Discovery recommended,** and **Insufficient information**. There is deliberately no
custom-build outcome. Harbor Fitness receives **Discovery recommended** because the
manual re-entry is corroborated and routine membership changes deserve bounded
internal investigation. It is not a project recommendation.

## 15. Executable exercise

Run:

```bash
python scripts/run_chapter_06.py
```

The output walks every relevant stage and prints the observation, hypothesis,
parties, sources, known facts, unknowns, follow-up question, frequency, severity,
disposition, grouped summary, and qualified recommendation. All Harbor Fitness inputs
are fictional training data.

## 16. Audit limitations

An audit cannot establish facts beyond its sources. In particular, public review
usually cannot reveal internal handling, volume, exceptions, economics, sentiment,
policy, root cause, or technical constraints. Observe normal public paths ethically;
do not scrape, evade controls, impersonate a customer, submit disruptive forms, or
access internal systems without permission. No financial impact or solution is
established in this chapter.

## 17. Chapter artifacts

- `artifacts/audit-methodology.md` defines the operating method and boundaries.
- `artifacts/digital-friction-audit-template.md` is the reusable field document.
- `artifacts/harbor_fitness/06-digital-friction-audit.md` is the fictional professional report.
- `local_works/audit.py` preserves the method in readable executable concepts.

## 18. Readiness checkpoint

Before continuing, the reader should be able to explain:

- the audit's question and why it does not select technology;
- observed fact versus friction hypothesis;
- why public evidence is useful but limited and employee workflows matter;
- why a call or human interaction may be good service;
- why `UNKNOWN` differs from `LOW`;
- why adequate processes and false positives must be documented; and
- why discovery recommended means permission to investigate—not permission to build.

Chapter 7 is intentionally not implemented here.
