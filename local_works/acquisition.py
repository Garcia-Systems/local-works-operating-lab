"""Evidence-cautious acquisition and market-experiment models for Chapter 3.

Everything here is a planning hypothesis or a fictional result.  It deliberately
keeps observations, interpretations, costs, and outcomes separate.
"""

from dataclasses import dataclass, replace
from enum import Enum


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
