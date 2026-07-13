# Research-Backed Proof Loop

Use this only for hard, research-level, or repeatedly failed proofs. Keep `SKILL.md` thin and load this file on demand.

## Map

- Imported patterns: use proof-agent and formalization lessons as light control rules.
- Loop: run statement audit, retrieval, workstream assignment, local proof, repair, and review in order.
- Stop budgets: stop or reroute when the proof state is unchanged, not merely when prose runs out.
- Prover-verifier loop: use one-move contracts, verifier verdicts, trace-back, and repair when local steps are fragile.
- Paper-inspired heuristics: turn outside sources into route structure, artifacts, and verification hooks.
- Source log: track where each imported workflow pattern came from.

## Imported Patterns

- Thin skill architecture: keep the trigger and core workflow short; move long proof tactics and references into separate files so normal use stays cheap.
- Lean-style cycle: plan, work, checkpoint, review, replan, then continue or stop. Natural-language proofs should use the same discipline even without Lean.
- Statement preservation: proving mode should not silently change theorem headers, assumptions, quantifiers, or conclusions. If a proof needs a different statement, mark theorem repair.
- Draft-Sketch-Prove: first draft the informal argument, then turn it into a proof sketch of named subgoals, then prove or repair each subgoal.
- Retrieval-augmented proving: before inventing a lemma, retrieve nearby known theorem patterns, paper lemmas, mathlib names, prior ledgers, formalization projects, and proof-agent workflows.
- Compiler/tool-guided repair: if Lean, algebra, Z3, CVXPy, Sage, or a finite example rejects a step, isolate the failing sublemma and repair that local statement.
- Proof-state feedback: try one proof move, check whether the subgoal is smaller, unchanged, or larger, and keep only moves that create a useful delta.
- Progress-aware search: do not spend unlimited effort on a route whose remaining obstruction is not shrinking.
- Lab-notebook memory: summarize failed proof states concisely so the next cycle sees the obstruction instead of rediscovering it.
- AI co-mathematician pattern: maintain a stateful workspace, treat failed workstreams as permanent project artifacts, surface uncertainty, and let the user steer when domain intuition can unlock a stalled route.
- Goal-based workstreams: define approved goals first, then create bounded workstream cards. Each card may use retrieval, computation, proof search, review, or steering as needed.
- How-others-do-it gate: before heavy execution, inspect nearby papers, appendices, prior ledgers, theorem names, analogous models, and formal-library patterns. Extract architecture and hidden assumptions, not prose.
- STAR-PolyaMath pattern: separate control from inference. The coordinator owns state, stop rules, trace-back, re-plan, and tool-use limits; the proof attempt supplies evidence and arguments, not control authority.
- Persistent meta-strategist pattern: keep cross-attempt memory of chronic failures, overused tools, failed plan families, and promising auxiliary routes. Use it to issue light guidance or mandatory route changes when a loop repeats.
- Reasoner-Verifier challenge pattern: review each fragile step with a goal gate and a logic gate. A step can be accepted, challenged, traced back to an earlier step, or sent to re-plan. Set a small challenge-round and replan cap before the loop starts.
- Prover-Verifier Game pattern: optimize for checkability under adversarial scrutiny. Ask whether a plausible but false version of the same local move could fool the verifier.
- Structure-consistency pattern: final proofs should use accepted subgoals or explicitly retire them; do not let a successful local proof drift away from the blueprint it was supposed to close.
- Rethlas/Archon pattern: separate informal strategy discovery from formal verification. The informal agent proposes routes and candidate proofs; the formal agent decomposes, formalizes, checks, and returns precise gaps.
- MA-LoT pattern: separate whole-proof generation from error-analysis/correction. Use one role to produce a coherent proof sketch and another role to read compiler/tool feedback and repair only the failing block.
- Ax-Prover pattern: tool-equipped agents can operate autonomously or with human experts, but formal correctness must come from Lean/tool feedback rather than role confidence.
- Tiered activation: use a micro pattern check for small unclear proofs, a workstream card for expensive branches, and a full project only when the proof needs durable state.
- Goedel-Architect blueprint pattern: plan a global dependency graph of definitions and lemmas before proving; prove nodes with only their declared dependencies; preserve solved nodes; diagnose failed nodes as `STATEMENT_WRONG` or `PROOF_TOO_HARD`; revise only the failed subgraph and its dependents.
- Numina/LEAP pattern: try direct formalization or direct proof first; if it fails, decompose into an AND/OR blueprint DAG, check that child lemmas are simpler and acyclic, and memoize shared subgoals.
- OProver pattern: repair from compact state, not full transcript: statement, retrieved context, previous attempt, and previous feedback. Feedback-conditioned repair beats blind regeneration.
- APOLLO pattern: preserve a useful skeleton, replace the bad block with a named sublemma, use solvers/search for routine blocks, and recursively repair only remaining gaps.
- AlphaProof Nexus pattern: maintain a small population of proof sketches, use reviewer/rater passes for decomposition quality, distinguish good gaps from bad gaps, and reuse solved or refuted subgoals.
- Cost-quality agent pattern: failed proof trajectories are useful routing signals. After repeated local failures, decide whether another attempt has positive value by checking proof-state delta, failure diversity, proof similarity/repetition, attempt count, and expected artifact.
- LeanArchitect pattern: keep informal and formal-blueprint views synchronized. Separate statement dependencies from proof dependencies, track statement readiness separately from proof status, and audit metadata when a node looks formally plausible but mathematically wrong.
- Aristotle pattern: combine informal lemma generation with Lean feedback and Monte Carlo-style proof-state search. Represent proof work as an AND/OR graph: alternative tactics/routes are OR choices, while all subgoals from a tactic or decomposition are AND obligations.
- Aristotle graph-search lesson: merge equivalent proof states and equivalent actions before spending more budget. Two states are equivalent for this workbench when the goal, local assumptions, central object, and failure witness are the same, even if notation changed.
- Aristotle bottleneck lesson: for an action that creates several required subgoals, prioritize the hardest unresolved child first. Do not expand new routes while an existing AND child is a known bad gap.
- Aristotle lemma-revision lesson: after a failed proof, keep proved helper lemmas, mark unproved or false lemmas explicitly, and revise only the failed subgraph plus its dependents.
- Aristotle verification lesson: compiling or receiving a formal artifact is not proof unless the main theorem has no `sorry`, admitted axioms, unresolved obligations, or unproved global assembly step.
- Evolutionary-search lesson: keep a small diverse frontier of proof sketches, but attach an automated or cheap evaluator to every candidate. Selection without a verifier only amplifies plausible prose.
- Discover-and-Prove lesson: when the answer itself is unknown, discover and challenge one candidate first, then freeze it and rewrite the task as a fixed theorem. Do not combine answer invention and formal proof in one uncontrolled pass.
- PatternBoost lesson: for search over constructions, alternate global structural proposals with a problem-specific local improver. Preserve diverse elites because scalar best-only memory collapses useful families.
- Self-supervised theorem-discovery lesson: failed trajectories can still reach valid intermediate theorems. Promote only general, hard-to-rederive, independently checked statements that reduce later search.
- Research-frontier lesson: evaluator-driven search is strongest inside a chosen representation. When all branches plateau for the same structural reason, audit the representation and try a definition or concept that compresses several obstructions before spending more search budget.
- Goedel-Prover-V2 correction lesson: preserve the valid prefix and precise verifier error when repairing a formal or algebraic attempt. Blind whole-proof regeneration discards useful state.
- Process-verification lesson: the first failed inference invalidates its suffix. Credit and reuse only the independently checked prefix and helper nodes.
- Aletheia lesson: generator, verifier, and reviser can be serial roles, but verification must be a separate pass and may return failure or uncertainty instead of forcing a proof.
- Self-play lesson: generate conjectures, examples, or helper lemmas near the current ability frontier, but reject artificial variants that add difficulty without helping the target dependency graph.
- LEAP decomposition-review lesson: a child can be formally admissible yet equivalent to an ancestor. Require semantic simplification and a conditional parent assembly before committing it.
- LeanMarathon repair-radius lesson: design the blueprint so one bad statement has few dependents, keep repair agents source-aware, and never use physical proof length as a reason to abandon a node.
- LeanSearch v2 retrieval lesson: multi-step proofs need a jointly sufficient premise bundle. Use sketch-retrieve-filter-judge-revise rather than independent similarity searches.
- Prover Agent discovery lesson: useful auxiliary lemmas can reveal a proof strategy bottom-up even when they do not appear in the final proof. Bound these probes and promote only those that expose structure.
- Hilbert failure-profile lesson: separate sketch generation, sketch assembly, and local solving failures because they require different compute and repair policies.
- Generative-verifier lesson: natural-language judges can learn stylistic rigor without mathematical validity. Agreement among similar judges is not independent evidence.
- Formal Conjectures lesson: proof and disproof attempts audit the statement. Distinguish translation errors, underspecified conventions, and source-level errors before treating a formal success as the intended theorem.
- Multi-agent dispatch lesson: parallelism helps only when roles are non-overlapping and artifact-based. Useful proof roles are Planner, Falsifier, Retriever, Formalizer/Tool-Checker, Reviewer, and Integrator. The integrator remains responsible for statement fidelity, route choice, and final proof status.

