"""Run Chapter 7's deterministic, fictional opportunity-gate exercise."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.hypothesis import EvidenceType  # noqa: E402
from local_works.opportunities import (  # noqa: E402
    DimensionRating as Rating, OpportunityAssessment, OpportunityCandidate,
    OpportunityDecision as Decision, OpportunityDimension as Dimension, signal,
)
from run_chapter_06 import harbor_audit  # noqa: E402


def candidate(name, *titles):
    audit = harbor_audit()
    findings = tuple(f for f in audit.findings if f.title in titles)
    return OpportunityCandidate.group(
        name, name, findings,
        "Related workflow steps may create customer inconvenience and repetitive staff work.",
        "The selected findings concern the same named business workflow."
    ) if len(findings) > 1 else OpportunityCandidate.from_finding(
        name, name, findings[0], "The observed condition may create avoidable workflow burden."
    )


def make_assessment(label, decision, problem, commercial, positives=(), negatives=(),
                    unknowns=(), disqualifiers=(), reason="", action=""):
    item = candidate(label, "Routine membership changes")
    dimensions = {
        Dimension.FREQUENCY: signal(Dimension.FREQUENCY,
            "Frequency is known." if "request frequency" not in unknowns else "Request frequency is unknown.",
            Rating.MODERATE if "request frequency" not in unknowns else Rating.UNKNOWN,
            EvidenceType.OBSERVED if "request frequency" not in unknowns else EvidenceType.HYPOTHESIS),
        Dimension.ECONOMIC_PLAUSIBILITY: signal(Dimension.ECONOMIC_PLAUSIBILITY,
            "Potentially worth measuring; economics are not quantified.", Rating.MODERATE),
        Dimension.AUTHORITY: signal(Dimension.AUTHORITY, "Sponsor access is assessed separately.", commercial),
    }
    return OpportunityAssessment(item, dimensions, problem, commercial, positives, negatives,
                                 unknowns, disqualifiers, decision, (reason,), (), action)


def show(title, item):
    finding_titles = "; ".join(f.title for f in item.candidate.source_findings)
    evidence = "; ".join(f.observation.observed_fact for f in item.candidate.source_findings)
    rows = (
        ("Finding", finding_titles), ("Workflow", item.candidate.workflow), ("Evidence", evidence),
        ("Positive signals", "; ".join(item.positive_signals) or "None recorded"),
        ("Negative signals", "; ".join(item.negative_signals) or "None recorded"),
        ("Unknowns", "; ".join(item.unknowns) or "None material"),
        ("Disqualifiers", "; ".join(item.hard_disqualifiers) or "None"),
        ("Problem potential", item.problem_potential.value), ("Commercial fit", item.commercial_fit.value),
        ("Decision", item.decision.name), ("Reason", " ".join(item.rationale)),
        ("Next action", item.next_action),
    )
    print(f"\n{title}")
    for key, value in rows:
        print(f"{key}: {value}")


def main():
    print("CHAPTER 7 — FROM AUDIT TO OPPORTUNITY\nFictional training exercise; not customer results.")
    print("\nSECTION 1 — THE OPPORTUNITY GATE")
    print("Friction → Assessment → Opportunity Decision")
    print("An audit identifies apparent friction. Assessment tests significance and engagement fit. "
          "A decision controls whether more Local Works time is justified.")

    print("\nSECTION 2 — EVALUATE FINDINGS")
    cases = (
        ("A. Strong candidate for discovery", Decision.DISCOVERY_WARRANTED, Rating.STRONG, Rating.STRONG,
         ("Repeated staff intervention is plausible.", "Multiple parties are affected."), (), (), (),
         "Corroborated workflow evidence makes focused discovery proportionate.", "Run bounded discovery; do not select a solution."),
        ("B. More information needed", Decision.MORE_INFORMATION_NEEDED, Rating.MODERATE, Rating.MODERATE,
         ("The staff-contact rule is visible.",), (), ("request frequency", "authority"), (),
         "Critical workload and sponsor evidence is absent.", "Ask the blocking questions."),
        ("C. Simple improvement", Decision.SIMPLE_IMPROVEMENT, Rating.WEAK, Rating.STRONG,
         ("Existing SaaS self-service is already enabled.",), ("Only instructions are outdated.",), (), (),
         "Correcting instructions is obvious, bounded, and low risk.", "Update and verify the instructions; skip discovery."),
        ("D. Leave alone", Decision.LEAVE_ALONE, Rating.WEAK, Rating.STRONG,
         ("The five-minute transfer friction is real.",), ("It occurs about twice per year.",), (), (),
         "Established burden is negligible.", "Leave the workflow alone."),
        ("E. Refer elsewhere", Decision.REFER_ELSEWHERE, Rating.STRONG, Rating.MODERATE,
         ("A valid urgent concern exists.",), ("It is primarily a cybersecurity incident.",), (), (),
         "Specialist incident response is the appropriate capability.", "Refer to a qualified cybersecurity responder."),
        ("F. Disqualify", Decision.DISQUALIFY, Rating.STRONG, Rating.WEAK,
         ("The underlying friction may be real.",), (), (), ("Prospect demands misrepresentation.",),
         "Engagement conditions are inappropriate regardless of problem size.", "Stop pursuit."),
    )
    made = []
    for values in cases:
        title, decision, problem, commercial, pos, neg, unknown, dq, reason, action = values
        item = make_assessment(title[3:], decision, problem, commercial, pos, neg, unknown, dq, reason, action)
        made.append(item); show(title, item)

    print("\nSECTION 3 — GROUP RELATED FINDINGS")
    grouped = candidate("Membership Account Management", "Routine membership changes", "Clean join form, hidden re-entry")
    print("Grouped:", "; ".join(f.title for f in grouped.source_findings))
    print("Why: both may be manifestations of membership-account administration across customer and staff steps.")
    print("Not grouped: Membership comparison — it concerns prospect understanding before account management, "
          "so relation has not been established.")

    print("\nSECTION 4 — PROBLEM FIT VS COMMERCIAL FIT")
    print("Scenario A: STRONG problem / WEAK commercial fit → seek appropriate authority; do not pursue locally.")
    print("Scenario B: MODERATE problem / STRONG commercial access → access does not make the burden meaningful.")
    print("Scenario C: STRONG problem / STRONG commercial fit → DISCOVERY_WARRANTED, not a project approval.")

    print("\nSECTION 5 — UNKNOWNS")
    print("With corroborated frequency, impact, and sponsor access: DISCOVERY_WARRANTED")
    print("Remove frequency, impact, and authority evidence: MORE_INFORMATION_NEEDED")
    print("UNKNOWN stays UNKNOWN; it never silently becomes LOW, NO BUDGET, or IMPOSSIBLE.")

    print("\nSECTION 6 — INTERPRETATION")
    for question in ("What makes friction worth deeper investigation?", "Which unknowns are blocking decisions?",
        "Are multiple symptoms part of one workflow?", "Is the problem potentially economically meaningful?",
        "Is Local Works actually positioned to investigate it?", "Is there an easier response than discovery?",
        "Should Local Works walk away?"):
        print("-", question)


if __name__ == "__main__":
    main()
