#!/usr/bin/env python3
"""Check a proposed proof attempt against recorded attempt fingerprints."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


FIELDS = [
    "route_family",
    "central_object",
    "target_lemma",
    "parameterization",
    "invariant_certificate",
    "failure_witness",
    "missing_assumption",
]


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def parse_index(text: str) -> list[dict[str, str]]:
    match = re.search(
        r"## Attempt Fingerprint Index(?P<body>.*?)(?:\n## No-Repeat Decision|\Z)",
        text,
        flags=re.S,
    )
    if not match:
        return []
    entries = []
    for line in match.group("body").splitlines():
        if not line.startswith("|") or "---" in line or "route family" in line.lower():
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 10:
            continue
        if len(cells) >= 11:
            new_evidence_expected = cells[9]
            retry_allowed_only_if = cells[10]
        else:
            new_evidence_expected = ""
            retry_allowed_only_if = cells[9]
        entry = {
            "id": cells[0],
            "status": cells[1],
            "route_family": cells[2],
            "central_object": cells[3],
            "target_lemma": cells[4],
            "parameterization": cells[5],
            "invariant_certificate": cells[6],
            "failure_witness": cells[7],
            "missing_assumption": cells[8],
            "new_evidence_expected": new_evidence_expected,
            "retry_allowed_only_if": retry_allowed_only_if,
        }
        if sum(bool(entry[field]) for field in FIELDS) >= 3:
            entries.append(entry)
    return entries


def field_match(a: str, b: str) -> bool:
    na = norm(a)
    nb = norm(b)
    if not na or not nb:
        return False
    return na == nb or na in nb or nb in na


def score_attempt(proposed: dict[str, str], entry: dict[str, str]) -> tuple[int, list[str]]:
    score = 0
    hits = []
    weights = {
        "route_family": 2,
        "central_object": 2,
        "target_lemma": 2,
        "parameterization": 2,
        "invariant_certificate": 2,
        "failure_witness": 3,
        "missing_assumption": 3,
    }
    for field, weight in weights.items():
        if field_match(proposed.get(field, ""), entry.get(field, "")):
            score += weight
            hits.append(field)
    return score, hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", help="Proof project directory containing WORKSTREAMS.md")
    parser.add_argument("--route-family", default="")
    parser.add_argument("--central-object", default="")
    parser.add_argument("--target-lemma", default="")
    parser.add_argument("--parameterization", default="")
    parser.add_argument("--invariant-certificate", default="")
    parser.add_argument("--failure-witness", default="")
    parser.add_argument("--missing-assumption", default="")
    parser.add_argument("--new-delta", default="", help="New assumption, invariant, certificate, verified trick, counterexample repair, or theorem repair")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    path = Path(args.project) / "WORKSTREAMS.md"
    if not path.exists():
        raise SystemExit(f"WORKSTREAMS.md not found: {path}")
    proposed = {
        "route_family": args.route_family,
        "central_object": args.central_object,
        "target_lemma": args.target_lemma,
        "parameterization": args.parameterization,
        "invariant_certificate": args.invariant_certificate,
        "failure_witness": args.failure_witness,
        "missing_assumption": args.missing_assumption,
    }
    entries = parse_index(path.read_text(encoding="utf-8"))
    matches = []
    for entry in entries:
        score, hits = score_attempt(proposed, entry)
        if score >= 4:
            matches.append(
                {
                    "id": entry["id"],
                    "status": entry["status"],
                    "score": score,
                    "matched_fields": hits,
                    "new_evidence_expected": entry.get("new_evidence_expected", ""),
                    "retry_allowed_only_if": entry["retry_allowed_only_if"],
                }
            )
    matches.sort(key=lambda item: item["score"], reverse=True)
    decision = "allow"
    if matches and not args.new_delta:
        decision = "block-repeat"
    elif matches:
        decision = "allow-with-delta"
    result = {
        "decision": decision,
        "recorded_fingerprints": len(entries),
        "matches": matches[:5],
        "new_delta": args.new_delta,
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"decision: {decision}")
        print(f"recorded_fingerprints: {len(entries)}")
        if matches:
            print("matches:")
            for item in matches[:5]:
                print(f"- {item['id']} score={item['score']} fields={','.join(item['matched_fields'])}")
                if item["new_evidence_expected"]:
                    print(f"  new_evidence_expected: {item['new_evidence_expected']}")
                if item["retry_allowed_only_if"]:
                    print(f"  retry_allowed_only_if: {item['retry_allowed_only_if']}")
        if args.new_delta:
            print(f"new_delta: {args.new_delta}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
