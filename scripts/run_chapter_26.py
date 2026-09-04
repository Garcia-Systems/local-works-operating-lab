#!/usr/bin/env python3
"""Run Chapter 26's entirely fictional launch and economics exercise."""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.launch import *
from local_works.project_economics import *


def money(value: float) -> str:
    return f"${value:,.2f}"


def main() -> None:
    print("FICTIONAL TRAINING SCENARIO")
    print("NO REAL SYSTEM IS BEING DEPLOYED")
    print("NO REAL PAYMENT IS BEING COLLECTED")
    print("\nSECTION 1 — Starting accepted project state")
    print("Harbor Fitness | membership-freeze configuration | HF-SCOPE-14-v1 / HF-REQ-21-v1")
    print("Acceptance: ACCEPTED_WITH_KNOWN_ISSUES; HF-D01 closed; HF-D02 cosmetic copy known")
    print("Terms: $6,000; 50% simulated deposit / 50% at acceptance; cancellation excluded")

    requirements = (
        LaunchRequirement("acceptance", True), LaunchRequirement("production access", True, True, LaunchDecision.NEEDS_ACCESS),
        LaunchRequirement("blocking defects resolved", True, True, LaunchDecision.NEEDS_DEFECT_RESOLUTION),
        LaunchRequirement("configuration method", True, True, LaunchDecision.NEEDS_DEPLOYMENT_PLAN),
        LaunchRequirement("prior settings / reversal", True, True, LaunchDecision.NEEDS_ROLLBACK_PLAN),
        LaunchRequirement("vendor coordination", True, True, LaunchDecision.NEEDS_VENDOR_COORDINATION),
        LaunchRequirement("verification, people, communication, escalation", True),
    )
    readiness = LaunchReadiness(True, requirements, ("HF-D02 awkward confirmation copy",))
    print("\nSECTION 2 — Launch readiness")
    for item in requirements:
        print(f"{item.name}: {'READY' if item.satisfied else 'NOT READY'}")
    print("Decision:", readiness.decide().name)

    rollback = RollbackPlan(RollbackReadiness.MANUAL, "restore recorded settings and prior staff process",
                            ResponsibleParty.SHARED, ("data integrity", "security/access", "core workflow unusable"))
    plan = LaunchPlan(SolutionLaunchType.CONFIGURE, CutoverApproach.SCHEDULED, date(2026, 9, 22),
                      ResponsibleParty.CUSTOMER, ResponsibleParty.DELIVERY_PARTNER,
                      ResponsibleParty.LOCAL_WORKS, ResponsibleParty.LOCAL_WORKS, rollback,
                      ("standard path", "exception path", "confirmation", "staff visibility"),
                      ("staffed operating-hours window",))
    print("\nSECTION 3 — Launch plan")
    print("Approach: configuration activation / SCHEDULED; not custom deployment")
    print("Authorize/perform/verify/communicate/rollback:", plan.authorizer.name, plan.performer.name,
          plan.verifier.name, plan.communicator.name, rollback.decision_owner.name)
    print("Verification:", ", ".join(plan.verification_steps), "| reversal:", rollback.reversal)

    event = LaunchEvent(date(2026, 9, 22), plan, ResponsibleParty.CUSTOMER)
    print("\nSECTION 4 — Simulated launch")
    print(event.occurred_on, "approved configuration activated; fictional:", event.fictional)
    checks = [ProductionCheck(name, True, "synthetic critical-path observation") for name in plan.verification_steps]
    print("\nSECTION 5 — Production verification")
    for check in checks:
        print(check.behavior, "PASS" if check.passed else "FAIL")
    print("This is production verification, not a complete QA rerun.")

    print("\nSECTION 6 — Launch issue")
    print("LOW: one confirmation used older awkward copy → CONTINUE_WITH_FIX, recheck, communicate.")
    print("No rollback. Hypothetical wrong-member update → PAUSE/ROLLBACK; it did not occur.")
    stabilization = StabilizationPeriod(date(2026, 9, 22), date(2026, 9, 25), StabilizationStatus.STABLE,
                                        ("copy corrected", "initial fictional requests monitored"))
    print("\nSECTION 7 — Stabilization")
    print(stabilization.status.name, "; ".join(stabilization.observations))

    schedule = PaymentSchedule(6000, 0, 0, 3000)
    print("\nSECTION 8 — Commercial completion")
    print("Original", money(schedule.original_price), "approved paid changes $0.00, credits $0.00")
    print("Charges", money(schedule.total_customer_charges), "deposit", money(schedule.payments_received),
          "final balance", money(schedule.final_amount_due))
    final_payment = PaymentRecord(3000, PaymentStatus.RECEIVED_SIMULATED, "customer acceptance",
                                  date(2026, 9, 19), date(2026, 9, 29), date(2026, 9, 29))
    print("\nSECTION 9 — Simulated final payment")
    print(final_payment.status.name, money(final_payment.amount), final_payment.received_date,
          "(charge/revenue and cash remain distinct)")

    effort = EstimateActual(18, 22, 25)
    cost = EstimateActual(2800, 3000, 3200)
    print("\nSECTION 10 — Estimated vs actual")
    print("Effort original/revised/actual:", effort.original_estimate, effort.revised_forecast, effort.actual,
          "hours; variance", effort.variance)
    print("Cost original/revised/actual:", money(cost.original_estimate), money(cost.revised_forecast or 0),
          money(cost.actual), "| schedule moved from original plan; owner time actual below")

    hours = OwnerTime({"acquisition": 2, "audit": 2, "discovery": 3, "solution_design": 2,
                       "proposal_sales": 3, "closing": 2, "delivery_coordination": 5,
                       "requirements_translation": 4, "project_management": 3, "qa": 4,
                       "change_control": 2, "customer_communication": 1, "commercial_closeout": 3})
    economics = ProjectEconomics(schedule, 3200, 400, hours, 75)
    print("\nSECTION 11 — Actual Local Works economics")
    print("Contribution", money(economics.contribution), "margin", f"{economics.contribution_margin:.1%}")
    print("Owner hours", hours.total_hours, "(presales", hours.presales_hours, "/ delivery-close", hours.delivery_hours, ")")
    print("Imputed owner time", money(economics.imputed_owner_time_value), "adjusted contribution",
          money(economics.contribution_after_owner_time), "contribution/owner hour",
          money(economics.contribution_per_owner_hour or 0), "(not a wage)")

    events = [CashEvent(date(2026, 9, 1), 3000, "deposit"), CashEvent(date(2026, 9, 8), -1600, "partner"),
              CashEvent(date(2026, 9, 15), -400, "direct"), CashEvent(date(2026, 9, 24), -1600, "partner"),
              CashEvent(date(2026, 9, 29), 3000, "final")]
    print("\nSECTION 12 — Cash flow")
    for item in events: print(item.occurred_on, money(item.amount), item.description)
    print("Maximum cash exposure:", money(maximum_cash_exposure(events)), "| outstanding after receipt: $0.00")

    print("\nSECTION 13 — Change/rework impact")
    print("Cancellation deferred: $0 charge; absorbed copy work: internal burden; HF-D01 3h correction/retest: $0 charge.")
    print("These help explain actual variance without rewriting the estimate.")
    value = ValueRealizationPlan("Chapter 10 burden estimate and underlying workflow samples",
                                 "fewer routine interventions and less waiting",
                                 ("staff interventions/week", "minutes/request", "member contacts", "exception/rework rate"))
    print("\nSECTION 14 — Customer economics")
    print("Expected hypothesis:", value.expected_value_hypothesis, "| measured value: NOT YET ESTABLISHED")
    print("Soft benefits remain non-monetized; unsupported savings claims are prohibited.")
    print("\nSECTION 15 — Value realization plan")
    print("Baseline preserved; 30 days sample interventions/time; 60 days contacts/exceptions; 90 days processing/rework.")
    print("Evidence:", value.evidence_status.name)
    print("\nSECTION 16 — Partner performance")
    print("Good configuration judgment, communication, documentation and defect response; mixed estimate accuracy; private evidence only.")
    print("\nSECTION 17 — Project postmortem")
    print("Repeat traceability, explicit exclusions, reversal and checks. Improve copy control and estimate/retest allowance.")
    print("Owner-time lesson: apparent 40% margin becomes negative after the chosen owner-time value.")
    print("\nSECTION 18 — Closeout checklist")
    checklist = CloseoutChecklist({"launch": True, "stabilization": True, "acceptance": True,
        "blocking defects": True, "known issues transferred": True, "documentation/control": True,
        "access reviewed": True, "payment statuses known": True, "economics": True,
        "value plan": True, "support boundary communicated": True, "lessons": True})
    for item, done in checklist.operational_items.items(): print(item, "COMPLETE" if done else "OPEN")
    closeout = ProjectCloseout(checklist, StabilizationStatus.STABLE, value_measurement_pending=True)
    print("\nSECTION 19 — Final closeout status")
    print(closeout.status().name)
    print("\nSECTION 20 — Interpretation")
    print("A completed project produces three kinds of truth: delivery truth, commercial truth, economic truth.")
    print("Working software alone cannot answer all three. Chapter 27 support execution is intentionally absent.")


if __name__ == "__main__":
    main()
