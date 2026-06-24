import argparse
import json
import re
from pathlib import Path

from audit_ledger import PLACEHOLDER_PATTERNS, REQUIRED_HEADINGS, section_body
from select_playbook import PLAYBOOKS, score


PATTERN_QUERIES = {
    "dp-proof-playbook.md": [
        "Bellman inequality certificate proof",
        "monotone optimal policy proof submodular dynamic programming",
        "threshold policy single crossing MDP proof",
    ],
    "optimization-or-playbook.md": [
        "KKT sufficiency proof constraint qualification",
        "primal dual certificate operations research proof",
        "exchange argument proof optimization matching scheduling",
    ],
    "mechanism-design-playbook.md": [
        "cyclic monotonicity proof mechanism design",
        "payment identity IC IR envelope theorem proof",
        "finite type payment feasibility LP incentive compatibility",
    ],
    "games-matching-playbook.md": [
        "fixed point theorem game equilibrium proof assumptions",
        "supermodular games increasing differences proof",
        "stable matching blocking pair invariant proof",
    ],
    "learning-theory-playbook.md": [
        "uniform convergence proof covering Rademacher concentration",
        "stability generalization proof learning theory",
        "PAC Bayes proof KL change of measure",
    ],
    "bandits-oco-playbook.md": [
        "uniform confidence event regret proof bandits",
        "elliptical potential lemma linear bandit proof",
        "online convex optimization potential proof regret",
    ],
    "lower-bounds-playbook.md": [
        "two point testing lower bound proof",
        "Fano Assouad minimax lower bound proof",
        "change of measure bandit lower bound KL proof",
    ],
}


