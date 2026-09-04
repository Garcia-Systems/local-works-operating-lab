"""Evidence-cautious acquisition and market-experiment models for Chapter 3.

Everything here is a planning hypothesis or a fictional result.  It deliberately
keeps observations, interpretations, costs, and outcomes separate.
"""

from dataclasses import dataclass, replace
from enum import Enum
import random

from local_works.hypothesis import EvidenceType


class AcquisitionChannel(Enum):
    PERSONALIZED_OUTREACH = "Personalized outreach"
    DIGITAL_FRICTION_AUDIT = "Digital Friction Audit"
    LOCAL_NETWORKING = "Local networking"
    REFERRAL = "Referral"
    LINKEDIN = "LinkedIn relationship/outreach"
    OUTBOUND_EMAIL = "Generic outbound email"
    PARTNERSHIP = "Partnership"
    BUSINESS_ORGANIZATION = "Business/community organization"
    CONTENT = "Educational content"
    VIDEO = "Educational video"
    SEO = "Search engine optimization"
    PAID_SOCIAL = "Paid Facebook/Instagram advertising"
    PAID_SEARCH = "Paid Google/search advertising"


class ChannelType(Enum):
    DIRECT_ACQUISITION = "direct customer acquisition"
    CREDIBILITY = "credibility and trust"
    RELATIONSHIP = "relationship development"
    MARKET_LEARNING = "market learning"


class ExperimentResult(Enum):
    NOT_RUN = "NOT YET RUN IN THE REAL WORLD"
    INCONCLUSIVE = "inconclusive"
    ENCOURAGING = "encouraging"
    DISCOURAGING = "discouraging"


class FunnelStage(Enum):
    """Common vocabulary; a channel may use only the stages that fit its path."""

    EXPOSURE = "Exposure"
    WEBSITE_VISIT = "Website Visit"
    AUDIT_START = "Audit Start"
    AUDIT_COMPLETION = "Audit Completion"
    LEAD = "Lead"
    QUALIFIED_LEAD = "Qualified Lead"
    DISCOVERY = "Discovery"
    PROPOSAL = "Proposal"
    SALE = "Sale"
    TARGET_IDENTIFIED = "Target Identified"
    OUTREACH = "Outreach"
    RESPONSE = "Response"
    QUALIFIED_CONVERSATION = "Qualified Conversation"
    REFERRAL = "Referral"


FUNNEL_DEFINITIONS: dict[FunnelStage, str] = {
    FunnelStage.EXPOSURE: "Someone had an opportunity to encounter Local Works.",
    FunnelStage.WEBSITE_VISIT: "Someone intentionally visited a Local Works page.",
    FunnelStage.AUDIT_START: "Someone began the Digital Friction Audit.",
    FunnelStage.AUDIT_COMPLETION: "Someone supplied enough audit information for review.",
    FunnelStage.LEAD: "A person or organization supplied enough information or engagement for possible follow-up.",
    FunnelStage.QUALIFIED_LEAD: "A lead appears relevant enough to justify more Local Works attention.",
    FunnelStage.DISCOVERY: "A meaningful discovery conversation or process occurs.",
    FunnelStage.PROPOSAL: "Local Works presents a specific commercial recommendation.",
    FunnelStage.SALE: "A customer accepts an engagement under agreed commercial terms.",
}


@dataclass(frozen=True)
class FunnelTransition:
    from_stage: FunnelStage
    to_stage: FunnelStage
    assumed_conversion_rate: float
    evidence_type: EvidenceType
    notes: str = ""

    def __post_init__(self) -> None:
        if not 0 <= self.assumed_conversion_rate <= 1:
            raise ValueError("Conversion rate must be between 0 and 1 inclusive.")


@dataclass(frozen=True)
class OwnerEffort:
    stage: FunnelStage
    minutes_per_activity: float
    evidence_type: EvidenceType = EvidenceType.HYPOTHESIS
    notes: str = ""

    def __post_init__(self) -> None:
        if self.minutes_per_activity < 0:
            raise ValueError("Minutes per activity cannot be negative.")


