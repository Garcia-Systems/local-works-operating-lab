#!/usr/bin/env python3
"""Compare fictional prospects using the Chapter 2 customer-fit hypothesis."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.customers import assess_customer, fictional_profiles  # noqa: E402


def print_items(heading: str, items: tuple[object, ...]) -> None:
    print(f"{heading}:")
    if not items:
        print("- None identified.")
        return
    for item in items:
        reason = getattr(item, "reason", str(item))
        name = getattr(item, "name", None)
        print(f"- {name}: {reason}" if name else f"- {reason}")


def main() -> None:
    print("CHAPTER 2 — THE IDEAL CUSTOMER HYPOTHESIS")
    print("INITIAL HYPOTHESIS — NOT VALIDATED")
    print("All organizations and observations below are fictional.")
    print("UNKNOWN is different from BAD. This is prioritization, not automatic acceptance.\n")

    for profile in fictional_profiles():
        assessment = assess_customer(profile)
        print(f"Business: {profile.business}")
        print(f"Industry/type: {profile.industry}")
        print_items("Positive signals", assessment.positive_signals)
        print_items("Negative signals", assessment.negative_signals)
        print_items("Unknowns", assessment.unknowns)
        print_items("Hard disqualifiers", profile.hard_disqualifiers)
        print(f"Current fit assessment: {assessment.rating.value}")
        print(f"Why: {assessment.rationale}")
        print(f"Recommended next action: {assessment.next_action}\n")

    print("Same-industry lesson:")
    print("An owner-controlled gym with recurring manual work and reachable authority may be promising.")
    print("A corporate gym branch can have the same friction but no local purchasing path.")
    print("Industry ≠ ICP.")


if __name__ == "__main__":
    main()
