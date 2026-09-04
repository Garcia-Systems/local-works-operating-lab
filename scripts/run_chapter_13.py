"""Run Chapter 13's deterministic, fictional solution-economics exercise."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.economics import (BurdenCategory, BurdenComponent, EconomicEstimate,
                                  EconomicInput, EvidenceStatus as E)
from local_works.solution_economics import (BenefitType, CostCategory, EconomicAssumption,
    EconomicDecision, RecoverableValueComponent, SolutionCost, SolutionEconomics,
    ValueCategory, compare_incrementally)


def assumption(name: str, value: float) -> EconomicAssumption:
    return EconomicAssumption(name, value, E.HYPOTHETICAL, "fictional Chapter 13 assumption")


def harbor_burden() -> BurdenComponent:
    source = EconomicInput("annual direct labor burden", 2450, "dollars/year", E.ESTIMATED,
                           "reconstructed Chapter 10 baseline; loaded rates hypothetical")
    return BurdenComponent("harbor-labor", BurdenCategory.LABOR, "Membership-request labor",
        EconomicEstimate(2450, E.ESTIMATED, (source,), "Chapter 10 baseline labor"),
        includes="front-desk and manager active labor")


def model(name: str, fraction: float, adoption: float, realization: float,
          implementation: float, recurring: float, new_work: float,
          decision: EconomicDecision) -> SolutionEconomics:
    value = RecoverableValueComponent(harbor_burden(), ValueCategory.LABOR_CAPACITY,
        BenefitType.FREED_CAPACITY, assumption("recoverable fraction", fraction),
        assumption("adoption", adoption), assumption("realization", realization),
        "Identity and eligibility checks, unusual memberships, disputes, and approvals remain.",
        freed_hours=2450 / 24 * fraction * adoption * realization)
    return SolutionEconomics(name, 2450, [value], [
        SolutionCost("implementation", CostCategory.OTHER, implementation, E.HYPOTHETICAL,
                     "preliminary training estimate; not a quote"),
        SolutionCost("annual platform/support", CostCategory.SUPPORT_MAINTENANCE, recurring,
                     E.HYPOTHETICAL, "preliminary training estimate", recurring=True),
    ], new_work, decision=decision,
       major_unknowns=["actual request volume and handling time", "platform capability",
                       "adoption, exception rate, and delivery estimate"])


def show(item: SolutionEconomics) -> None:
    value = item.components[0]
    payback = "NONE / NOT ACHIEVED" if item.payback_months is None else f"{item.payback_months:.1f} months"
    print(f"{item.alternative}: burden addressed $2,450; recoverable {value.recoverable_fraction.value:.0%}; "
          f"adoption {value.adoption_rate.value:.0%}; realization {value.realization_factor.value:.0%}")
    print(f"  Gross recoverable capacity value ${item.annual_gross_value:,.0f}; cash savings NOT ESTABLISHED; "
          f"new work ${item.annual_new_operating_burden:,.0f}; implementation ${item.implementation_cost:,.0f}; "
          f"recurring ${item.annual_recurring_cost:,.0f}; annual net ${item.annual_net_benefit:,.0f}; payback {payback}")
    print(f"  1/2/3-year cumulative: " + " / ".join(f"${item.cumulative_value(y):,.0f}" for y in (1, 2, 3)))
    print(f"  Evidence HYPOTHETICAL; decision {item.decision.name}; remaining: {value.remaining_work}")


def main() -> None:
    print("CHAPTER 13 — SOLUTION ECONOMICS\nFICTIONAL TRAINING SCENARIO\nNOT A REAL CUSTOMER ROI ANALYSIS")
    configure = model("CONFIGURE", .55, .75, .80, 1000, 0, 150, EconomicDecision.ECONOMICALLY_PLAUSIBLE)
    integrate = model("INTEGRATE/AUTOMATE", .75, .75, .80, 4500, 600, 300, EconomicDecision.MARGINAL)
    custom = model("CUSTOM BUILD", .90, .80, .85, 15000, 2400, 600, EconomicDecision.ECONOMICALLY_UNATTRACTIVE)
    print("\nSECTION 1 — Current burden\nChapter 10 baseline: $2,450/year estimated labor capacity burden. Revenue, retention, refunds, and rework remain UNKNOWN.")
    print("\nSECTION 2 — Candidate solutions\nCONFIGURE; INTEGRATE/AUTOMATE; CUSTOM BUILD; LEAVE ALONE (from the Chapter 12 hierarchy).")
    print("\nSECTION 3 — Recoverable value")
    for item in (configure, integrate, custom):
        value = item.components[0]
        print(f"{item.alternative}: {value.recoverable_fraction.value:.0%} × {value.adoption_rate.value:.0%} adoption × {value.realization_factor.value:.0%} realization; necessary review remains; new operating work included; HYPOTHETICAL.")
    print("\nSECTION 4 — Configuration economics"); show(configure)
    print("\nSECTION 5 — Integration/automation economics"); show(integrate)
    print("\nSECTION 6 — Custom-build economics"); show(custom)
    print("\nSECTION 7 — Leave alone\nImplementation cost: $0\nRecovered burden: $0\nCurrent $2,450 burden continues. Decision: LEAVE_ALONE is an available outcome.")
    print("\nSECTION 8 — Payback")
    for item in (configure, integrate, custom):
        print(f"{item.alternative}: " + (f"{item.payback_months:.1f} months" if item.payback_months else "NONE / NOT ACHIEVED"))
    print("\nSECTION 9 — 1/2/3-year economics")
    for item in (configure, integrate, custom): show(item)
    print("\nSECTION 10 — Incremental economics")
    for simpler, complex_item in ((configure, integrate), (configure, custom)):
        delta = compare_incrementally(simpler, complex_item)
        print(f"{delta.more_complex} vs {delta.simpler}: additional implementation ${delta.additional_implementation_cost:,.0f}; additional annual net benefit ${delta.additional_annual_net_benefit:,.0f}. Is that increment worth added cost and risk?")
    print("\nSECTION 11 — Low/base/high")
    for label, fraction, adoption, realization, cost in (("LOW", .35, .60, .65, 1300), ("BASELINE", .55, .75, .80, 1000), ("HIGH", .70, .85, .90, 800)):
        scenario = model(label, fraction, adoption, realization, cost, 0, 150, EconomicDecision.MORE_EVIDENCE_REQUIRED)
        print(f"CONFIGURE {label}: annual net ${scenario.annual_net_benefit:,.0f}; implementation ${cost:,.0f}; payback " + (f"{scenario.payback_months:.1f} months" if scenario.payback_months else "NONE"))
    print("\nSECTION 12 — Evidence quality\nMeasured: none.\nEstimated: Chapter 10 current labor burden.\nHypothetical: recovery, adoption, realization, new work, implementation and recurring costs.\nUnknown: revenue, retention, cash payroll savings, capability, exceptions, and firm delivery costs.")
    print("\nSECTION 13 — Current economic decision")
    for item in (configure, integrate, custom): print(f"{item.alternative}: {item.decision.name}")
    print("Economically attractive or plausible does not mean PROJECT APPROVED and creates no proposal. Configuration is the simplest currently plausible direction, conditional on evidence.")
    print("\nSECTION 14 — What evidence matters most?\nObserved request volume and time; workflow adoption; actual time reduction and exception work; platform capability; implementation and recurring estimates. Any could change the decision.")
    print("\nTEACHING EXAMPLES")
    print("BIG PROBLEM, BAD SOLUTION: $100,000 burden; $300,000 implementation; $60,000 maintenance; $40,000 recoverable value => negative annual net benefit. BIG PROBLEM ≠ GOOD PROJECT.")
    print("SMALLER PROBLEM, GREAT CONFIGURATION: $8,000 burden; $1,000 setup; minimal recurring cost; $5,000 recoverable value. SMALLER PROJECT can be BETTER BUSINESS.")
    print("FREED CAPACITY: 200 hours/year; indicative labor capacity value $5,000/year; cash payroll savings NOT ESTABLISHED.")
    print("SUNK COST: prior investigation spending does not justify future spending; compare future expected cost with future expected value.")


if __name__ == "__main__":
    main()
