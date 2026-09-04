# Chapter 17 — Close Without Disaster

## Part V — Assemble the Delivery System

**Core question:** What must happen after the customer says “yes” but before Local Works commits people, money, or delivery?

> **A CUSTOMER SAYING “YES” IS NOT THE SAME AS A SAFE PROJECT START.**

This chapter is operational/commercial training, not legal advice or contract drafting. Harbor Fitness remains fictional.

## 1. “Yes” is not yet a safe project

`INTERESTED`, `VERBAL_YES`, `ACCEPTED_IN_PRINCIPLE`, `AGREEMENT_READY`, `AGREEMENT_EXECUTED`, `DEPOSIT_REQUIRED`, `DEPOSIT_RECEIVED`, `PRECONDITIONS_SATISFIED`, and `AUTHORIZED_TO_PROCEED` are distinct facts. “Sounds good; let's do it” authorizes no hiring, software purchase, paid reservation, custom development, or non-refundable cost.

## 2. The dangerous gap between sale and delivery

The sequence is acceptance in principle → close checklist → agreement/terms → payment commitment → delivery preconditions → go/hold/walk away → authorization for delivery preparation. The checklist turns enthusiasm into a controlled decision without treating the customer as dishonest.

## 3. Identify the accepted version

Record proposal version, scope revision, pricing version, payment structure, assumptions, and exclusions. A customer expecting version 1 at $6,000 with reporting and Local Works expecting version 2 at $5,000 without reporting will almost certainly conflict. Block until reconciled.

## 4. Confirm authority

Record decision maker, budget owner, authorized signer, technical approver, and procurement contact as confirmed, unconfirmed, or insufficient. The person who values the solution may lack budget or signing authority. Missing required signer authority blocks authorization.

## 5. Agreement readiness

Confirm business/legal names, Local Works's appropriate entity, accepted versions, price/payment, responsibilities, assumptions, exclusions, acceptance, dependencies, ownership, and support. Results can be ready, need commercial clarification, need scope revision, or need risk review.

## 6. Proposal vs agreement

A proposal supports a commercial decision. An agreement defines the understood working relationship. A signed proposal sometimes participates in an agreement, but this lab draws no legal conclusion. Agreement topics require qualified counsel. Harbor Fitness is a display name; its contracting entity remains unknown. Local Works is the customer-facing initiative and Garcia Systems is the broader operating-company context—neither fact permits invented legal certainty.

## 7. Payment commitment

Track not required, invoice ready/sent, due, partly paid, paid, overdue, or waived. These are records only: the lab does not invoice, collect, or transfer money.

## 8. Deposits

When the agreed structure requires a deposit, a signature without receipt remains a hard guardrail. “Start the developer; the check is coming” receives `HOLD_FOR_PAYMENT`, unless Local Works makes and documents a deliberate exception rather than accidentally financing the customer.

## 9. Non-refundable commitments

Reservations, setup fees, licenses, travel, hardware, vendor charges, and retainers can expose cash. Record amount, payee, purpose, refundability, customer funds, approval, and status before commitment. No informal commitments.

## 10. Cash coverage

Subtract immediate commitments from funds received. A $1,500 deposit against a $5,000 partner commitment and $500 other cost creates $4,000 exposure. Future contribution does not remove present liquidity risk. A customer request that Local Works front $3,000 for a vendor requires responsibility, refundability, timing, and funding review.

## 11. Preconditions

Place each condition at the stage it truly controls: signer authority before authorization; capability, API entitlement, test access, sample data, partner availability, and security/access before implementation when appropriate; policy approval and launch data before launch. Not every unknown blocks every stage.

## 12. Critical assumptions

Carry uncertainty forward. Platform capability, subscription entitlement, and test access do not become facts because the sale progressed. Use paid validation or a technical hold when a critical assumption remains unresolved.

## 13. Hard blockers

Unknown versions/scope, unconfirmed authority, missing required agreement/deposit, material hidden scope, invalid critical capability, impossible payment, unacceptable exposure, included/excluded disagreement, unavailable required access, or no delivery path can block authorization explicitly.

## 14. Soft risks

