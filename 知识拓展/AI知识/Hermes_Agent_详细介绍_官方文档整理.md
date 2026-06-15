# Hermes Agent 详细介绍文档（基于官方资料整理）

> 整理日期：2026-05-11  
> 信息来源：Hermes Agent 官方网站、官方文档、NousResearch/hermes-agent GitHub 仓库。  
> 适用对象：初次接触 Hermes Agent、正在 Windows/WSL2/Linux 环境中安装配置、希望理解“自我改进型 Agent”设计的人。  
> 说明：本文尽量用中文通俗解释，但保留必要技术术语，方便后续安装、排错和扩展。

---

## 1. 一句话理解 Hermes Agent

Hermes Agent 是 Nous Research 开发的开源 AI Agent。它不是单纯的聊天机器人，也不是只绑定在 IDE 里的代码补全工具，而是一个可以长期运行在本机、服务器、VPS、云沙箱或容器中的“自我改进型 AI 工作环境”。

它的核心特点是：

1. 可以跨会话保留记忆；
2. 可以从成功经验中沉淀 Skills；
3. 可以调用终端、文件、浏览器、网页搜索、图像、语音、消息平台等工具；
4. 可以通过 Telegram、Discord、Slack、WhatsApp、Signal、Email、Weixin/WeChat、飞书、企业微信、Teams、LINE 等平台远程对话；
5. 可以执行定时任务；
6. 可以连接 MCP 工具服务器；
7. 可以用不同模型供应商，不固定绑定某一家模型。

官方对它的定位是：

> The Agent That Grows With You.  
> 一个会随着使用而成长的 Agent。

更直白地说，Hermes Agent 想解决的问题不是“让 AI 回答一句话”，而是“让 AI 长期驻留在一个工作环境中，记住你的项目、工具、习惯，并逐步积累可复用的操作能力”。

---

## 2. 官方定位：它不是哪类工具？

官方文档反复强调，Hermes Agent 不只是：

- 一个 IDE 代码补全工具；
- 一个聊天 API 包装器；
- 一个临时对话机器人；
- 一个只能在当前电脑前台运行的工具。

它更接近于：

- 一个可以部署在云服务器上的长期 AI 助手；
- 一个可以通过消息软件随时访问的远程 Agent；
- 一个拥有终端、文件、浏览器、搜索、记忆、技能、定时任务等能力的自动化执行环境；
- 一个可组合模型、工具、消息平台和持久化存储的 Agent 框架。

因此，Hermes Agent 的正确理解方式是：


```text
模型只是大脑的一部分。
Hermes Agent = 模型 + 工具系统 + 记忆系统 + 技能系统 + 终端环境 + 消息网关 + 自动化调度 + 安全边界。
```

---

## 3. Hermes Agent 的核心能力总览

| 模块 | 作用 | 典型用途 |
|---|---|---|
| CLI / TUI | 命令行或终端交互入口 | 在本机直接和 Agent 对话 |
| 模型提供商 Provider | 接入 LLM 模型 | Nous Portal、OpenRouter、OpenAI、Anthropic、Kimi、GLM 等 |
| Tools / Toolsets | 工具系统 | 搜索网页、读写文件、运行命令、浏览器自动化、图像生成等 |
| Terminal Backends | 命令执行环境 | local、Docker、SSH、Modal、Daytona、Vercel Sandbox、Singularity |
| Memory | 跨会话记忆 | 记住用户偏好、项目环境、操作经验 |
| Skills | 可复用技能文档 | 把成功任务沉淀成后续可调用的流程 |
| Messaging Gateway | 消息平台网关 | Telegram、Discord、Slack、微信、飞书、企业微信等 |
| Cron | 定时任务 | 每天汇报、定时备份、定时监控 |
| Subagents / Delegation | 子代理并行任务 | 多任务并行研究、代码审查、分工执行 |
| Kanban | 多 Agent 看板 | 持久化任务协作、角色分工、长期流水线 |
| MCP | 外部工具服务器连接 | GitHub、数据库、文件系统、内部 API 等 |
| Web Dashboard | 网页仪表盘 | 管理配置、API Key、会话、日志、定时任务、技能 |
| Security | 安全边界 | 危险命令审批、容器隔离、用户授权、MCP 凭证过滤 |

---

## 4. 工作方式：从“聊天”到“执行环境”

传统聊天机器人一般是：

```text
用户输入 → 模型回复 → 对话结束
```

Hermes Agent 更像：

```text
用户输入
  ↓
Hermes 会话管理
  ↓
模型推理
  ↓
工具选择
  ↓
执行终端 / 浏览器 / 文件操作 / 搜索 / MCP / 消息发送
  ↓
保存必要记忆
  ↓
必要时生成或调用 Skills
  ↓
返回结果
```

如果启用 Messaging Gateway，则交互入口可以不是 CLI，而是 Telegram、Discord、Slack、Weixin/WeChat 等平台：

```text
消息平台
  ↓
Hermes Gateway
  ↓
会话存储
  ↓
AIAgent
  ↓
模型 + 工具
  ↓
返回到原消息平台
```

