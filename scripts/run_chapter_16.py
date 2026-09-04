#!/usr/bin/env python3
"""Chapter 16: deterministic fictional proposal and negotiation exercise."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.pricing import (ContributionAnalysis, CustomerEconomicsView,
    LocalWorksEconomicsView, PaymentEvent, PaymentStructure, PaymentTiming,
    PriceScenario, PricingModel)
from local_works.proposals import discount_impact

money=lambda n: f"${n:,.0f}"
price=6000
analysis=ContributionAnalysis(price,2800,400,24,75)
print("CHAPTER 16 — PROPOSAL AND NEGOTIATION")
print("FICTIONAL TRAINING SCENARIO\nNOT A REAL CUSTOMER PROPOSAL")
print("\nSECTION 1 — Proposal inputs")
print("Problem: eligible membership-freeze requests require repeated staff handling")
print("Economic burden: $18,600/year HYPOTHETICAL; retention impact UNKNOWN")
print("Solution direction: paid capability validation, then CONFIGURE; INTEGRATE only if required")
print("Scope: freeze request through recorded decision/confirmation; cancellation excluded")
print("Price: $6,000 | Payment: 50% after contract, 50% at acceptance")
print("Assumptions: vendor capability, test access, approved policy, delivery estimate")
print("\nSECTION 2 — Generate concise proposal")
print("Reduce repeated freeze-request handling with the simplest validated path while preserving rules. Base scope excludes cancellation and platform replacement. Estimated outcomes are not guarantees.")
print("\nSECTION 3 — Proposal consistency check")
print("PASS: Chapter 14 inclusion/exclusion preserved; Chapter 15 price is $6,000; Chapter 13 claims remain hypothetical; retention remains UNKNOWN.")
print("\nSECTION 4 — Customer response")
print('“Your price is higher than another developer\'s quote.”')
print("\nSECTION 5 — Analyze objection")
print("Compare discovery, workflow, capability validation, coordination, QA, acceptance, documentation, support, third-party costs, and ownership. The developer may genuinely offer the better fit; do not disparage them.")
print("\nSECTION 6 — Customer asks for 15–20% discount")
for rate in (.15,.20):
 d=discount_impact(analysis,rate); print(f"{rate:.0%}: price {money(d.discounted_price)}, contribution {money(d.contribution)}, contribution reduction {d.contribution_change_rate:.1%}")
print("\nSECTION 7 — Counter with scope/phasing")
print("Phase 1: paid capability validation/configuration. Phase 2: integration only if required, supported, and repriced. No reflexive discount.")
print("\nSECTION 8 — Customer adds cancellation workflow")
print("OPTIONAL / PHASE_2 / REPRICE — cancellation remains excluded from base price.")
no_dep=PaymentStructure(PaymentTiming.ON_COMPLETION,(PaymentEvent(2,6000,"launch"),),(PaymentEvent(0,2800,"partner startup"),PaymentEvent(1,400,"other direct")))
print("\nSECTION 9 — Customer asks for no deposit")
print("Maximum Local Works cash exposure:",money(no_dep.maximum_cash_exposure),"=> COUNTER WITH PAYMENT STRUCTURE.")
print("\nSECTION 10 — Customer asks for ROI guarantee")
print("DECLINE unsupported guarantee: adoption, volume, policy, employee use, and vendor behavior matter. Preserve observable delivery acceptance commitments.")
print("\nSECTION 11 — Revised proposal")
print("Version 2: phased validation; integration conditional/repriced; cancellation excluded; 50/50 payment retained; no ROI guarantee; Version 1 preserved.")
print("\nSECTION 12 — Final customer decision\nACCEPTED_IN_PRINCIPLE — Phase 1 only; not a contract or project start.")
print("\nSECTION 13 — Local Works decision")
print("CONDITIONALLY HEALTHY: proceed to closing controls only. WALK AWAY if payment protection, truthful claims, bounded scope, capability, or viable economics fail.")
print("\nSECTION 14 — Lessons")
print("Protecting evidence, scope, economics, and cash matters more than winning. A postponement or lost sale can be a successful decision.")
print("\nFAILURE — BAD DISCOUNTING")
print("$10,000 price - $6,000 direct cost = $4,000 contribution. 25% discount => $7,500 - $6,000 = $1,500; less $2,000 owner time = -$500. DO NOT ACCEPT UNCHANGED SCOPE.")
print("Alternatives: reduce/re-cost scope, phase, simplify, restore price, or decline.")
print("\nFAILURE — SCOPE CREEP DURING SALES")
print("One workflow + reporting + mobile + migration + integration at the same price collapses economics before contract execution.")
print("\nSUCCESS — PHASED DEAL")
print("Validation first creates smaller commitment, lower risk, stronger evidence, a better estimate, and an easier stop decision.")
