#!/usr/bin/env python3
"""Create a compact proof ledger."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TEMPLATE = """# Proof Ledger: {title}

## Claim

{claim}

## Status

open

## Verification Status

conjecture

## Proof State

S0-parse

## Pattern Classification

Candidate patterns:

Selected playbooks:

## Mode Decision

- mode: {mode}
- why this mode is enough:
- next artifact expected:
- stop or escalation trigger:

## Pre-Solve Gate

- Direct theorem/certificate available:
- Direct route if yes:
- If no, why not:
- One close theorem/paper/prior-ledger pattern to inspect if needed:

## Strategy Portfolio

- Route A:
  - central object or theorem family:
  - expected artifact:
  - status:
- Route B:
  - novelty relative to Route A:
  - expected artifact:
  - status:
- Falsification route:
  - smallest failure world:
  - expected artifact:
  - status:

## Assumption Audit

- Required:
- Missing or suspicious:
- Boundary cases:

## Counterexample Search

- Finite/discrete examples:
- Numerical examples:
- Relaxed-assumption failures:

## Verification Gates

- Pre-solve gate:
- Statement gate:
- Assumption gate:
- Negation gate:
- Toy-model gate:
- Pattern gate:
- Lemma gate:
- Proof-state gate:
- Step-verdict gate:
- Quantifier gate:
- Boundary gate:
- Assembly gate:
- Review gate:
- Progress gate:

Use `not applicable` only with a short reason. Activate the detailed step or prover-verifier contract in `WORKSTREAMS.md` only for fragile, challenged, or repeated moves.

## Lemma Graph

Separate statement dependencies from proof dependencies. Use AND nodes for required children and OR nodes for alternate routes.

| node id | type | status | statement / role | statement deps | proof deps | used by assembly | expected artifact | gap grade | failure diagnosis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N1 | lemma | missing |  |  |  | yes / no / unknown | proof / tool check / counterexample / theorem pattern | good / bad / unknown |  |

## Failed Routes

None recorded. When activated, record route, central object, failed node, failure witness, proof-state delta, and retry condition.

## Failure Escalation

Not activated. After repetition, record the route decision, expected artifact, external method, result, and any theorem repair.

## Tool Checks

- Wolfram/SymPy: not used
- Python/CVXPy/Z3/OR-Tools/Sage: not used
- Lean: not used
- expected artifact before next tool call: not applicable
- formal artifact audit: not applicable

## Current Obstruction

None identified yet.

## Next Move

- next bounded move:
- expected artifact:
- retry allowed only if:
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip().lower()).strip("-")
    return slug or "proof"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("title", help="Short proof name")
    parser.add_argument("--claim", default="State the exact theorem here.", help="Initial theorem statement")
    parser.add_argument(
        "--mode",
        choices=["direct", "micro-check", "light-idea", "project", "recovery"],
        default="direct",
        help="Initial proof mode, default direct",
    )
    parser.add_argument("--dir", default="proof_ledgers", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(args.title)}.md"
    if path.exists():
        raise SystemExit(f"ledger already exists: {path}")
    path.write_text(
        TEMPLATE.format(title=args.title, claim=args.claim, mode=args.mode),
        encoding="utf-8",
    )
    print(path)


if __name__ == "__main__":
    main()
