# Proof Idea Generator

Use this optional pass when the proof route is not obvious, the theorem has failed before, or the user asks where the proof idea should come from. Skip it for routine lemmas with a clear theorem family.

The goal is not to force another checklist. The goal is to find a central object or central lemma that makes the theorem almost automatic.

An idea is an executable hypothesis, not a persuasive narrative. It must predict one local mathematical fact, name the cheapest observation that would support or kill it, and specify how either outcome changes the next move.

## Map

- Use/skip rules: decide whether an idea pass is worth the tokens.
- Idea map and proof kernel: find the central object and decisive local lemma.
- One-step queue and construction search: invent/check clever moves without looping.
- Idea engines and paper tricks: retrieve or synthesize a route, then stop.
- Gap review, route decision, and compact repair: decide whether a missing lemma is a real smaller step or just the theorem in disguise, then choose whether to continue, repair, re-decompose, retrieve, tool-check, or stop.

## When To Use

- The first proof route feels generic or decorative.
- The statement is true in examples but the key lemma is unknown.
- Two plausible routes lead to the same obstruction.
- The theorem mixes several domains, such as DP plus mechanism design or learning plus incentives.
- The user asks for proof strategy, proof idea, or why the theorem should be true.

Use the lightest pass that can change the next move. A one-screen idea map is enough unless the proof is genuinely stuck.

For small unclear proofs, do a micro pattern check before opening a full idea map: inspect one close theorem family, prior ledger, playbook pattern, or paper trick, then stop if it gives a usable central object or a clear mismatch.

## When To Skip

- The theorem is a direct application of a known theorem and the assumptions match.
- The user only wants exposition for an already complete proof.
- A counterexample has already refuted the claim.
- The next useful move is a narrow algebra, finite, SMT, optimization, or Lean check.
- The idea pass would only restate generic proof advice without producing a central object or central lemma.

## Idea Map

For a hard proof, optionally fill these before the final proof route:

- Direct-solve check: is there an obvious theorem, certificate, or short proof route?
- Statement fence: what exact theorem statement must not change without theorem repair?
- Failure world: what would the smallest counterexample look like?
- Central object: what quantity, correspondence, certificate, event, or potential controls that failure?
- Assumption engine: which stated assumptions can control that object?
- Central lemma: what one lemma would make the theorem straightforward?
- Local prediction: what observable identity, sign, witness, normal form, or proof state should appear if the idea is right?
- Verification hook: how can the lemma be tested, retrieved, tool-checked, or locally formalized?
- Decision consequence: what result keeps, repairs, or retires this route?
- Paper pattern: what proof architecture from a prior paper, local draft, or known theorem family can be transplanted?
- Paper trick: what local trick from a paper can be reused, and what assumptions make it legal?
- Gap grade: is the current missing step a good gap or bad gap?

If no central object appears, do not write a final proof. Switch to counterexample search, retrieval, or theorem repair.

## Divergence Before Convergence

When the same theorem has failed before, first make the search wider in a controlled way, then narrow it. Produce three short candidates with different central objects:

- failure-world candidate: start from the negation and find the object that rules it out;
- certificate candidate: search for a KKT, dual, Bellman, envelope, cyclic-monotonicity, concentration, KL, potential, or coupling certificate;
- outside-pattern candidate: mine a nearby theorem, paper appendix, prior ledger, formal-library lemma, or small-case pattern for proof architecture.

Score each candidate by failure-world control, assumptions used, verification hook, and route novelty. Continue only with the best candidate. If all three reduce to the same missing lemma, record that lemma as the bottleneck and escalate rather than writing another proof sketch.

## Proof Kernel

Before drafting a long proof, compress the route into one proof kernel: the smallest lemma, certificate, or counterexample barrier that would decide the route.

A usable kernel has four parts:

- statement: the exact local claim to prove, refute, retrieve, or certify.
- implication: why the kernel plus routine assembly gives the theorem.
- evidence type: direct proof, known theorem, tool certificate, finite falsification, or local formalization.
- failure shape: the counterexample, boundary case, or missing assumption that would make the kernel false.

If no kernel can be stated, keep searching for the central object or try to falsify the claim. If two kernels fail without shrinking the obstruction, switch route or repair the theorem.

## Good Gap / Bad Gap Review