@dataclass(frozen=True)
class FunnelStepResult:
    transition: FunnelTransition
    entered: float | int
    advanced: float | int

    @property
    def lost(self) -> float:
        return float(self.entered) - float(self.advanced)


@dataclass(frozen=True)
class FunnelResult:
    scenario_name: str
    steps: tuple[FunnelStepResult, ...]
    final_count: float | int
    is_simulated: bool
    evidence_type: EvidenceType
    notice: str


@dataclass(frozen=True)
class BottleneckFinding:
    transition: FunnelTransition
    value: float
    interpretation_required: bool = True
    is_business_failure: bool = False


@dataclass(frozen=True)
class FunnelScenario:
    name: str
    starting_count: int
    entry_stage: FunnelStage
    transitions: tuple[FunnelTransition, ...]
    owner_effort: tuple[OwnerEffort, ...] = ()
    quality_note: str = "Volume does not establish customer quality or economic fit."
    assumption_notice: str = "HYPOTHETICAL TRAINING ASSUMPTIONS — NOT OBSERVED LOCAL WORKS DATA"

    def __post_init__(self) -> None:
        if self.starting_count < 0:
            raise ValueError("Starting count cannot be negative.")
        expected_from = self.entry_stage
        for transition in self.transitions:
            if transition.from_stage is not expected_from:
                raise ValueError("Transitions must form a continuous path from the entry stage.")
            expected_from = transition.to_stage

    def expected(self) -> FunnelResult:
        count: float = float(self.starting_count)
        steps: list[FunnelStepResult] = []
        for transition in self.transitions:
            advanced = count * transition.assumed_conversion_rate
            steps.append(FunnelStepResult(transition, count, advanced))
            count = advanced
        return FunnelResult(self.name, tuple(steps), count, False,
                            EvidenceType.HYPOTHESIS,
                            "Expected values are planning arithmetic, not observed outcomes.")

    def simulate(self, seed: int) -> FunnelResult:
        """Run one transparent sequence of Bernoulli trials."""
        generator = random.Random(seed)
        count = self.starting_count
        steps: list[FunnelStepResult] = []
        for transition in self.transitions:
            advanced = sum(
                generator.random() < transition.assumed_conversion_rate
                for _ in range(count)
            )
            steps.append(FunnelStepResult(transition, count, advanced))
            count = advanced
        return FunnelResult(self.name, tuple(steps), count, True,
                            EvidenceType.HYPOTHESIS,
                            "SIMULATED OUTPUT IS NOT OBSERVED EVIDENCE.")

    def estimated_owner_hours(self, result: FunnelResult | None = None) -> float:
        result = result or self.expected()
        entered = {self.entry_stage: float(self.starting_count)}
        entered.update({step.transition.to_stage: float(step.advanced) for step in result.steps})
        minutes = sum(entered.get(item.stage, 0) * item.minutes_per_activity
                      for item in self.owner_effort)
        return minutes / 60

    def with_rate(self, from_stage: FunnelStage, rate: float, name: str) -> "FunnelScenario":
        transitions = tuple(
            replace(t, assumed_conversion_rate=rate) if t.from_stage is from_stage else t
            for t in self.transitions
        )
        return replace(self, name=name, transitions=transitions)


def analyze_bottlenecks(scenario: FunnelScenario) -> dict[str, BottleneckFinding]:
    result = scenario.expected()
    largest_loss = max(result.steps, key=lambda step: step.lost)
    weakest = min(result.steps, key=lambda step: step.transition.assumed_conversion_rate)
    # Compare a feasible ten-percentage-point improvement at each transition.
    leverage: list[tuple[float, FunnelTransition]] = []
    baseline = float(result.final_count)
    for transition in scenario.transitions:
        improved_rate = min(1.0, transition.assumed_conversion_rate + 0.10)
        improved = scenario.with_rate(transition.from_stage, improved_rate, "sensitivity")
        leverage.append((float(improved.expected().final_count) - baseline, transition))
    lift, leveraged_transition = max(leverage, key=lambda item: item[0])
    return {
        "largest_absolute_loss": BottleneckFinding(largest_loss.transition, largest_loss.lost),
        "lowest_conversion": BottleneckFinding(weakest.transition, weakest.transition.assumed_conversion_rate),
        "highest_ten_point_leverage": BottleneckFinding(leveraged_transition, lift),
    }


