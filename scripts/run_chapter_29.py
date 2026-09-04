#!/usr/bin/env python3
"""Run Chapter 29's fictional recurring-support economics exercise."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.support import SupportEntitlement, SupportPlan, SupportRequestType
from local_works.support_economics import *


OWNER_VALUE = 75.0
PARTNER_RATE = 100.0


def scenario(name: str, revenue: float, owner: float, partner: float, incidents: int = 0,
             after_hours: int = 0, partner_available: bool = True,
             direct: float = 50.0) -> SupportScenario:
    risk = InterruptionRisk.HIGH if after_hours else (InterruptionRisk.MODERATE if incidents else InterruptionRisk.LOW)
    return SupportScenario(name, SupportUsage(owner, partner, vendor_coordination_hours=.5 if incidents else .25,
        incidents=incidents, after_hours_events=after_hours), revenue, PARTNER_RATE, direct, OWNER_VALUE,
        SupportCapacity(20, owner, 5, after_hours_capacity=False), partner_available, risk)


def print_economics(case: SupportScenario) -> None:
    e = case.economics
    margin = "N/A" if e.margin is None else f"{e.margin:.1%}"
    per_hour = "N/A" if e.contribution_per_owner_hour is None else f"${e.contribution_per_owner_hour:.2f}"
    print(f"{case.name}: revenue ${e.revenue:.2f}; partner ${e.partner_cost:.2f}; other direct ${e.other_direct_cost:.2f}; "
          f"owner {case.usage.owner_hours:.1f}h; contribution ${e.contribution:.2f}; margin {margin}; "
          f"after owner time ${e.after_owner_time:.2f}; contribution/owner-hour {per_hour}; "
          f"capacity {case.capacity.state.name}; verdict {case.verdict().name}")


def main() -> None:
    print("FICTIONAL TRAINING SCENARIO")
    print("ALL SUPPORT USAGE, PRICING, COST, AND REVENUE DATA ARE SIMULATED")
    print("\nSECTION 1 — Starting support evidence")
    print("Chapter 27 records 8 requests, 4.92 owner hours, one 0.17h goodwill request, a likely warranty defect, how-to/configuration help, vendor coordination, and one security-sensitive incident.")
    print("Chapter 28 evidence is unavailable in this checkout; incident partner hours, coordination detail, recurrence, and after-hours usage below are explicit assumptions, not observations.")
    print("Partner hours assumed 0.5/month; vendor coordination 0.5h/month; after-hours expectation: none promised.")

    profile = SupportDemandProfile(3, .25, 2.5, .5, .5, 0, .5, .25, 0, 0, 2, .1,
        {SupportWorkCategory.HOW_TO: 1, SupportWorkCategory.CONFIGURATION: .5,
         SupportWorkCategory.VENDOR_COORDINATION: .5, SupportWorkCategory.INCIDENT_COORDINATION: .25,
         SupportWorkCategory.DOCUMENTATION: .25}, "Possible launch-period spike",
        "Only a short post-launch history; monthly normalization is hypothetical")
    print("\nSECTION 2 — Support demand profile")
    print(f"Requests {profile.requests_per_month}/month; incidents {profile.incidents_per_month}; owner {profile.owner_hours_per_month}h; partner {profile.partner_hours_per_month}h; uncertainty: {profile.uncertainty}")
    print("\nSECTION 3 — Support work mix")
    for category, hours in profile.request_mix.items(): print(f"{category.name}: {hours}h")

    common_exclusions = ("new workflows", "new integrations", "major redesign or reporting",
                         "large training", "third-party fees", "work requiring discovery")
    payg = SupportPlanOption("Pay as you go", SupportRevenue(RevenueModel.PAY_AS_YOU_GO, 0), None, None,
        incident_treatment="Approved billable work unless warranty/vendor responsibility",
        vendor_coordination="Billable with approval", exclusions=common_exclusions,
        overage=OverageTreatment.BILLABLE_HOURLY, partner_cost_model=PartnerCostModel.PER_HOUR)
    light_plan = SupportPlan("Light Support", SupportEntitlement.MONTHLY_SUPPORT,
        frozenset({SupportRequestType.HOW_TO, SupportRequestType.CONFIGURATION_ASSISTANCE,
                   SupportRequestType.DOCUMENTATION_QUESTION}), 3,
        "Business-hours acknowledgement; resolution is not guaranteed", common_exclusions,
        "Reasonable coordination within owner capacity", "Not included", "Monthly; hypothetical")
    light = SupportPlanOption("Light Support", SupportRevenue(RevenueModel.MONTHLY_FLAT_FEE, 600), light_plan, 3, .5,
        "Triage and limited coordination", "Within 3-hour owner boundary", "Not included", common_exclusions,
        RolloverPolicy.NO_ROLLOVER, OverageTreatment.BILLABLE_HOURLY, PartnerCostModel.PER_HOUR)
    managed_plan = SupportPlan("Managed Support", SupportEntitlement.MONTHLY_SUPPORT,
        frozenset({SupportRequestType.HOW_TO, SupportRequestType.CONFIGURATION_ASSISTANCE,
                   SupportRequestType.ROUTINE_SUPPORT, SupportRequestType.INCIDENT,
                   SupportRequestType.DOCUMENTATION_QUESTION}), 6,
        "Business-hours prioritized coordination; resolution depends on cause", common_exclusions,
        "Included within owner capacity; partner work bounded", "Not included", "Monthly; hypothetical")
    managed = SupportPlanOption("Managed Support", SupportRevenue(RevenueModel.HYBRID, 1050), managed_plan, 6, 1,
        "Business-hours incident coordination", "Included within capacity", "Separately approved", common_exclusions,
        RolloverPolicy.NO_ROLLOVER, OverageTreatment.QUOTE_REQUIRED, PartnerCostModel.PER_HOUR)

    for number, plan in ((4, payg), (5, light), (6, managed)):
        print(f"\nSECTION {number} — Plan {chr(61+number)}: {plan.name}")
        print(f"Revenue model {plan.revenue.model.name}; hypothetical price ${plan.revenue.amount:.2f}; owner capacity {plan.included_owner_capacity}; incident: {plan.incident_treatment}; vendor: {plan.vendor_coordination}; after-hours: {plan.after_hours}; overage: {plan.overage.name}")
        print("Included:", "approval-based support" if plan.support_plan is None else ", ".join(t.name for t in plan.support_plan.included_request_types))
        print("Exclusions:", ", ".join(plan.exclusions))
        print("Customer trade-off: lower commitment for PAYG; continuity and faster routing for bounded plans. Local Works trade-off: variable revenue versus reserved, interruption-prone capacity.")

    expected = {
        "Pay as you go": scenario("Pay as you go", 500, 2.5, .5, direct=25),
        "Light Support": scenario("Light Support", 600, 2.5, .5),
        "Managed Support": scenario("Managed Support", 1050, 4.5, 1),
    }
    print("\nSECTION 7 — Expected monthly economics")
    for case in expected.values(): print_economics(case)
    print("\nSECTION 8 — Break-even")
    for plan, revenue, direct in (("PAYG",500,75),("Light",600,100),("Managed",1050,150)):
        b = SupportBreakEven(revenue, direct, OWNER_VALUE, PARTNER_RATE)
        print(f"{plan}: owner {b.owner_hours:.2f}h; partner {b.partner_hours:.2f}h; usage break-even depends on mix, not ticket count")

    stress = [
        scenario("Normal month",600,2.5,.5), scenario("Busy month",600,5,1,1),
        scenario("Vendor incident month",600,6,1.5,1), scenario("After-hours incident month",600,7,1.5,1,1,direct=125),
        scenario("Partner unavailable",600,4,1,1,partner_available=False),
        scenario("Double demand",600,10,2,2),
    ]
    for section, case in enumerate(stress, 9):
        print(f"\nSECTION {section} — {case.name}"); print_economics(case)
    print("\nSECTION 15 — Capacity")
    cap = expected["Light Support"].capacity
    print(f"Available 20h; routine {cap.planned_support_hours}h; incident reserve {cap.incident_buffer}h; usable planned {cap.usable_planned_capacity}h; utilization {cap.utilization:.1%}; {cap.state.name}")
    print("\nSECTION 16 — Customer value")
    value = SupportCustomerValue(("one known point of contact", "faster business-hours routing", "vendor coordination", "documentation continuity", "predictable base cost"), ("light documentation review",), "Needs Harbor validation", "PLAUSIBLE_NOT_PROVEN")
    print("; ".join(value.benefits), "|", value.value_state, "— low usage alone would not prove value")
    print("\nSECTION 17 — Goodwill burden")
    print("Chapter 27: 0.17 owner hour and $15 internal estimate; occasional so far, but repetition would be an unpaid plan signal.")
    print("\nSECTION 18 — Warranty burden")
    print("Likely warranty defect: 1.5 owner hours; excluded from paid usage and revenue. A trend would indicate quality, not pricing, trouble.")
    print("\nSECTION 19 — Vendor burden")
    print("Expected 0.5 owner coordination hour/month is real effort even if vendor correction is free.")
    months = [scenario(f"Month {i+1}",600,owner,partner,incidents) for i,(owner,partner,incidents) in enumerate([
        (2,.25,0),(3,.5,0),(7,1.5,1),(1,.25,0),(4,.75,1),(2,.5,0),
        (5,1,1),(2,.25,0),(3,.5,0),(8,2,2),(1,.25,0),(4,.75,1)])]
    annual = aggregate_annual(months)
    print("\nSECTION 20 — Annual simulation")
    print(f"Revenue ${annual.revenue:.2f}; direct cost ${annual.direct_cost:.2f}; owner {annual.owner_hours:.1f}h; contribution ${annual.contribution:.2f}; after owner time ${annual.owner_time_adjusted_contribution:.2f}; incidents {annual.incidents}")
    print("\nSECTION 21 — Plan comparison")
    print("PAYG avoids idle-value concerns but adds approval friction; Light is positive normally but fails several stress months; Managed buys more room yet reserves more scarce capacity. Prepaid hours remain a bounded alternative.")
    print("\nSECTION 22 — Recommendation")
    print("PAY_AS_YOU_GO_BETTER until longer demand history and Harbor's continuity value are validated; then reconsider a bounded Light plan—not unlimited support.")
    print("\nSECTION 23 — Assumption sensitivity")
    print("A Light plan becomes more attractive with stable <=3 owner hours, reliable partner coverage, proven preventive value, low after-hours demand, or a higher fair price; heavier incidents/vendor coordination favor PAYG, vendor-led support, lower scope, or no plan.")
    print("\nSECTION 24 — Interpretation")
    print("The best support model is not the one with the most recurring revenue. It is the one that creates enough customer value while preserving Local Works economics and owner capacity.")
    print("Failure lessons: $199 unlimited support with 12 owner/4 partner hours is deeply negative after owner time; $600 less $100 hides 12 owner hours; filling all 20 hours leaves no incident buffer; 'always here' prices no availability; everything included swallows project work; low usage is not customer value; absent partners break promises; 20% revenue with 60% hours exposes burden concentration.")


if __name__ == "__main__":
    main()
