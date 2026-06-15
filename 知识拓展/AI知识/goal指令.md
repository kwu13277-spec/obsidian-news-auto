# Codex CLI `/goal` 指令专业技术文档

> 版本：v1.0  
> 日期：2026-05-12  
> 适用对象：Codex CLI 用户、AI coding agent 使用者、希望让 Codex 执行长时程开发任务的工程/科研用户  
> 核心结论：`/goal` 不是普通的一次性 prompt，也不是单纯的计划生成命令，而是 Codex CLI 中用于“设置、保持、暂停、恢复、清除长时程目标”的实验性 slash command。它适合有明确完成条件、可验证测试/检查循环、可分阶段推进的任务。

---

## 1. `/goal` 是什么？

`/goal` 是 Codex CLI 的一个实验性 slash command，用于给当前 Codex 线程设置一个“持久目标”（persistent / durable goal）。

普通 prompt 的基本逻辑是：

```text
用户给出一个任务 -> Codex 回答或执行一轮 -> 当前轮结束
```

而 `/goal` 的逻辑更接近：

```text
用户声明一个目标 -> Codex 将该目标附着到当前线程 -> Codex 围绕目标持续规划、执行、验证、修复 -> 直到目标达成、暂停、清除、阻塞或受预算限制
```

因此，`/goal` 的本质不是“让 Codex 写一段代码”，而是“让 Codex 追踪一个工程目标，并围绕这个目标持续推进”。

官方文档将它描述为：给 Codex 一个面向长时程工作的 durable objective，使 Codex 能够跨多个 turn 朝着一个可验证的停止条件持续工作。它尤其适合代码迁移、大型重构、原型开发、测试修复、prompt/eval 迭代等任务。

---

## 2. 功能定位

### 2.1 一句话理解

`/goal` = 给 Codex 设置一个“必须持续追踪的工程目标”，并要求它在可验证完成条件之前持续推进。

### 2.2 技术定位

从 Codex CLI 的交互模型看，`/goal` 属于 slash command。slash command 是 Codex CLI 中用于控制交互会话的命令体系，例如：

| 指令 | 作用 |
|---|---|
| `/plan` | 切换到计划模式，让 Codex 先提出执行方案 |
| `/status` | 查看当前会话配置、token 使用量、权限等状态 |
| `/diff` | 查看 Codex 对工作区造成的 Git diff |
| `/compact` | 压缩长上下文，保留关键信息 |
| `/resume` | 恢复一个历史会话 |
| `/goal` | 设置或查看一个实验性长时程目标 |

`/goal` 的特殊之处在于：它不是简单改变输出风格，也不是一次性查看状态，而是把一个目标绑定到当前线程，使 Codex 在后续工作中持续参考这个目标。

---

## 3. 启用条件

截至本文档编写时间，`/goal` 是实验性功能，需要启用 `features.goals`。

官方 Codex CLI 文档给出两种启用方式：

### 3.1 方式一：通过 `/experimental` 启用

在 Codex CLI 交互界面中输入：

```text
/experimental
```

然后在实验功能列表中开启 Goals 相关选项。若 CLI 提示需要重启，则退出并重新启动 Codex。

### 3.2 方式二：通过 `config.toml` 启用

打开 Codex 配置文件：

```bash
~/.codex/config.toml
```

加入或修改：

```toml
[features]
goals = true
```

然后重启 Codex CLI。

### 3.3 Windows 路径提示

在 Windows 中，配置文件通常位于：

```text
C:\Users\你的用户名\.codex\config.toml
```

如果你使用 WSL，则 Linux/WSL 内部的路径通常是：

```bash
/home/你的用户名/.codex/config.toml
```

注意：Windows 原生 Codex 与 WSL 内 Codex 可能读取不同的配置文件。你在哪个环境启动 Codex，就应修改对应环境下的配置文件。

---

## 4. 基本语法

### 4.1 设置目标

```text
/goal <objective>
```

示例：

```text
/goal Finish the migration and keep tests green.
```

中文示例：

```text
/goal 完成当前项目的 TypeScript 迁移，确保 npm test 和 npm run lint 全部通过，并保持现有功能行为不变。
```

