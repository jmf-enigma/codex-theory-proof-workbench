# Novel Problem Discovery

Use this only when the answer, extremal object, constant, formula, construction, invariant, or decisive concept is genuinely unknown. It is a discovery controller, not a claim that brute-force search can solve every open problem.

## Map

- Status gate: distinguish unknown-to-us from apparently open or genuinely new.
- Discovery contract: define what is generated, how it is checked, and when it is promoted.
- Frontier ladder: connect solved neighbors to the first unresolved case.
- Search cycle: alternate diverse global proposals with local repair under exact feedback.
- Concept and theorem extraction: turn patterns and failed searches into reusable mathematics.
- Discover-to-prove handoff: freeze one candidate before starting the proof loop.
- Stop and steering rules: stop on evaluator, representation, or prerequisite failure.

## Status Gate

Before expensive search:

1. Freeze the exact problem statement and intended notion of solution.
2. Run a bounded literature and local-result scan. Record exact neighboring theorems, best known bounds, and dates.
3. Classify the status as `known`, `likely known`, `apparently open`, or `genuinely new`. Use `apparently open` unless the novelty check is unusually strong.
4. Separate a missing answer from a missing proof. If the candidate answer is already supplied, return to the ordinary proof loop.
5. Preserve source fidelity. A solution to a weakened, discretized, or finite version is a partial result until the original quantifiers are restored.

The literature scan serves two purposes. It checks novelty and identifies solved neighbors, representations, baselines, obstructions, and evaluators. It does not authorize importing a result whose assumptions do not match.

## Discovery Contract

Do not launch broad candidate search until these fields are concrete:

- **Discovery target**: answer, threshold, formula, construction, policy, invariant, counterexample, intermediate theorem, or new representation.
- **Candidate representation**: the smallest object the search is allowed to modify, such as a graph, priority function, recurrence, basis, dual certificate, or lemma statement.
- **Validity gate**: an exact checker for feasibility, domains, constraints, and statement fidelity.
- **Score or evaluator**: a scalar or ordered tuple that distinguishes progress after validity passes.
- **Simplification ladder**: solved restrictions, small cases, relaxations, and the first unresolved frontier.
- **Holdout cases**: cases not used to generate the pattern, especially larger sizes, boundaries, adversarial parameters, and symmetry variants.
- **Promotion criterion**: the evidence required before a candidate becomes a fixed conjecture or proof target.
- **Budget**: candidate count, tool calls, time, or tokens, plus a plateau rule.

The evaluator should be a cascade, not one vague score:

1. statement and type validity;
2. exact feasibility or counterexample check;
3. objective or approximation quality;
4. holdout robustness and extrapolation;
5. simplicity, novelty, and proof affordance.

If no trustworthy evaluator exists, first design a finite relaxation, falsification oracle, residual check, symbolic identity test, or conditional assembly test. Without one of these, use bounded conceptual exploration and human steering rather than evolutionary search.

## Frontier Ladder

Build a short ladder from understood to unresolved:

| rung | version | status | witness or proof | first obstruction |
| --- | --- | --- | --- | --- |
| 0 | trivial or boundary case | solved | exact |  |
| 1 | smallest nontrivial case |  |  |  |
| 2 | strongest solved restriction or relaxation |  |  |  |
| 3 | first unresolved case |  |  |  |
| 4 | original asymptotic or general claim |  |  |  |

Use the first transition whose mechanism is not understood. A good discovery cycle should explain or cross one rung. Merely improving a score on a distant finite instance is not automatically progress on the theorem.

## Search Cycle

Keep two to four candidate families, not one long monologue.

1. **Seed** from solved neighbors, equality cases, literature constructions, failed proof prefixes, and random or symmetric baselines.
2. **Generate global jumps** by changing basis, representation, decomposition, invariant, construction family, or proof kernel.
3. **Repair locally** with small feasibility-preserving mutations, algebraic simplification, local search, or verifier feedback.
4. **Evaluate exactly** whenever possible. Reject invalid candidates before comparing quality.
5. **Archive diversity**. Keep the best candidate per structurally distinct family, a few informative failures, and the failure witness. Do not keep only the top scalar score.
6. **Share across branches** only as named components. Combine a representation from one branch with a local certificate from another; do not average incompatible arguments.
7. **Adapt the schedule**. Explore broadly early. After repeated valid improvements, concentrate on elite families while retaining one orthogonal branch.
8. **React to stagnation**. Local stagnation triggers branch review or cross-branch transfer. Global stagnation triggers representation change, evaluator audit, frontier-ladder revision, or stop.

