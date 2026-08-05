---
name: theory-proof-workbench
description: "Use for hard, blocked, suspect, previously failed, open, or unknown-answer theoretical problems in OR/MS, dynamic programming, mechanism design, economic theory, learning theory, bandits, online learning, optimization, games, lower bounds, and probabilistic constructions. Use when Codex must discover or debug mathematics, find an unknown construction or proof kernel, preserve failed-attempt memory, coordinate tools or literature, or report an exact obstruction. Do not use merely to polish a proof whose argument is already complete."
---

# Theory Proof Workbench

Treat this skill as a proof controller, not a theorem encyclopedia. Preserve the exact claim, seek decisive evidence, remember failed states, and distinguish a proof from a plausible sketch.

Use `math-proof-writing` after the mathematical argument is complete. Use `math-tools` only for a named local artifact. For a request mixing discovery and exposition, finish proof discovery first, then write the proof.

## Nonnegotiable Rules

- Preserve variables, domains, assumptions, quantifiers, and conclusion. Mark any change as theorem repair.
- Classify any post-failure assumption, binder, quantifier, semantic convention, or definition as source-explicit, source-implied, an encoding adapter, or theorem repair; compilation cannot hide assumption or definition drift.
- At the theorem fence, define an acceptance contract: exact success criterion, admissible objects or operations, required edge cases, tempting near-misses that do not count, and atomic semantic obligations every reduction or construction must preserve.
- Try to refute before investing in a long proof: negate the claim, inspect boundaries, and test the smallest nontrivial case.
- Identify a proof kernel: the smallest lemma, certificate, construction, or counterexample barrier that decides the route.
- Count only evidence as progress: a proved/refuted kernel, smaller subgoal, counterexample, missing assumption, checked certificate, retrieved theorem pattern, new central object, or repaired theorem.
- Calibrate a discovery evaluator on known-valid and known-invalid candidates before recording its scope and pass/fail implications. Passing a sampled, finite, proxy, or incomplete evaluator does not prove a broader theorem.
- Treat the same goal, assumptions, central object, and failure witness as the same proof state even when notation changes.
- Preserve solved lemmas. Repair only the failed node and affected dependents.
- Do not accept a missing lemma that restates the theorem, hides the construction, is circular, or lacks a verification hook.
- Treat model memory as `unverified`, never as evidence that a result is known or open. Before frontier classification, search external literature and verify source anchors against DOI/publisher, arXiv, proceedings, or another official page.
- For a known/open/new classification, require `literature/frontier-evidence.json`: executed Scholar evidence, a hashed lawful full text, exact theorem/proof anchors, and one proof-derived solution card. Hand-written status fields are not verification.
- A model reviewer is advisory. It cannot upgrade status without a problem-derived obligation audit and a different evidence channel; rejection requires a concrete first error or witness. Formal artifacts also need an axiom and external-trust audit.
- Report `lemma-conditional` or `still open` when the kernel remains unproved.

## Mode Router

Choose the lightest mode that can produce the next decisive artifact.

| Mode | Use when | Required action |
| --- | --- | --- |
| Direct | A named theorem, certificate, contradiction, or short decomposition is visible | Prove it and run final gates |
| Micro check | The proof is small but the route is unclear | Inspect one close theorem family, playbook pattern, prior ledger, or paper trick |
| Light idea | A central object, construction, or kernel is missing | Run `plan_idea.py`; use `--full` only when the compact pass is insufficient |
| Discovery | The answer, extremal object, formula, or decisive concept is genuinely unknown | Define a candidate representation, evaluator, simplification ladder, and promotion gate before proof |
| Project | The proof is hard, multi-lemma, tool-assisted, or literature-dependent | Start a proof project and follow its current state |
| Recovery | The theorem has failed before | Read the existing ledger and run `proof_doctor.py` before another attempt |

Do not open a full project for routine algebra or a standard theorem application. Do not browse broadly when one close pattern already changes the next move.

## Core Loop

