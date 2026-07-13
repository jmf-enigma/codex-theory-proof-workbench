# External Proof Pattern Scan

Use this when a proof is unfamiliar, has failed twice, or needs ideas from papers, formalization projects, or proof-agent workflows. The goal is to borrow search architecture and theorem patterns, not to copy prose or trust an unverified source.

Use a minimal scan first. For a small unclear proof, inspect one close theorem family, prior ledger, or paper pattern and stop when it changes the next proof move or clearly mismatches. Start from local papers, appendices, prior ledgers, and the closest theorem names. Browse broadly only when those sources do not identify a pattern guess, central object, proof kernel, central lemma, or missing assumption.

## Map

- When and what to scan: start local and stop when the next proof move changes.
- Extraction card and scorecard: turn sources into proof artifacts, hidden assumptions, and verification hooks.
- Importable patterns: borrow route control, dependency structure, and repair rules.
- Recent method patterns: use proof-agent literature as search architecture, not proof authority.
- Project use and queries: feed useful patterns into ledgers, attack matrices, and tool plans.

## When To Scan

- The theorem family is unclear or the current route keeps producing the same obstruction.
- A key lemma feels standard but the right theorem name is missing.
- Tool use is possible, but it is unclear which artifact would help.
- The user asks to learn from papers, proof assistants, or existing skills.
- The pre-solve gate says the claim is not directly solvable from the current assumptions and a micro pattern check is not enough.
- The answer is claimed to be new or open; the scan must distinguish unknown-to-us from a genuine frontier and identify the closest solved neighbors.

## What To Search

- Papers or docs for the theorem family: OR/MS, mechanism design, DP/MDP, learning theory, bandits, lower bounds.
- User-provided papers, local drafts, appendices, prior proof ledgers, and nearby papers in the same model family.
- Formalization projects: Lean/mathlib examples, blueprints, Liquid Tensor-style dependency graphs, Flyspeck-style certificates.
- Prover papers: Draft-Sketch-Prove, retrieval-augmented proving, compiler-guided repair, counterexample-guided repair, tree or best-first proof search.
- Agent skills/workflows: Lean proof skills, proof-review skills, proof-memory systems, formalization workflows.
- Recent proof-agent methods: blueprint refinement, compact feedback repair, AND/OR proof DAGs, answer-discovery before proof, evolutionary proof sketches, structured forfeits, and statement-fidelity audits.
- Long-horizon harness methods: target-fidelity review, dynamic DAG leaves, local repair scopes, cost-aware route decisions, and used-lemma filters.
- For a novel problem, search exact formulations, best known bounds, solved restrictions, counterexamples, benchmark instances, evaluator code, and dates. Record status evidence separately from proof inspiration.

## Extraction Card

For every useful source, record:

- source:
- search cutoff and queries:
- active-work signals: recent papers, authors, projects, or an evidence-bounded `none found`.
- trick name:
- theorem family:
- proof decomposition:
- retrieval target: theorem name, library lemma, assumption list, or paper lemma.
- tool/certificate pattern:
- failure or repair rule:
- routing or stopping rule:
- dependency lesson: statement dependency, proof dependency, downstream use, or orphan lemma.
- premise bundle: which results must work together, not merely resemble the target.
- repair-radius lesson: how much of the graph changes if this imported step fails.
- source anchor: the exact definition, theorem, or proof passage that prevents route drift.
- source verification: DOI/publisher, arXiv, proceedings, or another official page.
- failure stage addressed: strategy-discovery / decomposition / premise-retrieval / local-proof / assembly / fidelity / library-coverage.
- transplantable idea:
- hidden assumptions:
- verification hook:
- limits: what does not apply to the current problem.

## Route Scorecard

After scanning, score only routes that change the next proof move:

- route:
- retrieved premise or theorem:
- evidence type: paper lemma / formalized lemma / tool certificate / counterexample family / agent workflow.
- dependency value: high / medium / low.
- certificate availability: direct / local / indirect / none.
- failure risk: boundary / quantifier / missing assumption / theorem mismatch / computational trust.
- next experiment: prove, falsify, retrieve more, tool-check, formalize local lemma, or repair theorem.

