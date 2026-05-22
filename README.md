# Codex Theory Proof Workbench

A Codex skill for hard theoretical proof discovery, proof debugging, and failed-proof recovery.

The skill is designed for research problems in OR/MS, mechanism design, economic theory, dynamic programming, learning theory, bandits, online learning, optimization, games, IC/IR, regret analysis, and lower bounds. It is not a theorem database. It is a proof-control workflow that helps Codex avoid restarting from scratch, avoid silently changing the theorem, and keep failed proof attempts as useful state.

## What It Does

- Routes a proof by theorem family and proof pattern.
- Audits assumptions, quantifiers, boundary cases, and theorem statement drift.
- Forces one proof route and one falsification route before polished proof writing.
- Builds lemma graphs with statuses such as known, proved, tool-checked, missing, or false.
- Records repeated failed attempts with fingerprints so the same construction is not retried under new notation.
- Uses small cases, exact pattern mining, and tool checks to guess and verify clever constructions or algebraic normal forms.
- Escalates stuck proofs through counterexample search, symbolic checks, LP/SMT certificates, literature/premise retrieval, local Lean formalization, or theorem repair.

## When To Use

Use this skill when the proof itself is missing, blocked, suspicious, or has failed before.

Typical tasks include:

- Prove a monotone or threshold policy in a DP/MDP.
- Debug a mechanism design IC/IR or cyclic monotonicity proof.
- Find the right regret decomposition for a bandit or online learning theorem.
- Repair a lower-bound construction whose KL or separation argument does not work.
- Decide whether a theorem is true under the stated assumptions.
- Preserve failed proof attempts so later work starts from evidence instead of memory.

For exposition, polishing, or LaTeX cleanup after the proof idea is already complete, use a proof-writing skill instead.

## Installation

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git ~/.codex/skills/theory-proof-workbench
```

Restart Codex or refresh skill discovery if needed. The skill name is:

```text
theory-proof-workbench
```

## Quick Start

For a lightweight idea pass:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

For a hard or repeatedly failed proof, start a proof project:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

When returning to a proof project:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

Before claiming a final proof from a ledger:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

## Workflow

The core loop is:

1. Restate the claim with exact variables, domains, quantifiers, and assumptions.
2. Preserve the theorem statement. If the proof needs a changed claim, mark it as theorem repair.
3. Try a direct theorem, certificate, contradiction, or known decomposition.
4. Search for counterexamples in small, finite, boundary, or relaxed-assumption cases.
5. Choose a route and reduce it to a proof kernel.
6. Build a lemma graph and solve fragile lemmas one at a time.
7. Use tools only when their output becomes a checkable lemma, certificate, counterexample, or repair.
8. Record failed routes and unchanged proof states.
9. Apply verification gates before writing the final proof.

## Project Files

`start_proof.py` creates a structured proof workspace:

- `TRIAGE.md`: immediate next steps and proof-mode rules.
- `WORKSTREAMS.md`: bounded workstream cards and no-repeat attempt fingerprints.
- `IDEA_MAP.md`: central objects, proof kernels, and one-step proof moves.
- `ATTACK_MATRIX.md`: proof routes and falsification routes.
- `LEMMA_QUEUE.md`: candidate lemmas to prove, refute, or certify.
- `PATTERN_SCAN.md`: bounded extraction from papers, prior ledgers, or proof-agent workflows.
- `TOOL_PLAN.md`: expected artifacts before CAS, SMT, optimization, Python, Wolfram, Sage, or Lean checks.
- `LEDGER.md`: persistent proof state, failed routes, verification gates, and current obstruction.
- `ESCALATION.md`: what to do after repeated failure.

## Tool Philosophy

Tools do not replace proof. They help produce artifacts that can be checked:

- Wolfram or SymPy for algebra, inequalities, assumptions, and symbolic conditions.
- Python, CVXPy, Z3, OR-Tools, or Sage for finite examples, LP/MIP certificates, graph checks, or exact computations.
- Lean/mathlib for stable local lemmas once the statement is precise.
- Simulations only for falsification or sanity checks, not for proving universal claims.

## Verification Standards

The skill distinguishes proof statuses:

- `conjecture`: intuition or pattern match only.
- `counterexample-tested`: no counterexample found in bounded searches.
- `lemma-conditional`: final theorem depends on named missing lemmas.
- `human-proof`: every nontrivial step is justified in prose.
- `tool-checked`: fragile algebra or constraints were checked by tools.
- `formalized-local`: key local lemmas were checked in Lean or another formal system.
- `formalized-complete`: the full theorem is machine-formalized.

Do not call a result proved if the key lemma is only guessed.

## Repository Layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── dp-proof-playbook.md
│   ├── mechanism-design-playbook.md
│   ├── learning-theory-playbook.md
│   ├── bandits-oco-playbook.md
│   └── ...
└── scripts/
    ├── start_proof.py
    ├── proof_doctor.py
    ├── audit_ledger.py
    ├── pattern_miner.py
    └── ...
```

## Development Checks

Validate the skill structure:

```bash
codex-math-python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Compile scripts:

```bash
PYTHONPYCACHEPREFIX=/tmp/codex-pycache python3 -m py_compile scripts/*.py
```

Run a smoke test:

```bash
python3 scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## License

No license has been selected yet. Until a license is added, all rights are reserved by the repository owner.
