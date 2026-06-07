# Proof State Machine

Use this to keep a hard proof moving instead of looping.

## States

- `S0-parse`: exact claim, notation, quantifiers, domains, and statement fence.
- `S1-classify`: target type, direct-solve check, and candidate theorem families.
- `S2-stress-test`: negation, edge cases, finite/numeric examples, relaxed assumptions.
- `S2b-idea-map`: optional state for unclear or repeatedly failed proofs; propose failure world, small-case pattern guess, central object, proof kernel, central lemma, and verification hook.
- `S3-route-portfolio`: at least two plausible proof routes with switch rules.
- `S4-lemma-graph`: theorem reduced to a blueprint-style dependency graph of definitions, lemmas, and theorem assembly nodes with declared parents and statuses.
- `S5-local-certification`: check fragile lemmas with tools, known theorems, or one-step proof-state feedback.
- `S6-assembly`: combine lemmas into the exact target statement.
- `S7-adversarial-review`: try to break assumptions, quantifiers, boundary cases, and conclusion.
- `S8-finalize`: final proof with verification status.
- `S9-stuck`: exact obstruction named, next experiment chosen.

## Transitions

- `S0 -> S1`: all variables, domains, quantifiers, assumptions, and the no-silent-statement-change rule are explicit.
- `S1 -> S2`: at least one theorem family or proof route is plausible.
- `S1 -> S8`: direct theorem, certificate, contradiction, or known decomposition proves the claim and verification gates pass.
- `S2 -> refuted`: counterexample found.
- `S2 -> S3`: no counterexample found and assumptions look coherent.
- `S2 -> S2b`: no obvious central route or the same obstruction has appeared before.
- `S2b -> S3`: one proof kernel or candidate central lemma has a verification hook; if an unknown construction or answer is required, it has passed a holdout/self-check.
- `S3 -> S4`: route has a decomposable proof skeleton.
- `S4 -> S5`: all nontrivial steps are lemma candidates with declared dependencies, statuses, expected evidence artifacts, gap grades, and compact repair states for failed nodes.
- `S5 -> S6`: each essential lemma is proved, tool-checked, or explicitly marked conditional.
- `S6 -> S7`: assembled proof matches the exact claim.
- `S7 -> S8`: review finds no unhandled gaps.
- any state -> `S9`: a named obstruction blocks progress.
- `S9 -> S1/S2/S3/S4`: reclassify, search counterexample, switch route, or isolate missing lemma.

## Anti-Loop Rule

After two failed attempts, do not continue prose proof. Update the ledger with:

- current state,
- named obstruction,
- failed routes,
- failed proof state if the last move left the same subgoal unchanged,
- smallest toy version,
- next experiment.

Then apply `proof-escalation-protocol.md`: tool falsification, retrieval, local formalization, theorem repair, or stop/report.

## Research-Level Overlay

For proofs that have already failed or look paper-level, run `S3 -> S6` as a Draft-Sketch-Prove cycle:

- Draft: write the informal proof idea in 5-10 steps, including the theorem family each step is supposed to use.
- Sketch: convert the draft into named subgoals/lemmas, each with inputs, output, and likely prior result.
- Prove: fill or refute the subgoals one by one; for fragile kernels, try one move at a time and record whether the subgoal became smaller.
- Repair: when a subgoal fails, classify the exact failure, weaken the lemma or add the missing assumption, then recombine.
- Blueprint refinement: preserve solved nodes, diagnose failed nodes as false statement or too-hard proof, then rewrite only the failed node and its dependents.
- Good-gap review: do not accept a missing lemma unless it is smaller than its parent, non-circular, assumption-explicit, and checkable.
- Compact repair: the next repair should use the node statement, parents, previous attempt signature, previous feedback, and suggested fix, not the full failed transcript.

Do not polish final prose until every sketch subgoal is `proved`, `tool-checked`, `known`, or explicitly `missing`.
