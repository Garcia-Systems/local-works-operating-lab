#!/usr/bin/env python3
"""Run the Chapter 1 requested-solution versus first-service exercise."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from local_works.services import chapter_examples  # noqa: E402


def main() -> None:
    print("CHAPTER 1 — WHAT ARE WE ACTUALLY SELLING?")
    print("Customer solution language is a starting signal, not a problem definition.\n")

    for number, example in enumerate(chapter_examples(), start=1):
        print(f"Example {number}")
        print(f'Customer request: \u201c{example.statement}\u201d')
        print(f"Observed request: {example.observed_request}.")
        print(f"Local Works first service: {example.first_service.value}.")
        print(f"Reason: {example.reason}")
        selected = "Yes" if example.technical_solution_selected else "No"
        print(f"Technical solution selected? {selected}.\n")

    print("Local Works sells a structured path:")
    print("Problem → Understanding → Decision → Implementation → Ongoing operation")
    print("Implementation is possible, not inevitable.")


if __name__ == "__main__":
    main()
