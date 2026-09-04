"""Run Chapter 12's deterministic, entirely fictional solution comparison."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.hypothesis import SolutionPath  # noqa: E402
from local_works.solutions import (  # noqa: E402
    AlternativeStatus, CapabilityQuestion, RelativeComplexity, RelativeCost,
    SolutionAlternative, SolutionAssessment, SolutionAssumption, TimeCategory,
)


PROBLEM = ("Certain membership freezes require policy-dependent staff review and several "
           "manual administrative steps across systems. Frequency, total burden, errors, "
           "and customer impact remain unmeasured.")


def option(name: str, path: SolutionPath, description: str, coverage: str,
           complexity: RelativeComplexity, cost: RelativeCost, time: TimeCategory,
           assumption: str, *, status: AlternativeStatus = AlternativeStatus.NEEDS_VALIDATION,
           policy: str = "Potentially strong", dependency: str = "UNKNOWN",
           maintenance: str = "UNKNOWN", changes: tuple[str, ...] = ()) -> SolutionAlternative:
    return SolutionAlternative(
        name, path, description, PROBLEM, workflow_changes=changes,
        systems_involved=("Existing membership platform",),
        implementation_complexity=complexity, estimated_cost_category=cost,
        estimated_time_category=time, problem_coverage=coverage, policy_fit=policy,
        vendor_dependency=dependency, maintainability=maintenance,
        assumptions=(SolutionAssumption(assumption, "It may change feasibility and path selection"),),
        unresolved_questions=(assumption,), status=status,
    )


def build_assessment() -> SolutionAssessment:
    alternatives = [
        option("Configure existing membership platform", SolutionPath.CONFIGURE,
               "Enable a supported self-service or staff workflow, if one exists.",
               "UNKNOWN / potentially high", RelativeComplexity.LOW, RelativeCost.LOW,
               TimeCategory.DAYS, "The platform supports conditional freeze workflows.",
               dependency="High: existing vendor", maintenance="Low if vendor-supported"),
        option("Integrate a lightweight request interface", SolutionPath.INTEGRATE,
               "Move requests into the current platform while preserving approval rules.",
               "UNKNOWN / potentially high", RelativeComplexity.MODERATE, RelativeCost.MODERATE,
               TimeCategory.WEEKS, "Suitable supported APIs or integration mechanisms exist.",
               dependency="High: platform interface", maintenance="Moderate"),
        option("Automate staff coordination", SolutionPath.AUTOMATE,
               "Route requests, approvals, confirmations, and reminders around current systems.",
               "Partial to potentially high", RelativeComplexity.MODERATE, RelativeCost.MODERATE,
               TimeCategory.WEEKS, "Stable events and rules can safely drive automation.",
               dependency="Existing tools and interfaces", maintenance="Moderate"),
        option("Custom member account-management experience", SolutionPath.CUSTOM_BUILD,
               "Create a purpose-built member and staff workflow.", "Potentially high",
               RelativeComplexity.VERY_HIGH, RelativeCost.VERY_HIGH, TimeCategory.MONTHS,
               "Simpler paths cannot provide the required capabilities.",
               status=AlternativeStatus.NOT_RECOMMENDED, dependency="New and existing systems",
               maintenance="High long-term responsibility"),
        option("Leave current workflow alone", SolutionPath.LEAVE_ALONE,
               "Keep the policy-dependent manual workflow.", "No improvement; burden remains",
               RelativeComplexity.LOW, RelativeCost.VERY_LOW, TimeCategory.DAYS,
               "The modest, uncertain burden may not justify intervention.",
               status=AlternativeStatus.VIABLE_ALTERNATIVE, policy="Strong: unchanged",
               dependency="None added", maintenance="No new responsibility"),
    ]
    questions = [
        CapabilityQuestion("Membership platform", "Conditional self-service freezes", "Could make configuration adequate", validation_method="Vendor documentation and customer admin demonstration"),
        CapabilityQuestion("Membership platform", "Supported API or integration mechanism", "Controls integration feasibility", validation_method="Vendor documentation or sandbox/test environment"),
        CapabilityQuestion("Membership platform", "Approval rules, events, and notifications", "Controls safe automation", validation_method="Admin demonstration and bounded vendor support question"),
    ]
    return SolutionAssessment("Harbor Fitness membership-freeze workflow", alternatives, questions)


def main() -> None:
    assessment = build_assessment()
    print("CHAPTER 12 — CHOOSE THE SIMPLEST SENSIBLE SOLUTION")
    print("FICTIONAL TRAINING SCENARIO\nNOT A REAL CUSTOMER RECOMMENDATION")
    print("\nSECTION 1 — Qualified Harbor Fitness problem\n" + PROBLEM)
    print("Chapter 11 actually concluded MORE_EVIDENCE_REQUIRED; this comparison is provisional, not an override.")
    print("\nSECTION 2 — Solution hierarchy")
    print("\n→ ".join(path.name.replace("_", " ") for path in SolutionPath))
    print("This is a preference for simplicity when adequate, not a ladder and not cheapest-wins.")
    print("\nSECTION 3 — Generate Harbor alternatives")
    for letter, item in zip("ABCDE", assessment.alternatives):
        print(f"{letter}. {item.name} [{item.solution_path.name}]\n   Potential: {item.description}\n   Key unknown: {item.unresolved_questions[0]}")
    print("\nSECTION 4 — Capability questions")
    for question in assessment.capability_questions:
        print(f"- {question.system}: {question.capability} — {question.current_status.name}; validate via {question.validation_method}.")
    print("\nSECTION 5 — Compare alternatives")
    for item in assessment.alternatives:
        print(f"\nAlternative: {item.name}\nPath: {item.solution_path.name}\nProblem coverage: {item.problem_coverage}"
              f"\nImplementation complexity: {item.implementation_complexity.name}\nRelative cost: {item.estimated_cost_category.name}"
              f"\nTime to value: {item.estimated_time_category.name}\nPolicy fit: {item.policy_fit}"
              f"\nVendor dependency: {item.vendor_dependency}\nMaintainability: {item.maintainability}"
              f"\nCustomer change burden: UNKNOWN\nCritical assumption: {item.assumptions[0].assumption}"
              f"\nDecision: {item.status.name}\n---")
    print("Qualitative categories compare directions; they are not factual project estimates.")
    print("\nSECTION 6 — Reject premature custom build")
    print("‘We need a member portal’ names an implementation, not evidence that configuration, integration, or automation is inadequate. Custom build is NOT CURRENTLY JUSTIFIED.")
    print("\nSECTION 7 — Preferred current direction")
    print("Decision:", assessment.decision.name)
    print("Investigate CONFIGURE and then supported INTEGRATE/AUTOMATE capabilities before custom build. No final path is selected.")
    print("\nSECTION 8 — What would change the decision?")
    print("- Supported native workflow → CONFIGURE becomes strong.")
    print("- No native capability but suitable APIs/events → INTEGRATE/AUTOMATE becomes stronger.")
    print("- Critical capabilities and interfaces absent, with all custom-build gates supported → CUSTOM_BUILD becomes plausible.")
    print("- Burden remains too small for sensible intervention → LEAVE_ALONE.")
    print("No project has been priced. No ROI has been calculated. No proposal has been issued. No implementation technology has been selected.")


if __name__ == "__main__":
    main()
