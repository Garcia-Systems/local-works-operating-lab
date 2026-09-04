"""Run Chapter 14's deterministic, fictional engagement-scope exercise."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.scope import (AcceptanceCriterion, AssumptionStatus, CustomerResponsibility,
    DeliveryResponsibility, LocalWorksResponsibility, Priority, ProjectScope, RequestDisposition,
    ScopeAssumption, ScopeBoundary, ScopeDependency, ScopeExclusion, ScopeItem, ScopeRisk,
    ScopeRiskCategory, ScopedSystem, SystemClassification)


def harbor_scope() -> ProjectScope:
    return ProjectScope(
        "Harbor Fitness", "Reduce repeated handling of membership-freeze requests",
        "Designed to reduce administrative work in the membership-freeze workflow while preserving eligibility rules and manager approval for exceptions.",
        "Eligible freeze requests require repeated front-desk and manager handling.",
        "Validate whether bounded configuration of the existing platform can support request capture, rules, exception review, status, and confirmation.",
        ScopeBoundary("A member submits a freeze request for a defined membership type.",
                      "The request is approved or rejected, the decision is recorded, and confirmation is sent."),
        [ScopeItem(x) for x in ("Membership-freeze request workflow", "Required-data capture",
            "Eligibility determination using customer-approved rules", "Manager routing for exceptions",
            "Decision recording", "Confirmation communication")],
        [ScopeExclusion(x) for x in ("Membership cancellation", "Payment disputes", "Refunds",
            "Membership upgrades or downgrades", "Full account management", "Native mobile application",
            "Replacement membership platform")],
        actors=["Member", "Front desk employee", "Membership manager"],
        systems=[ScopedSystem("Existing membership platform", SystemClassification.UNKNOWN, "configuration target if capability is validated"),
                 ScopedSystem("Approved request mechanism", SystemClassification.IN_SCOPE, "request entry"),
                 ScopedSystem("Payment processor", SystemClassification.DEPENDENCY_ONLY, "membership status may depend on it; no modification"),
                 ScopedSystem("Accounting platform", SystemClassification.OUT_OF_SCOPE)],
        functional_requirements=[
            ScopeItem("Capture required request information", Priority.MUST),
            ScopeItem("Preserve approved eligibility rules", Priority.MUST),
            ScopeItem("Route exceptions to an authorized manager", Priority.MUST),
            ScopeItem("Record the approval outcome", Priority.MUST),
            ScopeItem("Send confirmation automatically", Priority.SHOULD),
            ScopeItem("Provide a manager status view", Priority.COULD),
            ScopeItem("Provide a native mobile application", Priority.NOT_IN_SCOPE)],
        non_functional_considerations=["Least-privilege temporary test access", "Usable request entry", "Auditable decision status", "Compatibility with validated vendor capabilities"],
        assumptions=[
            ScopeAssumption("Harbor can document eligibility and exception rules", "Rules define correct behavior", AssumptionStatus.CONFIRMED, "Requirements need clarification", evidence="Chapter 8/9 fictional discovery"),
            ScopeAssumption("The current subscription supports the required configuration", "It controls whether the preferred direction is feasible", AssumptionStatus.UNCONFIRMED, "Validate capability or revise the direction", critical=True)],
        dependencies=[
            ScopeDependency("Customer decision maker and approved business rules", "Harbor Fitness", AssumptionStatus.CONFIRMED, "Acceptance cannot be defined", critical=True),
            ScopeDependency("Vendor configuration capability and test access", "Harbor Fitness / platform vendor", AssumptionStatus.UNCONFIRMED, "A different solution or scope may be required", technical=True, critical=True)],
        customer_responsibilities=[CustomerResponsibility(x) for x in ("Provide approved rules and a decision maker", "Provide least-privilege test/admin access without emailing credentials", "Provide fictional or sanitized test data", "Review requirements and conduct acceptance testing", "Pay any approved third-party fees")],
        local_works_responsibilities=[LocalWorksResponsibility(x) for x in ("Translate discovery into requirements", "Coordinate capability validation and delivery", "Communicate status and coordinate QA and acceptance", "Coordinate documentation")],
        delivery_responsibilities=[DeliveryResponsibility(x) for x in ("Perform validated configuration or technical implementation", "Support testing and deployment", "Provide technical documentation")],
        acceptance_criteria=[
            AcceptanceCriterion("an eligible membership", "a freeze request is submitted", "required information is captured and the eligibility result is recorded"),
            AcceptanceCriterion("a request requiring an exception", "validation completes", "the request is routed to an authorized manager"),
            AcceptanceCriterion("a manager decision", "the request is approved or rejected", "status is recorded and the agreed confirmation is produced")],
        business_success_metrics=["Average staff handling time after an agreed observation period", "Share of routine requests completed without repeated handling"],
        data_required=["Member identifier", "Membership type", "Requested freeze dates", "Eligibility and approval status"],
        data_excluded=["Full payment-card data", "Passwords", "Unrelated member profile data"],
        risks=[ScopeRisk(ScopeRiskCategory.INTEGRATION_UNCERTAINTY, "Platform capability remains unknown", "HIGH", "Run bounded capability validation"),
               ScopeRisk(ScopeRiskCategory.POLICY_COMPLEXITY, "Exception rules may be incomplete", "MEDIUM", "Customer reviews rule set"),
               ScopeRisk(ScopeRiskCategory.THIRD_PARTY_DEPENDENCY, "Vendor behavior can change", "MEDIUM", "Document the supported boundary")])


def bullets(values: list[str]) -> None:
    for value in values: print(f"- {value}")


def main() -> None:
    scope = harbor_scope()
    scope.classify_request("Can we add cancellations too?", RequestDisposition.DEFERRED)
    scope.classify_request("Can members update credit cards?", RequestDisposition.CHANGE_LATER)
    scope.classify_request("Can we add family-account management?", RequestDisposition.DEFERRED)
    print("CHAPTER 14 — SCOPE THE ENGAGEMENT\nFICTIONAL TRAINING SCENARIO\nNOT A REAL STATEMENT OF WORK")
    print("\nSECTION 1 — Starting solution direction")
    print(f"Qualified problem: {scope.problem_statement}\nCurrent burden: Chapter 13 used an estimated $2,450/year labor-capacity burden; cash savings remain unestablished.\nPreferred solution direction: {scope.solution_direction}\nMajor unresolved assumptions: platform configuration capability and test access.")
    print(f"\nSECTION 2 — Business outcome\n{scope.business_outcome}")
    print(f"\nSECTION 3 — Workflow boundary\nTrigger: {scope.boundary.trigger}\nIncluded workflow: membership-freeze requests for defined membership types.\nEnd condition: {scope.boundary.end_condition}")
    print("\nSECTION 4 — Included / excluded\nINCLUDED:"); bullets([x.statement for x in scope.included]); print("EXCLUDED:"); bullets([x.statement for x in scope.excluded])
    print("\nSECTION 5 — Actors"); bullets(scope.actors)
    print("\nSECTION 6 — Systems"); bullets([f"{x.name}: {x.classification.name} — {x.role}" for x in scope.systems])
    print("\nSECTION 7 — Functional requirements")
    for priority, items in scope.requirements_by_priority.items(): print(priority.name + ": " + "; ".join(x.statement for x in items))
    print("\nSECTION 8 — Assumptions"); bullets([f"{x.status.name}: {x.statement}; if false: {x.impact_if_false}" for x in scope.assumptions])
    print("\nSECTION 9 — Dependencies"); bullets([f"{x.dependency} — owner {x.owner}; {x.status.name}" for x in scope.dependencies])
    print("\nSECTION 10 — Responsibilities")
    for heading, values in (("CUSTOMER", scope.customer_responsibilities), ("LOCAL WORKS", scope.local_works_responsibilities), ("DELIVERY TEAM (UNSELECTED)", scope.delivery_responsibilities)):
        print(heading + ":"); bullets([x.statement for x in values])
    print("\nSECTION 11 — Acceptance criteria"); bullets([f"Given {x.given}; when {x.when}; then {x.then}." for x in scope.acceptance_criteria])
    print("Business metrics are measured later and are not technical acceptance: " + "; ".join(scope.business_success_metrics))
    print("\nSECTION 12 — Scope-change examples"); bullets([f'“{x.request}” => {x.disposition.name}; it was not silently included.' for x in scope.change_requests])
    print("\nSECTION 13 — Risks"); bullets([f"{x.category.name} / {x.severity}: {x.description}; mitigation: {x.mitigation}" for x in scope.risks])
    print(f"\nSECTION 14 — Estimate-readiness gate\n{scope.estimate_readiness.name}\nValidate the critical vendor capability before implementation estimation.")
    print("\nSECTION 15 — Interpretation\nA smaller, explicit freeze workflow is safer and potentially more valuable than a vague membership-lifecycle project. Exclusions and new-request dispositions protect that boundary.")
    print("\nMINI-SCOPE EXAMPLES")
    print("EXAMPLE A — GOOD SMALL SCOPE: copy completed-job details into an invoice draft; exclude replacing scheduling/accounting => READY_FOR_ESTIMATE")
    print('EXAMPLE B — VAGUE SCOPE: “Fix our operations” => NEEDS_CUSTOMER_CLARIFICATION')
    print("EXAMPLE C — OVERLOADED SCOPE: CRM + website + mobile + payments + inventory + scheduling + analytics => NEEDS_SCOPE_REDUCTION")
    print("EXAMPLE D — TECHNICAL UNKNOWN: required vendor API capability unknown => NEEDS_TECHNICAL_VALIDATION")
    print("\nNo customer price, proposal, contract, or delivery partner has been created.")


if __name__ == "__main__":
    main()