Customer review availability, a minor vendor documentation gap, optional reporting detail, and low-impact schedule uncertainty may remain visible without becoming fatal. Closing is judgment, not a magic score.

## 15. Ownership and access questions

Do not invent answers. Register who owns custom deliverables, customer data, reusable methods, third-party software, licenses, repository/access, and continuity if a partner disappears. Customers authorize legitimate access; Local Works requests the minimum necessary, prefers test data, avoids casual credential sharing, and keeps access revocable.

## 16. Third parties and subcontractors

Record subcontractor use as allowed, requires notice, requires approval, or unknown. Surface material delivery realities. Third-party pricing, terms, uptime, limits, support, and policy can change; Local Works cannot guarantee permanent external behavior.

## 17. Support and warranty boundaries

Clarify limited defect correction, separate support, excluded feature work, and treatment of third-party problems. This prevents accidentally unlimited responsibility without attempting Chapter 27's support design.

## 18. Delivery capacity

Capacity can be available, tentative, unavailable, or unknown. Chapter 17 only says whether it must be validated; Chapter 18 selects no partner here.

## 19. Target vs committed start

A target is an aspiration used for planning. A committed date is a promise backed by sufficiently established conditions and capacity. With an unselected partner, manufacture no certainty.

## 20. Go, hold, or walk away

Choose authorization for the next stage, a requirement/payment/technical/customer hold, restructuring, decline, or pre-start cancellation. Authorization only permits assembling delivery. It does not begin implementation.

For pre-start cancellation, record performed work, incurred cost, refundable/non-refundable commitments, and possible payment treatment. After signing/payment, review agreement, costs, reservations, cancellation terms, and communication rather than improvising. Commercial treatment depends on the governing agreement.

## 21. Harbor Fitness close

Harbor Fitness accepted proposal version 2 in principle: scope revision B, $6,000, 50% deposit/50% acceptance, cancellation excluded. Its contracting entity and signer remain unknown; the agreement is ready but needs risk review and is not executed; no $3,000 deposit was received. Capability/API, ownership, access, subcontractor treatment, third-party behavior, and delivery capacity remain open. Result: `HOLD_FOR_PAYMENT`, with additional close and validation requirements.

## 22. Failure: verbal yes

A “go ahead” prompts a $4,000 contractor reservation. Budget approval then fails. Local Works owns $4,000 exposure. **VERBAL ENTHUSIASM IS NOT COMMERCIAL AUTHORIZATION.**

## 23. Failure: wrong proposal

One party expects reporting included at $6,000; the other expects it excluded at $5,000. Starting turns a detectable discrepancy into a delivery conflict. Block first.

## 24. Failure: no cash coverage

A $1,500 deposit cannot cover $5,500 immediate cost. A project might contribute later and still present a $4,000 cash-flow problem now.

## 25. Success: controlled close

Version 3 is identified; signer confirmed; agreement executed; 50% deposit received; assumptions identified; validation scheduled; no non-refundable partner commitment made. `AUTHORIZE_NEXT_STAGE` allows Local Works to assemble delivery—not implement tomorrow.

## 26. Executable exercise

Run `python scripts/run_chapter_17.py`. Inspect the version, authority, agreement, deposit, commitments, coverage, stage-specific conditions, risks, checklist, failure cases, and conservative decision. Then run `python -m pytest`.

## 27. Chapter artifacts

- `artifacts/harbor_fitness/17-commercial-close.md`
- `artifacts/commercial-close-template.md`
- `artifacts/close-checklist-template.md`
- `artifacts/agreement-topics.md`
- `artifacts/commercial-closing-methodology.md`

## 28. Readiness checkpoint

The reader can distinguish interest from authorization; freeze accepted versions; confirm authority; explain proposal versus agreement and deposits; calculate exposure; identify non-refundable commitments; stage preconditions; preserve assumptions; separate hard blockers from soft risks; catch scope disagreement; register ownership/access and partner/external dependencies; separate target and committed dates; and choose authorize, hold, restructure, decline, or cancellation.

Stop here. Chapter 18 asks who should perform the technical work and how to choose a delivery path without dependence on the wrong partner. It has not been implemented.