def _transition(start: FunnelStage, end: FunnelStage, rate: float, notes: str = "") -> FunnelTransition:
    return FunnelTransition(start, end, rate, EvidenceType.HYPOTHESIS, notes)


def baseline_website_funnel() -> FunnelScenario:
    S = FunnelStage
    return FunnelScenario("Website / content", 10_000, S.EXPOSURE, (
        _transition(S.EXPOSURE, S.WEBSITE_VISIT, .02),
        _transition(S.WEBSITE_VISIT, S.AUDIT_START, .15),
        _transition(S.AUDIT_START, S.AUDIT_COMPLETION, .25),
        _transition(S.AUDIT_COMPLETION, S.QUALIFIED_LEAD, .40, "Filtering may protect capacity."),
        _transition(S.QUALIFIED_LEAD, S.DISCOVERY, .60),
        _transition(S.DISCOVERY, S.PROPOSAL, .50),
        _transition(S.PROPOSAL, S.SALE, .30),
    ), (OwnerEffort(S.EXPOSURE, .12, notes="20 hypothetical content hours spread over exposures"),
        OwnerEffort(S.AUDIT_COMPLETION, 12), OwnerEffort(S.DISCOVERY, 60),
        OwnerEffort(S.PROPOSAL, 90)))


def outreach_funnel() -> FunnelScenario:
    S = FunnelStage
    return FunnelScenario("Personalized outreach", 80, S.TARGET_IDENTIFIED, (
        _transition(S.TARGET_IDENTIFIED, S.OUTREACH, .75), _transition(S.OUTREACH, S.RESPONSE, .25),
        _transition(S.RESPONSE, S.QUALIFIED_CONVERSATION, .40),
        _transition(S.QUALIFIED_CONVERSATION, S.DISCOVERY, .60),
        _transition(S.DISCOVERY, S.PROPOSAL, .50), _transition(S.PROPOSAL, S.SALE, .30),
    ), (OwnerEffort(S.TARGET_IDENTIFIED, 12), OwnerEffort(S.OUTREACH, 8),
        OwnerEffort(S.QUALIFIED_CONVERSATION, 15), OwnerEffort(S.DISCOVERY, 60),
        OwnerEffort(S.PROPOSAL, 90)))


def referral_funnel() -> FunnelScenario:
    S = FunnelStage
    return FunnelScenario("Referral", 12, S.REFERRAL, (
        _transition(S.REFERRAL, S.QUALIFIED_LEAD, .50),
        _transition(S.QUALIFIED_LEAD, S.DISCOVERY, .70),
        _transition(S.DISCOVERY, S.PROPOSAL, .60), _transition(S.PROPOSAL, S.SALE, .35),
    ), (OwnerEffort(S.REFERRAL, 10), OwnerEffort(S.QUALIFIED_LEAD, 15),
        OwnerEffort(S.DISCOVERY, 60), OwnerEffort(S.PROPOSAL, 90)))


@dataclass(frozen=True)
class ChannelHypothesis:
    channel: AcquisitionChannel
    primary_purpose: ChannelType
    cash_cost: str
    owner_time_cost: str
    learning_speed: str
    targeting_ability: str
    trust_requirement: str
    scalability_hypothesis: str
    main_assumption: str
    evidence_to_collect: str
    major_risk: str
    recommended_role: str
    current_status: str = "unvalidated hypothesis"


@dataclass(frozen=True)
class PublicFrictionObservation:
    """A public fact plus a *separate*, explicitly unvalidated interpretation."""

    source_context: str
    observed_fact: str
    possible_friction_hypothesis: str
    unknowns: tuple[str, ...]
    discovery_question: str
    validated_problem: bool = False

    def __post_init__(self) -> None:
        if not self.unknowns:
            raise ValueError("Public observations must preserve at least one unknown.")
        if self.validated_problem:
            raise ValueError(
                "A public observation cannot by itself be marked as a validated problem."
            )


