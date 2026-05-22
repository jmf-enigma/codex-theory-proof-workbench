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

## Pre-Solve Gate

- Direct theorem/certificate available:
- Direct route if yes:
- If no, why not:
- Paper or prior-ledger patterns to search:

## Strategy Portfolio

- Route A:
  - reason selected:
  - status:
- Route B:
  - reason selected:
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
- Quantifier gate:
- Boundary gate:
- Assembly gate:
- Review gate:
- Progress gate:

## Lemma Graph

- Lemma A:
  - statement:
  - status: missing

## Failed Routes

- Route 1:
  - idea:
  - where it broke:
  - obstruction type:
  - what it taught:

## Failure Escalation

- trigger:
- external method used:
- result:
- theorem repair, if any:

## Tool Checks

- Wolfram/SymPy:
- Python/CVXPy/Z3/OR-Tools/Sage:
- Lean:

## Current Obstruction

Name the exact missing lemma or condition.

## Next Move

The next proof pattern or counterexample search to try.
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", text.strip().lower()).strip("-")
    return slug or "proof"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a proof ledger markdown file.")
    parser.add_argument("title", help="Short proof name")
    parser.add_argument("--claim", default="State the exact theorem here.", help="Initial theorem statement")
    parser.add_argument("--dir", default="proof_ledgers", help="Output directory")
    args = parser.parse_args()

    out_dir = Path(args.dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slugify(args.title)}.md"
    if path.exists():
        raise SystemExit(f"ledger already exists: {path}")
    path.write_text(TEMPLATE.format(title=args.title, claim=args.claim), encoding="utf-8")
    print(path)


if __name__ == "__main__":
    main()
