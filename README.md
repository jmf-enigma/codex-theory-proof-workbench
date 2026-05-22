# Codex Theory Proof Workbench / 理论证明工作台

A Codex skill for hard theoretical proof discovery, proof debugging, and failed-proof recovery.

这是一个面向困难理论证明的 Codex skill，用来寻找证明思路、调试失败证明、记录失败路径，并在证明卡住时系统地转向反例、工具验证、文献套路或定理修复。

It is designed for research problems in OR/MS, mechanism design, economic theory, dynamic programming, learning theory, bandits, online learning, optimization, games, IC/IR, regret analysis, and lower bounds.

它主要服务于 OR/MS、机制设计、经济理论、动态规划、学习理论、bandit、online learning、优化、博弈、IC/IR、regret 分析和 lower bound 等研究型数学证明。

This is not a theorem database. It is a proof-control workflow that helps Codex avoid restarting from scratch, avoid silently changing the theorem, and preserve failed proof attempts as useful state.

它不是定理百科，而是一套 proof-control workflow。目标是让 Codex 不要每次从头开始，不要偷偷改 theorem statement，也不要把失败证明当成垃圾丢掉，而是把失败变成下一轮证明的状态信息。

## What It Does / 功能

- Routes a proof by theorem family and proof pattern.
- 根据 theorem family 和 proof pattern 对证明任务分类。
- Audits assumptions, quantifiers, boundary cases, and theorem statement drift.
- 检查 assumptions、quantifiers、boundary cases，以及证明过程中是否偷偷改了原命题。
- Forces at least one proof route and one falsification route before polished proof writing.
- 在写 polished proof 之前，要求至少尝试一条证明路线和一条 falsification/反例路线。
- Builds lemma graphs with statuses such as known, proved, tool-checked, missing, or false.
- 把证明拆成 lemma graph，并标记每个 lemma 的状态，例如 known、proved、tool-checked、missing 或 false。
- Records repeated failed attempts with fingerprints so the same construction is not retried under new notation.
- 给重复失败的 proof attempt 记录 fingerprint，避免换个符号又尝试同一个失败构造。
- Uses small cases, exact pattern mining, and tool checks to guess and verify clever constructions or algebraic normal forms.
- 利用 small cases、exact pattern mining 和工具检查来猜测并验证巧妙构造或代数 normal form。
- Escalates stuck proofs through counterexample search, symbolic checks, LP/SMT certificates, literature/premise retrieval, local Lean formalization, or theorem repair.
- 当证明卡住时，会转向 counterexample search、symbolic checks、LP/SMT certificates、文献/premise retrieval、local Lean formalization 或 theorem repair。

## When To Use / 什么时候用

Use this skill when the proof itself is missing, blocked, suspicious, or has failed before.

当证明本身还没有找到、已经卡住、看起来可疑，或者之前已经失败过时，用这个 skill。

Typical tasks include:

典型任务包括：

- Prove a monotone or threshold policy in a DP/MDP.
- 证明 DP/MDP 中的 monotone policy 或 threshold policy。
- Debug a mechanism design IC/IR or cyclic monotonicity proof.
- 调试机制设计里的 IC/IR 或 cyclic monotonicity 证明。
- Find the right regret decomposition for a bandit or online learning theorem.
- 为 bandit 或 online learning theorem 找正确的 regret decomposition。
- Repair a lower-bound construction whose KL or separation argument does not work.
- 修复 KL 或 separation argument 不成立的 lower-bound construction。
- Decide whether a theorem is true under the stated assumptions.
- 判断一个 theorem 在当前 assumptions 下是否真的成立。
- Preserve failed proof attempts so later work starts from evidence instead of memory.
- 保存失败证明尝试，让后续证明从证据开始，而不是靠记忆重来。

For exposition, polishing, or LaTeX cleanup after the core proof already exists, use a proof-writing skill instead.

如果核心证明已经存在，只需要润色、改写、LaTeX 化或提升可读性，应使用 proof-writing skill，而不是这个 proof-discovery workbench。

## Installation / 安装

Clone this repository into your Codex skills directory:

把仓库 clone 到 Codex 的 skills 目录：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git ~/.codex/skills/theory-proof-workbench
```

Restart Codex or refresh skill discovery if needed. The skill name is:

如有需要，重启 Codex 或刷新 skill discovery。skill 名称是：

```text
theory-proof-workbench
```

## Quick Start / 快速开始

For a lightweight idea pass:

轻量寻找证明思路：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/plan_idea.py "CLAIM"
```

For a hard or repeatedly failed proof, start a proof project:

对于困难证明或反复失败的证明，创建 proof project：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

When returning to a proof project:

