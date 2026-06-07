# Codex Theory Proof Workbench

A Codex skill for hard theoretical proof discovery, proof debugging, and failed-proof recovery.

This skill is designed for research problems in operations research, management science, mechanism design, economic theory, dynamic programming, learning theory, bandits, online learning, optimization, games, incentive compatibility, regret analysis, and lower bounds.

It is not a theorem database and it is not a proof-polishing tool. It is a proof-control workflow. Its purpose is to help Codex preserve the exact theorem statement, search for the right proof idea, avoid repeating failed routes, and turn partial attempts into reusable evidence.

## Why This Exists

Hard proofs often fail for reasons that are not visible from the final polished argument. A proposed proof may silently strengthen an assumption, prove a nearby theorem, ignore a boundary case, or loop around the same missing lemma under new notation. This skill makes those failure modes explicit.

The workbench encourages Codex to:

- state the theorem precisely before proving it;
- test whether the claim is false before trying to prove it;
- isolate the smallest proof kernel that would decide the route;
- record failed routes and unchanged proof states;
- use tools only when their outputs become checkable mathematical artifacts;
- stop with `still open` or `lemma-conditional` rather than present a polished but unsupported proof.

## Core Capabilities

- **Proof routing**: classify the target by theorem family and proof pattern.
- **Assumption audit**: check quantifiers, domains, compactness, convexity, continuity, measurability, boundedness, independence, tie-breaking, and boundary cases.
- **Statement-fidelity audit**: catch translation errors, implicit conventions, missing boundary cases, and formal/informal mismatch before proof search.
- **Falsification first**: search small, finite, boundary, and relaxed-assumption cases before committing to a proof route.
- **Blueprint lemma graphing**: split the theorem into a dependency graph of definitions, lemmas, and final assembly nodes, with declared parents, statuses, and failure diagnoses.
- **Gap grading**: distinguish good gaps that can be deferred as lemmas from bad gaps that hide the core proof idea.
- **No-repeat memory**: fingerprint repeated constructions, failed routes, missing assumptions, and unchanged proof states.
- **Progress contract**: require a retry to bring new evidence rather than a rewritten version of the same missing lemma.
- **Divergence before convergence**: compare proof, falsification, and orthogonal evidence routes before committing to a long proof.
- **Bottleneck surgery**: shrink a stuck proof to the smallest local lemma, flip it, change representation, then certify, refute, retrieve, or repair.
- **Construction search**: use small cases, exact pattern mining, tight examples, and algebraic normal forms to guess useful objects.
- **Compact local repair**: preserve a useful proof skeleton, isolate the bad block as a named lemma, and retry with only the statement, parents, previous attempt, and feedback.
- **Tool-assisted proof control**: translate Wolfram, Python, CVXPy, Z3, OR-Tools, Sage, or Lean output into lemmas, certificates, counterexamples, or theorem repairs.
- **Escalation**: when a proof stalls, move to counterexample search, symbolic checks, LP/SMT certificates, premise retrieval, local formalization, or theorem repair.

## When To Use

Use this skill when the proof itself is missing, blocked, suspicious, or has failed before.

Typical examples:

- prove monotonicity, threshold structure, or policy optimality in a DP or MDP;
- debug IC/IR, envelope, payment identity, or cyclic monotonicity arguments in mechanism design;
- find the right regret decomposition for a bandit or online learning theorem;
- repair a lower-bound construction whose KL, separation, or testing reduction does not work;
- decide whether a theorem is actually true under the stated assumptions;
- preserve failed proof attempts so later work starts from evidence rather than memory.

For exposition, rewriting, LaTeX cleanup, or making an already complete proof easier to read, use a proof-writing skill instead.

## Installation

