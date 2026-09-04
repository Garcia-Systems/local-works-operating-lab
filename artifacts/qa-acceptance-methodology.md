# QA and customer acceptance methodology

## The distinction that matters
**Testing** checks behavior. **Quality assurance (QA)** is the wider confidence process: scope and requirement traceability, business rules, acceptance criteria, proportional tests, evidence, defect handling, regression, documentation, and readiness. Customer acceptance is confirmation that agreed work is fit; business success may need weeks of adoption, staff-time, support-burden, or satisfaction evidence. Unless contracted, those lagging outcomes are not launch blockers.

## Plan proportional checks
Choose only relevant types: functional, business-rule, workflow, integration, data, security/access, usability, accessibility, error handling, regression, documentation, deployment, operations, or other. A compact case records its ID, links, preconditions, steps, expected and actual results, status, evidence, and notes. `BLOCKED` is not `FAIL`; retain `UNKNOWN` where evidence is absent. Evidence can be notes, logs, configuration snapshots, customer observation, recorded outcomes, or automated results—references are enough for this lab.

Trace each approved MUST requirement and acceptance criterion to meaningful cases and current results. Flag an uncovered MUST as `UNTESTED_REQUIREMENT`; “looks good” is not coverage. Test the happy path and material exceptions, not every imaginable edge. Important business rules each need a demonstrating case.

## Layers of responsibility
The delivery team first performs relevant component checks, configuration validation, integration/error-path testing, a smoke test, and documentation. Local Works then checks business workflow, scope fidelity, requirements, acceptance, important exceptions, obvious usability, known limitations, and handoff completeness. Only then should the customer validate policy correctness, representative real-world fitness, staff/member experience, and acceptance criteria—not every technical detail.

Record the conceptual environment: development, test, sandbox, staging, production-like, production, or unknown. Production-only vendor configuration is a risk, not permission to experiment carelessly. Prefer synthetic, fictional, or sanitized data and record sensitivity, source, and appropriateness at a high level; never place PII or credentials in lab artifacts.

## Risk-focused QA
Security/access checks can show that one member cannot see another's request, unauthorized staff cannot approve, delivery access is unnecessary for normal use, and secrets do not appear. These are not penetration tests or certification. Usability checks cover understandable labels/errors, clear outcomes, duplicate entry, and dead ends. Applicable accessibility basics cover labels, keyboard interaction, meaningful errors, and semantic clarity, without claiming WCAG certification.

Integration/data cases check the correct fictional record and fields, direction, duplicate handling, failure/recovery, associated member, preserved dates/status, and no lost data. A failed write must be visible and must never report false success. After a fix, run a small risk-based regression over related normal, exception, and confirmation behavior.

## Defects and changes
A defect is approved behavior not delivered. Severity describes business impact: critical may expose wrong-customer data; high may stop the core flow; medium may break an important exception; low may have a workaround; cosmetic has no workflow impact. Priority says when to act, so it stays separate. New requested behavior is a Chapter 24 change request, not a defect; matching approved behavior may be `NOT_A_DEFECT`, followed respectfully by clarification, documentation/training, or change review. Defect correction rework stays distinct from customer-paid scope-change work.

The QA cycle is TEST → DEFECT → FIX → RETEST → RESULT. Preserve cycles and retest evidence; repeated cycles may signal requirements, implementation, testing, or dependency problems without automatically blaming one party. A customer-found defect Local Works reasonably should have caught is a **QA escape**. First-pass quality and escapes are learning signals, not targets to game.

## Acceptance
Block acceptance for a failed MUST, critical/high open defect, failed criterion, incorrect important rule, unsafe access, material data-integrity issue, required missing documentation, or an in-scope unvalidated launch path. Cosmetic issues do not automatically block. A known issue may remain when noncritical, disclosed, understood, supported by an acceptable workaround and treatment, and explicitly accepted; record description, severity, impact, workaround, treatment, accepter, and review point. Never hide it.

A session should (1) restate scope, (2) demonstrate, (3) let the customer run representative cases, (4) review exceptions, (5) disclose known issues, (6) review handoff, (7) record the decision, and (8) separate defects from changes. Outcomes are accepted, accepted with known issues, conditional acceptance (materially acceptable subject to named items), rejected for defects, needs retest, blocked, or cancelled.

Rejection records the exact failed requirement/criterion, defect, evidence, action, and retest plan—not merely “unhappy.” For disagreement, inspect approved scope, requirements, acceptance wording, evidence, and decision history rather than personalities. Record ready-for-acceptance, customer-review, and acceptance dates separately so customer delay is not called QA failure; apply the previously agreed review-window concept without inventing contract language. Acceptance evidence may be a checklist, test report, system status, or conceptual email/signed record; this lab sends or signs nothing.
