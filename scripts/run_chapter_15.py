#!/usr/bin/env python3
"""Chapter 15 executable exercise: internal pricing analysis, not a quote."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.pricing import (
    ContributionAnalysis, CustomerEconomicsView, LocalWorksEconomicsView,
    PaymentEvent, PaymentStructure, PaymentTiming, PriceScenario, PricingDecision,
    PricingModel, PricingWindow, customer_ceiling_for_payback, discount_sensitivity,
)

money = lambda value: f"${value:,.0f}" if value is not None else "UNKNOWN"
months = lambda value: f"{value:.1f} months" if value is not None else "UNKNOWN"

current_burden = 18_600.0
recoverable_value = 9_600.0
recurring_cost = 1_200.0
delivery_cost = 2_800.0
other_cost = 400.0
owner_hours = 24.0
owner_rate = 75.0  # internal planning value, not a customer rate
price = 6_000.0
customer = CustomerEconomicsView(current_burden, recoverable_value, recurring_cost, price,
                                 evidence_quality="HYPOTHETICAL / needs validation")
lw = LocalWorksEconomicsView(delivery_cost, other_cost, owner_hours, owner_rate,
                             required_direct_contribution=800)
scenario = PriceScenario("bounded configuration", PricingModel.FIXED_FEE, customer, lw,
                         "MUST items plus one SHOULD reporting item")
ceiling = customer_ceiling_for_payback(customer.annual_net_benefit, 12)
window = PricingWindow(lw.economic_floor, ceiling)

print("CHAPTER 15 — PRICE THE ENGAGEMENT")
print("FICTIONAL TRAINING SCENARIO\nNOT A REAL CUSTOMER QUOTE\n")
print("SECTION 1 — Starting economics")
print("Current burden:", money(current_burden), "/ year")
print("Recoverable value:", money(recoverable_value), "/ year (hypothesis)")
print("Preferred solution direction: configure existing tools with bounded automation")
print("Scope status: READY FOR ESTIMATE, subject to capability validation\n")
print("SECTION 2 — Local Works cost hypothesis")
print("PRELIMINARY ASSUMPTIONS — not validated quotes")
print("Delivery cost:", money(delivery_cost), "| Other direct cost:", money(other_cost))
print("Owner hours:", owner_hours, "| Owner-hour internal planning value:", money(owner_rate))
print("Imputed owner-time cost:", money(lw.imputed_owner_time_cost), "(internal only)\n")

analysis = scenario.contribution
print("SECTION 3 — Candidate price")
print("Customer price:", money(price))
print("Direct contribution:", money(analysis.contribution))
print("Contribution margin:", f"{analysis.contribution_margin:.1%}")
print("Contribution after owner-time value:", money(analysis.contribution_after_owner_time))
print("Contribution is not accounting profit.\n")

print("SECTION 4 — Customer view")
print("First-year customer cost:", money(customer.first_year_cost))
print("Annual net benefit after recurring cost:", money(customer.annual_net_benefit))
print("Payback using candidate customer price:", months(customer.payback_months))
for year in (1, 2, 3): print(f"{year}-year customer result:", money(customer.cumulative_customer_result(year)))

print("\nSECTION 5 — Pricing window")
print("Local Works economic floor:", money(window.floor))
print("Customer ceiling at stated 12-month payback guardrail:", money(window.ceiling))
print("Practical window:", f"{money(window.floor)}–{money(window.ceiling)}" if window.has_overlap else "NO OVERLAP")

print("\nSECTION 6 — Price sensitivity")
for candidate in (3_000, 4_500, 6_000, 8_000):
    view = CustomerEconomicsView(current_burden, recoverable_value, recurring_cost, candidate)
    con = lw.contribution_at(candidate)
    print(money(candidate), "| payback", months(view.payback_months), "| contribution",
          money(con.contribution), "| after owner time", money(con.contribution_after_owner_time))

print("\nSECTION 7 — Discount sensitivity")
for rate in (.05, .10, .20):
    result = discount_sensitivity(analysis, rate)
    print(f"{rate:.0%}: price {money(result.discounted_price)}; contribution {money(result.contribution)}; "
          f"contribution reduction {result.contribution_change_rate:.1%}")

cost_events = (PaymentEvent(0, 2_800, "partner startup"), PaymentEvent(1, 400, "direct tools"))
no_deposit = PaymentStructure(PaymentTiming.ON_COMPLETION,
    (PaymentEvent(2, price, "completion"),), cost_events)
deposit = PaymentStructure(PaymentTiming.DEPOSIT_PLUS_FINAL,
    (PaymentEvent(0, price / 2, "deposit"), PaymentEvent(2, price / 2, "acceptance")), cost_events)
print("\nSECTION 8 — Payment timing")
print("No deposit maximum cash exposure:", money(no_deposit.maximum_cash_exposure))
print("50% deposit / 50% acceptance maximum cash exposure:", money(deposit.maximum_cash_exposure))
print("Deposit timing is not revenue-recognition guidance.\n")

print("SECTION 9 — Scope reduction")
reduced = ContributionAnalysis(5_200, 2_300, 300, 21, owner_rate)
reduced_customer = CustomerEconomicsView(current_burden, 8_700, recurring_cost, 5_200)
print("Remove SHOULD reminder reporting: price $5,200; delivery $2,300; recoverable value $8,700")
print("Contribution:", money(reduced.contribution), "| customer payback:", months(reduced_customer.payback_months))
print("Price and scope changed separately; neither change is automatic.\n")

print("SECTION 10 — Phased option")
print("Phase 1 capability validation: $900; optional Phase 2 bounded implementation: $5,100")
print("Structure: PHASED; Phase 2 proceeds only with evidence and refreshed estimate.\n")
print("SECTION 11 — No-deal case")
no_deal = PricingWindow(6_000, 4_000)
print("Healthy floor $6,000; customer ceiling $4,000; decision:", no_deal.decision.name)
print("Responses: reduce scope, simplify, phase, customer implements, leave alone, or decline.\n")
print("SECTION 12 — Harbor Fitness pricing decision")
print("Decision:", PricingDecision.PHASE_PROJECT.name)
print("Candidate $6,000 is inside the hypothesis window, but validate platform capability, partner cost,")
print("customer adoption/value evidence, internal effort, acceptance dependency, and payment willingness before proposal.")

print("\nTHREE CONTRASTING EXAMPLES")
print("A. High customer value, $3,200 price, $3,000 cash costs and owner effort: raise price, reduce scope, or decline.")
print("B. $12,000 price yields strong contribution but poor customer payback: restructure, reduce scope, or leave alone.")
print("C. $6,000 floor and $4,000 ceiling: NO HEALTHY PRICE is a successful analytical result.")
print("\nNo proposal has been issued. Pricing does not guarantee a sale.")