STATE_ACTIONS = {
    "S0-parse": [
        "Make variables, domains, quantifiers, assumptions, and desired conclusion explicit in claim.md.",
        "Record the statement fence: proof mode must not silently change assumptions, quantifiers, domains, or conclusion.",
        "Audit statement fidelity for model-heavy or literature-derived claims: definitions, zero/boundary behavior, implicit conventions, and quantifier scope.",
        "Run the direct-solve check: named theorem, certificate, contradiction, or known decomposition.",
        "Classify the theorem family with select_playbook.py.",
    ],
    "S1-classify": [
        "Before route search, check whether the selected playbook gives a direct theorem or certificate.",
        "If the statement came from a paper or informal model, confirm that the formal claim matches the intended theorem before route search.",
        "If no direct route is visible but the proof is still small, do a micro pattern check: one theorem family, prior ledger, or close paper pattern.",
        "Choose at least two proof routes and one falsification route in ATTACK_MATRIX.md or strategy.md.",
        "Move to stress testing before drafting the final proof.",
    ],
    "S2-stress-test": [
        "If direct solve failed, record why in IDEA_MAP.md or LEDGER.md.",
        "Write the negation and smallest toy model in counterexamples.md.",
        "Try one boundary case and one relaxed-assumption counterexample search.",
        "If no route has a pattern guess, chosen central object, or proof kernel, fill IDEA_MAP.md before drafting another proof.",
        "If the route is still unclear, first do a micro pattern check; create a workstream card only if the branch is hard, repeated, tool-assisted, or literature-dependent.",
    ],
    "S2b-idea-map": [
        "Fill failure world, central object candidates, one proof kernel, candidate central lemma, and verification hook in IDEA_MAP.md.",
        "If the kernel needs invention, guess from small cases: formula, threshold, invariant, active set, tight instance, or potential; use pattern_miner.py for exact sequences and keep one holdout check.",
        "If an answer, construction, threshold, potential, hard instance, or coefficient is unknown, treat discovery as a separate step before proof.",
        "Review the current missing lemma as a good gap or bad gap before promoting it.",
        "Use nearby papers, appendices, prior ledgers, theorem families, or analogous models to extract a candidate proof architecture.",
        "Move to route portfolio only after one kernel can be proved, refuted, retrieved, tool-checked, or locally formalized.",
    ],
    "S3-route-portfolio": [
        "Before adding another route, compare it with the Attempt Fingerprint Index in WORKSTREAMS.md; run check_attempt.py only if several fingerprints or an ambiguous match make this hard.",
        "Keep a small route candidate board: 2-4 routes scored by central object, verification hook, novelty, and gap quality.",
        "Update WORKSTREAMS.md only for branches that need durable state; each active card should include a look-at-how-others-do-it pass or a skip reason.",
        "If the user approved multi-agent work, fill the Multi-Agent Dispatch Gate with disjoint artifacts before delegation.",
        "Fill Route A, Route B, and Route C statuses in LEDGER.md.",
        "Pick the route whose theorem assumptions most closely match the claim.",
    ],
    "S4-lemma-graph": [
        "Before attacking the same missing lemma again, write the route family, central object, failure witness, and new delta in WORKSTREAMS.md.",
        "Turn every nontrivial step into a blueprint node with statement deps, proof deps, downstream use, status, expected artifact, gap grade, failure diagnosis, and compact repair state.",
        "Mark OR alternatives and AND required child lemmas; attack the lowest-confidence required child before expanding another route.",
        "Merge equivalent proof states/actions before retrying: same goal, assumptions, central object, and failure witness means same state unless a new artifact exists.",
        "Prove ready leaves that feed the current assembly path first; postpone orphan lemmas unless they falsify, repair, or unlock the route.",
        "After two local attempts on a node, fill the Route Decision Check before retrying.",
        "Preserve solved nodes; if a failed node is STATEMENT_WRONG, repair/drop it and rewire dependents; if PROOF_TOO_HARD, split it into helper nodes.",
        "After failure, keep proved helper lemmas and revise only unproved or false nodes plus dependents.",
        "If a skeleton is right but a block fails, preserve the skeleton and isolate the bad block as a named lemma.",
        "For the hardest unresolved lemma, run bottleneck surgery: shrink, flip, change representation, then certify/falsify/retrieve/repair.",
        "For the hardest fragile lemma, use one-step moves: current subgoal, proposed move, expected new subgoal, check result, proof-state delta.",
        "Promote the single hardest missing step to its own lemma card.",
    ],
    "S5-local-certification": [
        "Check fragile algebra, finite cases, optimization certificates, or formalizable inequalities with tools.",
        "For Lean/API artifacts, audit `sorry`, admitted axioms, unresolved obligations, and whether verified helper lemmas assemble into the original theorem.",
        "Record the exact command/result in LEDGER.md.",
    ],
    "S6-assembly": [
        "Assemble only proved or explicitly conditional lemmas into the exact claim.",
        "Check quantifiers and boundary cases before final review.",
    ],
    "S7-adversarial-review": [
        "Attack the proof for hidden assumptions, quantifier mismatch, boundary failure, and theorem-family mismatch.",
        "Run audit_ledger.py before finalizing.",
    ],
    "S8-finalize": [
        "Write the final proof with claim status, verification status, assumptions, lemma graph, and proof pattern.",
    ],
    "S9-stuck": [
        "Name the exact obstruction in LEDGER.md.",
        "Check the Attempt Fingerprint Index in WORKSTREAMS.md; run check_attempt.py only if several fingerprints or an ambiguous match make this hard.",
        "Fill Proof-State Equivalence if the new idea has the same goal, assumptions, central object, and failure witness as a prior route.",
        "Shrink the obstruction to one proof kernel before trying another long proof route.",
        "If the proof graph has an AND bottleneck, work that required child before opening another OR route.",
        "Fill Route Decision Check in WORKSTREAMS.md: continue, repair, re-decompose, retrieve, tool-falsify, or stop-report.",
        "Rank next moves by decision value: kernel proof/refutation, counterexample, missing assumption, certificate, retrieval, representation change, or theorem repair.",
        "If a proposed move leaves the proof state unchanged, add a Failed-State Notebook entry in WORKSTREAMS.md before retrying.",
        "If no construction is visible, mine small cases for a pattern; use pattern_miner.py for exact sequences and test one holdout case before promoting the guess.",
        "Classify the current gap as good or bad; bad gaps require splitting, retrieval, falsification, or theorem repair.",
        "Use compact repair state for the bottleneck: statement, dependencies, previous attempt signature, previous feedback, and suggested fix.",
        "Before repeating proof search, inspect one to three nearby papers, appendices, prior ledgers, theorem families, or analogous models for this obstruction.",
        "If the user approved multi-agent work, split roles by artifact: planner, falsifier, retriever, formalizer/tool-checker, reviewer; do not ask several agents to write the same full proof.",
        "Create a bounded workstream card only if the next branch needs durable state.",
        "Choose one escalation method: tool falsification, retrieval, local formalization, theorem repair, or stop/report.",
        "If the block depends on modeling taste or domain intuition, ask the user for a steering hint before another heavy cycle.",
    ],
}


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def audit_text(text: str, ledger: Path) -> dict:
    missing_headings = [h for h in REQUIRED_HEADINGS if section_body(text, h) is None]
    empty_sections = [h for h in REQUIRED_HEADINGS if section_body(text, h) == ""]
    placeholders = [pat for pat in PLACEHOLDER_PATTERNS if re.search(pat, text, flags=re.M)]
    return {
        "ledger": str(ledger),
        "missing_headings": missing_headings,
        "empty_sections": empty_sections,
        "placeholder_count": len(placeholders),
        "placeholders": placeholders,
        "ready_for_final_proof": not missing_headings and not empty_sections and not placeholders,
    }