Prefer a route with medium plausibility and a checkable certificate over a route that feels elegant but has no falsification or verification path.

## Patterns To Import

- **Blueprint graph**: build a dependency graph of definitions, lemmas, and theorem assembly before filling proofs.
- **Draft-Sketch-Prove**: write a short informal draft, convert it into named subgoals, then prove or repair each subgoal.
- **Premise retrieval**: search theorem names and nearby lemmas before inventing a proof from scratch.
- **Global premise retrieval**: sketch the route, retrieve per-step candidates, filter them, then judge whether the bundle can support a complete assembly.
- **Compiler-guided repair**: when Lean or another checker fails, isolate the failing sublemma instead of rewriting the whole proof.
- **Counterexample-guided repair**: use a concrete counterexample or toy failure to infer the missing invariant or missing assumption.
- **Best-first route scheduling**: rank unresolved lemmas by plausibility, dependency value, and certificate availability.
- **Hardest-case-first**: try the boundary, degenerate, or most constrained case early; if it fails, the theorem likely needs repair.
- **Idea-map extraction**: when a paper or formalization is useful, extract the failure world, pattern guess if any, central object, proof kernel or central lemma, and verification hook, not just the final theorem.
- **Paper trick card**: save local reusable moves with source, problem shape, hidden assumptions, transplant step, verification hook, and failure mode.
- **Persistent memory**: record successful patterns, dead ends, and reusable lemmas so the next attempt starts with evidence.
- **Cost-aware route control**: treat failed attempts as data. If failures are repetitive and the proof state is not shrinking, switch action instead of spending another attempt on the same node.
- **Target-fidelity first**: when a source paper or model motivates the theorem, check target statements and node roles before proving. A formally valid lemma that proves the wrong role is wasted.
- **Dynamic leaf proving**: prove ready leaves on the theorem path first; postpone orphan lemmas and side machinery until they have downstream use.
- **Repair-radius decomposition**: prefer a graph where one false child invalidates a small connected region rather than the entire argument.

## Recent Method Patterns

Use these as importable proof-search mechanisms:

- **Formal Conjectures**: audit the statement before proof. Look for translation errors, implicit conventions, underspecified source claims, zero/boundary behavior, and wrong quantifier scope.
- **Discover-and-Prove**: if an answer or object is hidden, separate discovery from proof. Self-check the discovered answer on holdout cases before turning it into a theorem.
- **PatternBoost/FunSearch/AlphaEvolve**: use candidate evolution only when validity and scoring are executable. Keep structurally diverse elites and alternate global proposals with local improvement.
- **Self-supervised theorem discovery**: salvage reached intermediate theorems from failed searches, but promote only checked, general, hard-to-rederive lemmas that reduce future search.
- **QED/frontier audits**: verify the exact problem statement, citations, and novelty before claiming an open problem is solved. Keep the verifier independent from the proposal context.
- **OProver/APOLLO**: use tool/compiler feedback as a local repair signal. Preserve the skeleton, isolate the bad block, and retry only the failed lemma with compact feedback.
- **LEAP/Goedel-Architect**: after direct failure, create a DAG of lemmas with declared dependencies. Review acyclicity, parent sufficiency, and whether each child lemma is simpler than its parent; semantic review matters even when a sketch type-checks.
- **LeanSearch v2**: retrieve a global premise set through sketch-retrieve-reflect. Treat empty or insufficient retrieval as feedback to revise the proof sketch, not as permission to invent a theorem.
- **Prover Agent**: when the full route is invisible, prove special cases or auxiliary facts bottom-up and infer the strategy they suggest. Keep exploratory lemmas separate from required assembly nodes.
- **Delta Prover/Hilbert**: classify whether failure is sketch generation, decomposition, local solve, or assembly, and spend further compute only at the failed stage.
- **Cost-quality Lean agents**: after failed attempts, decide between continuing the node and restarting/re-decomposing by using proof-state delta, failure diversity, proof similarity, and attempt count.
- **LeanArchitect**: use blueprint metadata to separate statement text, proof text, dependency inference, status, and discussion/not-ready notes.
- **LeanMarathon**: stabilize target fidelity before proof discharge, then work from dynamic leaves upward. Keep source-aware repair, bounded edit scope, and low repair radius; do not use proof length as an escape condition.
- **AlphaProof Nexus**: keep a small population of sketches; use a reviewer to score decomposition quality, novelty, plausibility, and good-gap versus bad-gap.
- **MerLean-Prover/lean-collab**: separate planning, proving, and checking roles. A clean proof must still pass faithfulness to the original statement and mathematical-correctness checks.
- **STAR-PolyaMath**: keep a non-reasoning coordinator or ledger in charge of state. Use a persistent meta-strategy note for chronic failure patterns, and review each fragile step with accept/challenge/trace-back/re-plan verdicts.
- **Rethlas/Archon**: split informal route discovery from formal checking. Let retrieval and natural-language reasoning propose candidate lemmas, then ask the checking side to return precise missing obligations.
- **MA-LoT**: separate whole-proof generation from feedback repair. One pass may draft the route; another pass should only analyze tool or reviewer feedback and patch the failing block.
- **Ax-Prover**: use tool-equipped agents as artifact producers, not proof authorities. Trust the checker, counterexample, or retrieved theorem pattern over role confidence.
- **Generative verifier studies**: verbal judges may reward proof style rather than validity, and ensembles of similar judges need not help. Triangulate fragile steps with a genuinely different evidence channel.
- **Formal Conjectures**: test definitions with easy variants and boundary lemmas. A proof or disproof can reveal a translation, underspecification, or source error in the statement itself.

