#!/usr/bin/env python3
"""Print Chapter 32C's final, explicitly fictional examination."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.capstone import assess_final_business


def money(value: float) -> str: return f"${value:,.0f}"


def main() -> None:
    a = assess_final_business(); base = next(x for x in a.scenarios if x.scenario == "BASELINE")
    sections = [
      ("Load final simulation evidence", f"32A baseline object reused: revenue={money(a.baseline.total_revenue)}, contribution={money(a.baseline.total_contribution)}. 32B scenarios={len(a.scenarios)}, owner income years={len(a.owner_income.years)}, sensitivities={len(a.sensitivities)}, Monte Carlo runs={a.monte_carlo.runs}, operating models={len(a.operating_models)}."),
      ("Business health scorecard", "\n".join(f"{x.dimension}: {x.status.name} — {x.evidence} Risk: {x.main_risk}" for x in a.scorecard.dimensions)),
      ("Evidence quality", f"{a.evidence_quality.name}. Passing means coherent under tested assumptions; it does not prove customers buy, partners quote modeled costs, support matches assumptions, income occurs, or the business is proven."),
      ("Primary bottleneck", f"{a.primary_bottleneck.bottleneck.name}: {a.primary_bottleneck.evidence}"),
      ("Bottleneck evolution", ", ".join(f"{period}={b.name}" for period,b in a.bottleneck_evolution)),
      ("Most sensitive assumptions", "\n".join(f"{i}. {x.assumption}: Y3 draw range {money(x.absolute_impact)}" for i,x in enumerate(a.sensitivities[:5],1))),
      ("Owner-income conclusion", "\n".join(f"Year {y.year}: draw={money(y.owner_draw)}, hours={y.owner_hours:.0f}, min cash={money(y.minimum_cash)}, overload={y.overload_months}" for y in a.owner_income.years)+f"\nStability={a.owner_income.stability.state.name}; quality={a.owner_income_quality.name}; baseline average/peak={base.average_owner_hours_week:.1f}/{base.peak_owner_hours_week:.1f} hours/week."),
      ("Operating-model conclusion", f"{a.operating_model_verdict.name}; plausible as a bounded side practice, not proven full-time employment."),
      ("Conditions for success", "\n".join(f"- {x.condition} ({x.evidence}; lever: {x.lever})" for x in a.success_conditions)),
      ("Conditions for failure", "\n".join(f"- {x.condition} ({x.evidence}; lever: {x.lever})" for x in a.failure_conditions)),
      ("Final business verdict", f"Primary: {a.primary_verdict.name}\nQualifiers:\n"+"\n".join(f"- {x}" for x in a.qualifiers)+f"\nRationale: {a.rationale}"),
      ("Evidence gaps", "\n".join(f"{i}. [{g.validation_priority.name}] {g.question} — {g.sensitivity}" for i,g in enumerate(a.evidence_gaps,1))),
      ("Validation priorities", "\n".join(f"{g.validation_priority.name}: {g.validation_method}" for g in a.evidence_gaps)),
    ]
    for i in range(3):
        e=a.experiments[i]; sections.append((f"Real-world experiment {i+1}",f"Question: {e.question}\nAssumption: {e.assumption}\nExperiment: {e.experiment}\nScope: {e.sample_size_or_scope}\nEvidence: {e.evidence_to_collect}\nSuccess: {e.success_signal}\nFailure: {e.failure_signal}\nDecision: {e.decision_after}"))
    sections += [
      ("First-real-customer validation","Test the real problem, willingness to pay, simplest path, partner estimate, owner discovery/project hours, quality, payment behavior, and support tail in a small bounded, low-risk, clear-acceptance engagement."),
      ("Production software verdict",f"{a.software_verdict.name}, separate from {a.primary_verdict.name}."),
      ("First-real-customer minimum tooling","YES, without a custom portal: a contact path, audit and discovery notes, proposal, existing project tracker, shared files, decision/change logs, calendar, and bounded support email."),
      ("Local Works dogfood assessment","\n".join(f"{c.capability}: {c.approach.name}" for c in a.capabilities)),
      ("Public website readiness","A small truthful site may explain positioning, process, audit, capabilities and contact. No fake logos, testimonials, outcomes, partners, or Harbor Fitness case study."),
      ("Customer portal readiness","DO_NOT_BUILD_YET; documents, email, calendar, and configured project software are adequate for first validation."),
      ("Back-office readiness","READY_FOR_MANUAL_CUSTOMER_OPERATION with configured lead, project, document, and cash records."),
      ("Delivery-partner collaboration readiness","READY_FOR_MANUAL_CUSTOMER_OPERATION using comparable estimate requests, shared milestones, decisions, QA, escalation, and documentation."),
      ("Production requirements priorities","\n".join(f"{p}: "+", ".join(c.capability for c in a.capabilities if c.priority.name==p) for p in ("MUST_FOR_FIRST_REAL_CUSTOMER","SHOULD_SOON","LATER","ONLY_IF_REPEATED","DO_NOT_BUILD_YET"))),
      ("What the lab proved","The lifecycle can be modeled coherently; major economic/capacity risks can be surfaced; assumptions can be scenario-tested; capability needs can be derived from modeled operations."),
      ("What the lab did not prove","Real demand, willingness to pay, close rate, partner price, implementation effort, support/incident burden, retention/referrals, payment timing, or owner income."),
      ("Next evidence-producing action","Run a small batch of public, evidence-only Digital Friction Audits and record qualified response; do not build the whole website."),
      ("Final interpretation","Simulation failure identifies where, why, at which stage, and which lever to test before spending real cash. Local Works should earn the right to build software for customers, and it should earn the right to build software for itself."),
    ]
    print("LOCAL WORKS FINAL OPERATING EXAMINATION — PART C\n\nFINAL BUSINESS ASSESSMENT\n\nFICTIONAL SIMULATION ONLY\n\nNO REAL CUSTOMER, REVENUE, CONVERSION, OWNER-INCOME, OR CASE-STUDY RESULT IS BEING CLAIMED")
    for i,(title,body) in enumerate(sections,1): print(f"\nSECTION {i} — {title}\n{body}")

if __name__ == "__main__": main()