### 4.2 查看当前目标

```text
/goal
```

作用：查看当前线程是否已经设置 goal，以及当前 goal 的内容和状态。

### 4.3 暂停目标

```text
/goal pause
```

作用：暂停当前目标的追踪与持续推进。适用于你想人工检查差异、重新评估方向、暂时阻止 Codex 继续自动推进的情况。

### 4.4 恢复目标

```text
/goal resume
```

作用：恢复此前暂停的 goal，使 Codex 回到该目标的持续推进状态。

### 4.5 清除目标

```text
/goal clear
```

作用：清除当前线程绑定的 goal。适用于目标已经完成、方向已经改变、目标写错、或者你想重新设定目标的情况。

---

## 5. `/goal` 的生命周期

一个典型 `/goal` 生命周期如下：

```text
未设置目标
  ↓
/goal <objective>
  ↓
目标激活：Codex 开始围绕目标工作
  ↓
阶段性执行：阅读代码/修改文件/运行测试/修复失败/记录进度
  ↓
状态分支：
  ├─ 达成目标 -> 结束或等待用户确认
  ├─ 遇到阻塞 -> 报告阻塞点
  ├─ 用户 pause -> 暂停
  ├─ 用户 resume -> 恢复
  ├─ 用户 clear -> 清除目标
  └─ 预算/限制触发 -> 停止或进入受限状态
```

可以把 `/goal` 理解为一个“目标状态机”。它围绕以下核心状态运行：

| 状态 | 含义 | 用户动作 |
|---|---|---|
| active / pursuing | 目标正在被追踪，Codex 正在推进 | 等待、检查进度、要求汇报 |
| paused | 目标被暂停 | `/goal resume` 恢复 |
| achieved / complete | 目标已被判定达成 | 检查结果，必要时 `/goal clear` |
| blocked / unmet | 目标未达成，存在阻塞 | 补充信息、调整权限、修正目标 |
| budget-limited | 受 token、时间、权限或其他预算约束 | 缩小目标、提高预算、分阶段执行 |
| cleared | 目标已清除 | 可重新设置新目标 |

实际 CLI 显示的状态可能随版本变化，但上述状态足以理解其使用逻辑。

---

## 6. `/goal` 与普通 prompt 的区别

| 维度 | 普通 prompt | `/goal` |
|---|---|---|
| 目标持续性 | 通常只影响当前回合 | 目标附着到当前线程，持续影响后续工作 |
| 适用任务 | 单次问答、局部修改、小问题 | 长时程任务、大型重构、迁移、反复验证 |
| 完成条件 | 常常隐含或模糊 | 应明确写入 objective |
| 验证方式 | 用户手动要求 | 应在 goal 中声明验证命令/验收标准 |
| 中断后恢复 | 依赖上下文与用户重复说明 | goal 本身用于保留目标方向 |
| 风险 | 容易任务漂移 | 若目标写得清楚，漂移风险较低；若目标模糊，风险更高 |

普通 prompt 适合：“帮我解释这段代码”“修复这个报错”“写一个函数”。

`/goal` 适合：“把整个项目迁移到新框架，并确保测试通过”“修复所有 failing tests，直到 CI 绿灯”“按照 PLAN.md 完成一个可运行原型”。

---

## 7. `/goal` 与 `/plan` 的区别

这是使用中最容易混淆的地方。

### 7.1 `/plan` 的定位

`/plan` 用于让 Codex 先制定方案。它强调“思考如何做”。

示例：

```text
/plan 请提出将该项目从 JavaScript 迁移到 TypeScript 的分阶段方案。
```

输出通常是：

```text
1. 检查项目结构
2. 添加 TypeScript 配置
3. 逐步迁移核心模块
4. 添加类型检查
5. 运行测试
```

### 7.2 `/goal` 的定位

`/goal` 用于让 Codex 持续执行到目标状态。它强调“做到什么结果才停”。

示例：

```text
/goal 将该项目从 JavaScript 迁移到 TypeScript，保留现有功能行为，完成后 npm test 和 npm run lint 必须全部通过。
```

