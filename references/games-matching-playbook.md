# Games And Matching Playbook

Use for Nash existence, supermodular games, price of anarchy, no-regret equilibrium links, matching stability, deferred acceptance, and market design.

## Branch Split

- Nash existence: compact convex strategies, continuous payoffs, quasi-concavity; apply Kakutani/Glicksberg.
- Supermodular games: lattice strategies, supermodularity, increasing differences; apply Tarski/Topkis.
- Potential games: construct potential; prove improvement path or existence of pure NE.
- Price of anarchy: smoothness inequality or potential comparison.
- Matching stability: blocking-pair contradiction and DA invariants.
- Strategy-proof matching: rejection-chain or lattice argument.

## Smart Routes

- Best response set not single-valued: use correspondence fixed point, not a function fixed point.
- Comparative statics of equilibria: use supermodular game increasing selections.
- POA proof stuck: first prove a local smoothness inequality, then sum across players.
- DA proof stuck: track proposal/rejection invariant instead of final matching directly.
- Strategy-proofness hard: prove no agent can avoid rejection from a preferred feasible option.

## Common Lemmas

- Kakutani/Glicksberg fixed point.
- Tarski fixed point theorem on complete lattices.
- Topkis monotone argmax theorem.
- Potential function existence of pure NE.
- Deferred acceptance no-blocking-pair invariant.
- Rural hospitals/lattice-style stable matching facts.

## Counterexample Tests

- Two players, two actions.
- Discontinuous payoff or noncompact strategy set.
- Nonconvex best responses.
- Matching with ties.
- Capacity one vs many-to-one.

## Tool Hooks

- Python/NetworkX for matching/blocking-pair search.
- Z3 for finite game equilibrium counterexamples.
- Sage for lattice/discrete structures.
- Wolfram for payoff algebra and smoothness inequalities.
