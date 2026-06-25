---
name: theory-proof-workbench
description: "Use for hard theoretical proofs, proof debugging, failed proof recovery, and judgment-guided proof projects in OR/MS, mechanism design, econ theory, learning theory, bandits, online learning, optimization, games, regret, IC/IR, and lower bounds."
---

# Theory Proof Workbench

Use this skill when a proof is nontrivial, has failed before, or belongs to OR/MS, mechanism design, economic theory, learning theory, bandits, online learning, optimization, games, or lower bounds.

This is a proof-control workflow, not a theorem encyclopedia. The goal is to stop restarting from scratch and force proof attempts through classification, assumption audit, counterexample search, lemma decomposition, verification gates, and persistent failure notes.

For proof exposition, rewriting, polishing, or LaTeXing a proof whose core argument already exists, use `math-proof-writing` instead. Use this workbench only when the proof itself is missing, blocked, or suspect.

If the request mixes proof discovery with proof writing, run the proof task router from `research-tools` before starting a proof project.

## Judgment First

The scripts create memory and guardrails; they do not decide the mathematics. Before each new route, decide:

- whether the last result made the claim more plausible, less plausible, refuted, or unchanged;
- whether the next step should prove, falsify, retrieve a known theorem, tool-check a lemma, or repair the statement;
- whether the route has a proof kernel: the smallest lemma, certificate, or counterexample barrier that would decide the route;
- whether small cases suggest a formula, invariant, construction, normal form, or tight example worth testing;
- whether the next move reduces the proof state, rather than only rewriting the same missing lemma;
- whether a proposed assumption repair changes the economic, OR/MS, or learning-theory meaning enough to ask the user;
- whether the obstruction needs the user's domain intuition before spending another heavy search cycle;
- whether to stop with `still open` rather than produce a polished but unsupported proof.

## Progress Contract

For a hard or previously failed proof, do not count a rewrite as progress. A new attempt is useful only if it adds one of these:

- a proved or refuted kernel lemma;
- a counterexample, boundary case, or missing assumption;
- a checked certificate, algebra identity, finite model, optimization/SMT result, or local formalization;
- a different central object, invariant, potential, hard instance, dual, envelope, coupling, or Bellman gap;
- a retrieved theorem pattern or paper trick with assumptions and a verification hook;
- a theorem repair that changes the exact statement honestly.

Before retrying the same obstruction, name the attempt signature: route family, central object, target kernel, failure witness, and expected new evidence. Changing notation, adding cosmetic cases, or restating a stronger missing lemma is not progress.

For hard proofs, use divergence before convergence unless a direct theorem already solves the claim: try one proof route, one falsification route, and one orthogonal idea source such as small-case pattern mining, a tool certificate, or a nearby paper pattern. Then choose the route with the strongest failure-world control and verification hook.

When a route stalls, optimize for decision value, not activity. The next move should decide a kernel, refute a small claim, expose a missing assumption, import a usable theorem pattern, or produce a checkable certificate. If it cannot do one of these, do not spend a long prose attempt on it.

## Recent Proof-Agent Lessons

Use these as light control rules, not a mandatory checklist.

- **Statement-fidelity first**: for formal, model-heavy, or literature-derived claims, check whether definitions, quantifiers, boundary cases, and implicit conventions match the intended theorem before proving.
- **Hard-mode discovery gate**: if the theorem needs an unknown construction, threshold, coefficient, potential, hard instance, or answer, first discover and self-check that object on small or symbolic cases; then prove it.
- **Compact repair state**: after a failed local attempt, carry only the exact statement, retrieved premises/patterns, previous attempt signature, and previous feedback into the next repair. Keep full history in the ledger, not in the active proof context.
- **Good gap / bad gap reviewer**: a good gap is smaller than the parent, routine under clear assumptions, and has a verification hook. A bad gap restates the theorem, hides the core insight, is circular, or has no falsification path.
- **Localize before regenerating**: preserve the proof skeleton when it is structurally right; isolate the failed block as a named lemma, repair or split that block, then recombine.
- **Small route population**: for hard proofs, maintain 2-4 route candidates and score them by failure-world control, novelty, decomposition quality, and certificate availability. Do not run a large search unless the user asks.
- **Cost-quality routing**: after two failed local attempts, use failed-state signals to decide whether to continue, locally repair, re-decompose, retrieve a premise/paper pattern, or stop/report.
- **Dynamic leaf discipline**: in a lemma graph, prove ready leaves whose dependencies are settled and that feed the current theorem path. Postpone orphan or unused lemmas.
- **AND/OR bottleneck discipline**: treat alternative routes as OR nodes and lemma dependencies as AND nodes; attack the lowest-confidence required child before expanding more prose.
- **State/action dedupe**: if two attempted routes have the same goal, context, central object, and failure witness, treat them as the same proof state even if notation differs.
- **Formal-status honesty**: Lean compilation, API output, or local tool success is not enough if the main theorem still has `sorry`, unresolved obligations, or unverified global bookkeeping.
- **Multi-agent only with a dispatch contract**: use actual parallel agents only when the user explicitly asks or approves; each role must have a disjoint artifact, stop rule, and no-overlap instruction.
- **Control separate from reasoning**: for hard projects, let the coordinator/ledger own state, stop rules, trace-back, and route choice. Do not let the same proof attempt both argue and certify itself.
- **Budgeted challenge-step-replan loop**: review fragile steps through a goal gate and a logic gate, then choose accept, challenge, trace back to an earlier step, re-decompose, or re-plan. Put a small cap on challenge rounds and replans before starting.
- **Tool-use brake**: if tool calls, code, or algebra loops consume budget without shrinking the proof state, switch to pure reasoning on the accumulated artifact, retrieval, theorem repair, or stop/report.
- **Structured forfeit**: when a route runs out of budget, write diagnosis, forensic analysis, and suggested fix before the next attempt.

