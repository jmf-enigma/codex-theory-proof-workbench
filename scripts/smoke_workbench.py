#!/usr/bin/env python3
"""Exercise routing, project creation, recovery control, and proof diagnosis."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        check=True,
        capture_output=True,
        text=True,
    )


def main() -> int:
    checks: list[dict[str, object]] = []

    frontier_spec = importlib.util.spec_from_file_location(
        "frontier_evidence_smoke",
        SCRIPTS / "frontier_evidence.py",
    )
    if frontier_spec is None or frontier_spec.loader is None:
        raise RuntimeError("could not load frontier_evidence.py")
    frontier_module = importlib.util.module_from_spec(frontier_spec)
    frontier_spec.loader.exec_module(frontier_module)
    signed_fixture = (
        "https://download.ssrn.com/20/07/29/"
        "ssrn_id3663420_code2380208.pdf?"
        "X-Amz-Date=20260710T072615Z&X-Amz-Expires=300&abstractId=3395992"
    )
    signed_expired = False
    try:
        frontier_module.validate_ssrn_signed_url(signed_fixture, "3395992")
    except ValueError as exc:
        signed_expired = "expired" in str(exc)
    fallback_args = frontier_module.build_parser().parse_args(
        [
            "fetch",
            "/tmp/project",
            "--paper-id",
            "P1",
            "--doi",
            "10.1287/example",
            "--fallback-url",
            "https://example.edu/paper.pdf",
        ]
    )
    checks.append(
        {
            "name": "ssrn-version-and-expiry-guard",
            "ok": frontier_module.normalize_ssrn_id(signed_fixture) == "3395992"
            and frontier_module.normalize_ssrn_id("https://doi.org/10.2139/ssrn.3395992")
            == "3395992"
            and signed_expired
            and frontier_module.automatic_pdf_url(
                "https://www.econstor.eu/bitstream/10419/1/paper.pdf"
            )
            and not frontier_module.automatic_pdf_url(
                "https://download.ssrn.com/temporary.pdf"
            )
            and frontier_module.same_work(
                {"title": "Mechanism Design and Intentions", "authors": ["Bierbrauer, Felix"]},
                {"title": "Mechanism Design & Intentions", "authors": ["Felix Bierbrauer"]},
            )
            and fallback_args.fallback_url == "https://example.edu/paper.pdf",
        }
    )

    idea = run(
        str(SCRIPTS / "plan_idea.py"),
        "In a finite discounted MDP, the Bellman operator is a contraction.",
    )
    checks.append(
        {
            "name": "idea-routing",
            "ok": "dp-proof-playbook.md" in idea.stdout and "Proof Kernel" not in idea.stdout,
        }
    )

    mechanism = run(
        str(SCRIPTS / "select_playbook.py"),
        "Prove incentive compatibility from cyclic monotonicity in a finite-type mechanism.",
    )
    selected = json.loads(mechanism.stdout)
    checks.append(
        {
            "name": "mechanism-routing",
            "ok": "mechanism-design-playbook.md" in selected.get("selected", []),
        }
    )

    bandit = run(
        str(SCRIPTS / "select_playbook.py"),
        "Prove a logarithmic UCB regret bound from a uniform confidence event.",
    )
    bandit_selected = json.loads(bandit.stdout)
    checks.append(
        {
            "name": "bandit-routing",
            "ok": "bandits-oco-playbook.md" in bandit_selected.get("selected", []),
        }
    )

    peppy_route = run(
        str(SCRIPTS / "select_playbook.py"),
        "Prove the worst-case rate of proximal gradient with a Lyapunov function.",
    )
    peppy_selected = json.loads(peppy_route.stdout)
    peppy_idea = run(
        str(SCRIPTS / "plan_idea.py"),
        "Prove the worst-case rate of proximal gradient with a Lyapunov function.",
    )
    checks.append(
        {
            "name": "peppy-optimization-routing",
            "ok": "optimization-or-playbook.md" in peppy_selected.get("selected", [])
            and "PEP dual/Lyapunov certificate" in peppy_idea.stdout,
        }
    )

    with tempfile.TemporaryDirectory(prefix="proof-workbench-smoke-") as temp_dir:
        created = run(
            str(SCRIPTS / "start_proof.py"),
            "--title",
            "smoke-mdp",
            "--claim",
            "In a finite discounted MDP, the Bellman operator is a contraction.",
            "--dir",
            temp_dir,
        )
        project = Path(created.stdout.strip())
        required = {
            "claim.md",
            "TRIAGE.md",
            "LEDGER.md",
            "IDEA_MAP.md",
            "LEMMA_QUEUE.md",
            "routing.json",
        }
        checks.append(
            {
                "name": "project-creation",
                "ok": project.is_dir() and all((project / name).is_file() for name in required),
            }
        )

        diagnosis = run(str(SCRIPTS / "proof_doctor.py"), str(project), "--json")
        diagnosed = json.loads(diagnosis.stdout)
        checks.append(
            {
                "name": "proof-diagnosis",
                "ok": bool(diagnosed.get("primary_action"))
                and diagnosed.get("project") == str(project)
                and not diagnosed["novel_problem"]["activated"],
            }
        )

        ledger = project / "LEDGER.md"
        ledger.write_text(
            ledger.read_text(encoding="utf-8").replace("S2-stress-test", "S9-stuck"),
            encoding="utf-8",
        )
        workstreams = project / "WORKSTREAMS.md"
        stalled = workstreams.read_text(encoding="utf-8") + (
            "\n- proof-state delta: unchanged\n"
            "- proof-state delta: unchanged\n"
        )
        workstreams.write_text(stalled, encoding="utf-8")
        stalled_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(project), "--json").stdout
        )
        checks.append(
            {
                "name": "first-error-gate",
                "ok": stalled_diagnosis["failure_localization"]["needed"]
                and stalled_diagnosis["primary_action"].startswith("Localize the earliest failing step"),
            }
        )

        localized = stalled.replace(
            "- verified prefix:\n",
            "- verified prefix: steps 1-2 and helper lemma H1\n",
        ).replace(
            "- first failing step:\n",
            "- first failing step: step 3, Bellman difference sign\n",
        ).replace(
            "- failure witness or verifier error:\n",
            "- failure witness or verifier error: boundary state x=0 reverses the inequality\n",
        ).replace(
            "- independently rescued artifacts:\n",
            "- independently rescued artifacts: helper lemma H1\n",
        ).replace(
            "- failure stage: strategy-discovery / decomposition / premise-retrieval / local-proof / assembly / fidelity / library-coverage\n",
            "- failure stage: local-proof\n",
        ).replace(
            "- next scope: local trace-back / re-decompose / route replan / statement repair / stop-report\n",
            "- next scope: local trace-back\n",
        )
        workstreams.write_text(localized, encoding="utf-8")
        localized_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(project), "--json").stdout
        )
        checks.append(
            {
                "name": "verified-prefix-salvage",
                "ok": not localized_diagnosis["failure_localization"]["needed"]
                and bool(localized_diagnosis["failure_localization"]["first_failing_step"])
                and bool(localized_diagnosis["failure_localization"]["rescued_artifacts"])
                and localized_diagnosis["primary_action"].startswith(
                    "Execute the localized scope: local trace-back"
                ),
            }
        )

        retrieval_failure = localized.replace(
            "- failure stage: local-proof\n",
            "- failure stage: retrieval\n",
        )
        workstreams.write_text(retrieval_failure, encoding="utf-8")
        retrieval_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(project), "--json").stdout
        )
        checks.append(
            {
                "name": "failure-stage-routing",
                "ok": retrieval_diagnosis["failure_stage"]["stage"] == "premise-retrieval"
                and retrieval_diagnosis["primary_action"].startswith(
                    "Run sketch-retrieve-reflect"
                ),
            }
        )

        discovery_created = run(
            str(SCRIPTS / "start_proof.py"),
            "--title",
            "smoke-discovery",
            "--claim",
            "Find the exact optimal threshold policy in a finite discounted MDP.",
            "--mode",
            "discovery",
            "--dir",
            temp_dir,
        )
        discovery_project = Path(discovery_created.stdout.strip())
        checks.append(
            {
                "name": "frontier-evidence-template",
                "ok": (discovery_project / "literature" / "frontier-evidence.json").is_file(),
            }
        )
        discovery_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(discovery_project), "--json").stdout
        )
        checks.append(
            {
                "name": "novel-frontier-scan-gate",
                "ok": discovery_diagnosis["novel_problem"]["activated"]
                and not discovery_diagnosis["novel_problem"]["ready_for_search"]
                and discovery_diagnosis["primary_action"].startswith(
                    "Run an external frontier scan"
                ),
            }
        )

        idea_map = discovery_project / "IDEA_MAP.md"
        discovery_text = idea_map.read_text(encoding="utf-8")
        memory_only = discovery_text.replace(
            "- known-solution status: not assessed / known / likely known / apparently open / genuinely new",
            "- known-solution status: known",
        )
        idea_map.write_text(memory_only, encoding="utf-8")
        memory_only_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(discovery_project), "--json").stdout
        )
        checks.append(
            {
                "name": "memory-is-not-known-evidence",
                "ok": memory_only_diagnosis["novel_problem"]["frontier_scan_needed"]
                and memory_only_diagnosis["primary_action"].startswith(
                    "Run an external frontier scan"
                ),
            }
        )
        idea_map.write_text(discovery_text, encoding="utf-8")

        evidence_dir = discovery_project / "literature" / "evidence"
        papers_dir = discovery_project / "literature" / "papers"
        evidence_dir.mkdir(parents=True, exist_ok=True)
        papers_dir.mkdir(parents=True, exist_ok=True)
        query_one = evidence_dir / "q01.json"
        query_two = evidence_dir / "q02.json"
        query_one.write_text('{"query":"exact threshold policy theorem","results":["P1"]}\n', encoding="utf-8")
        query_two.write_text('{"query":"finite MDP monotone threshold cited by","results":["P1"]}\n', encoding="utf-8")
        paper_pdf = papers_dir / "P1.pdf"
        paper_bytes = b"%PDF-1.4\n% synthetic smoke fixture\n%%EOF\n"
        paper_pdf.write_bytes(paper_bytes)

        def digest(path: Path) -> str:
            return hashlib.sha256(path.read_bytes()).hexdigest()

        evidence_bundle = {
            "schema_version": 1,
            "claim": "Find the exact optimal threshold policy in a finite discounted MDP.",
            "discovery": {
                "method": "google-scholar-serpapi",
                "queries": [
                    {
                        "query": "exact threshold policy theorem",
                        "url": "https://scholar.google.com/scholar?q=exact+threshold+policy+theorem",
                        "retrieved_at": "2026-07-13",
                        "evidence_path": "literature/evidence/q01.json",
                        "evidence_sha256": digest(query_one),
                    },
                    {
                        "query": "finite MDP monotone threshold cited by",
                        "url": "https://scholar.google.com/scholar?q=finite+MDP+monotone+threshold+cited+by",
                        "retrieved_at": "2026-07-13",
                        "evidence_path": "literature/evidence/q02.json",
                        "evidence_sha256": digest(query_two),
                    },
                ],
            },
            "papers": [
                {
                    "id": "P1",
                    "title": "A closest finite-horizon threshold theorem",
                    "authors": ["Ada Researcher"],
                    "year": 2026,
                    "identifier": "arXiv:2604.15839",
                    "verification_url": "https://arxiv.org/abs/2604.15839",
                    "fulltext": {
                        "status": "proof-read",
                        "path": "literature/papers/P1.pdf",
                        "source_url": "https://arxiv.org/pdf/2604.15839",
                        "retrieved_at": "2026-07-13",
                        "sha256": digest(paper_pdf),
                        "bytes": len(paper_bytes),
                        "version": "preprint",
                        "access": "open-access",
                        "license": "test fixture",
                    },
                    "statement_anchor": "Theorem 2, p. 7, source block S042",
                    "proof_anchor": "Proof of Theorem 2, pp. 18-20, source blocks S131-S149",
                    "result": "A threshold policy is optimal under finite horizon and stronger monotonicity.",
                    "assumptions": "Finite horizon, ordered states, submodular one-step costs.",
                    "gap_to_claim": "The user's infinite-horizon formula is not established.",
                    "solution_card": {
                        "central_object": "Bellman action-difference function",
                        "proof_decomposition": "preserve increasing differences, then invoke single crossing",
                        "key_nonroutine_step": "couple continuation values to keep the action difference monotone",
                        "transplantable_move": "reuse the action-difference representation",
                        "new_bridge_lemma": "prove discounted Bellman iteration preserves the required single crossing",
                        "falsifier_or_evaluator": "exact Bellman inequalities on every state and action",
                    },
                }
            ],
            "activity": {
                "queries": ["2025..2026 cited-by and author-project search for P1"],
                "signals": [],
                "none_found_note": "No exact public project was visible under the recorded query by 2026-07-13.",
            },
            "frontier": {
                "status": "apparently-open",
                "closest_paper_ids": ["P1"],
                "exact_gap": "infinite-horizon threshold formula without the stronger monotonicity assumption",
                "assessment": "Two bounded Scholar queries and a proof-read closest source found only the stronger finite-horizon result.",
            },
            "limitations": ["Bounded search does not prove novelty."],
        }
        (discovery_project / "literature" / "frontier-evidence.json").write_text(
            json.dumps(evidence_bundle, indent=2) + "\n",
            encoding="utf-8",
        )
        evidence_validation = json.loads(
            run(str(SCRIPTS / "frontier_evidence.py"), "validate", str(discovery_project)).stdout
        )
        checks.append(
            {
                "name": "frontier-evidence-validation",
                "ok": evidence_validation["ok"]
                and evidence_validation["counts"]["proof_read"] == 1
                and evidence_validation["counts"]["queries"] == 2,
            }
        )

        setup_replacements = {
            "- frontier scan status: not run / completed": "- frontier scan status: completed",
            "- search cutoff date:": "- search cutoff date: 2026-07-13",
            "- Scholar queries:": "- Scholar queries: exact threshold-policy claim; cited-by search on closest Bellman theorem",
            "- verified source anchors:": "- verified source anchors: Closest Bellman theorem, https://arxiv.org/abs/2604.15839",
            "- closest known result:": "- closest known result: finite-horizon threshold theorem under stronger monotonicity",
            "- active-work signals:": "- active-work signals: two 2026 preprints study related finite-state models; no exact general theorem found",
            "- current frontier gap:": "- current frontier gap: infinite-horizon threshold formula without the stronger monotonicity assumption",
            "- known-solution status: not assessed / known / likely known / apparently open / genuinely new": "- known-solution status: apparently open",
            "- status evidence:": "- status evidence: bounded scan found solved finite neighbors but no general threshold theorem",
            "- discovery target: answer / threshold / formula / construction / policy / invariant / counterexample / intermediate theorem / new representation": "- discovery target: threshold formula",
            "- candidate representation:": "- candidate representation: integer threshold as a function of model parameters",
            "- validity gate:": "- validity gate: exact Bellman inequalities for every state and action",
            "- score or evaluator:": "- score or evaluator: feasibility first, then Bellman slack and formula complexity",
            "- simplification ladder:": "- simplification ladder: two states, finite horizon, then general finite discounted model",
            "- discovery budget:": "- discovery budget: 40 candidates or two plateau cycles",
        }
        for old, new in setup_replacements.items():
            discovery_text = discovery_text.replace(old, new)
        idea_map.write_text(discovery_text, encoding="utf-8")
        search_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(discovery_project), "--json").stdout
        )
        checks.append(
            {
                "name": "novel-discovery-search-routing",
                "ok": search_diagnosis["novel_problem"]["ready_for_search"]
                and search_diagnosis["primary_action"].startswith(
                    "Run one bounded discovery cycle"
                ),
            }
        )

        paper_pdf.write_bytes(paper_bytes + b"tampered")
        tampered_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(discovery_project), "--json").stdout
        )
        checks.append(
            {
                "name": "frontier-hash-tamper-gate",
                "ok": tampered_diagnosis["novel_problem"]["frontier_scan_needed"]
                and any(
                    "sha256 mismatch" in item
                    for item in tampered_diagnosis["novel_problem"]["frontier_missing"]
                ),
            }
        )
        paper_pdf.write_bytes(paper_bytes)

        promoted = idea_map.read_text(encoding="utf-8").replace(
            "- holdout cases:",
            "- holdout cases: larger state spaces and boundary discount factors",
        ).replace(
            "- promotion criterion:",
            "- promotion criterion: exact Bellman feasibility on seeds and holdouts",
        ).replace(
            "- discovered candidate:",
            "- discovered candidate: threshold tau(theta) from the fitted recurrence",
        ).replace(
            "- fixed proof handoff:",
            "- fixed proof handoff: prove policy tau(theta) satisfies every Bellman inequality",
        )
        idea_map.write_text(promoted, encoding="utf-8")
        handoff_diagnosis = json.loads(
            run(str(SCRIPTS / "proof_doctor.py"), str(discovery_project), "--json").stdout
        )
        checks.append(
            {
                "name": "novel-discovery-proof-handoff",
                "ok": handoff_diagnosis["novel_problem"]["handoff_ready"]
                and handoff_diagnosis["novel_problem"]["recommended_action"].startswith(
                    "Switch to the ordinary proof loop"
                )
                and not handoff_diagnosis["primary_action"].startswith(
                    "Run one bounded discovery cycle"
                ),
            }
        )

    portable_text = (ROOT / "SKILL.md").read_text(encoding="utf-8") + (
        SCRIPTS / "start_proof.py"
    ).read_text(encoding="utf-8")
    checks.append(
        {
            "name": "portable-paths",
            "ok": "/Users/" not in portable_text,
        }
    )

    research_text = (ROOT / "references" / "research-backed-proof-loop.md").read_text(
        encoding="utf-8"
    )
    discovery_text = (ROOT / "references" / "novel-problem-discovery.md").read_text(
        encoding="utf-8"
    )
    frontier_text = (ROOT / "references" / "full-text-frontier-evidence.md").read_text(
        encoding="utf-8"
    )
    peppy_text = (ROOT / "references" / "peppy-proof-bridge.md").read_text(
        encoding="utf-8"
    )
    template_text = (SCRIPTS / "start_proof.py").read_text(encoding="utf-8")
    checks.append(
        {
            "name": "research-control-rules",
            "ok": all(
                phrase in research_text
                for phrase in [
                    "Frontier choice",
                    "First-error and stage pass",
                    "Decomposition admission",
                    "LeanSearch v2",
                    "Goedel-Prover-V2",
                    "Aletheia",
                ]
            )
            and "Decomposition Admission Gate" in template_text
            and "jointly sufficient premise bundle" in template_text
            and "Discover-To-Prove Handoff" in discovery_text
            and "Google Scholar-backed discovery" in discovery_text
            and "SHA-256" in frontier_text
            and "solution card" in frontier_text
            and "no_authorized_pdf_found" in frontier_text
            and "PatternBoost" in discovery_text
            and "Self-supervised theorem discovery" in discovery_text,
        }
    )
    checks.append(
        {
            "name": "peppy-conditional-proof-bridge",
            "ok": "peppy-proof-bridge.md" in portable_text
            and "PEP Eligibility Gate" in peppy_text
            and "Stop after the first block" in peppy_text
            and "A small floating residual is not an exact certificate" in peppy_text
            and all(
                source in peppy_text
                for source in [
                    "10.1007/s10107-013-0653-0",
                    "10.1007/s10107-016-1009-3",
                    "10.1137/16M108104X",
                    "proceedings.mlr.press/v80/taylor18a.html",
                    "openreview.net/forum?id=tJqsZZBmmB",
                    "github.com/pepflow-lib/PEPFlow",
                ]
            )
            and all(
                block in peppy_text
                for block in [
                    "pep-implement",
                    "pep-full-proof",
                    "lyap-define",
                    "lyap-vectors",
                    "lyap-closed-form",
                ]
            ),
        }
    )

    result = {"ok": all(bool(check["ok"]) for check in checks), "checks": checks}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
