# Optimization And OR/MS Playbook

Use for KKT, LP/convex duality, exchange arguments, queueing/control-style structural results, and algorithm optimality. For Bellman equations, MDPs, threshold policies, indexability, or average-cost DP, also read [dp-proof-playbook.md](dp-proof-playbook.md).

## Branch Split

- Convex program: prove convexity/closedness, Slater or LP feasibility, derive dual, certify by KKT.
- Nonconvex program: avoid KKT sufficiency; search for convexification, monotonicity, exchange, or global certificate.
- LP/integer program: inspect primal/dual, complementary slackness, total unimodularity, relaxation gap, rounding.
- Dynamic program: use [dp-proof-playbook.md](dp-proof-playbook.md) for Bellman recursion, monotonicity/convexity/contraction, and policy verification.
- Structural policy: try threshold, monotone policy, indexability, submodularity, coupling, or interchange argument.
- Algorithm proof: prove invariant, approximation ratio, primal-dual certificate, potential decrease, or exchange optimality.
- Fixed first-order/operator algorithm rate: if the method, class, normalization, and metric are PEP-encodable, use [peppy-proof-bridge.md](peppy-proof-bridge.md) to discover and certify a rate or Lyapunov function.

## Smart Routes

- Boundary-heavy FOC: replace with KKT/subgradient; split active constraints.
- Hard global optimality: construct a dual certificate or exchange argument.
- Monotone optimal policy: prove increasing differences or submodularity of value differences.
- DP convergence: use contraction if discounted; use monotone value iteration or span seminorm if average-cost.
- Approximation: choose benchmark first, then prove algorithm reaches fraction/additive gap.
- Unknown convergence rate: use Peppy Block 1 to conjecture the formula, Block 2 for certificate structure, and Blocks 3-5 only when an all-horizon readable Lyapunov proof is needed.

## Common Lemmas

- KKT sufficiency under convexity.
- Weak/strong duality and complementary slackness.
- Bellman optimality and policy improvement.
- Envelope theorem for value functions.
- Topkis monotonicity for argmax correspondence.
- Exchange argument for greedy structure.

## Counterexample Tests

- One constraint active at boundary.
- Two-item/two-period instance.
- Nonunique optimizer/tie-breaking.
- Nonconvex objective with local optimum.
- Relaxed LP fractional solution.

## Tool Hooks

- CVXPy for primal/dual sanity check.
- OR-Tools for small integer/assignment/scheduling instances.
- Wolfram/SymPy for FOC, Hessian, envelope, algebraic inequalities.
- Z3 for finite policy/threshold counterexamples.
- Peppy/PEPFlow for conditional fixed-algorithm performance estimation, dual certificates, and Lyapunov construction.
