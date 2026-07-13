#!/usr/bin/env python3
"""Print a compact proof-idea map; expand only when --full is requested."""

from __future__ import annotations

import argparse
import textwrap

from proof_doctor import external_pattern_queries
from start_proof import central_lemma_suggestions, idea_rows, select_playbooks


def wrap(text: str) -> str:
    return textwrap.fill(text, width=88, subsequent_indent="  ")


def print_compact(claim: str, selected: list[tuple[str, int]]) -> None:
    print("Mode")
    print("- Try direct proof first; use this map only if no named theorem, certificate, contradiction, or known decomposition closes the claim.")

    print("\nSelected playbooks")
    for name, value in selected:
        print(f"- {name} (score {value})")

    print("\nStatement and failure world")
    print(f"- claim: {claim}")
    print("- statement fence: exact variables, domains, assumptions, quantifiers, and conclusion")
    print("- negation: write the smallest object that would falsify the claim")
    print("- first stress test: smallest finite/scalar/boundary/relaxed-assumption case")

    print("\nCentral-object candidates")
    for obj, failure, assumptions, hook in idea_rows(selected)[:6]:
        print(f"- {obj}: controls {wrap(failure)}")
        print(f"  assumptions: {wrap(assumptions)}")
        print(f"  verification: {wrap(hook)}")

    print("\nKernel candidates")
    for line in central_lemma_suggestions(selected).splitlines():
        print(line)

    print("\nChoose one next artifact")
    print("- State one kernel: local claim, implication for the theorem, evidence type, and failure shape.")
    print("- Compare one proof route, one falsification route, and one orthogonal evidence route.")
    print("- Continue only with a route that controls the failure world and has a verification hook.")
    print("- If no kernel appears, retrieve one close theorem pattern or repair the statement; do not draft a long proof.")


def print_full() -> None:
    print("\nExtended search")
    print("- Discovery: if a threshold, potential, policy, hard instance, active set, coefficient, or exact answer is unknown, infer it from tiny/tight cases and reserve a holdout check.")
    print("- Novel problem: treat memory as unverified; first scan Scholar/recent public work and verify the closest result and frontier gap, then define the candidate representation, exact evaluator, simplification ladder, promotion rule, and budget.")
    print("- Bottleneck surgery: shrink the missing lemma, negate it, change representation once, then prove, falsify, retrieve, certify, or repair it.")
    print("- Construction seeds: dual/slack, Bellman gap, envelope term, deviation graph, coupling, KL bridge, potential, benchmark, or hard instance.")
    print("- Algebra forms: add-subtract benchmark, gap/telescope, completing square, conjugate/dual, log/KL/determinant, symmetrization, or conditioning on a good event.")
    print("- Good-gap test: require the kernel to be smaller, non-circular, assumption-explicit, and locally checkable.")

    print("\nOne-move control")
    print("- Record current subgoal, proposed move, expected artifact, check, and proof-state delta.")
    print("- After two unchanged moves, choose repair, re-decompose, retrieve, tool-falsify, theorem repair, or stop-report.")
    print("- Use a prover-verifier contract only for challenged, repeated, or hard-to-check moves.")
    print("- Merge attempts with the same goal, assumptions, central object, and failure witness.")

    print("\nOutside patterns and tools")
    print("- Scan one to three close sources only when the theorem family, central object, or standard lemma is missing.")
    print("- Extract assumptions, proof decomposition, local trick, verification hook, and mismatch; do not import prose as proof.")
    print("- Before a tool call, name the local claim, domain, negation, expected artifact, and translation back into proof.")
    print("- Audit Lean/API artifacts for `sorry`, admitted axioms, unresolved obligations, and missing assembly.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("claim", help="The theorem, lemma, or proof goal")
    parser.add_argument("--full", action="store_true", help="Add construction, repair, retrieval, and tool-control details")
    parser.add_argument("--include-paper-queries", action="store_true", help="Print claim-specific literature search prompts")
    args = parser.parse_args()

    selected = select_playbooks(args.claim)
    print_compact(args.claim, selected)
    if args.full:
        print_full()
    if args.include_paper_queries:
        print("\nSearch prompts")
        for query in external_pattern_queries(args.claim, selected):
            print(f"- {query}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