## Use Gate

Do not blindly escalate to the full workbench. Pick the lightest useful mode.

- **Direct mode**: if a named theorem, certificate, or short contradiction solves the claim, prove directly and run verification gates.
- **Micro pattern check**: if the route is not obvious but the proof is still small, look for one nearby theorem family, playbook pattern, prior ledger, or paper trick before inventing a new central lemma. Stop once it changes the next proof move or clearly does not apply.
- **Light idea mode**: if the route is unclear but no project is needed, run `plan_idea.py` and use only the relevant central-object candidates.
- **Project mode**: start a proof project only for hard, repeated, multi-lemma, tool-assisted, or literature-dependent proofs.
- **Recovery mode**: if the same proof has failed before, read the existing ledger or create one before trying another route.
- **Multi-agent mode**: use only for hard, stuck, or broad proof projects after explicit user approval. Keep roles few and disjoint: planner, falsifier, retriever, formalizer/tool-checker, and reviewer.

Use references and tools only when they change the next proof move. Do not load every playbook, scan papers, or start a project just because the topic is theoretical.

## Execution Spine

Use this order unless the theorem is already solved or refuted:

1. Exact statement and statement-fidelity check.
2. Direct-solve or micro pattern check.
3. Falsification and boundary stress test.
4. Idea/kernel discovery only if the route is unclear.
5. Small route portfolio for hard or failed proofs.
6. Blueprint lemma graph and ready-leaf local proof.
7. Route decision after repeated local failure.
8. Assembly, adversarial review, and final proof status.

## Project Start

