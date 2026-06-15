---
title: "Getting the most out of Codex如何充分利用 Codex"
source: "https://x.com/jxnlco/status/2057153744630890620"
author:
  - "[[@jxnlco]]"
published: 2026-05-21
created: 2026-05-21
description: "Most developers first use coding agents for code: inspect a repository, make a diff, run tests, and open a pull request.That’s still the cen..."
tags:
  - Codex
  - Agent
  - 工作流
  - MCP
  - Skill
  - clippings
---
![Image](https://pbs.twimg.com/media/HIx6TgrX0AAdNFj?format=jpg&name=large)

Most developers first use coding agents for code: inspect a repository, make a diff, run tests, and open a pull request.

That’s still the center of gravity for Codex. But much of the work on a computer is already mediated by code: executing shell commands, browsing web pages, calling APIs, exporting documents, responding to events, and triggering automations. As those surfaces become available to Codex, it starts to feel less like a coding assistant in the narrow sense and more like a system for getting computer work done.

The [Codex app](https://developers.openai.com/codex/app/features/) makes that shift concrete. A thread can keep context, use tools, surface artifacts, and continue across prompts instead of resetting after each exchange.

Getting more out of Codex means using these capabilities together:

- durable threads that preserve context
- voice, steering, and queuing while the user is still in the loop
- browser, computer-use, MCP servers, and connectors that let Codex act beyond a repo
- thread automations and Goals that continue the work while the user is away
- the side panel, where users can review code, documents, decks, and other artifacts

## Durable threads

> **Durable threads:** Long-running Codex threads that preserve working context across repeated sessions.

Pinned threads are one way to keep durable threads close at hand. They’re useful for recurring work streams such as:

- a Chief of Staff thread
- a release thread
- a documentation review thread
- a thread dedicated to external monitoring

These are persistent workspaces, not short chats. Codex can revisit them over time, preserving prior decisions, preferences, and working context that would otherwise need to be rebuilt from scratch.

Pinned-thread shortcuts make this practical. Command-1 through Command-9 jump directly into saved threads.

## Voice input

Voice input is valuable because it captures the rough version of a thought before it’s compressed into polished prose.

Codex has built-in voice input. It works especially well for vague starting points that are natural to say but awkward to type:

I think someone named Ben mentioned this in Slack. I do not remember the details. Please go look.

For an agent that can search, gather context, and report back, that’s often enough.

It also works well for a two- or three-minute thought dump before the task is fully formed.

Transcripts work the same way. A raw meeting transcript or dictated planning note often provides better source material than a short summary because it preserves uncertainty, emphasis, and unfinished lines of thought.

## Steering and queuing

Voice becomes even more useful when paired with explicit control over an active task.

> **Steering:** Interrupting an in-flight Codex task with new direction before the current step finishes.

Steering is useful when the agent is heading the wrong way and needs a correction before it finishes. During a website review, for example, the user can interrupt the work while annotating the surface in the side panel:

- make this smaller
- the spacing between these two elements feels off
- this copy is wrong

> **Queuing:** Adding work for Codex to do after the current step completes.

Queuing is different. It doesn’t interrupt the task in progress. It adds the next task to the line. A user might say:

Once the work is done, send the preview link to the reviewer in Slack.

Steering changes what Codex is doing now. Queuing changes what should happen next. Both keep the user close to the work while it’s unfolding.

## Tools and reach

Once a thread has continuity, the next question is what it can act on. Codex can move outward in layers:

- [$browser](https://developers.openai.com/codex/app/browser) for the in-app browser in the side panel, where Codex can inspect and annotate web surfaces
- [@chrome](https://developers.openai.com/codex/app/chrome-extension) for signed-in browser state and Chrome-based workflows
- [@computer](https://developers.openai.com/codex/app/computer-use) for work that only exists through a desktop GUI

[$browser](https://x.com/search?q=%24browser&src=cashtag_click) fits side-panel browser review. [@chrome](https://x.com/@chrome) fits signed-in browser work that depends on the user’s Chrome context. [@computer](https://x.com/@computer) fits tasks that only exist through a desktop GUI.

MCP servers and connectors extend the same idea into the rest of a workflow. [Slack](https://developers.openai.com/codex/integrations/slack), [Gmail](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), and [Calendar](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) matter because many important tasks first appear as messages, inbox items, or scheduling problems before they ever become code.

Skills make repeated workflows reusable. Once a workflow proves useful, [package it as a skill](https://developers.openai.com/codex/skills) so Codex can run it again without relearning the routine from scratch.

## Work from anywhere

The [Codex mobile app](https://openai.com/index/work-with-codex-from-anywhere/) changes when the user has to be at the desk. A task can start on a Mac where the files, permissions, and local setup already live, then continue while the user checks in from a phone.

That matters in small moments. Someone can leave the desk while Codex runs a longer task, answer a question from outside, approve the next step, or redirect the thread before they get back. The local environment stays in place; the user doesn’t have to.

## Automations

[Automations](https://developers.openai.com/codex/app/automations) run Codex work on a schedule. Use a scheduled automation when the recurring job should start fresh from a workspace, such as a daily report or a regular repository check. Use a thread automation when the schedule should return to an active conversation with its running context.

> **Thread automations:** Heartbeat-style recurring wake-up calls that return to the same Codex thread on a schedule.

Pinned threads are useful, but they still wait for the user to return. A thread automation can check on something every few minutes or every few hours, continue until it meets a condition, and adjust the cadence over time.

A Chief of Staff thread might run every 30 minutes:

Every 30 minutes, check Slack and Gmail for unanswered messages that need my attention. Help me prioritize what matters most. If someone asks me a question, research the answer as deeply as you can and draft a reply for me, but do not send it.

When the user returns, the expensive part of gathering context is often done. The human still decides what gets sent.

Thread automations also fit feedback loops. A thread automation can watch pull request comments, Google Docs comments, or Slack replies and keep the surrounding work moving while the user is away.

Consider an animation workflow where a reviewer shares a video in Slack. A thread automation can check the thread on a schedule, render an updated version when comments arrive, and reply in the same thread tagging the reviewer. If one integration can’t complete the final upload, desktop automation can finish the step through the GUI.

The loop spans Slack for feedback, the codebase for rendering, and desktop automation for the final upload.

## Goals

Goals are most powerful when the task has a real finish line that the agent can keep pushing toward. A weak goal is:

> **Goals:** Longer-running Codex tasks with a finish line the agent can keep working toward over time.

Implement the plan in this Markdown file.

A stronger goal has a measurable success criterion.

For example, an engineer might migrate an internal tool from Python to Rust by setting up the new directory, defining the goal, and making the finish line explicit: the new implementation isn’t done until the unit tests pass.

A goal combines ongoing execution with a verifier. The user defines the outcome, the stopping condition, and the signal that says whether Codex is getting closer.

Useful verifiers include:

- a test suite
- a benchmark
- a bug reproduction
- a validation matrix
- an end-to-end workflow that must keep passing

Ambition matters, but without verification it’s just a wish.

## The side panel侧面板

The [side panel](https://developers.openai.com/codex/app/features) keeps the work beside the conversation that produced it. Instead of exporting an artifact and switching contexts, the user can review it in place. The output might be code, but it might also be a deck, a PDF, a browser page, a table, or another artifact created along the way.这[侧面板](https://developers.openai.com/codex/app/features)它将工作成果保留在产生它的对话中。用户无需导出成果并切换上下文，即可直接在原地查看。输出结果可以是代码，也可以是演示文稿、PDF、浏览器页面、表格或其他过程中创建的内容。

It supports four jobs especially well:它尤其擅长支持以下四种工作：

1. Inspect artifacts检查文物
2. Annotate what needs to change标注需要更改的内容
3. Operate web surfaces操作网页表面
4. Review changes审查变更

The side panel lets users review Markdown, spreadsheets, data tables, documents, and slides in place. They can inspect, mark up, and revise artifacts without breaking the loop.侧边栏允许用户直接查看 Markdown 文件、电子表格、数据表、文档和幻灯片。他们可以在不中断当前操作的情况下检查、标记和修改这些内容。

![Image](https://pbs.twimg.com/media/HIx6vBrXsAAV42q?format=jpg&name=large)

Annotations注释

The deck or PDF can stay open beside the thread that produced it, ready for direct review and repair.卡组或 PDF 文件可以保持打开状态，与生成它的帖子并排显示，方便直接查看和修改。

![Image](https://pbs.twimg.com/media/HIx6njlXIAAWuXh?format=jpg&name=large)

Sheets in Codex法典中的纸张

The [in-app browser](https://developers.openai.com/codex/app/browser) lets Codex inspect a rendered page, control it, and respond to annotations directly on the surface under review. Comments on a page or artifact stay inside the working loop instead of becoming a separate handoff.这[应用内浏览器](https://developers.openai.com/codex/app/browser) Codex 允许检查已渲染的页面，对其进行控制，并直接在被审查的页面上响应注释。页面或工件上的注释会保留在工作循环中，而不会变成单独的交接流程。

The web becomes both output and control surface. Codex can build an artifact, open it in the side panel, inspect it, debug it, and keep refining the same object in place.Web 既是输出界面，也是控制界面。Codex 可以构建一个工件，在侧边栏中打开它，检查它，调试它，并不断地在原地完善同一个对象。

![Image](https://pbs.twimg.com/media/HIx62e0WgAA9wE4?format=jpg&name=large)

These surfaces work especially well:这些表面效果尤其好：

- index.html for lightweight static artifactsindex.html 用于轻量级静态文件
- Storybook for UI reviewUI 评审故事书
- Remotion Studio for programmatic animation用于程序化动画的 Remotion Studio
- browser-based slide decks for presentations用于演示的基于浏览器的幻灯片
- data apps for analysis workflows用于分析工作流程的数据应用程序

A single index.html file can become a durable interactive artifact with no server required. Thread automations can also refresh static artifacts over time so a thread has something new waiting when the user returns.单个 index.html 文件即可成为一个持久的交互式对象，无需服务器。线程自动化还可以随时间刷新静态对象，以便用户返回时线程能够提供新的内容。

## Shared memory共享内存

Long-running threads become more useful when they share memory outside any one conversation.长时间运行的线程如果能在单个对话之外共享内存，就会变得更有价值。

> **Shared memory:** Durable context stored outside a single thread so future work can resume from something explicit and reviewable.**共享内存：** 持久化上下文存储在单个线程之外，以便将来可以从明确且可审查的内容恢复工作。

One durable pattern is to anchor persistent threads in an Obsidian vault. In practice, that means a folder of plain files that stays straightforward to inspect, edit, move, and keep for a long time. Teams can store that folder in cloud storage, Git, Dropbox, Google Drive, or another sync layer that fits their workflow.一种持久的模式是将持久线程锚定在 Obsidian Vault 中。实际上，这意味着创建一个仅包含普通文件的文件夹，以便长期轻松地查看、编辑、移动和保存这些文件。团队可以将该文件夹存储在云存储、Git、Dropbox、Google Drive 或其他适合其工作流程的同步层中。

A vault might look like this:金库可能长这样：

vault/ ├── TODO.md ├── people/ ├── projects/ ├── agent/ └── notes/保险库/ ├── TODO.md ├── 人/ ├── 项目/ ├── 代理/ └── 注释/

At the top level, AGENTS.md can define how Codex should update that workspace as it learns more about people, projects, decisions, and open loops.在顶层，AGENTS.md 可以定义 Codex 应该如何更新工作区，随着它对人员、项目、决策和未解决的问题了解得越多，更新就越快。

Don’t copy one exact vault structure. Teach the agent where durable context should live, what context to preserve, and when not to create churn.不要照搬现有的存储库结构。要教会代理程序持久上下文应该存放在哪里，需要保留哪些上下文，以及何时不应该进行变更。

A practical AGENTS.md might say:一份实用的 AGENTS.md 文件可能会这样写：

\- Treat ~/vault as durable work memory. - Prefer canonical notes over note sprawl. - Route TODOs, people, projects, daily summaries, and scratch notes explicitly. - Preserve decisions, blockers, owners, dates, and useful links. - If nothing meaningful changed, do not churn the vault.- 将 ~/vault 视为持久工作内存。 - 比起杂乱无章的音符，更倾向于规范的音符。 - 明确记录待办事项、人员、项目、每日总结和草稿。 - 保留决策、阻碍因素、所有者、日期和有用链接。 - 如果没有实质性的变化，就不要翻动金库。

Repositories hold code. The vault holds rolling context: the people involved, what changed, what’s blocked, what needs follow-up, and what would otherwise disappear between sessions.代码仓库存放代码。代码库则保存着不断更新的上下文信息：包括相关人员、变更内容、阻塞问题、需要跟进的问题，以及那些在会话之间会丢失的信息。

Important context shouldn’t live only inside a conversation transcript. Write it down somewhere the next thread can pick back up.重要的背景信息不应该只存在于对话记录中。应该把它写下来，以便后续对话可以继续进行。

Codex also has first-party [memory features](https://developers.openai.com/codex/memories) in Settings > Personalization > Memories. They provide a local recall layer for preferences, recurring workflows, and known pitfalls. They complement explicit written context rather than replacing it. [Chronicle](https://developers.openai.com/codex/memories/chronicle) pushes in the same direction by helping Codex build memory from recent screen context.Codex 也拥有第一方[内存功能](https://developers.openai.com/codex/memories)在“设置”>“个性化”>“记忆”中。它们为偏好设置、重复性工作流程和已知陷阱提供了一个本地召回层。它们是对明确书面上下文的补充，而不是替代。 [编年史](https://developers.openai.com/codex/memories/chronicle)通过帮助 Codex 从最近的屏幕上下文中构建内存，朝着同一个方向推动。

## From code outward从代码向外

Codex still starts from code. But more of the work around code is now reachable through the same system: MCP servers, browser surfaces, desktop controls, thread automations, and reviewable artifacts.Codex 仍然以代码为基础。但现在更多与代码相关的工作都可以通过同一个系统完成：MCP 服务器、浏览器界面、桌面控件、线程自动化和可审查的工件。

That changes the control model. Steering interrupts the work in progress. Queuing lines up the next task. Thread automations keep a thread active when the user steps away. Goals add a concrete finish line that Codex can keep working toward.这改变了控制模型。转向会中断正在进行的工作。排队会安排下一个任务。线程自动化会在用户离开时保持线程处于活动状态。目标则为 Codex 设定了一个具体的终点，使其能够持续朝着这个目标努力。

Codex can now carry a workflow from instruction to execution to artifact review, even when the work leaves the repo.现在，即使工作成果离开了代码库，Codex 也能将工作流程从指令执行到成果审查。

---
