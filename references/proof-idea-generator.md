# Structural Proof Discovery

Use this only when the theorem is not directly solvable because its central object, construction, or first nonroutine implication is missing. It is a menu, not a checklist.

An idea is an executable hypothesis. It predicts one local mathematical fact, names the cheapest way to support or kill it, and changes the next action.

## The Compact Pass

Write one sentence for each item:

1. **Failure world:** what is the smallest shape of a counterexample?
2. **Tight world:** where should equality, indifference, or a binding constraint occur?
3. **Central object:** what quantity, correspondence, event, certificate, or representation controls both worlds?
4. **Proof kernel:** what exact local statement would make the rest routine?
5. **Check:** what observation, theorem, counterexample, identity, or formal leaf would decide that kernel cheaply?
6. **Assembly:** assuming the kernel, what short chain establishes every part of the exact target?

Then choose one route and try it end to end. If this pass produces only generic nouns, switch to a different lens below rather than elaborating the prose.

## Structural Lenses

Select the lens that matches the obstruction. Do not run all of them.

### Failure and contradiction

Write the negation with the fewest objects possible. Ask what must prevent it.

- monotonicity: two states, types, or parameters in reversed order;
- threshold: two crossings of an action difference;
- incentive compatibility: one profitable deviation or positive deviation cycle;
- optimality: one feasible improving move;
- regret: one history where the event or summation bound fails;
- lower bound: one algorithm that distinguishes the proposed hard instances too cheaply.

The object that excludes this failure is often the correct invariant or certificate.

### Tight case and reverse engineering

Start where the theorem is barely true. Locate equality, zero slack, an indifferent action, a binding constraint, a worst history, or least-favorable pair. Reverse-engineer the algebra or construction that makes this case visible.

A useful clever construction should explain the known tight example. If it does not, treat it as decorative.

### Assumption to mechanism

Translate assumptions into mathematical operations:

- compactness plus continuity gives existence;
- convexity or concavity turns local certificates into global conclusions;
- increasing differences or single crossing gives order or thresholds;
- quasilinear IC gives envelope, payment identities, or cyclic monotonicity;
- Markov structure gives Bellman recursion;
- adaptive data gives filtrations and martingales, not iid arguments;
- KL closeness gives testing and lower-bound transfer.

If a desired step has no supporting assumption, the theorem may be false or incomplete. If an assumption buys no step, check whether the proof has silently omitted its role.

### Representation change

Move one rung, not five:

1. original expression;
2. difference, slack, equality case, or deviation;
3. structural object such as a potential, dual, envelope, coupling, or good event;
4. certificate, countermodel, or formal leaf.

Useful normal forms include telescoping gaps, add-and-subtract benchmarks, convex conjugates, completed squares, log products, KL/TV bridges, Bregman divergences, symmetrization, conditioning, and boundary/interior splits.

Discard the representation if it does not make the recorded obstruction smaller or more checkable.

### Small cases and pattern discovery

Compute or derive the smallest cases to guess an exact formula, threshold, active set, coefficient pattern, hard instance, or invariant. Keep at least one holdout case that was not used to guess the pattern.

Promote a guess only when it survives the holdout and yields a proof kernel, theorem pattern, or independently checkable certificate. A surviving pattern creates a new proof obligation; it does not discharge the theorem. No-small-counterexample results are search signals, not proofs.

### Retrieval and proof migration

Search one close theorem family when the missing ingredient may already exist. Extract a proof move rather than a slogan:

- source theorem and definitions;
- exact assumption mapping;
- construction, reduction, invariant, or certificate to transfer;
- first point where the source proof does not apply;
- one local check that would validate the migration.

Do not force the current problem into a theorem with stronger hypotheses before understanding why those hypotheses were needed.

## Domain Seeds

Use these as starting objects, not as automatic answers.

| Domain | Objects worth inspecting first |
| --- | --- |
| DP/MDP | Bellman gap, value difference, post-decision value, monotone operator, coupling |
| Mechanism design | indirect utility, deviation graph, envelope, payment feasibility, cyclic monotonicity |
| Optimization/OR | dual variable, slack, exchange move, KKT residual, complementary slackness |
| Learning/bandits | good event, confidence radius, instantaneous regret, potential, filtration |
| Lower bounds | hard pair, packing, testing reduction, KL/TV bridge, least-favorable prior |
| Games/matching | potential, best-response correspondence, blocking-pair or exchange invariant |

## Lemma Admission

Before investing in an auxiliary lemma, ask:

1. Why does the target or tight case suggest this lemma?
2. Where is it consumed in the next few proof steps?
3. What part of the parent target becomes strictly simpler?
4. What would falsify or independently check it?

Reject a lemma that hides the main construction, restates the theorem, is equivalent to an ancestor, needs an unstated regularity condition, or has no downstream use.

## Construction Search

When the kernel needs a non-obvious object, generate at most three candidates with materially different mechanisms:

- one from the failure world;
- one from the tight or equality case;
- one from a nearby theorem, dual viewpoint, or changed representation.

For each candidate record only the central object, why it controls the failure, the cheapest decisive check, and the condition that retires it. Try the strongest candidate as a complete route. Keep the others dormant.

## Evidence-Layered Search Packet

Use this one-screen packet only when candidate rules or examples become noisy.

| Layer | Meaning | Proof effect |
| --- | --- | --- |
| sound shortcuts | exact theorem, rewrite, invariant, symmetry, duality, or decomposition | only after applicability is checked |
| executable falsifiers | replayable witness, finite model, separating algebra, or exact checker | refutation within its checked scope |
| scheduler priors | similarity, score, source hit, motif, or failure history | none |
| near-miss frontier | checked prefix, exact remaining gap, candidate bridge | none until the bridge is proved |

Audit semantic range before symbolic substitution. A compound term cannot be replaced by an arbitrary domain element unless its image is proved to cover that element. Sampled assignments, model agreement, retrieval rank, and failed finite search have `proof_effect=none`.

A failed attempt may donate a verified prefix, helper lemma, intermediate term, or obstruction fingerprint. A plausible trick remains `candidate` until its assumptions are source-checked and it replays on the current problem. This prevents an attractive false trick from poisoning later searches.

## Stop Rule

Stop the idea pass when one of these occurs:

- one route has a motivated central object, exact kernel, and decisive check;
- a counterexample or missing assumption is found;
- two moves preserve the same obstruction;
- every candidate hides the theorem inside an equally hard lemma.

In the last two cases, retrieve one closer premise, change representation, run one decisive tool check, repair the theorem, or report the exact obstruction. Do not produce another longer sketch.