@dataclass(frozen=True)
class MarketExperiment:
    name: str
    question: str
    target: str
    channel: AcquisitionChannel
    offer: str
    cash_limit: str
    owner_time_limit: str
    success_evidence: str
    failure_evidence: str
    result: ExperimentResult = ExperimentResult.NOT_RUN
    learning: tuple[str, ...] = ()

    @property
    def has_been_run(self) -> bool:
        return self.result is not ExperimentResult.NOT_RUN

    def record_result(
        self, result: ExperimentResult, learning: tuple[str, ...]
    ) -> "MarketExperiment":
        if result is ExperimentResult.NOT_RUN:
            raise ValueError("Use an outcome other than NOT_RUN when recording a result.")
        if not learning:
            raise ValueError("Every outcome, including a negative one, must record learning.")
        return replace(self, result=result, learning=learning)


def first_market_experiment() -> MarketExperiment:
    return MarketExperiment(
        name="Gym Digital Friction Audit Outreach — Experiment 001",
        question=("Can a specific public membership-journey observation begin useful "
                  "conversations with independent-gym decision makers?"),
        target="A small, fictional sample of independently operated gyms",
        channel=AcquisitionChannel.PERSONALIZED_OUTREACH,
        offer="A brief conversation to check the observation—not a software sale",
        cash_limit="Minimal incidental spending; no advertising buy",
        owner_time_limit="A small, precommitted owner-time block for research and outreach",
        success_evidence="Decision makers validate friction and agree to discovery conversations",
        failure_evidence=("Relevant decision makers consistently say the observed journey is not "
                          "meaningful, is already handled, or cannot be changed"),
    )