Use this before accepting a missing lemma or moving to final proof.

A good gap:

- is strictly smaller than the parent theorem;
- has explicit assumptions and declared dependencies;
- is not circular and does not restate the target;
- has a verification hook such as a theorem match, algebra check, finite falsification, certificate, or local formalization;
- if proved, would leave only routine assembly.

A bad gap:

- hides the main construction, threshold, hard instance, or inequality;
- is equivalent to the original theorem under renamed notation;
- depends on an unstated regularity, monotonicity, measurability, or boundary condition;
- cannot be falsified or checked locally;
- asks the user to trust "standard arguments" for the hardest step.

If the gap is bad, do not polish. Split it, retrieve a pattern, run construction search, try a counterexample, or repair the theorem.

## Hard-Mode Discovery

Use this when the proof cannot start because the theorem needs an unknown object: policy threshold, potential, active set, coefficient sequence, hard instance, coupling, payment, or exact answer.

1. Generate candidate objects from tiny cases, equality cases, binding constraints, or analogous papers.
2. Self-check candidates on at least one holdout case not used to guess them.
3. Reject candidates that only fit numerically but have no proof kernel.
4. Promote a candidate only when it yields a central lemma, certificate, theorem pattern, or local formalization target.

This is discovery, not proof. Once the object is found, return to the proof kernel and prove it.

## Bottleneck Surgery

Use this when the proof keeps circling one missing lemma. The goal is to change the local problem, not to make the prose longer.

1. Shrink: state the smallest local lemma where the obstruction first appears.
2. Flip: write the negation or equality/tight case of that lemma.
3. Explain the survivors: if a bounded counterexample search finds nothing, identify the structure shared by the surviving cases and formulate a rigidity or invariant conjecture. This creates a new proof obligation; it does not support the original theorem by itself.
4. Move one rung on a representation ladder: direct expression, difference/slack or equality case, structural lemma, then dual/countermodel/certificate or formal leaf. Choose the rung that exposes the recorded obstruction.
5. Certify or falsify: search for a finite witness, algebra identity, LP/SMT/CVX certificate, known theorem, or local formalization.
6. Repair: if the surgery reveals an extra condition or weaker conclusion, state the repaired theorem before continuing.

Stop surgery after one decisive artifact or two failed local moves. Then either switch route or mark the theorem `lemma-conditional` or `still open`.

## One-Step Proof Move Queue

Use this when the kernel is fragile or the route keeps circling the same missing lemma. A move is useful only if it changes the proof state.

Track a tiny queue:

- current subgoal:
- proposed move:
- intended theorem, algebra identity, tool check, or retrieved premise:
- expected new subgoal if the move works:
- result: kept / repaired / discarded:
- proof-state delta: smaller / unchanged / larger:

If two moves leave the same subgoal unchanged, stop proving in prose. Record the failed state in the ledger, retrieve a closer premise or paper pattern, tool-check the subgoal, or repair the theorem.

Before the next attempt, make a route decision. Continue only if the next move has a new expected artifact such as a smaller subgoal, verified identity, counterexample, theorem pattern, certificate, repaired statement, or genuinely new central object.

## Evidence-Layered Search Packet

Use this only after the direct pass fails and the search becomes noisy, repetitive, or crowded with candidate rules. It is a one-screen view inside the current idea map or ledger, not a new mandatory file.

| layer | keep | required annotation | proof effect |
| --- | --- | --- | --- |
| sound shortcuts | exact theorem, rewrite, invariant, duality, symmetry, or decomposition | preconditions, resulting obligation, replay check | only after the applicability check passes |
| executable falsifiers | concrete witness, finite model, generator, separating algebra, or exact checker | full premise check, target-failure trace, exhaustive or sampled scope | refutation only when the certificate is replayable and covers the claimed scope |
| scheduler priors | similarity, size, source hit, score, motif, or failure history | cost, expected artifact, and `proof_effect=none` | none |
| near-miss frontier | two to four checked or rejected intermediate states | verified prefix, exact remaining gap, candidate bridge | none until the bridge is proved or checked |

Build and use the packet in this order:

