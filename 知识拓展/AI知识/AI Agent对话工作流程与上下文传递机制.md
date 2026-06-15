建议文件名：AI Agent对话工作流程与上下文传递机制.md

# AI Agent 对话工作流程与上下文传递机制

内容类型：主题知识介绍

## 摘要

本文介绍用户与 Claude Code、Codex 等 AI Agent 对话过程中从输入到输出的完整工作流程，重点说明上下文组装、工具调用闭环、消息压缩策略及不同 Agent 平台的上下文传递差异。

## 关键词

AI Agent；上下文窗口；System Prompt；Tool Use；消息压缩；Claude Code；Codex；上下文传递

## 大纲

1. 对话生命周期：从用户输入到 Agent 响应
2. 上下文组装：System Prompt 与消息结构
3. 工具调用（Tool Use）的上下文往返机制
4. 上下文窗口管理与消息压缩策略
5. Claude Code 的上下文传递机制
6. Codex 平台的上下文传递特点
7. 多 Agent 协作中的上下文传递

## 正文

### 1. 对话生命周期：从用户输入到 Agent 响应的完整链路

本节概要：本节梳理一次完整对话交互中 Agent 内部处理的各个阶段。

一次完整的 Agent 对话交互遵循以下循环：
![[Pasted image 20260520195216.png|697]]

- **构建上下文**：将 System Prompt、对话历史、工具定义、用户输入等组装为一次请求的完整上下文。
- **发送到模型**：将组装好的上下文作为模型 API 调用的 messages 参数发送。
- **模型返回响应**：模型返回文本响应，可能包含文本内容和/或工具调用（Tool Use）指令。
- **解析响应**：检查模型是否请求调用工具。若无工具调用，直接展示文本；若有，解析工具名称和参数。
- **执行工具**：根据解析结果执行对应工具（读文件、写文件、执行命令、搜索等），获取工具返回结果。
- **追加到上下文**：将模型的工具调用和工具执行结果追加到消息列表中。
- **再次调用模型**：将更新后的消息列表再次发送给模型，模型基于工具结果继续推理。
- **最终响应**：模型不再请求工具时，输出最终文本响应给用户。

```
用户输入 → 上下文组装 → 模型推理 → 工具调用？
                                        ├── 否 → 输出响应 → 用户
                                        └── 是 → 执行工具 → 结果追加 → 模型推理 → ...
```

### 2. 上下文组装：System Prompt 与消息结构

本节概要：本节说明一次模型 API 调用中消息的结构组成，以及各部分的功能。

模型 API 接受的 messages 是一个消息数组，典型结构如下：

- **System Prompt（角色：system）**：定义 Agent 的行为准则、能力边界、输出格式、可用工具列表、安全规则等。这是 Agent 的"人格"与"操作手册"，由平台在每次请求中自动注入。
- **对话历史（角色：user / assistant）**：此前用户与模型的完整或摘要式对话记录，以交替的 user 和 assistant 消息形式排列。
- **工具定义（tools）**：以 JSON Schema 描述可用工具的清单，包括工具名称、参数类型、描述信息。模型据此判断是否调用哪个工具。
- **当前用户输入（角色：user）**：用户最新的一条消息。

示例消息结构：

```json
{
  "model": "claude-sonnet-4-6",
  "messages": [
    {"role": "system", "content": "You are Claude Code... (完整System Prompt)"},
    {"role": "user", "content": "帮我重构这个函数"},
    {"role": "assistant", "content": "我会先读取文件..."},
    {"role": "user", "content": "继续"},
    {"role": "assistant", "content": "Done.", "tool_calls": [{"name": "Edit", ...}]},
    {"role": "tool", "content": "File updated.", "tool_call_id": "..."},
    {"role": "user", "content": "把reading skill改名"}
  ]
}
```

### 3. 工具调用（Tool Use）的上下文往返机制

本节概要：本节说明 Tool Use 过程中消息如何往返增长，以及模型如何利用工具执行结果。

工具调用是 Agent 行为的核心，其上下文传递逻辑为：

- **模型输出 tool_calls**：模型在 assistant 消息中附带 `tool_calls` 数组，每个工具调用有唯一 ID、名称、参数。
- **执行工具**：Agent 运行时（非模型）解析 tool_calls，执行实际工具操作（读写文件、运行命令等）。
- **追加 tool 消息**：工具执行结果以 `role: "tool"` 消息追加到上下文，通过 `tool_call_id` 关联到请求。
- **模型读取结果**：下次模型调用时，模型看到完整的 tool 消息结果，据此判断下一步操作。
- **循环直到停止**：模型可能连续调用多次工具，每次往返都让上下文增长。

```
Message N:   [assistant] 调用 Read(file="foo.ts")
Message N+1: [tool]       返回文件内容（1000行）
Message N+2: [assistant]  调用 Edit(file="foo.ts", old="...", new="...")
Message N+3: [tool]       返回编辑成功
Message N+4: [assistant]  输出最终文本："已完成重构"
```

关键点：每次工具往返都是独立的模型 API 调用，上下文在每一轮都在增长。工具结果（尤其是大文件内容）会快速消耗上下文窗口容量。

### 4. 上下文窗口管理与消息压缩策略

本节概要：本节说明当对话历史超出模型上下文窗口限制时，Agent 平台如何处理上下文。

每个模型都有最大上下文窗口（如 200K tokens）。当对话持续进行，上下文会逐渐逼近上限。压缩策略包括：