## Use In A Proof Project

1. Fill `PATTERN_SCAN.md` only with sources that change the next proof move.
2. Add retrieved theorem names or assumptions to `LEDGER.md`.
3. If a source suggests tool use, add the expected artifact to `TOOL_PLAN.md`.
4. If a source suggests a proof route, add it as Route A/B/C in `ATTACK_MATRIX.md`.
5. If the source only provides intuition, mark it as intuition and do not use it as a proof step.

## Query Starters

- DP/MDP: `Bellman inequality certificate`, `monotone optimal policy proof`, `submodular dynamic programming`, `threshold policy single crossing`.
- Mechanism/econ: `cyclic monotonicity proof`, `payment identity IC IR`, `envelope theorem mechanism design`, `finite type payment feasibility LP`.
- Learning/bandits: `uniform confidence event regret proof`, `elliptical potential lemma`, `self-normalized concentration`, `online convex optimization potential proof`.
- OR/optimization: `KKT sufficiency proof`, `primal dual certificate`, `exchange argument proof`, `subgradient optimality certificate`.
- Lower bounds: `two point testing lower bound`, `Fano Assouad proof`, `change of measure bandit lower bound`, `KL TV reduction`.
- Probabilistic method: `Lovasz Local Lemma bad events dependency graph`, `Moser Tardos resampling algorithmic local lemma`, `lopsided local lemma proof`.
- Formal/prover: `Lean formalization theorem name`, `mathlib lemma`, `Draft Sketch Prove`, `retrieval augmented theorem proving`, `compiler guided proof repair`.
- Recent proof agents: `STAR PolyaMath meta strategist challenge trace back replan`, `Goedel Architect blueprint refinement`, `LeanMarathon dynamic proof DAG`, `LeanArchitect blueprint metadata`, `cost quality Lean theorem prover routing`, `MerLean Prover recursive proof plan`, `Rethlas Archon informal formal proof`, `MA-LoT Lean feedback correction`, `Ax-Prover multi-agent Lean MCP`, `AlphaProof Nexus good gap bad gap`, `OProver feedback refinement`, `APOLLO proof repair`, `LEAP AND OR proof DAG`.

## Stop Rule

Stop scanning when one of these happens:

- a concrete theorem pattern or known lemma is found;
- a source identifies a missing assumption or counterexample family;
- two independent sources point to the same proof architecture;
- the scan produces no new route within the agreed budget.
- the current proof is small and one close source gives either a route or a clear mismatch.

Do not continue scanning after finding a route with a clear verification hook. Switch back to proving or falsifying.
