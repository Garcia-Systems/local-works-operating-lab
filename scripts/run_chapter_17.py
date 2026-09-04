#!/usr/bin/env python3
"""Chapter 17: deterministic fictional commercial-close exercise."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.closing import *

money = lambda value: f"${value:,.0f}"
version = CommercialVersionReference(
    "Proposal version 2", "14-project-scope revision B", "Chapter 15 price revision 1",
    6000, "50% deposit / 50% acceptance",
    ("Existing platform capability and API access require validation", "Customer can provide test access"),
    ("Membership cancellation",),
)
agreement = AgreementRecord("Harbor Fitness", None, "Local Works", "Garcia Systems",
    AgreementReadiness.NEEDS_RISK_REVIEW, AgreementStatus.READY,
    ("scope", "payment", "acceptance", "change handling", "support boundary",
     "third-party dependencies", "ownership", "subcontractor use"))
payment = PaymentCommitment(True, 3000, 0, PaymentStatus.INVOICE_READY)
close = CommercialClose("Harbor Fitness", CloseStatus.ACCEPTED_IN_PRINCIPLE, version, agreement, payment,
    authorities=[
      AuthorityRecord(AuthorityRole.DECISION_MAKER, "Operations lead (fictional)", AuthorityStatus.CONFIRMED, "Chapter 16 discussion"),
      AuthorityRecord(AuthorityRole.BUDGET_OWNER, "Owner (fictional; identity not recorded)", AuthorityStatus.UNCONFIRMED),
      AuthorityRecord(AuthorityRole.AUTHORIZED_SIGNER, "UNKNOWN", AuthorityStatus.UNCONFIRMED)],
    commitments=[
      CommitmentAuthorization("Potential specialist validation reservation", 1200, False, "Unselected specialist", "Validate platform capability"),
      CommitmentAuthorization("Fictional tool setup", 300, True, "Third-party tool", "Test environment")],
    preconditions=[
      Precondition("Confirm authorized signer", PreconditionStage.REQUIRED_BEFORE_AUTHORIZATION, RequirementStatus.NOT_SATISFIED, True),
      Precondition("Validate platform capability and API entitlement", PreconditionStage.REQUIRED_BEFORE_IMPLEMENTATION, RequirementStatus.UNKNOWN, True),
      Precondition("Provide revocable test access and sample data", PreconditionStage.REQUIRED_BEFORE_IMPLEMENTATION, RequirementStatus.UNKNOWN),
      Precondition("Approve launch policy and staff communication", PreconditionStage.REQUIRED_BEFORE_LAUNCH, RequirementStatus.UNKNOWN)],
    requirements=[
      CloseRequirement("Accepted proposal version identified", RequirementStatus.SATISFIED, True),
      CloseRequirement("Scope version identified", RequirementStatus.SATISFIED, True),
      CloseRequirement("Price and payment structure confirmed", RequirementStatus.SATISFIED, True),
      CloseRequirement("Customer authority confirmed", RequirementStatus.NOT_SATISFIED, True),
      CloseRequirement("Agreement readiness confirmed", RequirementStatus.NOT_SATISFIED, True),
      CloseRequirement("Agreement executed", RequirementStatus.NOT_SATISFIED, True),
      CloseRequirement("Deposit status confirmed", RequirementStatus.SATISFIED),
      CloseRequirement("Critical assumptions reviewed", RequirementStatus.SATISFIED),
      CloseRequirement("Preconditions classified", RequirementStatus.SATISFIED),
      CloseRequirement("Immediate spend identified", RequirementStatus.SATISFIED),
      CloseRequirement("Cash coverage checked", RequirementStatus.SATISFIED),
      CloseRequirement("Customer responsibilities acknowledged", RequirementStatus.UNKNOWN),
      CloseRequirement("Local Works responsibilities acknowledged", RequirementStatus.UNKNOWN),
      CloseRequirement("Delivery responsibilities understood", RequirementStatus.UNKNOWN),
      CloseRequirement("Security/access boundaries acknowledged", RequirementStatus.UNKNOWN),
      CloseRequirement("Change mechanism understood", RequirementStatus.SATISFIED),
      CloseRequirement("Support/warranty boundary acknowledged", RequirementStatus.UNKNOWN)],
    risks=[
      CloseRisk(RiskCategory.ASSUMPTION_RISK, "HIGH", "OPEN", "Capability/API entitlement unconfirmed", "Paid validation before implementation", True),
      CloseRisk(RiskCategory.OWNERSHIP_RISK, "MEDIUM", "OPEN", "Repository and custom-deliverable ownership unresolved", "Review in agreement", True),
      CloseRisk(RiskCategory.DELIVERY_CAPACITY_RISK, "MEDIUM", "OPEN", "Partner not selected", "Validate in Chapter 18", False),
      CloseRisk(RiskCategory.THIRD_PARTY_RISK, "MEDIUM", "OPEN", "Vendor pricing, terms and behavior can change", "State dependency and allocate review", False)],
    ownership_questions=[OwnershipQuestion("Who owns custom deliverables and controls repository access?"), OwnershipQuestion("What licenses govern reusable methods and third-party software?")],
    subcontractor_use=SubcontractorUse.UNKNOWN, delivery_capacity=DeliveryCapacity.UNKNOWN,
)
print("CHAPTER 17 — CLOSE WITHOUT DISASTER\nPART V — ASSEMBLE THE DELIVERY SYSTEM")
print("FICTIONAL TRAINING SCENARIO\nNOT A REAL CONTRACT OR PAYMENT RECORD")
print("\nSECTION 1 — Commercial outcome from Chapter 16")
print(f"Customer decision: {close.customer_decision.name}\nLocal Works decision: proceed to close controls only\nProposal: {version.proposal_version}\nScope: {version.scope_version}; cancellation excluded\nPrice: {money(version.price)}\nPayment: {version.payment_structure}")
print("\nSECTION 2 — Authority")
for a in close.authorities: print(f"{a.role.name}: {a.person} — {a.status.name}")
print("\nSECTION 3 — Agreement readiness")
print(f"{agreement.readiness.name}; agreement status: {agreement.status.name}. Customer contracting entity remains UNKNOWN.")
print("\nSECTION 4 — Agreement topics")
print("Agreement topics to review with qualified counsel: " + ", ".join(agreement.topics_reviewed) + ". This is not legal advice.")
print("\nSECTION 5 — Deposit requirement")
print(f"Required: YES; amount: {money(payment.deposit_amount)}; status: {payment.status.name}; effect: NOT AUTHORIZED TO INCUR DELIVERY COST")
print("\nSECTION 6 — Immediate commitments")
for c in close.commitments: print(f"{c.description}: {money(c.amount)}; {'refundable' if c.refundable else 'NON-REFUNDABLE'}; not authorized")
print("\nSECTION 7 — Cash coverage")
print(f"Funds: {money(payment.funds_received)}; commitments: {money(close.immediate_commitments)}; exposure: {money(close.cash_exposure)}")
print("\nSECTION 8 — Preconditions")
for p in close.preconditions: print(f"{p.stage.value.upper()}: {p.description} — {p.status.name}")
print("\nSECTION 9 — Critical assumptions")
for a in version.assumptions: print(f"UNKNOWN: {a}")
print("\nSECTION 10 — Close checklist")
for item in close.requirements: print(f"[{item.status.name}] {item.description}")
print("\nSECTION 11 — Blocker simulation")
print('Customer: “Start now. Deposit will arrive next week.”\nDecision: HOLD_FOR_PAYMENT. Local Works does not casually finance the project.')
print("\nSECTION 12 — Scope misunderstanding simulation")
print('Customer: “I assumed cancellations were included too.”\nSCOPE DISAGREEMENT — BLOCK AUTHORIZATION UNTIL RECONCILED; cancellation is excluded.')
print("\nSECTION 13 — Ownership question")
for q in close.ownership_questions: print(f"{q.status}: {q.question}")
print("\nSECTION 14 — Delivery-capacity uncertainty")
print("Capacity: UNKNOWN; partner not selected; target start: tentative after close; committed start: NOT AVAILABLE.")
print("\nSECTION 15 — Final close decision")
print(close.decide().name)
print("Blockers: " + "; ".join(close.hard_blockers))
print("\nSECTION 16 — Interpretation")
print("Closing is a risk-control process, not paperwork after the ‘real sale.’ Authorization would permit delivery preparation, not implementation.")
print("\nFAILURE — STARTING ON A VERBAL YES")
print("Customer says ‘Go ahead’; Local Works incurs a $4,000 contractor reservation; budget approval fails. Exposure: $4,000. VERBAL ENTHUSIASM IS NOT COMMERCIAL AUTHORIZATION.")
print("\nFAILURE — WRONG PROPOSAL VERSION")
print("Customer expects version 1: $6,000 with reporting. Local Works expects version 2: $5,000 without reporting. BLOCK AUTHORIZATION UNTIL VERSION IS RECONCILED.")
print("\nFAILURE — NO CASH COVERAGE")
print("Deposit $1,500; partner $5,000; other costs $500; cash exposure $4,000. Later contribution does not remove today's cash-flow risk.")
print("\nSUCCESS — CONTROLLED CLOSE")
print("Version 3 accepted; signer confirmed; agreement executed; 50% deposit received; validation scheduled; no non-refundable partner commitment. AUTHORIZE_NEXT_STAGE means assemble delivery, not implement tomorrow.")
