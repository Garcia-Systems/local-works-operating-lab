#!/usr/bin/env python3
"""Run the entirely simulated Chapter 3 first-market exercise."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.acquisition import (  # noqa: E402
    ExperimentResult,
    channel_hypotheses,
    first_market_experiment,
)


RESPONSES = (
    ("Prospect A — Cedar Street Athletics", "That actually is a pain point. We get calls about it constantly.",
     "The hypothesis deserves validation; frequency and impact remain unknown.", "Follow up; offer discovery/audit.", "No"),
    ("Prospect B — Northstar Training Club", "Our software already handles that online. The website is just outdated.",
     "The observation was accurate but the inferred operational problem was wrong.", "Ask only whether an outdated page matters; no system audit yet.", "Yes, unless invited"),
    ("Prospect C — Juniper Strength House", "No, it really doesn't cause us problems.",
     "This prospect does not validate meaningful friction.", "Thank them; record the evidence.", "Yes"),
    ("Prospect D — Lantern Fitness", "We'd like to improve it, but corporate controls the system.",
     "Friction may exist but local authority and feasibility do not.", "Stop sales follow-up unless an authorized path is offered.", "Yes"),
    ("Prospect E — Bayside Barbell", "No response.",
     "Need, message fit, timing, and delivery are all still unknown.", "At most one respectful follow-up under the experiment rule.", "Yes after the limit"),
)


def main() -> None:
    print("CHAPTER 3 — THE FIRST MARKET EXPERIMENT")
    print("SIMULATION ONLY — NOT YET RUN IN THE REAL WORLD")
    print("Gyms are a market to investigate, not a selected permanent vertical.\n")
    for hypothesis in channel_hypotheses():
        print(f"Channel: {hypothesis.channel.value}")
        print(f"Primary purpose: {hypothesis.primary_purpose.value}")
        print(f"Cash-cost hypothesis: {hypothesis.cash_cost}")
        print(f"Owner-time hypothesis: {hypothesis.owner_time_cost}")
        print(f"Learning speed: {hypothesis.learning_speed}")
        print(f"Trust challenge: {hypothesis.trust_requirement}")
        print(f"Main assumption: {hypothesis.main_assumption}")
        print(f"What we would measure: {hypothesis.evidence_to_collect}")
        print(f"Major risk: {hypothesis.major_risk}")
        print(f"Recommended role in first experiment: {hypothesis.recommended_role}\n")

    experiment = first_market_experiment()
    print(f"Experiment: {experiment.name}")
    print(f"Result: {experiment.result.value}")
    print(f"Question: {experiment.question}")
    print(f"Target: {experiment.target}")
    print(f"Offer: {experiment.offer}")
    print(f"Cash limit: {experiment.cash_limit}")
    print(f"Owner-time limit: {experiment.owner_time_limit}")
    print("Process: observe public journey → separate fact from hypothesis → ask a genuine question → record response.")
    print('\nBAD: “Hi, we build custom software and AI solutions for local businesses. Would you like to schedule a call?”')
    print("Why weak: generic, solution-first, and gives an unknown business no reason to trust or respond.")
    print('\nBETTER: “Your public membership page says freezes are requested by calling the front desk. How are those requests handled, and do they create meaningful work or member complaints?”')
    print("Why better: accurately names a public fact, labels nothing a problem, and invites correction.\n")
    print('ALSO BETTER: “Your class page asks first-time visitors to call about availability. What purpose does that call serve, and is the process working well for your team?”')
    print("Why better: it leaves open the possibility that the current process is intentional and effective.\n")
    print("Deterministic fictional response practice:")
    for prospect, response, learned, follow_up, stop in RESPONSES:
        print(f"\n{prospect}\nResponse: {response}\nLearned: {learned}")
        print(f"Follow-up / audit decision: {follow_up}\nStop? {stop}")

    simulated = experiment.record_result(
        ExperimentResult.INCONCLUSIVE,
        ("Mixed fictional responses show that observation is not diagnosis.",
         "Negative replies and corrections can still improve the market hypothesis."),
    )
    print(f"\nSimulated practice classification: {simulated.result.value}")
    print("Early goal: LEARN WHETHER A REAL PROBLEM EXISTS AND WHETHER THE BUSINESS CARES—not close immediately.")
    print("Economics preview: total acquisition cost = cash spending + owner time + supporting expenses.")


if __name__ == "__main__":
    main()