def route_from_claim(claim: str) -> list[tuple[str, int]]:
    ranked = sorted(
        [(name, score(claim.lower(), keywords)) for name, keywords in PLAYBOOKS.items()],
        key=lambda item: item[1],
        reverse=True,
    )
    selected = [(name, value) for name, value in ranked if value > 0]
    return selected or [
        ("proof-router.md", 0),
        ("strategy-scheduler.md", 0),
        ("obstruction-taxonomy.md", 0),
    ]


def is_blank_pattern_scan(project: Path) -> bool:
    path = project / "PATTERN_SCAN.md"
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8")
    filled_source = re.search(r"^- source:\s*\S+", text, flags=re.M)
    imported_move = re.search(r"^- route to add .*:\s*\S+", text, flags=re.M)
    return not (filled_source or imported_move)


def is_blank_idea_map(project: Path) -> bool:
    path = project / "IDEA_MAP.md"
    if not path.exists():
        return True
    text = path.read_text(encoding="utf-8")
    central_object = re.search(r"^- chosen central object:\s*\S+", text, flags=re.M)
    central_lemma = re.search(r"^- chosen statement:\s*\S+", text, flags=re.M)
    proof_kernel = re.search(r"^- kernel statement:\s*\S+", text, flags=re.M)
    pattern_guess = re.search(r"^- guessed object or identity:\s*\S+", text, flags=re.M)
    selected_idea = re.search(r"^- selected idea:\s*\S+", text, flags=re.M)
    return not (central_object or central_lemma or proof_kernel or pattern_guess or selected_idea)


def idea_map_need(project: Path, state: str, selected: list[tuple[str, int]], text: str) -> dict:
    reasons = []
    idea_states = {"S1-classify", "S2-stress-test", "S2b-idea-map", "S3-route-portfolio", "S9-stuck"}
    if state not in idea_states:
        return {"needed": False, "reasons": reasons}
    if not (project / "IDEA_MAP.md").exists():
        reasons.append("IDEA_MAP.md is missing")
    elif is_blank_idea_map(project):
        if state in {"S2b-idea-map", "S9-stuck"}:
            reasons.append("IDEA_MAP.md has no pattern guess, central object, proof kernel, or central lemma")
    if state == "S2b-idea-map":
        reasons.append("proof state is idea-map")
    if state == "S9-stuck":
        reasons.append("proof state is stuck")
    if selected and max(value for _, value in selected) == 0 and state in {"S1-classify", "S2-stress-test", "S3-route-portfolio"}:
        reasons.append("playbook routing is low-confidence")
    if re.search(r"central lemma:\s*$", text, flags=re.M | re.I):
        reasons.append("ledger has no central lemma recorded")
    return {"needed": bool(reasons), "reasons": reasons}


def pattern_scan_need(project: Path, state: str, selected: list[tuple[str, int]], text: str) -> dict:
    reasons = []
    scan_states = {"S1-classify", "S3-route-portfolio", "S9-stuck"}
    if not (project / "PATTERN_SCAN.md").exists() and state in scan_states:
        reasons.append("PATTERN_SCAN.md is missing")
    elif is_blank_pattern_scan(project) and state in scan_states:
        reasons.append("PATTERN_SCAN.md has no imported source or route yet")
    if state == "S9-stuck":
        reasons.append("proof state is stuck")
    if selected and max(value for _, value in selected) == 0 and state in scan_states:
        reasons.append("playbook routing is low-confidence")
    if filled_field_count(text, "obstruction type") >= 2:
        reasons.append("two or more obstruction slots are present")
    return {"needed": bool(reasons), "reasons": reasons}


