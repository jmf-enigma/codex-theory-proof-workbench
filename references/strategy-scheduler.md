# Strategy Scheduler

Use this file to choose the next proof route after classification or failure.

## Normalize First

- Convert maximization/minimization to a standard objective and feasible set.
- Separate objects: primitives, decision variables, random variables, policies, mechanisms, outcomes, payments.
- Mark quantifier type: pointwise, uniform, in expectation, high probability, almost surely, asymptotic.
- Identify whether the desired statement is existence, uniqueness, monotonicity, optimality, incentive compatibility, regret, or lower bound.
- Create the simplest nontrivial instance: scalar, two actions, two types, one period, finite state, deterministic noise, or symmetric case.

## Portfolio Routes

Run at least two routes for a hard proof unless one route cleanly proves or refutes the claim.

- Direct theorem route: match assumptions to a named theorem and verify every condition.
- Contradiction route: assume failure and derive violation of optimality, IC, monotonicity, or concentration event.
- Dual route: rewrite as Lagrangian, LP dual, convex conjugate, envelope, or separating hyperplane.
- Local-to-global route: prove local monotonicity/FOC/single crossing then upgrade using convexity, lattice, or envelope conditions.
- Dynamic route: write one-step recursion, prove Bellman inequality, telescope.
- Potential route: define a potential/log-partition/Bregman term and telescope.
- Martingale route: define filtration, increments, variance proxy, then apply concentration.
- Information route: choose hard instances, compute KL/TV/mutual information, transfer to error/regret.

## Search Discipline

- Retrieval before invention: list the closest known theorem patterns, paper lemmas, textbook facts, or prior ledger lemmas before proposing a new lemma.
- Guess before proving when the object is hidden: compute tiny cases, infer a formula, threshold, active set, invariant, tight instance, or potential, then reserve one holdout case before promoting the guess.
- Kernel before long proof: state the one lemma, certificate, or counterexample barrier that would decide the route, then prove, refute, retrieve, or tool-check that kernel first.
- Draft-Sketch-Prove: turn the intuitive proof into named subgoals before filling details; subgoals should be small enough for algebra, finite checks, Lean, or direct theorem matching.
- One-step verifier loop: for a fragile subgoal, try one move, predict the new subgoal, check it, and record whether the proof state became smaller.
- Repair by isolation: when a route fails, isolate the first false or unproved subgoal instead of rewriting the whole proof.
- Progress estimate: after each route, mark whether the remaining obstacle is smaller, unchanged, or bigger; stop or switch after two unchanged/bigger cycles.
- Recombine only after local checks: a final proof is allowed only when each sketch lemma has a status and the assembly matches the original quantifiers.

## Switch Rules

- FOC fails or boundary matters: switch to KKT/subgradient/complementary slackness.
- Many IC constraints: switch to envelope theorem for one-dimensional types or cyclic monotonicity/no-positive-cycle for multidimensional types.
- Monotonicity is intuitive but unproved: switch to increasing differences, single crossing, supermodularity, or lattice fixed point.
- Existence proof handwaves best response: switch to compactness/continuity/upper hemicontinuity audit and a fixed-point theorem.
- Regret proof loses a factor: split into confidence event, instantaneous regret bound, summation lemma, and failure-event term.
- Linear bandit proof stalls: isolate ridge confidence, optimism, and elliptical potential as separate lemmas.
- Lower bound has no bite: reduce to two instances, compute KL, then generalize with Fano/Assouad only if needed.
- Optimization proof proves necessary conditions only: add sufficiency via convexity/concavity or construct a dual certificate.

## Route Scoring

Prefer a route when:

- its theorem assumptions are close to the problem assumptions,
- the target conclusion exactly matches the theorem conclusion,
- key lemmas can be checked by local tools,
- it produces reusable lemma cards for future problems,
- it avoids hidden regularity assumptions.

Avoid a route when it requires stronger smoothness, compactness, independence, or convexity than the user stated, unless presenting a conditional theorem.
