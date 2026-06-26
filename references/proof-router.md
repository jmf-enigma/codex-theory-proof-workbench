# Proof Router

Use this file to classify a hard proof before attempting it.

## Target To Pattern

- Existence of optimizer/equilibrium: Weierstrass, Berge maximum theorem, Brouwer, Kakutani, Tarski, contraction, measurable selection.
- Uniqueness: strict concavity/convexity, contraction, single crossing, diagonal strict concavity, strong monotonicity.
- Comparative statics: increasing differences, single crossing, supermodularity, Topkis, Milgrom-Shannon.
- Optimality in OR/MS: KKT, Lagrangian duality, LP duality, complementary slackness, exchange argument, dynamic programming.
- Mechanism design IC/IR: monotone allocation, envelope theorem, payment identity, cyclic monotonicity, revenue equivalence, ironing.
- Game theory: fixed point, potential function, supermodular game, no-regret to equilibrium, smoothness/price of anarchy.
- Matching/market design: blocking pair contradiction, deferred acceptance invariant, lattice of stable matchings, strategy-proofness.
- Learning generalization: uniform convergence, VC/Rademacher, stability, online-to-batch, PAC-Bayes.
- Stochastic bandit regret: confidence event, optimism, regret decomposition, gap-dependent/gap-free split.
- Linear/contextual bandit: ridge confidence ellipsoid, self-normalized martingale, elliptical potential.
- Adversarial bandit/OCO: potential argument, exponential weights, FTRL/OMD, Bregman divergence.
- Lower bound: Le Cam, Fano, Assouad, change of measure, KL decomposition, hard instance construction.
- Probabilistic existence: random construction, bad-event family, union bound, alteration, Lovasz Local Lemma, dependency graph, lopsided LLL, Moser-Tardos resampling.

## Stuck Signal To Next Move

- Algebra will not simplify: use Wolfram/SymPy; check domains and zero denominators.
- FOC argument fails at boundary: switch to KKT or subgradient conditions.
- Monotonicity claim feels intuitive but not derivable: check increasing differences/single crossing; search for counterexample.
- IC proof has many pairwise constraints: try envelope theorem for one-dimensional types or cyclic monotonicity for multidimensional types.
- Regret proof loses a log or dimension factor: isolate confidence event, decomposition, and summation lemma.
- Lower bound has no hard instance: choose two nearby instances and compute KL; if multi-hypothesis, try Fano/Assouad.
- Union bound too loose in an existence proof: define bad events and a dependency graph; try Lovasz Local Lemma, lopsided LLL, or alteration.
- Equilibrium existence proof handwaves continuity/compactness: audit correspondence properties and apply the correct fixed point theorem.

## Source Map

- Convex optimization and duality: Boyd-Vandenberghe, Convex Optimization.
- Mechanism design and algorithmic game theory: Roughgarden, Twenty Lectures on Algorithmic Game Theory; Nisan-Roughgarden-Tardos-Vazirani, Algorithmic Game Theory; Hartline, mechanism design notes.
- Comparative statics: Topkis; Milgrom-Shannon monotone comparative statics.
- Learning theory: Shalev-Shwartz and Ben-David, Understanding Machine Learning.
- Bandits: Lattimore-Szepesvari, Bandit Algorithms; Bubeck-Cesa-Bianchi, Regret Analysis.
- Online learning/OCO: Hazan, Introduction to Online Convex Optimization.
- Probabilistic method: Alon-Spencer, The Probabilistic Method; Moser-Tardos constructive Lovasz Local Lemma.
