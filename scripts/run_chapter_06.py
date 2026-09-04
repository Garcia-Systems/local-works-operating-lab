"""Run Chapter 6's fictional Digital Friction Audit."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.audit import (  # noqa: E402
    AffectedParty as Party, AuditFinding, AuditRecommendation, Confidence,
    DigitalFrictionAudit, EvidenceSource as Source, FindingDisposition as Disposition,
    Frequency, FrictionObservation, FrictionType, JourneyStage as Stage, Severity,
)


def finding(title, stage, fact, hypothesis, parties, sources, disposition, reasoning,
            known=(), unknowns=(), questions=(), frequency=Frequency.UNKNOWN,
            severity=Severity.UNKNOWN, confidence=Confidence.LIMITED,
            friction_types=(), workaround=None, business_objective=None,
            policy_reason=None, tradeoff=None):
    return AuditFinding(title, FrictionObservation(
        stage, parties, fact, hypothesis, sources, frequency, severity, workaround,
        unknowns, questions, confidence, business_objective=business_objective,
        policy_or_regulatory_reason=policy_reason, potential_tradeoff=tradeoff,
    ), friction_types, disposition, reasoning, known)


def harbor_audit() -> DigitalFrictionAudit:
    findings = (
        finding("Clear location discovery", Stage.FIND,
                "The fictional site presents the address, hours, map, and phone number together.",
                None, (Party.CUSTOMER,), (Source.PUBLIC_WEBSITE,), Disposition.WORKING_ADEQUATELY,
                ("The needed public information is directly visible.",),
                ("Location and opening information is available.",),
                ("Whether listings remain accurate elsewhere",), ("How often are directions questions received?",),
                severity=Severity.LOW),
        finding("Membership comparison", Stage.UNDERSTAND,
                "Membership names and headline prices are published, but joining fees and freeze terms are not explained on the comparison page.",
                "Prospects may need staff help to understand the full commitment.",
                (Party.CUSTOMER, Party.EMPLOYEE), (Source.PUBLIC_WEBSITE,), Disposition.NEEDS_MORE_EVIDENCE,
                ("Missing terms are observable; resulting questions and burden are not.",),
                ("Headline prices are public.",), ("question volume", "whether terms appear later in joining"),
                ("Which membership questions repeatedly require explanation?",),
                friction_types=(FrictionType.UNCLEAR_INFORMATION,)),
        finding("Useful tour conversation", Stage.CONTACT,
                "Prospective members may request an optional staffed tour by phone or email.",
                "The conversation may be valuable human guidance rather than avoidable friction.",
                (Party.CUSTOMER, Party.EMPLOYEE), (Source.PUBLIC_WEBSITE,), Disposition.WORKING_ADEQUATELY,
                ("Contact is optional.", "A tailored tour can be part of service."),
                ("Two contact channels are offered.",), ("tour response time",),
                ("Do prospects value the conversation?",), severity=Severity.LOW),
        finding("Clean join form, hidden re-entry", Stage.BOOK_OR_JOIN,
                "A fictional employee demonstration shows that staff copy completed online join forms into a separate membership system.",
                "Manual re-entry may consume employee time and introduce errors although customers see a clean flow.",
                (Party.EMPLOYEE, Party.MANAGER), (Source.SYSTEM_DEMONSTRATION, Source.EMPLOYEE_STATEMENT),
                Disposition.WORTH_INVESTIGATING,
                ("Internal demonstration corroborates the manual step.", "Frequency and effort still need measurement."),
                ("The customer can submit online.", "Staff re-enter the submission."),
                ("weekly volume", "handling time", "error rate", "system constraints"),
                ("How often is data copied, how long does it take, and what errors occur?",),
                frequency=Frequency.FREQUENT, severity=Severity.MODERATE,
                confidence=Confidence.CORROBORATED,
                friction_types=(FrictionType.MANUAL_DATA_ENTRY, FrictionType.DISCONNECTED_SYSTEMS)),
        finding("Card payment", Stage.PAY,
                "The fictional membership flow accepts card payment and displays a confirmation.",
                None, (Party.CUSTOMER,), (Source.PUBLIC_MEMBERSHIP_FLOW,),
                Disposition.WORKING_ADEQUATELY, ("The observed public path completes without an evident obstacle.",),
                ("A confirmation is displayed.",), ("failure handling", "staff reconciliation"),
                ("What happens after failed or disputed payments?",), severity=Severity.LOW),
        finding("Payment reconciliation not externally observable", Stage.PAY,
                "The public payment confirmation does not reveal the employee reconciliation workflow.",
                "Staff may or may not perform manual exception work; no claim can yet be made.",
                (Party.EMPLOYEE, Party.MANAGER), (Source.PUBLIC_MEMBERSHIP_FLOW,),
                Disposition.UNKNOWN_INTERNAL,
                ("Public evidence cannot establish the internal workflow.",),
                ("A customer confirmation is visible.",),
                ("reconciliation steps", "failure volume", "manual effort", "error rate"),
                ("Please demonstrate settlement, failures, refunds, and reconciliation.",),
                friction_types=(FrictionType.OTHER,), confidence=Confidence.UNKNOWN),
        finding("Friendly check-in", Stage.RECEIVE_SERVICE,
                "Members check in with a staffed welcome desk using a membership card.",
                "A staffed greeting may be intentional hospitality, not an automation opportunity.",
                (Party.CUSTOMER, Party.EMPLOYEE), (Source.DIRECT_WORKFLOW_OBSERVATION,),
                Disposition.WORKING_ADEQUATELY, ("No delay or duplicate work was observed.",),
                ("Observed check-ins proceeded normally.",), ("peak-time wait data",),
                ("Are there recurring peak-time exceptions?",), severity=Severity.LOW),
        finding("Routine membership changes", Stage.MANAGE,
                "The fictional public site says freezes and cancellations require contacting the front desk.",
                "Routine requests may inconvenience members and create employee administration.",
                (Party.CUSTOMER, Party.EMPLOYEE, Party.MANAGER), (Source.PUBLIC_WEBSITE,),
                Disposition.WORTH_INVESTIGATING,
                ("Required contact is known.", "Burden and the merits of the policy remain unknown."),
                ("Public instructions require staff contact.",),
                ("request frequency", "handling time", "member satisfaction", "billing implications", "software capability"),
                ("Why is contact required, and what happens from request through billing?",),
                friction_types=(FrictionType.UNNECESSARY_CALL, FrictionType.REPETITIVE_ADMINISTRATION),
                business_objective="Offer retention help before cancellation.",
                policy_reason="No contractual or regulatory requirement has been established.",
                tradeoff="Member control may conflict with a useful retention conversation."),
        finding("Rare identity-protected correction", Stage.MANAGE,
                "A legal-name correction requires a call and identity documentation.",
                "The call initially appears inconvenient.",
                (Party.CUSTOMER, Party.EMPLOYEE), (Source.PUBLIC_DOCUMENT, Source.MANAGER_STATEMENT),
                Disposition.LOW_SIGNIFICANCE,
                ("Additional fictional manager evidence says requests are extremely rare.",
                 "Identity verification is required, so changing this path has little apparent value."),
                ("The process is rare.", "Identity verification is required."),
                ("exact annual count",), ("Has this process produced complaints or errors?",),
                frequency=Frequency.RARE, severity=Severity.LOW, confidence=Confidence.CORROBORATED,
                friction_types=(FrictionType.UNNECESSARY_CALL,), workaround="Brief assisted verification",
                policy_reason="Identity verification is required."),
        finding("Return visit history", Stage.RETURN,
                "A returning member can use the existing membership card without completing intake again.",
                None, (Party.CUSTOMER,), (Source.DIRECT_WORKFLOW_OBSERVATION,),
                Disposition.WORKING_ADEQUATELY, ("No repeated intake was observed.",),
                ("Observed returning members resumed normally.",), ("exception handling",),
                ("Which exceptions require staff rework?",), severity=Severity.LOW),
    )
    return DigitalFrictionAudit("Harbor Fitness", tuple(Stage), findings,
        AuditRecommendation.DISCOVERY_RECOMMENDED,
        ("Corroborated manual join-form re-entry deserves internal investigation.",
         "Membership-change burden and policy tradeoffs need evidence.",
         "Several stages work adequately, so no broad transformation is justified."), True)


def main() -> None:
    audit = harbor_audit()
    print("CHAPTER 6 — THE DIGITAL FRICTION AUDIT")
    print("FICTIONAL TRAINING SCENARIO\nNOT A REAL LOCAL WORKS CUSTOMER")
    for item in audit.findings:
        o = item.observation
        print(f"\nJourney stage: {o.journey_stage.name}\nFinding: {item.title}")
        print(f"Observed information: {o.observed_fact}")
        print(f"Possible friction: {o.friction_hypothesis or 'None observed.'}")
        print("Affected party: " + ", ".join(p.value for p in o.affected_parties))
        print("Evidence source: " + ", ".join(s.value for s in o.evidence_sources))
        print("Known: " + ("; ".join(item.known_facts) or "No additional facts."))
        print("Unknown: " + ("; ".join(o.unknowns) or "None recorded."))
        print("Follow-up question: " + ("; ".join(o.follow_up_questions) or "None."))
        print(f"Current significance: {item.disposition.value}; Frequency: {o.frequency.value}; Severity: {o.severity.value}")
    print("\nSUMMARY")
    for disposition in Disposition:
        names = [f.title for f in audit.findings_by_disposition(disposition)]
        print(f"{disposition.value}: " + (", ".join(names) or "None"))
    print(f"\nAUDIT RECOMMENDATION: {audit.recommendation.name}")
    for reason in audit.recommendation_reasoning:
        print(f"- {reason}")
    print("DISCOVERY RECOMMENDED does not mean PROJECT RECOMMENDED.")
    print("No financial impact, technical solution, or custom software recommendation is established.")


if __name__ == "__main__":
    main()
