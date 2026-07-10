# Codex Theory Proof Workbench

A Codex skill for discovering, debugging, and recovering hard theoretical proofs.

The workbench is designed for proofs where the hard part is still missing. It keeps the theorem statement fixed, searches for decisive lemmas or constructions, remembers failed routes, coordinates local mathematical tools, and reports an exact obstruction when the proof remains open.

It is not a theorem database and it does not make an unsupported argument correct. Its job is to make proof search more deliberate, checkable, and less repetitive.

## When To Use It

- Operations research, management science, optimization, queueing, inventory, scheduling, and control.
- Dynamic programming, MDPs, Bellman certificates, threshold policies, and indexability.
- Mechanism design, economic theory, IC/IR, envelope arguments, and cyclic monotonicity.
- Learning theory, bandits, online learning, regret bounds, and information-theoretic lower bounds.
- Games, matching, probabilistic constructions, and the Lovasz Local Lemma.
- Any proof that has already failed and should resume from evidence rather than restart from scratch.

Use a proof-writing skill instead when the mathematical argument is already complete and only needs clearer exposition, LaTeX, or paper-style polishing.

## What It Changes

| Failure mode | Workbench response |
| --- | --- |
| The proof silently changes the claim | Statement-fidelity and theorem-repair gates |
| The same idea returns under new notation | Attempt fingerprints and proof-state deduplication |
| The central construction is unknown | Small-case discovery, tight-case search, and pattern mining |
| A missing lemma hides the entire theorem | Proof-kernel and good-gap/bad-gap checks |
| Tools return data but no proof | Artifact-first tool plans and proof translation |
| A plausible local step may contain a gap | Conditional prover-verifier review |
| Several attempts make no progress | Route decisions, bounded escalation, and honest stop statuses |

## Install

Clone the repository into the Codex skills directory:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench"
```

Restart Codex or refresh skill discovery. To update later:

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench" pull --ff-only
```

The skill itself needs no Python packages. Its helper scripts support Python 3.9 or newer. Wolfram, Lean, Sage, Z3, CVXPy, and other mathematical backends are optional and are not bundled with this repository.

## Use It In Codex

Codex may invoke the skill implicitly for a hard or repeatedly failed proof. Explicit invocation is the most reliable way to request the full workflow:

```text
Use $theory-proof-workbench to prove this theorem. First check the exact
statement and small counterexamples. If the route is unclear, identify the
proof kernel before writing a long proof.
```

For a proof that has already failed:

```text
Use $theory-proof-workbench in recovery mode. Read the existing ledger first,
identify what is genuinely new, and do not retry an equivalent construction.
```

For strategy without a full proof project:

```text
Use $theory-proof-workbench only for a light idea pass. Give me the failure
world, central object, proof kernel, and one checkable next move.
```

This is a skill, not a resident background service. It runs when Codex handles a proof task. Persistent proof state lives in the generated project files.

## Command-Line Helpers

The scripts are optional. Codex can run them while working, or they can be called directly:

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench"
```

Compact idea pass:

```bash
python3 scripts/plan_idea.py "CLAIM"
```

Add `--full` only when the compact pass does not reveal a useful central object or proof kernel.

Start a hard proof project:

```bash
python3 scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

Use `--mode recovery` when the same theorem has already failed.

Diagnose one primary next move:

```bash
python3 scripts/proof_doctor.py path/to/proof_project
```

Use `--json` for machine-readable output. Before presenting a final proof, audit its ledger:

```bash
python3 scripts/audit_ledger.py path/to/proof_project/LEDGER.md
```

Other focused helpers include:

| Script | Purpose |
| --- | --- |
| `select_playbook.py` | Route a claim to the relevant domain playbook |
| `check_attempt.py` | Detect a repeated route or construction |
| `pattern_miner.py` | Guess exact patterns from small-case sequences |
| `new_lemma_card.py` | Save a reusable local lemma |
| `new_trick_card.py` | Save a validated paper or proof trick |

If a configured mathematical environment provides `codex-math-python`, it can replace `python3`. It is not required by this repository.

