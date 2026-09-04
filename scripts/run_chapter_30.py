#!/usr/bin/env python3
"""Run Chapter 30's fictional relationship exercise; no outreach occurs."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_works.relationships import *


def main() -> None:
    print("FICTIONAL TRAINING SCENARIO")
    print("NO REAL CUSTOMER REFERRALS, TESTIMONIALS, OR CASE STUDIES ARE BEING CLAIMED")
    outcome = CustomerOutcomeEvidence("membership-request handling time", "prior chapter baseline", UNKNOWN,
        "post-launch window pending", EvidenceType.EXPECTED_ONLY, "Chapter 26 measurement plan", "UNKNOWN")
    health = RelationshipHealth(HealthRating.HEALTHY, HealthRating.HEALTHY, HealthRating.HEALTHY,
        HealthRating.HEALTHY, HealthRating.HEALTHY, HealthRating.HEALTHY, HealthRating.HEALTHY,
        HealthRating.MIXED, HealthRating.MIXED, HealthRating.UNKNOWN, HealthRating.HEALTHY,
        HealthRating.HEALTHY, HealthRating.HEALTHY)
    cancellation = ExpansionSignal("online cancellation", SignalSource.DEFERRED_CHANGE, "repeated",
        "plausible; unmeasured", "unconfirmed", "deferred scope plus support pattern", ExpansionPipelineState.QUALIFYING)
    family = ExpansionSignal("family membership handling", SignalSource.HYPOTHETICAL)
    dashboard = ExpansionSignal("quarterly custom dashboard", SignalSource.CUSTOMER_REQUEST, "quarterly", "low", "low",
        "existing platform report is adequate", ExpansionPipelineState.LEAVE_ALONE)
    opportunity = ExpansionOpportunity(cancellation, "manual cancellation workflow", "members and staff",
        "unconfirmed", UNKNOWN, UNKNOWN, None, None, "configure or existing vendor first",
        support_impact=UNKNOWN, decision=ExpansionDecision.DISCOVERY_REQUIRED)
    economics = RelationshipEconomics(12000,6600,600,150,350,0,0,100,5,35,5,3,2,3,1,75)
    relationship = CustomerRelationship("Harbor Fitness", RelationshipStatus.SUPPORTED, health,
        RetentionRisk.LOW, economics, False, "on-demand", 1.0, RelationshipAction.SUPPORT_LIGHTLY)
    sections = [
      ("Starting Harbor relationship", "Project accepted/launched fictionally; PAYG support; one simulated incident history; commercial status positive; realized value measurement pending."),
      ("Relationship health", "Overall HEALTHY: stability, support recovery, trust and commerce are healthy; measured outcomes remain UNKNOWN; no magic score."),
      ("Value realization", f"{outcome.metric}: baseline preserved; current UNKNOWN; {outcome.evidence_type.name}. Measured, partially measured, expected, and unknown must remain distinct."),
      ("Expansion signals", "online cancellation (deferred/repeated); family membership (hypothetical idea); quarterly dashboard (low burden). Signals are not opportunities."),
      ("Expansion qualification", "Cancellation appears real enough to investigate, but frequency, burden, authority, urgency, policy, feasibility, budget, and measurability need discovery."),
      ("Expansion economics", "Recoverable value, cost, price, payback, support burden, and new risk are UNKNOWN. Review/discovery/proposal owner effort is not free."),
      ("Expansion decision", opportunity.decision.name),
      ("Leave-alone opportunity", f"Quarterly dashboard: {ExpansionDecision.LEAVE_ALONE.name}; existing report and rare use make customization disproportionate."),
      ("Support vs expansion boundary", "Repeated 'Can members cancel online?' contact becomes a signal for separate qualification—not free support and not an automatic proposal."),
      ("Retention status", f"{relationship.status.name}; PAYG/SUPPORT_LIGHTLY is voluntary. No monthly plan or dependency is forced."),
      ("Churn-risk assessment", "LOW with measurement uncertainty visible. Quiet activity is not dissatisfaction; address observable unresolved issues only."),
      ("Healthy churn example", f"{ChurnReason.PROJECT_COMPLETE_NO_SUPPORT_NEEDED.name}: solution works, staff operates it, vendor support suffices; offboard gracefully."),
      ("Unhealthy churn example", "SUPPORT_QUALITY: ignored requests, repeated defects, and unclear billing cause avoidable loss; record lessons."),
      ("Referral readiness", assess_referral(stable=True, health=health.overall, measured_value=False, unresolved_dispute=False).name),
      ("Referral request simulation", "UNSENT/OPTIONAL: If you know another business with a similar membership workflow problem, I'd be glad to talk. No pressure."),
      ("Case-study readiness", f"{assess_case_study(real_customer=False, permission=None, measured_evidence=False, confidentiality_reviewed=None).name}; public use forbidden."),
      ("Reusable pattern assessment", f"MEMBERSHIP_ACCOUNT_MANAGEMENT: {ReuseConfidence.EARLY_SIGNAL.name}; one fictional case is not repeatability."),
      ("Cumulative relationship economics", f"Revenue ${economics.cumulative_revenue:,.0f}; direct cost ${economics.cumulative_direct_cost:,.0f}; contribution ${economics.cumulative_contribution:,.0f}; prior components remain separate."),
      ("Owner relationship hours", f"{economics.total_owner_hours:.1f} hours across acquisition, delivery, support, incident, review, expansion, and admin."),
      ("Expansion contribution per owner hour", f"${economics.expansion_contribution_per_owner_hour:.2f}; qualification consumed time but no expansion was won."),
      ("Relationship-overhead capacity", f"{relationship.overhead_hours_per_month:.1f} hour/customer/month of context and readiness; Part VIII will handle portfolios."),
      ("Expansion pipeline", f"Cancellation {cancellation.pipeline_state.name}; family {family.pipeline_state.name}, not forecast; dashboard {dashboard.pipeline_state.name}."),
      ("Referral pipeline", f"{ReferralPipelineState.REQUEST_NOT_APPROPRIATE.name} while value measurement remains pending; simulation only."),
      ("Final relationship decision", "SUPPORT_LIGHTLY; VALUE_REVIEW; cancellation DISCOVERY_REQUIRED; dashboard LEAVE_ALONE."),
      ("Interpretation", "Healthy customer relationships are not measured by how much more Local Works can sell. They are measured by whether both sides continue to receive value without creating unnecessary dependency or work. Failure lessons: do not upsell everything, avoid selling forever, ask too early, fake proof, lock in, retain bad economics, misread quiet customers, or skip expansion economics."),
    ]
    for i,(title,body) in enumerate(sections,1): print(f"\nSECTION {i} — {title}\n{body}")

if __name__ == "__main__": main()