## Loop

1. Prior-result audit: list definitions, assumptions, and allowed prior theorems. A step is not allowed in the final proof unless it is a prior result, a proved lemma, or a checked derivation.
2. Pre-solve gate: check whether a direct theorem, certificate, contradiction, or known decomposition solves the claim. If it does, prove directly and verify.
3. Negation and toy model: if direct solve is not available, write what a counterexample needs, then test scalar, two-action, two-type, one-period, boundary, deterministic, and symmetric cases when available.
4. Optional idea pass: if the central route is unclear, use `proof-idea-generator.md` to propose a failure world, small-case pattern guess, central object, proof kernel or central lemma, and verification hook. Skip this when the theorem family is already obvious.
5. Retrieval: before inventing a new central lemma, search relevant playbooks, prior ledgers, local paper text, user-provided papers, paper appendices, theorem names, formal libraries, and external proof-pattern sources if available. For small unclear proofs, do this as a micro check and stop after one useful pattern or a clear mismatch. Use `external-proof-pattern-scan.md` when the proof is unfamiliar or repeatedly stuck.
6. Workstream assignment: for hard projects, fill `WORKSTREAMS.md` with approved goals and only the active workstream cards needed next. Each card must include a look-at-how-others-do-it pass or a skip reason. Keep the first pass to one to three strong sources or patterns. Use roles serially by default; use actual parallel agents only when the user explicitly asks.
7. Multi-agent dispatch gate: if the user asked for parallel agents, write role briefs before delegation. Each role must have a single artifact, explicit exclusions, and a stop rule. Do not spawn two agents to write competing full proofs of the same route.
8. Integrator checkpoint: after agents return, merge artifacts by proof-state delta, not by eloquence. Prefer counterexamples, verified lemmas, hidden assumptions, retrieved theorem patterns, and concrete gap reports over long prose.
9. Discovery gate: if the theorem contains an unknown construction, coefficient, threshold, policy, potential, active set, hard instance, or numerical answer, treat memory as unverified and first scan exact/neighboring results, recent cited-by work, and public active projects. Record verified source anchors and the precise frontier gap. Only then discover and self-check the object with holdouts and a verification hook; do not let the proof infer the answer by wishful algebra.
10. Draft: write a rough proof in 5-10 steps. Each step must name its intended theorem family, such as convex duality, envelope, single crossing, martingale concentration, elliptical potential, or information lower bound.
11. Sketch: convert the draft into a blueprint dependency graph. Each node gets statement dependencies, proof dependencies, downstream use, likely proof route, tool check, statement status, proof status, failure mode, gap grade, and compact repair state. Independent branches should stay independent.
12. Decomposition admission: before committing children, write a conditional parent assembly and review strict simplification, acyclicity, source fidelity, repair radius, and premise feasibility. Reject formally valid but non-simplifying children.
13. Graph search discipline: mark OR nodes for alternative routes, constructions, or tactics; mark AND nodes for required subgoals. Before expanding a new OR branch, check whether an existing AND child is the bottleneck and should be proved, refuted, split, retrieved, or repaired first.
14. Frontier choice: keep two to four non-equivalent candidates at most. Give each one an expected artifact and the cheapest decisive evaluator. Expand the candidate with the best qualitative combination of decision value, assembly relevance, novelty, and cost.
15. State/action dedupe: compare a new proof move against prior states and fingerprints. If the goal, local assumptions, central object, failure witness, and expected artifact match a prior attempt, treat it as the same state/action unless there is a real new premise or certificate.
16. Prove locally: solve the smallest ready leaf on the current assembly path first. Work one move at a time when fragile: proposed move, expected new subgoal, check, proof-state delta. Tag the move as tool-verified, easy-to-check, or hard-to-check; accept it only if it passes both the declared-goal gate and the logic gate. For repeated or adversarially fragile moves, use `prover-verifier-loop.md` to record the prover move, verifier verdict, soundness probe, proof-state delta, and coordinator decision. Use Wolfram/SymPy for algebra, Python/Z3/CVXPy/Sage for finite or optimization checks, and Lean for local formalizable lemmas. If a top-level assembly can be checked conditionally using assumed lemmas, use that to identify which lemmas are actually needed before proving side lemmas.
17. First-error and stage pass: when a check fails, identify the earliest invalid step, preserve the verified prefix, classify the failure stage, and invalidate only affected dependents. Repair strategy, decomposition, retrieval, local proof, assembly, fidelity, or library coverage at its own layer.
18. Bottleneck surgery: if the same lemma remains unresolved, shrink it, flip to the negation, change representation, then certify/falsify/retrieve/repair before another prose proof.
19. Gap review: accept a missing lemma only if it is a good gap, meaning smaller, non-circular, assumption-explicit, and checkable. If it is a bad gap, split, retrieve, falsify, or change route.
20. Repair: if a lemma fails, determine whether the issue is false claim, missing assumption, quantifier mismatch, boundary case, or proof technique mismatch.
21. Lemma revision loop: preserve proved nodes and verified helper lemmas, then generate only the missing helper lemmas needed by the failed subgraph. Do not rewrite solved parts unless their statement dependencies changed.
22. Route decision: after two failed local attempts or one repeated failure signature, choose one action before another attempt: continue current node, locally repair, re-decompose the subgraph, retrieve a premise/paper pattern, run a tool/falsification check, or stop/report. Continue only if the next attempt has new evidence or the proof state is shrinking.
23. Recombine: assemble only after all essential lemmas have statuses. Verify exact variables, quantifiers, constants, events, and assumptions.
24. Formal artifact audit: if Lean, Aristotle, or any prover/API produced code, inspect declarations and dependencies. A helper lemma being verified does not prove the theorem unless the final theorem reduces to verified obligations and has no `sorry` or admitted gap.
25. Review: adversarially attack the proof. Try to break the weakest lemma and the final assembly.
26. Human steering checkpoint: if the obstruction is mathematical taste, model choice, definition choice, or a missing heuristic rather than a narrow check, ask the user for domain intuition before spending another heavy cycle.
27. Escalate: if two consecutive cycles make no progress, use `proof-escalation-protocol.md` to choose counterexample search, tool certification, retrieval, local formalization, theorem repair, or stop/report.

