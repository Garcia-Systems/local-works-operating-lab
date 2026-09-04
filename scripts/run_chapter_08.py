"""Run Chapter 8's deterministic, fictional discovery session."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.discovery import (  # noqa: E402
    CauseType, DiscoveredSystem, DiscoveryAnswer, DiscoveryFinding,
    DiscoveryOutcome, DiscoveryQuestion, DiscoveryQuestionCategory as Category,
    DiscoverySession, EvidenceConflict, EvidenceKind, EvidenceValue,
)

HYPOTHESIS = ("Routine membership-account creation and changes appear to require staff "
              "intervention and, in at least the demonstrated join path, entry into a "
              "separate system. This may create member inconvenience and repetitive "
              "administrative work.")


def build_session() -> DiscoverySession:
    session = DiscoverySession(HYPOTHESIS)

    def answer(category, question, participant, statement, value=None, unit="", kind=EvidenceKind.CUSTOMER_STATEMENT, notes=""):
        evidence = EvidenceValue(value, unit, participant, kind, notes) if value is not None or kind is EvidenceKind.UNKNOWN else None
        return session.add_answer(DiscoveryAnswer(DiscoveryQuestion(question, category), participant, statement, evidence))

    # Manager evidence: policy changes the interpretation of the audit observation.
    answer(Category.CURRENT_STATE, "Walk me through a membership freeze.", "Owner / general manager",
           "A member contacts the front desk; staff check eligibility, obtain approval when needed, update the membership platform, and send confirmation.")
    manager_frequency = answer(Category.FREQUENCY_VOLUME, "How often does that happen?", "Owner / general manager",
           "Probably about 8 freeze requests per week, but I have not checked a report.", 8, "requests/week", EvidenceKind.ESTIMATE)
    answer(Category.PEOPLE, "Who handles it?", "Owner / general manager",
           "Front-desk staff handle normal requests; the membership manager handles exceptions.")
    answer(Category.TIME_BURDEN, "How long does a normal request take?", "Owner / general manager",
           "I think a normal request takes about five minutes.", 5, "minutes/request", EvidenceKind.ESTIMATE)
    answer(Category.ERRORS_EXCEPTIONS, "What makes a request complicated?", "Owner / general manager",
           "An overdue balance or a medical-freeze request can require manager review.")
    policy = answer(Category.POLICY, "Why is staff approval required?", "Owner / general manager",
           "We intentionally require review because eligibility depends on membership type and some exceptions need approval.")
    answer(Category.SYSTEMS, "What systems are involved?", "Owner / general manager",
           "The membership platform, staff email, and sometimes a spreadsheet.")
    answer(Category.ERRORS_EXCEPTIONS, "What happens if something is entered incorrectly?", "Owner / general manager",
           "Staff correct the membership record and may need to explain an unexpected charge; correction frequency is unknown.")
    answer(Category.URGENCY, "Why would you want this process improved?", "Owner / general manager",
           "Staff interruptions are frustrating, but we have not quantified their effect and there is no fixed deadline.")
    answer(Category.SUCCESS_CRITERIA, "What would success look like?", "Owner / general manager",
           "Fewer repetitive steps and clear member status while preserving eligibility review.")
    answer(Category.AUTHORITY, "Who could approve further analysis?", "Owner / general manager",
           "I can approve a bounded analysis; no implementation has been approved.")
    answer(Category.BUDGET, "Is funding available for a change?", "Owner / general manager",
           "No budget has been set; we would need evidence that the problem matters.", None, "", EvidenceKind.UNKNOWN)

    # Employee evidence overlaps rather than replacing the manager's account.
    employee_frequency = answer(Category.FREQUENCY_VOLUME, "How often do you handle freeze requests?", "Front-desk employee",
           "It feels closer to 3 or 4 most weeks, with seasonal spikes.", "3–4", "requests/week", EvidenceKind.ESTIMATE)
    answer(Category.CURRENT_STATE, "Walk me through what you do.", "Front-desk employee",
           "I read the email or take the call, look up the account, check notes, ask the manager if eligibility is unclear, update the platform, note the spreadsheet, and reply.")
    answer(Category.TIME_BURDEN, "How long does it take?", "Front-desk employee",
           "Simple requests may take five minutes, but an overdue balance can take 15 to 20. We have never timed them.", "5; 15–20 exception", "minutes/request", EvidenceKind.ESTIMATE)
    answer(Category.ERRORS_EXCEPTIONS, "What happens when it does not go normally?", "Front-desk employee",
           "An overdue balance or missing membership notes means I stop and ask the membership manager.")
    answer(Category.CUSTOMER_IMPACT, "Do members abandon or complain because of this?", "Front-desk employee",
           "A few have asked why approval is needed, but I do not know how many abandon.", None, "", EvidenceKind.UNKNOWN)

    session.findings.extend([
        DiscoveryFinding("Freeze review", "Staff involvement is at least partly an intentional eligibility policy, not established technical incapability.", (policy,), CauseType.BUSINESS_POLICY),
        DiscoveryFinding("Feature request", "A portal or app has not been validated as the problem or selected as a solution.", (), CauseType.UNKNOWN, False),
    ])
    session.record_conflict(EvidenceConflict(
        "Weekly freeze frequency", (manager_frequency, employee_frequency),
        "How many freeze requests occur in a representative week/month?",
        "Membership change logs for a representative period"))
    session.request_evidence("Representative freeze-request volume", "Membership change logs by month", "How frequent and seasonal are requests?")
    session.request_evidence("Employee handling time", "Observe or sample 20 normal and exception requests", "How much staff time is involved?")
    session.request_evidence("Customer complaints or abandonment", "Review categorized support inbox messages", "What customer impact occurs?")
    session.request_evidence("Correction rate", "Review correction records or billing exceptions", "How often do entry errors create rework?")
    session.systems.extend([
        DiscoveredSystem("Membership Management Platform", "Membership records and status", ("Front desk", "Membership manager"), "Eligibility review and status update", unknown_capabilities=("Available self-service and rule configuration",), owner_vendor="UNKNOWN", access_constraints=("Access not assessed",)),
        DiscoveredSystem("Staff Email", "Receive requests and send confirmations", ("Front desk",), "Request intake and response", unknown_capabilities=("Reliable request categorization",), owner_vendor="Business-managed"),
        DiscoveredSystem("Spreadsheet", "Supplemental tracking", ("Front desk", "Membership manager"), "Manual note/tracking step", unknown_capabilities=("Completeness and authoritative status",), owner_vendor="Business-managed"),
    ])
    session.revised_understanding = ("Certain membership freezes require policy-dependent staff review, and staff appear to perform "
        "several manual administrative steps across systems. Frequency, total handling burden, errors, and customer impact remain unmeasured.")
    session.outcome = DiscoveryOutcome.MORE_EVIDENCE_REQUIRED
    return session


def main() -> None:
    session = build_session()
    print("CHAPTER 8 — DISCOVERY\nFICTIONAL TRAINING SCENARIO\nNOT A REAL CUSTOMER INTERVIEW")
    print("\nSECTION 1 — Starting hypothesis\n" + session.opportunity_hypothesis)
    for heading, participant in (("SECTION 2 — Manager interview", "Owner / general manager"), ("SECTION 3 — Employee interview", "Front-desk employee")):
        print("\n" + heading)
        for item in (a for a in session.answers if a.participant == participant):
            provenance = f" [{item.evidence.kind.name}: {item.evidence.value} {item.evidence.unit}]" if item.evidence else " [CUSTOMER_STATEMENT]"
            print(f"Q: {item.question.text}\nA: {item.statement}{provenance}")
    print("\nSECTION 4 — Follow the workflow")
    print("Contact → account lookup → eligibility/notes check → exception approval when needed → platform update → supplemental note → confirmation")
    print("Emerging outline only; Chapter 9 has not reconstructed the formal workflow.")
    print("\nSECTION 5 — Contradictions and unknowns")
    print("Confirmed: staff review reflects an eligibility policy; multiple systems participate.")
    print("Estimated: manager says ~8/week and ~5 minutes; employee says ~3–4/week, with 15–20 minute exceptions.")
    print("Conflicting: weekly frequency estimates disagree; neither is averaged or promoted to fact.")
    print("Unknown: measured volume/time, correction rate, abandonment, platform capabilities, and budget.")
    print("\nSECTION 6 — Revised problem understanding")
    print("BEFORE DISCOVERY:\nMembers cannot self-manage account changes.")
    print("AFTER DISCOVERY:\n" + session.revised_understanding)
    print("\nEvidence requests:")
    for request in session.evidence_requests:
        print(f"- Need: {request.need} | Possible evidence: {request.possible_evidence}")
    print("\nSECTION 7 — Discovery decision")
    print(session.outcome.name)
    print("No technical solution selected. No project approved. No financial value established.")


if __name__ == "__main__":
    main()
