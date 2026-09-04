#!/usr/bin/env python3
"""Demonstrate manual Validation Sprint 1 records without external activity."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.audit import JourneyStage
from local_works.capstone import assess_final_business
from local_works.validation import (
    AuditDecision, DigitalFrictionAudit, FrictionType, JourneyReview,
    OUTREACH_TEMPLATES, Rating, SPRINT_FAILURE_SIGNALS,
    SPRINT_SUCCESS_SIGNALS, SolutionPath, TargetDimension,
    ValidationEvidence, ValidationHypothesis, ValidationObservation,
    ValidationTarget, ValidationTargetScore,
)

FICTIONAL_NOTICE = "FICTIONAL DEMONSTRATION"


def fictional_example() -> tuple[ValidationTarget, DigitalFrictionAudit]:
    ratings = {
        TargetDimension.PUBLIC_JOURNEY_VISIBILITY: Rating.HIGH,
        TargetDimension.FRICTION_OBSERVABILITY: Rating.HIGH,
        TargetDimension.BUSINESS_VALUE_POTENTIAL: Rating.UNKNOWN,
        TargetDimension.DECISION_MAKER_REACHABILITY: Rating.MEDIUM,
        TargetDimension.SOLUTION_FLEXIBILITY: Rating.UNKNOWN,
        TargetDimension.FIRST_PROJECT_SAFETY: Rating.MEDIUM,
        TargetDimension.LEARNING_VALUE: Rating.HIGH,
    }
    target = ValidationTarget(
        "Harbor Fitness", "Fitness studio", "https://example.invalid/harbor",
        "One fictional location", "Visible joining and membership journey",
        ValidationTargetScore(ratings), is_fictional=True,
    )
    observation = ValidationObservation(
        observation="The fictional membership page says members must call to cancel.",
        inference="This may create front-desk administrative work.",
        unknown="The number and handling time of membership-change calls.",
        discovery_question="How many membership-change calls does the front desk handle in a typical week?",
        friction=FrictionType.REQUIRES_PHONE_CALL,
        public_evidence="Fictional membership-page copy created only for this demonstration.",
    )
    journey = (
        JourneyReview(JourneyStage.FIND, "Location and hours are visible.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "Fictional location page."),
        JourneyReview(JourneyStage.UNDERSTAND, "Membership options are described.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "Fictional membership page."),
        JourneyReview(JourneyStage.CONTACT, "Phone and email are listed.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "Fictional contact page."),
        JourneyReview(JourneyStage.BOOK_OR_JOIN, "A fictional online joining path is shown.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "Fictional joining page."),
        JourneyReview(JourneyStage.PAY, "Payment behavior is not demonstrated.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "No transaction performed.", "How payment failures are handled.", "", "How are payment failures handled?"),
        JourneyReview(JourneyStage.RECEIVE_SERVICE, "Internal service delivery is not public.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "No public evidence.", "How intake reaches staff.", "", "How does new-member information reach staff?"),
        JourneyReview(JourneyStage.MANAGE, observation.observation, FrictionType.REQUIRES_PHONE_CALL, observation.public_evidence, observation.unknown, observation.inference, observation.discovery_question),
        JourneyReview(JourneyStage.RETURN, "Return experience is not publicly established.", FrictionType.NO_MEANINGFUL_PUBLIC_FRICTION_FOUND, "No public evidence.", "Whether returning members repeat information.", "", "What must a returning member provide again?"),
    )
    audit = DigitalFrictionAudit(
        target, journey, (observation,), AuditDecision.WORTH_DISCOVERY,
        "One directly visible constraint raises a bounded question about frequency and staff burden.",
        (ValidationHypothesis("If call volume and handling time are substantial, self-service may create recoverable administrative capacity."),),
        SolutionPath.UNKNOWN,
    )
    return target, audit


def main() -> None:
    exam = assess_final_business()
    gap = exam.evidence_gaps[0]  # repository-derived CRITICAL_NEXT priority
    target, audit = fictional_example()
    finding = audit.observations[0]
    ledger = ValidationEvidence(gap.current_assumption, "48% qualified; 42% close", "Chapter 32 fictional simulation")

    print("LOCAL WORKS VALIDATION SPRINT 1")
    print("\nTHE DEMONSTRATION DATA BELOW IS FICTIONAL.")
    print("REAL VALIDATION DATA MUST BE ENTERED ONLY AFTER ACTUAL RESEARCH OR BUSINESS INTERACTION.")
    print(f"\n{FICTIONAL_NOTICE}")
    print(f"\n1. FINAL LAB EVIDENCE GAP\n[{gap.validation_priority.name}] {gap.question}\nAssumption: {gap.current_assumption}\nSensitivity: {gap.sensitivity}\nMethod: {gap.validation_method}")
    print(f"\n2. TARGET SCORING EXAMPLE — {target.name} (FICTIONAL)\n" + "\n".join(f"- {d.name}: {target.score.ratings[d].name}" for d in TargetDimension) + f"\nVerdict: {target.score.verdict.name} (UNKNOWN is preserved)")
    print("\n3. PUBLIC CUSTOMER JOURNEY AUDIT EXAMPLE\n" + "\n".join(f"- {j.stage.name}: {j.observed_experience} | {j.friction.name}" for j in audit.journey))
    print(f"\n4. OBSERVATION VS INFERENCE\nObservation: {finding.observation}\nInference: {finding.inference}\nUnknown: {finding.unknown}")
    print(f"\n5. DISCOVERY QUESTIONS\n- {finding.discovery_question}")
    print(f"\n6. AUDIT VERDICT\n{audit.decision.name}: {audit.decision_reason}\nSolution path: {audit.solution_path.name}\nValue hypothesis: {audit.value_hypotheses[0].status} — {audit.value_hypotheses[0].statement}")
    outreach_observation = finding.observation.rstrip(".").lower()
    print("\n7. OUTREACH TEMPLATE — PREPARATION ONLY; NOTHING IS SENT\n" + OUTREACH_TEMPLATES["EMAIL"].format(name="[decision maker]", business=target.name, observation=outreach_observation))
    print(f"\n8. EVIDENCE-LEDGER PROCESS\nOriginal: {ledger.original_value} ({ledger.evidence_status}). Record real provenance, denominator, result, date, and time. No update occurs without evidence.")
    print("\n9. SPRINT SUCCESS LOGIC\n" + "\n".join(f"- {x}" for x in SPRINT_SUCCESS_SIGNALS))
    print("\nSPRINT FAILURE LOGIC (VALUABLE RESULTS)\n" + "\n".join(f"- {x}" for x in SPRINT_FAILURE_SIGNALS))
    print("\n10. REPLACE THE EXAMPLE\nManually research five real targets; record URLs/dates and UNKNOWN ratings; complete three public-only audits; prepare and manually decide on up to three outreach attempts; log each stage and actual minutes; then update the ledger only from attributable real evidence. Never copy Harbor Fitness into the real log.")


if __name__ == "__main__":
    main()