1. State the theorem fence and acceptance contract: exact claim, objects, domains, assumptions, quantifiers, conclusion, required edge cases, excluded near-misses, and atomic semantic obligations under every reduction or construction.
2. Run a direct-solve check and match every theorem assumption explicitly.
3. Write the negation and test the smallest finite, scalar, boundary, symmetric, or relaxed-assumption case.
4. If the route is unclear, find the failure world, central object, proof kernel, and verification hook. If the answer or object may be unknown, first run an external frontier scan for exact and neighboring results, recent cited-by work, and active public projects. Then separate discovery from proof: define what generates candidates, how they are evaluated, and what evidence freezes one candidate as the theorem target.
5. For a hard proof, seed two to four routes independently before naming a favorite. Register them by mathematical mechanism rather than wording, give each one expected artifact and its cheapest decisive evaluator, then compare them. Keep one incompatible shadow family alive until the leading kernel is proved, refuted, or blocked, and rebalance after each bounded round.
6. Build an AND/OR lemma graph. Admit a decomposition only when the children conditionally imply the parent, are strictly simpler, acyclic, faithful, and locally repairable. Work the least-certain required child on the current assembly path.
7. For each fragile move, name the subgoal, move, expected artifact, check, and proof-state delta. Formal tasks begin with one generate-check-repair loop; escalate only after it stalls and only to assemblable children. Activate the prover-verifier loop after challenge, repetition, or hard-to-check feedback. For a complete challenged candidate or fragile global assembly, prepare a fresh-context referee packet. Run it only when the host permits and the user approved sharing; otherwise run a local adversarial audit plus exact replay, record `fresh-context-unavailable`, and keep status below independent review.
8. On failure, locate the first invalid step, preserve the verified prefix and independent helper lemmas, and separate the reported diagnostic site from the inferred root cause. Then classify the failure as strategy, decomposition, premise retrieval, local proof, assembly, fidelity, or library coverage before repairing that layer.
9. After two unchanged local attempts, choose exactly one action: repair, re-decompose, retrieve, tool-falsify, formalize locally, repair the theorem, or stop/report. Block a route that merely moves the theorem into a theorem-strength missing lemma; reopen it only with a materially new mechanism, invariant, construction, representation, or premise.
10. Assemble only proved, checked, known, or explicitly conditional nodes into the original theorem.
11. Map every acceptance obligation and edge case to a proved or checked node, derive a problem-specific audit checklist from the definitions and reductions, run adversarial review, and assign an honest proof status.

## Commands

Run a compact idea pass without creating files:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/plan_idea.py" "CLAIM"
```

Add `--full` only when the compact output does not identify a useful kernel.

Start a hard proof project:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/start_proof.py" --title "SHORT NAME" --claim "CLAIM"
```

Add `--mode recovery` when the theorem has already failed. Add `--mode discovery` when the answer or central object is not yet known.

Diagnose one primary next move before resuming a project:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/proof_doctor.py" path/to/project
```

Load only compact active state when resuming:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/proof_runtime.py" brief path/to/project --markdown
```

This initializes `.proof_runtime` automatically for an older project. If `routing.json` or `claim.md` intentionally changes the theorem, adopt it explicitly with `proof_runtime.py revise-claim path/to/project --reason "REASON"`; this resets active proof status instead of reusing stale evidence.

For a complete, challenged candidate, prepare the exact fresh-context referee packet first. `--prepare-only` is local; omitting it invokes another Codex process and is allowed only after the sharing condition above is satisfied:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/run_referee.py" path/to/project --proof writeup/candidate.md --prepare-only
```

Missing packet premises are `uncertain`, not a mathematical refutation. After a referee pass, rerun `proof_doctor.py`: it targets the recorded first unsupported dependency and lists passed computation claims that must not be retried.

Check a possibly repeated attempt only when the match is ambiguous:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/check_attempt.py" path/to/project --route-family "ROUTE" --central-object "OBJECT" --target-lemma "LEMMA" --failure-witness "WITNESS"
```