## Adaptive Workflow

The workbench selects the lightest useful mode. The advanced machinery is conditional, not a checklist for every proof.

| Mode | Use when | Typical output |
| --- | --- | --- |
| Direct | A named theorem, certificate, or short derivation is visible | A verified proof |
| Micro check | A small proof needs one nearby theorem pattern | A theorem match or clear mismatch |
| Light idea | The central object or construction is unclear | A proof kernel and verification hook |
| Project | The proof is hard, multi-lemma, or tool-assisted | Persistent proof state and a lemma graph |
| Recovery | The theorem has failed before | A no-repeat diagnosis and a genuinely new move |

For hard proofs, the core loop is:

1. Freeze the exact statement, assumptions, domains, and quantifiers.
2. Check direct theorems and try to falsify the claim on small and boundary cases.
3. Identify the failure world, central object, and smallest decisive proof kernel.
4. Compare a small number of genuinely different routes.
5. Build an AND/OR lemma graph and work the least-certain required child.
6. Use tools only for a named counterexample, condition, identity, certificate, or formal lemma.
7. After two unchanged local attempts, repair, re-decompose, retrieve, tool-check, or stop.
8. Assemble the original theorem and run an adversarial final review.

## Proof Project Memory

`start_proof.py` creates durable project files. They are not all loaded at once. `proof_doctor.py` recommends only the files relevant to the current proof state.

| File | Role |
| --- | --- |
| `TRIAGE.md` | Initial mode and immediate decisions |
| `ATTACK_MATRIX.md` | Proof, falsification, and orthogonal evidence routes |
| `IDEA_MAP.md` | Central objects, constructions, kernels, and one-step moves |
| `LEMMA_QUEUE.md` | AND/OR lemma graph and node status |
| `WORKSTREAMS.md` | Attempt fingerprints, bounded branches, and route decisions |
| `PATTERN_SCAN.md` | Bounded extraction from papers, ledgers, or formal libraries |
| `TOOL_PLAN.md` | Expected artifacts before computation or formalization |
| `LEDGER.md` | Persistent claim, evidence, failures, and verification status |
| `ESCALATION.md` | Legal next moves after repeated failure |

The idea map, literature scan, prover-verifier loop, formal checks, and multi-agent roles activate only when the current proof needs them.

## Mathematical Tools

Tool output becomes proof evidence only after it is translated into a named artifact:

- a counterexample or finite witness;
- an exact identity or quantified condition;
- a KKT, dual, Bellman, LP, SMT, or combinatorial certificate;
- a local Lean theorem with no admitted gap;
- a theorem repair exposing the missing assumption.

Numerical experiments and simulations can falsify or guide a conjecture, but they do not prove a universal statement. A formal helper lemma also does not close the main theorem when the final assembly still contains `sorry`, admitted axioms, or an unencoded obligation.

### Optional Wolfram Support

