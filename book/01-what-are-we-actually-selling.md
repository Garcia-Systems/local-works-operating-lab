# Chapter 1 — What Are We Actually Selling?

## 1. The trap of selling the requested technology

A customer often arrives speaking in solutions: “We need a new website,” “We want AI,” or “Build us an app.” Accepting that language as a scope is easy—and dangerous. The request may describe a preference, a symptom, or the first remedy somebody imagined. It does not yet tell us what workflow is frustrating, who experiences it, how often it happens, what consequence it has, or whether fixing it is worthwhile.

Local Works must not become a vague “we build websites and software” business. Its promise is **Make your business easier to use.** That means helping businesses remove frustrating customer and employee workflows, even when the responsible answer produces no custom build.

## 2. Problems, services, and solutions are different things

Keep five concepts separate:

1. **Business problem:** the costly or important workflow friction experienced by a customer, employee, or business.
2. **Local Works service:** the structured work Local Works performs to understand, decide, deliver, or support.
3. **Technical solution:** the selected response, if one is justified.
4. **Delivery work:** execution of an approved response by Local Works, a partner, a vendor, the customer, or a combination.
5. **Support relationship:** bounded help operating a delivered solution after launch.

Therefore:

> Customer request: “We need an app.”

is not equivalent to:

> Validated problem: Customers cannot complete a high-value workflow without repeated manual staff intervention.

And neither statement automatically implies:

> Solution: Custom application.

Configure → Integrate → Automate → Custom Build → Leave Alone describes possible **solution choices**, not the customer-facing service ladder and not a mandatory sequence. “Leave alone” can be an excellent answer.

## 3. The Local Works service ladder

Local Works sells a structured path:

**Problem → Understanding → Decision → Implementation → Ongoing operation**

The six working service stages are:

1. Digital Friction Audit
2. Discovery
3. Solution Design
4. Implementation / Delivery
5. Support
6. Continuous Improvement / Account Development

The ladder says what Local Works is doing for the customer at that moment. It does not promise that every customer climbs every rung. An honest exit is a successful service outcome when the evidence says to stop.

## 4. Digital Friction Audit

The audit asks: **Is there meaningful friction worth investigating?** It is a diagnostic entry point. Local Works listens to the request, inspects initial workflow context, and looks for evidence beneath the solution language.

Valid audit outcomes include no meaningful issue, an issue too small to pursue, an obvious configuration or process correction, or a recommendation for discovery. The audit might eventually be free, paid, or packaged in multiple forms; Chapter 1 does not decide that policy. It never guarantees software work.

## 5. Discovery

Discovery asks: **What is happening, why does it matter, and is it economically sensible to address?** Work may include stakeholder interviews, workflow reconstruction, systems inventory, frequency and volume analysis, burden estimation, constraints, authority, urgency, and technical feasibility questions.

Discovery produces understanding and a decision—not a predetermined build. **No project is a valid outcome.** Local Works should be willing to earn money by creating clarity rather than forcing implementation. “The problem is real, but the economics do not justify fixing it” protects both parties.

## 6. Solution Design

Solution design asks: **What is the simplest sensible response to the validated problem?** Only now should Local Works compare process change, configuration, integration, automation, custom build, a combination, and leaving the issue alone.

Examples of responsible recommendations are:

- “Your current software already supports this; configure it.”
- “This process should change before any software is purchased.”
- “The problem is real, but the economics do not justify fixing it.”
- “A custom build may be justified, but we do not know yet.”

Whether design later becomes billable, remains part of discovery, or is included with implementation is intentionally undecided.

## 7. Implementation

Implementation executes an approved solution; it does not discover a reason for building after work begins. Local Works retains appropriate project leadership, customer communication, coordination, and QA. Execution may involve Local Works, an independent contractor, specialist, agency, SaaS vendor, the customer's internal team, or a combination.

Owning the relationship and leading toward an agreed outcome does not require Local Works to perform every technical task. Delivery begins only after a response is justified and approved.

## 8. Support

Support helps the customer operate a delivered solution after launch. It can include bug triage, configuration assistance, third-party issue coordination, documentation, operational questions, minor changes, and incident coordination within clear boundaries.

Three adjacent categories must remain distinct:

- **Warranty work** addresses obligations arising from the delivered scope.
- **Support** helps operate the delivered solution under an agreed relationship.
- **New project work or feature expansion** changes the solution and requires a new decision.

Calling all post-launch requests “support” obscures responsibility and value.

## 9. Continuous Improvement

Continuous Improvement / Account Development periodically asks whether new friction is worth examining. It may reveal integrations, reporting, automation, operational changes, or other workflow improvements.

This is not permission for aggressive upselling. Every new opportunity must pass the same value and economics tests as the first. “Nothing worth changing now” is a valid result.

## 10. Harbor Fitness: “We need a member portal”

Harbor Fitness is a **fictional** two-location independent gym with recurring memberships. Staff handles membership questions; customers can find information online; some membership changes require staff contact; and billing runs through an existing membership system. Management suspects that joining and account management are frustrating and says:

> “We think we need a new member portal.”

That statement establishes a requested solution, not a problem definition. We do not yet know which workflows cause friction, who encounters it, its frequency or burden, why staff contact is required, or what the current system supports. We have no basis to select architecture, claim financial effects, or promise a portal.

The next service is a **Digital Friction Audit**. Its proper first question is:

> **What friction are members and staff actually experiencing?**

The initial-request artifact preserves known facts, unknowns, the premature portal assumption, and the next service without solving the fictional case.

## 11. Executable exercise

Run from the repository root:

```bash
python scripts/run_chapter_01.py
```

The exercise uses explicit fictional cases rather than fuzzy classification or an artificial-intelligence guess. For each statement it prints the observed request, first Local Works service, reason not to jump into implementation, and whether a technical solution has been selected.

Two boundary cases matter. Correcting an old phone number in an editable notification calls for a proportionate configuration fix and exit—not discovery. Duplicate questions in a handoff checklist call for a process correction and observation before software. Small, clear answers are not failed sales.

## 12. What this changes about the future Local Works business

Local Works primarily performs marketing, qualification, audits, discovery, workflow and economic analysis, solution design, proposal development, sales, project leadership, customer communication, QA, and support coordination. Its customer value cannot depend exclusively on selling code.

The operating model must preserve a customer's words while allowing evidence to change the response. It must also make walking away legible: stopping after an audit, discovery, or design can demonstrate judgment rather than pipeline failure. Chapter 1 records possible production-system capabilities prompted by these needs, but does not design a production system.

## 13. Chapter artifacts

- `artifacts/service-ladder.md` is the detailed working definition of each service stage.
- `artifacts/harbor_fitness/01-initial-request.md` records the fictional case without invented results.
- `artifacts/production-system-discovery.md` records the evidence-backed operating needs exposed by this exercise.
- `local_works/services.py` makes the ladder and examples inspectable and testable.

## 14. Readiness checkpoint

Before moving beyond Chapter 1, the reader should be able to answer:

- Can I distinguish a customer's requested solution from a validated business problem?
- Can I name what Local Works is doing at each service stage?
- Can an audit or discovery succeed without producing implementation? **Yes.**
- Is Solution Design the same as Delivery? **No.**
- Are Support and Continuous Improvement interchangeable? **No.**
- Has Harbor Fitness been promised a portal? **No.**
- Have pricing, proposal logic, CRM behavior, or partner selection been decided? **No.**

Chapter 1 ends with disciplined uncertainty: Local Works sells an attempt to improve a business outcome through a structured service path. Technology comes later.
