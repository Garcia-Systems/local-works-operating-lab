"""Run Chapter 5's entirely hypothetical acquisition-economics exercise."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.acquisition import FunnelScenario, FunnelStage, FunnelTransition  # noqa: E402
from local_works.acquisition_economics import (
    AcquisitionCost, AcquisitionPeriod, ChannelEconomics, OwnerTimeActivity,
    compare_channels, cumulative_economics,
)  # noqa: E402
from local_works.hypothesis import EvidenceType  # noqa: E402


NOTICE = "HYPOTHETICAL TRAINING ASSUMPTIONS — NOT REAL LOCAL WORKS DATA"


def money(value: float | None) -> str:
    return "undefined (no customers acquired)" if value is None else f"${value:,.2f}"


def transition(start: FunnelStage, end: FunnelStage, rate: float) -> FunnelTransition:
    return FunnelTransition(start, end, rate, EvidenceType.HYPOTHESIS)


def show_result(result) -> None:
    print(f"{result.name:<24} cash {money(result.total_cash_cost):>10} | "
          f"owner hours {result.total_owner_hours:>6.1f} | customers {result.customers_acquired:>2} | "
          f"cash CAC {money(result.cash_cac):>32} | loaded CAC {money(result.fully_loaded_cac)}")


def main() -> None:
    print(f"CHAPTER 5 — CUSTOMER ACQUISITION ECONOMICS\n{NOTICE}")
    print("\nSECTION 1 — CAC vocabulary")
    print("Cash acquisition cost: attributable cash spending. Owner time cost: owner hours × an assumed hour value.")
    print("Fully loaded acquisition cost: cash + owner time cost. Cash CAC and fully loaded CAC divide those totals by customers.")
    print("Owner hours per customer remains visible. These are management views, not one universal accounting definition.")

    outreach = ChannelEconomics("Personalized outreach", (AcquisitionCost("research/outreach", 0, 40),), 1)
    paid = ChannelEconomics("Paid campaign", (AcquisitionCost("advertising", 600, 8),), 1)
    print('\nSECTION 2 — "Free" acquisition is not free (at hypothetical $50/hour)')
    for result in compare_channels((outreach, paid), 50): show_result(result)

    print("\nSECTION 3 — Owner-hour sensitivity (training values, not an owner salary recommendation)")
    for value in (25, 50, 75, 100):
        values = compare_channels((outreach, paid), value)
        print(f"${value}/hour: outreach {money(values[0].fully_loaded_cac)}; paid {money(values[1].fully_loaded_cac)}")
    print("The loaded-cost gap changes with the assumption; cash-only ranking reverses once time is valued. No winner is established.")

    month_one = AcquisitionPeriod("Month 1", ChannelEconomics("Month 1", (AcquisitionCost("campaign", 500, 20),), 0))
    month_two = AcquisitionPeriod("Month 2", ChannelEconomics("Month 2", (AcquisitionCost("follow-up", 250, 6),), 1))
    print("\nSECTION 4 — Zero-customer month")
    show_result(month_one.economics.calculate(50))
    print("CAC cannot be meaningfully calculated because no customers were acquired, but $500 and 20 hours still exist.")
    print("\nSECTION 5 — Cumulative acquisition")
    show_result(month_two.economics.calculate(50))
    show_result(cumulative_economics("Months 1 + 2", (month_one, month_two)).calculate(50))
    print("The cumulative view includes failed attempts; the successful period alone does not.")

    S = FunnelStage
    funnel = FunnelScenario("Hypothetical paid funnel", 1000, S.WEBSITE_VISIT, (
        transition(S.WEBSITE_VISIT, S.AUDIT_START, .10),
        transition(S.AUDIT_START, S.AUDIT_COMPLETION, .40),
        transition(S.AUDIT_COMPLETION, S.LEAD, .50),
        transition(S.LEAD, S.QUALIFIED_LEAD, .50),
        transition(S.QUALIFIED_LEAD, S.DISCOVERY, .40),
        transition(S.DISCOVERY, S.PROPOSAL, .50),
        transition(S.PROPOSAL, S.SALE, .50),
    )).simulate(5)
    funnel_channel = ChannelEconomics("Paid funnel", (AcquisitionCost("advertising", 500, 6),), int(funnel.final_count), funnel)
    print("\nSECTION 6 — Cost through the funnel (one simulation; SIMULATED OUTPUT IS NOT EVIDENCE)")
    print(f"{'Stage':<20} {'Count':>8} {'Cash/outcome':>18} {'Loaded/outcome':>20}")
    for row in funnel_channel.cost_per_stage(50):
        print(f"{row.stage.value:<20} {row.count:>8.0f} {money(row.cash_cost_per_outcome):>18} {money(row.fully_loaded_cost_per_outcome):>20}")

    channels = (
        outreach,
        ChannelEconomics("Networking", (AcquisitionCost("event/travel", 350, 28),), 1),
        ChannelEconomics("Content", (AcquisitionCost("production", 150, 45),), 0),
        ChannelEconomics("Paid social", (AcquisitionCost("ads/creative", 900, 18),), 1),
        ChannelEconomics("Paid search", (AcquisitionCost("ads/landing page", 1200, 12),), 2),
        ChannelEconomics("Referral", (AcquisitionCost("relationship/follow-up", 50, 10),), 1),
    )
    print("\nSECTION 7 — Channel comparison (hypothetical; no winner declared; $50/hour)")
    for result in compare_channels(channels, 50): show_result(result)

    weak = ChannelEconomics("Many weak leads", (), 0, activities=(
        OwnerTimeActivity("lead review", 80, 10), OwnerTimeActivity("qualification", 40, 20),
        OwnerTimeActivity("discovery", 12, 60)))
    strong = ChannelEconomics("Fewer strong leads", (), 1, activities=(
        OwnerTimeActivity("lead review", 12, 10), OwnerTimeActivity("qualification", 10, 20),
        OwnerTimeActivity("discovery", 5, 60)))
    print("\nSECTION 8 — Lead-quality burden (example-only time assumptions)")
    for result in compare_channels((weak, strong), 50): show_result(result)

    print("\nSECTION 9 — Interpretation questions")
    for question in (
        "Which channel consumes the most cash?", "Which consumes the most owner time?",
        "Which conclusions depend heavily on the assumed owner-hour value?",
        "Which channels produced no simulated customers?",
        "How much effort was spent on prospects who did not buy?",
        "Which metrics require real-world measurement?",
        "Why can't CAC alone show whether Local Works works?",
    ): print(f"- {question}")
    print("CAC is necessary but insufficient: acquisition economics must eventually be compared with customer economic contribution.")


if __name__ == "__main__":
    main()
