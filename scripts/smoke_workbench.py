#!/usr/bin/env python3
"""Exercise routing, project creation, recovery control, and proof diagnosis."""

from __future__ import annotations

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
            and "PatternBoost" in discovery_text
            and "Self-supervised theorem discovery" in discovery_text,
        }
    )

    result = {"ok": all(bool(check["ok"]) for check in checks), "checks": checks}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
