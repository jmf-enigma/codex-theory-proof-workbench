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

- mode: direct / micro-check / light-idea / project / recovery
- why this mode is enough:
- next artifact expected:
- stop or escalation trigger:

## Pre-Solve Gate

- Direct theorem/certificate available:
- Direct route if yes:
- If no, why not:
- Paper or prior-ledger patterns to search:

## Strategy Portfolio

- Route A:
  - reason selected:
  - route novelty:
  - expected artifact:
  - status:
- Route B:
  - reason selected:
  - route novelty:
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

## Lemma Graph

Use statement deps for mathematical meaning and proof deps for facts/tools/helper lemmas used to prove the node.
Use OR nodes for alternative routes and AND nodes for required child lemmas. Merge equivalent states/actions before retrying the same obstruction.

| node id | type | status | statement / role | statement deps | proof deps | used by assembly | expected artifact | gap grade | failure diagnosis |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N1 | lemma | missing |  |  |  | yes / no / unknown | proof / tool check / counterexample / theorem pattern | good / bad / unknown |  |

## Proof-State Equivalence

- repeated state/action:
- shared goal and assumptions:
- shared central object:
- shared failure witness:
- decision: merge / allow-new

## Step Challenge Loop

- current step:
- verification tag: tool-verified / easy-to-check / hard-to-check
- goal gate:
- logic gate:
- prover move if using PV:
- verifier verdict if using PV:
- soundness probe if using PV:
- coordinator decision if using PV:
- challenge rounds used / cap:
- replans used / cap:
- time or token budget status:
- verdict: accept / challenge / trace-back / re-decompose / re-plan / stop
- trace-back target:
- re-plan directive:
- tool-use brake needed:

## Failed Routes

- Route 1:
  - idea:
  - where it broke:
  - obstruction type:
  - proof-state delta:
  - attempt fingerprint:
  - new evidence expected before retry:
  - what it taught:

## Failure Escalation

- trigger:
- route decision: continue / repair / re-decompose / retrieve / tool-falsify / stop-report
- proof-state delta and failure diversity:
- external method used:
- result:
- theorem repair, if any:

## Tool Checks

- Wolfram/SymPy:
- Python/CVXPy/Z3/OR-Tools/Sage:
- Lean:
- formal artifact audit: `sorry` / admitted axioms / unresolved obligations / missing assembly:
- expected artifact before next tool call:

## Current Obstruction

Name the exact missing lemma or condition.

## Next Move

- next bounded move:
- expected artifact:
- retry allowed only if:
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