如果启用 Cron，则 Hermes 可以在无人值守情况下执行任务：

```text
Cron 调度器
  ↓
新建一次 Agent 运行
  ↓
执行指定 prompt
  ↓
调用工具
  ↓
把结果发送到本地文件 / 消息平台 / 邮件等目标
```

---

## 5. 安装方式

### 5.1 Linux / macOS / WSL2 推荐安装方式

官方推荐的一行安装命令：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装后刷新 shell：

```bash
source ~/.bashrc
# 或
source ~/.zshrc
```

然后启动：

```bash
hermes
```

或进行完整配置：

```bash
hermes setup
```

### 5.2 Windows 用户建议

官方文档已经提供 Native Windows 安装方式，但标注为 early beta。对于 Windows 用户，官方仍然建议优先使用 WSL2，因为 WSL2 路径更成熟。

Native Windows PowerShell 安装命令：

```powershell
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

但是，如果你已经在 Windows 11 上配置了 WSL2，建议优先在 WSL2 终端里使用 Linux 安装命令：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 5.3 Android / Termux

官方也支持 Termux 路径，安装命令同样是：

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

安装器会自动识别 Termux 环境，并走对应依赖安装流程。

---

## 6. 安装器会做什么？

根据官方安装文档，安装器会自动处理：

- `uv`：Python 包管理器；
- Python 3.11；
- Node.js 22；
- `ripgrep`：快速文件搜索；
- `ffmpeg`：音频格式转换，用于语音相关功能；
- Hermes Agent 仓库克隆；
- Python 虚拟环境；
- `hermes` 命令链接；
- 基础模型供应商配置。

典型 per-user 安装布局：

```text
代码目录：~/.hermes/hermes-agent/
命令链接：~/.local/bin/hermes
数据目录：~/.hermes/
```

Root 模式安装布局则可能位于：

```text
代码目录：/usr/local/lib/hermes-agent/
命令路径：/usr/local/bin/hermes
数据目录：/root/.hermes/ 或 $HERMES_HOME
```

---

## 7. 安装后最重要的几个命令

| 命令 | 用途 |
|---|---|
| `hermes` | 启动默认交互 |
| `hermes chat` | 启动聊天会话 |
| `hermes setup` | 完整配置向导 |
| `hermes model` | 选择 / 修改模型供应商与模型 |
| `hermes tools` | 配置工具与工具集 |
| `hermes gateway setup` | 配置消息平台网关 |
| `hermes gateway` | 前台运行消息网关 |
| `hermes gateway install` | 安装为用户服务 |
| `hermes gateway start` | 启动网关服务 |
| `hermes gateway stop` | 停止网关服务 |
| `hermes gateway status` | 查看网关服务状态 |
| `hermes dashboard` | 启动本地 Web 仪表盘 |
| `hermes doctor` | 诊断安装和依赖问题 |
| `hermes config set` | 修改单个配置项 |
| `hermes config check` | 检查配置 |
| `hermes config migrate` | 配置迁移 |
| `hermes update` 或 `/update` | 更新 Hermes Agent |

---

## 8. 模型 Provider：Hermes 不绑定单一模型

Hermes Agent 可以通过 `hermes model` 选择模型供应商。官方文档和 GitHub README 中提到的供应商包括：

- Nous Portal；
- OpenRouter；
- OpenAI；
- Anthropic；
- Kimi / Moonshot；
- Kimi 中国区 endpoint；
- Z.AI / GLM；
- Arcee AI；
- GMI Cloud；
- NVIDIA NIM；
- MiniMax；
- Hugging Face；
- 自定义 OpenAI-compatible endpoint；
- 其他兼容接口。

基本配置流程：

```bash
hermes model
```

然后按照向导选择供应商、输入 API Key 或完成 OAuth。

如果你在中国大陆网络环境中使用，需要重点考虑：

1. 目标 provider 是否可访问；
2. API Key 是否有效；
3. endpoint 是否是中国区；
4. VPN / 代理是否影响网络连接；
5. 是否需要在 `~/.hermes/.env` 中设置代理或特定 provider 的 API Key。

---

## 9. Terminal Backend：命令到底在哪里执行？

Hermes 的终端工具可以执行 shell 命令，但“执行在哪里”由 terminal backend 决定。

官方配置示例：

```yaml
terminal:
  backend: local    # local | docker | ssh | modal | daytona | vercel_sandbox | singularity
  cwd: "."
  timeout: 180
