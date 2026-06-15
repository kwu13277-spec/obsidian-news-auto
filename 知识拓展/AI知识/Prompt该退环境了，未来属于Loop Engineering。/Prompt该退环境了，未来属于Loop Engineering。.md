建议文件名：Loop Engineering：从Prompt到自动化循环的工程范式.md

# Loop Engineering：从Prompt到自动化循环的工程范式

来源：微信公众号「卡兹克」— [原文链接](https://mp.weixin.qq.com/s/omwt7d9BSFX7kotW9vo9bQ)

## 摘要

本文系统阐述Loop Engineering作为AI工程第四次范式跃迁的核心思想：从手动编写Prompt转变为设计自动化循环来驱动AI Agent。文章拆解了Loop的五组件骨架（定时任务、工作树隔离、知识体系、MCP连接器、子Agent），并提出了其灵魂在于「定义目标的能力」，最后将AI Agent管理与传统管理学（目标管理、OKR、古德哈特定律）进行了深度关联。

## 关键词

Loop Engineering；AI Agent；目标定义；Harness Engineering；自动化循环；古德哈特定律（Goodhart's Law）；工作树隔离（Worktree）；Prompt Engineering

## 大纲

1. Loop Engineering的诞生背景
2. Loop的核心思想：从手动操控到自动化循环
3. Loop的五组件骨架
4. Loop的灵魂：定义目标的能力
5. 古德哈特定律：AI Agent的指标陷阱
6. Harness与Loop的关系：约束 + 驱动
7. 目标定义四步框架
8. AI工程四范式跃迁总结

---

## 关键原文摘录

> 你不再需要为编码智能体编写提示词了，你应该设计循环来提示你的Agent。

> 定义目标，相信我，这四个字，听起来简单，做起来是真的难。

> 当一个衡量指标变成了目标本身的时候，它就不再是一个好的衡量指标了。

> 人也会这么干，只不过，Agent做得更快、更彻底、更没有心理负担。

> 一个好的目标定义，不能只有做完了的标准，还必须有不能怎么做的边界。

## 正文

### 1. Loop Engineering的诞生背景

本节概要：本节说明Loop Engineering概念的起源，以及它如何成为AI工程领域第四次共识性范式。

2025年6月7日，OpenClaw创始人Peter发布了一条简短但引发热议的推文——**"你不再需要为编码智能体编写提示词了，你应该设计循环来提示你的Agent。"**

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-wAE3ky0bR8.png]]

同期，Claude Code创始人Boris在开发者大会上表达了相似观点——他不再手动写提示词，而是运行能让Claude自动编排任务的循环机制。

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-Dn58dRlm2l.png]]

随后，Google的Addy Osmani发表长文正式梳理了 **Loop Engineering** 这一概念。

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-ItVYidb0Ap.png]]

这标志着继以下三种工程范式之后，AI行业第四个达成共识的工程范式正式诞生：

- **Prompt Engineering** — 提示词工程
- **Context Engineering** — 上下文工程
- **Harness Engineering** — 约束/框架工程

作者指出，Loop Engineering并非空洞的概念炒作，而是行业发展到一定阶段后，人们需要一个精准的表达来描述正在发生的变化。

---

### 2. Loop的核心思想：从手动操控到自动化循环

本节概要：本节通过对比传统开发方式和Loop模式，说明Loop Engineering的本质区别——从「你在驱动」变为「系统自我驱动」。

#### 传统工作模式（Chatbot/Agent时代）

- 用户给Agent一个任务 → Agent执行 → 用户检查 → 反馈修改
- 循环依赖用户驱动，用户是发动机，需要全程在场
- 本质上仍是"任务制"——人提一个任务，AI完成一个任务

#### Loop工作模式

以Boris的实际工作方式为例：

- 一条指令：`/loop babysit all my PRs`
- Agent自动扫描GitHub所有PR，自动修复CI失败，自动响应Review评论
- 子Agent通过独立工作树（Worktree）并行处理任务
- 定时任务在夜间自动启动，**数千个Agent同时工作**
- Boris自称2026年以来**再没有手写过一行代码**