def attempt_fingerprint_summary(project: Path) -> dict:
    path = project / "WORKSTREAMS.md"
    if not path.exists():
        return {"exists": False, "count": 0, "blocked_retry_count": 0, "has_real_entries": False}
    text = path.read_text(encoding="utf-8")
    index_match = re.search(
        r"## Attempt Fingerprint Index(?P<body>.*?)(?:\n## No-Repeat Decision|\Z)",
        text,
        flags=re.S,
    )
    index_text = index_match.group("body") if index_match else ""
    table_entries = 0
    for line in index_text.splitlines():
        if not line.startswith("|"):
            continue
        if "---" in line or "route family" in line.lower():
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or cells[0] == "A1" and sum(bool(cell) for cell in cells[1:]) <= 1:
            continue
        if sum(bool(cell) for cell in cells) >= 4:
            table_entries += 1
    blocked = len(re.findall(r"forbidden retry:[^\S\r\n]*\S+", text, flags=re.I))
    fingerprints = len(re.findall(r"obstruction fingerprint:[^\S\r\n]*\S+", text, flags=re.I))
    count = max(table_entries, fingerprints)
    return {
        "exists": True,
        "count": count,
        "blocked_retry_count": blocked,
        "has_real_entries": count > 0,
    }


def filled_field_count(text: str, field: str) -> int:
    return len(
        re.findall(
            rf"^(?:[-*][^\S\r\n]*)?{re.escape(field)}:[^\S\r\n]*\S+",
            text,
            flags=re.I | re.M,
        )
    )


def filled_field_values(text: str, field: str) -> list[str]:
    pattern = rf"^(?:[-*][^\S\r\n]*)?{re.escape(field)}:[^\S\r\n]*(?P<value>\S.*)$"
    return [match.group("value").strip() for match in re.finditer(pattern, text, flags=re.I | re.M)]


def looks_like_template_choice(value: str) -> bool:
    lower = value.strip().lower()
    if not lower:
        return True
    if " / " in lower:
        return True
    if lower in {"pending", "planned", "missing", "candidate", "yes", "no", "unknown"}:
        return True
    return False


def progress_evidence_summary(project: Path) -> dict:
    chunks = []
    for name in ["LEDGER.md", "IDEA_MAP.md", "WORKSTREAMS.md", "ATTACK_MATRIX.md"]:
        path = project / name
        if path.exists():
            chunks.append(path.read_text(encoding="utf-8"))
    text = "\n".join(chunks)
    unchanged = len(re.findall(r"proof-state delta:[^\S\r\n]*(unchanged|larger)", text, flags=re.I))
    unchanged += len(re.findall(r"\|[^|\n]*\|[^|\n]*\|[^|\n]*\|[^|\n]*\|[^|\n]*\|\s*(unchanged|larger)\s*\|", text, flags=re.I))
    smaller = len(re.findall(r"proof-state delta:[^\S\r\n]*smaller", text, flags=re.I))
    smaller += len(re.findall(r"\|[^|\n]*\|[^|\n]*\|[^|\n]*\|[^|\n]*\|[^|\n]*\|\s*smaller\s*\|", text, flags=re.I))
    blocked = len(
        re.findall(
            r"^(?:[-*]\s*)?(blocked retry|forbidden retry|block-repeat):\s*\S+",
            text,
            flags=re.I | re.M,
        )
    )
    evidence = 0
    for field in [
        "result",
        "external method used",
        "theorem repair, if any",
        "new evidence expected",
        "expected artifact",
        "retrieved theorem",
        "tool certificate",
        "counterexample",
        "missing assumption",
        "verified trick",
        "formalization",
    ]:
        evidence += sum(1 for value in filled_field_values(text, field) if not looks_like_template_choice(value))
    return {
        "unchanged_or_larger_moves": unchanged,
        "smaller_moves": smaller,
        "blocked_retries": blocked,
        "evidence_markers": evidence,
        "no_progress_threshold_met": unchanged >= 2 or blocked >= 1,
    }