Clone the repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git ~/.codex/skills/theory-proof-workbench
```

Restart Codex or refresh skill discovery if needed. The skill name is:

```text
theory-proof-workbench
```

## Optional Wolfram Engine Setup

This skill can use Wolfram through the local `wmath`/`codex-wmath` wrapper when the companion `math-tools` skill is installed. Wolfram is optional, but it is useful for symbolic algebra, inequality checks, condition discovery, quantifier elimination, FOCs/KKT algebra, Bellman/Q-value differences, envelope derivatives, and small counterexample searches.

`codex-wmath` is a local command wrapper around the Wolfram Language kernel. On this machine, `wmath` delegates to `codex-wmath`; `codex-wmath` calls `WolframKernel` directly when available and falls back to `wolframscript` if needed. It also uses a timeout guard and a temporary lock so multiple Codex calls do not compete for the same local kernel.

Install the backend from Wolfram's official pages:

- [Wolfram Engine](https://www.wolfram.com/engine/) and [Wolfram Engine FAQ](https://www.wolfram.com/engine/faq/).
- [Install WolframScript](https://reference.wolfram.com/language/workflow/InstallWolframScript.html.en), if your setup needs the command-line script interface.
- Wolfram support note on selecting a kernel path for `wolframscript`: [How do I specify which kernel wolframscript should use?](https://support.wolfram.com/47243/).

After installing and activating Wolfram Engine, verify:

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

## Quick Start

For a lightweight idea pass:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

For a hard or repeatedly failed proof, start a proof project:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

When returning to an existing proof project:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

Before claiming a final proof from a ledger:

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

## Workflow

The core loop is:

1. Restate the claim with exact variables, domains, quantifiers, and assumptions.
2. Preserve the theorem statement. If the proof needs a changed statement, mark it as theorem repair.
3. Check for a direct theorem, certificate, contradiction, or known decomposition.
4. Audit whether the statement matches the intended theorem when the claim comes from a model, paper, or informal derivation.
5. Try to break the claim using small, finite, boundary, and relaxed-assumption cases.
6. If the theorem needs an unknown construction, threshold, potential, hard instance, or answer, discover and self-check that object before proving.
7. Choose a proof route and compress it into a proof kernel.
8. For hard or previously failed proofs, compare genuinely different proof, falsification, and evidence routes.
9. If one lemma remains stuck, perform bottleneck surgery and gap grading before another long proof attempt.
10. Build a lemma graph and solve fragile lemmas one at a time.
11. Use tools only when their output becomes a checkable lemma, certificate, counterexample, or repair.
12. Record failed routes, blocked retries, compact repair states, and unchanged proof states.
13. Apply verification gates before writing the final proof.

## Project Workspace

`start_proof.py` creates a structured proof workspace:

- `TRIAGE.md`: immediate next steps and proof-mode rules.
- `WORKSTREAMS.md`: bounded workstream cards and no-repeat attempt fingerprints.
- `IDEA_MAP.md`: central objects, proof kernels, construction search, gap grading, route candidates, and one-step proof moves.
- `ATTACK_MATRIX.md`: proof routes and falsification routes.
- `LEMMA_QUEUE.md`: blueprint-style dependency graph of candidate definitions, lemmas, theorem assembly nodes, declared parents, statuses, gap grades, compact repair states, and failure diagnoses.
- `PATTERN_SCAN.md`: bounded extraction from papers, prior ledgers, formalization projects, or proof-agent workflows.
- `TOOL_PLAN.md`: expected artifacts before CAS, SMT, optimization, Python, Wolfram, Sage, or Lean checks.
- `LEDGER.md`: persistent proof state, failed routes, verification gates, and current obstruction.
- `ESCALATION.md`: next moves after repeated failure.

## Tool Philosophy

Tools do not replace proof. They are useful only when their outputs can be translated into mathematical artifacts.

- Wolfram via `codex-wmath`/`wmath`, or SymPy, can support algebra, inequalities, assumptions, and symbolic conditions.
- Python, CVXPy, Z3, OR-Tools, or Sage can support finite examples, LP/MIP certificates, graph checks, and exact computations.
- Lean/mathlib can check stable local lemmas once the statement is precise.
- Simulations can falsify or sanity-check, but they do not prove universal claims.

## Proof Status

The workbench distinguishes several proof statuses:

- `conjecture`: intuition or pattern match only.
- `counterexample-tested`: no counterexample found in bounded searches.
- `lemma-conditional`: the final theorem depends on named missing lemmas.
- `human-proof`: every nontrivial step is justified in prose.
- `tool-checked`: fragile algebra or constraints were checked by tools.
- `formalized-local`: key local lemmas were checked in Lean or another formal system.
- `formalized-complete`: the full theorem is machine-formalized.

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

## License

This project is released under the MIT License. See [LICENSE](LICENSE).

---

# Codex 理论证明工作台

这是一个用于困难理论证明的 Codex skill，服务于证明思路发现、失败证明调试和 proof recovery。

它主要面向运筹与管理科学、机制设计、经济理论、动态规划、学习理论、bandit、online learning、优化、博弈、激励相容、regret 分析和 lower bound 等研究型证明问题。

它不是定理百科，也不是证明润色工具。它是一套 proof-control workflow，用来帮助 Codex 保持原命题不变，寻找真正的证明思路，避免重复失败路线，并把未完成的证明尝试转化为后续可用的证据。

## 为什么需要它

困难证明失败时，问题往往不在最后的文字表述里。一个看似顺畅的证明可能偷偷加强了 assumption，证明了一个相邻但不同的 theorem，忽略了 boundary case，或者换了一套符号又回到同一个 missing lemma。这个 workbench 的目标就是把这些失败模式显式化。

它会促使 Codex：

- 在证明前精确写出 theorem statement；
- 在证明前先尝试反驳命题；
- 找到能决定一条 proof route 的最小 proof kernel；
- 记录失败路线和没有推进的 proof state；
- 只在工具输出能转化成可检查数学 artifact 时使用工具；
- 在关键 lemma 仍未证明时，返回 `still open` 或 `lemma-conditional`，而不是写出看似漂亮但没有支撑的证明。

## 核心能力

- **证明路由**：根据 theorem family 和 proof pattern 分类。
- **假设审计**：检查 quantifiers、domains、compactness、convexity、continuity、measurability、boundedness、independence、tie-breaking 和 boundary cases。
- **先反驳再证明**：先搜索 small、finite、boundary 和 relaxed-assumption cases，再投入主要证明路线。
- **Blueprint lemma graph**：把 theorem 拆成带依赖关系的 definitions、lemmas 和 final assembly nodes，并记录 parents、statuses 和 failure diagnoses。
- **防重复记忆**：记录重复构造、失败路线、missing assumptions 和 unchanged proof states 的 fingerprints。
- **进步契约**：要求每次 retry 带来新证据，而不是把同一个 missing lemma 换一种说法。
- **先发散再收敛**：在长证明前比较证明路线、反驳路线和独立证据路线。
- **瓶颈手术**：把卡住的证明缩到最小 local lemma，翻成反命题或 tight case，换表示，再认证、反驳、检索或修复。
- **构造搜索**：用 small cases、exact pattern mining、tight examples 和 algebraic normal forms 来猜有用的对象。
- **工具辅助证明控制**：把 Wolfram、Python、CVXPy、Z3、OR-Tools、Sage 或 Lean 的输出转化成 lemmas、certificates、counterexamples 或 theorem repairs。
- **失败升级**：证明卡住时，切换到 counterexample search、symbolic checks、LP/SMT certificates、premise retrieval、local formalization 或 theorem repair。

## 什么时候使用

当证明本身缺失、卡住、可疑，或者已经失败过时，使用这个 skill。

典型任务包括：

- 证明 DP 或 MDP 中的 monotonicity、threshold structure 或 policy optimality；
- 调试机制设计中的 IC/IR、envelope、payment identity 或 cyclic monotonicity 证明；
- 为 bandit 或 online learning theorem 找到正确的 regret decomposition；
- 修复 KL、separation 或 testing reduction 不成立的 lower-bound construction；
- 判断一个 theorem 在当前 stated assumptions 下是否真的成立；
- 保存失败证明尝试，让之后的工作从证据出发，而不是从记忆重来。

如果核心证明已经完成，只需要润色、改写、LaTeX 化或提升可读性，应使用 proof-writing skill，而不是这个 proof-discovery workbench。

## 安装

将仓库 clone 到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git ~/.codex/skills/theory-proof-workbench
```