- **截断旧消息**：删除最早的对话记录，保留最近的 N 条消息。最激进的方式，可能导致丢失重要早期上下文。
- **摘要压缩**：对面较早的对话内容生成摘要，用摘要替换原始消息。Claude Code 的 system-reminder 中明确提示系统会自动压缩先前的消息。
- **Tool Result 截断**：工具返回的结果（如大文件内容）可能被截断，只保留开头部分。
- **滑动窗口**：保留一个固定大小的消息窗口，新消息进入时最旧消息移出。
- **关键信息锚定**：System Prompt 和关键用户指令通常固定在窗口内，不参与轮换。Claude 中 `<system-reminder>` 标签标记的内容会被优先保留。

压缩的本质权衡：

| 策略 | 优点 | 缺点 |
|------|------|------|
| 截断旧消息 | 实现简单 | 丢失早期关键上下文 |
| 摘要压缩 | 保留关键信息 | 摘要可能不准确 |
| Tool Result 截断 | 释放大量空间 | 模型看不到完整文件 |
| 滑动窗口 | 逻辑清晰 | 窗口边界可能切断关联对话 |

### 5. Claude Code 的上下文传递机制

本节概要：本节聚焦 Claude Code CLI 工具在上下文传递中的具体实现特点。

Claude Code 是 Anthropic 官方 CLI Agent 工具，其上下文管理特点：

- **System Prompt 分层次注入**：
  - 环境信息（操作系统、日期、Shell、工作目录）
  - Skills 列表（`<system-reminder>` 中列出所有可用的 Skill）
  - 标签化提示（`<system-reminder>` 包裹的指令会被优先处理）
  - 安全规则与能力边界
- **Skills 按需加载**：Skill 通过 `Skill` 工具调用时动态加载完整内容到上下文，而非全部预加载。Skill 描述在 System Prompt 中始终可见，完整内容仅在触发后加载。
- **文件读取优先**：Claude Code 强调使用 Read 工具读取文件而非 Bash cat 等，确保文件内容以结构化方式进入上下文。
- **压缩警告**：`<system-reminder>` 标签中的"System will automatically compress prior messages"明确告知模型上下文可能被压缩。
- **持久化记忆（Memory）**：`~/.claude/projects/` 下的 MEMORY.md 文件充当跨对话的持久记忆，在新对话开始时被注入上下文。
- **子 Agent 隔离上下文**：通过 Agent 工具启动的子 Agent 拥有独立的上下文空间，只接收父 Agent 传递的任务描述（prompt），不会共享父 Agent 的全部对话历史。

### 6. Codex 平台的上下文传递特点

本节概要：本节介绍 Codex（OpenAI 的 Agent SDK）在上下文传递中的架构差异。

Codex 平台的核心差异：

- **AGENTS.md / CLAUDE.md 文件注入**：Codex 在会话启动时读取项目或用户目录下的 `AGENTS.md` 文件，将其中指令注入 System Prompt。用户通过编辑该文件控制 Agent 行为。
- **Skill 注册机制**：Codex 的 Skill 以文件系统中的目录形式存在，通过 `Skill` 工具加载。Skill 的 YAML frontmatter 中的 `description` 字段决定了 Skill 的触发匹配。
- **Hook 系统**：支持 `SessionStart` 等生命周期 Hook，可以在会话启动时执行自定义逻辑并注入额外上下文（如 `<system-reminder>` 中的标签内容）。
- **Tool Result 完整性**：Codex 的工具调用结果会完整返回，通过 `persisted-output` 标签标记超大输出，提供截断文件路径供模型后续读取。
- **多 Agent 协作**：Codex 通过 `Agent` 工具派生子 Agent，子 Agent 有独立上下文但通过 prompt 参数接收来自父 Agent 的完整任务指令。

### 7. 多 Agent 协作中的上下文传递

本节概要：本节说明父 Agent 与子 Agent 之间的上下文传递方式和隔离机制。

多 Agent 协作的核心机制：

- **任务描述传递（Prompt Injection）**：父 Agent 将任务封装为详细 prompt 字符串，作为子 Agent 的初始 user 消息。这是唯一的直接信息传递通道。
- **上下文隔离**：子 Agent 不继承父 Agent 的对话历史。它拥有全新的 System Prompt 和独立的消息序列。这避免了上下文无限膨胀。
- **结果回传**：子 Agent 完成后返回一个最终消息给父 Agent，包含任务执行摘要。父 Agent 将摘要纳入自身上下文。
- **文件系统作为共享状态**：父 Agent 和子 Agent 通过读写同一文件系统进行间接通信。父 Agent 写出任务文件，子 Agent 读取并修改，完成后父 Agent 读取结果。
- **工作树隔离（Worktree）**：在 git 仓库中，Agent 工具支持创建临时 git worktree，子 Agent 在隔离的文件副本上工作，避免污染主工作区。

```
父 Agent
  │
  ├── 派生子 Agent 1: prompt="搜索项目中的认证逻辑"
  │     └── 返回: "在 auth.ts 第42-100行找到了JWT认证逻辑"
  │
  ├── 派生子 Agent 2: prompt="查看所有API endpoint定义"
  │     └── 返回: "共找到15个endpoint，定义在 routes/ 目录"
  │
  └── 整合结果 → 输出最终响应
```

关键原则：子 Agent 之间彼此完全隔离，互不知晓。所有协作通过父 Agent 协调，父 Agent 负责信息整合与任务拆解。

---