1. Freeze the exact statement signature: objects, types, domains, assumptions, quantifiers, conclusion, structural form, symmetry or dual transforms, and boundary or equality regimes. For symbolic identities, parse and canonicalize the exact expression trees once; every rule, cached witness, and rewrite must consume that representation rather than visual or character similarity.
2. Run an exact or direct route, then a cheap witness cascade ordered by the structural mismatch it can expose. For a proposed finite countermodel, recheck the cached or generated table against the current statement, verify every premise under every required assignment, and only then exhibit one explicit target failure. Label finite sampling as sampling, never universal verification.
3. If neither decides the claim, run one bounded forward/backward proof-state search or premise-retrieval pass. A rejected proof may donate its independently checked prefix and intermediate terms to deterministic local search, but neither the rejected proof nor those search seeds are evidence.
4. Repair the first local failure. If two moves preserve the same gap, change representation or route instead of adding more examples or prompt text.
5. Stop on a decisive artifact or two unchanged moves. Keep at most two verified examples in active context, deduplicate equivalent rules, and retire routes whose only support is a heuristic score.

The promotion gate is strict. An explicit derivation, source-checked and assumption-matched theorem application, replayable counterexample or certificate, or formal check may change status. No-small-counterexample results, default labels, leaderboard rank, statement similarity, character overlap, sampled assignments, and majority votes may schedule work but have `proof_effect=none`.

Audit semantic range before symbolic substitution. A compound term cannot be replaced by an arbitrary domain element unless its image is proved to cover that element. A diagonal or square law does not automatically control the full binary operation, a term-valued witness may depend on the quantified variable, and an invariant refutes a claim only after its preservation is proved or realized by a fully checked witness model.

A failed attempt may donate a verified prefix, helper lemma, useful intermediate term, or obstruction fingerprint. A trick may seed future search only after its source and assumptions are checked, it replays exactly on the current problem, and it passes an independent route or held-out case. Until then, keep it `candidate`; this prevents a plausible but false trick from poisoning later searches.

## Construction And Algebra Move Search

Use this only when the proof kernel needs a clever object or a non-obvious manipulation. The goal is to synthesize one local move, not to brainstorm indefinitely.

First guess from patterns. Compute or reason through the smallest cases, then look for a formula, threshold, invariant, active set, tight instance, coefficient pattern, or potential. Keep at least one holdout case that was not used to guess the pattern. If the small cases form an exact sequence, use `scripts/pattern_miner.py` to inspect finite differences, ratios, a Newton/binomial form, and a simple holdout check.

Start from the tight case. Ask where equality would hold, which constraint binds, which action is indifferent, which lower-bound instances are barely distinguishable, or which regret term dominates. Then reverse-engineer the object or algebra that makes that tight case visible.

Common construction seeds:

- dual/slack variable, Lagrange multiplier, KKT residual, or complementary slackness term.
- Bellman gap, post-decision value, value-difference, or threshold indifference equation.
- envelope term, payment normalization, deviation graph, or cyclic-monotonicity potential.
- coupling, ghost sample, filtration, confidence event, peeling layer, or stopping time.
- hard instance pair, packing, change of measure, KL bridge, or least favorable prior.
- benchmark, potential, Lyapunov function, Bregman divergence, entropy, or log determinant.

Common algebra normal forms:

- add and subtract the right benchmark, optimum, continuation value, or conditional expectation.
- rewrite ratios as differences, gaps as sums of local gaps, or global claims as telescopes.
- complete a square, use convex conjugates or Fenchel-Young, or expose a dual certificate.
- take logs for products, determinants for linear bandits, KL/TV for testing, or Bregman form for OCO.
- symmetrize, couple two worlds, condition on the good event, or split boundary and interior cases.

Check the move quickly on the smallest toy instance or with Wolfram/SymPy/Python before building a long proof. If the normal form does not control the failure world, discard it and record the obstruction fingerprint.

A pattern guess is not a lemma. Promote it only after one of these happens: it survives holdout toy cases, it has a proof kernel, it matches a known theorem pattern, or it yields a certificate that can be checked independently.

The best clever move usually explains the tight case. Prefer a construction that makes equality, indifference, binding constraints, worst-case histories, least favorable instances, or zero-slack conditions visible. If a construction cannot say why the known hard example is hard, treat it as decorative.

## Route Candidate Board

When several clever moves are plausible, keep a small board instead of a long brainstorm.

