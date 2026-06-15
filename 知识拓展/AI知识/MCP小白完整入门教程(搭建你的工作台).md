---
title: "MCP小白完整入门教程(搭建你的工作台)"
source: "https://x.com/ai_xiaomu/status/2059202018682831129"
author:
  - "[[@ai_xiaomu]]"
published: 2026-05-26
created: 2026-05-27
description: "从前面的Claude Code学到Skill，你应该搭建起了一个自己的SOP：告诉 AI 遇到\"写公众号\"该走什么流程，遇到\"发飞书消息\"该按什么模板。但 Skill 不会让 AI 多长出一只手。让 AI 真的能去爬一个网页、操作你的 Chrome、读写你硬盘上的文件、调你公司内..."
tags:
  - MCP
  - ClaudeCode
  - 入门教程
  - AI工具
  - Skill
  - clippings
---
![Image](https://pbs.twimg.com/media/HJO5voOa0AAEZlo?format=jpg&name=large)

从前面的Claude Code学到Skill，你应该搭建起了一个自己的SOP：告诉 AI 遇到"写公众号"该走什么流程，遇到"发飞书消息"该按什么模板。

但 Skill 不会让 AI 多长出一只手。

让 AI 真的能去爬一个网页、操作你的 Chrome、读写你硬盘上的文件、调你公司内部 API——这件事的标准答案，叫 MCP。

这一篇讲三件事：

MCP 到底是什么

在 Claude Code 里装哪几个就够用

自己怎么接一个最小可用的 MCP Server。

## 先把 Skill 和 MCP 分清楚

很多人把这两个混成一个东西。不是。

![Image](https://pbs.twimg.com/media/HJOwGRrbQAAApuz?format=jpg&name=large)

官方专门成立了一个工作组([modelcontextprotocol.io](https://modelcontextprotocol.io/)), 名字就叫 **Skills Over MCP Working Group**，章程页就摆在 community 目录下。

官方亲口承认这是两个独立、但可以协同的东西。

一个 Skill 内部当然可以调 MCP 工具，就像一篇 SOP 里可以写"打开锤子去钉钉子"。

但 Skill 本身不是锤子，MCP 才是。

所以这篇文章和上一篇 Skill 文是接力的关系：Skill 让 AI 知道做事的章法，MCP 让 AI 真的有手有脚。

## 一、 MCP 是什么

Anthropic 官方和微软的 mcp-for-beginners 课程，给 MCP 下的定义出奇一致,就两个字——**USB-C**。

> "Think of MCP like a USB-C port for AI applications."“可以将 MCP 想象成用于 AI 应用的 USB-C 端口。”

USB-C 接口在 MCP 出现之前，AI 应用接外部世界长什么样？

每接一个工具就写一套定制代码。

接 GitHub 写一套、接 Slack 写一套、接 Postgres 又写一套。

N 个 AI 应用 × M 个工具 = N×M 个对接，组合爆炸。

USB-C 出现之后呢？

AI 应用只要实现"USB-C 母口"，工具只要实现"USB-C 公口"，剩下的是同一套协议在跑。 N+M。

这就是 MCP 在解决的工程问题。

它不是新模型、不是新框架，是一个**协议**——和 HTTP、和 USB 一个层级的东西。

Host、Client、Server：三个角色主机、客户端、服务器：三个角色

MCP 协议里有三个角色，搞清楚就够了：

- **Host**：你实际在用的那个 AI 应用，比如 Claude Code、Claude Desktop、Cursor、VS Code。它是大脑，决定什么时候调用工具。
- **Client**：Host 内部的一个组件，负责按 MCP 协议和外部 Server 通信。普通用户看不见它，但它一直在工作。
- **Server**：真正提供能力的进程。可以跑在你本机（stdio 协议），也可以跑在远程（HTTP+SSE）。每个 MCP Server 暴露自己能做什么。

打个比方：Host 是你电脑、Client 是你电脑上的 USB 控制器、Server 是你插进去的那块移动硬盘。

三种原语：Tools、Resources、Prompts橙色原语：工具、资源、提示

每个 MCP Server 能往外暴露三类东西，官方叫"三原语"。

这个名词听着抽象，其实就三句话：

- **Tools（工具）**：AI 可以主动调用的动作。"帮我搜个网页""帮我跑个 SQL"。这是用得最多的一类，90% 的 MCP Server 暴露的都是 Tools。
- **Resources（资源）**：AI 可以主动读的数据。"读一下这个文件""读一下这张表的 schema"。它和 Tools 的区别是：Resources 是**只读、被动**的，像 URL；Tools 是**主动执行**的，像 RPC 调用。
- **Prompts（提示词模板）**：可复用的提示词片段。"按代码评审 SOP 给我评一下这段代码"。这一类用得最少，大多数 Server 不会暴露 Prompts。

实际上你装的大部分 MCP Server，能看到的就是一堆 Tools。

Resources 和 Prompts 是高阶玩法，刚开始你不用纠结。

MCP vs 传统 API：不是替代，是抽象层

这里有个常见的误解：MCP 出来了，是不是要替代 REST API、替代 GraphQL？

不是。

MCP 在传统 API **上面**多包了一层。

下面这层 GitHub API、Slack API 该长什么样还长什么样，没人动它。

MCP 只是把"AI 想用这些 API"这个场景标准化了：

AI 不需要再去看每家 API 的文档、自己拼参数、自己处理鉴权。

它只要会说 MCP 这门语言，剩下的事 MCP Server 帮它翻译。

所以你看 GitHub 官方提供的 MCP Server，本质就是一个**翻译器**：

上面接 MCP 协议（给 AI 用），下面调 GitHub REST API。

这一层翻译看着像是冗余，但它换来的是：所有 AI 应用对所有工具，只学一套协议。这就是协议层抽象的价值。

## 二、 应该装哪些 MCP

先说一个坑，新手很容易栽进去：Claude Code 装 MCP 的方式，和 Cline、Cursor 不一样。

Cline 和 Cursor 是丢一段 JSON 配置进去就行，UI 友好。

Claude Code 是命令行优先，要用 claude mcp add 命令注册。

我自己最开始就栽过——把一段 mcpServers 的 JSON 丢给 Claude Code 让它"帮我配置一下"，折腾了几天没搞定。

正确姿势就一行：

```bash
claude mcp add <名字> -s user -- <启动命令>
```

三个要点：

- \-s user 是作用域，意思是装到用户级别，所有项目都能用。不写 -s 默认是 local，只在当前目录生效——你换个目录就得重装一遍。新手建议无脑加 -s user。
- \-- 是分隔符，前面是 Claude Code 自己的参数，后面是真正启动 MCP Server 的命令。
- 大部分 MCP 用 npx -y 拉包跑起来，Windows 用户在 npx 前面加 cmd /c。

下面这 7 个是我自己装的最多的。

**这是我个人最常用的清单，不是 MCP Registry 的官方排名**：你照着装能覆盖 80% 的日常场景，剩下的根据自己的工作流再补。

1\. Sequential Thinking1. 顺序思维

让 Claude 在解复杂问题之前先做结构化推理的脚手架。

比如你扔给它一个调度算法、一道脑筋急转弯，它会先列出推理步骤再下结论，而不是直接给答案。

```bash
claude mcp add sequential-thinking -s user -- npx -y @modelcontextprotocol/server-sequential-thinking
```

不需要 API Key，开箱即用。

Anthropic 官方维护的包，最稳的那一类。

2\. Filesystem2. 文件系统

给 Claude 一双手去读写你硬盘上的文件。注意，要明确**授权哪些目录**给它，不是整盘开放。

```bash
claude mcp add filesystem -s user -- npx -y @modelcontextprotocol/server-filesystem ~/Documents ~/Desktop ~/Downloads ~/Projects
```

后面跟的几个路径就是授权目录，你可以按自己习惯改。

Claude Code 本身已经能读当前工作目录，这个 MCP 的价值是让它能跨目录操作：比如让它把 Downloads 里的 PDF 整理到 Documents 的某个分类下。

3\. Playwright3. 剧作家

浏览器自动化。让 Claude 帮你测网页、抓动态加载的内容、模拟点击。

和老牌的 Selenium 一脉相承，但 API 现代得多。

```bash
claude mcp add playwright -s user -- npx @playwright/mcp@latest
```

Windows 用户把命令改成 cmd /c npx @playwright/mcp@latest。

这个 MCP 第一次跑会下载 Chromium，慢一点正常。

4\. Context74. 背景7

让 Claude 在写代码时能拿到**最新版本**的库文档和示例。

痛点很真实——大模型训练数据有截止时间，你让它写 Next.js 15、React 19 的代码，它经常给你写成 13、18 的写法。

Context7 是个文档中转层，按需拉最新文档喂给 Claude。

```bash
claude mcp add context7 -s user -- npx -y @upstash/context7-mcp@latest
```

写代码时在 prompt 末尾加一句 "use context7"，它就会去拉对应库的最新文档。

5\. Chrome MCP

这个和 Playwright 不一样，它不是新开一个浏览器，而是**接管你已经登录的 Chrome**。

这意味着 Claude 操作的浏览器自带你所有的 cookie、登录态、扩展。

爬有登录墙的页面、操作 SaaS 后台，用这个比 Playwright 顺手得多。

它需要先在 Chrome 里装一个扩展，再装一个 bridge 进程，最后才注册 MCP：

```bash
# 第一步：装 bridge
npm install -g mcp-chrome-bridge

# 第二步：去 github.com/hangwin/mcp-chrome/releases 下载扩展，在 chrome://extensions 加载

# 第三步：注册 MCP（用 SSE 传输）
claude mcp add --transport sse chrome-mcp-server http://127.0.0.1:12306/mcp
```

第一次配比较折腾，配完就能一直用。

6\. Firecrawl6. 火行者

爬虫。Playwright 和 Chrome MCP 是"模拟人操作浏览器"，Firecrawl 是"直接拿网页 markdown"，专门为 AI 优化过输出。

要写需要处理大批量网页的工具，用 Firecrawl 比浏览器自动化省事。

```bash
claude mcp add firecrawl -s user -- env FIRECRAWL_API_KEY=fc-YOUR_API_KEY npx -y firecrawl-mcp
```

要 API Key，去 [firecrawl.dev](https://firecrawl.dev/) 注册，免费额度够个人玩。

把 fc-YOUR\_API\_KEY 换成你自己的。

7\. GitHub

让 Claude 能直接读写你的仓库——开 issue、读 PR、改文件、看 commit。

开发流里有 GitHub 操作的，装这个能少走很多步。

GitHub 官方在 2025 年把 MCP Server 收编了，新的实现是 Go 写的二进制，安装方式按 github/github-mcp-server 仓库 README 走。

它要一个 GitHub Personal Access Token，去 [github.com/settings/tokens](https://github.com/settings/tokens) 申请。它需要一个 GitHub 个人访问令牌，去 [github.com/settings/tokens](https://github.com/settings/tokens) 申请。

我没把具体安装命令写在这里，是因为这个仓库迭代得快，命令可能下个月就变。直接看官方 README 最准。

装完之后验证一下

```bash
claude mcp list
```

会列出所有已注册的 MCP Server 和它们的状态。

在 Claude Code 会话里输入 /mcp 还能看每个 Server 当前连得通不通。

装错了想删：

```bash
claude mcp remove <名字>
```

这就是 7 个 MCP 的基本盘。

Sequential Thinking 加强推理，Filesystem 加手，Playwright/Chrome/Firecrawl 是三种不同形态的网页交互，Context7 让代码不过时，GitHub 让仓库可控。

你日常 80% 的 AI 编程场景，这套组合都能罩住。

## 第三章 自己接一个最小可用的 MCP Server

装别人写好的 MCP 够用了，为什么还要自己写一个？

两个理由。

一是搞懂机制——你装过几十个 MCP，但不知道它内部到底是什么样，认知是空的。

自己写一遍，三原语、Tool 注册、Server 启动这套东西就再也忘不掉。

二是定制: 你工作里那些**别人不会写**的内部 API、私有数据库、自家工具链，迟早要自己接一个 MCP Server 把 AI 接进来。

下面用微软 mcp-for-beginners 课程里的 Calculator 例子走一遍。

25 行 Python，跑得起来。

准备 Python 环境

官方 MCP SDK 推荐用 uv 管理（比 pip 快很多，但用 pip 也行）：

```bash
# 推荐：用 uv
uv init mcp-calc && cd mcp-calc
uv add "mcp[cli]"

# 或者：用 pip
pip install "mcp[cli]"
```

装好之后，新建一个 [server.py](https://server.py/)。

25 行代码：Calculator MCP Server25 行代码：计算器 MCP 服务器

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator MCP Server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together and return the result."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a and return the result."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together and return the result."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    mcp.run()
```

代码读一遍，几个关键点：

- FastMCP("Calculator MCP Server") 创建一个 Server 实例，括号里的字符串是 Server 名字，Claude 会看到。
- [@mcp](https://x.com/@mcp).tool() 装饰器把一个普通函数注册成 MCP 的 Tool。函数的参数类型注解（a: float, b: float）和 docstring 会自动转换成 MCP 协议里的工具 schema 和描述——AI 就是靠这些来判断"这个工具是干什么的、要传什么参数"。
- [mcp.run](https://mcp.run/)() 用默认的 stdio 传输启动 Server。Claude Code 会通过标准输入输出和它通信。

整篇代码没有一行手写协议、没有一行 JSON-RPC、没有一行 schema 定义。FastMCP 这层封装把脏活全干了，你只需要写 Python 函数。

用 MCP Inspector 调试

注册到 Claude Code 之前，先用官方的调试工具 MCP Inspector 验证 Server 能跑。这是个网页版的调试面板，不用装：

```bash
npx @modelcontextprotocol/inspector python server.py
```

跑完会在浏览器打开一个本地面板。左边能看到你注册的四个 Tool（add/subtract/multiply/divide），点进任意一个，填上 a、b 两个参数，点击 Run，能看到返回值。

这一步如果跑通，证明你的 MCP Server 本身没问题，剩下的就是接入 Host 了。

注册到 Claude Code注册 Claude Code

接入 Claude Code 就是上一章那个命令的事：

```bash
claude mcp add calculator -s user -- python /你的绝对路径/server.py
```

注意要写**绝对路径**，相对路径在 Claude Code 启动时会找不到。

用 uv 管理环境的话，命令改成：

```bash
claude mcp add calculator -s user -- uv --directory /你的绝对路径/mcp-calc run python server.py
```

注册完 claude mcp list 确认一下，看到 calculator 在列表里就成了。

打开 Claude Code，问它"帮我算 27 乘以 41"，它会调用你刚才写的 multiply 工具，给出 1107。

那一刻你写的是 25 行 Python，但你做的事是：给一个跑在云端的大模型，接了一只它原本没有的手。

你刚才做了什么

回头看一下这套流程：你定义了 4 个 Python 函数 → FastMCP 把它们打包成符合 MCP 协议的 Tools → stdio 传输让 Claude Code 能调用 → Claude 看到工具描述决定什么时候用。

这就是所有 MCP Server 的最小骨架，再复杂的 MCP——GitHub 的、Slack 的、你公司的——本质都是这个结构，只是 Tool 更多、参数更复杂、底下调的是真实的 API 罢了。

## 第四章 把自己的 MCP Server 上架到 Registry

第三章那个 Calculator 跑在你自己机器上，只有你一个人能用。

这一章要做的事：

把它推到 **MCP Registry**——Anthropic、GitHub、Microsoft、PulseMCP 联合维护的官方中心目录。

上架之后，任何支持 Registry 的 AI 客户端都能搜到你的 Server。

> 注意：Registry 当前是 **preview 阶段**，规范和命令都可能变。下面流程基于 2025-12-11 版的 server.json schema，跟官方 [modelcontextprotocol.io/registry/quickstart](https://modelcontextprotocol.io/registry/quickstart) 走最稳。

这一章你会做的 5 件事

为了不被流程绕晕，先把全貌摆出来：

1. 把代码发到 npm
2. 装一个叫 mcp-publisher 的官方 CLI
3. 生成一份描述文件 server.json
4. 用 GitHub 账号认证身份
5. 一键上架，然后用 curl 验证

每一步对应一两条命令。下面逐个拆开。

动手前先懂三件事:

否则上面 5 个步骤你做完也不知道自己在做什么。

1\. Registry 只存元数据，不存代码

你写的代码该发 npm 还得发 npm，该发 PyPI 还得发 PyPI。

Registry 只是把"这个 Server 叫什么、底层包在哪、怎么启动、要什么环境变量"这套描述集中存起来。

打个比方：npm 是图书馆里的书，Registry 是图书馆门口的检索目录。两者是合作关系，不是替代。

2\. 名字用反向 DNS 防止抢注

你的 Server 在 Registry 里的全局唯一名长这样：

```text
io.github.你的GitHub用户名/server-name
```

或者用你自己拥有的域名：

```text
com.你公司域名/server-name
```

这套设计是为了防止冒名顶替——Registry 会通过 GitHub 登录或 DNS 验证确认你确实拥有这个前缀。

3\. 这一章跟 TypeScript 走

官方 quickstart 用 TypeScript 演示，Python 和 Rust 的 publisher 流程文档还没 TS 这么齐。

我们这一章用官方提供的样例代码 weather-server-typescript 作为底子。Python 的 Calculator 走 PyPI 也能上架，但细节得对照 package-types 文档自己摸。

准备环境

要的东西很少：

- Node.js
- npm 账号（[npmjs.com](https://npmjs.com/) 注册）
- GitHub 账号（用来认证身份）

clone 官方样例代码：

```bash
git clone --depth 1 git@github.com:modelcontextprotocol/quickstart-resources.git
cp -r quickstart-resources/weather-server-typescript .
rm -rf quickstart-resources
cd weather-server-typescript
```

下面进入正题，5 个步骤一个个走。

步骤 1 — 把代码发到 npm

**这一步做什么**：让你的 Server 代码先在公开包仓库里有个家。Registry 后面只是指向它的元数据。

改 package.json修改 package.json 文件

打开 package.json，关键改这几个字段：

```json
{
  "name": "@你的npm用户名/mcp-weather-server",
  "version": "1.0.1",
  "mcpName": "io.github.你的GitHub用户名/weather"
}
```

两个字段的意思：

- **name**：npm 上的包名。加 @用户名/ 前缀（scope）和别人区分。
- **mcpName**：你在 Registry 里的唯一标识。**用 GitHub 登录的话，必须以 \`io.github.你的GitHub用户名/\` 开头**。

发布到 npm

```bash
npm install
npm run build
npm publish --access public
```

注意一个坑

\--access public 不能漏。

npm 默认 scoped 包是私有的，漏了这个标志就发成了私有包，后面上 Registry 会因为底层包不公开而失败。

步骤 2 — 装 mcp-publisher CLI步骤 2 — 安装 mcp-publisher CLI

**这一步做什么**：装 Registry 官方的命令行工具。这是个独立的 CLI，不在 npm 里——别去 npm 找。

最省事的方式

```bash
brew install mcp-publisher
```

没装 Homebrew？拉二进制

```bash
curl -L "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher && sudo mv mcp-publisher /usr/local/bin/
```

确认装好了

```bash
mcp-publisher --help
```

能看到 init / login / logout / publish 四个子命令就对了。

步骤 3 — 生成 server.json

**这一步做什么**：写一份元数据描述文件，告诉 Registry 你这个 Server 长什么样。

一行命令生成模板

在项目根目录跑：

```bash
mcp-publisher init
```

生成的文件内容

```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.你的GitHub用户名/weather",
  "description": "An MCP server for weather information.",
  "repository": {
    "url": "https://github.com/你的GitHub用户名/mcp-weather-server",
    "source": "github"
  },
  "version": "1.0.1",
  "packages": [
    {
      "registryType": "npm",
      "identifier": "@你的npm用户名/mcp-weather-server",
      "version": "1.0.1",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

三个字段必须看懂

- **name**：必须和 package.json 里的 mcpName **完全一致**。拼错一个字符就过不了——这是最常见的坑。
- **packages\[\].registryType**：底层包发在哪。npm / pypi / oci（Docker）三选一。**packages\[\].registryType** ：底层包发在哪里。npm / pypi / oci（Docker）三选一。
- **packages\[\].transport.type**：传输方式。stdio 是本地进程（Calculator 这种），streamable-http 是远程部署的 HTTP Server。

需要环境变量怎么办

如果你的 Server 要 API Key 之类的环境变量，在packages\[\].environmentVariables 字段里声明。

下游 marketplace 帮用户安装时会引导填写。

步骤 4 — 用 GitHub 登录

**这一步做什么**：让 Registry 验证你确实是 io.github.你的GitHub用户名/ 这个命名空间的拥有者。

触发登录

```bash
mcp-publisher login github
```

会看到这样的输出

```text
Logging in with github...
To authenticate, please:
1. Go to: https://github.com/login/device
2. Enter code: ABCD-1234
3. Authorize this application
Waiting for authorization...
```

操作三步

1. 浏览器打开 [https://github.com/login/device](https://github.com/login/device)
2. 输入终端里那个验证码（比如 ABCD-1234）
3. 点 Authorize点 授权

回到终端看到 Successfully authenticated! 就成了。返回终端看到身份验证成功！ 就成了。

步骤 5 — 上架 + 验证

**这一步做什么**：把 server.json 推到 Registry，然后验证它真的进去了。

一行命令上架

```bash
mcp-publisher publish
```

看到 ✓ Successfully published 就完事了。看到✓成功发布就完事了。

验证一下

去 Registry 公开 API 搜自己：

```bash
curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.你的GitHub用户名/weather"
```

返回的 JSON 里能搜到你的 Server，说明上架成功。

容易踩的三个坑

按官方 troubleshooting 表整理，每个坑给症状、原因、解法。

坑一：Registry validation failed for package坑一：软件包注册表验证失败

- **症状**：publish 时报这个错
- **原因**：你的 npm 包 package.json 里没加 mcpName 字段，Registry 没法验证归属
- **解法**：回去补上 mcpName，npm publish 发个新版本（version 要 +1），再 mcp-publisher publish

坑二：Invalid or expired Registry JWT token坑二：无效或过期的注册表 JWT 令牌

- **症状**：上架时报 JWT 过期
- **原因**：登录有时效，过期了
- **解法**：跑一遍 mcp-publisher login github 重新登

坑三：You do not have permission to publish this server坑三：您没有权限发布此服务器

- **症状**：publish 时被拒，说没权限
- **原因**：你的 mcpName 前缀和 GitHub 登录身份不匹配。比如 GitHub 用户名是 alice，但 mcpName 写成了 io.github.bob/...
- **解法**：要么改 mcpName 前缀对上自己 GitHub 用户名，要么换 DNS 认证（用你自己拥有的域名做命名空间）

上架之后

谁会用到你的 Server

下游的 marketplace（PulseMCP、各种聚合器）会定期抓 Registry，一般每小时一次，拿到最新元数据收进自己的目录。

读者在那些 marketplace 搜索时，就能找到你的 Server，并且能一键安装到 Claude Desktop、Claude Code、Cursor、VS Code 等 Host 应用。

怎么发新版本

重复**步骤 1 → 3 → 5**：

1. npm publish 新版本（version 字段 +1）
2. 更新 server.json 的 version 字段
3. mcp-publisher publishmcp-publisher 发布

想完全自动化？

官方提供了 GitHub Actions 模板，每次 git tag 自动上架。文档在 [modelcontextprotocol.io/registry/github-actions](https://modelcontextprotocol.io/registry/github-actions)。

到这里，一个 MCP Server 从写出来 → 跑在自己机器 → 全世界都能搜到的完整闭环就走完了。

## 第五章 想继续往深里走

四章走完，主线已经齐了：

**理解 MCP、装上够用的、自己接一个最小的、推到公开目录**。

再往深里走分两个方向：要么夯实基础，要么往生产环境走。

方向一：想再夯实基础？看这两个

官方文档 — [modelcontextprotocol.io](https://modelcontextprotocol.io/)官方文档 — [modelcontextprotocol.io](https://modelcontextprotocol.io/)

新手看四个页面就够：

- docs/getting-started/intro — 概念再复习一遍
- docs/learn/architecture — 协议层细节
- docs/develop/build-server — 写 Server 的官方教程docs/develop/build-server — 写服务器的官方教程
- docs/tools/inspector — Inspector 调试工具用法docs/tools/inspector — 检查器调试工具用法

微软 mcp-for-beginners 课程

仓库地址： [github.com/microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners)。仓库地址： [github.com/microsoft/mcp-for-beginners](https://github.com/microsoft/mcp-for-beginners) 。

11 个模块，覆盖六种语言（C# / Java / JS / Python / Rust / TS）的实战代码。**有完整简中翻译**，路径在仓库的 translations/zh-CN/ 下。

想系统学的话从这个走，比看碎片文章高效。

方向二：想往生产环境走？三条路径

每条路径对应一个具体的工程需求。

看自己撞上哪个就深入哪个。

1\. 远程部署 MCP Server1.远程部署 MCP 服务器

**啥时候需要**：想让团队共享同一个 MCP 实例，而不是每人在自己机器上跑一份。

第三章的 Calculator 是 stdio 本地进程，每个用户都得本地起一份。

要部署成 HTTP+SSE 服务全员共享，看官方文档 docs/develop/connect-remote-servers。

2\. 给 Server 加 OAuth 鉴权

**啥时候需要**：你的 Server 背后有敏感数据（公司数据库、用户隐私），不想让随便哪个 AI 客户端都能调。

注意区分两件不同的 OAuth：

- **第四章那个**：Registry 用 GitHub OAuth 验你的**发布身份**
- **这里这个**：Server 自己用 OAuth 验**调用方身份**

完全是两套机制，参考 docs/tutorials/security/authorization。

3\. 用企业域名做命名空间

**啥时候需要**：你不想用 [io.github.xxx/](https://io.github.xxx/)，想用 com.你公司域名/ 上架，看起来更专业、更品牌化。

需要走 DNS 认证流程：在你域名的 DNS 里加一条 TXT 记录证明所有权。

文档在 registry/authentication。文档在注册/认证。

整个系列(可以看之前的长文)链路是：

Claude Code 是大脑，Obsidian 是它的记忆，Skill 是它的章法，MCP 是它的手脚。

四件齐了，你手里就有一个真正能干活的 AI 工作台。

**黄小木｜T11级架构师｜内容为ai辅助创作，若有侵权请指出｜持续分享 AI 信息、副业赚钱、程序员转型OPC心得｜X：**[@ai\_xiaomu](https://x.com/@ai_xiaomu)

---
