#!/usr/bin/env python3
"""Run the fictional Chapter 23 Harbor Fitness control exercise."""
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from local_works.project_control import *


def section(n, title): print(f"\nSECTION {n} — {title}")

print("FICTIONAL TRAINING SCENARIO")
print("NO REAL CUSTOMER PROJECT WORK IS OCCURRING")
section(1,"Starting project state")
print("Scope: HF-SCOPE-14-v1 paid configuration validation; cancellation excluded")
print("Requirements: HF-REQ-21-v1 | Translation: ready for bounded validation | Estimate: 18h")
ms=[Milestone("M1","Kickoff Complete",MilestoneType.KICKOFF,WorkOwner.LOCAL_WORKS,date(2026,9,1),MilestoneStatus.COMPLETE), Milestone("M2","Platform Capability Validated",MilestoneType.TECHNICAL_VALIDATION,WorkOwner.DELIVERY_PARTNER,date(2026,9,7),MilestoneStatus.IN_PROGRESS), Milestone("M3","Configuration Path Confirmed",MilestoneType.CONFIGURATION_COMPLETE,WorkOwner.DELIVERY_PARTNER,date(2026,9,9)), Milestone("M4","Test Workflow Ready",MilestoneType.QA_READY,WorkOwner.LOCAL_WORKS,date(2026,9,11)), Milestone("M5","Customer Review",MilestoneType.CUSTOMER_REVIEW,WorkOwner.SHARED,date(2026,9,14)), Milestone("M6","Delivery Recommendation / Acceptance Ready",MilestoneType.ACCEPTANCE_READY,WorkOwner.LOCAL_WORKS,date(2026,9,16))]
tasks=[ProjectTask("T1","Validate freeze capability",TaskCategory.VALIDATION,WorkOwner.DELIVERY_PARTNER,"M2",estimated_effort=4,actual_effort=4,status=TaskStatus.DONE,done_condition="Evidence recorded"), ProjectTask("T2","Confirm eligibility fields",TaskCategory.COORDINATION,WorkOwner.CUSTOMER,"M3",dependencies=("D1",),estimated_effort=2,remaining_estimate=2,status=TaskStatus.BLOCKED,done_condition="Fields confirmed"), ProjectTask("T3","Prepare standard case",TaskCategory.TEST_PREPARATION,WorkOwner.DELIVERY_PARTNER,"M4",dependencies=("T1",),estimated_effort=2,actual_effort=2,status=TaskStatus.DONE,done_condition="Case recorded"), ProjectTask("T4","Prepare exception route",TaskCategory.TEST_PREPARATION,WorkOwner.DELIVERY_PARTNER,"M4",dependencies=("T2",),estimated_effort=4,actual_effort=3,remaining_estimate=4,status=TaskStatus.IN_PROGRESS,done_condition="Route evidence planned"), ProjectTask("T5","Validate confirmation behavior",TaskCategory.VALIDATION,WorkOwner.DELIVERY_PARTNER,"M2",dependencies=("T1",),estimated_effort=2,actual_effort=2,remaining_estimate=1,status=TaskStatus.IN_PROGRESS,done_condition="Outcomes recorded"), ProjectTask("T6","Document limitations",TaskCategory.DOCUMENTATION,WorkOwner.LOCAL_WORKS,"M4",dependencies=("T1",),estimated_effort=2,actual_effort=1,remaining_estimate=1,status=TaskStatus.READY,done_condition="Limits recorded"), ProjectTask("T7","Prepare customer review",TaskCategory.CUSTOMER_REVIEW,WorkOwner.LOCAL_WORKS,"M5",dependencies=("T3","T4","T5","T6"),estimated_effort=2,remaining_estimate=2,done_condition="Review ready")]
control=ProjectControl(ms,tasks)
section(2,"Milestones")
for m in ms: print(m.milestone_id,m.name,"plan",m.baseline_date,"status",m.status.value)
section(3,"Tasks")
for t in tasks: print(t.task_id,t.title,"owner",t.owner.value,"depends",t.dependencies or "none","status",t.status.value)
section(4,"First project update"); print("Completed: capability, standard case | In progress: confirmation | Next: limitations")
section(5,"Blocker appears")
b=Blocker("B1","Vendor documentation does not clarify configurable exception routing",BlockerCategory.VENDOR,WorkOwner.VENDOR,date(2026,9,4),"T4 cannot finish",("T4",),("M2","M4"),BlockerStatus.WAITING,"Delivery Partner seeks fictional clarification")
control.apply_blocker(b); print(b.description,"|",b.status.value,"| next:",b.next_action)
section(6,"Impact propagation"); print("T4:",tasks[3].status.value,"| M2/M4:",ms[1].status.value,ms[3].status.value,"| project can continue partially")
section(7,"Decision request")
d=ProjectDecisionRequest("D1","Which membership types require exception approval?","Harbor Operations Manager",date(2026,8,31),date(2026,9,2),"T2/T4 and M4 move",("All types","Confirmed selected types")); print(d.question,"| owner",d.decision_owner,"| fictional latency",d.latency_days(date(2026,9,4)),"days")
section(8,"Estimate vs actual")
v=DeliveryVariance(18,12,10); print(f"18h baseline; 12h actual simulated + 10h ETC = {v.forecast_total:g}h; variance {v.amount:+g}h / {v.percent:+.1f}%")
section(9,"Forecast change"); ms[3].reforecast(date(2026,9,15)); print("M4 plan",ms[3].baseline_date,"| forecast",ms[3].forecast_date,"| MODERATE | vendor clarification + extra exception case")
section(10,"Corrective action"); print("RESEQUENCE_WORK + REFORECAST: continue T5, T6, and review skeleton; adding people would not answer the rule")
section(11,"Scope-creep signal"); s=control.add_scope_signal("Add cancellation workflow"); print(s.status,"| executed:",s.executed,"| no task created")
section(12,"Owner workload"); effort=OwnerEffort(1,1.5,.75,1.25,.5); print("Local Works simulated project-control effort:",effort.total,"hours")
section(13,"Customer update"); print("Capability and standard-case preparation are complete. Exception routing awaits fictional vendor clarification. M4 moves from Friday 11 September to Tuesday 15 September with moderate confidence; available documentation work continues. Forecast effort is 22h versus 18h. Cancellation is logged for later scope review, not implementation.")
section(14,"Project health")
health=ProjectHealth({HealthDimension.SCOPE:HealthAssessment(HealthState.WATCH,"Potential change held"),HealthDimension.SCHEDULE:HealthAssessment(HealthState.AT_RISK,"M4 reforecast"),HealthDimension.COST:HealthAssessment(HealthState.WATCH,"+4h forecast"),HealthDimension.QUALITY:HealthAssessment(HealthState.ON_TRACK,"Controls retained"),HealthDimension.DEPENDENCIES:HealthAssessment(HealthState.AT_RISK,"Vendor UNKNOWN"),HealthDimension.CUSTOMER_DECISIONS:HealthAssessment(HealthState.WATCH,"Two-day fictional delay")})
for k,x in health.dimensions.items(): print(k.value,x.state.value,"—",x.rationale)
section(15,"Final project-control decision"); print(control.decide(reforecast=True).name,"| overall",health.overall.value)
section(16,"Interpretation"); print("Good project control makes reality visible early enough to do something about it.")
print("\nFAILURE — GREEN UNTIL RED: weeks 1–3 on track; week 4 three-week miss. Ignored: vendor question, overrun, test failures, decision delay. STATUS REPORTING WITHOUT FORECASTING IS NOT PROJECT CONTROL.")
print("FAILURE — EVERYTHING URGENT: context switching makes MUST work late; urgency needs business impact.")
print("FAILURE — HIDDEN BAD NEWS: Monday API blocker disclosed Friday creates CUSTOMER SURPRISE; communicate early.")
print("FAILURE — ADD PEOPLE: a second developer cannot resolve an unanswered business rule.")
print("SUCCESS — EARLY REFORECAST: record, resequence, forecast, inform, request decision; Friday brings no surprise.")