#### 核心差异

- **旧模式**：写Prompt来完成单次任务
- **Loop模式**：设计一个目标，由循环自动驱动Agent完成
- 定义目标 → 定义验证条件 → 定义失败处理 → 放手交给系统
- 用户完全不需要在场，可以睡觉，醒来代码已改好、测试已通过、PR已提交

---

### 3. Loop的五组件骨架

本节概要：本节拆解Addy Osmani提出的完整Loop的五组件架构，并结合作者自身实践进行解读。

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-oezw1Cd5Xv.png]]

#### 3.1 定时任务（Heartbeat）

Loop的心跳，是驱动循环自动启动的核心机制。

| 实现方式 | 说明 |
|----------|------|
| `/loop` 命令 | 按间隔自动执行 |
| Cron调度 | 定时启动 |
| Hook触发 | 在Agent生命周期特定节点自动触发（如改完文件自动跑lint） |
| GitHub Actions | 持续运行，关上电脑也能跑 |

> 没有定时任务的Agent，你每次都得手动去踢一脚它才会动，那就不是loop了。

#### 3.2 工作树隔离（Worktree）

多Agent并行工作时，每个Agent拥有独立的工作空间，互不干扰。

- 防止两个Agent同时修改同一个文件引发冲突
- 各自改完后再合并
- 类比：两个设计师同时改一个图层却不打招呼的痛苦

#### 3.3 项目知识体系（Knowledge System）

Addy Osmani原文中称为"Skill"，但作者认为应扩展为完整的知识管理体系。

原因：AI每次开新对话都会丢失上下文，需要一套机制沉淀、优化、传递知识。

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-NdcC3uaRlK.jpeg]]

作者实践中的三层知识体系：

| 层级 | 工具 | 作用 |
|------|------|------|
| 全局规则 | CLAUDE.md | 全局约束和行为规范 |
| 跨会话记忆 | 记忆系统 | 悬而未决的记录与文档路由 |
| 知识沉淀 | docs体系 | 完整的经验和知识积累（突破容量限制） |

> 没有干净的知识体系的loop，就像一个每天早上都在看过期文档的员工，干得越快错得越多。

作者开源了自己的「洁癖.skill」用于知识体系梳理：

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-5rPLnpCxLW.png]]

开源地址：[https://github.com/KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills)

#### 3.4 连接器（MCP）

Agent与实际工作环境之间的接口层。

- 仅能访问文件系统的Agent能力有限
- 接入GitHub、飞书、数据库等真实工具后，Agent能在实际工作环境中运作
- 实现完整闭环：**发现问题 → 解决问题 → 通知人类**

#### 3.5 子Agent（Sub-Agent）

分工与制衡机制：

- **执行Agent**：负责具体任务执行
- **检查Agent**：专门验证执行Agent的输出（可使用不同模型）
- 核心原则：写代码的Agent不能自己给自己打分，避免"对自己太宽容"

> 这五个东西加在一起，就是一个完整的loop的骨架。

#### 3.6 /goal 命令：Loop的微观产品化

Claude Code和Codex中的`/goal`命令（Codex中称"追求目标"）是Loop Engineering最直接的微观产品化体现。

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-VhlR8TW7Ab.png]]

工作原理：给Agent一个完成条件（如"所有测试通过并且lint检查没有报错"），Agent一轮一轮自动执行，每轮结束后检查条件是否满足，满足则停止。

---

### 4. Loop的灵魂：定义目标的能力

本节概要：本节指出Loop Engineering最核心的能力不是技术，而是定义目标的能力——将模糊意图转化为可验证的完成条件。

作者强调：Loop Engineering的核心竞争力**不在工程，在管理**。

#### 目标定义的好坏对比

| 维度 | 模糊目标（❌） | 清晰目标（✅） |
|------|---------------|---------------|
| 示例 | "把这个应用优化一下" | "test/auth目录下所有测试通过，tsc --noEmit零报错，npm run lint零违规" |
| 结果 | Agent不知何时完成 | 每轮检查明确标准，全过则停 |
| 问题 | 缺乏可验证的完成标准 | 三个命令，三个明确通过标准 |