For a hard or previously failed proof, start a proof project only when light modes are insufficient:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/start_proof.py --title "SHORT PROOF NAME" --claim "CLAIM"
```

This creates `TRIAGE.md`, `WORKSTREAMS.md`, `IDEA_MAP.md`, `ATTACK_MATRIX.md`, `LEMMA_QUEUE.md`, `PATTERN_SCAN.md`, `TOOL_PLAN.md`, `LEDGER.md`, `ESCALATION.md`, `counterexamples.md`, `strategy.md`, `state.md`, `tool_checks/`, `trick_cards/`, and supporting folders. Use `ATTACK_MATRIX.md` to force one proof route and one falsification route before drafting a final proof. Use `LEMMA_QUEUE.md` as a blueprint DAG: named definitions/lemmas, statement and proof dependencies, node statuses, used-node path, gap grades, failure diagnoses, and refinement notes.

When returning to an existing proof project, diagnose the next move first:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

For a lightweight idea pass without creating a project, run:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

If small cases give a numeric sequence and the route needs a guessed formula, potential, threshold, or coefficient pattern, mine the sequence before promoting the guess:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## Core Loop

1. Restate the claim with variables, domains, quantifiers, and all assumptions.
Do not silently change the theorem statement, assumptions, or conclusion. If the proof needs a different statement, mark it as theorem repair or ask the user when the modeling meaning changes.
2. Run the statement-fidelity and pre-solve gates: decide whether the claim is the intended theorem, then whether an obvious direct theorem, certificate, or one-page proof applies. If yes, prove directly and still pass verification gates. If no, do a micro pattern check or use the light idea pass. Retrieve nearby proof patterns from prior papers, local drafts, ledgers, or literature only when the central object or central lemma is unclear.
3. Classify the proof target using [references/proof-router.md](references/proof-router.md) and the state machine in [references/proof-state-machine.md](references/proof-state-machine.md).
For hard, research-level, or twice-failed proofs, also apply [references/research-backed-proof-loop.md](references/research-backed-proof-loop.md): prior-result audit, Draft-Sketch-Prove, premise retrieval, tool-guided repair, and progress-budget stop rules.
When the proof idea is unclear, optionally apply [references/proof-idea-generator.md](references/proof-idea-generator.md) before the route portfolio. This is not mandatory for routine proofs; use it to find the failure world, central object, proof kernel, pattern guess, central lemma, and verification hook.
For unfamiliar theorem families, literature-dependent proofs, or user-requested outside learning, apply [references/external-proof-pattern-scan.md](references/external-proof-pattern-scan.md): extract proof architectures from papers, formalization projects, and proof-agent skills before inventing another route.
When the route needs computation, CAS, SMT, optimization solvers, or Lean, apply [references/tool-assisted-proof-patterns.md](references/tool-assisted-proof-patterns.md) before running broad tool queries.
If a route fails twice or the same obstruction repeats, use [references/proof-escalation-protocol.md](references/proof-escalation-protocol.md) before another prose proof attempt.
4. For hard proof projects, use `WORKSTREAMS.md` to define approved goals and active workstream cards. Before heavy execution, each card should inspect how nearby papers, appendices, prior ledgers, theorem families, or analogous models solve similar problems, unless there is a written skip reason. Keep this local-first and bounded: one to three strong sources or patterns are enough before trying the next proof move. Use actual parallel agents only when the user explicitly asks for delegation.
If the user explicitly asks for multi-agent work, assign disjoint roles and artifacts before spawning agents. Do not let two agents attack the same missing lemma in the same way; one should falsify, one retrieve, one formalize/tool-check, one review, or one plan.
5. Choose proof routes with [references/strategy-scheduler.md](references/strategy-scheduler.md); run at least two genuinely different routes for hard or previously failed proofs. Different means a different central object, theorem family, certificate type, failure world, or evidence source.
6. Before proving, try to break the claim: edge cases, missing compactness/convexity/continuity, finite counterexamples, numerical examples, and relaxed assumptions.
7. If the route is still unclear, run the optional idea pass: failure world -> small-case pattern guess -> central object -> proof kernel -> central lemma -> verification hook. Use `pattern_miner.py` only when the small cases produce a useful exact sequence. If the same obstruction remains, do bottleneck surgery: shrink to the smallest local lemma, flip to the negation, try a certificate or alternate representation, then retrieve or repair before drafting again.
8. Build a blueprint-style lemma graph: label each needed definition/lemma/theorem node, declare statement dependencies and proof dependencies, and mark status as missing, proved, checked, false/negated, or conditional. For repeated attempts, record the attempt fingerprint and expected new evidence in `WORKSTREAMS.md` before trying a variant. When a node fails, diagnose it as `STATEMENT_WRONG` or `PROOF_TOO_HARD`, grade the gap as good or bad, and keep a compact repair state; preserve solved nodes and refine only the failed subgraph when possible.
For hard formalizable proofs, make the graph AND/OR-aware: OR branches are alternative routes or constructions, AND branches are required sublemmas. Merge equivalent states and actions before retrying. Preserve proved lemmas, revise only unproved or false nodes, and attack the bottleneck child first.
Before proving a repeated or expensive node, run a lightweight route decision: continue current node, locally repair it, re-decompose the subgraph, retrieve a premise/paper pattern, or stop/report. Prefer ready leaves whose dependencies are settled and that feed the current assembly path. Do not prove unused lemmas that are not on that path.
9. Work one proof move at a time when a kernel is fragile: name the current subgoal, propose one move, predict the new subgoal, check it by theorem match, algebra, toy case, tool, or reviewer pass, then keep, repair, or discard it based on proof-state delta. For multi-step plans, tag each step as tool-verified, easy-to-check, or hard-to-check; run a goal gate and a logic gate before accepting it. If two moves leave the same obstruction unchanged, stop proving in prose and switch to retrieval, tools, counterexample search, theorem repair, or user steering.
10. Read only the relevant branch playbook. If unsure, run:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/select_playbook.py "CLAIM OR TOPIC"
```

Branch playbooks:

