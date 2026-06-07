# Codex Theory Proof Workbench

A Codex skill for hard theoretical proof discovery, proof debugging, and failed-proof recovery.

It helps Codex stop looping on the same missing lemma. The workbench preserves the exact theorem statement, searches for proof ideas with falsification and small cases, tracks failed routes, uses tools only for checkable artifacts, and stops with `still open` or `lemma-conditional` rather than producing a polished unsupported proof.

## Best For

- Operations research and management science proofs.
- Mechanism design, economic theory, IC/IR, envelope, and cyclic-monotonicity arguments.
- Dynamic programming, MDPs, threshold policies, and Bellman certificates.
- Learning theory, bandits, online learning, regret, and lower bounds.
- Proofs that have already failed once and need memory rather than another restart.

For polishing, rewriting, LaTeX cleanup, or making an already complete proof easier to read, use a proof-writing skill instead. This repository is about proof discovery and proof control.

## Install

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git ~/.codex/skills/theory-proof-workbench
```

Restart Codex or refresh skill discovery if needed. The skill name is:

```text
theory-proof-workbench
```

## Quick Start

Lightweight idea pass:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

Start a hard or repeatedly failed proof project:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

Diagnose an existing proof project:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

Audit a proof ledger before claiming a final proof:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

## What The Skill Adds

| Problem in hard proofs | Workbench response |
| --- | --- |
| The proof silently changes the theorem | Statement-fidelity and theorem-repair gates |
| The same route keeps returning | Attempt fingerprints and no-repeat decisions |
| The key construction is unknown | Small-case discovery, pattern mining, tight-case search |
| A lemma hides the whole theorem | Good-gap / bad-gap review |
| Tools produce numbers but not proof | Artifact-first tool plans |
| The proof gets stuck after several tries | Route decision: continue, repair, re-decompose, retrieve, tool-check, or stop |

## Core Workflow

The default spine is deliberately small:

1. State the exact theorem, variables, domains, quantifiers, and assumptions.
2. Check statement fidelity and whether a direct theorem or certificate already solves it.
3. Choose the lightest mode: direct, micro-check, light-idea, project, or recovery.
4. Try to falsify the claim with small, finite, boundary, and relaxed-assumption cases.
5. If needed, discover the central object, proof kernel, or missing construction.
6. For hard proofs, compare a small portfolio of genuinely different routes.
7. Build a blueprint lemma graph with statement deps, proof deps, downstream use, and node statuses.
8. Prove ready leaves on the current theorem path before side lemmas.
9. After repeated local failure, make a route decision before another attempt.
10. Assemble, adversarially review, and report the final proof status.

## Proof Project Files

`start_proof.py` creates a structured workspace:

| File | Purpose |
| --- | --- |
| `TRIAGE.md` | Mode decision and immediate next steps |
| `WORKSTREAMS.md` | Attempt fingerprints, bounded workstream cards, route decisions |
| `IDEA_MAP.md` | Central objects, proof kernels, construction search, one-step moves |
| `ATTACK_MATRIX.md` | Proof, falsification, and alternate route candidates |
| `LEMMA_QUEUE.md` | Blueprint lemma graph with statement deps, proof deps, downstream use, statuses |
| `PATTERN_SCAN.md` | Bounded extraction from papers, ledgers, formalization projects, or proof-agent workflows |
| `TOOL_PLAN.md` | Expected artifacts before CAS, SMT, optimization, Wolfram, Python, Sage, or Lean checks |
| `LEDGER.md` | Persistent proof state, failed routes, verification gates, and current obstruction |
| `ESCALATION.md` | Next moves after repeated failure |

## Route Decisions

When a proof fails locally, the next move must have decision value. A retry is allowed only if it brings a new artifact:

- a proved or refuted kernel lemma;
- a counterexample, boundary case, or missing assumption;
- a checked algebra identity, finite model, LP/SMT result, or local Lean formalization;
- a different central object, invariant, potential, hard instance, dual, envelope, coupling, or Bellman gap;
- a retrieved theorem pattern or paper trick with assumptions and a verification hook;
- an honest theorem repair.

If none of these is expected, the workbench routes away from prose proof and toward retrieval, tools, counterexample search, theorem repair, user steering, or `still open`.

## Optional Wolfram Support

The skill can use Wolfram through the local `wmath`/`codex-wmath` wrapper when the companion `math-tools` skill is installed. Wolfram is optional, but useful for symbolic algebra, inequality checks, condition discovery, quantifier elimination, FOC/KKT algebra, Bellman/Q-value differences, envelope derivatives, and small counterexample searches.

Install the backend from Wolfram's official pages:

- [Wolfram Engine](https://www.wolfram.com/engine/) and [Wolfram Engine FAQ](https://www.wolfram.com/engine/faq/).
- [Install WolframScript](https://reference.wolfram.com/language/workflow/InstallWolframScript.html.en), if your setup needs the command-line script interface.
- Wolfram support note on selecting a kernel path for `wolframscript`: [How do I specify which kernel wolframscript should use?](https://support.wolfram.com/47243/).

Verify:

```bash
wolframscript -code '2+2'
codex-wmath '2+2'
wmath '2+2'
```

For proof work, prefer queries that produce checkable artifacts:

```bash
codex-wmath 'ExportString[With[{s = FullSimplify[x^2 >= 0, Element[x, Reals]]}, <|"verified" -> TrueQ[s], "result" -> ToString[s, InputForm]|>], "RawJSON"]'
```

Treat Wolfram output as evidence, not as the final proof. A useful result should become a named lemma, condition, counterexample, certificate, or theorem repair in the proof ledger.

## Proof Statuses

| Status | Meaning |
| --- | --- |
| `conjecture` | Intuition or pattern match only |
| `counterexample-tested` | No counterexample found in bounded searches |
| `lemma-conditional` | Final theorem depends on named missing lemmas |
| `human-proof` | Every nontrivial step is justified in prose |
| `tool-checked` | Fragile algebra or constraints were checked by tools |
| `formalized-local` | Key local lemmas were checked in Lean or another formal system |
| `formalized-complete` | Full theorem is machine-formalized |

Do not call a result proved if the key lemma is only guessed.

## Repository Layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── dp-proof-playbook.md
│   ├── mechanism-design-playbook.md
│   ├── learning-theory-playbook.md
│   ├── bandits-oco-playbook.md
│   └── ...
└── scripts/
    ├── start_proof.py
    ├── proof_doctor.py
    ├── audit_ledger.py
    ├── pattern_miner.py
    └── ...
```

