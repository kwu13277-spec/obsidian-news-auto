# Superpowers：给 AI Agent 使用的 Skill 工作流框架

> 版本整理日期：2026-05-12  
> 项目地址：https://github.com/obra/superpowers  
> 适合对象：Claude Code、Codex CLI、Codex App、Gemini CLI、Cursor、OpenCode、GitHub Copilot CLI 等 coding agent 用户。

---

## 1. 先说结论

**Superpowers 不是普通的代码库，也不是一个单独的 Python 包。**

它更像是一套给 AI 编程 Agent 使用的 **开发工作流系统**。  
它把很多优秀的软件开发习惯整理成一个个 `skill`，让 Agent 在写代码、调试、规划项目、做代码审查时，按照固定流程执行，而不是想到哪里写到哪里。

一句话理解：

```text
Superpowers = 给 AI 编程 Agent 安装一套“工程纪律系统”
```

普通 Agent 可能是这样工作的：

```text
用户提出需求
  ↓
Agent 直接写代码
  ↓
代码可能能跑，也可能不能跑
  ↓
出错后继续修补
  ↓
项目越来越乱
```

用了 Superpowers 后，理想流程是：

```text
用户提出需求
  ↓
Agent 先澄清需求
  ↓
Agent 给出设计方案
  ↓
用户确认方案
  ↓
Agent 写实施计划
  ↓
Agent 按计划开发
  ↓
开发时先写测试，再写代码
  ↓
完成后代码审查
  ↓
最后验证是否真的完成
```

所以，它的核心价值不是“让模型多知道知识”，而是让 Agent **更稳定、更有流程、更像一个工程师团队**。

---

## 2. Superpowers 到底是什么

Superpowers 官方介绍是：

> A complete software development methodology for your coding agents.

通俗翻译：

> 它是一套给 AI 编程 Agent 使用的软件开发方法论。

它由两部分组成：

```text
Superpowers
├── 一组可复用的 skills
└── 一套要求 Agent 使用这些 skills 的初始规则
```

每个 skill 通常是一个文件夹，里面有一个 `SKILL.md` 文件。

大概结构类似：

```text
skills/
  using-superpowers/
    SKILL.md
  brainstorming/
    SKILL.md
  writing-plans/
    SKILL.md
  test-driven-development/
    SKILL.md
  systematic-debugging/
    SKILL.md
  verification-before-completion/
    SKILL.md
```

你可以把 `SKILL.md` 理解为：

```text
给 Agent 看的操作手册
```

里面会告诉 Agent：

- 什么时候应该使用这个 skill；
- 使用时必须遵守什么流程；
- 哪些步骤不能跳过；
- 如何验证任务是否完成；
- 常见错误有哪些；
- 遇到特殊情况应该怎么处理。

---

## 3. 为什么需要 Superpowers

AI 编程 Agent 很强，但常见问题也很明显。

### 3.1 普通 Agent 的常见问题

很多 Agent 会出现这些行为：

```text
1. 需求还没问清楚，就直接写代码
2. 没有设计方案，边写边想
3. 没有测试，代码看起来能跑但不可靠
4. 遇到 bug 靠猜，改来改去
5. 完成后没有验证，却说“已经完成”
6. 项目稍微复杂一点，就容易偏离原目标
```

这些问题在小任务里不明显，但在真实项目中会非常危险。

例如你让 Agent 写一个 UKB 数据分析脚本，如果它没有先确认：

- 暴露变量是什么；
- 结局变量是什么；
- 协变量有哪些；
- ICD 编码怎么定义；
- 缺失值如何处理；
- Cox 模型怎么建；
- 输出结果格式是什么；

它直接写代码，很容易得到一个“看起来完整、实际上不可靠”的脚本。

### 3.2 Superpowers 的作用

Superpowers 试图让 Agent 养成这些习惯：

```text
先问清楚，再设计
先设计，再计划
先计划，再写代码
先写测试，再写实现
先验证，再宣布完成
```