```

### 9.1 后端对比

| Backend | 命令执行位置 | 隔离性 | 适合场景 |
|---|---|---|---|
| `local` | 当前机器 | 无隔离 | 个人开发、可信任务 |
| `docker` | 持久 Docker 容器 | 强隔离 | 安全沙箱、CI/CD、可复现环境 |
| `ssh` | 远程服务器 | 网络边界隔离 | 远程开发、让 Agent 远离自身代码 |
| `modal` | Modal 云沙箱 | 云端隔离 | 弹性云计算、评测 |
| `daytona` | Daytona workspace | 云容器隔离 | 管理型云开发环境 |
| `vercel_sandbox` | Vercel Sandbox microVM | 云端隔离 | 云执行、快照持久化 |
| `singularity` | Singularity / Apptainer 容器 | 命名空间隔离 | HPC 集群、无 root 场景 |

### 9.2 local backend 的风险

`local` 是默认模式，但 Agent 与当前用户拥有相同文件系统权限。也就是说，它能读写你当前用户有权限访问的文件。

因此：

- 新手不建议直接开启高风险自动执行；
- 不建议在 local 下随意使用 `--yolo`；
- 重要目录建议备份；
- 对不确定任务建议使用 Docker 或 SSH 后端。

### 9.3 Docker backend 的特点

Docker 后端不是“每条命令一个新容器”，而是一个长期存在的容器。Hermes 启动一个持久容器后，后续 terminal、file、execute_code 等工具调用都会进入同一个容器。

这意味着：

- 你安装的 Python 包会保留；
- 你修改的工作目录会保留；
- `/workspace` 中写入的文件会保留；
- 它更像一个持久沙箱，而不是一次性临时容器。

配置示例：

```yaml
terminal:
  backend: docker
  docker_image: python:3.11-slim
  container_cpu: 1
  container_memory: 5120
  container_disk: 51200
  container_persistent: true
```

---

## 10. Tools / Toolsets：Hermes 的工具系统

Hermes 的能力主要通过工具扩展。官方文档将工具按功能组织成 toolsets，可以按平台启用或禁用。

常见工具类别：

| 类别 | 示例工具 | 作用 |
|---|---|---|
| Web | `web_search`, `web_extract` | 网页搜索与网页内容提取 |
| Terminal & Files | `terminal`, `process`, `read_file`, `patch` | 运行命令、进程管理、读写和修改文件 |
| Browser | `browser_navigate`, `browser_snapshot`, `browser_vision` | 浏览器自动化、网页交互、视觉分析 |
| Media | `vision_analyze`, `image_generate`, `text_to_speech` | 图像理解、图像生成、语音输出 |
| Agent orchestration | `todo`, `clarify`, `execute_code`, `delegate_task` | 规划、澄清、代码执行、子代理委派 |
| Memory & recall | `memory`, `session_search` | 记忆与历史会话检索 |
| Automation & delivery | `cronjob`, `send_message` | 定时任务与消息发送 |
| Integrations | `ha_*`, MCP server tools, `rl_*` | Home Assistant、MCP、RL 训练等 |

查看工具：

```bash
hermes tools
```

指定工具集启动：

```bash
hermes chat --toolsets "web,terminal"
```

### 10.1 浏览器工具是做什么的？

浏览器工具不是普通网页搜索，而是让 Agent 操作一个真实或近似真实的浏览器环境，例如：

- 打开网页；
- 点击按钮；
- 读取网页结构；
- 使用视觉能力分析页面；
- 填写表单；
- 下载内容；
- 与需要浏览器状态的网页交互。

如果你只需要“查资料”，`web_search` / `web_extract` 足够。  
如果你需要“像人一样操作网页”，才需要 browser tools。

### 10.2 为什么 Playwright Chromium 会出问题？

浏览器工具常依赖 Playwright / Chromium。某些非常新的 Linux 发行版版本可能暂时不在 Playwright 官方支持矩阵内。例如你之前遇到的：

```text
Playwright does not support chromium on ubuntu26.04-x64
```

这种情况下通常不是 Hermes 主体坏了，而是 Playwright 浏览器引擎对该系统版本支持不足。可选处理思路：

1. 先不启用 browser tools，保留核心 CLI / terminal / messaging 功能；
2. 改用 Ubuntu 22.04 / 24.04 等更常见环境；
3. 使用 Docker 后端放到受支持镜像里；
4. 等 Playwright 支持更新；
5. 手动安装系统依赖并测试 `npx playwright install --with-deps chromium`。

---

## 11. Memory：跨会话记忆系统

Hermes Agent 有“有边界、可整理”的持久记忆。官方文档说明，它主要由两个文件组成：

| 文件 | 作用 | 限制 |
|---|---|---|
| `MEMORY.md` | Agent 自己的笔记：环境事实、项目约定、工具经验、已完成任务 | 约 2,200 字符 |
| `USER.md` | 用户画像：偏好、沟通风格、期望、技术水平 | 约 1,375 字符 |

存储位置：

```text
~/.hermes/memories/
```

### 11.1 Memory 如何进入上下文？

每次会话开始时，Hermes 会把记忆文件加载进系统提示词，作为冻结快照。

这意味着：

- 会话开始后，记忆内容会固定；
- 本轮中新增记忆会立即写入磁盘；
- 但新增内容要到下一次会话才会出现在系统提示词里；
- 这样设计有利于性能和 prefix cache。

### 11.2 适合保存什么？

适合保存：

- 用户长期偏好；
- 项目固定路径；
- 环境配置；
- 常见排错经验；
- 项目约定；
- 成功完成的重要操作；
- 用户明确要求“记住”的事项。

不适合保存：

- 临时日志；
- 大段数据；
- 一次性文件路径；
- 可通过搜索轻松重新获得的常识；
- 过于模糊的信息；
- 已经写在 `SOUL.md` 或 `AGENTS.md` 里的内容。

---

## 12. Skills：Hermes 的“程序性记忆”

如果 Memory 更像“事实记忆”，Skills 更像“操作方法记忆”。

官方定义中，Skills 是按需加载的知识文档，遵循 progressive disclosure 设计，减少 token 浪费。

存储位置：

```text
~/.hermes/skills/
```

Skills 来源包括：

1. 内置 bundled skills；
2. 从 Skills Hub 安装的 skills；
3. Agent 在任务中自动创建或改进的 skills；
4. 用户手动创建的 skills；
5. 外部技能目录。

### 12.1 Skills 的调用方式

每个已安装 skill 会自动成为 slash command：

```text
/plan design a rollout for migrating our auth provider
/github-pr-workflow create a PR for the auth refactor
/axolotl help me fine-tune Llama 3 on my dataset
```

你也可以直接问：

```bash
hermes chat --toolsets skills -q "What skills do you have?"
```

### 12.2 Progressive Disclosure：为什么说它节省 token？

Skills 分三层加载：

```text
Level 0: skills_list()           → 只列出名称、描述、分类
Level 1: skill_view(name)        → 加载完整 skill
Level 2: skill_view(name, path)  → 加载 skill 内某个参考文件
```

Agent 不会一开始把所有 skill 全部塞进上下文，而是先看列表，需要时再加载完整内容。

### 12.3 一个 Skill 通常包含什么？

典型结构：

```yaml
---
name: my-skill
description: Brief description of what this skill does
version: 1.0.0
platforms: [macos, linux]
metadata:
  hermes:
    tags: [python, automation]
    category: devops
    requires_toolsets: [terminal]
