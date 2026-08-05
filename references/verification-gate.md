# Verification Gate

Use this file before presenting a hard proof as correct.

## Proof Status Ladder

- `conjecture`: intuition or pattern match only.
- `counterexample-tested`: no counterexample found in toy/numeric/finite searches.
- `lemma-conditional`: final theorem follows if named missing lemmas hold.
- `human-proof`: every nontrivial step is justified in prose by a theorem, lemma, or derivation.
- `tool-checked`: fragile algebra/optimization/discrete constraints were checked by Wolfram, Python, Z3, CVXPy, Sage, or similar.
- `formalized-local`: key local lemmas were checked in Lean.
- `formalized-complete`: full theorem is Lean-checked or otherwise machine-formalized.

Never call a proof "proved" if it is only `conjecture`, `counterexample-tested`, or `lemma-conditional`.

## Required Gates

1. Pre-solve gate: record whether a direct theorem, certificate, contradiction, or known decomposition was available before broader search.
2. Statement gate: verify the proof proves the exact original theorem. Any changed assumption, quantifier, domain, or conclusion must be marked as theorem repair.
3. Assumption gate: list all compactness, continuity, convexity, measurability, independence, boundedness, support, tie-breaking, differentiability, and domain assumptions used.
4. Negation gate: write what a counterexample would need to satisfy.
5. Toy-model gate: test finite/small-dimensional/symmetric/boundary cases when the statement permits it.
6. Pattern gate: if a formula, construction, active set, potential, or algebra normal form was guessed from examples, check a holdout case or independent certificate before using it as a lemma.
7. Lemma gate: every non-obvious proof step must point to a named lemma, theorem pattern, tool check, or explicit derivation.
8. Proof-state gate: for fragile kernels, record the current subgoal, one proposed move, check result, and whether the remaining subgoal became smaller.
9. Step-verdict gate: for multi-step plans, tag each step as tool-verified, easy-to-check, or hard-to-check; then record goal gate, logic gate, challenge/replan budget, and verdict: accept, challenge, trace-back, re-decompose, re-plan, or stop. For prover-verifier loops, also record the prover move, verifier verdict, soundness probe, proof-state delta, and coordinator decision.
10. Quantifier gate: check whether the claim is pointwise, uniform, in expectation, high probability, almost surely, asymptotic, or finite-sample.
11. Boundary gate: check zero denominators, inactive/active constraints, ties, support endpoints, nonunique optimizers, and event complements.
12. Assembly gate: verify the proved lemmas imply exactly the user claim, not a nearby weaker/stronger statement.
13. Review gate: run an adversarial pass that tries to break the proof before writing the final answer.
14. Progress gate: if the same obstruction survives two cycles, stop polishing and either isolate the missing lemma, weaken the theorem, or return `still open`.
15. Novelty gate: for a repeated proof, state what changed since the last failed attempt. Acceptable changes are a new central object, theorem family, certificate, counterexample, missing assumption, verified trick, tool artifact, or theorem repair.
16. Decision-value gate: before another long proof attempt, state the artifact it is expected to produce. If there is no expected artifact, choose counterexample search, retrieval, local formalization, theorem repair, or stop.
17. Formal artifact gate: if Lean or a formal-proving API was used, check for `sorry`, admitted or unexpected axioms, unsafe shortcuts, incomplete declarations, unproved theorem dependencies, and whether verified helper lemmas actually imply the original theorem. Record an expected axiom allowlist or footprint and isolate every external trust assumption; kernel validity, trust footprint, and statement fidelity are separate checks.
18. Decomposition gate: before accepting child lemmas, check parent sufficiency, strict simplification, acyclicity, source fidelity, repair radius, and premise feasibility.
19. Verifier-diversity gate: do not upgrade confidence because similar verbal reviewers agree. A model judge is never the sole acceptance or refutation channel; rejection must identify a concrete first error or witness. Derive atomic acceptance obligations from the problem and require a different evidence channel for the fragile kernel when feasible; a longer prose rubric is not additional evidence.
20. Definition-sanity gate: when the theorem introduces custom objects or formal definitions, prove easy expected variants and boundary/API lemmas before trusting a difficult target built on them.
21. Semantic-obligation gate: decompose custom definitions and exact counting, feasibility, closure, multiplicity, support, or object-type requirements into atomic obligations; verify that every reduction and construction preserves them.
22. Completion-coverage gate: map every acceptance-contract item, required edge case, and reduction obligation to the proof node or certificate that discharges it. Any uncovered required row prevents complete-proof status.
23. Hypothesis-lineage gate: classify every assumption, binder, quantifier, semantic convention, or definition field introduced after the theorem fence as original/source-explicit, source-implied, an encoding adapter, or theorem repair. Compilation must not launder an unresolved obligation into a hypothesis or definition.
24. Reusable-formalization gate: only when the output is intended as library code, review whether definitions are mathematically natural, theorem statements have useful generality, namespaces support search, and a small API avoids downstream unfolding. This gate measures reuse quality, not theorem truth.

