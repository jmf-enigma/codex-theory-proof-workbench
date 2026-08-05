# Lean Formalization Bridge

Use this protocol when a Theory Proof Workbench node is mathematically stable enough to formalize. The bridge records an immutable request and a replayable Lean result; it does not turn Lean compilation into evidence for an unencoded or incompletely assembled theorem.

## Escalation Gate

Send a node to Lean only when it has:

- an exact statement with domains and assumptions;
- a role: `local-lemma`, `interface-theorem`, or `full-theorem`;
- declared dependencies and a named downstream use;
- a namespace-qualified Lean target and declaration kind;
- no unresolved semantic ambiguity that Lean would merely encode.

Keep discovery in Theory Workbench when the statement, central object, construction, or mathematical route is still moving.

## Prepare A Request

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/lean_bridge.py" prepare PROJECT \
  --node-id L3 \
  --role local-lemma \
  --statement-file lemmas/L3.md \
  --lean-file lean/LocalLemmas.lean \
  --target-name Project.L3 \
  --target-kind lemma \
  --dependency L1 \
  --dependency L2 \
  --downstream-use "closes the monotonicity step"
```

The request in `lean/handoffs/` freezes the project claim hash and revision, node statement, statement-source path and hash when file-backed, dependencies, target, and source-fidelity notes. Relative statement paths resolve inside the proof project. `packet_sha256` detects silent edits. If the theorem or node changes, prepare a new request instead of editing the old one.

For a full theorem, the command also creates an acceptance report. Its four gates start as `not-audited`:

- `claim_fidelity`: the checked Lean target has the same force as the fenced claim;
- `assumption_lineage`: every added assumption is sourced, derived, an explicit interface, or theorem repair;
- `assembly_coverage`: every required child and edge case reaches the final target;
- `axiom_audit`: dependencies contain only accepted foundational or project axioms.

Each passing gate needs concrete evidence text. Lean compilation alone cannot fill these fields.

## Verify And Return

```bash
codex-math-python "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench/scripts/lean_bridge.py" verify PROJECT \
  lean/handoffs/REQUEST.request.json \
  --runner auto
```

The verifier calls the companion `lean-theorem-formalizer` status checker, requires the exact target name and kind, scans blockers, compares the checked file's before/after hashes, writes a unique result packet, and appends the result to `.proof_runtime`. A file changed during checking is not eligible evidence.

Use `--failure-stage statement-fidelity`, `mathematical`, or `assembly` when Lean exposed a problem outside local proof repair. Use `--diagnosis` only for a root-cause judgment grounded in the exact diagnostic, and `--repair` for one bounded next edit. The raw diagnostic remains preserved.

## Ownership Rule

| Result | Next owner |
| --- | --- |
| Exact target passes | Theory integrator assembles the verified node |
| First parse, import, type, premise, or local proof failure | Lean formalizer repairs once |
| Same failure class, site, and diagnostic fingerprint repeat | Theory Workbench retrieves, re-decomposes, or audits the statement |
| Statement-fidelity, mathematical, or assembly failure | Theory Workbench immediately |
| Full theorem passes but an acceptance gate is missing | Theory integrator completes the audit; status stays below complete |

`formalized-local` applies only to the checked node. Use `--promote-final` only for a `full-theorem` request after all four acceptance gates pass. A tampered request, stale claim revision, missing target, placeholder, target-encoding axiom, or incomplete acceptance report blocks promotion.

## Return Packet

The Lean-to-Theory result records:

- exact checker command and exit code;
- request and Lean-file hashes;
- target gate and node status;
- raw diagnostic and diagnostic site;
- failure class, diagnostic fingerprint, inferred root cause, repair, and proof-state delta;
- prior count of the same failure signature;
- recommended owner and final-promotion eligibility.

Treat the result as evidence about the encoded target. The parent theorem remains conditional until the AND-path is assembled and its acceptance obligations are discharged.
