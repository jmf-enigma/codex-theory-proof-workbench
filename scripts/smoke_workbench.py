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
                "ok": bool(diagnosed.get("primary_action")) and diagnosed.get("project") == str(project),
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
    checks.append(
        {
            "name": "research-control-rules",
            "ok": all(
                phrase in research_text
                for phrase in [
                    "Frontier choice",
                    "First-error and salvage pass",
                    "Goedel-Prover-V2",
                    "Aletheia",
                ]
            ),
        }
    )

    result = {"ok": all(bool(check["ok"]) for check in checks), "checks": checks}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
