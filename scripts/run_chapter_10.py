"""Run Chapter 10's deterministic, fictional problem-economics exercise."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.economics import (  # noqa: E402
    EconomicInput, EvidenceStatus as E, Frequency, FrequencyUnit as U,
    LaborRole, Scenario, rework_burden, scenario_labor_burdens,
)


def value(name: str, amount: float | None, unit: str, evidence: E, source: str) -> EconomicInput:
    return EconomicInput(name, amount, unit, evidence, source)


def frequency(per_week: float, weeks: float = 50) -> Frequency:
    return Frequency(value("requests", per_week, "requests/week", E.ESTIMATED, "manager estimate"), U.PER_WEEK,
                     value("operating weeks", weeks, "weeks/year", E.HYPOTHETICAL, "training assumption"))


def role(name: str, minutes: float, cost: float, involvement: float = 1) -> LaborRole:
    return LaborRole(name,
        value("handling time", minutes, "minutes/event", E.ESTIMATED, "employee estimate"),
        value("loaded labor cost", cost, "dollars/hour", E.HYPOTHETICAL, "training assumption; not wage data"),
        value("involvement", involvement, "proportion", E.ESTIMATED, "manager estimate"))


def main() -> None:
    print("CHAPTER 10 — THE ECONOMICS BEHIND THE PAIN\nFICTIONAL TRAINING ANALYSIS — NOT CUSTOMER RESULTS")
    print("\nSECTION 1 — Economic vocabulary")
    print("Frequency annualizes events. Labor burden values active work. Rework burden values correction work.\nHard cost is supported and monetized; soft burden is real but non-monetized. Unknown potential impact remains UNKNOWN. Annual burden describes the current state, not solution value.")
    example_frequency = frequency(20)
    front_desk = role("Front desk", 8, 24)
    basic = front_desk.annual_burden(example_frequency)
    print("\nSECTION 2 — One workflow calculation")
    print("20 requests/week [MANAGER ESTIMATE]\n× 50 weeks [HYPOTHETICAL TRAINING ASSUMPTION]\n= 1,000 requests/year\n\n1,000 × 8 minutes [EMPLOYEE ESTIMATE]\n= 8,000 minutes\n\n8,000 / 60\n= 133.33 labor hours\n\n133.33 × $24 [HYPOTHETICAL LOADED COST]\n= $3,200 annual estimated labor burden")
    print(f"Model result: ${basic.annual_amount:,.2f}; provenance: {basic.evidence.name}. Loaded cost may include wage, payroll taxes, benefits, and other employer costs; there is no universal formula here.")
    manager = role("Manager", 3, 36, .25).annual_burden(example_frequency)
    print("\nSECTION 3 — Multiple roles")
    print(f"Manager: 1,000 × 25% × 3/60 × $36 = ${manager.annual_amount:,.2f}. Incremental, not averaged with front-desk work. Combined: ${basic.annual_amount + manager.annual_amount:,.2f}.")
    rework = rework_burden(example_frequency,
        value("correction rate", .05, "proportion", E.HYPOTHETICAL, "training assumption"),
        value("correction time", 15, "minutes", E.HYPOTHETICAL, "training assumption"),
        value("loaded cost", 24, "dollars/hour", E.HYPOTHETICAL, "training assumption"))
    print("\nSECTION 4 — Rework")
    print(f"1,000 × 5% × 15/60 × $24 = ${rework.annual_amount:,.2f} hypothetical annual rework. Do not reuse this assumption for Harbor Fitness.")
    print("\nSECTION 5 — Waiting")
    print("A 2-day approval wait does NOT equal 48 labor hours. Waiting is elapsed friction; only separately evidenced consequences may be monetized.")
    print("\nSECTION 6 — Unknown revenue impact")
    print("Potential lost revenue: UNKNOWN\nReason: No evidence connects the workflow to lost memberships or revenue. Retention impact is likewise UNKNOWN, not $0.")

    frequencies = {Scenario.LOW: frequency(15), Scenario.BASELINE: frequency(20), Scenario.HIGH: frequency(25)}
    roles = {
        Scenario.LOW: (role("Front desk", 4, 24), role("Manager", 2, 36, .15)),
        Scenario.BASELINE: (role("Front desk", 5, 24), role("Manager", 3, 36, .25)),
        Scenario.HIGH: (role("Front desk", 6, 24), role("Manager", 5, 36, .35)),
    }
    scenarios = scenario_labor_burdens(frequencies, roles)
    print("\nSECTION 7 — Low/base/high")
    for scenario, amount in scenarios.items(): print(f"{scenario.name}: ${amount:,.2f}")
    print("Sensitivity analysis, not proof.")
    tiny = 2 * 10 / 60 * 30
    print("\nSECTION 8 — Tiny problem")
    print(f"2 times/year × 10 minutes ÷ 60 × $30 = ${tiny:,.2f}/year. Technically fixable; economically trivial: LEAVE IT ALONE.")
    larger = 500 * 12 * 6 / 60 * 28
    print("\nSECTION 9 — Larger problem")
    print(f"Home-services re-entry: 500/month × 12 × 6 minutes ÷ 60 × $28 = ${larger:,.2f}/year (all hypothetical). It deserves economic attention, not an automatic software recommendation.")
    print("\nSECTION 10 — Harbor Fitness")
    print(f"Monetized: estimated/hypothetical direct front-desk and manager labor; baseline ${scenarios[Scenario.BASELINE]:,.2f}/year (low ${scenarios[Scenario.LOW]:,.2f}; high ${scenarios[Scenario.HIGH]:,.2f}).")
    print("Non-monetized: member effort, repeated information, employee frustration, approval waiting.\nUnknown: correction/rework, lost revenue, retention, refunds/credits, and financial effect of delay.\nDecision: MORE_EVIDENCE_REQUIRED. The direct burden may be modest; no project is recommended.")
    print("\nSECTION 11 — Interpretation")
    for question in ("Which burden is actually supported?", "Which numbers are estimates?", "Which are hypothetical?", "What remains unknown?", "Which potential impacts should NOT be monetized yet?", "Is known burden large enough to justify continuing analysis?", "What evidence would most improve confidence?"):
        print(f"- {question}")
    print("Next evidence: request counts, time observation, manager-escalation logs, correction records, and documented cancellations/refunds.\nCURRENT BURDEN IS NOT RECOVERABLE VALUE. No solution value or ROI has been calculated.")


if __name__ == "__main__":
    main()