---
```

正文部分则写具体的执行原则、流程、命令、注意事项、模板等。

---

## 13. Messaging Gateway：把 Hermes 接入消息平台

Messaging Gateway 是 Hermes 的消息平台网关。它是一个后台进程，用来连接多个消息平台、维护会话、运行 cron，并把结果发回相应平台。

官方支持的平台包括：

- Telegram；
- Discord；
- Slack；
- WhatsApp；
- Signal；
- SMS；
- Email；
- Home Assistant；
- Mattermost；
- Matrix；
- DingTalk；
- Feishu / Lark；
- WeCom；
- Weixin / WeChat；
- BlueBubbles / iMessage；
- QQ Bot；
- Yuanbao；
- Microsoft Teams；
- LINE；
- Open WebUI；
- Webhooks。

### 13.1 快速配置

```bash
hermes gateway setup
```

这个向导会：

1. 列出可配置平台；
2. 提示输入 token / webhook / 凭证；
3. 保存配置；
4. 可选择启动或重启 gateway。

### 13.2 Gateway 常用命令

```bash
hermes gateway              # 前台运行
hermes gateway setup        # 配置消息平台
hermes gateway install      # 安装为用户服务
sudo hermes gateway install --system   # Linux 系统级服务
hermes gateway start
hermes gateway stop
hermes gateway status
```

### 13.3 消息平台内 slash commands

在消息平台内可使用：

| 命令 | 作用 |
|---|---|
| `/new` 或 `/reset` | 开启新会话 |
| `/model [provider:model]` | 查看或切换模型 |
| `/personality [name]` | 设置人格 |
| `/retry` | 重试上一条 |
| `/undo` | 移除上一轮交换 |
| `/status` | 查看会话状态 |
| `/stop` | 停止当前运行 |
| `/approve` | 批准危险命令 |
| `/deny` | 拒绝危险命令 |
| `/sethome` | 设置当前聊天为 home channel |
| `/compress` | 手动压缩上下文 |
| `/title [name]` | 设置或查看会话标题 |
| `/resume [name]` | 恢复命名会话 |
| `/usage` | 查看 token 使用 |
| `/insights [days]` | 查看使用分析 |
| `/voice [on/off/tts/join/leave/status]` | 控制语音相关功能 |
| `/rollback [number]` | 查看或恢复文件系统 checkpoint |
| `/background <prompt>` | 后台运行一个 prompt |
| `/reload-mcp` | 重载 MCP 服务器 |
| `/update` | 更新 Hermes |
| `/help` | 查看帮助 |
| `/<skill-name>` | 调用任意已安装 skill |

---

## 14. Weixin / WeChat 接入说明

Hermes 官方文档提供了 Weixin / WeChat 适配器。需要注意：这里指个人微信，不是企业微信。企业微信要使用 WeCom adapter。

### 14.1 工作机制

Weixin adapter 使用 Tencent iLink Bot API。消息通过 long-polling 方式传递，因此不需要公网 webhook endpoint。

关键点：

- 使用二维码登录；
- 连接到的是 iLink bot identity；
- 一般更适合 DM 私聊；
- 普通微信群可能不稳定或不可用；
- 群消息是否能送达取决于 iLink 是否返回 group events；
- 不是把你的普通个人微信号变成完全可脚本化账号。

### 14.2 基本要求

需要：

```bash
pip install aiohttp cryptography
pip install hermes-agent[messaging]  # 可选，用于终端二维码等消息功能
```

### 14.3 配置流程

```bash
hermes gateway setup
```

选择 Weixin 后，向导会：

1. 向 iLink Bot API 请求二维码；
2. 在终端显示二维码或 URL；
3. 用手机微信扫码；
4. 在手机上确认登录；
5. 将账号凭证保存到：

```text
~/.hermes/weixin/accounts/
```

### 14.4 关键环境变量

至少需要：

```bash
WEIXIN_ACCOUNT_ID=your-account-id
```

可选：

```bash
WEIXIN_TOKEN=your-bot-token
WEIXIN_DM_POLICY=open
WEIXIN_ALLOWED_USERS=user_id_1,user_id_2
WEIXIN_HOME_CHANNEL=chat_id
WEIXIN_HOME_CHANNEL_NAME=Home
```

### 14.5 DM 授权策略

| 策略 | 含义 |
|---|---|
| `open` | 任何人都可以私聊 bot |
| `allowlist` | 只有白名单用户可以私聊 |
| `disabled` | 忽略所有私聊 |
| `pairing` | 配对模式，用于初始设置 |

建议：

- 个人使用：`allowlist` 更安全；
- 测试阶段：可以短暂使用 `open`；
- 面向陌生人：不要直接 `open`，除非你明确知道风险。

### 14.6 群聊策略

默认：

```bash
WEIXIN_GROUP_POLICY=disabled
```

可选：

```bash
WEIXIN_GROUP_POLICY=open
WEIXIN_GROUP_POLICY=allowlist
WEIXIN_GROUP_ALLOWED_USERS=group_id_1,group_id_2
```

注意：`WEIXIN_GROUP_ALLOWED_USERS` 这个变量名容易误导，它实际需要的是 group chat ID，不是群成员 user ID。

### 14.7 微信接入常见问题

| 问题 | 处理 |
|---|---|
| `aiohttp and cryptography are required` | 安装 `pip install aiohttp cryptography` |
| `WEIXIN_TOKEN is required` | 重新运行 `hermes gateway setup` 扫码 |
| `WEIXIN_ACCOUNT_ID is required` | 在 `.env` 中设置账号 ID |
| gateway 不响应 DM | 检查 `WEIXIN_DM_POLICY` 和白名单 |
| gateway 不响应群消息 | 可能是 iLink 账号类型无法收到群事件 |
| 媒体上传下载失败 | 检查 `cryptography` 和 CDN 网络 |
| session expired | 重新扫码登录 |
| 二维码无法显示 | 安装 messaging extra 或打开终端给出的 URL |
| 消息重复 | 检查是否启动了多个 gateway 实例 |

---

## 15. Cron：定时任务系统

Hermes 内置 cron 调度。它可以通过自然语言或 cron 表达式创建任务。

可以做：

- 一次性任务；
- 周期性任务；
- 暂停 / 恢复 / 编辑 / 触发 / 删除任务；
- 给任务附加 skill；
- 把结果发送到原聊天、本地文件或指定平台；
- 运行纯脚本 no-agent mode，不经过 LLM，直接发送 stdout。

### 15.1 聊天内创建定时任务

```text
/cron add 30m "Remind me to check the build"
/cron add "every 2h" "Check server status"
/cron add "every 1h" "Summarize new feed items" --skill blogwatcher
```

### 15.2 典型用途

| 场景 | 示例 |
|---|---|
| 每日报告 | 每天早上总结新闻、项目状态或服务器状态 |
| 论文追踪 | 每天检索 PubMed / arXiv 新文献 |
| 运维监控 | 每小时检查服务健康 |
| 数据任务 | 每晚备份文件或运行数据脚本 |
| 自媒体工作流 | 定时收集热点、生成选题候选 |
| 个人提醒 | 定时提醒喝水、运动、检查任务 |

### 15.3 安全限制

官方文档说明，Cron-run session 不能递归创建更多 cron job。这样做是为了避免无限调度循环。

---

## 16. Subagents：任务委派与并行执行

Hermes 支持 `delegate_task`，可以把任务拆给子代理执行。

适合：

- 并行研究多个方向；
- 一个代理查资料，一个代理写总结；
- 代码实现与代码审查分离；
- 多个数据处理任务并行；
- 复杂任务拆解。

官方文档中强调：

- 每个 subagent 有自己的 terminal session；
- 子代理结果通常以最终摘要进入父上下文；
- 父任务被中断时，子代理也会被中断；
- 子代理默认不会在父任务结束后继续运行；
- 如果需要长期、可恢复的任务，应使用 cronjob 或 background terminal。

---

## 17. Kanban：多 Agent 持久任务看板

Hermes Kanban 是一个跨 Hermes profiles 共享的持久任务板，底层存储在：

```text
~/.hermes/kanban.db
```

它的作用不是普通待办清单，而是让多个具名 Agent 协作处理任务。

适合：

- 研究工作流：researcher → analyst → writer；
- 工程工作流：拆解 → 并行实现 → review → PR；
- 长期运营：每日简报、账号运营、服务监控；
- 多角色协作：一个 Agent 负责资料，一个负责写作，一个负责校对；
- 数字分身：给不同任务创建不同长期助手。

两类入口：

1. Agent 通过 `kanban_*` 工具操作；
2. 用户通过 CLI、slash command 或 dashboard 操作。

---

## 18. MCP：连接外部工具生态

MCP 即 Model Context Protocol。Hermes 可以通过 MCP 连接外部工具服务器。

适合连接：

- GitHub；
- 数据库；
- 文件系统；
- 浏览器栈；
- 公司内部 API；
- 自定义工具服务；
- 第三方 MCP server。

配置示例：

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

HTTP MCP 示例：

```yaml
mcp_servers:
  company_api:
    url: "https://mcp.internal.example.com"
    headers:
      Authorization: "Bearer ***"
