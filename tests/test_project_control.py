from datetime import date
from local_works.project_control import *


def milestone(): return Milestone("M1", "Capability validated", MilestoneType.TECHNICAL_VALIDATION, WorkOwner.DELIVERY_PARTNER, date(2026, 9, 4))
def task(task_id="T1", **kw):
    values=dict(title="Validate", category=TaskCategory.VALIDATION, owner=WorkOwner.DELIVERY_PARTNER, related_milestone="M1", done_condition="Evidence recorded")
    values.update(kw); return ProjectTask(task_id, **values)

def test_milestone_and_task_are_distinct_and_baseline_is_preserved():
    m=milestone(); original=m.baseline_date; m.reforecast(date(2026,9,8))
    assert not isinstance(task(), Milestone) and m.baseline_date == original and m.forecast_date != original

def test_task_owner_and_dependency_readiness():
    first=task(status=TaskStatus.IN_PROGRESS); dependent=task("T2", dependencies=("T1",))
    assert dependent.owner is WorkOwner.DELIVERY_PARTNER and not dependent.ready([first, dependent])
    first.status=TaskStatus.DONE; assert dependent.ready([first, dependent])

def test_blocker_is_not_at_risk_and_affects_many_records():
    m1=milestone(); m2=Milestone("M2","Review",MilestoneType.CUSTOMER_REVIEW,WorkOwner.CUSTOMER,date(2026,9,8)); t1=task(); t2=task("T2")
    blocker=Blocker("B1","Vendor answer absent",BlockerCategory.VENDOR,WorkOwner.VENDOR,date(2026,9,1),"Validation cannot finish",("T1","T2"),("M1","M2"))
    control=ProjectControl([m1,m2],[t1,t2]); control.apply_blocker(blocker)
    assert blocker.status is BlockerStatus.OPEN and all(t.status is TaskStatus.BLOCKED for t in control.tasks)
    assert all(m.status is MilestoneStatus.AT_RISK for m in control.milestones)

def test_decision_has_owner_latency_and_forecast_effect():
    d=ProjectDecisionRequest("D1","Which types?","Harbor Operations Manager",date(2026,9,1),date(2026,9,2),"Test moves",("All","Selected"))
    assert d.decision_owner and d.latency_days(date(2026,9,5)) == 4 and d.threatens_forecast(date(2026,9,5))

def test_variance_math_positive_and_negative():
    over=DeliveryVariance(18,12,10); under=DeliveryVariance(18,8,6)
    assert over.forecast_total == 22 and over.amount == 4 and round(over.percent) == 22
    assert under.amount == -4

def test_delay_sources_preserve_causality():
    delays=[DeliveryDelay(source,"Cause") for source in (DelaySource.CUSTOMER,DelaySource.DELIVERY_PARTNER,DelaySource.VENDOR,DelaySource.LOCAL_WORKS)]
    assert len({d.source for d in delays}) == 4

def test_optional_work_defers_and_scope_signal_does_not_execute():
    optional=task(priority="COULD"); control=ProjectControl(tasks=[optional]); signal=control.add_scope_signal("Add cancellation")
    assert optional.defer_optional() and signal.status == "POTENTIAL_SCOPE_CHANGE" and not signal.executed and len(control.tasks)==1

def test_health_supports_on_track_at_risk_and_blocked():
    for state in (HealthState.ON_TRACK,HealthState.AT_RISK,HealthState.BLOCKED):
        health=ProjectHealth({HealthDimension.SCHEDULE: HealthAssessment(state,"Evidence")}); assert health.overall is state

def test_control_can_reforecast_pause_or_continue():
    control=ProjectControl(tasks=[task()])
    assert control.decide(reforecast=True) is ProjectControlDecision.CONTINUE_WITH_REFORECAST
    assert control.decide(pause=True) is ProjectControlDecision.PAUSE
    assert control.decide() is ProjectControlDecision.CONTINUE

def test_chapter_does_not_execute_scope_qa_or_deployment():
    control=ProjectControl(); assert not hasattr(control,"execute_scope_change") and not hasattr(control,"run_qa") and not hasattr(control,"deploy")