这时 Codex 不只是给出方案，而是会围绕该目标持续进行：

```text
读取项目 -> 修改配置 -> 迁移文件 -> 运行测试 -> 修复报错 -> 再次测试 -> 汇报完成状态
```

### 7.3 实战建议

对于复杂任务，推荐组合使用：

```text
第一步：/plan 让 Codex 提出方案
第二步：人工审查并修改方案
第三步：把方案保存为 PLAN.md
第四步：/goal Implement PLAN.md until all acceptance criteria pass
```

这样比直接写一个很长的 `/goal` 更稳，因为 PLAN.md 可以承载详细需求、边界条件、验收标准和禁止事项。

---

## 8. 适合使用 `/goal` 的任务类型

### 8.1 代码迁移

适用场景：

- JavaScript -> TypeScript
- Vue 2 -> Vue 3
- React class components -> hooks
- Jest -> Vitest
- CommonJS -> ESM
- 旧 API -> 新 API

示例：

```text
/goal Migrate this repository from Jest to Vitest. Preserve existing test semantics, update configuration and package scripts, and stop only when all tests pass locally.
```

### 8.2 大型重构

适用场景：

- 拆分巨型文件
- 重构认证模块
- 抽象重复逻辑
- 改善目录结构
- 提升类型安全

示例：

```text
/goal Refactor the authentication module into clear service, repository, and middleware layers. Preserve public behavior and stop only when existing tests pass and the Git diff is limited to auth-related files.
```

### 8.3 测试修复与 CI 修复

适用场景：

- `npm test` 失败
- GitHub Actions 失败
- lint/typecheck 不通过
- flaky tests 需要定位

示例：

```text
/goal Fix the failing test suite. Run npm test after each meaningful fix, avoid changing test expectations unless implementation behavior is demonstrably correct, and stop only when the full test suite passes.
```

### 8.4 原型开发

适用场景：

- 根据 PLAN.md 做一个 MVP
- 根据截图实现前端界面
- 做一个可运行 demo
- 搭建工具脚手架

示例：

```text
/goal Implement PLAN.md as a working MVP. Create tests for each milestone, verify the app builds and launches, and keep a concise progress log in GOAL_PROGRESS.md.
```

### 8.5 Prompt / Eval 迭代

适用场景：

- 有 eval suite
- 需要反复优化 prompt
- 需要根据失败样本调整策略

示例：

```text
/goal Improve the prompt until the eval score increases by at least 10 percentage points or no further improvement is observed after three consecutive iterations. Record each prompt revision and eval result.
```

---

## 9. 不适合使用 `/goal` 的任务类型

`/goal` 并不适合所有任务。

| 不适合场景 | 原因 | 推荐替代方式 |
|---|---|---|
| 单次解释问题 | 不需要长时程状态 | 普通 prompt |
| 开放式研究 | 缺少明确完成条件 | 先让 Codex 制定 research plan |
| 一堆无关任务 | goal 容易发散 | 拆成多个独立 goal |
| 高风险生产操作 | 自动推进可能误操作 | 手动 review + 小步执行 |
| 没有测试/验收标准的重构 | 无法判断是否完成 | 先补充验收标准 |
| 需要频繁人工决策的设计任务 | Codex 可能错误推进 | 使用 `/plan` + 人工确认 |

错误示例：

```text
/goal 帮我把这个项目做得更好。
```

问题：目标过于抽象，Codex 无法判断“更好”意味着什么。

更好的写法：

```text
/goal Improve the project by reducing TypeScript errors to zero, removing unused dependencies, and making npm test and npm run lint pass. Do not change public APIs unless necessary, and document any necessary API changes.
```

---

## 10. 高质量 `/goal` 的写法

一个高质量 `/goal` 通常包含 6 个要素：

```text
/goal [目标对象] + [具体任务] + [约束边界] + [验证方式] + [停止条件] + [进度记录方式]
```

### 10.1 模板

```text
/goal Complete <objective>.
Scope: <files/modules/features that may be changed>.
Constraints: <what must not change>.
Validation: <commands/tests/checks to run>.
Stop when: <verifiable end state>.
Progress: <how to report or record progress>.
```

