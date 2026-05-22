# Proof Escalation Protocol

Use this when a hard proof fails, repeats the same obstruction, or risks turning into polished but unsupported prose.

## Trigger

Escalate when any of these occurs:

- the same obstruction survives two proof cycles;
- two distinct proof routes fail without shrinking the missing lemma;
- a tool check, toy model, or boundary case contradicts a proof step;
- the current proof needs an unstated assumption;
- the user has asked the same theorem before and it remained unresolved.

## Escalation Ladder

Move upward only after recording the result in `LEDGER.md`.

1. Local reroute:
   - name the obstruction using `obstruction-taxonomy.md`;
   - shrink the target to the proof kernel: the smallest missing lemma, certificate, or counterexample barrier;
   - switch theorem family using `strategy-scheduler.md`.
2. Tool falsification:
   - write the negation explicitly;
   - search smallest finite, scalar, two-action, two-type, one-period, or boundary examples;
   - use Wolfram/SymPy for algebraic signs and rates;
   - use Python/Z3/CVXPy/Sage/OR-Tools for finite constraints, LP certificates, graph checks, or small MDPs.
3. Retrieval:
   - search the relevant playbook, prior ledgers, local paper text, theorem names, and formal libraries;
   - if network is allowed or the user asks for current literature, search papers/books/docs for the nearest theorem pattern;
   - record the retrieved theorem name and assumptions before using it.
4. Local formalization:
   - formalize only the fragile local lemma, not the whole research theorem by default;
   - use Lean/mathlib for quantifier-sensitive algebra, order, convexity, or probability lemmas when feasible;
   - if Lean is too costly, write a pseudo-formal lemma card with exact inputs and outputs.
5. Theorem repair:
   - if a counterexample exists, mark the original claim `refuted`;
   - otherwise propose the weakest extra assumption or weaker conclusion that makes the lemma true;
   - ask the user only when the repair changes the economic/modeling meaning.
6. Stop/report:
   - return `still open` rather than a fake proof;
   - report the exact obstruction, failed routes, attempted tools, and next bounded experiment.

## Domain Escalations

- DP/MDP/Bellman: after a failed monotonicity proof, test Q-value single crossing on finite grids; check boundary states, tie-breaking, transient/recurrent classes, and beta -> 1. Escalate to Bellman inequality certificates or theorem repair before claiming threshold optimality.
- Mechanism design/econ: after IC/IR failure, encode finite type deviations; check envelope/cyclic monotonicity and boundary IR. Escalate to payment feasibility LP or weaker implementability conditions.
- Learning theory/bandits: after a regret/concentration route fails, separate confidence event, instantaneous regret, summation lemma, and failure-event contribution. Escalate to toy distributions or known concentration theorem retrieval.
- OR/optimization: after FOC/KKT failure, check convexity/concavity and constraint qualification. Escalate to dual certificate, subgradient/case split, or counterexample search.
- Games/matching: after fixed-point or stability failure, check compactness/continuity/upper hemicontinuity, then finite game or blocking-pair examples.
- Lower bounds: after a hard-instance route fails, compute KL/TV explicitly on the smallest pair before moving to Fano/Assouad.

## Required Ledger Entry

For each escalation, record:

- trigger:
- failed route:
- obstruction:
- smaller lemma or negation:
- external method used:
- result:
- theorem repair, if any:
- next bounded move:

## Final Answer Rule

If escalation does not prove or refute the claim, the answer must say `still open` or `lemma-conditional`. It may include a proof skeleton, but must mark every unproved key lemma.