Wolfram is useful for symbolic simplification, inequality conditions, quantifier elimination, KKT algebra, Bellman differences, envelope calculations, and small counterexample searches. Install it separately from the official [Wolfram Engine](https://www.wolfram.com/engine/) and [WolframScript](https://reference.wolfram.com/language/workflow/InstallWolframScript.html.en) pages.

```bash
wolframscript -code '2+2'
```

If the companion `math-tools` setup provides `wmath` or `codex-wmath`, the workbench can use those wrappers. This repository does not install them.

## Multi-Agent Use

Parallel agents are opt-in. When explicitly requested, split them by artifact: one planner, one falsifier, one retriever, one local tool-checker or formalizer, and one reviewer. A single integrator remains responsible for the theorem statement, route choice, and final proof status. Several agents should not write competing versions of the same proof route.

## Proof Statuses

| Status | Meaning |
| --- | --- |
| `conjecture` | Intuition or pattern match only |
| `counterexample-tested` | No counterexample found in bounded tests |
| `lemma-conditional` | The theorem depends on named missing lemmas |
| `human-proof` | Every nontrivial step has a mathematical justification |
| `tool-checked` | Fragile local steps have independent tool artifacts |
| `formalized-local` | Important local lemmas are machine-checked |
| `formalized-complete` | The complete theorem and assembly are machine-checked |

Never label a result as proved when its decisive lemma is still guessed.

## Repository Layout

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── proof-router.md
│   ├── proof-idea-generator.md
│   ├── dp-proof-playbook.md
│   ├── mechanism-design-playbook.md
│   └── ...
└── scripts/
    ├── start_proof.py
    ├── proof_doctor.py
    ├── audit_ledger.py
    └── ...
```

## Development

The workbench scripts use only the Python standard library. The Codex skill validator additionally needs PyYAML:

```bash
python3 -m pip install pyyaml
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONPYCACHEPREFIX=/tmp/codex-pycache python3 -m py_compile scripts/*.py
python3 scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## Design Influences

The workflow translates ideas from proof-agent and formalization research into lightweight control rules:

- [Draft, Sketch, and Prove](https://arxiv.org/abs/2210.12283): turn an informal route into smaller named proof obligations.
- [Prover-Verifier Games](https://arxiv.org/abs/2407.13692): optimize fragile steps for adversarial checkability.
- [STAR-PolyaMath](https://arxiv.org/abs/2605.19338): separate proof reasoning from persistent control, trace-back, and re-planning.
- [Goedel-Architect](https://arxiv.org/abs/2606.06468): maintain and refine a dependency blueprint instead of restarting solved subgraphs.

These papers inspire the workflow. They are not treated as proof authority for a user's theorem.

## License

MIT License. See [LICENSE](LICENSE).

---

# Codex 理论证明工作台

这是一个用于困难理论证明的 Codex skill，负责寻找证明思路、调试失败路线并从旧的 proof state 继续推进。

它适合“关键数学还没有解决”的情况。工作台会固定原命题，寻找真正有决定作用的 lemma 或构造，记住失败路线，按需调用数学工具，并在证明仍未闭合时明确报告 obstruction。

它不是定理百科，也不会把一个缺少关键 lemma 的推导包装成正确证明。它解决的是证明搜索的判断、记忆和验证问题。

## 适用范围

- 运筹、管理科学、优化、排队、库存、调度和控制。
- 动态规划、MDP、Bellman certificate、threshold policy 和 indexability。
- 机制设计、经济理论、IC/IR、envelope 和 cyclic monotonicity。
- Learning theory、bandits、online learning、regret bound 和信息论 lower bound。
- 博弈、匹配、概率构造和 Lovasz Local Lemma。
- 已经失败过，需要读取证据继续推进，而不是重新开始的证明。

如果核心证明已经完成，只需要改善表达、LaTeX 或论文写作，应改用 proof-writing skill。

## 它解决什么

| 常见问题 | Workbench 的处理方式 |
| --- | --- |
| 证明过程中偷偷改了命题 | Statement-fidelity 和 theorem-repair gate |
| 同一个想法换符号后反复出现 | Attempt fingerprint 和 proof-state 去重 |
| 不知道关键构造是什么 | 小例子、tight case 和 pattern mining |
| Missing lemma 其实等于整个 theorem | Proof kernel 和 good-gap/bad-gap 检查 |
| 工具只返回数字，没有形成证明 | Artifact-first tool plan 和 proof translation |
| 某个局部步骤看起来对但可能藏着漏洞 | 条件触发的 prover-verifier review |
| 多次尝试没有进展 | Route decision、有限升级和诚实停止 |

## 安装

把仓库克隆到 Codex 的 skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/jmf-enigma/codex-theory-proof-workbench.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench"
```

随后重启 Codex 或刷新 skill discovery。以后更新可以运行：

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench" pull --ff-only
```

Skill 本身不需要额外 Python package，辅助脚本支持 Python 3.9 及以上版本。Wolfram、Lean、Sage、Z3、CVXPy 等数学后端都是可选项，本仓库不会自动安装。

## 在 Codex 中调用

Codex 遇到困难或重复失败的证明时可以隐式触发这个 skill。显式调用最稳定：

```text
使用 $theory-proof-workbench 证明这个 theorem。先检查精确命题和小型反例。
如果路线不清楚，先找 proof kernel，不要直接写很长的证明。
```

对于已经失败过的证明：

```text
使用 $theory-proof-workbench 的 recovery mode。先读取已有 ledger，说明这次真正
新增了什么，不要再次尝试等价构造。
```

只想寻找思路而不创建完整项目时：

```text
使用 $theory-proof-workbench 做一次 light idea pass。只给我 failure world、
central object、proof kernel 和一个可检查的 next move。
```

这是一个按任务触发的 skill，不是持续运行的后台服务。需要跨多次对话保存的 proof state 会写入项目文件。

## 命令行辅助脚本

这些脚本不是必须手动运行的，Codex 可以在证明过程中自动调用。也可以直接使用：

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/theory-proof-workbench"
```

轻量 idea pass：

```bash
python3 scripts/plan_idea.py "CLAIM"
```

只有精简输出仍找不到 central object 或 proof kernel 时才加入 `--full`。

创建困难证明项目：

```bash
python3 scripts/start_proof.py \
  --title "short-proof-name" \
  --claim "Exact theorem statement"
```

同一个 theorem 已经失败过时，加入 `--mode recovery`。

诊断一个首要 next move：

```bash
python3 scripts/proof_doctor.py path/to/proof_project
```

使用 `--json` 可以获得机器可读输出。提交最终证明前检查 ledger：

```bash
python3 scripts/audit_ledger.py path/to/proof_project/LEDGER.md
```

其他辅助脚本：

| Script | 用途 |
| --- | --- |
| `select_playbook.py` | 根据 claim 选择对应领域 playbook |
| `check_attempt.py` | 识别重复路线或重复构造 |
| `pattern_miner.py` | 从小规模精确序列中猜测规律 |
| `new_lemma_card.py` | 保存可复用的 local lemma |
| `new_trick_card.py` | 保存经过验证的论文或证明 trick |

如果本机数学环境提供 `codex-math-python`，可以用它替换 `python3`；本仓库不依赖这个 wrapper。

## 自适应工作流

Workbench 会选择足够解决当前问题的最轻模式。高级流程是条件触发的，不是每次证明都要执行的 checklist。

| Mode | 适用情况 | 典型输出 |
| --- | --- | --- |
| Direct | 已经看到标准定理、certificate 或短推导 | 经过验证的证明 |
| Micro check | 小证明只缺一个相近 theorem pattern | 定理匹配或明确不匹配 |
| Light idea | Central object 或构造不清楚 | Proof kernel 和 verification hook |
| Project | 证明困难、多 lemma 或需要工具 | 持久化 proof state 和 lemma graph |
| Recovery | 命题以前证明失败过 | No-repeat 诊断和真正的新路线 |

困难证明的主流程是：

1. 固定精确命题、assumptions、domains 和 quantifiers。
2. 检查直接定理，并在小例子和边界情形上尝试反驳。
3. 找到 failure world、central object 和最小的决定性 proof kernel。
4. 比较少量但真正不同的路线。
5. 构建 AND/OR lemma graph，优先处理最不确定的 required child。
6. 工具只能用于产生明确的反例、条件、恒等式、certificate 或 formal lemma。
7. 两次局部尝试都没有缩小 proof state 时，必须修复、重拆、检索、工具检查或停止。
8. 最后组装回原命题并做 adversarial review。

## Proof Project 记忆

`start_proof.py` 会创建持久化项目文件，但不会每次把它们全部加载。`proof_doctor.py` 只推荐当前 proof state 真正需要的文件。

| 文件 | 作用 |
| --- | --- |
| `TRIAGE.md` | 初始模式和立即需要作出的判断 |
| `ATTACK_MATRIX.md` | 证明、反驳和正交证据路线 |
| `IDEA_MAP.md` | Central object、构造、kernel 和 one-step move |
| `LEMMA_QUEUE.md` | AND/OR lemma graph 和节点状态 |
| `WORKSTREAMS.md` | Attempt fingerprint、有限分支和 route decision |
| `PATTERN_SCAN.md` | 从论文、旧 ledger 或 formal library 中有限提取结构 |
| `TOOL_PLAN.md` | 计算或 formalization 之前声明 expected artifact |
| `LEDGER.md` | 持久化 claim、证据、失败记录和 verification status |
| `ESCALATION.md` | 重复失败后允许采取的下一步 |

Idea map、文献扫描、prover-verifier、formal check 和多 Agent 分工都只在当前证明确实需要时启用。

## 数学工具

工具输出只有转化成明确 artifact 后才能进入证明：

- counterexample 或 finite witness；
- exact identity 或 quantified condition；
- KKT、dual、Bellman、LP、SMT 或组合 certificate；
- 没有 admitted gap 的 local Lean theorem；
- 暴露 missing assumption 的 theorem repair。

数值实验和 simulation 可以反驳或启发 conjecture，但不能证明 universal statement。如果最终 assembly 仍含 `sorry`、admitted axiom 或未编码 obligation，那么 formal helper lemma 也不能算完整证明。

### 可选 Wolfram 支持

Wolfram 适合 symbolic simplification、inequality condition、quantifier elimination、KKT algebra、Bellman difference、envelope calculation 和小规模反例搜索。需要从官方 [Wolfram Engine](https://www.wolfram.com/engine/) 与 [WolframScript](https://reference.wolfram.com/language/workflow/InstallWolframScript.html.en) 页面单独安装。

```bash
wolframscript -code '2+2'
```

如果配套的 `math-tools` 环境提供 `wmath` 或 `codex-wmath`，workbench 可以使用这些 wrapper。本仓库不会安装它们。

## 多 Agent 使用

并行 Agent 只在用户明确要求时启用。合理分工应按 artifact 划分，例如 planner、falsifier、retriever、local tool-checker 或 formalizer、reviewer。始终由一个 integrator 负责命题一致性、route choice 和最终 proof status，不应让多个 Agent 同时写同一证明路线的不同版本。

## Proof Status

| Status | 含义 |
| --- | --- |
| `conjecture` | 只有直觉或 pattern match |
| `counterexample-tested` | 在有限测试中没有发现反例 |
| `lemma-conditional` | Theorem 依赖明确列出的 missing lemma |
| `human-proof` | 每个非平凡步骤都有数学依据 |
| `tool-checked` | 脆弱局部步骤有独立 tool artifact |
| `formalized-local` | 重要 local lemma 已经 machine-checked |
| `formalized-complete` | 完整 theorem 和 assembly 都已经 machine-checked |

决定性 lemma 仍然只是猜测时，不能把结果称为 proved。

## 仓库结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── proof-router.md
│   ├── proof-idea-generator.md
│   ├── dp-proof-playbook.md
│   ├── mechanism-design-playbook.md
│   └── ...
└── scripts/
    ├── start_proof.py
    ├── proof_doctor.py
    ├── audit_ledger.py
    └── ...
```

## 开发检查

Workbench 脚本只使用 Python 标准库。Codex 的 skill validator 还需要 PyYAML：

```bash
python3 -m pip install pyyaml
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONPYCACHEPREFIX=/tmp/codex-pycache python3 -m py_compile scripts/*.py
python3 scripts/pattern_miner.py --seq "1,4,9,16,25" --start 1
```

## 设计来源

这个工作流把自动证明与 formalization 研究中的一些思路转化成轻量控制规则：

- [Draft, Sketch, and Prove](https://arxiv.org/abs/2210.12283)：把非形式化路线拆成更小的命名 proof obligations。
- [Prover-Verifier Games](https://arxiv.org/abs/2407.13692)：让脆弱步骤能够经受对抗性检查。
- [STAR-PolyaMath](https://arxiv.org/abs/2605.19338)：把证明推理与持续控制、trace-back 和 re-plan 分开。
- [Goedel-Architect](https://arxiv.org/abs/2606.06468)：维护并修正 dependency blueprint，而不是重复推倒已经解决的 subgraph。

这些论文只提供工作流启发，不会被当成用户命题的证明依据。

## 许可证

MIT License。详见 [LICENSE](LICENSE)。