### 10.2 中文模板

```text
/goal 完成 <具体目标>。
范围：只允许修改 <文件/模块/功能范围>。
约束：不得改变 <公共 API/数据库结构/现有行为/视觉样式>，除非有明确理由。
验证：每个阶段运行 <测试命令/构建命令/lint/typecheck>。
停止条件：当 <明确、可验证的完成状态> 达成时停止。
进度记录：将关键步骤、失败原因、修复方式记录到 <文件或最终汇报>。
```

### 10.3 优质示例

```text
/goal Complete the migration from CommonJS to ESM.
Scope: only source files, test config, package scripts, and import/export statements.
Constraints: preserve public APIs and runtime behavior; do not introduce new dependencies unless necessary.
Validation: run npm test, npm run lint, and npm run typecheck after each major checkpoint.
Stop when: all three validation commands pass and the package can be imported from a clean install.
Progress: maintain a short checklist in MIGRATION_PROGRESS.md.
```

### 10.4 较差示例

```text
/goal 重构这个项目。
```

问题：

- 不知道重构哪个部分
- 不知道能不能改 API
- 不知道如何验证
- 不知道什么时候停止
- 容易产生大范围无意义改动

---

## 11. 推荐工作流：PLAN.md + `/goal`

对于大型项目，不建议直接把所有要求写进一条 `/goal`。更稳的方式是先准备一个 `PLAN.md`。

### 11.1 文件结构

```text
project/
  PLAN.md
  GOAL_PROGRESS.md
  package.json
  src/
  tests/
```

### 11.2 PLAN.md 示例结构

```markdown
# PLAN.md

## Objective
Migrate the project from Jest to Vitest while preserving all existing test behavior.

## Scope
- package.json
- vitest.config.ts
- test setup files
- test imports and mocks

## Out of scope
- Do not rewrite application logic.
- Do not change public APIs.
- Do not remove tests unless they are obsolete and explicitly justified.

## Milestones
1. Inspect current Jest configuration.
2. Add Vitest dependencies and config.
3. Convert test setup files.
4. Convert incompatible Jest APIs.
5. Run full test suite.
6. Fix failures.
7. Remove obsolete Jest configuration.

## Validation
- npm test
- npm run lint
- npm run typecheck

## Done when
- All validation commands pass.
- No Jest dependency remains unless explicitly justified.
- GOAL_PROGRESS.md summarizes what changed and why.
```

### 11.3 对应 `/goal`

```text
/goal Implement PLAN.md exactly. Work milestone by milestone, keep GOAL_PROGRESS.md updated, and stop only when npm test, npm run lint, and npm run typecheck all pass.
```

这种方式有三个优点：

1. goal 本身更短、更稳定。
2. 复杂约束放入文件，便于人工审查。
3. Codex 可以反复回读 PLAN.md，降低长任务漂移。

---

## 12. 与 Agent Skills 的关系

Codex 的 Agent Skills 是另一套机制：它通过 `SKILL.md` 封装可复用的专业工作流、规则、脚本和参考资料。官方文档指出，skill 是一个包含 `SKILL.md` 的目录，可附带 scripts、references、assets 等资源；Codex 可以显式或隐式调用 skill。

### 12.1 `/goal` 与 skill 的区别

| 维度 | `/goal` | Agent Skill |
|---|---|---|
| 作用 | 设置当前线程的长时程目标 | 提供可复用能力/流程/知识 |
| 生命周期 | 绑定到当前 thread 的目标状态 | 安装后可在多个任务中复用 |
| 触发方式 | 用户输入 `/goal ...` | 显式 `$skill` 或 Codex 根据描述隐式选择 |
| 内容 | 一个 objective + 目标状态 | `SKILL.md` + 可选脚本/参考资料/模板 |
| 适用 | “这次要做到什么结果” | “遇到某类任务时应该怎么做” |

### 12.2 组合使用方式

最强的用法是：

```text
Skill 负责规范流程，/goal 负责驱动执行。
```

例如你有一个 `wp-spec-to-goal` skill，用于把模糊需求转换为 WordPress 插件开发规范。那么工作流可以是：

