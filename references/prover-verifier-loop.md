# Prover-Verifier Loop

Use this when a proof attempt needs step-level checking, adversarial review, Lean/tool feedback, or repeated repair. Keep it light: the loop is a control contract, not a substitute for mathematical judgment.

## Map

- Activation: use only when a local move is fragile, repeated, challenged, or tool/Lean feedback is involved.
- Role contract: separate proposal, verification, coordination, and memory.
- Move protocol: make one local move, verify declared goal and logic, then record proof-state delta.
- Diagnostic repair: preserve exact checker feedback, diagnose locally, make the smallest patch, and replay.
- Failure localization: identify the first invalid step, preserve the verified prefix, and salvage independent artifacts.
- Repair protocol: preserve good skeletons and revise only the failed subgraph.
- Literature lessons: import checkability, blueprints, correction, trace-back, and retrieval as methods.
- Stop rule: stop or reroute when the loop produces no new artifact.

## Activation

Use this loop when one of these holds:

- the same local lemma or construction has failed once already;
- a proof step is hard-to-check, algebraically delicate, boundary-sensitive, or assumption-sensitive;
- tool, Lean, or reviewer feedback rejected a block;
- a plausible proof skeleton exists but one block is suspect;
- the verifier must distinguish a true local step from a plausible false one.

Skip it for routine direct proofs, standard theorem applications with matched assumptions, and steps that already have a short explicit derivation.

## Role Contract

- **Prover** proposes one local move: lemma, construction, inequality, reduction, certificate, counterexample attempt, or proof-skeleton edit.
- **Verifier** is read-only by default. It checks the proposed move, attacks it, and returns a verdict; it should not write a competing full proof unless explicitly assigned a proof role.
- **Coordinator** chooses accept, challenge, trace back, re-decompose, retrieve, tool-check, statement-repair, or stop.
- **Memory** records accepted artifacts, failed signatures, repaired assumptions, and forbidden repeats.

Use actual multi-agent parallelism only with explicit user approval. Serial role switching inside one agent is enough for most proof work.

For a complete proof candidate produced after earlier failures, or a candidate whose global assembly is difficult to inspect, use `scripts/run_referee.py`. It prepares a fresh, ephemeral, read-only Codex context containing the exact claim, acceptance contract, candidate proof, and only the selected reference excerpts. Inspect it first with `--prepare-only`; do not give the referee the generator ledger or current favorite route. Running the packet through another model requires an environment that permits the call and explicit user approval to share the selected packet. This reduces anchoring and prompt carryover, but it does not provide filesystem isolation, model independence, or formal correctness. A same-model verdict remains review evidence.

A nested Codex CLI may initially fail inside the parent workspace sandbox because it cannot write its state database or reach the model service. Preserve that failed verification record. Use ordinary sandbox escalation only when the host identifies a local permission or network restriction and sharing is approved. If policy rejects transferring the packet, or no independent pass is available, do not work around it. Record `fresh-context-unavailable`, run a local adversarial audit plus exact artifact replay, and cap the result at `human-proof` or `tool-checked` rather than `fresh-context-reviewed`. Never replace this with `--dangerously-bypass-approvals-and-sandbox`.

## One-Move Protocol

Before the move, write:

- current subgoal:
- proposed move:
- expected new subgoal or artifact:
- declared dependencies:
- parent step and last verified step:
- verification tag: tool-verified / easy-to-check / hard-to-check
- attempt signature: route family, central object, target lemma, failure witness

Verifier checks:

- **Goal gate**: did the move prove the declared subgoal, not just a nearby true claim?
- **Logic gate**: is each inference valid under the stated assumptions?
- **Delta gate**: is the remaining proof state smaller, refuted, or otherwise more decided?
- **Soundness probe**: can a plausible sneaky version of the same move hide a counterexample, boundary failure, missing assumption, or circular step?
- **Structure consistency**: if a proof sketch promised subgoals, does the final proof use them or explicitly retire them?
- **Failure-stage check**: is the defect in strategy, decomposition, premise retrieval, local proof, assembly, fidelity, or formal-library coverage?

Use the cheapest decisive verifier first:

1. statement, type, domain, dimension, and assumption check;
2. negation, boundary case, toy instance, or adversarial example;
3. exact algebra, solver certificate, numerical interval, or premise match;
4. local Lean/formal check when the statement is stable;
5. independent assembly review.

When a check fails, return the earliest failing step and a witness. Do not critique later deductions as if they were independent failures.

For checker-guided repair, record one tuple before retrying:

- runtime marker `feedback_kind: checker` and the pinned checker backend;
- failed proof or artifact;
- exact diagnostic and local goal/state, preserved verbatim;
- diagnostic site and inferred root cause, kept distinct because the reported location may be downstream of the actual defect;
- failure class: local tactic/theorem mismatch, semantic line/multiline defect, or decomposition/assembly defect;
- compact diagnosis grounded only in that feedback and the declared dependencies;
- smallest proposed repair;
- replay result from the same pinned checker.

Do not silently turn a compiler message into a broader mathematical diagnosis. For a local tactic or theorem mismatch, make the smallest patch and replay. For a semantic or assembly failure, allow one minimal repair; if the state does not shrink, return to the statement or decomposition instead of editing the reported line repeatedly. A natural-language explanation may route the next move, but only replay changes proof status.

