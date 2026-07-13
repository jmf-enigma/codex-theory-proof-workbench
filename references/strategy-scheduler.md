# Strategy Scheduler

Use this file to choose the next proof route after classification or failure.

## Map

- Normalize first: make objects, quantifiers, and the smallest nontrivial case explicit.
- Portfolio routes: choose genuinely different proof architectures before converging.
- Search discipline: retrieve, guess, kernelize, verify, and repair locally.
- Frontier control: compare a few non-equivalent next moves by decision value, check cost, and assembly relevance.
- Marginal value routing: after repeated failure, choose exactly one next action.
- Novelty and decision value: continue only when a route changes evidence, object, or obstruction.
- Switch rules and scoring: select the route whose assumptions and certificates best match the theorem.

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
- Direct-first then blueprint: try a short direct route once. If it fails, build a lemma graph rather than extending the same prose proof.
- One-step verifier loop: for a fragile subgoal, try one move, predict the new subgoal, check it, and record whether the proof state became smaller.
- Repair by isolation: when a route fails, find the earliest false or unproved step, preserve the verified prefix, and rewrite only the affected subgraph.
- First-error rule: downstream steps after the first invalid inference are not evidence. Earlier checked steps and independent helper lemmas remain reusable artifacts.
- Compact feedback repair: when retrying a failed node, use the node statement, retrieved pattern, previous attempt signature, and previous feedback. Do not reload the whole failed history into the next attempt.
- Progress estimate: after each route, mark whether the remaining obstacle is smaller, unchanged, or bigger; stop or switch after two unchanged/bigger cycles.
- Recombine only after local checks: a final proof is allowed only when each sketch lemma has a status and the assembly matches the original quantifiers.
- Gap reviewer: before accepting a missing lemma, classify it as a good gap or bad gap. A bad gap is equivalent to the theorem, hides the core construction, is circular, or lacks a verification hook.
- Used-node filter: before proving side lemmas, check whether they feed the current theorem assembly. If not, postpone them unless they are being used to falsify, retrieve, or repair the theorem.
- Dependency split: distinguish statement dependencies from proof dependencies. A theorem can structurally depend on one lemma while its proof temporarily needs a different theorem, tool certificate, or local helper.

## Marginal Value Routing

Use this after two failed local attempts, one repeated failure signature, or any expensive proof move.

Choose exactly one next action:

- continue current node: only if the proof state got smaller, failures are genuinely diverse, or a new certificate/premise is now available;
- local repair: if the statement seems right but the proof block fails for one identifiable reason;
- re-decompose: if the current missing lemma is a bad gap, too broad, circular, or hides the core construction;
- retrieve/pattern scan: if the route needs a theorem name, standard trick, or assumption list not yet identified;
- tool/falsification check: if a finite example, algebra identity, LP/SMT witness, or local formalization can decide the kernel;
- stop/report: if failure signatures repeat, the proof state is unchanged, and no next move has a checkable artifact.

Route by signals, not vibes:

- proof-state delta: smaller / unchanged / larger;
- failure diversity: new obstruction or same obstruction;
- proof similarity: same central object, same algebra, same parameterization, or same construction;
- attempt count on the node;
- expected artifact from the next attempt.

If the next attempt cannot name an expected artifact, do not continue the same proof route.

## Novelty And Evidence

For a hard or previously failed proof, a new route must change at least one real axis:

- theorem family or proof architecture;
- central object such as a dual, Bellman gap, envelope, potential, coupling, hard instance, certificate, or good event;
- failure world or boundary case being controlled;
- evidence source, such as a tool certificate, finite counterexample search, retrieved theorem, or local formalization;
- statement repair or newly identified missing assumption.

Do not treat these as new routes: same missing lemma with stronger wording, same construction under different notation, same algebra after adding a cosmetic case split, or a proof sketch whose only new ingredient is hope.

A route has made progress only if it proves/refutes a kernel, shrinks the missing lemma, exposes a missing assumption, imports a checked theorem pattern, or produces a checkable artifact. If none of those happen, record the failed state and switch route.

For difficult proofs, use a three-lane first pass unless direct mode succeeds: proof route, falsification route, and orthogonal evidence route. The third lane can be small-case pattern mining, symbolic simplification, LP/SMT/CVX certificate search, Lean for a local lemma, or a one-to-three-source pattern scan.

## Frontier Controller

For a research-level stuck proof, keep a small candidate frontier after the first pass:

- 2-4 routes only;
- each route must differ by central object, certificate type, theorem family, or failure world;
- attach one cheap evaluator to each route: toy counterexample, symbolic identity, premise match, local certificate, or formalizable leaf;
- rank routes qualitatively by decision value, evaluator cost, assembly relevance, novelty, and circularity risk;
- retire any route whose compact failure state matches an earlier fingerprint.

Expand one route at a time. Prefer the route whose next artifact can prove, refute, or sharply re-decompose the kernel. Keep a lower-ranked route alive only when it explores a genuinely different proof state. Do not average several weak sketches into one proof.

After an evaluator returns:

- `accept`: add the artifact to the lemma graph;
- `local repair`: preserve the verified prefix and repair the first failing node;
- `trace-back`: reopen the earliest accepted ancestor contradicted by the new evidence;
- `route replan`: retire the proof family only when its central object, decomposition, or required assumptions fail;
- `stop/report`: use when every live candidate is equivalent, low-value, or lacks a checkable artifact.

## Decision Value Ranking

When several next moves are possible, choose the one with the highest decision value. A high-value move can end or sharply reroute the search:

- prove or refute the current kernel;
- produce a counterexample, boundary case, or missing assumption;
- produce a checkable certificate, exact identity, LP/SMT/CVX witness, or local formalization;
- retrieve a theorem pattern whose assumptions can be matched immediately;
- replace an opaque algebra step with a dual, envelope, Bellman, KL, coupling, potential, or telescope representation.

Use a verification cascade and stop at the first decisive level: dimensional/domain checks, smallest counterexample or boundary case, exact symbolic/numeric certificate, local formalization, then adversarial assembly review. Expensive formal search is justified only when the local statement is stable and the cheaper checks cannot decide it.

Low-value moves include polishing exposition, adding an unmotivated case split, strengthening the same missing lemma, or trying another route whose failure witness is unchanged.

If all candidate moves have low decision value, stop and ask whether the theorem statement, modeling assumptions, or intended conclusion should change.

When the theorem needs a construction, threshold, potential, hard instance, coefficient, or exact answer, the highest decision-value move is often discovery, not proof: compute or derive the object, self-check it on a holdout case, then convert it into a lemma.

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
