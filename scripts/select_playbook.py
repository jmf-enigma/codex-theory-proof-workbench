import argparse
import json
import re


PLAYBOOKS = {
    "dp-proof-playbook.md": [
        "dynamic programming", "dynamic program", "dp", "bellman", "mdp", "markov decision",
        "value function", "policy iteration", "value iteration", "optimal policy",
        "optimal stopping", "threshold policy", "threshold structure", "monotone policy", "index policy", "indexability",
        "average cost", "discounted", "finite horizon", "infinite horizon",
        "post-decision", "queue", "inventory", "stochastic control",
        "bellman equation", "bellman inequality", "q-value", "q function",
        "contraction mapping", "span seminorm", "relative value", "bias function",
    ],
    "optimization-or-playbook.md": [
        "kkt", "duality", "convex", "linear program", "lp", "scheduling", "or/ms",
        "subgradient", "lagrangian", "complementary slackness", "slater",
        "exchange argument", "primal-dual", "total unimodularity", "relaxation gap",
    ],
    "mechanism-design-playbook.md": [
        "mechanism", "ic", "ir", "dsic", "bic", "auction", "myerson", "payment",
        "envelope", "cyclic monotonicity", "virtual value", "truthful",
        "incentive compatible", "individual rationality", "screening", "ironing",
        "allocation rule", "single crossing", "revelation principle", "implementable",
        "rochet", "bayesian persuasion", "contract", "principal agent",
    ],
    "games-matching-playbook.md": [
        "nash", "equilibrium", "game", "matching", "stable", "deferred acceptance",
        "price of anarchy", "supermodular", "potential game", "strategy-proof",
        "kakutani", "glicksberg", "tarski", "best response", "blocking pair",
        "market design", "matching with contracts", "smoothness", "lattice",
    ],
    "learning-theory-playbook.md": [
        "generalization", "vc", "rademacher", "pac", "stability", "uniform convergence",
        "sample complexity", "excess risk", "sgd", "online-to-batch",
        "covering number", "metric entropy", "symmetrization", "contraction",
        "pac-bayes", "mcdiarmid", "azuma", "freedman", "classification",
        "regression", "erm", "statistical learning", "fast rate", "localized",
    ],
    "bandits-oco-playbook.md": [
        "bandit", "ucb", "thompson", "regret", "linucb", "oful", "exp3", "hedge",
        "online learning", "oco", "ftrl", "omd", "elliptical potential",
        "linear bandit", "contextual bandit", "self-normalized", "confidence ellipsoid",
        "optimism", "upper confidence", "adversarial bandit", "importance-weighted",
        "mirror descent", "bregman", "doubling trick", "gap-free", "gap dependent",
    ],
    "lower-bounds-playbook.md": [
        "lower bound", "minimax", "fano", "assouad", "le cam", "kl", "impossibility",
        "change of measure", "hard instance", "pinsker", "testing", "two-point",
        "packing", "covering", "oracle lower bound", "resisting oracle",
        "information bottleneck", "bretagnolle", "bayes risk",
    ],
    "probabilistic-method-playbook.md": [
        "probabilistic method", "random construction", "random coloring", "bad event",
        "bad events", "lovasz local lemma", "local lemma", "lll", "moser tardos",
        "dependency graph", "lopsided", "alteration", "union bound too loose",
        "hypergraph coloring", "erdos lovasz", "erdos-faber-lovasz",
        "satisfiability", "resampling", "monochromatic", "latin transversal",
    ],
}


def score(text: str, keywords: list[str]) -> int:
    total = 0
    for kw in keywords:
        if re.search(r"\b" + re.escape(kw) + r"\b", text):
            total += 2 if " " in kw else 1
    return total


def main() -> None:
    parser = argparse.ArgumentParser(description="Suggest theory proof workbench playbooks.")
    parser.add_argument("claim", nargs="+", help="Claim or topic text")
    args = parser.parse_args()
    text = " ".join(args.claim).lower()
    ranked = sorted(
        [(name, score(text, kws)) for name, kws in PLAYBOOKS.items()],
        key=lambda item: item[1],
        reverse=True,
    )
    selected = [name for name, value in ranked if value > 0]
    if not selected:
        selected = ["proof-router.md", "strategy-scheduler.md", "obstruction-taxonomy.md"]
    print(json.dumps({"selected": selected, "scores": dict(ranked)}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