这就是它的核心价值。

---

## 4. Superpowers 的基本工作流

官方 README 中列出了一个基础工作流。通俗理解如下。

---

### 第一步：brainstorming

作用：**先把需求问清楚。**

Agent 不应该一上来就写代码，而是先问：

```text
你到底想做什么？
输入是什么？
输出是什么？
边界条件是什么？
有没有现有代码？
有没有必须遵守的技术栈？
哪些行为一定不能发生？
```

例如你说：

```text
帮我写一个 PDF 转 Markdown 的工具
```

Agent 应该先问：

```text
是否需要 OCR？
是否需要保留表格？
是否需要批量处理？
输出 Markdown 是否需要固定模板？
PDF 是英文论文还是中文文件？
```

---

### 第二步：using-git-worktrees

作用：**给开发任务创建隔离环境。**

简单说，就是不要直接在主分支乱改代码，而是创建一个独立的工作区或分支。

这样做的好处：

```text
主项目不容易被改坏
不同任务可以并行
开发失败可以直接丢弃
方便之后合并或提交 PR
```

---

### 第三步：writing-plans

作用：**把设计方案拆成具体任务。**

不是简单写一句“实现功能”，而是拆成非常具体的小步骤。

一个好的计划应该包括：

```text
要创建哪些文件
要修改哪些文件
每个文件负责什么
每一步怎么实现
每一步怎么测试
每一步完成后如何验证
```

例如：

```text
任务 1：创建 tests/test_pdf_reader.py
任务 2：写一个失败测试，验证能读取 PDF 文本
任务 3：创建 src/pdf_reader.py
任务 4：实现最小 PDF 读取函数
任务 5：运行测试，确认通过
任务 6：提交代码
```

这比“写一个 PDF 读取模块”清楚得多。

---

### 第四步：subagent-driven-development / executing-plans

作用：**按照计划执行开发。**

如果任务很复杂，Agent 可以把不同任务交给不同子 Agent 执行。  
如果平台不支持子 Agent，也可以按计划一批一批执行。

核心原则：

```text
不要自由发挥
不要跳过计划
不要未经验证就进入下一步
```

---

### 第五步：test-driven-development

作用：**强制 TDD：先写测试，再写代码。**

TDD 的基本流程是：

```text
RED：先写一个失败测试
GREEN：写最少的代码让测试通过
REFACTOR：在测试通过的前提下重构代码
```

也就是：

```text
先证明“现在还不行”
再写代码让它“刚好可以”
最后再整理代码质量
```

这能减少 Agent 写出一堆看起来完整、但没人验证的代码。

---

### 第六步：requesting-code-review

作用：**开发完成后，请另一个视角检查代码。**

代码审查会关注：

```text
是否符合原计划
是否有明显 bug
是否有过度设计
是否有重复代码
是否缺少测试
是否破坏现有功能
```

这一步是防止 Agent “自我感觉良好”。

---

### 第七步：finishing-a-development-branch

作用：**收尾。**

收尾不是说一句“完成了”，而是要检查：

```text
测试是否全部通过
lint 是否通过
有没有未提交文件
是否需要合并分支
是否需要创建 PR
是否要保留还是删除临时工作区
```

---

## 5. Superpowers 内置的重要 skills

下面是一些最重要、最常用的 skills。

| Skill 名称 | 通俗解释 | 适合场景 |
|---|---|---|
| `using-superpowers` | 总入口，告诉 Agent 要先检查有没有相关 skill | 每次开始任务 |
| `brainstorming` | 需求澄清和方案讨论 | 需求还不清楚时 |
| `writing-plans` | 写详细实施计划 | 开发前 |
| `test-driven-development` | 先写测试，再写代码 | 实现功能、修 bug |
| `systematic-debugging` | 系统化调试，不乱猜 | 复杂 bug |
| `verification-before-completion` | 完成前验证 | 任务收尾 |
| `requesting-code-review` | 请求代码审查 | 每个功能完成后 |
| `using-git-worktrees` | 创建隔离开发环境 | 多任务开发 |
| `subagent-driven-development` | 子 Agent 分工开发 | 复杂项目 |
| `writing-skills` | 创建自己的 skill | 想定制个人工作流时 |