## Stop Budgets

- Small lemma: 10-20 minutes or one route plus one counterexample search.
- Medium theorem: 30-60 minutes, two proof routes, one toy/refutation pass, one tool-check pass.
- Hard/repeatedly failed proof: create a proof project, run at least two routes, and keep a ledger. Escalate after two unchanged obstruction cycles or when a missing lemma becomes the bottleneck.
- Micro pattern check: one theorem family, prior ledger, or close paper pattern; stop as soon as it yields a central object, hidden assumption, or mismatch.
- Never use proof length, number of written lines, or polished prose as a mathematical stopping signal. Stop on repeated proof state, exhausted artifact-bearing moves, prerequisite absence, or an explicit time/token budget.

## Paper-Inspired Heuristics

- Use informal proof as guidance, not authority. A plausible paragraph should become a checkable sketch before it becomes final prose.
- Use proof ideas as hypotheses, not proof steps. An idea becomes useful only when it yields a central lemma, certificate, counterexample family, or theorem repair.
- Treat guessed formulas, potentials, active sets, and algebra normal forms as conjectures until they pass a holdout case or produce an independently checkable certificate.
- Prefer premise retrieval over free invention when a proof uses standard machinery.
- Treat failed proof states as data: record the exact bad step and reuse it to avoid repeating the same route.
- Let proof-state delta govern search: if a move only renames the same missing lemma, it is not progress.
- Use failed-attempt features as a stop signal: repeated proof shape, low failure diversity, no smaller subgoal, high attempt count, and no new artifact mean route away rather than retry.
- Keep a compact failed-state note: subgoal, attempted move, why it failed, and what new ingredient would make a retry legal.
- Preserve negative results as first-class outputs. A rejected proof can still contain the right strategy, missing condition, useful counterexample, or reusable trick.
- Use coordinator-style summaries for hard projects: current claim, active routes, blocked lemma, failed routes, next bounded move, and where user steering would help.
- Keep each workstream small: first extract how similar work is done, then return one bounded artifact. Retrieval returns a pattern card, computation returns a certificate or counterexample, proof search returns a lemma status, review returns gaps, and steering returns one precise question. If none of these outputs is expected, do not open a workstream.
- For multi-agent runs, keep the coordinator/integrator single-threaded. Parallel agents produce evidence; they do not vote the proof true. The integrator chooses the route and records why.
- Good multi-agent split: Planner finds lemma graph and route options; Falsifier searches small failures; Retriever imports theorem patterns; Formalizer/Tool-Checker checks one local lemma; Reviewer attacks final assembly. Bad split: several agents all write the same full proof.
- For long step plans, use STAR-PolyaMath-style verdicts: accept if both gates pass, challenge if the local fix is plausible, trace back if an earlier step caused the failure, re-plan if the plan family is broken, and stop/report if challenge, replan, time, or token budgets are exhausted.
- For adversarial local checks, use PVG-style sneaky proof review: try to make the same step look true while hiding the weakest counterexample, boundary case, or missing assumption.
- If computation or CAS use dominates without a shrinking proof state, switch to pure mathematical analysis of the tool artifacts or retire the route. Tools should decide kernels, not replace strategy.
- For formalizable fragments, Lean-style checking is strongest on local lemmas, not necessarily on the full research theorem.
- For empirical or simulation support, route to `empirical-tools`; simulations can refute or sanity-check but do not prove the theorem.
- When searching papers or existing skills, extract route structure, certificate type, stopping rule, and failure repair rule. Do not import unexplained claims as proof steps.
- When a proof attempt fails, require a structured forfeit: diagnosis, forensic analysis, and suggested fix. If the statement is false, repair/drop it. If the proof is too hard, split it into helper lemmas.
- When a local proof skeleton is coherent but a block fails, "sorrify" the block: name it as a lemma, preserve the good skeleton, and repair only the isolated lemma.
- When several routes are plausible, keep a small candidate board rather than one long monologue. Rate each route by plausibility, novelty, decomposition quality, evidence, and risk of circularity.
- Use a used-node filter in lemma graphs: prove only definitions and lemmas that are on the current route to the theorem, unless an exploratory lemma has a clear falsification or theorem-repair purpose.
- For long proof projects, target fidelity comes before proof effort. If the statement, role, or dependency metadata of a node is suspect, file a repair note before trying to prove it.
- For formal prover/API outputs, separate verified helper components from unverified global bookkeeping. Local exchange, algebra, or monotonicity lemmas may be real progress even when the final counting, assembly, or theorem statement is still open.
- Use proof history as a visible action trace. A short comment on why a move was tried helps later cycles avoid circular trajectories, but do not preserve hidden or sprawling reasoning in the active context.

