# Codex Theory Proof Workbench

[![Codex Skill](https://img.shields.io/badge/Codex-skill-111827?logo=openai&logoColor=white)](SKILL.md)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](#development)
[![MIT License](https://img.shields.io/badge/License-MIT-2EA44F.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/jmf-enigma/codex-theory-proof-workbench?style=social)](https://github.com/jmf-enigma/codex-theory-proof-workbench/stargazers)

[Quick start](#quick-start) · [Controls](#proof-controls) · [Evidence](#tools-and-evidence) · [中文](#codex-理论证明工作台)

**A lightweight, auditable controller for hard, stuck, or unknown-answer mathematical proofs.**

Theory Proof Workbench is an open Codex skill for proof discovery and recovery. It is designed for problems where the key lemma, construction, certificate, or answer is unclear. Its main domains are OR/MS, dynamic programming, mechanism design, economics, learning theory, bandits, optimization, games, lower bounds, and probabilistic methods.

The skill helps Codex do six things reliably.

- Freeze the exact claim before proof search drifts.
- Try direct closure, small cases, and counterexamples before long prose.
- Compare mathematically distinct routes and remember failed states.
- Admit only decompositions whose children really feed the parent proof.
- Route local obligations to literature, computation, Lean, or specialist skills.
- Report only the proof status supported by replayable evidence.

It does not guarantee a solution to every true or open problem. When the mathematics is already complete and only exposition remains, use `math-proof-writing`.

## Quick Start

### Install

Ask Codex to install the repository-root skill.

```text
Use $skill-installer to install
https://github.com/jmf-enigma/codex-theory-proof-workbench
as theory-proof-workbench.
```

Or install it manually.

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench"
```

Restart Codex or refresh skill discovery. The core uses Python 3.10+ and the standard library. Mathematical backends are optional.

### Invoke

```text
Use $theory-proof-workbench to prove this theorem. Preserve the exact statement,
test the smallest counterexamples, and find the proof kernel before drafting.

Use $theory-proof-workbench in recovery mode. Read the existing proof state and
do not retry an equivalent construction.

Use $theory-proof-workbench in discovery mode. Verify the literature frontier,
freeze one admissible candidate, and then prove it.
```

Explicit invocation is the most predictable route. Clearly hard or previously failed proof requests may also trigger the skill implicitly. It starts no resident agent or Wolfram process.

## Proof Controls

The default loop is small.

1. Freeze variables, domains, assumptions, quantifiers, and the conclusion.
2. Attempt a direct theorem, contradiction, certificate, or known decomposition.
3. Stress-test the negation on the smallest informative cases.
4. Identify one proof kernel and compare genuinely different route families.
5. Build an AND/OR lemma graph only when the proof needs durable decomposition.
6. Check fragile local claims with the cheapest decisive backend.
7. Assemble the exact parent theorem and run an adversarial review.

Hard problems activate additional controls only when needed.

| Control | What it prevents |
| --- | --- |
| Answer-hole contract | A construction or find-all answer that merely restates the target |
| Decomposition admission | Circular, non-simplifying, or unassemblable child lemmas |
| Lemma consumption and replay | Counting a true but unused lemma as parent progress |
| Failed-state fingerprints | Repeating the same route under new notation or wording |
| Phase-adaptive workstreams | Broad parallel search after the real bottleneck is already known |
| Statement and completion gates | Formally checking an encoding that does not match the intended theorem |

`proof_doctor.py` now enforces the decomposition controls. Every required child needs an exact use site in a conditional parent assembly. Once a required child is proved, the parent assembly must be replayed and recorded as passed or failed before that child counts as progress.

## Tools And Evidence

| Backend | Expected artifact |
| --- | --- |
| Wolfram or SymPy | Exact identity, sign region, quantified condition, symbolic witness |
| Python, Z3, CVXPy, Sage, NetworkX | Finite witness, unsat core, optimization certificate, discrete structure |
| Lean | Checked local lemma or complete formal assembly |
| Peppy and PEPFlow | Exact PEP certificate or verified Lyapunov structure |
| Matlas and TheoremSearch | Statement candidate that still requires source verification |
| Scholar, arXiv, OpenAlex, DOI records | Literature coverage, theorem identity, assumptions, and proof anchors |

Experiments can refute a claim or suggest a formula, but they do not prove a universal statement. A CAS result supports only the encoded local claim and assumptions. A checked lemma supports its parent only after the dependency path is assembled. A Lean kernel verifies the formal statement it receives, so semantic fidelity and final assembly remain separate obligations.

Remote statement search requires `--remote-ok` and an abstracted, non-sensitive query. Retrieval scores and model rankings have `proof_effect=none` until the source and proof are checked.

## Persistent Projects

Codex normally runs these helpers automatically.

```bash
python3 scripts/start_proof.py --title "short-name" --claim "EXACT CLAIM"
python3 scripts/proof_doctor.py path/to/proof_project
python3 scripts/proof_runtime.py brief path/to/proof_project --markdown
```

The active project stores the exact claim, route portfolio, lemma graph, failed-attempt fingerprints, tool artifacts, and proof status. Detailed rules live in [SKILL.md](SKILL.md). Source-to-rule mappings and benchmark boundaries live in [Research-Backed Proof Loop](references/research-backed-proof-loop.md).

## Development

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONPYCACHEPREFIX=/tmp/codex-pycache python3 -m py_compile scripts/*.py
python3 scripts/smoke_workbench.py
```

Contributions should address a named proof bottleneck and include a reproducible check. Use anonymized examples and never upload confidential mathematics. Released under the [MIT License](LICENSE).

---

# Codex 理论证明工作台

[快速开始](#快速开始) · [证明控制](#证明控制) · [工具与证据](#工具与证据) · [English](#codex-theory-proof-workbench)

**一个面向困难、卡住或答案尚不明确数学问题的轻量、可审计证明控制器。**

Theory Proof Workbench 是一个开源 Codex skill，用来发现证明思路并恢复失败证明。它适合关键 lemma、构造、certificate 或答案仍不清楚的问题，重点覆盖 OR/MS、动态规划、机制设计、经济理论、learning theory、bandits、优化、博弈、lower bounds 和概率方法。

它帮助 Codex 稳定完成六件事。

- 在搜索漂移前冻结准确命题。
- 在写长证明前尝试直接闭合、小规模情形和反例。
- 比较数学机制真正不同的路线，并记住已经失败的 proof state。
- 只接受确实能够进入 parent proof 的分解。
- 把局部义务交给文献、计算、Lean 或相应 specialist skill。
- 只报告可重放证据支持的证明状态。

它不保证解决每个真命题或开放问题。数学已经完整、只需要整理表达时，应使用 `math-proof-writing`。

## 快速开始

### 安装

让 Codex 安装仓库根目录中的 skill。

```text
使用 $skill-installer 安装
https://github.com/jmf-enigma/codex-theory-proof-workbench
安装名称使用 theory-proof-workbench。
```

也可以手动安装。

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench"
```

重启 Codex 或刷新 skill discovery。核心需要 Python 3.10+，只依赖标准库。Wolfram、Lean、Peppy 等数学后端都是可选项。

### 调用

```text
使用 $theory-proof-workbench 证明这个 theorem。保持原命题不变，
先检查最小反例，并在写长证明前找出 proof kernel。

使用 $theory-proof-workbench 的 recovery mode。读取已有 proof state，
不要重试等价构造。

使用 $theory-proof-workbench 的 discovery mode。先核查文献 frontier，
固定一个满足约束的 candidate，然后证明它。
```

显式调用最稳定。明显困难或已经失败过的证明请求也可能自动触发。skill 不会启动常驻 Agent 或 Wolfram 进程。

## 证明控制

默认循环保持简洁。

1. 冻结变量、定义域、假设、量词和结论。
2. 尝试直接定理、反证、certificate 或已知分解。
3. 在最小且有信息量的情形上检查命题的否定。
4. 找到一个 proof kernel，并比较机制不同的路线。
5. 只有确实需要持久分解时才建立 AND/OR lemma graph。
6. 用成本最低且有决定性的工具检查脆弱局部命题。
7. 组装准确 parent theorem，并进行对抗审查。

困难问题才会按需启用以下控制。

| 控制 | 防止的问题 |
| --- | --- |
| Answer-hole contract | 构造题或 find-all 任务用目标本身充当答案 |
| Decomposition admission | 循环、不更简单或无法组装的 child lemma |
| Lemma consumption and replay | 把真实但没有用于 parent 的 lemma 当成进展 |
| Failed-state fingerprints | 换一种记号或说法后重复同一条失败路线 |
| Phase-adaptive workstreams | 已找到瓶颈后仍然进行无边界的宽搜索 |
| Statement and completion gates | 形式化通过，但编码的并不是原 theorem |

`proof_doctor.py` 现在会执行分解门槛。每个 required child 必须在 conditional parent assembly 中有准确使用位置。required child 证明完成后，还要重放 parent assembly，并记录通过或失败，才可以把它计入 parent 的证明进展。

## 工具与证据

| 后端 | 应返回的 artifact |
| --- | --- |
| Wolfram 或 SymPy | 精确恒等式、符号区域、量化条件、symbolic witness |
| Python、Z3、CVXPy、Sage、NetworkX | finite witness、unsat core、optimization certificate、离散结构 |
| Lean | 通过检查的 local lemma 或完整 formal assembly |
| Peppy 与 PEPFlow | 精确 PEP certificate 或经过核验的 Lyapunov 结构 |
| Matlas 与 TheoremSearch | 仍需核查原文的命题候选 |
| Scholar、arXiv、OpenAlex、DOI 记录 | 文献覆盖、定理身份、假设和 proof anchor |

实验可以反驳命题或提示公式，但不能证明 universal statement。CAS 结果只支持实际编码的局部命题和假设。局部 lemma 只有沿 dependency path 完成组装后，才能支持 parent。Lean kernel 检查它收到的 formal statement，因此语义一致性和最终组装仍是独立义务。

远程命题检索必须显式传入 `--remote-ok`，并且只能发送抽象化后的非敏感 query。检索分数和模型排名的 `proof_effect=none`，直到来源和原文证明完成核查。

## 持久证明项目

多数情况下由 Codex 自动调用。

```bash
python3 scripts/start_proof.py --title "short-name" --claim "EXACT CLAIM"
python3 scripts/proof_doctor.py path/to/proof_project
python3 scripts/proof_runtime.py brief path/to/proof_project --markdown
```

项目会保存准确命题、路线组合、lemma graph、失败尝试指纹、工具证据和证明状态。完整规则见 [SKILL.md](SKILL.md)。来源与具体控制规则的对应关系，以及 benchmark 能力边界，见 [Research-Backed Proof Loop](references/research-backed-proof-loop.md)。

## 开发与许可

运行 `python3 scripts/smoke_workbench.py` 可以执行完整回归检查。贡献应解决一个明确的证明瓶颈，并提供可复现检查。请使用匿名例子，不要上传保密数学内容。本仓库使用 [MIT License](LICENSE)。