---

## 6. 它和普通 Prompt 有什么区别

普通 Prompt 是：

```text
请你写代码前先思考，写完后测试一下。
```

问题是：  
Agent 可能会忘，也可能表面上答应，实际还是直接写代码。

Superpowers 的方式是：

```text
把“应该怎么做”写进一个独立的 SKILL.md
让 Agent 在合适场景主动加载并执行
```

区别如下：

| 对比项 | 普通 Prompt | Superpowers Skill |
|---|---|---|
| 稳定性 | 容易被忽略 | 更容易被持续执行 |
| 复用性 | 每次都要重新说 | 安装后可反复使用 |
| 结构化程度 | 取决于你怎么写 | 已经写成标准流程 |
| 适合任务 | 简单任务 | 复杂开发、调试、长期项目 |
| 可扩展性 | 较弱 | 可以自己写新 skill |

---

## 7. 如何安装

不同 Agent 的安装方式不同。  
如果你同时使用 Claude Code、Codex、Gemini CLI、Cursor，需要分别安装。

---

### 7.1 Claude Code 安装

方式一：官方插件市场

```bash
/plugin install superpowers@claude-plugins-official
```

方式二：Superpowers 自己的 marketplace

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

---

### 7.2 Codex CLI 安装

在 Codex CLI 里输入：

```bash
/plugins
```

然后搜索：

```text
superpowers
```

选择：

```text
Install Plugin
```

---

### 7.3 Codex App 安装

在 Codex App 中：

```text
左侧栏 Plugins
  → Coding 区域找到 Superpowers
  → 点击 “+”
  → 按提示安装
```

---

### 7.4 Gemini CLI 安装

安装：

```bash
gemini extensions install https://github.com/obra/superpowers
```

后续更新：

```bash
gemini extensions update superpowers
```

---

### 7.5 OpenCode 安装

在 OpenCode 里告诉 Agent：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
```

---

### 7.6 Cursor 安装

在 Cursor Agent chat 中输入：

```bash
/add-plugin superpowers
```

或者在插件市场搜索：

```text
superpowers
```

---

### 7.7 GitHub Copilot CLI 安装

```bash
copilot plugin marketplace add obra/superpowers-marketplace
copilot plugin install superpowers@superpowers-marketplace
```

---

## 8. 安装后怎么使用

理论上，安装后 Agent 会自动检查相关 skill。  
但刚开始使用时，建议你明确提醒它使用 Superpowers。

例如：

```text
请使用 Superpowers 工作流帮我完成这个任务。
先不要直接写代码，先进行 brainstorming。
```

或者：

```text
请使用 Superpowers 的 writing-plans skill，把这个功能拆成可执行开发计划。
不要直接实现。
```

如果你要修 bug，可以说：

```text
请使用 Superpowers 的 systematic-debugging skill 来定位这个 bug。
不要猜测原因，先收集证据，再提出根因假设。
```

如果你要开发功能，可以说：

```text
请使用 Superpowers 的 test-driven-development skill。
先写失败测试，确认测试失败，再写最小实现让测试通过。
```

如果你要收尾，可以说：

```text
请使用 verification-before-completion 检查这个任务是否真的完成。
包括测试、lint、边界条件和未提交修改。
```

---

## 9. 推荐使用模板

你可以直接复制下面这段给 Codex / Claude Code / Gemini CLI。

```text
我想开发一个功能：{在这里写你的需求}。

请使用 Superpowers 工作流：