如有需要，重启 Codex 或刷新 skill discovery。skill 名称是：

```text
theory-proof-workbench
```

## 可选的 Wolfram Engine 设置

如果同时安装了 `math-tools` skill，这个 workbench 可以通过本地 `wmath`/`codex-wmath` wrapper 调用 Wolfram。Wolfram 不是必须的，但它很适合做 symbolic algebra、inequality checks、condition discovery、quantifier elimination、FOC/KKT algebra、Bellman/Q-value difference、envelope derivatives 和小型 counterexample search。

`codex-wmath` 是本地 Wolfram Language kernel wrapper。在这台机器上，`wmath` 会委托给 `codex-wmath`；`codex-wmath` 会优先直接调用 `WolframKernel`，必要时退回 `wolframscript`。它还带 timeout guard 和临时锁，避免多个 Codex 调用抢同一个本地 kernel。

后端从 Wolfram 官方页面安装：

- [Wolfram Engine](https://www.wolfram.com/engine/) 和 [Wolfram Engine FAQ](https://www.wolfram.com/engine/faq/)。
- 如果需要命令行脚本接口，参考 [Install WolframScript](https://reference.wolfram.com/language/workflow/InstallWolframScript.html.en)。
- 如果 `wolframscript` 找不到 kernel，参考 Wolfram support 的 kernel path 说明：[How do I specify which kernel wolframscript should use?](https://support.wolfram.com/47243/)。

安装并激活 Wolfram Engine 后，验证：

```bash
wolframscript -code '2+2'
codex-wmath '2+2'
wmath '2+2'
```

证明任务里优先让 Wolfram 输出可检查 artifact：

```bash
codex-wmath 'ExportString[With[{s = FullSimplify[x^2 >= 0, Element[x, Reals]]}, <|"verified" -> TrueQ[s], "result" -> ToString[s, InputForm]|>], "RawJSON"]'
```

不要把 Wolfram 输出直接当作最终证明。真正有用的输出应该被翻译成 proof ledger 里的 lemma、condition、counterexample、certificate 或 theorem repair。

## 快速开始

轻量寻找证明思路：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

对于困难证明或反复失败的证明，创建 proof project：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

回到已有 proof project 时，先诊断下一步：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

在基于 ledger 宣称最终证明之前，先检查缺口：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

## 工作流

核心流程是：

1. 用精确的 variables、domains、quantifiers 和 assumptions 重述 claim。
2. 保持原 theorem statement 不变；如果证明必须改命题，要明确标为 theorem repair。
3. 先检查是否存在直接 theorem、certificate、contradiction 或 known decomposition。
4. 在 small、finite、boundary 和 relaxed-assumption cases 中尝试反驳命题。
5. 选择一条 proof route，并压缩成 proof kernel。
6. 对困难或曾经失败的证明，先比较真正不同的证明路线、反驳路线和独立证据路线。
7. 如果一个 lemma 持续卡住，先做 bottleneck surgery，再尝试长证明。
8. 构建 lemma graph，一次解决一个脆弱 lemma。
9. 只有当工具输出能转化为可检查 lemma、certificate、counterexample 或 repair 时，才把它纳入证明。
10. 记录失败路线、blocked retries 和没有推进的 proof states。
11. 写最终证明前通过 verification gates。

## 项目工作区

`start_proof.py` 会创建一个结构化 proof workspace：

- `TRIAGE.md`：当前证明的下一步和 proof-mode rules。
- `WORKSTREAMS.md`：有边界的 workstream cards，以及避免重复尝试的 fingerprints。
- `IDEA_MAP.md`：central objects、proof kernels、construction search 和 one-step proof moves。
- `ATTACK_MATRIX.md`：proof routes 和 falsification routes。
- `LEMMA_QUEUE.md`：blueprint-style dependency graph，记录 candidate definitions、lemmas、theorem assembly nodes、declared parents、statuses 和 failure diagnoses。
- `PATTERN_SCAN.md`：从论文、旧 ledgers、formalization projects 或 proof-agent workflows 中提取可迁移结构。
- `TOOL_PLAN.md`：在运行 CAS、SMT、optimization、Python、Wolfram、Sage 或 Lean 前写清 expected artifacts。
- `LEDGER.md`：持久化 proof state、失败路线、verification gates 和当前 obstruction。
- `ESCALATION.md`：重复失败后的下一步。

## 工具使用原则

工具不能替代证明。只有当工具输出能转化为数学 artifact 时，它才真正有用。

- 通过 `codex-wmath`/`wmath` 调用的 Wolfram，或 SymPy，可用于代数、inequalities、assumptions 和 symbolic conditions。
- Python、CVXPy、Z3、OR-Tools 或 Sage 可用于 finite examples、LP/MIP certificates、graph checks 和 exact computations。
- Lean/mathlib 适合在 statement 已经稳定后检查 local lemmas。
- Simulation 只能用于 falsification 或 sanity check，不能证明 universal claims。

## 证明状态

这个 workbench 区分以下 proof statuses：

- `conjecture`：只是直觉或 pattern match。
- `counterexample-tested`：在有限搜索中没有找到反例。
- `lemma-conditional`：最终 theorem 依赖明确列出的 missing lemmas。
- `human-proof`：每个非平凡步骤都有文字证明或引用。
- `tool-checked`：脆弱代数或 constraints 已经由工具检查。
- `formalized-local`：关键 local lemmas 已经由 Lean 或其他 formal system 检查。
- `formalized-complete`：完整 theorem 已经 machine-formalized。

如果关键 lemma 只是猜出来的，不要把结果称为 proved。

## 仓库结构

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

## 开发检查

检查 skill 结构：

```bash
codex-math-python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

编译脚本：

```bash
PYTHONPYCACHEPREFIX=/tmp/codex-pycache codex-math-python -m py_compile scripts/*.py
```

运行 smoke test：

```bash
codex-math-python scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## 许可证

本项目采用 MIT License 开源。详情见 [LICENSE](LICENSE)。
