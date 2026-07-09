#!/usr/bin/env python3
"""Audit a theory-proof ledger without forcing inactive advanced workflows."""

from __future__ import annotations

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

# These fields are required for every final proof ledger. Advanced workflow fields
# are activated separately below so a direct proof is not forced through PV or Lean.
BASE_PLACEHOLDER_PATTERNS = [
    r"Name the exact missing lemma",
    r"The next proof pattern",
    r"Candidate patterns:[ \t]*\n[ \t]*(?:\n|Selected playbooks:)",
    r"Selected playbooks:[ \t]*\n[ \t]*(?:\n|## )",
    r"mode:[ \t]*$",
    r"mode:[ \t]*direct / micro-check / light-idea / project / recovery[ \t]*$",
    r"next artifact expected:[ \t]*$",
    r"expected artifact:[ \t]*$",
    r"expected artifact:[ \t]*(?:proof / counterexample / missing assumption / certificate / theorem pattern / repaired theorem|counterexample / exact identity / conditions / KKT-dual certificate / SMT model-or-unsat / Lean lemma / other)[ \t]*$",
    r"status:[ \t]*$",
    r"Direct theorem/certificate available:[ \t]*$",
    r"If no, why not:[ \t]*$",
    r"Required:[ \t]*$",
    r"Missing or suspicious:[ \t]*$",
    r"Boundary cases:[ \t]*$",
    r"Finite/discrete examples:[ \t]*$",
    r"Numerical examples:[ \t]*$",
    r"Relaxed-assumption failures:[ \t]*$",
    r"next bounded move:[ \t]*$",
    r"retry allowed only if:[ \t]*$",
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
    r"Quantifier gate:[ \t]*$",
    r"Boundary gate:[ \t]*$",
    r"Assembly gate:[ \t]*$",
    r"Review gate:[ \t]*$",
    r"Progress gate:[ \t]*$",
]

FAILURE_PLACEHOLDER_PATTERNS = [
    r"route decision:[ \t]*$",
    r"route decision:[ \t]*continue / repair / re-decompose / retrieve / tool-falsify / stop-report[ \t]*$",
    r"proof-state delta:[ \t]*$",
    r"obstruction type:[ \t]*$",
]

EQUIVALENCE_PLACEHOLDER_PATTERNS = [
    r"repeated state/action:[ \t]*$",
    r"shared goal and assumptions:[ \t]*$",
    r"shared central object:[ \t]*$",
    r"shared failure witness:[ \t]*$",
    r"decision:[ \t]*merge / allow-new[ \t]*$",
]

STEP_PLACEHOLDER_PATTERNS = [
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

PV_PLACEHOLDER_PATTERNS = [
    r"prover move if using PV:[ \t]*$",
    r"verifier verdict if using PV:[ \t]*$",
    r"soundness probe if using PV:[ \t]*$",
    r"coordinator decision if using PV:[ \t]*$",
]

TOOL_PLACEHOLDER_PATTERNS = [
    r"expected artifact before next tool call:[ \t]*$",
]

FORMAL_PLACEHOLDER_PATTERNS = [
    r"formal artifact audit:[ \t]*`sorry` / admitted axioms / unresolved obligations / missing assembly:[ \t]*$",
]

PLACEHOLDER_PATTERNS = (
    BASE_PLACEHOLDER_PATTERNS
    + FAILURE_PLACEHOLDER_PATTERNS
    + EQUIVALENCE_PLACEHOLDER_PATTERNS
    + STEP_PLACEHOLDER_PATTERNS
    + PV_PLACEHOLDER_PATTERNS
    + TOOL_PLACEHOLDER_PATTERNS
    + FORMAL_PLACEHOLDER_PATTERNS
)


def section_body(text: str, heading: str) -> str | None:
    pattern = rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.M | re.S)
    return match.group("body").strip() if match else None


def field_values(text: str, field: str) -> list[str]:
    pattern = rf"^[ \t]*(?:[-*][^\S\r\n]*)?{re.escape(field)}:[^\S\r\n]*(?P<value>\S.*)$"
    return [match.group("value").strip() for match in re.finditer(pattern, text, flags=re.I | re.M)]


def is_real_value(value: str) -> bool:
    lower = value.strip().lower()
    if not lower or " / " in lower:
        return False
    return lower not in {"none", "not used", "not applicable", "n/a", "pending", "planned", "unknown"}


def any_real_field(text: str, fields: list[str]) -> bool:
    return any(is_real_value(value) for field in fields for value in field_values(text, field))


def collect_placeholders(text: str, patterns: list[str]) -> list[str]:
    return [pattern for pattern in patterns if re.search(pattern, text, flags=re.M)]


def activation_summary(text: str) -> dict[str, bool]:
    failed_routes = section_body(text, "Failed Routes") or ""
    tool_checks = section_body(text, "Tool Checks") or ""
    verification = (section_body(text, "Verification Status") or "").lower()
    return {
        "failure_recovery": any_real_field(
            failed_routes,
            ["idea", "where it broke", "obstruction type", "attempt fingerprint"],
        ),
        "state_equivalence": any_real_field(
            text,
            ["repeated state/action", "shared goal and assumptions", "shared central object", "shared failure witness"],
        ),
        "step_challenge": any_real_field(
            text,
            ["current step", "goal gate", "logic gate", "trace-back target", "re-plan directive"],
        ),
        "prover_verifier": any_real_field(
            text,
            [
                "prover move if using PV",
                "verifier verdict if using PV",
                "soundness probe if using PV",
                "coordinator decision if using PV",
            ],
        ),
        "tool_check": any_real_field(
            tool_checks,
            ["Wolfram/SymPy", "Python/CVXPy/Z3/OR-Tools/Sage", "Lean"],
        ),
        "formal_check": "formalized" in verification or any_real_field(tool_checks, ["Lean"]),
    }


def audit_ledger_text(text: str, ledger: Path | str) -> dict:
    activations = activation_summary(text)
    patterns = list(BASE_PLACEHOLDER_PATTERNS)
    if activations["failure_recovery"]:
        patterns.extend(FAILURE_PLACEHOLDER_PATTERNS)
    if activations["state_equivalence"]:
        patterns.extend(EQUIVALENCE_PLACEHOLDER_PATTERNS)
    if activations["step_challenge"]:
        patterns.extend(STEP_PLACEHOLDER_PATTERNS)
    if activations["prover_verifier"]:
        patterns.extend(PV_PLACEHOLDER_PATTERNS)
    if activations["tool_check"]:
        patterns.extend(TOOL_PLACEHOLDER_PATTERNS)
    if activations["formal_check"]:
        patterns.extend(FORMAL_PLACEHOLDER_PATTERNS)

    missing_headings = [heading for heading in REQUIRED_HEADINGS if section_body(text, heading) is None]
    empty_sections = [heading for heading in REQUIRED_HEADINGS if section_body(text, heading) == ""]
    placeholders = collect_placeholders(text, patterns)
    return {
        "ledger": str(ledger),
        "missing_headings": missing_headings,
        "empty_sections": empty_sections,
        "placeholder_count": len(placeholders),
        "placeholders": placeholders,
        "conditional_workflows": activations,
        "ready_for_final_proof": not missing_headings and not empty_sections and not placeholders,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", help="Path to LEDGER.md or proof ledger")
    args = parser.parse_args()

    path = Path(args.ledger)
    result = audit_ledger_text(path.read_text(encoding="utf-8"), path)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