Do not treat repeated verbal approval as mathematical evidence. Use a second verifier only when it brings a different channel, such as counterexample search, source comparison, exact algebra, solver certificate, formal checking, or conditional assembly. Several similar LLM judges can share the same style bias and unsupported assumption. A negative model verdict must expose a concrete first error or witness before it can invalidate an otherwise supported step.

The referee controller accepts `correct` only when claim fidelity and assumption coverage pass, `failure_kind` is `none`, the first-error field is empty, and both error lists are empty. A missing cited premise, source excerpt, or tool certificate is `missing-packet-evidence` and therefore `uncertain`, not a visible mathematical refutation. Malformed or contradictory output is also downgraded to `uncertain`; timeouts and nonzero exits are preserved as verification records rather than silently retried. `proof_doctor.py` consumes the latest first error and passed computation claims so packet repair takes precedence over restarting proof search.

Allowed verdicts:

- `accept`: move proves the subgoal or produces the promised artifact.
- `challenge`: local fix likely works; Prover may revise within the same subgoal.
- `trace-back`: the failure came from an earlier accepted step; name the earliest suspect ancestor.
- `re-decompose`: the target lemma is too large or hides multiple ideas.
- `retrieve`: a known theorem/paper lemma/library premise is likely missing.
- `tool-check`: Wolfram, Python, Z3, CVXPy, Sage, or Lean can decide the kernel.
- `statement-repair`: the statement is false, underspecified, or has wrong quantifiers/assumptions.
- `stop-report`: no positive-decision move remains within budget.

## Repair Protocol

- Preserve a coherent skeleton. Replace the failing block with a named local lemma rather than rewriting the whole proof.
- Freeze the verified prefix. Record which earlier steps and helper lemmas remain valid, then invalidate only the first failing node and its dependents.
- Classify every failed node as `STATEMENT_WRONG`, `PROOF_TOO_HARD`, `TOOL_GAP`, `RETRIEVAL_GAP`, or `ASSEMBLY_GAP`.
- If `STATEMENT_WRONG`, weaken conclusion, strengthen assumptions, fix quantifiers/domains, or drop the node and re-route dependents.
- If `PROOF_TOO_HARD`, split into helper lemmas that each need at most one or two new ideas beyond their parents.
- If a counterexample or negated sublemma is found, keep it as a diagnostic artifact and revise only affected downstream nodes.
- If tool feedback is used, keep the exact artifact: counterexample, condition, unsat certificate, algebra identity, optimizer/KKT certificate, or Lean error/goal.
- Keep diagnosis separate from diagnostic. If replay fails, preserve the new exact output and repair from the first changed error rather than from the old explanation.
- An incomplete proof may still yield `partial-verified` artifacts. Promote only steps whose dependencies were checked independently of the failed suffix.
- If the failure stage is not local proof, do not spend another local-repair round. Route decomposition failures to the blueprint, retrieval failures to a premise bundle search, assembly failures to a conditional parent proof, fidelity failures to the statement fence, and library-coverage failures to prerequisite inventory.
- After two failed repairs on the same node, use route decision: continue only with a new premise, representation, invariant, certificate, counterexample repair, or theorem pattern.

## Literature Lessons To Apply

- **PVG/checkability**: optimize proofs for being easy to check, not just for reaching the right conclusion. Run a sneaky-proof pass that tries to make a false local step look plausible.
- **Draft-Sketch-Prove**: treat informal proofs as scaffolds. Convert them into named subgoals; final proof must close the gaps independently.
- **APOLLO/MA-LoT**: separate whole-proof drafting from feedback-conditioned correction. Use compiler/tool/reviewer feedback to isolate and repair the bad block.
- **APRIL**: [diagnostic-conditioned Lean repair](https://arxiv.org/abs/2602.02990) supports preserving the failing proof, exact compiler output, local state, diagnosis, repair, and replay as one unit. Its evidence is single-shot repair on synthetic mutations, not general theorem discovery.
- **SorryDB/self-modifying agents**: realistic project tasks favor iterative checker feedback, while richer tool use or decomposition can distract or fail at final assembly. Start with the smallest grounded loop and escalate only when it stops reducing the checked state.
- **Goedel-Architect/LEAP/DeepSeek-Prover-V2**: maintain a dependency graph or AND/OR DAG. Preserve solved nodes, reject orphan lemmas, and require final proof structure to match accepted subgoals or explain the change.
- **STAR-PolyaMath**: keep control outside the proof attempt. Use challenge rounds, trace-back, re-plan caps, and a pure-reasoning mode when tool use stops shrinking the proof state.
- **Goedel-Prover-V2/process verification**: feed the precise first error and valid prefix into correction; do not regenerate from an undifferentiated failure signal.
- **Aletheia-style separation**: let verification inspect the proposed proof rather than merely continue its reasoning. A verifier may abstain or reject when evidence is insufficient.
- **MerLean-Prover**: enforce role authority. Planner edits the plan, prover edits one local proof object, checker answers one precise correctness or decomposition question.
- **Rethlas/Archon**: separate strategy generation from verifier replay, preserve structured run artifacts, and inspect definitions and proof technique rather than only theorem statements. Import the separation and replay discipline, not the claim that a language-model verdict is a kernel proof.

## Stop Rule

End the loop or reroute when one of these holds:

- two cycles leave the same obstruction unchanged;
- the verifier keeps challenging the same local move with no new evidence;
- proposer and verifier keep converging on the same unsupported assumption;
- tool calls produce data but no smaller proof state;
- the statement needs a modeling choice, domain convention, or assumption repair;
- the next move has no expected artifact.

Report the exact obstruction instead of polishing an unsupported proof.