```

Hermes 会将 MCP 工具注册成：

```text
mcp_<server_name>_<tool_name>
```

例如：

```text
mcp_filesystem_read_file
mcp_github_create_issue
```

### 18.1 MCP 工具过滤

可以只暴露白名单工具：

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [create_issue, list_issues]
```

也可以排除高风险工具：

```yaml
mcp_servers:
  stripe:
    url: "https://mcp.stripe.com"
    tools:
      exclude: [delete_customer]
```

### 18.2 MCP 安全点

官方文档说明，Hermes 对 stdio MCP server 不会盲目传递完整 shell 环境，而是只传显式配置的 `env` 和安全 baseline，以降低密钥泄露风险。

---

## 19. Web Dashboard：浏览器管理界面

Hermes 提供本地 Web Dashboard，用于管理安装、配置和运行状态。

启动：

```bash
hermes dashboard
```

默认打开：

```text
http://127.0.0.1:9119
```

官方强调：Dashboard 默认只绑定 localhost，数据不会离开本机。

### 19.1 需要额外依赖

如果默认安装不包含 Web 依赖，可安装：

```bash
pip install 'hermes-agent[web,pty]'
```

或更全面：

```bash
pip install 'hermes-agent[all]'
```

### 19.2 Dashboard 可以管理什么？