def route_decision_summary(state: str, progress: dict, fingerprints: dict, idea_map: dict, pattern_scan: dict) -> dict:
    reasons = []
    decision = "continue"
    next_artifact = "smaller proof state or proved local lemma"

    if progress["no_progress_threshold_met"] or fingerprints["blocked_retry_count"] > 0:
        decision = "re-decompose / retrieve / tool-falsify before another prose attempt"
        next_artifact = "new helper DAG, retrieved theorem pattern, counterexample, certificate, or theorem repair"
        reasons.append("no-progress threshold or blocked retry is present")
    elif progress["smaller_moves"] > 0 and progress["unchanged_or_larger_moves"] == 0:
        decision = "continue current node with local repair"
        next_artifact = "proved local lemma or one smaller subgoal"
        reasons.append("recent proof-state evidence is shrinking")
    elif state in {"S1-classify", "S2-stress-test"} and idea_map["needed"]:
        decision = "run direct-solve or micro pattern check before proving"
        next_artifact = "named theorem/certificate, clear mismatch, or one central object"
        reasons.append("route is low-confidence but not yet in idea-map mode")
    elif state in {"S2b-idea-map", "S3-route-portfolio"} and idea_map["needed"]:
        decision = "run idea pass before proving"
        next_artifact = "central object, proof kernel, central lemma, or verification hook"
        reasons.append("proof route is not yet grounded in a kernel")
    elif pattern_scan["needed"]:
        decision = "retrieve / pattern scan before another same-style route"
        next_artifact = "theorem pattern, hidden assumption, or route repair"
        reasons.append("external pattern scan is needed for this state")
    elif state in {"S4-lemma-graph", "S5-local-certification"}:
        decision = "prove a ready leaf on the assembly path"
        next_artifact = "proved/tool-checked leaf lemma or failed-node diagnosis"
        reasons.append("proof is in local lemma/certification mode")
    elif state == "S9-stuck":
        decision = "escalate before proving"
        next_artifact = "counterexample, certificate, retrieval result, local formalization, or theorem repair"
        reasons.append("proof state is stuck")
    else:
        reasons.append("no repeated-failure signal found")

    return {
        "decision": decision,
        "next_artifact": next_artifact,
        "reasons": reasons,
    }


def external_pattern_queries(claim: str, selected: list[tuple[str, int]]) -> list[str]:
    queries = []
    for name, _ in selected[:2]:
        queries.extend(PATTERN_QUERIES.get(name, []))
    if claim:
        cleaned = " ".join(re.findall(r"[A-Za-z][A-Za-z0-9_-]+", claim))[:120]
        if cleaned:
            queries.append(f"{cleaned} proof theorem assumptions")
            queries.append(f"{cleaned} counterexample missing assumption")
    queries.extend(
        [
            "Aristotle IMO-level automated theorem proving Monte Carlo Graph Search Lean",
            "Aristotle API Lean proof sorry verified helper lemmas",
            "Rethlas Archon Matlas LeanSearch informal formal reasoning agents",
            "MA-LoT model collaboration Lean theorem proving error analysis correction",
            "MerLean Prover Planning Check Lean roles recursive proof plan",
            "Ax-Prover multi-agent Lean theorem proving MCP",
            "Goedel Architect blueprint refinement proof DAG",
            "MerLean Prover proof plan faithfulness decomposition check",
            "LeanMarathon dynamic proof DAG target fidelity",
            "LeanArchitect blueprint metadata dependency graph",
            "optimizing cost quality Lean agent routing failed trajectories",
            "AlphaProof Nexus proof sketches good gap bad gap",
            "OProver APOLLO LEAP feedback repair proof DAG",
            "Draft Sketch Prove theorem proving proof decomposition",
            "retrieval augmented theorem proving premise selection",
            "compiler guided proof repair Lean",
        ]
    )
    out = []
    seen = set()
    for query in queries:
        if query not in seen:
            seen.add(query)
            out.append(query)
    return out[:8]


