# Mechanism Design Playbook

Use for DSIC/BIC/IC/IR, auctions, allocation monotonicity, revenue equivalence, virtual values, ironing, and multidimensional types.

## Branch Split

- Single-parameter DSIC: allocation monotonicity plus payment identity.
- Single-parameter BIC: interim allocation monotonicity plus envelope formula.
- Multidimensional IC: cyclic monotonicity, convex utility, subgradient allocation.
- Revenue optimality: virtual surplus maximization, regularity, ironing if nonmonotone.
- Approximation mechanism: algorithmic approximation plus monotonicity/truthfulness proof.
- Budget/payment constraints: separate feasibility, utility, and payment monotonicity.

## Smart Routes

- IC constraints too many: convert pairwise IC to envelope or cyclic monotonicity.
- Payment formula unclear: derive utility derivative first, then payment from envelope.
- Allocation monotonicity false: look for ironing, randomization, or weaker implementability.
- Multidimensional type hard: check finite type graph for positive cycles; search Rochet cyclic monotonicity.
- Revenue proof stuck: identify benchmark and prove virtual surplus or approximation to benchmark.

## Common Lemmas

- Monotone allocation iff DSIC implementable in single-parameter domains.
- Envelope theorem for one-dimensional BIC.
- Revenue equivalence via equal allocation and boundary utility.
- Cyclic monotonicity iff implementable for quasilinear multidimensional types.
- Myerson virtual surplus characterization under regularity.

## Counterexample Tests

- Two types, two allocations.
- Lowest/highest type boundary IR.
- Nonmonotone allocation rule.
- Type misreport cycles of length 3.
- Nonregular distribution virtual value decreasing.

## Tool Hooks

- Z3/linear inequalities for finite IC/IR feasibility.
- CVXPy for payment feasibility and dual certificates.
- Wolfram for envelope derivatives and virtual values.
- Graph negative/positive cycle checks for cyclic monotonicity.
