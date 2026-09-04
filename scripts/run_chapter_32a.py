#!/usr/bin/env python3
"""Print Chapter 32A's one fictional baseline examination."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.capstone import BASELINE, BusinessSimulationResult, simulate


def money(value: float) -> str: return f"${value:,.0f}"


def month_table(result: BusinessSimulationResult, start: int, end: int) -> str:
    header = "Mo Leads Sales Active Support Revenue Contrib Cash Hours Capacity Pipeline"
    rows = [header]
    for m in result.months[start-1:end]:
        rows.append(f"{m.month_number:02} {m.leads:5} {m.sales:5} {m.portfolio.active_projects:6} "
                    f"{m.portfolio.support_customers:7} {m.revenue.total:7.0f} {m.contribution.total:7.0f} "
                    f"{m.cash.flow.ending_cash:7.0f} {m.owner_hours:5.0f} {m.capacity_state.name:10} {m.pipeline_state.name}")
    return "\n".join(rows)


def year_line(year) -> str:
    return (f"leads={year.leads}; qualified={year.qualified_opportunities}; sales={year.sales}; "
            f"delivered={year.projects_delivered}; support-at-end={year.support_customers}; "
            f"revenue={money(year.revenue)}; contribution={money(year.contribution)}; "
            f"minimum/ending cash={money(year.minimum_cash)}/{money(year.ending_cash)}; "
            f"owner hours={year.owner_hours:.1f}; overload months={year.overload_months}; pipeline={year.pipeline_condition.name}")


def main() -> None:
    result = simulate(BASELINE); last = result.months[-1]
    peak = max(result.months, key=lambda m: m.owner_hours)
    support_hours = [m.paid_support_hours+m.warranty_hours+m.goodwill_hours for m in result.months]
    work = {name: sum(getattr(m.owner_workload.hours, name) for m in result.months) for name in
            ("sales", "audit", "discovery", "proposal", "solution_design", "project_coordination", "qa", "support", "incidents", "relationship_management", "admin")}
    sections = [
        ("Capstone purpose", "Model prospect → qualification → discovery → proposal → signed/queued delivery → stabilization → support/quiet health → expansion/referral/churn, with cash and finite owner/partner capacity."),
        ("Baseline assumptions", "\n".join(f"{a.group}: {a.name}={a.value} {a.unit} [{a.evidence.name}]" for a in BASELINE.assumptions())),
        ("Starting state", f"cash={money(BASELINE.opening_cash)}; owner={BASELINE.sustainable_owner_hours}h/month; partner={BASELINE.partner_capacity_hours}h/month; pipeline=small startup ramp; customers=0"),
        ("Months 1–12", month_table(result, 1, 12)),
        ("Year 1 summary", year_line(result.years[0])),
        ("Months 13–24", month_table(result, 13, 24)),
        ("Year 2 summary", year_line(result.years[1])),
        ("Months 25–36", month_table(result, 25, 36)),
        ("Year 3 summary", year_line(result.years[2])),
        ("36-month portfolio state", f"customers={last.portfolio.customers}; projects completed/active/queued={last.portfolio.completed_projects}/{last.portfolio.active_projects}/{last.portfolio.queued_projects}; support={last.portfolio.support_customers}; quiet={last.portfolio.quiet_customers}; incidents={sum(m.incidents for m in result.months)}; expansions={sum(m.expansions for m in result.months)}; churn={sum(m.churn for m in result.months)}"),
        ("Revenue/contribution", f"revenue={money(result.total_revenue)}; contribution={money(result.total_contribution)}; pipeline excluded; these are distinct measures"),
        ("Cash", f"minimum={money(result.minimum_cash)}; ending={money(result.ending_cash)}; cash failures={','.join(x.name for x in result.failure_reasons) or 'none'}; working-capital flag={result.working_capital_required}"),
        ("Owner workload", f"average={result.owner_hours/36:.1f}h; peak=M{peak.month_number:02} {peak.owner_hours:.1f}h; overload months={result.overload_months}; work mix=" + ", ".join(f"{k}={v:.0f}" for k,v in work.items())),
        ("Pipeline behavior", f"final={last.pipeline_state.name}; weak months={sum(m.pipeline_state.name=='WEAK' for m in result.months)}; delivery/queue constraints can defer progression rather than creating unlimited selling"),
        ("Support-tail behavior", f"monthly total support demand grew from {support_hours[0]:.1f}h to {support_hours[-1]:.1f}h; warranty, paid support, and goodwill remain separate"),
        ("Concentration", f"largest revenue/contribution/owner-hour/support shares={last.concentration.revenue:.0%}/{last.concentration.contribution:.0%}/{last.concentration.owner_hours:.0%}/{last.concentration.support:.0%}; primary-partner={last.concentration.partner:.0%}; shared-vendor={last.concentration.vendor:.0%}"),
        ("Owner absence", f"M{BASELINE.absence_month}: available capacity reduced by {BASELINE.absence_hours:.0f}h; capacity={result.months[BASELINE.absence_month-1].capacity_state.name}; work was not assigned to absent hours and deferral/queue effects remain visible"),
        ("Baseline health snapshot", "\n".join(f"{k}: {v.name}" for k,v in result.health.items())),
        ("Primary baseline bottleneck", f"{result.primary_bottleneck.bottleneck.name}: {result.primary_bottleneck.evidence}"),
        ("What remains for 32B/32C", "32B: scenario analysis, owner income, break-even, sensitivity, and Monte Carlo. 32C: final verdict, real-world validation, and production requirements. None is performed here."),
    ]
    print("LOCAL WORKS FINAL OPERATING EXAMINATION — PART A")
    print("FICTIONAL BUSINESS SIMULATION")
    print("NO REAL CUSTOMER, CONVERSION, REVENUE, PROJECT, SUPPORT, OR OWNER-INCOME RESULT IS BEING CLAIMED")
    for number, (title, body) in enumerate(sections, 1): print(f"\nSECTION {number} — {title}\n{body}")


if __name__ == "__main__": main()
