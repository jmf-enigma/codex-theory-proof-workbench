# Learning Theory Playbook

Use for generalization, uniform convergence, VC/Rademacher bounds, stability, PAC-Bayes, SGD-style convergence, and online-to-batch conversion.

## Branch Split

- Finite class: concentration for fixed hypothesis plus union bound.
- Infinite class: symmetrization, Rademacher complexity, covering number, VC dimension, or contraction.
- Stability: compare neighboring samples and bound generalization by stability.
- PAC-Bayes: choose prior/posterior, KL term, change of measure.
- Optimization-to-generalization: split excess risk into estimation plus optimization error.
- Online-to-batch: convert regret to expected/statistical risk.

## Smart Routes

- Uniform claim from pointwise concentration: add union bound, covering, VC, or Rademacher step.
- Adaptive/algorithm-dependent hypothesis: condition on sample carefully; use stability or PAC-Bayes.
- Bound too loose: replace union bound with Rademacher/contraction or localized complexity.
- High-probability missing: track failure probability and union over all events.
- SGD proof stuck: separate optimization descent lemma from stochastic noise martingale.

## Common Lemmas

- Symmetrization.
- Massart finite class lemma.
- Sauer-Shelah growth bound.
- Rademacher contraction.
- McDiarmid/Azuma/Freedman concentration.
- Stability generalization lemma.

## Counterexample Tests

- Infinite class without capacity control.
- Unbounded loss.
- Data-dependent class chosen after seeing sample.
- Expectation result incorrectly stated as high probability.
- Non-iid samples.

## Tool Hooks

- Python simulations for toy distributions.
- Wolfram/SymPy for optimizing rates over epsilon/net size.
- Lean for elementary inequalities if useful.
