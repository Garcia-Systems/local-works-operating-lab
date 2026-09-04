#!/usr/bin/env python3
"""Run Chapter 31B's deterministic fictional portfolio exercise."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.portfolio import WorkCategory
from local_works.portfolio_simulation import *
from scripts.run_chapter_31a import build_portfolio


def money(value: float) -> str: return f"${value:,.0f}"


def summary(result: ScenarioResult) -> str:
    return (f"{result.name}: revenue={money(result.revenue)}, contribution={money(result.contribution)}, "
            f"ending/minimum cash={money(result.ending_cash)}/{money(result.minimum_cash)}, "
            f"exposure={money(result.maximum_cash_exposure)}, owner hours={result.owner_hours:.0f}, "
            f"overload months={result.overload_months}, starts/completions={result.projects_started}/{result.projects_completed}, "
            f"support customers={result.support_customers}, incidents={result.incidents}, "
            f"pipeline={result.pipeline_state.name}, verdict={result.verdict.name}")


def main() -> None:
    foundation = build_portfolio()
    results = [simulate(c) for c in (BASELINE, CONSERVATIVE, GROWTH, STRESS)]
    base, conservative, growth, stress = results
    sample = base.periods[2]; stress_month = stress.periods[6]
    ar = stress.periods[2].cash_flow.accounts_receivable[0]
    sections = [
        ("Chapter 31A foundation loaded", f"customers={len(foundation.customers)}; work inventory={len(foundation.work_items)}; owner={foundation.owner_capacity.total_working_hours}h/week; delivery slots={foundation.delivery_capacity.delivery_slots}; incident reserve={foundation.owner_capacity.incident_reserve_hours}h"),
        ("Portfolio financial assumptions", f"opening cash={money(BASELINE.opening_cash)}; customer deposit day 20; partner deposit day 2; monthly overhead=$2,400; funds are finite"),
        ("Revenue mix", f"{sample.month}: project={money(sample.revenue.project)}, support={money(sample.revenue.support)}, expansion={money(sample.revenue.expansion)}, total={money(sample.revenue.total)}; pipeline is excluded"),
        ("Contribution mix", f"project={money(sample.contribution.project)}, support={money(sample.contribution.support)}, incident burden={money(sample.contribution.incident_warranty_burden)}, total={money(sample.contribution.total)}"),
        ("Cash timing", f"customer cash arrives after partner commitment; inflow={money(sample.cash_flow.inflow_total)}, outflow={money(sample.cash_flow.outflow_total)}, ending={money(sample.cash_flow.ending_cash)}"),
        ("Accounts receivable", f"{ar.customer}: {money(ar.amount_due)}; status={ar.status.name}; risk={ar.risk}; no invoice is issued"),
        ("Maximum cash exposure", f"baseline maximum={money(base.maximum_cash_exposure)}; this is peak funding before corresponding receipts/coverage"),
        ("Pipeline coverage", f"baseline final={base.pipeline_state.name}; conservative final={conservative.pipeline_state.name}; pipeline never becomes revenue until a sale"),
        ("Project-start gating", f"cash={gate_project_start(owner_hours_needed=8, owner_hours_available=20, partner_hours_needed=20, partner_hours_available=30, required_cash=9000, cash_above_buffer=4000)}; queued work is visible"),
        ("Support-tail accumulation", f"baseline support customers {base.periods[0].support_customers}->{base.support_customers}; owner support {base.periods[0].owner_hours.support:.0f}h->{base.periods[-1].owner_hours.support:.0f}h"),
        ("Harbor incident collision", f"{foundation.prioritized_work()[0].work_id} remains first; severe Harbor incident preempts routine support and launch work, preserving Chapter 31A priority logic"),
        ("Marginal new-deal decision", str(marginal_deal_test())),
        ("Cash-constrained project decision", str(cash_constrained_deal_test()) + " — PROFIT DOES NOT EQUAL LIQUIDITY"),
        ("Customer-concentration decision", str(concentration_deal_test())),
        ("Owner-absence effect", "three business days: project coordination delayed; support degraded; sales follow-up deferred; customer communication delegated"),
        ("Baseline 12-month simulation", "\n".join(f"{p.month}: customers={p.customers} active/queued={p.active_projects}/{p.queued_projects} support={p.support_customers} revenue={money(p.revenue.total)} contribution={money(p.contribution.total)} cash={money(p.cash_flow.ending_cash)} hours={p.owner_hours.total:.0f}/{p.available_owner_hours:.0f} capacity={p.capacity_state.name} pipeline={p.pipeline_state.name}" for p in base.periods)),
        ("Baseline annual result", summary(base)),
        ("Conservative scenario", summary(conservative) + "; late receipt and reduced selling produce a pipeline cliff"),
        ("Growth scenario", summary(growth) + "; revenue rises while queue, support tail, owner overload, and quality risk worsen"),
        ("Stress scenario", summary(stress) + "; late cash, two incidents, owner absence, and partner bottleneck collide"),
        ("Scenario comparison", "\n".join(summary(r) for r in results)),
        ("Portfolio health", "\n".join(f"{k}: {v.name}" for k,v in stress.health.items())),
        ("Weekly operating review", weekly_review(stress_month, stress=True)),
        ("Monthly business review", monthly_review(stress_month)),
        ("Portfolio decisions", "accept bounded work; queue excess demand; defer unsafe starts; decline unsupported work; protect capacity; protect cash; adjust marketing before a cliff; qualify backup partner"),
        ("Final Chapter 31 verdict", f"baseline={base.verdict.name}; stress={stress.verdict.name}; bottlenecks=owner/support/primary partner; highest risks=cash timing, shared vendor, pipeline cliff. This is a portfolio verdict, not Chapter 32's owner-income or final-business verdict."),
        ("Production-system discoveries", "cash timing vs profitability; capacity-and-cash start checks; support-load forecast; pipeline trend; future-period overload; multi-dimensional concentration; scenario planning; operating-period snapshots"),
        ("Interpretation", "A Local Works portfolio is healthy only when sales, delivery, support, cash, partners, and owner capacity remain coordinated over time. A snapshot of profitable customers is not enough."),
    ]
    print("FICTIONAL TRAINING SCENARIO")
    print("ALL CUSTOMERS, REVENUE, COSTS, CASH FLOWS, AND WORKLOADS ARE SIMULATED")
    for number, (title, body) in enumerate(sections, 1):
        print(f"\nSECTION {number} — {title}\n{body}")


if __name__ == "__main__": main()
