import argparse
import json
import re
from pathlib import Path


REQUIRED_HEADINGS = [
    "Claim",
    "Status",
    "Verification Status",
    "Proof State",
    "Pattern Classification",
    "Mode Decision",
    "Pre-Solve Gate",
    "Strategy Portfolio",
    "Assumption Audit",
    "Counterexample Search",
    "Verification Gates",
    "Lemma Graph",
    "Failed Routes",
    "Failure Escalation",
    "Tool Checks",
    "Current Obstruction",
    "Next Move",
]

PLACEHOLDER_PATTERNS = [
    r"Name the exact missing lemma",
    r"The next proof pattern",
    r"Candidate patterns:[ \t]*\n[ \t]*(?:\n|Selected playbooks:)",
    r"Selected playbooks:[ \t]*\n[ \t]*(?:\n|## )",
    r"mode:[ \t]*$",
    r"mode:[ \t]*direct / micro-check / light-idea / project / recovery[ \t]*$",
    r"next artifact expected:[ \t]*$",
    r"route decision:[ \t]*$",
    r"route decision:[ \t]*continue / repair / re-decompose / retrieve / tool-falsify / stop-report[ \t]*$",
    r"expected artifact:[ \t]*$",
    r"expected artifact:[ \t]*(?:proof / counterexample / missing assumption / certificate / theorem pattern / repaired theorem|counterexample / exact identity / conditions / KKT-dual certificate / SMT model-or-unsat / Lean lemma / other)[ \t]*$",
    r"proof-state delta:[ \t]*$",
    r"status:[ \t]*$",
    r"obstruction type:[ \t]*$",
    r"Direct theorem/certificate available:[ \t]*$",
    r"If no, why not:[ \t]*$",
    r"Required:[ \t]*$",
    r"Missing or suspicious:[ \t]*$",
    r"Boundary cases:[ \t]*$",
    r"Finite/discrete examples:[ \t]*$",
    r"Numerical examples:[ \t]*$",
    r"Relaxed-assumption failures:[ \t]*$",
    r"expected artifact before next tool call:[ \t]*$",
    r"next bounded move:[ \t]*$",
    r"retry allowed only if:[ \t]*$",
    r"repeated state/action:[ \t]*$",
    r"shared goal and assumptions:[ \t]*$",
    r"shared central object:[ \t]*$",
    r"shared failure witness:[ \t]*$",
    r"decision:[ \t]*merge / allow-new[ \t]*$",
    r"formal artifact audit:[ \t]*`sorry` / admitted axioms / unresolved obligations / missing assembly:[ \t]*$",
    r"\|\s*N1\s*\|\s*lemma\s*\|\s*missing\s*\|[^\n]*yes / no / unknown[^\n]*proof / tool check / counterexample / theorem pattern[^\n]*good / bad / unknown",
    r"Pre-solve gate:[ \t]*$",
    r"Statement gate:[ \t]*$",
    r"Assumption gate:[ \t]*$",
    r"Negation gate:[ \t]*$",
    r"Toy-model gate:[ \t]*$",
    r"Pattern gate:[ \t]*$",
    r"Lemma gate:[ \t]*$",
    r"Proof-state gate:[ \t]*$",
    r"Step-verdict gate:[ \t]*$",
    r"prover move if using PV:[ \t]*$",
    r"verifier verdict if using PV:[ \t]*$",
    r"soundness probe if using PV:[ \t]*$",
    r"coordinator decision if using PV:[ \t]*$",
    r"Quantifier gate:[ \t]*$",
    r"Boundary gate:[ \t]*$",
    r"Assembly gate:[ \t]*$",
    r"Review gate:[ \t]*$",
    r"Progress gate:[ \t]*$",
    r"current step:[ \t]*$",
    r"verification tag:[ \t]*tool-verified / easy-to-check / hard-to-check[ \t]*$",
    r"goal gate:[ \t]*$",
    r"logic gate:[ \t]*$",
    r"challenge rounds used / cap:[ \t]*$",
    r"replans used / cap:[ \t]*$",
    r"time or token budget status:[ \t]*$",
    r"verdict:[ \t]*accept / challenge / trace-back / re-decompose / re-plan / stop[ \t]*$",
    r"tool-use brake needed:[ \t]*$",
]


def section_body(text: str, heading: str) -> str | None:
    pattern = rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group("body").strip() if match else None


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit a theory proof ledger for missing gates.")
    parser.add_argument("ledger", help="Path to LEDGER.md or proof ledger")
    args = parser.parse_args()

    path = Path(args.ledger)
    text = path.read_text(encoding="utf-8")

    missing_headings = [h for h in REQUIRED_HEADINGS if section_body(text, h) is None]
    empty_sections = [h for h in REQUIRED_HEADINGS if section_body(text, h) == ""]
    placeholders = []
    for pat in PLACEHOLDER_PATTERNS:
        if re.search(pat, text, flags=re.M):
            placeholders.append(pat)

    result = {
        "ledger": str(path),
        "missing_headings": missing_headings,
        "empty_sections": empty_sections,
        "placeholder_count": len(placeholders),
        "placeholders": placeholders,
        "ready_for_final_proof": not missing_headings and not empty_sections and not placeholders,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