For construction problems, alternate global pattern generation with a problem-specific local improver. For formula discovery, infer the shortest law explaining seed cases, test holdouts, then derive why that law should persist. For analytical problems, search over representations and bases as well as identities; a new basis or normalization can remove the obstruction rather than merely simplify its notation.

## Concept And Lemma Invention

Novel problems may require a new intermediate object rather than a better route through old objects. Propose a definition only when it earns its cost by doing at least two of these:

- compressing several recurring expressions or failure witnesses;
- turning a global obstruction into a local invariant or monotone quantity;
- transferring across multiple rungs of the simplification ladder;
- exposing a checkable lemma or certificate;
- explaining the structure shared by several elite candidates.

Treat every reached, independently verified intermediate statement as a theorem candidate, even if the original search failed. Promote it to reusable memory only when it is general rather than a specialization, difficult or costly to rederive, useful in more than one branch, and accompanied by a proof or checker. Deduplicate by implication or specialization before growing the lemma library.

## Discover-To-Prove Handoff

Discovery and proof are separate stages:

1. Record one explicit candidate object, answer, formula, or theorem statement.
2. Run validity, holdout, boundary, and novelty checks.
3. Freeze the candidate. Subsequent proof attempts may repair the theorem openly but may not silently move the answer.
4. Rewrite the unknown-answer problem as a fixed theorem about that candidate.
5. Return to the ordinary workbench: theorem fence, negation, lemma graph, local certification, assembly, and adversarial review.

A finite construction is not a universal theorem. A numerical identity is not an exact formula. A high score is not originality. Keep `candidate`, `empirically supported`, `formally checked`, and `proved` as distinct statuses.

## Stop And Steering Rules

Stop or ask for steering when any of these holds:

- no exact or defensible proxy evaluator can be built;
- the archive has collapsed to equivalent candidates;
- two plateau cycles add no valid candidate, new frontier rung, representation, or theorem;
- holdout performance fails repeatedly, indicating overfitting to seed cases;
- the remaining step requires an unavailable domain theorem or modeling judgment;
- the budget is exhausted;
- a candidate is ready for proof, so continued discovery would move the target.

Report the strongest honest artifact: best candidate and checker, improved bound, counterexample, solved frontier rung, reusable intermediate theorem, failed representation, or exact missing prerequisite.

## Paper-Grounded Lessons

- [Discover and Prove](https://arxiv.org/abs/2604.15839) separates unknown-answer discovery from formal proving; its ablation supports freezing the discovered answer before rewriting the formal goal.
- [AlphaEvolve](https://arxiv.org/abs/2506.13131) and [Generative Modelling for Mathematical Discovery](https://arxiv.org/abs/2503.11061) use executable evaluators, diverse program populations, and human-controlled validity-preserving solvers.
- [PatternBoost](https://arxiv.org/abs/2411.00566) alternates global pattern generation with local problem-specific improvement; either side alone can be much weaker.
- [AI-assisted open-problem discovery](https://arxiv.org/abs/2603.04735) searches across analytical representations, prunes most branches with high-precision numerical feedback, and then uses a separate rigorous refinement pass.
- [Self-supervised theorem discovery](https://arxiv.org/abs/2606.28747) reuses reached theorems and selects library additions by generality and difficulty of reproof rather than by interesting-looking prose.
- [MLEvolve](https://arxiv.org/abs/2606.06473) motivates cross-branch references, retrospective memory, explicit stagnation triggers, and an exploration-to-exploitation schedule for long-horizon search.
- [QED](https://arxiv.org/abs/2604.24021) motivates clean prover/verifier context, exact citation and statement checks, stable plans, and independent review for open-problem claims.
- [From Solvers to Research](https://arxiv.org/abs/2607.07779) identifies the remaining boundary: evaluator-driven search scales existing representations, but genuinely new mathematics may require concept invention, relational transfer, and human judgment.

These systems provide useful mechanisms and case studies, not a general guarantee of solving open problems. Import only the control rule that matches the current problem and produces a checkable artifact.