```text
1. 用 skill 生成 SPEC.md / PLAN.md / acceptance criteria
2. 人工审查并修改
3. 使用 /goal 执行该计划，直到测试与验收条件通过
```

示例：

```text
$project-migration-skill 根据当前仓库生成迁移计划和验收标准。
```

然后：

```text
/goal Implement the generated PLAN.md using the project-migration-skill workflow. Stop only when all acceptance criteria pass.
```

---

## 13. 安全与权限控制

`/goal` 适合长时间推进任务，因此权限与边界尤其重要。

### 13.1 建议使用 Git 保护

执行前：

```bash
git status
git checkout -b codex-goal/<task-name>
git add .
git commit -m "baseline before codex goal"  # 如果当前改动应保存
```

执行中定期查看：

```text
/diff
/status
```

执行后：

```bash
git diff
git status
npm test
npm run lint
npm run typecheck
```

### 13.2 设置明确的禁止事项

在 goal 或 PLAN.md 中明确写：

```text
Do not delete tests.
Do not change public APIs.
Do not modify database migrations.
Do not introduce new dependencies without justification.
Do not touch files outside src/auth and tests/auth.
```

### 13.3 长任务不要直接作用于主分支

推荐：

```bash
git checkout -b codex-goal-auth-refactor
```

不推荐：

```bash
git checkout main
/goal 重构整个项目
```

### 13.4 高风险操作应要求暂停

如果任务涉及数据库迁移、生产配置、部署脚本、鉴权逻辑，应在 goal 中加入：

```text
Pause and ask for confirmation before changing database migrations, production deployment files, authentication policies, or secrets-related configuration.
```

---

## 14. 验证循环设计

`/goal` 的质量高度依赖验证循环。如果没有验证循环，Codex 只能依赖自我判断，容易产生“看起来完成但实际没完成”的问题。

### 14.1 常见验证命令

| 项目类型 | 验证命令示例 |
|---|---|
| Node.js | `npm test`, `npm run lint`, `npm run typecheck`, `npm run build` |
| Python | `pytest`, `ruff check .`, `mypy .` |
| Rust | `cargo test`, `cargo clippy`, `cargo build` |
| Go | `go test ./...`, `go vet ./...` |
| 前端 | `npm run build`, `npm run test:e2e`, Playwright screenshot comparison |
| 文档 | link checker, markdownlint, doctest |

### 14.2 验证命令应写进 goal

差：

```text
/goal 修复测试。
```

好：

```text
/goal Fix the failing tests. Run npm test after each meaningful change, run npm run lint before stopping, and stop only when both commands pass.
```

### 14.3 对视觉任务使用截图验证

前端迁移或 UI 重构时，应明确：

```text
Use Playwright to compare the current UI against the reference screenshots. Preserve layout, spacing, typography, and interactive behavior.
```

---

## 15. 常见错误与修正

### 15.1 目标太大

错误：

```text
/goal 把这个项目全部优化好。
```

修正：

```text
/goal Reduce TypeScript errors to zero in src/auth only. Do not change runtime behavior. Run npm run typecheck after each checkpoint and stop when typecheck passes.
```

### 15.2 没有停止条件

错误：

```text
/goal 改进用户体验。
```

修正：

```text
/goal Improve the checkout page by reducing form validation errors, adding inline error messages, and preserving the current visual design. Stop when Playwright checkout tests pass and manual test steps in CHECKOUT_QA.md are completed.
```

### 15.3 没有修改边界

错误：

```text
/goal 重构认证模块。
```

修正：

```text
/goal Refactor only src/auth and tests/auth. Do not modify database schema, public API routes, or deployment config. Stop when auth tests and full test suite pass.
```

### 15.4 用 `/goal` 做开放式研究

错误：

```text
/goal 调研所有 AI coding agent。
```

修正：

```text
/plan 为 AI coding agent 调研设计一个研究框架，包括检索范围、评价指标、输出格式和时间边界。
```

待计划确认后，再设置：

