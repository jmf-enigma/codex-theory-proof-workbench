---
name: theory-proof-workbench
description: "Use for hard, blocked, suspect, or previously failed theoretical proofs and proof-strategy work in OR/MS, dynamic programming, mechanism design, economic theory, learning theory, bandits, online learning, optimization, games, lower bounds, and probabilistic constructions. Use when Codex must discover or debug the mathematics, preserve failed-attempt memory, find a construction or proof kernel, coordinate tools or literature, or report an exact obstruction. Do not use merely to polish a proof whose argument is already complete."
---

# Theory Proof Workbench

Treat this skill as a proof controller, not a theorem encyclopedia. Preserve the exact claim, seek decisive evidence, remember failed states, and distinguish a proof from a plausible sketch.

Use `math-proof-writing` after the mathematical argument is complete. Use `math-tools` only for a named local artifact. For a request mixing discovery and exposition, finish proof discovery first, then write the proof.

## Nonnegotiable Rules

- Preserve variables, domains, assumptions, quantifiers, and conclusion. Mark any change as theorem repair.
- Try to refute before investing in a long proof: negate the claim, inspect boundaries, and test the smallest nontrivial case.
- Identify a proof kernel: the smallest lemma, certificate, construction, or counterexample barrier that decides the route.
- Count only evidence as progress: a proved/refuted kernel, smaller subgoal, counterexample, missing assumption, checked certificate, retrieved theorem pattern, new central object, or repaired theorem.
- Treat the same goal, assumptions, central object, and failure witness as the same proof state even when notation changes.
- Preserve solved lemmas. Repair only the failed node and affected dependents.
- Do not accept a missing lemma that restates the theorem, hides the construction, is circular, or lacks a verification hook.
- Report `lemma-conditional` or `still open` when the kernel remains unproved.

## Mode Router

Choose the lightest mode that can produce the next decisive artifact.

| Mode | Use when | Required action |
| --- | --- | --- |
| Direct | A named theorem, certificate, contradiction, or short decomposition is visible | Prove it and run final gates |
| Micro check | The proof is small but the route is unclear | Inspect one close theorem family, playbook pattern, prior ledger, or paper trick |
| Light idea | A central object, construction, or kernel is missing | Run `plan_idea.py`; use `--full` only when the compact pass is insufficient |
| Project | The proof is hard, multi-lemma, tool-assisted, or literature-dependent | Start a proof project and follow its current state |
| Recovery | The theorem has failed before | Read the existing ledger and run `proof_doctor.py` before another attempt |

Do not open a full project for routine algebra or a standard theorem application. Do not browse broadly when one close pattern already changes the next move.

## Core Loop

1. State the theorem fence: exact claim, objects, domains, assumptions, quantifiers, and conclusion.
2. Run a direct-solve check and match every theorem assumption explicitly.
3. Write the negation and test the smallest finite, scalar, boundary, symmetric, or relaxed-assumption case.
4. If the route is unclear, find the failure world, central object, proof kernel, and verification hook. Discover unknown thresholds, potentials, hard instances, coefficients, or policies before trying to prove them.
5. For a hard proof, keep two to four genuinely different routes. Change the theorem family, central object, certificate type, failure world, or evidence source.
6. Build an AND/OR lemma graph. Mark required children as AND nodes and alternative routes as OR nodes. Work the least-certain required child on the current assembly path.
7. For each fragile move, name the current subgoal, proposed move, expected artifact, check, and proof-state delta. Use the prover-verifier loop only after challenge, repetition, or hard-to-check feedback.
8. After two unchanged local attempts, choose exactly one action: repair, re-decompose, retrieve, tool-falsify, formalize locally, repair the theorem, or stop/report.
9. Assemble only proved, checked, known, or explicitly conditional nodes into the original theorem.
10. Run adversarial review and assign an honest proof status.

## Commands

Run a compact idea pass without creating files:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

Add `--full` only when the compact output does not identify a useful kernel.

Start a hard proof project:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/start_proof.py --title "SHORT NAME" --claim "CLAIM"
```

Add `--mode recovery` when the theorem has already failed.

Diagnose one primary next move before resuming a project:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/project
```

