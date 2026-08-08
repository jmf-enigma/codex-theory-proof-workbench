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

## Autonomous Capability Radar

Do not wait for the user to name a prover, database, skill, or paper. Trigger one current-method scan only when the failure stage exposes a missing artifact or independent evidence channel.

1. Name the missing output, such as a construction, counterexample, premise bundle, formal declaration, strict verifier, or assembly certificate.
2. Derive the query from that output and the failure stage, not from a product name. Check local tools and prior packets first, then Papers With Lean, arXiv, Scholar, and official repositories or documentation.
3. Reject a candidate that only repackages an existing channel. Admit it only when a primary source and inspectable implementation support a non-duplicated capability, the privacy boundary fits, and one bounded live probe succeeds.
4. Import the mechanism, not its marketing claim. Record the produced artifact, assumptions, verifier boundary, cost, failure mode, and exact point where it changes the route.
5. Stop after one admitted candidate or two clear mismatches. Return to proving; capability browsing is not progress by itself.

Useful but non-default candidates:

| Candidate | Distinct value | Admission caution |
| --- | --- | --- |
| [Papers With Lean](https://paperswithlean.com/) | Current formal-mathematics radar | Discovery only; open the primary paper and code |
| [OpenProver](https://arxiv.org/abs/2607.09217) | Interactive Planner-Worker-Verifier harness with compact active state | Separate system; borrow its control ideas unless a full Lean harness is needed |
| [OpenGauss](https://github.com/math-inc/OpenGauss) | Managed project, swarm, checkpoint, and reattachment interface | Heavy overlap with the current Codex and Lean stack |
| [AXLE](https://arxiv.org/abs/2606.26442) | Remote Lean extraction, isolated solving, merging, and stricter verification | Source sharing and trust limits require explicit approval |
| [LeanExplore](https://arxiv.org/abs/2506.11085) | Package-level formal declaration search | Add only for a demonstrated local search coverage gap |
| [TheoremDB](https://theoremdb.org/how-it-works/) | Public shared orientation and evidence-graded result memory | Writes enter a public research record |
| [mathlas](https://github.com/Archerkattri/mathlas) | Local bundle for retrieval, numerical discovery, and Lean checks | Audit overlap, resource cost, verifier strength, and author evaluations first |

Do not depend on a documented graph endpoint or service until a fresh live probe succeeds. Remote source or query sharing needs explicit approval.

## Statement Retrieval

Use statement retrieval when the missing artifact is a theorem, construction, example, counterexample, proof trick, or obstruction. It searches individual mathematical statements rather than only titles and abstracts. It is not a proof engine, a frontier classifier, or a Mathlib premise checker.

| Service | Prefer when | Main limitation |
| --- | --- | --- |
| Matlas | Mature results in curated published papers or textbooks | Not a recency or complete-coverage check |
| TheoremSearch | Broad arXiv and open-source theorem coverage, with source/type/year filters | Mostly preprints and open sources; query text and filters are logged |
| LeanSearch/Loogle/LeanFinder | The target is a formal declaration or current Lean goal | Searches formal libraries, not informal papers |

Run one service only after identifying the local target and intent:

```bash
python3 scripts/statement_search.py \
  "A COMPLETE, ABSTRACTED MATHEMATICAL STATEMENT" \
  --service matlas --intent theorem --remote-ok --project path/to/project
```

Change to `--service theoremsearch` for arXiv/open-source coverage; optional filters include `--tag math.OC`, `--source arXiv`, `--result-type Lemma`, and `--year-range MIN MAX`. Both services are remote. TheoremSearch publishes that it logs query text and filters; no Matlas query-retention policy was verified. For unpublished or sensitive work, remove private notation, constants, model names, data, and surrounding claims. If abstraction destroys the mathematics, do not send it.

Use this bounded protocol:

1. Search local references, prior packets, and the failed-state ledger first.
2. Phrase the query as a complete desired result or obstruction, not a keyword list. For construction problems, include the properties the object must jointly satisfy.
3. Start with the corpus that fits the need. Use the other service only when the first has a clear coverage mismatch, not merely weak top ranks.
4. Use a reformulation ladder rather than repeated paraphrases: original claim, then the smallest bridge lemma, existence statement, dual form, or failure-world obstruction exposed by the current proof state.
5. Request the default ten results. Across both services, allow at most one materially different reformulation before returning to mathematics.
6. Keep at most three candidates for source verification. Treat every packet as `retrieved-unverified`; rank and similarity are not applicability evidence, and `proof_effect=none` is mandatory.
7. Verify authoritative metadata, retrieve a lawful full text, expand definitions, map assumptions, read the cited proof, and extract the transferable move plus the remaining bridge lemma.
8. For every extra assumption, record what job it performs, exactly where the proof fails without it, and whether that failure suggests a counterexample, theorem repair, or new construction.
9. Before another remote query, make one retrieval-off move: independently derive a bridge, test a boundary case, seek a counterexample, or reject the candidate by assumption mismatch. Search again only if this changes the query target.
10. Only a source-verified theorem or proof-derived move may enter `PATTERN_SCAN.md`, a trick card, or a proof step. Preserve the packet as discovery provenance.

For recent work, cited-by evidence, or a known/open/new claim, use Scholar, arXiv, OpenAlex, and [full-text-frontier-evidence.md](full-text-frontier-evidence.md). On timeout, service error, or an exhausted reformulation, record `retrieval-unavailable` or `no-useful-candidate` and continue locally.

The services are described in the [Matlas paper](https://arxiv.org/abs/2604.17484) and [TheoremSearch paper](https://arxiv.org/abs/2602.05216). Rethlas used a preliminary arXiv endpoint that its current paper says will be deprecated; do not copy that endpoint. Its useful lesson is the broad-search, theorem-reformulation, focused-search cycle, followed by independent construction and verification. See the [Rethlas report](https://arxiv.org/abs/2604.03789) and [source](https://github.com/frenzymath/Rethlas).

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
- extra-hypothesis role: where each added assumption enters and what fails without it.
- applicability contract: exact needs, guaranteed output, and mismatch traps.
- retrieval-off check: the independent derivation, falsification, or mismatch test run after retrieval.
- independent replay: current-problem check plus a held-out case or mechanism-distinct route when promotion is proposed.
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
- **LeanProgress**: use proof history and remaining-obligation structure to schedule search. A state is smaller only if a required obligation vanishes, the worst gap weakens, or an opaque gap becomes a checkable leaf.
- **Learning to Disprove**: remove or weaken one high-leverage hypothesis and seek an explicit formal or finite witness. Use the first point where the original assumption blocks that witness to diagnose necessity; do not mutate every assumption at once.
- **AXLE**: when a coherent Lean skeleton has a failing block, mechanically extract the block with its exact context, solve it separately, merge by dependencies, and strictly verify the frozen declaration. Remote success does not bypass statement, assumption, assembly, or trust audits.
- **mathlas applicability scaffold**: describe a retrieved move by `needs`, `guarantees`, and `mismatch traps`, then attach source and replay evidence before promotion. This scaffold is useful even without installing the package.
- **Prover Agent**: when the full route is invisible, prove special cases or auxiliary facts bottom-up and infer the strategy they suggest. Keep exploratory lemmas separate from required assembly nodes.
- **Delta Prover/Hilbert**: classify whether failure is sketch generation, decomposition, local solve, or assembly, and spend further compute only at the failed stage.
- **Cost-quality Lean agents**: after failed attempts, decide between continuing the node and restarting/re-decomposing by using proof-state delta, failure diversity, proof similarity, and attempt count.
- **LeanArchitect**: use blueprint metadata to separate statement text, proof text, dependency inference, status, and discussion/not-ready notes.
- **LeanMarathon**: stabilize target fidelity before proof discharge, then work from dynamic leaves upward. Keep source-aware repair, bounded edit scope, and low repair radius; do not use proof length as an escape condition.
- **AlphaProof Nexus**: start with a basic Lean-feedback loop. Its population and heuristic rater can schedule diverse sketches after that loop stalls, but the rater is not an acceptance channel and the paper's simple-agent comparison covered selected successful problems.
- **MerLean-Prover/lean-collab**: separate planning, proving, and checking roles. A clean proof must still pass faithfulness to the original statement and mathematical-correctness checks.
- **STAR-PolyaMath**: keep a non-reasoning coordinator or ledger in charge of state. Use a persistent meta-strategy note for chronic failure patterns, and review each fragile step with accept/challenge/trace-back/re-plan verdicts.
- **Rethlas/Archon**: use broad search to reformulate the target, focused statement search to expose a construction, and retrieval-off reasoning to prove the bridge. Diagnose why partial-result assumptions are needed, record exact failed mechanisms, and let a formal checker rather than Rethlas's model verifier control any machine-checked status.
- **MA-LoT**: separate whole-proof generation from feedback repair. One pass may draft the route; another pass should only analyze tool or reviewer feedback and patch the failing block.
- **Ax-Prover**: use tool-equipped agents as artifact producers, not proof authorities. Trust the checker, counterexample, or retrieved theorem pattern over role confidence.
- **Generative verifier studies**: verbal judges may reward proof style rather than validity, and ensembles of similar judges need not help. Triangulate fragile steps with a genuinely different evidence channel.
- **APRIL**: preserve a diagnostic-grounded repair tuple and replay the minimal patch; do not substitute an LLM explanation for the compiler output.
- **Beyond the Frontier**: when heuristic route scores are noisy, keep a bounded historical state pool and allow one under-ranked, mechanism-distinct state a cheap revisit. Treat this as a scheduling analogy, not proof evidence.
- **$k$-server-bench**: turn potential or certificate discovery into counterexample-guided search. Cache hard violations, early-stop weak candidates, and distinguish a finite one-sided evaluator from a global proof.
- **QEDBench/Axiom-Audited Lean**: an LLM judge can be systematically lenient, while a compiling proof can hide an unexpected trust base. Require problem-derived obligations, heterogeneous evidence, axiom-footprint regression, and explicit external assumptions.
- **TacMiner**: identify reusable moves by dependency structure and collapsible input-output boundaries rather than adjacent text. TacMiner studies Rocq tactic fragments; keeping an informal trick local until a second-route or held-out replay succeeds is this workbench's additional safeguard.
- **SorryDB/Lean Finder**: for Lean-workflow evaluation, use pinned real project obligations and held-out or later snapshots in addition to synthetic smoke tests; for retrieval, model user intent rather than only theorem-statement similarity. This is a workbench design inference, not a general theorem about mathematical evaluation.
- **Formal Conjectures/hypothesis-disciplined formalization/AI4SLT**: test definitions with easy variants, trace every added assumption or definition to its source, and freeze probability semantics before formal proof. A checked artifact can still encode a translation, underspecification, or source error.
- **Sorries Are Not the Hard Part**: when the goal is reusable formal library code, review definitions, theorem generality, namespaces, and API surface after kernel correctness. Do not impose this design review on a one-off local certificate.

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
