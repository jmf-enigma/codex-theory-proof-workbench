#!/usr/bin/env python3
"""Print a lightweight optional proof-idea map for a theorem claim."""

from __future__ import annotations

import argparse
import textwrap

from proof_doctor import external_pattern_queries
from start_proof import central_lemma_suggestions, idea_rows, select_playbooks


def wrap(text: str) -> str:
    return textwrap.fill(text, width=88, subsequent_indent="  ")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("claim", help="The theorem, lemma, or proof goal")
    parser.add_argument("--include-paper-queries", action="store_true", help="Print prior-paper/literature search prompts")
    args = parser.parse_args()

    selected = select_playbooks(args.claim)

    print("Use mode")
    print("- Direct mode first. If a theorem, certificate, contradiction, or known decomposition solves the claim, do not start a project.")
    print("- Micro pattern check when the route is unclear but small: inspect one theorem family, prior ledger, or close paper pattern, then stop.")
    print("- Light idea mode only when the direct route is unclear.")
    print("- Full project mode only for hard, repeated, multi-lemma, tool-assisted, or literature-dependent proofs.")

    print("\nProgress contract")
    print("- A retry is useful only if it brings new evidence: proved/refuted kernel, counterexample, missing assumption, checked certificate, different central object, retrieved theorem pattern, verified trick, or theorem repair.")
    print("- Changing notation, adding cosmetic cases, or restating a stronger missing lemma is not progress.")
    print("- Before a second attempt on the same obstruction, name the route family, central object, target kernel, failure witness, and expected new evidence.")

    print("Direct-solve check")
    print("- State the theorem fence: no silent change to assumptions, quantifiers, domains, or conclusion.")
    print("- Is there a named theorem whose assumptions exactly match?")
    print("- Is there a certificate already visible: KKT, dual, Bellman, envelope, cyclic monotonicity, concentration, or KL?")
    print("- Is there a one-page contradiction or known decomposition?")
    print("- If yes, prove directly and run verification gates. If no, use the idea map below.")

    print("\nSelected playbooks")
    for name, score in selected:
        print(f"- {name} (score {score})")

    print("\nCentral object candidates")
    for obj, failure, assumptions, hook in idea_rows(selected):
        print(f"- object: {obj}")
        print(f"  failure: {wrap(failure)}")
        print(f"  assumptions: {wrap(assumptions)}")
        print(f"  hook: {wrap(hook)}")

    print("\nCentral lemma starters")
    for line in central_lemma_suggestions(selected).splitlines():
        print(line)

    print("\nProof kernel")
    print("- Pick the smallest lemma, certificate, or counterexample barrier that would decide the route.")
    print("- State how that kernel implies the theorem with only routine assembly left.")
    print("- Choose one evidence type: direct proof, known theorem, tool certificate, finite falsification, or local formalization.")
    print("- Name the failure shape: the counterexample or missing assumption that would make the kernel false.")

    print("\nDivergence before convergence")
    print("- For hard or previously failed proofs, compare three lanes before writing a long proof.")
    print("- Lane 1: proof route from a central object or theorem family.")
    print("- Lane 2: falsification route from the smallest failure world or boundary case.")
    print("- Lane 3: orthogonal evidence route from small cases, symbolic/tool checks, local formalization, or a nearby paper pattern.")
    print("- Continue with the lane that best controls the failure world and has a verification hook.")

    print("\nBottleneck surgery")
    print("- If the same missing lemma survives, shrink it to the smallest local lemma.")
    print("- Flip it to the negation or tight/equality case.")
    print("- Try one alternate representation: dual, slack, Bellman gap, envelope, deviation graph, coupling, KL bridge, potential, or telescope.")
    print("- Choose the highest decision-value move: proof/refutation, counterexample, missing assumption, certificate, retrieval, or theorem repair.")
    print("- Stop after one decisive artifact or two failed local moves.")

    print("\nOne-step proof move")
    print("- For a fragile kernel, try one move at a time: current subgoal, proposed move, expected new subgoal, check result.")
    print("- Keep the move only if the proof state becomes smaller or reveals a concrete theorem repair.")
    print("- If two moves leave the same subgoal unchanged, record the failed state and switch to retrieval, tool-checking, or theorem repair.")

    print("\nConstruction and algebra search")
    print("- Guess from small cases first: formula, threshold, invariant, active set, tight instance, coefficient pattern, or potential.")
    print("- Keep one holdout case that was not used to guess the pattern.")
    print("- If the small cases form a sequence, run pattern_miner.py to inspect finite differences, ratios, Newton form, and holdout behavior.")
    print("- Start from the tight or equality case: binding constraint, indifference, least favorable instance, or dominant error term.")
    print("- Try one construction seed: dual/slack variable, Bellman gap, envelope term, coupling, hard instance, potential, benchmark, or change of measure.")
    print("- Try one algebra normal form: add-subtract benchmark, gap form, ratio-to-difference, log/KL/determinant expansion, conjugate/dual, or telescope.")
    print("- Promote the guess only after holdout checks, a proof kernel, a known theorem pattern, or an independent certificate.")

    print("\nPaper-pattern trigger")
    print("- If no candidate object controls the failure world, run a bounded local-first check of prior papers, local drafts, appendices, ledgers, or formal libraries before inventing a new lemma.")
    print("- For small unclear proofs, one strong pattern or one clear mismatch is enough; use WORKSTREAMS.md only for expensive branches.")
    print("- Extract the proof architecture: failure world, pattern guess if any, central object, proof kernel or central lemma, certificate, and repair rule.")
    print("- Record reusable paper tricks as cards with source, problem shape, obstruction solved, hidden assumptions, transplant step, verification hook, and failure mode.")

    if args.include_paper_queries:
        print("\nSearch prompts")
        for query in external_pattern_queries(args.claim, selected):
            print(f"- {query}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