Check a possibly repeated attempt only when the match is ambiguous:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/check_attempt.py path/to/project --route-family "ROUTE" --central-object "OBJECT" --target-lemma "LEMMA" --failure-witness "WITNESS"
```

Audit the ledger before claiming a final proof:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/project/LEDGER.md
```

Use `pattern_miner.py` only for an exact small-case sequence. Use `new_lemma_card.py` and `new_trick_card.py` only after a lemma or trick has proved useful in a real route.

## Reference Router

Read only files needed by the current decision.

- For classification, read [proof-router.md](references/proof-router.md). For project state and legal transitions, read [proof-state-machine.md](references/proof-state-machine.md).
- When routes compete, read [strategy-scheduler.md](references/strategy-scheduler.md). When the central object or construction is missing, read [proof-idea-generator.md](references/proof-idea-generator.md).
- For a hard or repeatedly failed research proof, read [research-backed-proof-loop.md](references/research-backed-proof-loop.md). For unfamiliar theorem families or missing standard tricks, read [external-proof-pattern-scan.md](references/external-proof-pattern-scan.md).
- When stuck, first classify the block with [obstruction-taxonomy.md](references/obstruction-taxonomy.md), then use [proof-escalation-protocol.md](references/proof-escalation-protocol.md).
- For a challenged, repeated, or hard-to-check local move, read [prover-verifier-loop.md](references/prover-verifier-loop.md).
- Before CAS, SMT, optimization, simulation, or Lean work, read [tool-assisted-proof-patterns.md](references/tool-assisted-proof-patterns.md).
- Before finalizing, read [verification-gate.md](references/verification-gate.md).

Read at most the relevant domain playbook:

- OR/MS and optimization: [optimization-or-playbook.md](references/optimization-or-playbook.md)
- Dynamic programming and MDPs: [dp-proof-playbook.md](references/dp-proof-playbook.md)
- Mechanism design: [mechanism-design-playbook.md](references/mechanism-design-playbook.md)
- Games and matching: [games-matching-playbook.md](references/games-matching-playbook.md)
- Learning theory: [learning-theory-playbook.md](references/learning-theory-playbook.md)
- Bandits and online learning: [bandits-oco-playbook.md](references/bandits-oco-playbook.md)
- Lower bounds: [lower-bounds-playbook.md](references/lower-bounds-playbook.md)
- Probabilistic method and Lovasz Local Lemma: [probabilistic-method-playbook.md](references/probabilistic-method-playbook.md)

If classification is uncertain, run:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/select_playbook.py "CLAIM OR TOPIC"
```

## Tool Contract

Before a tool call, name the local claim, explicit domains, negation to test, backend, expected artifact, and how that artifact changes the proof.

- Use Wolfram or SymPy for exact algebra, sign conditions, quantifier elimination, and counterexamples under explicit assumptions.
- Use Python, Z3, CVXPy, OR-Tools, Sage, or NetworkX for finite witnesses, optimization certificates, and discrete structures.
- Use Lean for stable local lemmas, not as a default wrapper around the whole research theorem.
- Treat simulations as falsification or sanity checks, never as universal proof.
- Audit formal artifacts for `sorry`, admitted axioms, unresolved obligations, and missing global assembly.

Stop a tool route after two timeouts or two outputs that do not shrink or decide the proof state. Change the lemma or artifact type before calling again.

## Recovery Memory

Record only compact, decision-relevant state:

- exact claim and current proof state;
- proved, checked, false, conditional, and missing nodes;
- failed attempt signature and failure witness;
- current obstruction and proof-state delta;
- accepted counterexamples, certificates, theorem patterns, and local tricks;
- next allowed action and expected artifact.

Keep full history in the ledger, but feed the next repair only the node statement, dependencies, previous attempt signature, previous feedback, and proposed new evidence.

## Output Contract

For hard proofs, report the proof status, essential assumptions, decisive proof pattern, proof or exact obstruction, what changed since the previous failure, and the next bounded move if still open. Keep internal boards and ledgers out of the visible answer unless they help the user assess correctness.
