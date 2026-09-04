#!/usr/bin/env python3
"""Run Chapter 32B's fictional owner-economics examination."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.capstone import BASELINE, simulate
from local_works.capstone_scenarios import (
    OwnerIncomeModel, OwnerIncomeTarget, SCENARIOS, bottleneck_evolution,
    break_even, capacity_mode_plausibility, lever_test, monte_carlo,
    operating_models, ranked_sensitivities, scenario_suite, target_result,
)


def money(value: float) -> str: return f"${value:,.0f}"


def main() -> None:
    baseline_result = simulate(BASELINE)
    income = OwnerIncomeModel().calculate(baseline_result, BASELINE)
    comparisons = scenario_suite()
    by_name = {row.scenario: row for row in comparisons}
    thresholds = break_even()
    sensitivity = ranked_sensitivities()
    mc = monte_carlo()
    models = operating_models()
    lever = lever_test()
    targets = tuple(target_result(income, OwnerIncomeTarget(value)) for value in (50_000,75_000,100_000,125_000))
    yearly = "\n".join(f"Y{y.year}: revenue={money(y.business_revenue)}; contribution={money(y.business_contribution)}; draw={money(y.owner_draw)}; hours={y.owner_hours:.0f}; draw/hour={money(y.owner_draw_per_hour)}; min/end cash={money(y.minimum_cash)}/{money(y.ending_cash)}; overload={y.overload_months}" for y in income.years)
    compact = "\n".join(f"{r.scenario:24} rev={money(r.revenue_36_months):>10} contribution={money(r.contribution_36_months):>9} draws={'/'.join(money(x) for x in r.yearly_owner_draws)} cash={money(r.ending_cash)} min={money(r.minimum_cash)} hours/wk={r.average_owner_hours_week:.1f} overload={r.overload_months} bottleneck={r.primary_bottleneck.name} target={r.target_status.name}" for r in comparisons)
    sections = [
      ("Load 32A baseline", f"Exact config object reused: {BASELINE.name}; revenue={money(baseline_result.total_revenue)}; contribution={money(baseline_result.total_contribution)}; min cash={money(baseline_result.minimum_cash)}; 32A bottleneck={baseline_result.primary_bottleneck.bottleneck.name}."),
      ("Owner compensation assumptions", f"policy={income.policy.name}; reserve={money(income.reserve_minimum)}; 50% of eligible cash capped at $10,000/month after reserve and next overhead. Simulation only; not tax/accounting advice."),
      ("Baseline owner income", yearly),
      ("Owner income stability", f"zero-draw={income.stability.months_with_zero_draw}; below $75k/12={income.stability.months_below_target}; min/max={money(income.stability.minimum_draw)}/{money(income.stability.maximum_draw)}; standard deviation={money(income.stability.standard_deviation)}; state={income.stability.state.name}. Draw/hour is not economic profit/hour."),
      ("Owner workload", f"average={by_name['BASELINE'].average_owner_hours_week:.1f}h/week; peak={by_name['BASELINE'].peak_owner_hours_week:.1f}h/week; overload={by_name['BASELINE'].overload_months} months. Sales, project, support, incident, relationship, and admin hours remain separate in each 32A month."),
      ("Owner-income targets", "\n".join(f"{money(t.target.annual_amount)}: {t.state.name} — {t.reason}" for t in targets)),
    ]
    for title in ("Conservative","Optimistic","Stress","Rapid growth","Low demand","Low price","High support burden","Cash stress","Partner failure","Customer concentration","Owner absence"):
        key=title.upper().replace(" ","_"); r=by_name[key]
        sections.append((f"{title} scenario",f"revenue={money(r.revenue_36_months)}; contribution={money(r.contribution_36_months)}; Y3 draw={money(r.yearly_owner_draws[2])}; min cash={money(r.minimum_cash)}; overload={r.overload_months}; bottleneck={r.primary_bottleneck.name}; flags={','.join(x.name for x in r.failure_flags) or 'none'}"))
    sections.extend([
      ("Scenario comparison",compact),
      ("Break-even qualified leads",f"{thresholds.qualified_leads_per_month:.2f}/month for the selected {money(thresholds.annual_target)} annual target, under current funnel and contribution assumptions."),
      ("Break-even sales/year",f"{thresholds.sales_per_year:.2f} sales/year."),
      ("Break-even project contribution",f"{money(thresholds.project_contribution)} average contribution at modeled expected sales."),
      ("Owner-hours break-even",f"{thresholds.maximum_owner_hours_per_project:.1f} hours/project at configured owner-time value."),
      ("Support-burden break-even",f"{thresholds.maximum_support_hours_per_customer_month:.1f} owner hours/customer/month before support margin is consumed."),
      ("Cash break-even",f"Estimated minimum opening cash={money(thresholds.minimum_opening_cash)}, holding modeled timing constant; this is not legal or financial advice."),
      ("Sensitivity analysis","\n".join(f"{x.assumption}: low/base/high Y3 draw={money(x.low_year3_draw)}/{money(x.base_year3_draw)}/{money(x.high_year3_draw)}; impact={money(x.absolute_impact)}" for x in sensitivity)),
      ("Sensitivity ranking","\n".join(f"{i}. {x.assumption}: {money(x.absolute_impact)} Y3 draw range" for i,x in enumerate(sensitivity[:5],1))),
      ("Monte Carlo",f"runs={mc.runs}; seed={mc.seed}; Y3 draw P10/P50/P90={money(mc.p10_year3_draw)}/{money(mc.p50_year3_draw)}/{money(mc.p90_year3_draw)}; cash nonnegative={mc.cash_nonnegative_frequency:.1%}; target achieved={mc.target_achieved_frequency:.1%}; overload={mc.overload_frequency:.1%}; working capital={mc.working_capital_frequency:.1%}; concentration={mc.concentration_frequency:.1%}."),
      ("Monte Carlo interpretation",f"{mc.interpretation} A target frequency means that share of these configured simulation draws; it does NOT mean Local Works has that real-world chance of success."),
      ("Operating-model comparison","\n".join(f"{m.model}: contribution={money(m.comparison.contribution_36_months)}; Y3 draw={money(m.comparison.yearly_owner_draws[2])}; workload={m.comparison.average_owner_hours_week:.1f}h/week; bottleneck={m.comparison.primary_bottleneck.name}" for m in models)),
      ("Side/part/full-time plausibility","\n".join(f"{k}: {v}" for k,v in capacity_mode_plausibility().items())+"\nThese are model-capacity classifications, not a personal recommendation."),
      ("Weak scenario",f"LOW_PRICE before: Y3 draw={money(lever.before.yearly_owner_draws[2])}; contribution={money(lever.before.contribution_36_months)}."),
      ("Business-design lever",f"{lever.lever.name}: {', '.join(lever.changed_assumptions)}; plausible rather than magical."),
      ("Before/after result",f"Y3 draw {money(lever.before.yearly_owner_draws[2])} → {money(lever.after.yearly_owner_draws[2])}; contribution {money(lever.before.contribution_36_months)} → {money(lever.after.contribution_36_months)}. Unchanged: {', '.join(lever.unchanged_assumptions)}."),
      ("Bottlenecks","\n".join(f"{r.scenario}: {r.primary_bottleneck.name}" for r in comparisons)),
      ("Bottleneck evolution","Baseline: "+", ".join(f"{p}={b.name}" for p,b in bottleneck_evolution(BASELINE))+"\nRapid growth: "+", ".join(f"{p}={b.name}" for p,b in bottleneck_evolution(SCENARIOS['RAPID_GROWTH']))),
      ("Evidence produced for 32C","Scenario ranges, owner draws and stability, capacity, thresholds, sensitivity ranking, simulation frequencies, model alternatives, and a bounded lever test. No final verdict, validation plan, or production requirements are produced."),
      ("Interpretation","Robust business economics depend not only on the baseline but on how the model behaves when demand, price, cost, support, cash, and owner capacity move against assumptions."),
    ])
    print("LOCAL WORKS FINAL OPERATING EXAMINATION — PART B\n\nFICTIONAL BUSINESS SIMULATION\n\nALL OWNER-INCOME, BUSINESS, CASH, AND PROBABILITY RESULTS ARE SIMULATION OUTPUTS")
    for number,(title,body) in enumerate(sections,1): print(f"\nSECTION {number} — {title}\n{body}")


if __name__ == "__main__": main()