def recommended_files(project: Path, routing: dict, state: str) -> list[str]:
    routing_files = list(routing.get("next_files", []))
    if state not in {"S3-route-portfolio", "S5-local-certification", "S7-adversarial-review", "S9-stuck"}:
        routing_files = [name for name in routing_files if name != "WORKSTREAMS.md"]
    state_files = {
        "S0-parse": ["claim.md", "TRIAGE.md"],
        "S1-classify": ["TRIAGE.md", "ATTACK_MATRIX.md", "PATTERN_SCAN.md", "strategy.md"],
        "S2-stress-test": ["counterexamples.md", "ATTACK_MATRIX.md", "LEDGER.md"],
        "S2b-idea-map": ["IDEA_MAP.md", "counterexamples.md", "ATTACK_MATRIX.md", "LEDGER.md"],
        "S3-route-portfolio": ["WORKSTREAMS.md", "strategy.md", "ATTACK_MATRIX.md", "PATTERN_SCAN.md", "LEDGER.md"],
        "S4-lemma-graph": ["LEMMA_QUEUE.md", "WORKSTREAMS.md", "LEDGER.md"],
        "S5-local-certification": ["TOOL_PLAN.md", "tool_checks/README.md", "WORKSTREAMS.md", "LEDGER.md"],
        "S6-assembly": ["LEDGER.md", "writeup"],
        "S7-adversarial-review": ["LEDGER.md", "counterexamples.md"],
        "S8-finalize": ["LEDGER.md", "writeup"],
        "S9-stuck": ["LEDGER.md", "WORKSTREAMS.md", "IDEA_MAP.md", "counterexamples.md", "ATTACK_MATRIX.md", "PATTERN_SCAN.md", "TOOL_PLAN.md", "trick_cards/README.md", "ESCALATION.md"],
    }
    files = state_files.get(state, ["TRIAGE.md", "LEDGER.md"]) + routing_files
    existing = []
    for name in files:
        if name not in existing and (project / name).exists():
            existing.append(name)
    return existing


def diagnose(project: Path) -> dict:
    ledger = project / "LEDGER.md"
    if not ledger.exists():
        raise SystemExit(f"LEDGER.md not found in {project}")
    text = ledger.read_text(encoding="utf-8")
    routing = read_json(project / "routing.json")
    claim = section_body(text, "Claim") or routing.get("claim", "")
    state = (section_body(text, "Proof State") or "S0-parse").splitlines()[0].strip()
    verification = (section_body(text, "Verification Status") or "conjecture").splitlines()[0].strip()
    status = (section_body(text, "Status") or "open").splitlines()[0].strip()
    selected = routing.get("selected_playbooks") or route_from_claim(claim)
    audit = audit_text(text, ledger)
    idea_map = idea_map_need(project, state, selected, text)
    pattern_scan = pattern_scan_need(project, state, selected, text)
    fingerprints = attempt_fingerprint_summary(project)
    progress = progress_evidence_summary(project)
    route_decision = route_decision_summary(state, progress, fingerprints, idea_map, pattern_scan)

    actions = []
    if not (project / "ATTACK_MATRIX.md").exists():
        actions.append("Create ATTACK_MATRIX.md with one proof route and one falsification route.")
    if not (project / "LEMMA_QUEUE.md").exists():
        actions.append("Create LEMMA_QUEUE.md as a blueprint DAG with nodes, statement deps, proof deps, downstream use, statuses, and failure diagnoses.")
    if not (project / "WORKSTREAMS.md").exists() and state in {"S3-route-portfolio", "S5-local-certification", "S7-adversarial-review", "S9-stuck"}:
        actions.append("Create WORKSTREAMS.md with approved goals, bounded workstream cards, and a look-at-how-others-do-it gate.")
    if state in {"S3-route-portfolio", "S4-lemma-graph", "S9-stuck"} and fingerprints["exists"] and not fingerprints["has_real_entries"]:
        actions.append("Fill the Attempt Fingerprint Index in WORKSTREAMS.md before trying another similar route or construction.")
    elif state in {"S3-route-portfolio", "S4-lemma-graph", "S9-stuck"} and fingerprints["has_real_entries"]:
        actions.append(f"Compare the next attempt against {fingerprints['count']} recorded attempt fingerprint(s) before proceeding.")
    if progress["no_progress_threshold_met"]:
        actions.append("No-progress threshold met: do not retry prose. Switch to counterexample search, tools, retrieval, local formalization, theorem repair, or user steering.")
    if state in {"S4-lemma-graph", "S5-local-certification", "S9-stuck"}:
        actions.append(f"Route decision: {route_decision['decision']}; expected artifact: {route_decision['next_artifact']}.")
    actions.extend(STATE_ACTIONS.get(state, STATE_ACTIONS["S9-stuck"]))
    if idea_map["needed"] and state in {"S1-classify", "S2-stress-test", "S2b-idea-map", "S3-route-portfolio", "S9-stuck"}:
        actions.append("Use IDEA_MAP.md as an optional idea pass: failure world, pattern guess, central object, proof kernel, central lemma, verification hook.")
    if idea_map["needed"] or pattern_scan["needed"]:
        actions.append("If direct solve is unavailable, mine prior papers, local drafts, appendices, or ledgers for a transferable proof architecture.")
        actions.append("Save only useful paper tricks as short local trick cards; do not promote them globally until validated or reused.")
    if (project / "ESCALATION.md").exists() and filled_field_count(text, "obstruction type") >= 2:
        actions.append("Two or more failed-route slots are present; run the escalation ladder before trying another route.")
    if audit["placeholder_count"]:
        actions.append("Fill ledger placeholders before presenting a final proof.")
    if not (project / "TOOL_PLAN.md").exists():
        actions.append("Create TOOL_PLAN.md before relying on CAS/SMT/optimization/Lean output in the proof.")
    if pattern_scan["needed"] and state in {"S1-classify", "S3-route-portfolio", "S9-stuck"}:
        actions.append("Fill PATTERN_SCAN.md with one extraction card and route scorecard before another same-style proof route.")
    if any("gate" in pat.lower() for pat in audit["placeholders"]):
        actions.append("Complete all verification gates: pre-solve, statement, assumption, negation, toy-model, pattern, lemma, proof-state, quantifier, boundary, assembly, review, progress.")
    if "S9-stuck" in state:
        actions.append("Use ESCALATION.md before another prose proof attempt; record the external method and result in LEDGER.md.")
        actions.append("Name the smallest missing lemma or false condition, then switch route or repair the theorem.")

    files = recommended_files(project, routing, state)
    if idea_map["needed"] and (project / "IDEA_MAP.md").exists() and "IDEA_MAP.md" not in files:
        files.insert(0, "IDEA_MAP.md")

    return {
        "project": str(project),
        "claim": claim,
        "status": status,
        "verification_status": verification,
        "proof_state": state,
        "selected_playbooks": selected,
        "recommended_files": files,
        "next_actions": actions[:8],
        "idea_map": idea_map,
        "external_pattern_scan": {
            **pattern_scan,
            "queries": external_pattern_queries(claim, selected) if pattern_scan["needed"] else [],
            "scorecard_fields": [
                "route",
                "retrieved premise or theorem",
                "evidence type",
                "dependency value",
                "certificate availability",
                "failure risk",
                "next experiment",
            ],
        },
        "attempt_fingerprints": fingerprints,
        "progress_evidence": progress,
        "route_decision": route_decision,
        "audit": audit,
    }


