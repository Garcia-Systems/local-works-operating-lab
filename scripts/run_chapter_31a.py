#!/usr/bin/env python3
"""Run Chapter 31A's one-week fictional portfolio exercise."""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.portfolio import *
from local_works.project_economics import PaymentRecord, PaymentStatus
from local_works.relationships import RelationshipStatus
from local_works.support import (IncidentSeverity, SupportEntitlement, SupportPlan,
                                 SupportPlanStatus, SupportRequestType)


def build_portfolio() -> CustomerPortfolio:
    harbor_plan = SupportPlan("Bounded PAYG", SupportEntitlement.LIMITED_SUPPORT,
        frozenset({SupportRequestType.ROUTINE_SUPPORT, SupportRequestType.INCIDENT}), 4,
        status=SupportPlanStatus.ACTIVE_SIMULATED)
    customers = [
        PortfolioCustomer("Harbor Fitness", LifecycleStage.EXPANSION, RelationshipStatus.SUPPORTED,
            support_arrangement=harbor_plan, open_incidents=(IncidentSeverity.SEVERE,),
            expansion_opportunities=("cancellation workflow discovery",),
            payment_status=PaymentRecord(600, PaymentStatus.NOT_DUE, "monthly support"),
            expected_owner_hours=9, delivery_partner="Blue Heron", vendor="MemberCloud",
            next_action="Stabilize incident before expansion", risks=("shared vendor outage",),
            booked_revenue=12600, contribution=5400, support_burden_hours=6),
        PortfolioCustomer("James River Kitchen", LifecycleStage.DISCOVERY,
            expected_owner_hours=5, next_action="Complete workflow discovery", risks=("authority unconfirmed",)),
        PortfolioCustomer("Tidewater Home Services", LifecycleStage.ACTIVE_DELIVERY,
            active_project={"source": "Chapter 21-style project record"}, expected_owner_hours=11,
            delivery_partner="Blue Heron", vendor="FlowDesk", next_action="QA milestone",
            risks=("partner capacity",), booked_revenue=18000, contribution=6500,
            receivables=6000, project_start_state=ProjectStartState.START_AUTHORIZED),
        PortfolioCustomer("Colonial Professional Group", LifecycleStage.SUPPORT,
            relationship_status=RelationshipStatus.SUPPORTED, support_arrangement=harbor_plan,
            expected_owner_hours=3, vendor="MemberCloud", next_action="Routine configuration reply",
            booked_revenue=4800, contribution=2900, support_burden_hours=3, receivables=600),
        PortfolioCustomer("Peninsula Events", LifecycleStage.AUDIT, expected_owner_hours=2,
            next_action="Review audit evidence"),
        PortfolioCustomer("Old Dominion Dental", LifecycleStage.SIGNED, expected_owner_hours=7,
            delivery_partner="Blue Heron", vendor="ClinicStack", next_action="Hold in delivery queue",
            booked_revenue=14000, contribution=6000, receivables=7000,
            project_start_state=ProjectStartState.QUEUED, risks=("signed but no available start slot",)),
    ]
    work = [
        PortfolioWorkItem("HF-INC", "Harbor Fitness", WorkCategory.INCIDENT, WorkPriority.CRITICAL, WorkStatus.IN_PROGRESS, 6, 4, business_impact="member workflow unavailable", dependency_blocking=True),
        PortfolioWorkItem("THS-QA", "Tidewater Home Services", WorkCategory.QA, WorkPriority.HIGH, WorkStatus.READY, 7, 10, customer_commitment=True),
        PortfolioWorkItem("CPG-SUP", "Colonial Professional Group", WorkCategory.SUPPORT, WorkPriority.NORMAL, WorkStatus.READY, 3, business_impact="routine request"),
        PortfolioWorkItem("JRK-DISC", "James River Kitchen", WorkCategory.DISCOVERY, WorkPriority.NORMAL, WorkStatus.READY, 5),
        PortfolioWorkItem("PE-AUDIT", "Peninsula Events", WorkCategory.AUDIT, WorkPriority.LOW, WorkStatus.READY, 2),
        PortfolioWorkItem("ODD-START", "Old Dominion Dental", WorkCategory.PROJECT_MANAGEMENT, WorkPriority.NORMAL, WorkStatus.BACKLOG, 7, 12, customer_commitment=True),
        PortfolioWorkItem("HF-COLLECT", "Harbor Fitness", WorkCategory.COMMERCIAL_COLLECTION, WorkPriority.NORMAL, WorkStatus.READY, 1, cash_impact=600),
        PortfolioWorkItem("MKT", None, WorkCategory.MARKETING, WorkPriority.LOW, WorkStatus.READY, 3),
    ]
    return CustomerPortfolio(
        PortfolioPeriod("Fictional operating week", date(2026, 9, 7), date(2026, 9, 11)), customers, work,
        OwnerCapacity(40, {"sales": 4, "marketing": 3, "discovery": 5, "solution_design": 2,
            "delivery_coordination": 11, "qa": 7, "support": 4, "relationship_management": 2,
            "administration": 2, "buffer": 0}, incident_reserve_hours=4, context_switch_hours=3),
        DeliveryCapacity(24, 26, 11, specialist_available_hours=4, delivery_slots=1, starts_requested=2,
            risk="One partner carries three relationships"),
        SupportCapacity(10, 5, 4, partner_support_hours=4, vendor_coordination_hours=2),
        PipelineCoverage(3, 2, 1, 1, {"James River Kitchen": "late September"}, 27000, 12),
        [PortfolioRisk("MemberCloud outage affects two customers", ("Harbor Fitness", "Colonial Professional Group"), WorkPriority.HIGH, PortfolioDecision.PROTECT_INCIDENT_RESERVE)]
    )


