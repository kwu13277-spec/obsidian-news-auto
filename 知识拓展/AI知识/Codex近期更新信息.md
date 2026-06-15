建议文件名：Codex近期更新信息.md

# Codex 近期更新：移动端远程访问、CLI 改进与计费变化

内容类型：主题知识介绍

## 摘要

截至 2026-05-18，Codex 的近期更新集中在移动端远程访问、CLI 迭代、Chrome 扩展、Auto-review 文档、Windows/WSL 支持和 token-based 计费。

## 关键词

Codex；Codex CLI；远程连接；ChatGPT 移动端；Auto-review；Windows Sandbox；WSL2；token-based pricing

## 大纲

1. [近期更新主线](#section-1)
2. [移动端远程访问](#section-2)
3. [CLI 版本更新](#section-3)
4. [Chrome 扩展与浏览器工作流](#section-4)
5. [Windows 与 WSL2 支持](#section-5)
6. [计费与使用限制](#section-6)
7. [实际更新操作建议](#section-7)
8. [参考来源](#section-8)

## 正文

<a id="section-1"></a>

### 1. 近期更新主线：Codex 从本地编码工具转向跨设备开发代理

本节概要：本节说明 Codex 近期更新的总体方向，重点是远程控制、自动化、浏览器协作和更细化的计费方式。

Codex 近期变化的核心不是单一功能增加，而是产品形态的变化：它正在从“在本地终端或桌面 App 中帮你写代码的工具”，逐步扩展为“可以在桌面、CLI、浏览器、移动端之间连续运行的开发代理”。这意味着 Codex 不再只处理一次性代码生成，而是更强调长任务、并行线程、审批、差异审查、自动化和跨设备接管。

2026 年 5 月的官方 Codex changelog 中，OpenAI 把“Work with Codex from anywhere”列为重点更新。该能力允许用户在 ChatGPT 手机 App 中连接一台正在运行 Codex App 的 Mac，使手机端可以继续访问同一主机上的项目、文件、凭据、插件、skills 和配置。同期更新还包括 Hooks general availability、Codex access tokens for trusted automation 和 Enterprise admin setup guidance。

<a id="section-2"></a>

### 2. 移动端远程访问：手机连接的是运行 Codex 的 Mac 主机

本节概要：本节说明移动端远程访问的工作方式，重点是手机端负责控制和审批，实际代码环境仍在连接主机上。

2026-05-14 的 ChatGPT Release Notes 显示，Codex 已在 ChatGPT mobile app 中以 preview 形式开放。用户可以在手机端继续已有 Codex 线程，也可以新建线程、回答 Codex 的问题、调整方向、批准操作、查看 Codex 找到的内容，并在多个连接主机之间切换。

这里需要特别理解一个关键点：手机端并不是直接运行你的项目环境。Codex 仍然运行在连接的 Mac 主机上，手机端加载的是该主机上的实时上下文，包括项目上下文、审批状态、插件、截图、终端输出、diff 和测试结果。因此，手机端更像是一个“远程控制台”，而不是一个独立开发环境。

官方说明中还提到，Codex mobile experience 正在 iOS 和 Android 上面向所有计划逐步推出，包括 Free 和 Go，但前提是位于支持地区。使用前需要同时更新 ChatGPT mobile app 和 macOS Codex App。设置流程从主机端 Codex App 开始，再通过扫描二维码在 ChatGPT 中继续；远程访问持续可用的前提是主机保持唤醒、在线并运行 Codex。

<a id="section-3"></a>

### 3. CLI 版本更新：0.130.0 强化远程控制，0.129.0 强化 TUI 体验

本节概要：本节说明 Codex CLI 最近两个重要版本的变化，重点是 remote-control、app-server、Vim 模式、状态栏和线程操作体验。

2026-05-08，Codex CLI 发布 `0.130.0`。这个版本的重点是远程控制和 app-server 相关能力。官方安装命令为：

```bash
npm install -g @openai/codex@0.130.0
```

`0.130.0` 的主要变化包括：插件详情页可以显示 bundled hooks；插件分享支持链接元数据和可发现性控制；新增 `codex remote-control`，作为启动 headless、可远程控制 app-server 的更简单入口；app-server 客户端可以对大型线程分页加载；Bedrock auth 可以使用来自 `aws login` profiles 的 AWS console-login 凭据；`view_image` 在多环境会话中可以通过选定环境解析文件。

该版本也修复了一些工程体验问题，例如 live app-server 线程无需重启即可读取配置变化、apply-patch 后 diff 更准确、线程摘要/重命名/恢复/fork 路径更稳定，以及 Windows sandbox 在多个 CLI 版本和已安装 app 目录场景下的启动处理更稳。

2026-05-07，Codex CLI 发布 `0.129.0`。这个版本更偏向终端交互体验，尤其适合经常在 TUI 中使用 Codex 的用户。官方安装命令为：

```bash
npm install -g @openai/codex@0.129.0
```

`0.129.0` 的主要变化包括：TUI composer 支持 Vim 模态编辑，包括 `/vim`、默认模式配置和 Vim-specific keymap contexts；resume/fork picker 重做；支持 raw scrollback mode、`/ide` 上下文注入和 workspace-aware `/diff`；状态栏可以显示主题适配颜色、可选 PR 摘要和分支变化摘要；`/keymap debug` 可用于检查终端按键事件。

如果你主要关心稳定性和远程控制，应优先更新到 `0.130.0` 或更新的最新版本。如果你主要关心终端交互体验，`0.129.0` 开始的 Vim、状态栏和 thread 操作改进也很关键。

<a id="section-4"></a>

### 4. Chrome 扩展与浏览器工作流：Codex 开始处理网页和多标签任务

本节概要：本节说明 Codex for Chrome 的意义，重点是浏览器内应用、网页任务和多标签后台协作。

2026-05-07，官方 changelog 发布 Codex for Chrome。该扩展让 Codex 更适合处理浏览器中的应用和网站任务。官方说明强调，它可以在后台跨多个标签页并行工作，不会直接接管你的浏览器，同时用户可以控制 Codex 能访问哪些网站。

这类能力对前端开发、网页测试、后台管理系统调试和需要登录态的页面检查更有价值。它不是普通意义上的“网页搜索工具”，而是让 Codex 在浏览器上下文中观察页面、操作网页应用并反馈结果，更接近真实用户工作流。

<a id="section-5"></a>

### 5. Windows 与 WSL2 支持：Windows App 已支持核心工作流，但远程移动端重点仍是 macOS

本节概要：本节说明 Windows 端 Codex 的当前状态，重点是 Windows 原生、PowerShell、Windows sandbox 与 WSL2 的关系。

官方 Codex App 文档显示，Codex App 已支持 macOS 和 Windows。Windows 版 Codex App 可以通过 Microsoft Store 下载，也可以使用 `winget` 安装：

```powershell
winget install Codex -s msstore
```

Windows 版支持核心工作流，包括 projects、parallel agent threads、reviewable diffs、worktrees、automations、Git functionality、in-app browser、artifact previews、plugins 和 skills。默认情况下，Windows 版 Codex App 使用 Windows-native agent，也就是通过 PowerShell 运行命令，并配合 Windows sandbox。用户也可以配置 Codex 在 WSL2 中运行，以获得 Linux-native environment。

对你这种 Windows + WSL2 使用场景，需要特别注意三点。第一，如果 agent 运行在 Windows native 模式，项目放在 Windows 文件系统中通常更稳；第二，如果要打开 WSL 文件系统项目，可以通过 `\\wsl$\` 进入对应发行版目录；第三，如果希望 agent 本身在 WSL2 中运行，需要在 Codex App 设置里把 agent 从 Windows native 切换到 WSL，并重启 App 才生效。

不过，移动端远程访问当前官方重点仍是“手机连接运行 Codex 的 macOS 主机”。Windows App 虽然已经可用，但从官方 Release Notes 的表述看，手机远程连接 Windows 主机并不是当前已经明确开放的主路径。

<a id="section-6"></a>

### 6. 计费与使用限制：Codex 转向 token-based pricing

本节概要：本节说明 Codex 计费变化，重点是从按消息估算转向按 input、cached input 和 output tokens 计算 credits。

OpenAI Help Center 的 Codex rate card 显示，2026-04-02 起，Codex pricing 更新为与 API token usage 对齐，而不是 per-message pricing。该变化最初适用于新旧 Plus、Pro、ChatGPT Business 和新的 ChatGPT Enterprise 计划。2026-04-23 起，该更新扩展到所有现有 ChatGPT Enterprise 计划，包括 Edu、Health、Gov 和 ChatGPT for Teachers。

新的计费方式按每 100 万 tokens 计算 credits，并区分三类 token：input tokens、cached input tokens 和 output tokens。官方表格中列出的部分费率如下：

| 模型 | Input tokens / 1M | Cached input tokens / 1M | Output tokens / 1M |
|---|---:|---:|---:|
| GPT-5.5 | 125 credits | 12.50 credits | 750 credits |
| GPT-5.4 | 62.50 credits | 6.250 credits | 375 credits |
| GPT-5.4-Mini | 18.75 credits | 1.875 credits | 113 credits |
| GPT-5.3-Codex | 43.75 credits | 4.375 credits | 350 credits |
| GPT-5.2 | 43.75 credits | 4.375 credits | 350 credits |

这个变化对实际使用的影响是：大项目、长上下文、多轮修复、测试日志、代码 diff 和输出较多的任务会明显影响 credits 消耗。缓存输入 token 的价格较低，因此复用上下文、减少无效输出、避免反复塞入大段无关内容，会更有利于控制成本。

官方 Help Center 还说明，Codex 包含在 ChatGPT Plus、Pro、Business 和 Enterprise/Edu 计划中；限定时间内，Free 和 Go 也包含 Codex，其他计划享有 2x rate limits。

<a id="section-7"></a>

### 7. 实际更新操作建议：按 App、CLI、Windows 三条线分别处理

本节概要：本节给出实际更新路径，重点是避免把桌面 App、CLI、移动端和 Windows/WSL 混为一谈。

如果你使用的是 Codex CLI，最直接的更新方式是运行：

```bash
npm i -g @openai/codex@latest
```

如果你想安装某个明确版本，例如 `0.130.0`，可以使用：

```bash
npm install -g @openai/codex@0.130.0
```

如果你使用的是 macOS Codex App，并且想使用手机远程访问，需要更新两个东西：ChatGPT mobile app 和 macOS Codex App。设置时从 Mac 主机上的 Codex App 开始，然后用手机 ChatGPT 扫码连接。连接后，Mac 主机必须保持在线、唤醒并运行 Codex。

如果你使用的是 Windows Codex App，更新方式是打开 Microsoft Store，进入 Downloads，然后点击 Check for updates。也可以通过 Microsoft Store 或 `winget` 安装。Windows 用户还要根据项目位置决定使用 Windows native agent 还是 WSL2 agent：普通 Windows 项目优先用 Windows native；Linux 工具链强依赖项目可以考虑 WSL2。

如果你主要关注 `/goal`、statusline、Vim 模式、`/ide`、`/diff`、remote-control、plugins hooks、Windows sandbox 或 app-server，那近期版本值得更新。你的使用习惯偏 Windows + WSL2，所以建议优先确认三件事：Codex App 是否为最新、CLI 是否为最新、agent 当前到底运行在 PowerShell 还是 WSL2。

<a id="section-8"></a>

### 8. 参考来源：优先采用 OpenAI 官方资料

本节概要：本节列出本文依据的官方来源，重点是 changelog、release notes、rate card 和平台安装文档。

- OpenAI Developers — Codex changelog  
  https://developers.openai.com/codex/changelog

- OpenAI Help Center — ChatGPT Release Notes  
  https://help.openai.com/en/articles/6825453-chatgpt-release-notes

- OpenAI Help Center — Codex rate card  
  https://help.openai.com/en/articles/20001106-codex-rate-card

- OpenAI Developers — Codex App  
  https://developers.openai.com/codex/app

- OpenAI Developers — Codex App for Windows  
  https://developers.openai.com/codex/app/windows

- OpenAI Developers — Codex CLI  
  https://developers.openai.com/codex/cli

- OpenAI Help Center — Using Codex with your ChatGPT plan  
  https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