```text
/goal Execute RESEARCH_PLAN.md and produce REPORT.md with cited sources, comparison table, and reproducible notes.
```

---

## 16. 故障排查

### 16.1 输入 `/goal` 没有反应或列表中没有 `/goal`

检查：

```bash
codex --version
```

然后检查配置：

```toml
[features]
goals = true
```

再重启 Codex CLI。

可能原因：

| 原因 | 处理 |
|---|---|
| Codex CLI 版本过旧 | 更新到较新版本 |
| 未启用 `features.goals` | 使用 `/experimental` 或修改 `config.toml` |
| 修改了错误的配置文件 | 确认是当前运行环境的 `~/.codex/config.toml` |
| TOML 格式错误 | 检查 `[features]` 是否重复、缩进/引号是否异常 |
| 未重启 CLI | 完全退出后重新进入 |

### 16.2 `/goal` 设置后 Codex 改动范围过大

处理：

```text
/goal pause
```

然后人工补充边界：

```text
继续前请限制修改范围：只允许修改 src/auth 和 tests/auth，不得修改 package.json、数据库迁移和部署配置。请先汇报当前 diff，再等待确认。
```

必要时：

```text
/goal clear
```

重新设置更窄的目标。

### 16.3 Codex 反复修复但测试仍失败

处理策略：

1. 暂停 goal。
2. 要求 Codex 输出失败测试分组。
3. 将大 goal 拆成多个小 goal。
4. 先修复最底层、最确定的问题。
5. 禁止 Codex 通过删除测试或放宽断言来“修复”。

示例：

```text
/goal pause
```

```text
请根据当前 npm test 输出，将失败用例按原因分组：配置问题、类型问题、mock 问题、真实逻辑 bug。不要修改文件，只输出诊断表。
```

---

## 17. 最佳实践清单

使用 `/goal` 前，建议逐项确认：

- [ ] 当前项目已经进入独立 Git 分支。
- [ ] 当前工作区没有未保存的重要改动。
- [ ] goal 中有明确目标。
- [ ] goal 中有明确修改范围。
- [ ] goal 中有明确禁止事项。
- [ ] goal 中有验证命令。
- [ ] goal 中有停止条件。
- [ ] 对高风险文件设置了暂停要求。
- [ ] 对长期任务要求记录进度。
- [ ] 任务可以被拆成阶段性 checkpoint。

---

## 18. 推荐 `/goal` 模板库

### 18.1 修复测试

```text
/goal Fix the failing test suite. Do not delete or weaken tests unless a test is demonstrably obsolete and you document why. Run npm test after each meaningful fix and stop only when the full suite passes.
```

### 18.2 TypeScript 类型修复

```text
/goal Reduce TypeScript errors to zero. Preserve runtime behavior and public APIs. Run npm run typecheck after each checkpoint. Stop only when typecheck passes without errors.
```

### 18.3 前端页面还原

```text
/goal Implement the target UI from the provided screenshots. Preserve layout, spacing, typography, colors, and responsive behavior. Use Playwright to verify the page visually and stop only when the app builds and the screenshot comparison is acceptable.
```

### 18.4 重构模块

```text
/goal Refactor <module> for maintainability while preserving public behavior. Only modify <allowed paths>. Add or update tests where necessary. Stop when unit tests, integration tests, lint, and typecheck all pass.
```

### 18.5 按 PLAN.md 执行

```text
/goal Implement PLAN.md exactly. Work milestone by milestone, keep GOAL_PROGRESS.md updated, and stop only when all acceptance criteria in PLAN.md pass.
```

### 18.6 科研代码项目清理

```text
/goal Clean and standardize this research analysis repository. Scope: scripts, environment files, README, and reproducibility notes. Do not change statistical logic unless a bug is found and documented. Stop when the analysis scripts run from a clean environment and README contains exact reproduction steps.
```

---

## 19. 面向科研/数据分析用户的用法建议

如果你用 Codex 做科研代码，例如 UKB、WES、蛋白组学、代谢组学或流行病学分析，不建议直接写：

```text
/goal 帮我完成这个科研项目。
```

更合适的方式是将任务拆成可验证的工程单元。