def main() -> None:
    p = build_portfolio(); c = p.concentration()
    start_conflict = capacity_conflict("two starts", [w for w in p.work_items if w.work_id in {"THS-QA", "ODD-START"}], 10,
        (PortfolioDecision.DELAY_KICKOFF, PortfolioDecision.RESEQUENCE), "One delivery slot cannot absorb two commitments.")
    sections = [
        ("Portfolio starting state", f"{len(p.customers)} fictional organizations; booked revenue ${p.booked_revenue:,.0f}; pipeline remains separate."),
        ("Customer lifecycle states", "; ".join(f"{x.name}: {x.lifecycle_stage.name}" for x in p.customers)),
        ("Unified work inventory", "; ".join(f"{w.work_id}/{w.category.name}/{w.priority.name}" for w in p.prioritized_work())),
        ("Owner capacity", f"{p.owner_capacity.total_working_hours} total hours; {p.owner_capacity.customer_delivery_hours} customer-delivery hours; {p.owner_capacity.context_switch_hours} context switching; {p.owner_capacity.state.name}."),
        ("Delivery capacity", f"{p.delivery_capacity.committed_hours}/{p.delivery_capacity.partner_available_hours} partner hours; {p.delivery_capacity.starts_requested}/{p.delivery_capacity.delivery_slots} starts/slots; {p.delivery_capacity.state.name}."),
        ("Support capacity", f"Demand {p.support_capacity.demand_hours} vs {p.support_capacity.owner_available_hours} hours; shortfall {p.support_capacity.shortfall_hours}."),
        ("Pipeline", f"{p.pipeline.leads} leads, {p.pipeline.qualified_opportunities} qualified, {p.pipeline.discoveries} discovery, {p.pipeline.proposals} proposal; potential ${p.potential_revenue:,.0f}, not booked revenue."),
        ("Concentration", f"Revenue leader {c.largest_share(c.revenue):.0%}; owner-hour leader {c.largest_share(c.owner_hours):.0%}; support leader {c.largest_share(c.support_burden):.0%}; shared vendor: {', '.join(c.vendor_correlated_risks)}."),
        ("Capacity conflict", f"{start_conflict.name}: {start_conflict.shortfall_hours} owner-hour shortfall; {', '.join(d.name for d in start_conflict.decisions)}."),
        ("Harbor incident collision", "CRITICAL Harbor incident outranks routine large-customer work. Protect incident reserve and resequence QA without confusing noise with impact."),
        ("New-deal collision", "Old Dominion is profitable and SIGNED but remains QUEUED. DELAY_KICKOFF: A GOOD DEAL is not necessarily A GOOD DEAL RIGHT NOW."),
        ("Owner absence", f"Three-business-day thought experiment: {p.owner_absence(3).name}; critical coordination is owner-heavy."),
        ("Weekly operating review", "Commit incident recovery and QA; monitor support, pipeline, cash due, owner/partner capacity and risks; explicitly defer audit and queued kickoff."),
        ("Current portfolio risks", "; ".join(r.description for r in p.risks) + "; owner dependence; partner concentration; support overload."),
        ("Interpretation", "Portfolio judgment protects commitments, incident readiness, cash, and continuity. It does not maximize starts or automatically hire through overload. Chapter 31B will add scenario and cash-flow simulation."),
    ]
    print("FICTIONAL TRAINING SCENARIO\nALL CUSTOMERS AND WORKLOADS ARE SIMULATED")
    for i, (title, body) in enumerate(sections, 1): print(f"\n{i}. {title}\n{body}")


if __name__ == "__main__": main()
