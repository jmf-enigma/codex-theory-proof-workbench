# Tool-Assisted Proof Patterns

Use this for hard proofs where computation, CAS, SMT, optimization solvers, or Lean may help. The goal is not to "ask tools for a proof"; it is to turn tool output into a smaller human-checkable lemma, certificate, counterexample, or theorem repair.

## Map

- Imported patterns and tool roles: choose the backend by expected artifact.
- Tool plan and default loop: refute, shrink, run the narrowest query, translate.
- Artifact translation and domain recipes: convert output into a proof step or repair.
- Stop rules: avoid trusting numerical evidence or repeated timeouts.

## Imported Patterns

- **Lean/Goedel blueprint pattern**: maintain a human-readable proof map and a machine-checkable or reviewer-checkable dependency graph. Each node has a statement, declared parents, status, and failure diagnosis. Prove or check a node using only its declared parents unless explicitly rewiring the graph.
- **Flyspeck pattern**: combine a human proof with formal verification and external computations only when every computational step has a checked certificate or proof object.
- **CAS refutation pattern**: before simplifying a theorem, ask for a counterexample to the theorem's negation under explicit domains.
- **Certificate pattern**: prefer certificates that can be independently checked: dual variables, KKT conditions, exact rational identities, interval bounds, SMT models/unsat cores, or Lean proof terms.
- **Premise-retrieval pattern**: when a lemma feels standard, search for the nearest theorem pattern or library lemma before inventing a new proof.
- **Repair-loop pattern**: when a tool rejects a step, preserve the failed subgoal, extract the smallest missing lemma, then retry only that lemma.

## Tool Roles

- **Wolfram**: symbolic simplification, quantifier elimination, condition discovery, inequality checks, FOCs/KKT algebra, counterexample search with `FindInstance`.
- **Python/SymPy/flint/gmpy2**: exact rational algebra, polynomial coefficient checks, finite stress tests, high-precision sanity checks.
- **Z3/cvc5/PySAT**: finite/integer/Boolean counterexamples, IC/IR feasibility, small-model search, discrete impossibility.
- **CVXPy/OR-Tools**: primal/dual optimization sanity checks, finite LP/MIP certificates, policy/capacity/matching counterexamples.
- **Sage**: exact combinatorics, graph/algebra/finite-field/group computations.
- **Lean/mathlib**: local formalization of stable lemmas once the informal statement is precise.
- **Empirical/simulation tools**: falsification and sanity checks only; they do not prove universal claims.

## Tool Plan Template

For each proof-critical step, write:

- lemma or claim fragment:
- assumptions/domains:
- negation to test:
- backend:
- query or script:
- expected artifact: counterexample, `True`, conditions, dual certificate, unsat result, exact identity, Lean proof.
- how the artifact becomes a proof step:
- failure interpretation:

If the expected artifact is only "numerical evidence," the step is not proof-ready.

## Default Tool Loop

1. **Normalize** the claim: remove ambiguous notation, name domains, list boundary cases.
2. **Refute first**: test the negation in the smallest scalar, finite, boundary, or relaxed-assumption model.
3. **Guess a pattern if needed**: use exact small cases, active sets, coefficient sequences, symbolic simplification, or optimized witnesses to infer a construction, invariant, or algebra normal form. If the evidence is a sequence, run `scripts/pattern_miner.py` before treating the guess as a candidate lemma.
4. **Hold out a case**: test at least one small case that was not used to guess the pattern.
5. **Shrink** the theorem into one or more tool-checkable lemmas.
6. **Pick artifact type** before running the tool.
7. **Run the narrowest query**: avoid global simplification on a full theorem. For multiple candidate lemmas, try the hardest boundary case or the most certificate-friendly subgoal first.
8. **Translate** tool output into a lemma, missing assumption, counterexample, or certificate.
9. **Independently check** proof-critical artifacts when feasible: symbolic plus numeric, CAS plus exact arithmetic, LP solution plus dual certificate, informal proof plus Lean.
10. **Record** command, assumptions, result, and translation in `TOOL_PLAN.md` and `LEDGER.md`.

## Artifact Translation

- `FindInstance` returns an instance: the theorem is false under current assumptions.
- `FindInstance` returns `{}`: no counterexample found in that theory/search scope; not a proof unless the backend solved the quantified formula completely.
- `Reduce`/`Resolve` gives conditions: these are candidate assumptions or case splits, not prose by themselves.
- `FullSimplify[..., assumptions] == True`: a proof-critical algebraic step is strongly checked under those assumptions; still state the algebraic lemma.
- Numerical optimizer returns a solution: use it to guess active constraints, then prove KKT/duality/convexity or construct an exact certificate.
- LP/MIP/SMT feasible model: use it as a counterexample or witness.
- LP dual variables or Bellman inequalities: convert to a certificate that a human can verify line by line.
- Lean accepts a lemma: status becomes `formalized-local`; still explain how the lemma fits the paper proof.
- Lean fails: inspect the failed subgoal; often it reveals a missing assumption, coercion/domain issue, or too-strong statement.

## Domain Recipes

### Optimization / OR/MS

- Use tools to guess active sets, simplify KKT conditions, and search boundary failures.
- Final proof needs convexity/concavity, constraint qualification, feasibility, and a primal-dual/KKT certificate.
- For nonconvex problems, numerical optima are only conjecture generators unless paired with a global argument.

### Dynamic Programming / MDP

- Use finite-state Python/LP to test Bellman inequalities and policy structure.
- Use Wolfram for Q-value difference signs and threshold boundaries.
- Final proof needs Bellman equality for the candidate policy and Bellman inequality for deviations, with boundary/tie cases.

### Mechanism Design / Econ

- Use finite type grids and LP/Z3 for IC/IR feasibility and deviation search.
- Use Wolfram for envelope derivatives, virtual values, and payoff differences.
- Final proof needs monotonicity/cyclic monotonicity, payment construction, and boundary IR.

### Learning Theory / Bandits

- Use Python to stress-test finite horizons and constants; use Wolfram/SymPy for summation and tuning.
- Use Lean only for stable local inequalities or algebraic lemmas.
- Final proof needs a named good event, failure probability, instantaneous bound, summation/telescope, and exact quantifier type.

### Lower Bounds

- Use tools to tune hard instances and KL/TV expressions.
- Final proof needs feasible instances, closeness bound, separation bound, and testing-to-risk transfer.

## Stop Rules

- If a tool query times out twice, shrink the lemma or change artifact type.
- If two tools disagree, inspect domains, numeric precision, branch cuts, and boundary assumptions before trusting either.
- If the same missing assumption appears in two tool outputs, repair the theorem statement before drafting prose.
- If no artifact can be translated into a proof step, report `still open` with the smallest remaining lemma.

## Source Patterns

- Lean/mathlib projects: blueprint, premise retrieval, local formalization, proof-state repair.
- Liquid Tensor Experiment: human-readable blueprint linked to Lean formalization.
- Flyspeck/Kepler: formal proof plus checked external computation and nonlinear inequality certification.
- Wolfram theorem proving: `FindInstance`, `Reduce`, `Resolve`, and simplification under explicit assumptions.
