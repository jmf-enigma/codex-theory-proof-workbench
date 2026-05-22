# Bandits And Online Learning Playbook

Use for stochastic/adversarial bandits, contextual/linear bandits, online convex optimization, Hedge/EXP3, FTRL/OMD, and regret proofs.

## Branch Split

- Stochastic finite-arm UCB: confidence event, optimism, pull-count bound, failure event.
- Gap-free regret: split small-gap and large-gap arms; optimize threshold.
- Thompson sampling: posterior concentration or information ratio.
- Linear/contextual bandit: ridge estimator, confidence ellipsoid, optimism, elliptical potential.
- Adversarial bandit: unbiased loss estimator, exponential weights potential, variance control.
- OCO: OGD/FTRL/OMD one-step inequality and telescoping Bregman divergence.

## Smart Routes

- Regret decomposition unclear: write instantaneous regret under good event first.
- Missing uniformity: make confidence event uniform over arms/time/actions.
- Linear bandit stuck: isolate self-normalized concentration and elliptical potential as separate lemmas.
- EXP3 variance explodes: track importance-weighted estimator and exploration probability.
- OCO proof stuck: choose regularizer that makes telescoping clean.
- Unknown horizon: doubling trick or time-varying learning rate.

## Common Lemmas

- Hoeffding/Bernstein/Freedman confidence event.
- Peeling/union bound over time.
- Self-normalized martingale inequality.
- Elliptical potential lemma.
- Hedge log-potential bound.
- OGD/FTRL/OMD regret lemma.

## Counterexample Tests

- One optimal and one near-optimal arm.
- Zero gap vs positive gap.
- Adaptive context sequence.
- Loss estimates with tiny action probability.
- Comparator outside feasible set.

## Tool Hooks

- Python for small simulations and summation checks.
- Wolfram/SymPy for rate optimization and algebra.
- Lean for telescoping/elementary inequalities when local.
