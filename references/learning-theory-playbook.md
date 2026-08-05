# Learning Theory Playbook

Use for generalization, empirical processes, uniform convergence, VC/Rademacher bounds, stability, PAC-Bayes, statistical learning rates, SGD-style convergence, and online-to-batch conversion.

## Semantic Audit

Freeze the result's probability mode before choosing a proof:

- pointwise, uniform, almost sure, in probability, in expectation, high probability, or in `Lp`;
- fixed or data-dependent function class, including which sigma-field makes it measurable;
- bounded, sub-Gaussian, sub-exponential, or finite-moment loss/noise;
- measurability or separability of suprema, integrability of envelopes, and any continuity or total-boundedness assumption;
- every interchange of supremum, expectation, integral, conditional expectation, or limit.

Do not silently upgrade expectation to high probability, pointwise to uniform, or a fixed-class argument to an adaptively chosen class.

## Branch Split

- Finite class: fixed-hypothesis concentration plus a union bound.
- Infinite class: symmetrization, Rademacher/Gaussian complexity, covering number, VC dimension, contraction, or chaining.
- Localized excess risk: basic inequality, localized class, concentration plus capacity, critical radius, then fixed-point closure.
- Stability: compare neighboring samples and translate stability into generalization.
- PAC-Bayes: choose prior/posterior, apply change of measure, and track the KL and confidence terms.
- Optimization-to-generalization: separate estimation, approximation, and optimization errors.
- Online-to-batch: specify averaging, convexity, filtration, and whether the conclusion is expected or high probability.

## Localized Empirical-Process Route

1. Derive the basic inequality for excess risk or estimation error.
2. Define the localized class by the metric or risk quantity the inequality actually controls.
3. Bound stochastic fluctuations by concentration and a capacity measure.
4. Solve the critical-radius or fixed-point inequality with constants and monotonicity stated.
5. Prove the estimator lies in the localized region, then close the self-consistent bound.

If the fixed point does not close, check curvature/Bernstein conditions, star-shapedness, the localization metric, and whether the capacity bound is global when a local one is required.

## Chaining Route

1. Choose multiscale nets in the correct metric and verify total boundedness.
2. Write a telescoping chain from coarse projections to the target process.
3. Control each increment at its scale and allocate failure probability across scales.
4. Sum entropy terms or justify the entropy integral.
5. Control the terminal remainder using continuity, separability, or an explicit approximation limit.

A finite-net proof is incomplete if the limit to the full class lacks measurability, path continuity, integrability, or a vanishing remainder.

## Smart Routes

- Uniform claim from pointwise concentration: add a union bound, covering argument, VC step, symmetrization, or Rademacher route.
- Adaptive or algorithm-dependent hypothesis: condition on the right history; use stability, PAC-Bayes, sequential complexity, or a martingale argument.
- Bound too loose: replace a global union bound with contraction, localization, peeling, or chaining.
- SGD proof stuck: separate deterministic descent, bias, and stochastic-noise martingale terms.
- Persistent formal or algebraic failure: audit the theorem statement and construct the smallest distribution/class counterexample before rewriting the proof again.

## Common Lemmas

- Symmetrization and ghost samples.
- Massart finite-class lemma and Sauer-Shelah growth bound.
- Rademacher contraction and comparison inequalities.
- McDiarmid, Azuma, Freedman, Bernstein, and self-normalized concentration.
- Stability generalization and PAC-Bayes change of measure.
- Peeling, covering-to-chaining, and critical-radius fixed-point lemmas.

## Counterexample Tests

- Infinite class without capacity control or measurability.
- Unbounded loss without a tail or moment condition.
- Data-dependent class treated as fixed after seeing the sample.
- Expectation result stated as high probability, or pointwise convergence stated uniformly.
- Non-iid or adaptively sampled data passed through an iid lemma.
- Supremum, expectation, or limit exchanged without domination, uniform integrability, tightness, or continuity.

## Tool Hooks

- Python simulations for toy distributions and counterexample search.
- Wolfram/SymPy for exact rate optimization over confidence, net scale, or critical radius.
- Lean for stable local inequalities after the probability semantics and imported infrastructure are fixed.

The semantic and formalization checks are informed by the [AI4SLT case study](https://arxiv.org/abs/2602.02285). Its project-specific workflow results do not establish a general theorem-proving success rate.