def channel_hypotheses() -> tuple[ChannelHypothesis, ...]:
    """Qualitative comparisons—not performance forecasts or a winner ranking."""
    C, T = AcquisitionChannel, ChannelType
    return (
        ChannelHypothesis(C.PERSONALIZED_OUTREACH, T.MARKET_LEARNING, "Low", "High",
            "Fast if prospects respond", "High", "Must earn attention with relevance",
            "May remain owner-led until a repeatable pattern exists",
            "A specific public observation earns a candid conversation",
            "Replies, observation corrections, validated pain, and conversations",
            "Time-intensive research may not produce replies", "Lead the first bounded test"),
        ChannelHypothesis(C.DIGITAL_FRICTION_AUDIT, T.MARKET_LEARNING, "Low", "High",
            "Moderate", "High", "Careful evidence can earn trust but is not diagnosis",
            "A safe method may repeat, while judgment remains owner-intensive",
            "Public workflow observations reveal questions owners consider relevant",
            "Corrections, validated impact, constraints, conversations, and effort",
            "Inference may be presented as fact or research may become intrusive", "Mechanism for personalized test"),
        ChannelHypothesis(C.OUTBOUND_EMAIL, T.DIRECT_ACQUISITION, "Low", "Moderate",
            "Potentially fast but shallow", "Moderate", "High from an unknown sender",
            "May reach more prospects if a resonant message is learned",
            "A broad service message can earn attention without prior trust",
            "Relevant replies, objections, and conversation quality",
            "Silence reveals little about market need versus message/delivery", "Small comparison only"),
        ChannelHypothesis(C.LOCAL_NETWORKING, T.RELATIONSHIP, "Low to moderate", "High",
            "Slow", "Moderate", "Trust develops through repeated contact",
            "Difficult to scale directly; relationships may compound",
            "Relevant owners attend and will discuss workflows",
            "Conversations, introductions, repeated concerns, and owner hours",
            "Slow attribution and unfocused attendance", "Relationship and language learning"),
        ChannelHypothesis(C.LINKEDIN, T.RELATIONSHIP, "Low", "Moderate to high",
            "Moderate", "High when roles are current", "Unknown profile needs credibility",
            "May support repeatable relationship activity, not automatic trust",
            "Independent-gym decision makers are reachable and active there",
            "Accepted connections, substantive replies, objections, and time",
            "Activity metrics can be mistaken for market evidence", "Targeted supporting test"),
        ChannelHypothesis(C.PARTNERSHIP, T.RELATIONSHIP, "Low to moderate", "High to establish",
            "Slow", "Depends on partner reach", "Trust and reputation transfer both ways",
            "A few aligned partners may create recurring qualified introductions",
            "Partners serve the same buyers with complementary capabilities",
            "Qualified introductions, alignment, delivery expectations, and effort",
            "Misaligned incentives or unclear customer ownership", "Explore relationships, not primary test"),
        ChannelHypothesis(C.BUSINESS_ORGANIZATION, T.RELATIONSHIP, "Membership or event dependent", "High",
            "Slow", "Depends on membership", "Local presence may compound but attribution stays difficult",
            "Trust requires genuine participation rather than extraction",
            "Relevant owners participate and discuss operational workflows",
            "Repeated conversations, introductions, themes, cash, and time",
            "Unfocused attendance can consume substantial time", "Selective relationship learning"),
        ChannelHypothesis(C.CONTENT, T.CREDIBILITY, "Low", "High",
            "Slow", "Broad unless deliberately distributed", "Must demonstrate useful judgment",
            "A useful library may compound, but distribution remains unproven",
            "Gym operators seek and trust educational workflow material",
            "Relevant questions, qualified conversations, and reuse in outreach",
            "Publishing without distribution or buyer interest", "Credibility support, not primary test"),
        ChannelHypothesis(C.VIDEO, T.CREDIBILITY, "Low to moderate", "High",
            "Slow to moderate", "Broad unless distributed deliberately",
            "Personal presence may help; polish cannot replace evidence",
            "Useful videos may be reusable, but distribution remains unproven",
            "Relevant operators value workflow demonstrations in video form",
            "Qualified questions, reuse in outreach, production time, and expense",
            "Views can be mistaken for buyer interest", "Optional credibility support"),
        ChannelHypothesis(C.SEO, T.CREDIBILITY, "Low cash to higher support cost", "High and ongoing",
            "Slow", "Search intent can target, but language is unproven",
            "Visibility does not itself establish confidence",
            "Relevant search visibility may compound if genuine demand exists",
            "Qualified buyers search for problems Local Works can credibly address",
            "Search intent, qualified conversations, downstream fit, time, and cost",
            "Optimizing for traffic without buyer relevance", "Defer as primary learning channel"),
        ChannelHypothesis(C.PAID_SOCIAL, T.DIRECT_ACQUISITION, "Higher", "Moderate",
            "Fast message feedback, uncertain sales learning", "Platform-dependent",
            "Cold audiences require a clear credible offer",
            "Could scale only after audience, offer, and economics are understood",
            "Platform targeting can reach relevant independent-gym decision makers",
            "Qualified conversations—not clicks alone—plus spend and owner time",
            "Buying traffic before learning message, qualification, or value", "Defer meaningful spend"),
        ChannelHypothesis(C.PAID_SEARCH, T.DIRECT_ACQUISITION, "Higher", "Moderate",
            "Fast traffic feedback, uncertain demand learning", "Intent-based but imperfect",
            "Unknown provider must establish confidence quickly",
            "Could scale if relevant demand, conversion, and economics are established",
            "Decision makers search using terms Local Works can serve credibly",
            "Search intent, qualified conversations, spend, and downstream fit",
            "Paying for ambiguous or solution-first searches", "Defer meaningful spend"),
        ChannelHypothesis(C.REFERRAL, T.RELATIONSHIP, "Low cash", "High relationship investment",
            "Fast after an introduction; slow to establish", "Depends on referrer network",
            "Borrowed trust helps, but still requires validation",
            "May compound after credible relationships and results exist",
            "Existing contacts know suitable decision makers and will introduce them",
            "Introduction source, fit, conversation, and relationship effort",
            "Not available at meaningful scale before trust exists", "Accept warm tests; do not depend on scale"),
    )