1. 先调用 brainstorming，帮我澄清需求，不要直接写代码；
2. 根据我的回答，整理一个简短、清晰的设计方案；
3. 等我确认设计后，再调用 writing-plans；
4. writing-plans 阶段要把任务拆成可以逐步执行的小步骤；
5. 我说 “go” 之后，再开始开发；
6. 开发阶段必须使用 test-driven-development；
7. 每个任务完成后进行 code review；
8. 最后用 verification-before-completion 检查是否真的完成。
```

---

## 10. 一个完整例子：开发 PDF 转 Markdown 工具

假设你想让 Agent 开发一个工具：

```text
把医学论文 PDF 转成 Markdown，并提取 Introduction、Methods、Results、Discussion。
```

不要这样说：

```text
帮我写一个 PDF 转 Markdown 工具。
```

更推荐这样说：

```text
我想开发一个本地工具，用于把医学论文 PDF 转换成 Markdown，
并提取 Introduction、Methods、Results、Discussion 的核心结构。

请使用 Superpowers 工作流：

- 先调用 brainstorming，不要直接写代码；
- 先问我必要问题；
- 然后给出设计方案；
- 我确认后，再调用 writing-plans 生成开发计划；
- 执行阶段必须使用 test-driven-development；
- 每完成一个任务后进行 code review；
- 最后用 verification-before-completion 验证功能是否完成。
```

理想情况下，Agent 会先问：

```text
1. PDF 是否都是英文论文？
2. 是否需要 OCR？
3. 是否需要保留表格？
4. 是否需要保留参考文献？
5. Markdown 输出格式是否固定？
6. 是单个 PDF，还是批量处理？
7. 使用 Python 还是 Node.js？
```

然后才进入设计和开发。

---

## 11. 如何自己创建一个 skill

Superpowers 也支持你创建自己的 skill。  
官方 `writing-skills` 文档说明，skill 是可复用的技术、模式或工具参考，不应该只是某一次任务的记录。

简单说：

```text
好的 skill = 以后还会反复用的工作方法
不好的 skill = 某一次任务的流水账
```

### 11.1 skill 的基本结构

一个 skill 通常是一个文件夹：

```text
my-skill-name/
  SKILL.md
```

### 11.2 一个最简单的 SKILL.md 模板

```markdown
---
name: my-skill-name
description: Use when the agent needs to do X under Y conditions.
---

# My Skill Name

## Overview

这里写这个 skill 的用途。

## When to Use

在什么情况下使用这个 skill。

## Workflow

1. 第一步做什么
2. 第二步做什么
3. 第三步做什么

## Rules

- 不能跳过哪些步骤
- 不能做哪些事情
- 必须验证哪些结果

## Common Mistakes

- 常见错误 1
- 常见错误 2
- 常见错误 3
```

---

## 12. 适合你创建的科研类 skills

结合你的研究方向，可以考虑创建这些自定义 skills。

### 12.1 UKB 表型定义 skill

名称：

```text
ukb-phenotype-definition
```

用途：

```text
用于定义 UKB 中的疾病表型、暴露、结局、ICD 编码、随访时间和排除标准。
```

适合任务：

```text
定义 OSA
定义 OA
定义 RA
定义肺炎
定义结核
定义泌尿系统感染
整理 ICD-10 编码
构建 baseline exclusion criteria
```

---

### 12.2 UKB Cox 分析 skill

名称：

```text
ukb-cox-analysis
```

用途：

```text
用于规范 UKB 队列研究中的 Cox 比例风险模型。
```

应该规定：

```text
暴露变量
结局变量
随访起点
随访终点
协变量
缺失值处理
模型分层
敏感性分析
比例风险假设检查
结果输出格式
```

---

### 12.3 蛋白组学中介分析 skill

名称：

```text
proteomics-mediation-analysis
```

用途：

```text
用于 OSA → protein → OA 这类蛋白组学中介分析。
```

应该规定：

```text
蛋白缺失率过滤
均值插补
winsorization
z-score 标准化
OSA → protein 关联
protein → OA 关联
交集蛋白筛选
中介模型选择
多重校正
GO/KEGG 富集分析
敏感性分析
```

---

### 12.4 医学论文写作 skill

名称：

```text
biomedical-paper-writing
```

用途：

```text
用于撰写或修改医学论文的 Introduction、Methods、Results、Discussion。
```

应该规定：

```text
少用空泛表达
少用 AI 味套话
不要重复车轱辘话
不要过度因果化
结果必须紧贴数据
讨论必须围绕机制、临床意义、局限性展开
语言要像人类研究者，而不是宣传文案
```

---

### 12.5 低 AI 痕迹改写 skill

名称：

```text
low-ai-signature-editing
```

用途：

```text
用于降低论文文字中的 AI 味。
```

重点约束：

```text
减少过度工整的三段式表达
减少 “plays a crucial role” 这类泛化短语
减少过强的总结句
增加具体研究语境
增加审稿人关心的限制性表达
保留适度不完美但自然的人类写作节奏
```

---

## 13. 你可以采用的最佳组合

如果你现在主要用：

```text
Claude Code + Opus 做规划
Codex + GPT-5.5 做详细开发和执行
```

可以这样组合：

```text
Superpowers 原生 skills
├── brainstorming
├── writing-plans
├── test-driven-development
├── systematic-debugging
├── requesting-code-review
└── verification-before-completion