- Optimization and OR/MS: [references/optimization-or-playbook.md](references/optimization-or-playbook.md).
- Dynamic programming and MDPs: [references/dp-proof-playbook.md](references/dp-proof-playbook.md).
- Mechanism design: [references/mechanism-design-playbook.md](references/mechanism-design-playbook.md).
- Games and matching: [references/games-matching-playbook.md](references/games-matching-playbook.md).
- Learning theory: [references/learning-theory-playbook.md](references/learning-theory-playbook.md).
- Bandits and online learning: [references/bandits-oco-playbook.md](references/bandits-oco-playbook.md).
- Lower bounds: [references/lower-bounds-playbook.md](references/lower-bounds-playbook.md).
11. If stuck, name the obstruction using [references/obstruction-taxonomy.md](references/obstruction-taxonomy.md) before changing routes. If the block is about model meaning, promising structure, or domain taste, surface a short steering question to the user. If the obstruction repeats, escalate through counterexample search, tools, retrieval, local formalization, or theorem repair with [references/proof-escalation-protocol.md](references/proof-escalation-protocol.md).
12. Apply the proof-status and review gates in [references/verification-gate.md](references/verification-gate.md).
13. Use `math-tools` for local checks: Wolfram for algebra/conditions, Python/CVXPy/OR-Tools/Z3 for finite or numeric checks, Sage for discrete structures, Lean for local formalizable lemmas. For proof-critical checks, first decide the expected artifact: counterexample, condition, exact identity, KKT/dual certificate, SMT model/unsat result, or Lean lemma.
If using Lean or an external formal prover/API, audit the final artifact for `sorry`, admitted axioms, incomplete declarations, and whether verified helper lemmas actually assemble into the original theorem.
14. Write the proof in layers: intuition, formal lemma statements, proof of each lemma, final assembly.

## Failure Recovery

If a proof attempt stalls, do not start over. Create or update a proof ledger. The ledger must record:

- the exact claim and assumptions,
- failed proof routes and where they broke,
- failed proof states that remained unchanged after a move,
- blocked retries and why they had no new evidence,
- route decisions after repeated local failures: continue, repair, re-decompose, retrieve, or stop, with reason,
- step-level verdicts for fragile plans: accept, challenge, trace-back, re-decompose, re-plan, or stop,
- named obstruction types,
- attempted counterexamples,
- proved lemmas,
- missing lemmas,
- the next most plausible theorem pattern,
- compact repair state for the current bottleneck: statement, retrieved premise/pattern, previous attempt signature, previous feedback, and next legal edit.

When the user asks again about the same proof, read the ledger first and continue from it.

If two routes fail, or if the ledger shows the same obstruction twice, stop trying the same proof style. Open [references/proof-escalation-protocol.md](references/proof-escalation-protocol.md), then run the next bounded external method: finite counterexample search, symbolic simplification, LP/SMT certificate, literature/premise retrieval, local Lean formalization, or theorem repair.

For repeated attempts, check the attempt fingerprint index in `WORKSTREAMS.md` before proposing another route or construction. Do not retry the same signature unless there is a new assumption, central object, invariant, certificate, verified trick, counterexample repair, theorem repair, or external theorem pattern that directly addresses the previous failed witness.

For a hard proof where direct mode and the light idea pass are insufficient, start a project:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/start_proof.py --title "SHORT PROOF NAME" --claim "CLAIM"
```

For an existing proof project, use the proof doctor before trying another proof route:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

If a new attempt may repeat an old route or construction and the match is ambiguous, compare it against recorded fingerprints:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/check_attempt.py path/to/proof_project --route-family "ROUTE" --central-object "OBJECT" --target-lemma "LEMMA" --failure-witness "WITNESS"
```

To create a standalone ledger, run:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/new_ledger.py "SHORT PROOF NAME" --claim "CLAIM"
```

Before presenting a final proof from a ledger, audit missing gates:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

When a missing lemma becomes reusable, promote it to a lemma card:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/new_lemma_card.py "LEMMA NAME" --statement "STATEMENT"
```

When a paper trick becomes reusable outside a project, save it as a standalone trick card:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/new_trick_card.py "TRICK NAME" --source "PAPER/APPENDIX/LEMMA" --shape "PROBLEM SHAPE" --obstruction "OBSTRUCTION SOLVED"
```

Prefer saving into a proof project:

```bash
codex-math-python /Users/mingfeijiang/.codex/skills/theory-proof-workbench/scripts/new_trick_card.py "TRICK NAME" --project path/to/proof_project --source "PAPER/APPENDIX/LEMMA" --shape "PROBLEM SHAPE" --obstruction "OBSTRUCTION SOLVED"
```

Keep trick cards local to the proof project first. Standalone cards are for cross-project tricks only. Promote a trick to a global reference only after it has helped on a real proof or clearly identified a false route.

## Output Contract

For hard proofs, keep the visible answer compact. Use the ledger and gates internally, but report only what the user needs to trust the result:

- claim status and verification status,
- essential assumptions,
- proof pattern and final proof, or the exact obstruction if still open,
- missing lemma, counterexample, tool artifact, external pattern, or workstream result only when it materially changes the conclusion,
- what genuinely changed since the last failed attempt, when the proof has been tried before,
- next bounded move if the proof is still blocked.

Do not present a polished proof if the key lemma is only guessed. Mark it as a missing lemma.