def print_human(result: dict) -> None:
    print(f"project: {result['project']}")
    print(f"state: {result['proof_state']}")
    print(f"status: {result['status']} / {result['verification_status']}")
    print("selected playbooks:")
    for name, value in result["selected_playbooks"]:
        print(f"- {name} (score {value})")
    print("recommended files:")
    for name in result["recommended_files"]:
        print(f"- {name}")
    print("next actions:")
    for action in result["next_actions"]:
        print(f"- {action}")
    idea = result["idea_map"]
    if idea["needed"]:
        print("idea map:")
        for reason in idea["reasons"]:
            print(f"- reason: {reason}")
    scan = result["external_pattern_scan"]
    if scan["needed"]:
        print("external pattern scan:")
        for reason in scan["reasons"]:
            print(f"- reason: {reason}")
        for query in scan["queries"][:5]:
            print(f"- query: {query}")
    fingerprints = result["attempt_fingerprints"]
    if fingerprints["exists"]:
        print("attempt fingerprints:")
        print(f"- count: {fingerprints['count']}")
        print(f"- blocked retries: {fingerprints['blocked_retry_count']}")
    progress = result["progress_evidence"]
    print("progress evidence:")
    print(f"- unchanged_or_larger_moves: {progress['unchanged_or_larger_moves']}")
    print(f"- smaller_moves: {progress['smaller_moves']}")
    print(f"- blocked_retries: {progress['blocked_retries']}")
    print(f"- evidence_markers: {progress['evidence_markers']}")
    route = result["route_decision"]
    print("route decision:")
    print(f"- decision: {route['decision']}")
    print(f"- next_artifact: {route['next_artifact']}")
    for reason in route["reasons"]:
        print(f"- reason: {reason}")
    print(f"ready_for_final_proof: {result['audit']['ready_for_final_proof']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Diagnose the next move for a theory proof project.")
    parser.add_argument("project", help="Proof project directory containing LEDGER.md")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    args = parser.parse_args()

    result = diagnose(Path(args.project))
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print_human(result)


if __name__ == "__main__":
    main()
