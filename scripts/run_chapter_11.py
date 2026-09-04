"""Run Chapter 11's deterministic, entirely fictional qualification exercise."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.economics import EconomicSignificance as E  # noqa: E402
from local_works.qualification import (  # noqa: E402
    BudgetStatus as B, DimensionAssessment, QualificationAssessment,
    QualificationDimension as D, QualificationGap, QualificationRating as R,
    QualificationRisk, RiskSeverity,
)


def qualify(name: str, *, economics: E = E.MEANINGFUL_BURDEN_ESTABLISHED,
            budget: B = B.PLAUSIBLE_CAPACITY, changes: dict[D, R] | None = None,
            risks: list[QualificationRisk] | None = None,
            gaps: list[QualificationGap] | None = None, hours: float = 3,
            rationale: str = "The stated evidence supports this gate decision.") -> QualificationAssessment:
    ratings = {dimension: R.STRONG for dimension in D}
    ratings[D.URGENCY] = R.ACCEPTABLE
    ratings[D.COMMERCIAL_RISK] = R.ACCEPTABLE
    ratings.update(changes or {})
    return QualificationAssessment(
        name,
        [DimensionAssessment(dimension, rating, ("fictional scenario evidence",))
         for dimension, rating in ratings.items()],
        economics, budget, risks=risks or [], gaps=gaps or [],
        expected_presales_hours=hours, rationale=rationale,
    )


def show(item: QualificationAssessment) -> None:
    for dimension in D:
        print(f"{dimension.value:29} {item.rating_for(dimension).name}")
    print("Positive signals:", ", ".join(item.positive_signals) or "See dimension evidence")
    print("Concerns:", ", ".join(item.concerns) or "None recorded")
    print("Unknowns:", "; ".join(item.unknowns) or "None recorded")
    print("Hard disqualifiers:", "; ".join(r.description for r in item.hard_disqualifiers) or "None")
    print("Decision:", item.decision.name)
    print("Rationale:", item.rationale)


def main() -> None:
    print("CHAPTER 11 — QUALIFY THE OPPORTUNITY\nALL BUSINESSES AND SCENARIOS ARE FICTIONAL; NO CUSTOMER RESULTS")
    print("\nSECTION 1 — Qualification gate")
    print("Problem\n→ Evidence\n→ Economics\n→ Qualification\n→ Continue or Stop")

    print("\nSECTION 2 — Strong candidate")
    strong = qualify("Fictional strong candidate", rationale="Meaningful problem, customer priority, authority, plausible capacity, and no hard risk support continued design effort.")
    show(strong)

    print("\nSECTION 3 — Real problem, no priority")
    show(qualify("Fictional no-priority candidate", changes={D.CUSTOMER_PRIORITY: R.WEAK},
                 rationale="The customer says this is not a priority this year; stop for now rather than manufacture urgency."))

    print("\nSECTION 4 — Real problem, trivial economics")
    show(qualify("Fictional $75 burden", economics=E.ECONOMICALLY_TRIVIAL,
                 rationale="A real problem with approximately $75 annual direct burden does not justify pursuit."))

    print("\nSECTION 5 — Strong problem, no authority")
    show(qualify("Fictional corporate location", changes={D.AUTHORITY: R.UNCERTAIN},
                 gaps=[QualificationGap("corporate authorization path", "Identify an authorized corporate decision maker")],
                 rationale="The local manager cannot authorize technology changes; seek authority before further design."))

    print("\nSECTION 6 — Good problem, wrong Local Works fit")
    show(qualify("Fictional specialist legal matter", changes={D.LOCAL_WORKS_FIT: R.WEAK},
                 rationale="The need is real but requires specialist legal expertise; make a responsible referral."))

    print("\nSECTION 7 — Dangerous engagement")
    show(qualify("Fictional unsafe request", risks=[QualificationRisk(
        "Customer requires Local Works to conceal unauthorized access from corporate", RiskSeverity.DISQUALIFIER)],
        rationale="An unethical and unauthorized condition is a hard disqualifier regardless of positive signals."))

    print("\nSECTION 8 — Budget unknown")
    show(qualify("Fictional unknown-budget candidate", budget=B.UNKNOWN,
        gaps=[QualificationGap("budget/capacity", "Ask who controls spending, the budget cycle, approval level, and willingness to invest if value is established")],
        rationale="UNKNOWN does not mean NO. Test capacity with bounded effort; do not assert an amount."))

    print("\nSECTION 9 — Owner-time protection")
    print("Opportunity A: strong evidence, clear authority, approximately 3 remaining pre-sales hours.")
    print("Opportunity B: many unknowns, unclear authority, approximately 20 unpaid research hours.")
    print("Finite owner time favors bounded, evidence-rich pursuit before pricing; this is opportunity-cost discipline, not cynicism.")

    print("\nSECTION 10 — Harbor Fitness")
    harbor = qualify("Harbor Fitness membership-change workflow", economics=E.MORE_EVIDENCE_REQUIRED,
        budget=B.UNKNOWN, hours=5,
        changes={D.PROBLEM_UNDERSTANDING: R.ACCEPTABLE, D.ECONOMIC_SIGNIFICANCE: R.UNCERTAIN,
                 D.CUSTOMER_PRIORITY: R.UNCERTAIN, D.URGENCY: R.UNCERTAIN,
                 D.AUTHORITY: R.UNCERTAIN, D.BUDGET_CAPACITY: R.UNCERTAIN,
                 D.TECHNICAL_PLAUSIBILITY: R.UNCERTAIN,
                 D.ORGANIZATIONAL_FEASIBILITY: R.UNCERTAIN, D.MEASURABILITY: R.ACCEPTABLE},
        gaps=[QualificationGap("customer priority and why now", "Ask management to rank this work"),
              QualificationGap("owner authority and spending capacity", "Confirm owner roles, willingness, and approval path"),
              QualificationGap("platform restrictions", "Conduct bounded vendor documentation research"),
              QualificationGap("measured volume and handling time", "Review request logs and observe a sample")],
        rationale="Discovery and workflow evidence establish plausible friction, but Chapter 10 found estimated/hypothetical direct burden and important unknowns. Run one bounded evidence step before solution design.")
    show(harbor)
    print("Expected remaining pre-sales effort: approximately 5 hours (fictional planning estimate).")
    print("Qualification selects no solution, creates no proposal, and guarantees no sale.")


if __name__ == "__main__":
    main()
