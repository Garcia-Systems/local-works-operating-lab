#!/usr/bin/env python3
"""Run the Chapter 0 evidence-labeling exercise."""

from pathlib import Path
import sys

# Allow the script to run directly from a fresh checkout without installation.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.hypothesis import (  # noqa: E402
    BusinessTest,
    EvidenceType,
    group_by_business_test,
    initial_hypotheses,
)


def main() -> None:
    print("CHAPTER 0 — THE LOCAL WORKS EXPERIMENT")
    print("What exactly are we testing?\n")
    print("Evidence language:")
    for evidence_type in EvidenceType:
        print(f"  {evidence_type.value}")

    print("\nInitial business hypotheses:")
    grouped = group_by_business_test(initial_hypotheses())
    for business_test in BusinessTest:
        print(f"\n{business_test.value}")
        for hypothesis in grouped[business_test]:
            print(f"  • {hypothesis.statement}")
            print(f"    Evidence: {hypothesis.evidence_label}")
            print(f"    Status: {hypothesis.confidence}")

    print("\nConclusion: NONE of these business hypotheses are proven yet.")
    print("Observation and measurement must come from future operating experiments.")


if __name__ == "__main__":
    main()
