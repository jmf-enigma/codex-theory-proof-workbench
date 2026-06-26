# Probabilistic Method Playbook

Use for existence proofs by random construction, bad-event avoidance, Lovasz Local Lemma, alteration, dependency graphs, random coloring, hypergraph/coloring arguments, and union bounds that are too loose.

## Branch Split

- Direct union bound: define bad events and show the sum of probabilities is below 1.
- Alteration: sample a random object, count violations, then delete/repair a small set.
- Symmetric Lovasz Local Lemma: bound every bad-event probability by `p`, maximum dependency degree by `d`, and check `e p (d+1) <= 1`.
- Asymmetric LLL: assign witnesses `x(A)` and check `Pr[A] <= x(A) product_{B in Gamma(A)} (1-x(B))`.
- Lopsided LLL: use when events are not independent but negative/lopsided dependence makes the ordinary dependency graph too pessimistic.
- Algorithmic LLL: if the proof needs a construction, identify variables, bad events, and a Moser-Tardos-style resampling step.

## Smart Routes

- Union bound too loose: localize dependencies and try LLL before inventing a new object.
- Bad events too likely: change the random distribution, split events into smaller events, or use alteration.
- Dependency degree too large: refine the dependency graph, exploit lopsided dependence, expose fewer random variables, or group constraints.
- Existence without construction: decide whether nonconstructive LLL is enough; if not, switch to Moser-Tardos resampling or a deterministic derandomization route.
- Random coloring proof stuck: define forbidden monochromatic structures, compute event probabilities, and count overlapping structures.
- Matching/packing proof stuck: define conflict events and check whether conflicts are local enough for LLL or resampling-oracle variants.

## Common Lemmas

- Random object distribution is explicit and satisfies all model constraints before conditioning.
- Bad events exactly cover failure of the desired property.
- Each bad-event probability is correctly bounded under the chosen distribution.
- The dependency graph is valid: every event is independent of all non-neighbors.
- Symmetric or asymmetric LLL numerical condition holds with stated constants.
- Constructive claim has a resampling algorithm whose bad-event variables and termination assumptions match Moser-Tardos.
- Alteration step repairs all bad events without destroying the desired size/value bound.

## Counterexample Tests

- Pairwise independence is mistaken for mutual independence outside the dependency graph.
- Events share hidden random variables, making the dependency degree larger than claimed.
- Bad events do not cover all forbidden configurations.
- LLL proves positive probability but the theorem claims an efficient algorithm.
- Alteration deletes too much or creates new violations.
- Constants fail for small `n`, sparse edge cases, or high-degree vertices.

## LLL Checklist

1. Random space: variables, distribution, and independence structure.
2. Bad events: one event per forbidden local obstruction.
3. Failure coverage: no bad events implies the theorem.
4. Probability bound: `Pr[A] <= p_A`.
5. Dependency graph: neighbors are all events sharing relevant randomness, or a justified lopsided graph.
6. Criterion: union bound, symmetric LLL, asymmetric LLL, lopsided LLL, or alteration.
7. Constants: verify the final inequality symbolically or numerically for the stated parameter range.
8. Constructiveness: if needed, specify resampling variables, termination criterion, and output certificate.
9. Assembly: translate avoided bad events into the exact theorem statement.

## Tool Hooks

- Python/NetworkX to count dependency degree, enumerate small bad-event overlaps, and search finite counterexamples.
- SymPy/Wolfram to check `e p (d+1) <= 1`, optimize parameters, and verify asymptotic constants.
- Z3 for finite dependency-graph or coloring counterexamples.
- Sage/NetworkX for graph and hypergraph structures.
- Moser-Tardos simulation only as sanity check; it is not a proof unless the LLL hypotheses are proved.

## When Not To Use LLL

- Events are globally dependent and no valid lopsided dependency graph is available.
- A direct deterministic construction, compactness theorem, LP dual, or greedy invariant already proves the claim.
- The probability of success is high enough for an ordinary union bound.
- The statement needs exact enumeration or optimization rather than existence.

## Source Log

- Erdos and Lovasz, "Problems and results on 3-chromatic hypergraphs and some related questions" introduced the local-lemma line of probabilistic existence arguments.
- Moser and Tardos, "A constructive proof of the general Lovasz Local Lemma" gives the standard resampling view for algorithmic LLL.
- Harvey and Vondrak, "An Algorithmic Proof of the Lovasz Local Lemma via Resampling Oracles" generalizes constructive LLL beyond product spaces.
- Harris work on lopsided/resampling-oracle variants is useful when ordinary dependency graphs are too pessimistic.
- Erdos-Faber-Lovasz is a concrete hypergraph-coloring conjecture; absorb it as a source of coloring/degree-splitting patterns, not as the main reusable workflow.