Before claiming a final proof, rerun the doctor so missing or tampered runtime evidence cannot survive on ledger text alone, then audit the ledger:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/proof_doctor.py" path/to/project
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/audit_ledger.py" path/to/project/LEDGER.md
```

Use `pattern_miner.py` only for an exact small-case sequence. Use `new_lemma_card.py` and `new_trick_card.py` only after a lemma or trick has proved useful in a real route.

For discovery evidence, read [full-text-frontier-evidence.md](references/full-text-frontier-evidence.md) and use `frontier_evidence.py`; `proof_doctor.py` validates the bundle before candidate search. Treat INFORMS and SSRN pages as identity/version anchors first: resolve DOI and lawful mirrors automatically before asking for browser authentication.

## Reference Router

Read only files needed by the current decision.

- For classification, read [proof-router.md](references/proof-router.md). For project state and legal transitions, read [proof-state-machine.md](references/proof-state-machine.md).
- When routes compete, read [strategy-scheduler.md](references/strategy-scheduler.md). When the central object or construction is missing, read [proof-idea-generator.md](references/proof-idea-generator.md). When the answer, object, or concept may be unknown or open, read [novel-problem-discovery.md](references/novel-problem-discovery.md), then [full-text-frontier-evidence.md](references/full-text-frontier-evidence.md) only for the evidence pass; use `citation-tools` for Scholar-backed discovery and authoritative metadata.
- For a hard or repeatedly failed research proof, or when adapting AI-assisted proof-search methods, read [research-backed-proof-loop.md](references/research-backed-proof-loop.md). For unfamiliar theorem families or missing standard tricks, read [external-proof-pattern-scan.md](references/external-proof-pattern-scan.md).
- When stuck, first classify the block with [obstruction-taxonomy.md](references/obstruction-taxonomy.md), then use [proof-escalation-protocol.md](references/proof-escalation-protocol.md).
- For a challenged, repeated, or hard-to-check local move, read [prover-verifier-loop.md](references/prover-verifier-loop.md).
- Before CAS, SMT, optimization, simulation, or Lean work, read [tool-assisted-proof-patterns.md](references/tool-assisted-proof-patterns.md).
- For a fixed-algorithm worst-case rate, PEP certificate, or all-horizon Lyapunov construction, read [peppy-proof-bridge.md](references/peppy-proof-bridge.md) only after its eligibility gate passes, then invoke the companion `peppy` skill.
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
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/select_playbook.py" "CLAIM OR TOPIC"
```

Run the integrated smoke test after modifying the skill:

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/smoke_workbench.py"
```

## Tool Contract

Before a tool call, name the local claim, explicit domains, negation to test, backend, expected artifact, and how that artifact changes the proof.

- Use Wolfram or SymPy for exact algebra, sign conditions, quantifier elimination, and counterexamples under explicit assumptions.
- Use Python, Z3, CVXPy, OR-Tools, Sage, or NetworkX for finite witnesses, optimization certificates, and discrete structures.
- Use Peppy/PEPFlow only for an exactly encoded fixed-algorithm performance problem. Treat Block 1 sweeps as conjecture discovery and promote a certificate only through the gates in [peppy-proof-bridge.md](references/peppy-proof-bridge.md).
- Use Lean for stable local lemmas, not as a default wrapper around the whole research theorem.
- Treat simulations as falsification or sanity checks, never as universal proof.
- Audit formal artifacts for `sorry`, admitted axioms, unresolved obligations, and missing assembly; if reuse is intended, also audit definitions, theorem generality, namespaces, and API surface.
- Direct tool calls may explore or falsify. Before a proof-critical computation upgrades status, put the query in a project-local script and use `computation_artifact.py record`, `replay`, and `audit` to bind its inputs, assumptions, backend version, output check, executable fingerprint, and current local presence. If a stricter artifact replaces stale evidence, append an explicit `supersede` event; never delete history or infer replacement from similar names. Exact counterexamples, symbolic identities, condition sets, and solver certificates require canonical exact-output comparison; exit code alone proves only that the process finished. A batch driver must fail on any child timeout, nonzero exit, output mismatch, or unexpected child stderr instead of reporting only a final `True`.
- A fresh-context referee reduces anchoring but is still model review, not formal verification. Promote only the mathematical artifacts it actually checks.

Stop a tool route after two timeouts or two outputs that do not shrink or decide the proof state. Change the lemma or artifact type before calling again.

## Recovery Memory

Record only compact, decision-relevant state:

- exact claim and current proof state;
- proved, checked, false, conditional, and missing nodes;
- failed attempt signature and failure witness;
- current obstruction and proof-state delta;
- first failing step, verified prefix, and independently rescued artifacts;
- failure stage and its layer-specific repair;
- accepted counterexamples, certificates, theorem patterns, and local tricks;
- next allowed action and expected artifact.

Keep full history in the ledger. On resume, read the compact `.proof_runtime` brief first; open older ledger sections only when the current node needs them. Feed the next repair only the node statement, dependencies, previous attempt signature, previous feedback, and proposed new evidence.

## Output Contract

For hard proofs, report the proof status, essential assumptions, decisive proof pattern, proof or exact obstruction, what changed since the previous failure, and the next bounded move if still open. Keep internal boards and ledgers out of the visible answer unless they help the user assess correctness.
