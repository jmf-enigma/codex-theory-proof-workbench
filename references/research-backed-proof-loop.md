# Research-Backed Proof Loop

Use this only for hard, research-level, or repeatedly failed proofs. Keep `SKILL.md` thin and load this file on demand.

## Imported Patterns

- Thin skill architecture: keep the trigger and core workflow short; move long proof tactics and references into separate files so normal use stays cheap.
- Lean-style cycle: plan, work, checkpoint, review, replan, then continue or stop. Natural-language proofs should use the same discipline even without Lean.
- Statement preservation: proving mode should not silently change theorem headers, assumptions, quantifiers, or conclusions. If a proof needs a different statement, mark theorem repair.
- Draft-Sketch-Prove: first draft the informal argument, then turn it into a proof sketch of named subgoals, then prove or repair each subgoal.
- Retrieval-augmented proving: before inventing a lemma, retrieve nearby known theorem patterns, paper lemmas, mathlib names, prior ledgers, formalization projects, and proof-agent workflows.
- Compiler/tool-guided repair: if Lean, algebra, Z3, CVXPy, Sage, or a finite example rejects a step, isolate the failing sublemma and repair that local statement.
- Proof-state feedback: try one proof move, check whether the subgoal is smaller, unchanged, or larger, and keep only moves that create a useful delta.
- Progress-aware search: do not spend unlimited effort on a route whose remaining obstruction is not shrinking.
- Lab-notebook memory: summarize failed proof states concisely so the next cycle sees the obstruction instead of rediscovering it.
- AI co-mathematician pattern: maintain a stateful workspace, treat failed workstreams as permanent project artifacts, surface uncertainty, and let the user steer when domain intuition can unlock a stalled route.
- Goal-based workstreams: define approved goals first, then create bounded workstream cards. Each card may use retrieval, computation, proof search, review, or steering as needed.
- How-others-do-it gate: before heavy execution, inspect nearby papers, appendices, prior ledgers, theorem names, analogous models, and formal-library patterns. Extract architecture and hidden assumptions, not prose.
- Tiered activation: use a micro pattern check for small unclear proofs, a workstream card for expensive branches, and a full project only when the proof needs durable state.
- Goedel-Architect blueprint pattern: plan a global dependency graph of definitions and lemmas before proving; prove nodes with only their declared parents; preserve solved nodes; diagnose failed nodes as `STATEMENT_WRONG` or `PROOF_TOO_HARD`; revise only the failed subgraph and its dependents.
- Numina/LEAP pattern: try direct formalization or direct proof first; if it fails, decompose into an AND/OR blueprint DAG, check that child lemmas are simpler and acyclic, and memoize shared subgoals.
- OProver pattern: repair from compact state, not full transcript: statement, retrieved context, previous attempt, and previous feedback. Feedback-conditioned repair beats blind regeneration.
- APOLLO pattern: preserve a useful skeleton, replace the bad block with a named sublemma, use solvers/search for routine blocks, and recursively repair only remaining gaps.
- AlphaProof Nexus pattern: maintain a small population of proof sketches, use reviewer/rater passes for decomposition quality, distinguish good gaps from bad gaps, and reuse solved or refuted subgoals.
- Formal Conjectures pattern: treat statement auditing as part of proof work. Translation, underspecification, source errors, and implicit conventions can make a formally precise theorem different from the intended one.
- MerLean-Prover pattern: keep the proof plan as the global state; use focused roles for planning, local proof, and checking; replan when faithfulness, mathematical correctness, or decomposition checks fail.

## Loop

