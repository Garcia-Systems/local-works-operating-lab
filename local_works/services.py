"""The small service-ladder model used by the Chapter 1 exercise."""

from dataclasses import dataclass
from enum import Enum


class ServiceStage(Enum):
    """What Local Works is doing at a point in the customer relationship."""

    AUDIT = "Digital Friction Audit"
    DISCOVERY = "Discovery"
    SOLUTION_DESIGN = "Solution Design"
    IMPLEMENTATION = "Implementation / Delivery"
    SUPPORT = "Support"
    CONTINUOUS_IMPROVEMENT = "Continuous Improvement / Account Development"


@dataclass(frozen=True)
class ServiceStageDefinition:
    stage: ServiceStage
    primary_purpose: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    implementation_required: bool
    project_must_result: bool
    exit_conditions: tuple[str, ...]


SERVICE_DEFINITIONS: dict[ServiceStage, ServiceStageDefinition] = {
    ServiceStage.AUDIT: ServiceStageDefinition(
        ServiceStage.AUDIT,
        "Identify meaningful friction in customer or employee workflows.",
        ("customer-reported concern", "initial workflow context"),
        ("friction observations", "recommended next step"),
        False,
        False,
        (
            "no meaningful issue",
            "issue is not worth solving",
            "simple configuration or process fix",
            "discovery recommended",
        ),
    ),
    ServiceStage.DISCOVERY: ServiceStageDefinition(
        ServiceStage.DISCOVERY,
        "Understand whether an economically sensible response exists.",
        ("audit findings", "stakeholder and workflow access", "known constraints"),
        ("validated problem statement", "economics and constraints", "decision brief"),
        False,
        False,
        ("no project", "solution design recommended", "more evidence required"),
    ),
    ServiceStage.SOLUTION_DESIGN: ServiceStageDefinition(
        ServiceStage.SOLUTION_DESIGN,
        "Determine the simplest sensible response to a validated problem.",
        ("validated problem", "economics", "systems and constraints"),
        ("recommended response", "alternatives and trade-offs", "delivery outline"),
        False,
        False,
        ("leave alone", "process change", "approved response", "no feasible response"),
    ),
    ServiceStage.IMPLEMENTATION: ServiceStageDefinition(
        ServiceStage.IMPLEMENTATION,
        "Execute an approved solution with appropriate leadership and coordination.",
        ("approved solution", "scope and acceptance criteria", "delivery resources"),
        ("delivered change", "quality evidence", "launch and handoff materials"),
        True,
        True,
        ("accepted delivery", "stopped engagement", "handoff to operations"),
    ),
    ServiceStage.SUPPORT: ServiceStageDefinition(
        ServiceStage.SUPPORT,
        "Help the customer operate a delivered solution after launch.",
        ("supported solution", "reported issue or question", "support boundaries"),
        ("triage or guidance", "issue coordination", "operational documentation"),
        False,
        False,
        ("issue resolved", "warranty referral", "new project identified"),
    ),
    ServiceStage.CONTINUOUS_IMPROVEMENT: ServiceStageDefinition(
        ServiceStage.CONTINUOUS_IMPROVEMENT,
        "Periodically identify additional improvements that pass value and economics tests.",
        ("operating experience", "new friction", "business priorities"),
        ("improvement observations", "value assessment", "recommended next step"),
        False,
        False,
        ("no worthwhile change", "audit or discovery recommended", "revisit later"),
    ),
}


def service_definition(stage: ServiceStage) -> ServiceStageDefinition:
    """Return the definition for a stage without inferring a technical solution."""
    return SERVICE_DEFINITIONS[stage]


@dataclass(frozen=True)
class CustomerRequestExample:
    statement: str
    observed_request: str
    first_service: ServiceStage
    reason: str
    technical_solution_selected: bool = False


def chapter_examples() -> tuple[CustomerRequestExample, ...]:
    """Return explicit fictional cases; this is not a text-classification engine."""
    return (
        CustomerRequestExample(
            "We need a new website.", "Website replacement", ServiceStage.AUDIT,
            "The underlying business problem has not yet been established.",
        ),
        CustomerRequestExample(
            "We need an app so members can cancel online.", "Custom member app",
            ServiceStage.DISCOVERY,
            "The cancellation workflow, constraints, volume, and current system capabilities are unknown.",
        ),
        CustomerRequestExample(
            "Our staff spends all day answering the same appointment questions.",
            "Reduce repetitive appointment questions", ServiceStage.AUDIT,
            "The friction sounds important, but its causes and frequency still need evidence.",
        ),
        CustomerRequestExample(
            "Our booking system is terrible.", "Booking system replacement",
            ServiceStage.AUDIT,
            "A product judgment does not identify the failing workflow or its business effect.",
        ),
        CustomerRequestExample(
            "We want AI.", "AI implementation", ServiceStage.AUDIT,
            "A technology preference is not a validated business problem.",
        ),
        CustomerRequestExample(
            "Our customers complain that joining takes too long.",
            "Faster customer joining", ServiceStage.DISCOVERY,
            "The workflow and complaint are plausible evidence, but the cause and economics remain unknown.",
        ),
        CustomerRequestExample(
            "The confirmation email has the old phone number; our admin can edit the template.",
            "Correct a phone number", ServiceStage.AUDIT,
            "The safe response is the obvious configuration fix, then exit; deeper discovery is disproportionate.",
        ),
        CustomerRequestExample(
            "Staff retypes notes because our handoff checklist asks for the same details twice.",
            "Remove duplicate handoff work", ServiceStage.AUDIT,
            "Change the checklist first and observe the result before considering software implementation.",
        ),
    )