回到已有 proof project 时，先诊断下一步：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/proof_doctor.py path/to/proof_project
```

Before claiming a final proof from a ledger:

在基于 ledger 宣称最终证明之前，先检查缺口：

```bash
codex-math-python ~/.codex/skills/theory-proof-workbench/scripts/audit_ledger.py path/to/LEDGER.md
```

## Workflow / 工作流

The core loop is:

核心流程是：

1. Restate the claim with exact variables, domains, quantifiers, and assumptions.
2. Preserve the theorem statement. If the proof needs a changed claim, mark it as theorem repair.
3. Try a direct theorem, certificate, contradiction, or known decomposition.
4. Search for counterexamples in small, finite, boundary, or relaxed-assumption cases.
5. Choose a route and reduce it to a proof kernel.
6. Build a lemma graph and solve fragile lemmas one at a time.
7. Use tools only when their output becomes a checkable lemma, certificate, counterexample, or repair.
8. Record failed routes and unchanged proof states.
9. Apply verification gates before writing the final proof.

中文解释：

1. 先把 theorem 的 variables、domains、quantifiers 和 assumptions 写清楚。
2. 保持原 theorem statement 不变；如果证明必须改命题，要明确标为 theorem repair。
3. 先尝试直接 theorem、certificate、contradiction 或 known decomposition。
4. 在 small、finite、boundary 或 relaxed-assumption cases 中寻找反例。
5. 选择一条路线，并压缩成一个 proof kernel。
6. 构建 lemma graph，一次解决一个脆弱 lemma。
7. 工具输出只有在能变成可检查 lemma、certificate、counterexample 或 repair 时才进入证明。
8. 记录失败路线和没有推进的 proof state。
9. 写最终证明前通过 verification gates。

## Project Files / 项目文件

`start_proof.py` creates a structured proof workspace:

`start_proof.py` 会创建一个结构化 proof workspace：

- `TRIAGE.md`: immediate next steps and proof-mode rules.
- `TRIAGE.md`：当前证明的下一步和证明模式规则。
- `WORKSTREAMS.md`: bounded workstream cards and no-repeat attempt fingerprints.
- `WORKSTREAMS.md`：有边界的 workstream cards，以及避免重复尝试的 fingerprints。
- `IDEA_MAP.md`: central objects, proof kernels, and one-step proof moves.
- `IDEA_MAP.md`：central objects、proof kernels 和 one-step proof moves。
- `ATTACK_MATRIX.md`: proof routes and falsification routes.
- `ATTACK_MATRIX.md`：证明路线和 falsification 路线。
- `LEMMA_QUEUE.md`: candidate lemmas to prove, refute, or certify.
- `LEMMA_QUEUE.md`：待证明、反驳或认证的 candidate lemmas。
- `PATTERN_SCAN.md`: bounded extraction from papers, prior ledgers, or proof-agent workflows.
- `PATTERN_SCAN.md`：从论文、旧 ledger 或 proof-agent workflow 中提取可迁移结构。
- `TOOL_PLAN.md`: expected artifacts before CAS, SMT, optimization, Python, Wolfram, Sage, or Lean checks.
- `TOOL_PLAN.md`：运行 CAS、SMT、optimization、Python、Wolfram、Sage 或 Lean 前先写清 expected artifact。
- `LEDGER.md`: persistent proof state, failed routes, verification gates, and current obstruction.
- `LEDGER.md`：持久化 proof state、失败路线、verification gates 和当前 obstruction。
- `ESCALATION.md`: what to do after repeated failure.
- `ESCALATION.md`：重复失败后的升级路线。

## Tool Philosophy / 工具观

Tools do not replace proof. They help produce artifacts that can be checked.

工具不能替代证明。工具的作用是产生可检查的 artifact。

- Wolfram or SymPy for algebra, inequalities, assumptions, and symbolic conditions.
- Wolfram 或 SymPy：代数、inequalities、assumptions 和 symbolic conditions。
- Python, CVXPy, Z3, OR-Tools, or Sage for finite examples, LP/MIP certificates, graph checks, or exact computations.
- Python、CVXPy、Z3、OR-Tools 或 Sage：finite examples、LP/MIP certificates、graph checks 或 exact computations。
- Lean/mathlib for stable local lemmas once the statement is precise.
- Lean/mathlib：当局部 lemma statement 足够稳定后，用来 formalize local lemmas。
- Simulations only for falsification or sanity checks, not for proving universal claims.
- Simulation 只能用于 falsification 或 sanity check，不能证明 universal claims。

## Verification Standards / 证明状态标准

The skill distinguishes proof statuses:

这个 skill 区分不同的 proof status：

- `conjecture`: intuition or pattern match only.
- `conjecture`：只是直觉或 pattern match。
- `counterexample-tested`: no counterexample found in bounded searches.
- `counterexample-tested`：在有限搜索中没有找到反例。
- `lemma-conditional`: final theorem depends on named missing lemmas.
- `lemma-conditional`：最终 theorem 依赖明确列出的 missing lemmas。
- `human-proof`: every nontrivial step is justified in prose.
- `human-proof`：每个非平凡步骤都有文字证明或引用。
- `tool-checked`: fragile algebra or constraints were checked by tools.
- `tool-checked`：脆弱代数或 constraints 已经由工具检查。
- `formalized-local`: key local lemmas were checked in Lean or another formal system.
- `formalized-local`：关键 local lemmas 已经由 Lean 或其他 formal system 检查。
- `formalized-complete`: the full theorem is machine-formalized.
- `formalized-complete`：完整 theorem 已经 machine-formalized。

Do not call a result proved if the key lemma is only guessed.

如果关键 lemma 只是猜出来的，不要把结果称为 proved。

## Repository Layout / 仓库结构

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

## Development Checks / 开发检查

Validate the skill structure:

检查 skill 结构：

```bash
codex-math-python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

Compile scripts:

编译脚本：

```bash
PYTHONPYCACHEPREFIX=/tmp/codex-pycache python3 -m py_compile scripts/*.py
```

Run a smoke test:

运行 smoke test：

```bash
python3 scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## License / 许可证

No license has been selected yet. Until a license is added, all rights are reserved by the repository owner.

当前还没有选择开源许可证。在添加 license 之前，所有权利由仓库 owner 保留。