## Development Checks

Validate the skill structure:

```bash
codex-math-python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Compile scripts:

```bash
PYTHONPYCACHEPREFIX=/tmp/codex-pycache codex-math-python -m py_compile scripts/*.py
```

Run a smoke test:

```bash
codex-math-python scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## Research Influences

The workflow is inspired by practical patterns from proof-agent and formalization work: Draft-Sketch-Prove, premise retrieval, compiler-guided repair, blueprint-style dependency graphs, cost-aware theorem-prover routing, LeanArchitect, LeanMarathon, and AI co-mathematician workstreams. The skill imports these as lightweight control rules rather than as a mandatory heavy process.

## License

MIT License. See [LICENSE](LICENSE).

---

# Codex 理论证明工作台

这是一个用于困难理论证明的 Codex skill，服务于证明思路发现、失败证明调试和 proof recovery。

它的核心目标很简单：让 Codex 不要在同一个 missing lemma 上反复换说法。这个 workbench 会保持原命题不漂移，先尝试反驳和寻找小例子，记录失败路线，只在工具输出能转化成可检查 artifact 时使用工具，并在关键 lemma 没证明时明确返回 `still open` 或 `lemma-conditional`。

## 适合什么问题

- 运筹、管理科学、优化、排队、库存、调度等理论证明。
- 机制设计、经济理论、IC/IR、envelope、cyclic monotonicity。
- DP、MDP、threshold policy、Bellman certificate。
- Learning theory、bandits、online learning、regret、lower bounds。
- 已经失败过的证明，需要记忆、拆解和恢复，而不是从头再试。

如果核心证明已经完成，只需要润色、改写、LaTeX 化或提升可读性，应使用 proof-writing skill。这个仓库关注的是证明发现和证明控制。

## 安装

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git ~/.codex/skills/theory-proof-workbench
```

如有需要，重启 Codex 或刷新 skill discovery。skill 名称是：

```text
theory-proof-workbench
```

## 快速开始

轻量寻找证明思路：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

创建困难证明项目：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

诊断已有证明项目：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

最终证明前检查 ledger：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

## 它解决什么

| 困难证明里的问题 | Workbench 的做法 |
| --- | --- |
| 证明偷偷改了 theorem | Statement-fidelity 和 theorem-repair gates |
| 同一条路线反复失败 | Attempt fingerprints 和 no-repeat decisions |
| 关键构造不知道是什么 | 小例子、pattern mining、tight-case search |
| 一个 lemma 其实藏了整个 theorem | Good-gap / bad-gap review |
| 工具只给了数值现象 | Artifact-first tool plans |
| 局部证明失败多次 | Route decision：继续、修复、重拆、检索、工具检查或停止 |

## 核心流程

默认主线是：

1. 写清 theorem statement、variables、domains、quantifiers 和 assumptions。
2. 检查 statement fidelity，以及是否有直接 theorem 或 certificate。
3. 选择最轻的模式：direct、micro-check、light-idea、project 或 recovery。
4. 用 small、finite、boundary 和 relaxed-assumption cases 尝试反驳命题。
5. 必要时寻找 central object、proof kernel 或 missing construction。
6. 对困难证明，比较几条真正不同的 proof routes。
7. 构建 blueprint lemma graph，区分 statement deps、proof deps、downstream use 和 node status。
8. 优先证明当前 theorem path 上的 ready leaves，而不是证明没有下游用途的 side lemmas。
9. 局部失败重复后，先做 route decision，再决定是否继续。
10. 最后 assemble、adversarial review，并报告 proof status。

## Proof Project 文件

`start_proof.py` 会创建一个结构化 proof workspace：

| 文件 | 用途 |
| --- | --- |
| `TRIAGE.md` | Mode decision 和立即要做的步骤 |
| `WORKSTREAMS.md` | Attempt fingerprints、bounded workstream cards、route decisions |
| `IDEA_MAP.md` | Central objects、proof kernels、construction search、one-step moves |
| `ATTACK_MATRIX.md` | Proof routes、falsification routes、alternative routes |
| `LEMMA_QUEUE.md` | Blueprint lemma graph，含 statement deps、proof deps、downstream use、statuses |
| `PATTERN_SCAN.md` | 从论文、旧 ledgers、formalization projects 或 proof-agent workflows 中提取结构 |
| `TOOL_PLAN.md` | 运行 CAS、SMT、optimization、Wolfram、Python、Sage 或 Lean 前写清 expected artifacts |
| `LEDGER.md` | 持久化 proof state、失败路线、verification gates 和当前 obstruction |
| `ESCALATION.md` | 重复失败后的下一步 |

## Route Decision

一次 retry 必须带来新 artifact，例如：

- proved/refuted kernel lemma；
- counterexample、boundary case 或 missing assumption；
- checked algebra identity、finite model、LP/SMT result 或 local Lean formalization；
- 新的 central object、invariant、potential、hard instance、dual、envelope、coupling 或 Bellman gap；
- 带 assumptions 和 verification hook 的 theorem pattern 或 paper trick；
- 诚实的 theorem repair。

如果没有这些，workbench 会从 prose proof 切到 retrieval、tools、counterexample search、theorem repair、user steering，或直接报告 `still open`。

## 可选 Wolfram 支持

如果同时安装了 `math-tools` skill，这个 workbench 可以通过本地 `wmath`/`codex-wmath` wrapper 调用 Wolfram。Wolfram 不是必须的，但适合 symbolic algebra、inequality checks、condition discovery、quantifier elimination、FOC/KKT algebra、Bellman/Q-value difference、envelope derivatives 和小型 counterexample search。

安装后验证：

```bash
wolframscript -code '2+2'
codex-wmath '2+2'
wmath '2+2'
```

证明任务里优先让 Wolfram 输出可检查 artifact，而不是直接把 Wolfram 输出当作最终证明。

## Proof Status

| 状态 | 含义 |
| --- | --- |
| `conjecture` | 只是直觉或 pattern match |
| `counterexample-tested` | 在有限搜索中没有找到反例 |
| `lemma-conditional` | 最终 theorem 依赖明确列出的 missing lemmas |
| `human-proof` | 每个非平凡步骤都有文字证明或引用 |
| `tool-checked` | 脆弱代数或 constraints 已经由工具检查 |
| `formalized-local` | 关键 local lemmas 已经由 Lean 或其他 formal system 检查 |
| `formalized-complete` | 完整 theorem 已经 machine-formalized |

如果关键 lemma 只是猜出来的，不要把结果称为 proved。

## 开发检查

```bash
codex-math-python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONPYCACHEPREFIX=/tmp/codex-pycache codex-math-python -m py_compile scripts/*.py
codex-math-python scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## 许可证

MIT License。详见 [LICENSE](LICENSE)。
