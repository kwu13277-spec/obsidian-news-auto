# Obsidian News Auto

每日自动抓取英文新闻 RSS → DeepSeek 翻译/总结 → 生成 Obsidian Markdown 笔记 → 推送到 GitHub。

## 工作流程

```text
每天 UTC 00:00 (北京时间 08:00)
↓
GitHub Actions 自动运行
↓
读取英文新闻 RSS
↓
抓取其中一篇文章
↓
调用 DeepSeek 翻译、总结、提取单词
↓
生成 Markdown 文件
↓
自动提交到 GitHub 仓库
↓
手机端 Obsidian 同步后看到当天文章
```

## 目录结构

```
obsidian-news-auto/
├── EnglishReading/          # 每天自动生成的英文阅读笔记
├── scripts/
│   └── daily_news.py        # 抓新闻、调用 DeepSeek、生成 Markdown
├── .github/
│   └── workflows/
│       └── daily-news.yml   # GitHub 定时任务配置
├── requirements.txt         # Python 依赖
└── README.md
```

## 配置步骤

1. 在 GitHub 仓库 Settings → Secrets and variables → Actions 中添加 `DEEPSEEK_API_KEY`
2. 手动触发一次 Workflow 测试：
   - Actions → Daily English News → Run workflow
3. 确认 EnglishReading/ 下生成了 Markdown 文件

## 手机端 Obsidian 同步

推荐使用 Obsidian Git 插件：
- 安装 community plugin: Obsidian Git
- 配置 GitHub 仓库地址
- 设置自动同步间隔（建议 60 分钟）

## RSS 数据源

- BBC Future
- BBC Travel
- Smithsonian Science
- Smithsonian History
- Smithsonian Innovation
- The Conversation Education
- The Conversation Environment
- The Conversation Technology
- ScienceDaily Science
- ScienceDaily Environment
