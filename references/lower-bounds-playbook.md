# Lower Bounds Playbook

Use for minimax lower bounds, bandit lower bounds, impossibility results, sample complexity, regret lower bounds, and information-theoretic arguments.

## Branch Split

- Two-point lower bound: Le Cam, total variation, KL/Pinsker.
- Multi-hypothesis lower bound: Fano or Assouad.
- Bandit lower bound: change of measure and expected pull counts.
- Optimization lower bound: resisting oracle or hard quadratic family.
- Mechanism impossibility: finite type profile construction or cycle/monotonicity violation.
- Communication/information bottleneck: mutual information or data processing.

## Smart Routes

- Start with two instances; only use Fano/Assouad after the binary construction is clear.
- Make instances close enough in observations but far enough in required decision.
- Compute KL exactly before choosing parameters.
- Convert testing error into regret/risk via a decision gap.
- For bandits, ensure the algorithm must sample the confusing arm enough.
- For mechanisms, construct types that force contradictory IC/monotonicity constraints.

## Common Lemmas

- Le Cam two-point method.
- Pinsker inequality.
- Bretagnolle-Huber inequality.
- Fano inequality.
- Assouad cube method.
- Bandit change-of-measure lemma.

## Counterexample Tests

- Hard instances accidentally distinguishable too quickly.
- Alternative instance violates model assumptions.
- Gap too small to imply target loss.
- Prior/hypothesis set not symmetric enough.
- Lower bound only proves Bayesian, not minimax, without transfer.

## Tool Hooks

- Python/SymPy for KL and parameter optimization.
- Z3 for finite impossibility profiles.
- CVXPy/LP duality for adversarial distributions or certificates.