| 页面 | 功能 |
|---|---|
| Status | 查看版本、gateway 状态、平台状态、活跃会话 |
| Chat | 浏览器内聊天 |
| Config | 修改配置 |
| API Keys | 管理 `.env` 中的密钥 |
| Sessions | 查看最近会话 |
| Logs | 查看日志 |
| Analytics | token 使用与成本分析 |
| Cron | 创建、暂停、恢复、触发、删除定时任务 |
| Skills | 浏览、搜索、启用 / 禁用技能 |
| Toolsets | 查看工具集启用状态 |

### 19.3 Dashboard 安全风险

不要随便使用：

```bash
hermes dashboard --host 0.0.0.0
```

原因：Dashboard 可以读写 `.env`，而 `.env` 中可能有 API keys、消息平台 token 等敏感信息。官方文档明确警告：如果绑定到 `0.0.0.0`，同一网络的人可能访问并修改你的凭证，除非你有防火墙和强认证。

---

## 20. 安全模型

Hermes Agent 官方文档将安全模型描述为 defense-in-depth，即多层防御。

主要层级包括：

1. 用户授权：谁能和 Agent 对话；
2. 危险命令审批；
3. 容器隔离；
4. MCP 凭证过滤；
5. 上下文文件扫描；
6. 跨会话隔离；
7. 输入清洗。

### 20.1 危险命令审批

配置位置：

```yaml
approvals:
  mode: manual    # manual | smart | off
  timeout: 60
```

| 模式 | 含义 |
|---|---|
| `manual` | 默认模式。危险命令必须人工确认 |
| `smart` | 使用辅助 LLM 评估风险，低风险自动批准，高风险自动拒绝，不确定再让用户确认 |
| `off` | 关闭审批，相当于 yolo，非常危险 |

### 20.2 YOLO mode

启用方式：

```bash
hermes --yolo
hermes chat --yolo
```

或会话内：

```text
/yolo
```

或环境变量：

```bash
HERMES_YOLO_MODE=1
```

风险：YOLO 会绕过危险命令审批。除非是在一次性容器、CI/CD 或完全可信环境中，否则不建议新手使用。

### 20.3 Hardline Blocklist

即使开启 yolo，某些命令仍然会被 Hermes 永久拦截，例如：

- `rm -rf /`；
- fork bomb；
- 对根设备执行 `mkfs`；
- `dd if=/dev/zero of=/dev/sd*`；
- 在 rootfs 顶层 pipe 远程 URL 到 `sh` 的危险形式。

这属于不可绕过的安全底线。

### 20.4 容器隔离

容器后端会使用多种加固措施：

- 只读 root filesystem；
- drop Linux capabilities；
- no privilege escalation；
- PID limits；
- namespace isolation；
- 使用 volumes 持久化 workspace，而不是写 root layer。

---

## 21. SOUL.md、Context Files 与人格配置

Hermes 支持通过文件给 Agent 提供长期上下文或人格约束。

常见概念：

| 文件 / 功能 | 作用 |
|---|---|
| `SOUL.md` | 定义 Hermes 默认语气、风格、人格 |
| `AGENTS.md` | 项目级 Agent 指南 |
| Context Files | 给特定项目或目录提供上下文 |
| Memory | 动态记忆 |
| Skills | 可复用操作技能 |