## Adversarial Review Checklist

- Did any step assume interior optimum when boundary solutions exist?
- Did any monotonicity argument require increasing differences or single crossing?
- Did any fixed-point theorem require compact convex values, closed graph, or upper hemicontinuity?
- Did any envelope theorem require absolute continuity, differentiability, or IC regularity?
- Did any regret proof ignore the failure event or misuse adaptively collected data as independent?
- Did any lower bound choose instances too far apart, making the KL argument weak?
- Did any limit exchange require domination, uniform convergence, tightness, or monotone convergence?
- Did any optimization proof confuse necessary FOC/KKT conditions with sufficiency?
- Did any proof of uniqueness rely only on weak concavity or weak monotonicity?
- Did the proof retry the same missing lemma with only different notation or a stronger unsupported claim?
- Did the hardest algebra step have a sign, equality case, certificate, or alternate representation?
- Did a local step prove its declared goal, or only prove something true but irrelevant?
- Did the verifier only approve a local-looking argument without checking goal match, proof-state delta, soundness probe, and final assembly?
- Did a formal artifact verify only local helper lemmas while leaving the main theorem, counting step, or global assembly obligation open?
- Did two routes reach equivalent proof states under different notation or variable names?
- Did a proposed child lemma actually simplify the parent, or merely unfold and refold the same statement?
- Could one false child force a wholesale rewrite because the decomposition has a large repair radius?
- Did retrieval produce a jointly sufficient premise set, or only individually similar theorems?
- Did formalization invent placeholder objects because the required library theory was absent?
- Did a reduction preserve the exact object class and every semantic obligation, or did it solve a cleaner neighboring problem?
- Does each required edge case and acceptance item have a named place in the final proof rather than an implicit promise?
- If Peppy/PEPFlow was used, did the encoding match the exact algorithm, class, initial condition, performance metric, and horizon in the theorem?
- Was a numerical sweep or floating-point dual kept below proof status until an exact certificate, sign conditions, and final theorem assembly were checked?
- Was the evaluator exhaustive for the stated theorem, or did a pass only mean no violation on a finite, sampled, or proxy suite?
- If the proof was formalized, did the recorded axiom footprint match the allowlist, and were real-world oracle or data assumptions kept outside the proved core?
- Did a failed proof become compilable only because its missing obligation was moved into a new hypothesis, structure field, or weakened definition?
- If reusable formal code is claimed, would another theorem use its definitions and API without transport through application-specific wrappers?

## Missing Lemma Search

When a proof is stuck on a lemma:

1. Prove a scalar/two-action/two-type/single-period version.
2. Try the contrapositive or dual statement.
3. Search for the closest theorem pattern in `proof-router.md`, relevant playbooks, prior ledgers, and any paper/theorem names already in the problem context.
4. Check whether strengthening assumptions makes the lemma true.
5. Try to refute the lemma with finite or numerical counterexamples.
6. If the lemma is true only with extra conditions, state a conditional theorem.
7. If two attacks on the lemma fail, try the negation, a finite search, a retrieved theorem pattern, or a weaker repaired lemma before another prose attempt.

## Final Answer Gate

For a hard proof, the final answer should include:

- proof status from the ladder,
- essential assumptions,
- proof pattern,
- lemma graph with statuses,
- any formal artifact status, including unresolved `sorry`/admitted obligations if present,
- any theorem repair or non-original assumption and its lineage,
- counterexample searches attempted,
- proof or exact obstruction,
- novelty since the last failed route, if applicable,
- confidence level and what would raise it.