| route | central object | why plausible | verification hook | novelty | gap grade | retire if |
| --- | --- | --- | --- | --- | --- | --- |

Keep 2-4 routes. Retire a route if its compact failure state matches a previous attempt or if its key gap is bad and cannot be split.

Prefer routes that feed the current theorem assembly. A clever side lemma that has no downstream use is a pattern card or exploratory note, not a proof target.

When no top-down route is visible, use a bounded bottom-up probe: choose at most two special cases or auxiliary facts derivable from the assumptions, prove or refute them cheaply, and ask what invariant, representation, or common strengthening explains both. These probes may reveal the strategy without appearing in the final assembly. Stop if they do not expose a shared structure or a new verification hook.

## Pre-Solve Gate

Before running a full idea pass, ask whether the problem is directly solvable.

- Direct theorem: a named theorem matches the assumptions and conclusion.
- Direct certificate: KKT, dual, Bellman inequality, envelope, cyclic monotonicity, concentration, or KL certificate is already visible.
- Direct contradiction: the negation immediately violates optimality, IC, monotonicity, feasibility, or a good event.
- Direct decomposition: the claim splits into known lemmas already available in the prompt or prior ledger.

If one of these is true, proceed directly and use the idea map only as a short note. If none is true, update the idea map. Scan prior papers or proof patterns only when the central object or central lemma is still unclear.

## Idea Engines

### 1. Failure-World Engine

Write the negation in the smallest form.

- Monotonicity fails: find two states, types, times, or parameters with reversed order.
- Threshold fails: find two crossings of an action difference.
- IC fails: find one profitable deviation or a positive deviation cycle.
- Optimality fails: find a feasible deviation that beats the candidate.
- Regret bound fails: find a history where instantaneous regret or the summation term is too large.
- Lower bound fails: find an algorithm that distinguishes the hard instances too cheaply.

Then ask which object prevents that failure.

### 2. Assumption-To-Machine Engine

Translate each useful assumption into the proof machine it buys.

- Compactness plus continuity buys existence.
- Convexity or concavity buys global optimality from local conditions.
- Increasing differences buys monotone comparative statics.
- Single crossing buys threshold or sorting.
- Quasilinear IC buys envelope, payment identity, or cyclic monotonicity.
- Markov structure buys Bellman recursion.
- Adaptive data buys filtration and martingale concentration, not iid concentration.
- KL closeness buys testing or lower-bound transfer.

If an assumption buys no move, it may be unused. If the desired move has no assumption, the theorem may be missing one.

### 3. Central-Object Engine

Look for the object whose structure implies the conclusion.

- DP or MDP: Bellman operator, Q-value difference, post-decision value, Bellman certificate.
- Mechanism design: indirect utility, allocation monotonicity, deviation graph, payment feasibility LP.
- Optimization: Lagrangian, dual variables, subgradient, feasible direction, exchange invariant.
- Games and matching: best-response correspondence, potential, blocking-pair invariant.
- Learning and bandits: good event, confidence radius, instantaneous regret, summation potential.
- Lower bounds: hard instance pair, packing, KL/TV bridge, testing-to-risk reduction.

The central lemma should usually state a structural property of this object.

### 4. Certificate Engine

Search for an independently checkable certificate rather than a long derivation.

- Optimality: KKT, dual variables, Bellman inequalities, complementary slackness.
- Feasibility: explicit construction, flow/LP certificate, measurable selector.
- IC/IR: payment formula plus all deviation inequalities.
- Regret: event validity plus telescoping or summation certificate.
- Lower bound: feasible hard instances plus explicit KL and separation.

Certificates are useful because they expose missing assumptions and boundary cases.

### 5. Invariant, Potential, And Telescope Engine

Use this when a proof involves time, iterations, algorithms, learning, or induction.

- Find a quantity that never increases, never decreases, or telescopes.
- Try a potential even when the target is not obviously a potential result.
- For induction, prove the step preserves the property rather than solving the object exactly.
- For algorithms, track what the update changes by one step.

Good potentials often come from the final bound, a dual objective, a norm, a log determinant, entropy, or a Bellman gap.

### 6. Local-To-Global Engine

Use this when the theorem claims a global structure.