1. Prior-result audit: list definitions, assumptions, and allowed prior theorems. A step is not allowed in the final proof unless it is a prior result, a proved lemma, or a checked derivation.
2. Pre-solve gate: check whether a direct theorem, certificate, contradiction, or known decomposition solves the claim. If it does, prove directly and verify.
3. Negation and toy model: if direct solve is not available, write what a counterexample needs, then test scalar, two-action, two-type, one-period, boundary, deterministic, and symmetric cases when available.
4. Optional idea pass: if the central route is unclear, use `proof-idea-generator.md` to propose a failure world, small-case pattern guess, central object, proof kernel or central lemma, and verification hook. Skip this when the theorem family is already obvious.
5. Retrieval: before inventing a new central lemma, search relevant playbooks, prior ledgers, local paper text, user-provided papers, paper appendices, theorem names, formal libraries, and external proof-pattern sources if available. For small unclear proofs, do this as a micro check and stop after one useful pattern or a clear mismatch. Use `external-proof-pattern-scan.md` when the proof is unfamiliar or repeatedly stuck.
6. Workstream assignment: for hard projects, fill `WORKSTREAMS.md` with approved goals and only the active workstream cards needed next. Each card must include a look-at-how-others-do-it pass or a skip reason. Keep the first pass to one to three strong sources or patterns. Use roles serially by default; use actual parallel agents only when the user explicitly asks.
7. Discovery gate: if the theorem contains an unknown construction, coefficient, threshold, policy, potential, active set, hard instance, or numerical answer, discover and self-check that object before writing a proof. Use holdout toy cases and a verification hook; do not let the proof infer the answer by wishful algebra.
8. Draft: write a rough proof in 5-10 steps. Each step must name its intended theorem family, such as convex duality, envelope, single crossing, martingale concentration, elliptical potential, or information lower bound.
9. Sketch: convert the draft into a blueprint dependency graph. Each node gets inputs, output, parents, likely proof route, tool check, status, failure mode, gap grade, and compact repair state. Independent branches should stay independent.
10. Prove locally: solve the smallest unresolved lemma first. Work one move at a time when fragile: proposed move, expected new subgoal, check, proof-state delta. Use Wolfram/SymPy for algebra, Python/Z3/CVXPy/Sage for finite or optimization checks, and Lean for local formalizable lemmas.
11. Bottleneck surgery: if the same lemma remains unresolved, shrink it, flip to the negation, change representation, then certify/falsify/retrieve/repair before another prose proof.
12. Gap review: accept a missing lemma only if it is a good gap, meaning smaller, non-circular, assumption-explicit, and checkable. If it is a bad gap, split, retrieve, falsify, or change route.
13. Repair: if a lemma fails, determine whether the issue is false claim, missing assumption, quantifier mismatch, boundary case, or proof technique mismatch.
14. Recombine: assemble only after all essential lemmas have statuses. Verify exact variables, quantifiers, constants, events, and assumptions.
15. Review: adversarially attack the proof. Try to break the weakest lemma and the final assembly.
16. Human steering checkpoint: if the obstruction is mathematical taste, model choice, definition choice, or a missing heuristic rather than a narrow check, ask the user for domain intuition before spending another heavy cycle.
17. Escalate: if two consecutive cycles make no progress, use `proof-escalation-protocol.md` to choose counterexample search, tool certification, retrieval, local formalization, theorem repair, or stop/report.

## Stop Budgets

- Small lemma: 10-20 minutes or one route plus one counterexample search.
- Medium theorem: 30-60 minutes, two proof routes, one toy/refutation pass, one tool-check pass.
- Hard/repeatedly failed proof: create a proof project, run at least two routes, and keep a ledger. Escalate after two unchanged obstruction cycles or when a missing lemma becomes the bottleneck.
- Micro pattern check: one theorem family, prior ledger, or close paper pattern; stop as soon as it yields a central object, hidden assumption, or mismatch.

## Paper-Inspired Heuristics