你的自定义科研 skills
├── ukb-phenotype-definition
├── ukb-cox-analysis
├── ukb-psm-analysis
├── proteomics-mediation-analysis
├── biomedical-paper-writing
└── low-ai-signature-editing
```

推荐工作流：

```text
1. Claude Code + Superpowers
   用于需求澄清、研究框架设计、开发计划

2. Codex + Superpowers
   用于执行代码开发、测试、调试、文件整理

3. 自定义科研 skills
   用于保证 UKB 分析、蛋白组学分析、论文写作符合你的研究规范
```

---

## 14. 使用时的注意事项

### 14.1 不适合所有任务

Superpowers 更适合复杂任务，例如：

```text
开发工具
写分析脚本
修复杂 bug
重构项目
设计工作流
构建个人 skill
```

不适合简单问答，例如：

```text
什么是 Cox 回归？
Python 怎么打印 hello world？
这个英文单词什么意思？
```

这些简单问题没必要启动完整工作流。

---

### 14.2 它不是万能保证

Superpowers 可以提高 Agent 的稳定性，但不能保证：

```text
所有代码都一定正确
所有分析方案都一定科学
所有结果都能发表
所有安装都一定成功
```

它解决的是“流程混乱”的问题，不是替代你做最终判断。

---

### 14.3 安装第三方 skill 要谨慎

Skill 本质上是一种高权限提示文件。  
如果一个 skill 里面写了危险规则，Agent 可能会照做。

所以安装前最好检查：

```text
SKILL.md 是否要求读取敏感文件
是否要求上传密钥
是否要求删除文件
是否要求执行不明命令
是否要求绕过安全检查
```

如果你自己写科研 skill，建议只写工作流规则，不要写危险系统命令。

---

## 15. 最简使用口诀

可以记住这句话：

```text
Superpowers 不是让 Agent 直接变强，
而是让 Agent 先问清楚、再做计划、按测试开发、最后验证完成。
```

再压缩一点：

```text
先澄清 → 再设计 → 写计划 → 做测试 → 写代码 → 审查 → 验证
```
---

## 17. 参考来源

1. Superpowers GitHub 仓库  
   https://github.com/obra/superpowers

2. Superpowers README：安装方式、基础工作流、支持的 Agent  
   https://github.com/obra/superpowers

3. `using-superpowers` skill  
   https://github.com/obra/superpowers/blob/main/skills/using-superpowers/SKILL.md

4. `writing-skills` skill  
   https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md

5. `writing-plans` skill  
   https://github.com/obra/superpowers/blob/main/skills/writing-plans/SKILL.md
