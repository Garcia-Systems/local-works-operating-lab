from datetime import date, timedelta

from local_works.launch import (
    CloseoutChecklist, CloseoutStatus, LaunchDecision, LaunchPlan, LaunchReadiness,
    LaunchRequirement, ProjectCloseout, ProductionCheck, ResponsibleParty,
    RollbackPlan, RollbackReadiness, SolutionLaunchType, CutoverApproach,
    StabilizationStatus,
)
from local_works.project_economics import (
    CashEvent, EstimateActual, EvidenceStatus, OwnerTime, PaymentRecord,
    PaymentSchedule, PaymentStatus, ProjectEconomics, ValueRealizationPlan,
    maximum_cash_exposure,
)


def test_acceptance_is_not_launch_and_blocker_prevents_readiness():
    readiness = LaunchReadiness(True, (LaunchRequirement(
        "blocking defects", False, True, LaunchDecision.NEEDS_DEFECT_RESOLUTION),))
    assert readiness.decide() is LaunchDecision.NEEDS_DEFECT_RESOLUTION
    # Readiness is a decision, not a launch event or status transition.
    assert not hasattr(readiness, "occurred_on")


def test_nonblocking_known_issue_allows_monitored_launch():
    readiness = LaunchReadiness(True, (LaunchRequirement("access", True),), ("copy",))
    assert readiness.decide() is LaunchDecision.READY_WITH_MONITORED_RISKS


def test_rollback_and_authority_are_preserved():
    plan = LaunchPlan(SolutionLaunchType.CONFIGURE, CutoverApproach.SCHEDULED, date.today(),
                      ResponsibleParty.CUSTOMER, ResponsibleParty.DELIVERY_PARTNER,
                      ResponsibleParty.LOCAL_WORKS, ResponsibleParty.LOCAL_WORKS,
                      RollbackPlan(RollbackReadiness.MANUAL, "restore settings",
                                   ResponsibleParty.SHARED), ("core workflow",))
    assert plan.authorizer is ResponsibleParty.CUSTOMER
    assert plan.rollback.readiness is RollbackReadiness.MANUAL


def test_production_verification_can_fail_after_acceptance():
    check = ProductionCheck("notification", False, "fictional production check")
    assert not check.passed


def test_payments_keep_charges_cash_and_lateness_distinct():
    schedule = PaymentSchedule(6000, 500, 0, 3000)
    assert schedule.total_customer_charges == 6500
    assert schedule.final_amount_due == 3500
    record = PaymentRecord(3500, PaymentStatus.LATE, "acceptance",
                           due_date=date.today() - timedelta(days=60))
    assert record.days_outstanding(date.today()) == 60
    assert record.amount != schedule.total_customer_charges


def test_economics_owner_time_and_safe_zero_margin():
    time = OwnerTime({"acquisition": 2, "delivery_coordination": 18})
    economics = ProjectEconomics(PaymentSchedule(6000), 2800, 400, time, 75)
    assert economics.contribution == 2800
    assert economics.contribution_margin == 2800 / 6000
    assert economics.imputed_owner_time_value == 1500
    assert economics.contribution_after_owner_time == 1300
    assert economics.contribution_per_owner_hour == 140
    assert time.presales_hours == 2 and time.delivery_hours == 18
    zero = ProjectEconomics(PaymentSchedule(0), 0, 0, OwnerTime({}), 75)
    assert zero.contribution_margin is None and zero.contribution_per_owner_hour is None


def test_estimate_versions_remain_distinct_and_immutable():
    comparison = EstimateActual(20, 28, 35)
    assert (comparison.original_estimate, comparison.revised_forecast,
            comparison.actual, comparison.variance) == (20, 28, 35, 15)


def test_change_and_rework_only_charge_when_approved():
    # Schedule accepts only the explicitly approved paid-change total; absorbed
    # work and defect rework belong in actual cost/effort instead.
    schedule = PaymentSchedule(6000, approved_paid_changes=0)
    actual = ProjectEconomics(schedule, 3200, 400, OwnerTime({"change_control": 4}), 75)
    assert schedule.total_customer_charges == 6000
    assert actual.contribution == 2400


def test_maximum_cash_exposure_uses_event_timing():
    events = [CashEvent(date(2026, 1, 1), -4000, "partner"),
              CashEvent(date(2026, 1, 2), 3000, "deposit"),
              CashEvent(date(2026, 1, 3), 5000, "final")]
    assert maximum_cash_exposure(events) == 4000


def test_expected_value_is_not_measured_value():
    plan = ValueRealizationPlan("12 interventions/week", "reduce routine handling",
                                ("interventions/week",))
    assert plan.evidence_status is EvidenceStatus.MEASUREMENT_PENDING
    assert plan.measured_value is None


def test_closeout_can_preserve_payment_measurement_and_stabilization_states():
    checklist = CloseoutChecklist({"launch": True, "documentation": True})
    assert ProjectCloseout(checklist, StabilizationStatus.STABLE,
                           payment_outstanding=True).status() is CloseoutStatus.CLOSED_WITH_OUTSTANDING_PAYMENT
    assert ProjectCloseout(checklist, StabilizationStatus.STABLE,
                           value_measurement_pending=True).status() is CloseoutStatus.MEASUREMENT_PENDING
    assert ProjectCloseout(checklist, StabilizationStatus.MONITORING).status() is CloseoutStatus.STABILIZATION_REQUIRED


def test_chapter_has_no_support_execution_models():
    import local_works.launch as launch
    assert not hasattr(launch, "SupportTicket")
    assert not hasattr(launch, "RecurringSupportPlan")