- Prove local order, derivative sign, exchange improvement, or one-step deviation first.
- Upgrade to global via convexity, lattice structure, envelope theorem, contraction, or induction.
- If local conditions are not sufficient, search for a counterexample or a global certificate.

### 7. Abstraction-Refinement Engine

Use this when the model is too rich.

- Start with a coarse abstraction: scalar, finite state, two actions, two types, one period, deterministic shock.
- If the abstraction proves the claim, identify the invariant that survived.
- If it fails, decide whether the failure is real or an artifact of the abstraction.
- Refine only the missing feature, such as boundary states, tie-breaking, dependence, or information.

This is a proof-search version of counterexample-guided abstraction refinement.

### 8. Retrieval-And-Analogy Engine

Before inventing a nonstandard lemma, search for nearby theorem patterns. Start with local drafts, appendices, ledgers, and known theorem names. Browse broadly only if those do not produce a central object or missing assumption.

- Name the family: Topkis, Berge, Kakutani, envelope, Rochet, self-normalized martingale, elliptical potential, Fano, Le Cam.
- Retrieve assumptions, conclusion, proof decomposition, and the central object used by prior papers.
- Search local drafts, user-provided papers, prior ledgers, paper appendices, textbook lemmas, and formal libraries before broad web search.
- Import only the route structure or lemma statement, not an unsupported proof step.
- Prefer a route with a local certificate over a beautiful route that cannot be falsified.

## Paper Trick Cards

Record a paper trick only if it changes the next proof move. Do not store vague inspiration.

Each trick card should include:

- source: paper, appendix, theorem, lemma, page, or local draft section.
- trick name: short label, such as coupling, envelope normalization, Bellman certificate, ironing, peeling, change of measure.
- problem shape: when this trick applies.
- obstruction solved: the proof failure it fixes.
- central object: the object the trick manipulates.
- hidden assumptions: regularity, boundary, independence, measurability, convexity, monotonicity, or support conditions.
- transplant step: how to adapt the trick to the current notation.
- verification hook: finite check, algebra check, theorem citation, certificate, or local formalization.
- failure mode: when the trick should not be used.

Good trick cards are small. A reusable trick should be one local move, not an entire proof.

## Learning Update

Treat trick cards as working memory, not permanent truth.

- Record a trick after it changes a proof route, finds a missing assumption, produces a useful counterexample, or gives a verifiable central lemma.
- Mark the trick as `candidate` until it is checked in the current proof.
- Mark it as `validated-local` only after it proves, refutes, or repairs a concrete lemma.
- Mark it as `rejected` if the hidden assumptions do not hold.
- For reuse, compare the trick's dependency signature: required assumptions and inputs, transformation, produced artifact, and verification hook. It must act like a collapsible subproof with no hidden cross-boundary dependency. Similar prose or notation is not recurrence.
- Promote it to global skill memory only after replay on a second route or held-out problem shape, or after the user asks to keep it. A valuable one-off remains `validated-local`.

The dependency test adapts [TacMiner's](https://arxiv.org/abs/2503.24036) tactic-dependence graph and collapsible-fragment idea. TacMiner mines Rocq tactic fragments, and its downstream proving set was selected for partial progress and tactic relevance; the second-route or held-out promotion rule is this workbench's stricter safeguard, not a reported TacMiner result. Do not store long paper summaries. Store the local move, dependencies, and failure mode.

### 9. Theorem-Repair Engine

When the idea almost works, ask which theorem should replace the original.

- Add the weakest assumption that fixes the failing central lemma.
- Weaken uniqueness to set-valued optimality.
- Weaken strict monotonicity to monotone selection.
- Change exact optimality to approximation or bound.
- State conditional proof if the economic or modeling meaning changes.

## Route Score

Score an idea before spending proof time:

- Does it control the failure world?
- Does it use the stated assumptions rather than invented ones?
- Does it produce a named central lemma?
- Can the central lemma be tested on a toy case or checked by a tool?
- Does it assemble back to the exact theorem?

Prefer the idea with the best failure control and verification hook, even if it is less elegant.

## Stop Rule

Stop the idea pass when one route has the needed pattern guess, a plausible central object, proof kernel or central lemma, and verification hook. If no route appears after two idea engines, move to counterexample search or retrieval rather than generating more prose.