## Source Log

Keep provenance compact; operational rules above are the part to use.

- **Blueprint, decomposition, and durability**: Draft-Sketch-Prove, Goedel-Architect, LeanArchitect, [LEAP](https://arxiv.org/abs/2606.03303), [LeanMarathon](https://arxiv.org/abs/2606.05400), [MerLean-Prover](https://arxiv.org/abs/2605.26959), [Delta Prover](https://arxiv.org/abs/2507.15225), and [Hilbert](https://arxiv.org/abs/2509.22819) motivate dependency graphs, semantic decomposition review, low repair radius, source-aware repair, and failure-stage routing.
- **Retrieval, strategy growth, and local repair**: LeanDojo/ReProver, [LeanSearch v2](https://arxiv.org/abs/2605.13137), [Prover Agent](https://arxiv.org/abs/2506.19923), [OProver](https://arxiv.org/abs/2605.17283), APOLLO, and [proof-strategy extraction](https://arxiv.org/abs/2510.10131) motivate global premise bundles, bottom-up auxiliary lemmas, verified repair memory, and reusable strategy promotion.
- **Discovery and route search**: [Discover and Prove](https://arxiv.org/abs/2604.15839), [AlphaEvolve](https://arxiv.org/abs/2506.13131), [PatternBoost](https://arxiv.org/abs/2411.00566), [AI-assisted open-problem discovery](https://arxiv.org/abs/2603.04735), [self-supervised theorem discovery](https://arxiv.org/abs/2606.28747), [MLEvolve](https://arxiv.org/abs/2606.06473), AlphaProof Nexus, and [Aristotle](https://arxiv.org/abs/2510.01346) motivate discover-then-prove handoff, evaluator-backed diverse populations, local-global alternation, cross-branch memory, theorem extraction, AND/OR search, and state deduplication.
- **Research-level limits**: [QED](https://arxiv.org/abs/2604.24021) and [From Solvers to Research](https://arxiv.org/abs/2607.07779) motivate independent verification, exact statement and citation checks, concept/representation audits, and honest human steering for genuinely new problems.
- **Control and collaboration**: [AI co-mathematician](https://arxiv.org/abs/2605.06651), [STAR-PolyaMath](https://arxiv.org/abs/2605.19338), MerLean-Prover, Numina-Lean-Agent, Rethlas/Archon, and Ax-Prover motivate persistent workspaces, bounded artifact roles, trace-back, re-plan, and a single integrator.
- **Correction and verification**: [Goedel-Prover-V2](https://arxiv.org/abs/2508.03613), [process-verified theorem proving](https://arxiv.org/abs/2606.20068), [Aletheia](https://arxiv.org/abs/2602.10177), and Prover-Verifier Games motivate first-error feedback, verified-prefix reuse, independent checking, abstention, and final assembly audits.
- **Decomposition curriculum**: [DeepSeek-Prover-V2](https://arxiv.org/abs/2504.21801) and [self-play theorem proving](https://arxiv.org/abs/2502.00212) motivate recursive subgoals and useful near-frontier auxiliary problems.
- **Natural-language verification**: [scaling generative verifiers](https://arxiv.org/abs/2511.13027) motivates evidence-diverse checking and warns that stylistic rigor or same-family verifier agreement is not proof validity.
- **Fidelity and status honesty**: [Formal Conjectures](https://arxiv.org/abs/2605.13171) and formal-prover case studies motivate statement audits and the rule that verified helper lemmas do not close an unencoded or `sorry`-bearing main theorem.