区别可以这样理解：

```text
SOUL.md       → 这个 Agent 说话和工作的大风格
AGENTS.md    → 当前项目怎么做事
Memory       → 它长期记住的事实和经验
Skills       → 它学会的一套操作流程
```

---

## 22. Hermes Agent 与普通 AI 工具的区别

| 对比项 | 普通聊天机器人 | IDE Copilot | Hermes Agent |
|---|---|---|---|
| 运行方式 | 浏览器或 App | IDE 内 | CLI、服务器、VPS、容器、云沙箱、消息平台 |
| 是否长期运行 | 通常不是 | 通常不是 | 可以 |
| 是否跨会话记忆 | 取决于产品 | 较弱 | 内置 Memory |
| 是否生成技能 | 通常不会 | 通常不会 | 内置 Skills |
| 是否能操作终端 | 通常不能 | 有限 | 可以 |
| 是否能接消息平台 | 通常不能 | 不能 | 可以 |
| 是否能做定时任务 | 通常不能 | 不能 | 可以 |
| 是否能接 MCP | 取决于平台 | 取决于 IDE | 支持 |
| 是否可自部署 | 多数不能 | 部分不能 | 开源，可部署 |
| 安全边界 | 平台控制 | IDE 权限 | 审批、容器、授权、过滤等 |

---

## 23. 典型使用场景

### 23.1 个人长期助手

你可以让 Hermes 记住：

- 你的研究方向；
- 常用文件路径；
- 常用命令；
- 写作偏好；
- 固定工作流程；
- 常见报错处理办法。

之后你可以通过微信、Telegram 或 CLI 让它继续处理任务。

### 23.2 编程 Agent

适合：

- 读取项目结构；
- 修改文件；
- 运行测试；
- 写脚本；
- 创建 PR；
- 生成文档；
- 调用 GitHub MCP；
- 通过 ACP 接入编辑器。

### 23.3 科研资料助手

适合：

- 定时检索论文；
- 汇总文献；
- 维护研究主题看板；
- 生成初步综述；
- 整理实验流程；
- 调用浏览器和网页提取工具；
- 保存学术写作偏好为 skill。

### 23.4 自媒体工作流

适合：

- 定时收集热点；
- 生成选题；
- 检索资料；
- 生成脚本；
- 生成封面提示词；
- 整理发布计划；
- 通过消息平台随时远程调用。

### 23.5 运维与自动化

适合：

- 定时检查服务器；
- 运行备份脚本；
- 汇报日志；
- 监控服务；
- 通过 Slack/Discord/Telegram 推送结果。

---

## 24. 新手推荐配置路径

如果你是 Windows 11 + WSL2 用户，推荐路径如下。

### 第一步：确认 WSL2 可用

```powershell
wsl --status
```

进入 WSL：

```powershell
wsl
```

### 第二步：在 WSL2 内安装 Hermes

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes setup
```

### 第三步：配置模型

```bash
hermes model
```

优先先让一个模型能正常聊天，不要一开始就配置所有功能。

### 第四步：测试 CLI

```bash
hermes chat
```

测试一个简单任务：

```text
请回复“Hermes 已正常工作”
```

### 第五步：配置工具

```bash
hermes tools
```

新手先启用：

- terminal；
- file；
- web；
- memory；
- skills；
- session_search。

浏览器工具可以后面再处理。

### 第六步：配置消息平台

```bash
hermes gateway setup
```

建议先选一个平台测试，不要一次接入太多平台。

### 第七步：安全设置

建议：

```yaml
approvals:
  mode: manual
```

不要一开始使用：

```bash
hermes --yolo
```

### 第八步：出现问题用 doctor

```bash
hermes doctor
```

---

## 25. 你之前遇到的问题如何理解？

### 25.1 `Directory exists but is not a git repository`

含义：目标目录存在，但不是正常 git 仓库。可能是之前安装中断或目录残留。

常见处理思路：

```bash
rm -rf /home/kingwu/.hermes/hermes-agent
```

然后重新运行安装命令。

前提：确认该目录不是你手动保存的重要文件。

### 25.2 `Playwright does not support chromium on ubuntu26.04-x64`

含义：Hermes 主体可能已经装好了，但 browser tools 所依赖的 Playwright Chromium 不支持当前系统版本。

处理优先级：

1. 先跳过 browser tools；
2. 保证 CLI、模型、terminal、file、gateway 正常；
3. 需要浏览器工具时，换 Ubuntu 22.04 / 24.04 或 Docker；
4. 再执行：

```bash
cd /home/kingwu/.hermes/hermes-agent
npx playwright install --with-deps chromium
```

### 25.3 “浏览器工具安装失败”是否影响 Hermes 主体？

通常不影响核心功能。受影响的是：

- browser_navigate；
- browser_snapshot；
- browser_vision；
- 依赖真实浏览器的网页自动化能力。

不受影响或通常仍可用的是：

- CLI 对话；
- 模型调用；
- terminal；
- 文件操作；
- memory；
- skills；
- 部分 web search / extract；
- gateway；
- cron。

---

## 26. 学习 Hermes Agent 的建议顺序

建议不要从“所有功能”开始，而是分层学习：

```text
第 1 层：安装 + 模型配置 + CLI 聊天
第 2 层：terminal / file / web 工具
第 3 层：memory / skills
第 4 层：gateway 消息平台
第 5 层：cron 定时任务
第 6 层：Docker / SSH backend 安全隔离
第 7 层：MCP 外部工具
第 8 层：browser tools / dashboard / kanban / subagents
```

### 为什么这样学？

因为 Hermes 的复杂性来自“组合能力”。如果一开始就配置微信、浏览器、MCP、定时任务、Docker、多个模型，很难判断报错来自哪里。

更稳妥的顺序是：

```text
先让它能说话
再让它能执行命令
再让它能记住东西
再让它能远程对话
再让它能定时工作
最后再做复杂集成
```

---

## 27. 最小可用配置模板

下面是一套适合初学者的最小可用思路。

### 27.1 基础安装

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
```