- Use informal proof as guidance, not authority. A plausible paragraph should become a checkable sketch before it becomes final prose.
- Use proof ideas as hypotheses, not proof steps. An idea becomes useful only when it yields a central lemma, certificate, counterexample family, or theorem repair.
- Treat guessed formulas, potentials, active sets, and algebra normal forms as conjectures until they pass a holdout case or produce an independently checkable certificate.
- Prefer premise retrieval over free invention when a proof uses standard machinery.
- Treat failed proof states as data: record the exact bad step and reuse it to avoid repeating the same route.
- Let proof-state delta govern search: if a move only renames the same missing lemma, it is not progress.
- Keep a compact failed-state note: subgoal, attempted move, why it failed, and what new ingredient would make a retry legal.
- Preserve negative results as first-class outputs. A rejected proof can still contain the right strategy, missing condition, useful counterexample, or reusable trick.
- Use coordinator-style summaries for hard projects: current claim, active routes, blocked lemma, failed routes, next bounded move, and where user steering would help.
- Keep each workstream small: first extract how similar work is done, then return one bounded artifact. Retrieval returns a pattern card, computation returns a certificate or counterexample, proof search returns a lemma status, review returns gaps, and steering returns one precise question. If none of these outputs is expected, do not open a workstream.
- For formalizable fragments, Lean-style checking is strongest on local lemmas, not necessarily on the full research theorem.
- For empirical or simulation support, route to `empirical-tools`; simulations can refute or sanity-check but do not prove the theorem.
- When searching papers or existing skills, extract route structure, certificate type, stopping rule, and failure repair rule. Do not import unexplained claims as proof steps.
- When a proof attempt fails, require a structured forfeit: diagnosis, forensic analysis, and suggested fix. If the statement is false, repair/drop it. If the proof is too hard, split it into helper lemmas.
- When a local proof skeleton is coherent but a block fails, "sorrify" the block: name it as a lemma, preserve the good skeleton, and repair only the isolated lemma.
- When several routes are plausible, keep a small candidate board rather than one long monologue. Rate each route by plausibility, novelty, decomposition quality, evidence, and risk of circularity.

## Source Log

- Claude Code skills documentation: thin `SKILL.md`, supporting files, lifecycle, and dynamic context ideas.
- Lean 4 skills workflow pack: draft/formalize/prove/autoprove/review/repair cycle, explicit stop budgets, and LSP-first verification discipline.
- Lean Copilot and LeanDojo: tactic suggestion, proof search, premise selection, and proof-state feedback are useful patterns even for informal research proofs.
- AxProver-style loop: proposer, compiler, reviewer, and compact failed-attempt memory prevent repeated proof-state failures.
- Draft, Sketch, and Prove: informal proofs can guide formal proof sketches and reduce proof search to easier subproblems.
- LeanDojo/ReProver: retrieval of accessible premises is a central bottleneck and improves theorem proving.
- APOLLO: compiler-guided repair, sublemma isolation, solver use, recombination, and controlled attempt budgets.
- Goedel-Architect (Chung et al., 2026): blueprint generation and refinement, node-level proving with declared dependencies, negated sub-lemmas, structured forfeits, and solved-node preservation.
- Numina-Lean-Agent (Liu et al., 2026): general agent harness, theorem retrieval, proof-state tools, informal-prover generator/verifier loop, discussion partner, and blueprint refinement.
- OProver (2026): feedback-conditioned refinement with compact state, retrieval memory of verified proofs, and test-time depth/width tradeoff.
- LEAP (2026): direct-first proving, AND/OR proof DAG, decomposition review, shared subgoal memoization, and acyclicity checks.
- Discover and Prove (2026): separate answer/construction discovery from proof verification for hard-mode problems.
- AlphaProof Nexus (DeepMind, 2026): evolutionary proof sketches, good-gap/bad-gap review, rater-guided route selection, and solved/refuted goal cache.
- Formal Conjectures (DeepMind, 2026): statement-fidelity auditing, `answer(sorry)`-style separation of discovery from proof, and misformalization taxonomy.
- MerLean-Prover (Li, Zhu, Ren, 2026): proof-plan global state, planning/proving/checking roles, faithfulness checks, mathematical-correction checks, and decomposition-driven replanning.
- LeanSearch-style global premise retrieval: sketch-retrieve-reflect cycles help find scattered lemma sets.
- BFS-Prover-style route search: simple best-first expansion can be useful when many subgoals compete for attention.
- ExVerus-style counterexample repair: concrete failures can suggest the invariant or assumption needed to repair a proof.
- Liquid Tensor/Flyspeck: large proofs need a blueprint/dependency graph and checked certificates for external computation.
- Theorem Proving in Lean: formal checking requires every claim to be justified by definitions, axioms, or prior theorems.
- Montana State proof guidelines: expand definitions, use prior results, test conjectures by examples, and search counterexamples to failed steps.
- Zheng et al. 2026, AI co-mathematician: stateful mathematical workspace, asynchronous workstreams, uncertainty management, failed-exploration preservation, reviewer loops, and human steering.
