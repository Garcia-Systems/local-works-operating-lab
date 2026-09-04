"""Run Chapter 4's hypothetical acquisition-funnel exercise."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.acquisition import (  # noqa: E402
    FUNNEL_DEFINITIONS, FunnelStage, analyze_bottlenecks,
    baseline_website_funnel, outreach_funnel, referral_funnel,
)


def show_result(scenario):
    result = scenario.expected()
    print(f"\n{scenario.name} (entry: {scenario.entry_stage.value}, n={scenario.starting_count:,})")
    print(f"{'Stage':24} {'Entered':>10} {'Conversion':>12} {'Advanced':>11}")
    for step in result.steps:
        print(f"{step.transition.from_stage.value:24} {step.entered:10,.2f} "
              f"{step.transition.assumed_conversion_rate:11.1%} {step.advanced:11,.2f}")
    return result


def main() -> None:
    scenario = baseline_website_funnel()
    print("SECTION 1 — Funnel vocabulary")
    for stage, definition in FUNNEL_DEFINITIONS.items():
        print(f"{stage.value}: {definition}")
    print("Sale is not cash collected, project completion, or profitability.")

    print("\nSECTION 2 — Hypothetical baseline")
    print("HYPOTHETICAL TRAINING SCENARIO")
    print("HYPOTHETICAL TRAINING ASSUMPTIONS — NOT OBSERVED LOCAL WORKS DATA")
    print("NO LOCAL WORKS RESULTS ARE BEING CLAIMED")
    expected = show_result(scenario)

    print("\nSECTION 3 — Expected vs simulated")
    print(f"Expected sales: {expected.final_count:.2f} (planning value; not fractional people)")
    for seed in (4, 14, 24, 34, 44):
        trial = scenario.simulate(seed)
        print(f"Seed {seed:>2}: {trial.final_count} simulated sales — {trial.notice}")

    print("\nSECTION 4 — Bottleneck analysis")
    for label, finding in analyze_bottlenecks(scenario).items():
        t = finding.transition
        print(f"{label.replace('_', ' ').title()}: {t.from_stage.value} → {t.to_stage.value} ({finding.value:.2f})")
    print("These are numerical flags, not prescriptions. Qualification drop-off may protect scarce sales time;")
    print("largest loss and lowest rate do not automatically identify what the business should fix.")

    print("\nSECTION 5 — Sensitivity (one hypothetical change at a time)")
    variants = (
        ("Baseline", scenario),
        ("Improved website visit rate", scenario.with_rate(FunnelStage.EXPOSURE, .04, "Visit sensitivity")),
        ("Improved audit completion", scenario.with_rate(FunnelStage.AUDIT_START, .75, "Completion sensitivity")),
        ("Improved discovery progression", scenario.with_rate(FunnelStage.DISCOVERY, .70, "Discovery sensitivity")),
        ("Improved proposal close rate", scenario.with_rate(FunnelStage.PROPOSAL, .45, "Close sensitivity")),
    )
    for label, variant in variants:
        print(f"{label:35} {variant.expected().final_count:6.2f} expected sales")
    print("No modeled improvement is claimed to be easy, realistic, or universally best.")

    print("\nSECTION 6 — Different channel shapes")
    channels = (scenario, outreach_funnel(), referral_funnel())
    for channel in channels:
        path = " → ".join([channel.entry_stage.value] + [t.to_stage.value for t in channel.transitions])
        print(f"{channel.name}: {path}; expected final={channel.expected().final_count:.2f}")
    print("Referral starts deeper; its rates remain hypotheses, not claims about referral performance.")

    print("\nSECTION 7 — Owner time")
    for channel in channels:
        print(f"{channel.name:24} {channel.estimated_owner_hours():7.2f} hypothetical owner hours")
    print("Low cash cost can still consume substantial owner capacity; no salary or profitability is calculated.")

    print("\nSECTION 8 — Interpretation")
    for question in (
        "Where does the funnel currently rely on the weakest assumptions?",
        "Which conversion rates would we need to measure first?",
        "Which stages consume the most owner time?",
        "Could qualification protect downstream capacity?",
        "How many prospects might be required before we learn anything useful?",
        "What would we change before spending more money?",
    ):
        print(f"- {question}")
    print("\nSIMULATED OUTPUT IS NOT OBSERVED EVIDENCE.")


if __name__ == "__main__":
    main()