### 27.2 选择模型

```bash
hermes model
```

### 27.3 启动聊天

```bash
hermes chat
```

### 27.4 检查工具

```bash
hermes tools
```

### 27.5 启动诊断

```bash
hermes doctor
```

### 27.6 设置消息平台

```bash
hermes gateway setup
hermes gateway
```

### 27.7 使用 Docker 隔离

```yaml
terminal:
  backend: docker
  docker_image: python:3.11-slim
  container_persistent: true
```

---

## 28. 进阶配置模板：更适合长期使用

```yaml
terminal:
  backend: docker
  cwd: "."
  timeout: 180
  docker_image: python:3.11-slim
  container_cpu: 2
  container_memory: 8192
  container_disk: 51200
  container_persistent: true

approvals:
  mode: manual
  timeout: 60

mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    enabled: true
```

对应思路：

- Docker 隔离 Agent 的 shell 操作；
- 保留危险命令人工审批；
- 通过 MCP 暴露特定项目目录；
- 不把整个用户主目录暴露给 Agent；
- 需要更多工具时逐步添加。

---

## 29. 最重要的安全建议

1. 不要在不了解风险时开启 `--yolo`。
2. 不要把 Dashboard 绑定到公网地址。
3. 不要把所有 API Key 暴露给所有 MCP server。
4. 不要在 local backend 下让 Agent 操作重要目录。
5. 用 Docker 或 SSH backend 隔离高风险任务。
6. 微信 / Telegram 等消息平台建议设置 allowlist。
7. 不要让陌生人直接 DM 你的 Agent。
8. 定时任务要先小范围测试。
9. 删除、格式化、批量修改文件前必须人工确认。
10. 重要数据先备份。

---

## 30. 结论

Hermes Agent 的价值不在于“它能不能回答问题”，而在于它把 LLM 放进了一个长期运行、可记忆、可调用工具、可跨平台交互、可定时执行、可自我沉淀技能的执行环境中。

它更适合这些人：

- 想要一个长期 AI 助手；
- 想把 AI 接入服务器、终端、文件和消息平台；
- 想做自动化、定时任务或远程控制；
- 想让 AI 逐步记住自己的项目和工作方式；
- 想用开源框架搭建自己的 Agent 工作流；
- 愿意处理环境配置、API Key、权限和安全边界。

它不适合这些人：

- 只想打开网页问一句话；
- 不想处理任何命令行；
- 不愿意配置模型 API；
- 不能接受安装和排错成本；
- 对安全边界完全没有概念但又想让 Agent 操作真实文件系统。

对初学者最稳妥的路线是：

```text
WSL2 安装 → hermes model → hermes chat → hermes tools → memory/skills → gateway → cron → Docker/MCP/browser/kanban
```
---

32. 官方资料来源

1. Hermes Agent 官方首页：<https://hermes-agent.nousresearch.com/>
2. Hermes Agent 官方文档首页：<https://hermes-agent.nousresearch.com/docs/>
3. Quickstart：<https://hermes-agent.nousresearch.com/docs/getting-started/quickstart>
4. Installation：<https://hermes-agent.nousresearch.com/docs/getting-started/installation>
5. Configuration：<https://hermes-agent.nousresearch.com/docs/user-guide/configuration>
6. Tools & Toolsets：<https://hermes-agent.nousresearch.com/docs/user-guide/features/tools>
7. Persistent Memory：<https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
8. Skills System：<https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
9. Messaging Gateway：<https://hermes-agent.nousresearch.com/docs/user-guide/messaging>
10. Weixin / WeChat：<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/weixin>
11. Security：<https://hermes-agent.nousresearch.com/docs/user-guide/security>
12. Scheduled Tasks / Cron：<https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>
13. MCP：<https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp>
14. Web Dashboard：<https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard>
15. Subagent Delegation：<https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation>
16. Kanban：<https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban>
17. ACP Editor Integration：<https://hermes-agent.nousresearch.com/docs/user-guide/features/acp>
18. GitHub 仓库：<https://github.com/NousResearch/hermes-agent>