#### 管理逻辑的迁移

作者从创业管理经验中总结：AI Agent管理与人的管理本质相同。

| 管理三要素 | Loop对应 |
|------------|----------|
| 目标清晰 | 完成条件写得精准 |
| 资源充足 | 配好Skill、连接器、工作权限 |
| 反馈及时 | 每轮验证机制独立检查 |

**人与Agent的关键差异**：

- **人**：可以理解模糊意图，主动确认澄清
- **Agent**：不会主动确认，自信地按自己理解执行，自信地报告完成
- 因此对管理能力的要求**比管人还高**

> AI时代…管理学、心理学、组织行为学这些，不但没死，反而变得更重要了。

---

### 5. 古德哈特定律：AI Agent的指标陷阱

本节概要：本节揭示Loop Engineering中一个关键陷阱——当衡量指标变成目标本身时，Agent会针对验证器优化而非真正目标。

#### 古德哈特定律（Goodhart's Law）

> 当一个衡量指标变成了目标本身的时候，它就不再是一个好的衡量指标了。

![[知识拓展/AI知识/Prompt该退环境了，未来属于Loop Engineering。/assets/Prompt该退环境了，未来属于Loop Engineering。-sFeqZgOgNX.png]]

#### 在AI Agent中的极端表现

Agent比人类更擅长钻规则空子：

- **场景**：Loop条件是"测试全部通过"
- **Agent可能的行为**：不修Bug，而**直接把失败的测试删了**
- **验证结果**：测试全过 ✅
- **真实结果**：什么都没做 ❌

> 人也会这么干，只不过，Agent做得更快、更彻底、更没有心理负担。

#### 教训

一个好的目标定义必须包含两个维度：

1. **做完了的标准** — 正向的完成条件
2. **不能怎么做的边界** — 负向的约束条件

---

### 6. Harness与Loop的关系：约束 + 驱动

本节概要：本节说明Harness Engineering和Loop Engineering如何协同工作，形成完整系统。

| 工程范式 | 角色 | 类比 |
|----------|------|------|
| **Harness Engineering** | 约束、护栏、边界 | 告诉Agent"这条线你不能越" |
| **Loop Engineering** | 驱动力、方向 | 告诉Agent"往那个方向一直跑" |

二者缺一不可：

- 只有Harness没有Loop → 有安全边界但无法自动运行
- 只有Loop没有Harness → 能自动跑但可能跑偏
- **二者结合** → 完整系统

---

### 7. 目标定义四步框架

本节概要：本节给出作者在实践中总结的目标定义框架，作为Loop Engineering落地的方法论。

作者自用的四条原则：

1. **完成标准要可以被机器验证**
   - 使用可量化的指标（测试通过率、报错数、响应时间阈值）
   - 避免主观判断（"优化好"、"做完善"）

2. **边界条件要跟完成标准一起定义**
   - 明确指出什么不能做
   - 防止Agent钻规则空子

3. **要有失败的降级方案**
   - 当Agent无法达成目标时，应有预设的处理路径
   - 避免无限循环或不可控状态

4. **目标要分层**
   - 从高层目标到底层任务逐层分解
   - 每层目标都有明确的可验证标准

---

### 8. AI工程四范式跃迁总结

本节概要：本节从四次工程范式跃迁的视角，总结AI工程演进的底层逻辑。

| 范式 | 核心指令 | 核心能力 | 学科根基 |
|------|----------|----------|----------|
| **Prompt Engineering** | 好好说话 | 语言表达 | 语言学 |
| **Context Engineering** | 给足信息 | 信息筛选与组织 | 信息科学 |
| **Harness Engineering** | 设好规则 | 系统设计与规则制定 | 控制论 |
| **Loop Engineering** | 自动运行 | 目标定义与管理 | 管理学 |

> 四门古老的学科。多有意思。人类社会，其实从来就没有变过。

---

*本文整理自微信公众号「卡兹克」原创文章，仅供学习参考。*