### 19.1 数据清洗 goal

```text
/goal Implement the data preprocessing pipeline described in PREPROCESSING_PLAN.md. Do not change cohort definitions without documenting the reason. Stop when the script produces the expected cleaned dataset, missingness report, and reproducibility log.
```

### 19.2 Cox 回归分析 goal

```text
/goal Implement the Cox regression analysis in R according to ANALYSIS_PLAN.md. Preserve the specified covariate sets, generate model tables, check proportional hazards assumptions where specified, and stop when all result tables are reproducible from a clean run.
```

### 19.3 中介分析 goal

```text
/goal Implement the mediation analysis pipeline according to MEDIATION_PLAN.md. Use the specified exposure, mediator, outcome, covariates, and bootstrap settings. Stop when all mediation result tables and diagnostic logs are generated.
```

### 19.4 机器学习分析 goal

```text
/goal Implement the ML pipeline in ML_PLAN.md with nested cross-validation, leakage prevention, model comparison, and SHAP interpretation. Stop when all models produce reproducible metrics and figures.
```

关键原则：科研场景下，`/goal` 应服务于“可复现代码产物”，而不是替代你做统计学决策。暴露定义、结局定义、协变量选择、缺失值策略、敏感性分析等核心科学决策，应由你先写入计划文件。

---

## 20. 推荐使用策略

### 20.1 小任务不用 `/goal`

例如：

```text
解释这个报错
写一个 Python 函数
帮我改 README 的一段话
```

这些用普通 prompt 即可。

### 20.2 中型任务先 `/plan` 再 `/goal`

例如：

```text
/plan 设计将当前项目测试框架从 Jest 迁移到 Vitest 的方案。
```

确认方案后：

```text
/goal 按照确认后的迁移方案执行，直到 npm test、npm run lint、npm run typecheck 全部通过。
```

### 20.3 大型任务用文件化规范

推荐结构：

```text
SPEC.md          # 需求规范
PLAN.md          # 执行计划
ACCEPTANCE.md    # 验收标准
GOAL_PROGRESS.md # 进度记录
```

然后：

```text
/goal Implement SPEC.md and PLAN.md. Stop only when all acceptance criteria in ACCEPTANCE.md pass. Keep GOAL_PROGRESS.md updated.
```

---

## 21. 总结

`/goal` 是 Codex CLI 中面向长时程 agentic coding 的关键能力。它将一次性对话扩展为目标驱动的持续执行过程，使 Codex 能围绕一个明确 objective 进行多轮规划、修改、测试和修复。

但 `/goal` 的效果取决于目标质量。一个好的 goal 必须具备：

1. 明确目标；
2. 明确范围；
3. 明确禁止事项；
4. 明确验证命令；
5. 明确停止条件；
6. 明确进度记录方式。

最推荐的工作方式不是直接写一个超长 `/goal`，而是：

```text
先用 /plan 生成方案
↓
人工审查
↓
写入 PLAN.md / ACCEPTANCE.md
↓
用 /goal 驱动 Codex 执行
↓
用 /diff /status /测试命令持续审查
```

对于工程开发、科研代码、数据分析 pipeline、前端实现、测试修复和大型迁移任务，`/goal` 可以显著降低反复手动提示的成本。但对于开放式、无边界、无验证标准的任务，它也可能放大错误。因此，使用 `/goal` 的核心不是“让 Codex 自己随便做”，而是“把目标、约束、验证和停止条件写清楚，让 Codex 在清晰边界内持续执行”。
## 23. 参考资料

1. OpenAI Developers. **Follow a goal | Codex use cases**. https://developers.openai.com/codex/use-cases/follow-goals  
2. OpenAI Developers. **Slash commands in Codex CLI**. https://developers.openai.com/codex/cli/slash-commands  
3. OpenAI Developers. **Agent Skills – Codex**. https://developers.openai.com/codex/skills  
4. OpenAI Codex GitHub Issue #20536. **Document the /goal CLI command and Goals lifecycle in slash-command docs**. https://github.com/openai/codex/issues/20536  
5. OpenAI Codex changelog. https://developers.openai.com/codex/changelog
