import os
import re
import datetime
from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup
from openai import OpenAI


# ========== 基础配置 ==========

RSS_FEEDS = [
    {
        "name": "BBC Future",
        "url": "https://www.bbc.com/future/feed.rss"
    },
    {
        "name": "BBC Travel",
        "url": "https://www.bbc.com/travel/feed.rss"
    },
    {
        "name": "Smithsonian Science",
        "url": "https://www.smithsonianmag.com/rss/science-nature/"
    },
    {
        "name": "Smithsonian History",
        "url": "https://www.smithsonianmag.com/rss/history/"
    },
    {
        "name": "Smithsonian Innovation",
        "url": "https://www.smithsonianmag.com/rss/innovation/"
    },
    {
        "name": "The Conversation Education",
        "url": "https://theconversation.com/us/education/articles.atom"
    },
    {
        "name": "The Conversation Environment",
        "url": "https://theconversation.com/us/environment/articles.atom"
    },
    {
        "name": "The Conversation Technology",
        "url": "https://theconversation.com/us/technology/articles.atom"
    },
    {
        "name": "ScienceDaily Science",
        "url": "https://www.sciencedaily.com/rss/top/science.xml"
    },
    {
        "name": "ScienceDaily Environment",
        "url": "https://www.sciencedaily.com/rss/top/environment.xml"
    }
]

OUTPUT_DIR = Path("EnglishReading")
OUTPUT_DIR.mkdir(exist_ok=True)

# ========== 工具函数 ==========

def get_deepseek_client():
    """延迟初始化 DeepSeek 客户端，确保 API Key 已设置"""
    api_key = os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "DeepSeek API Key 未设置。请在 GitHub 仓库 Settings → Secrets and variables → Actions 中 "
            "添加 DEEPSEEK_API_KEY secret。"
        )
    return OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

def clean_filename(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:80]


def get_today_str():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def get_output_path(title: str) -> Path:
    safe_title = clean_filename(title)
    return OUTPUT_DIR / f"{get_today_str()}-{safe_title}.md"


def extract_text_from_html(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
        tag.decompose()

    paragraphs = soup.find_all("p")
    texts = []

    for p in paragraphs:
        text = p.get_text(" ", strip=True)
        if len(text) > 40:
            texts.append(text)

    content = "\n\n".join(texts)
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip()


def fetch_article_text(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        resp = requests.get(url, headers=headers, timeout=20)
        resp.raise_for_status()
        text = extract_text_from_html(resp.text)
        return text
    except Exception as e:
        print(f"Failed to fetch article: {e}")
        return ""


def select_article():
    """
    从 RSS 中选择第一篇能抓到正文的文章。
    """

    for feed in RSS_FEEDS:
        print(f"Checking feed: {feed['name']}")
        parsed = feedparser.parse(feed["url"])

        for entry in parsed.entries[:5]:
            title = entry.get("title", "Untitled")
            link = entry.get("link", "")
            summary = entry.get("summary", "")

            if not link:
                continue

            output_path = get_output_path(title)
            if output_path.exists():
                print(f"Skipping existing article: {output_path}")
                continue

            article_text = fetch_article_text(link)

            if len(article_text) < 500:
                article_text = BeautifulSoup(summary, "html.parser").get_text(" ", strip=True)

            if len(article_text) >= 200:
                return {
                    "source": feed["name"],
                    "title": title,
                    "link": link,
                    "text": article_text
                }

    raise RuntimeError("No valid article found from RSS feeds.")


def ask_deepseek(client: OpenAI, title: str, source: str, article: str) -> str:
    """
    调用 DeepSeek，把英文文章整理为中文学习笔记。
    """

    # 不限长度，完整文章发送给 DeepSeek

    prompt = f"""
你是一名面向雅思阅读备考者的英文精读导师。请基于下面这篇英文文章，生成适合中文学习者的 Obsidian Markdown 精读笔记。

任务目标：
1. 保留英文标题，并给出中文标题。
2. 不需要整篇文章摘要，不需要新闻立场分析。
3. 按英文原文的自然段逐段处理，不要合并多个自然段。
4. 每一段都必须包含：英文原文、中文翻译、长难句语法解构、重点词汇/短语。
5. 重点词汇/短语优先选择雅思阅读考试中常见、可迁移、值得积累的表达。
6. 全部使用 Markdown 格式，结构清晰，便于 Obsidian 阅读。
7. 在全文逐段精读结束后，增加一个“辩证观点”收尾模块，帮助学习者从多个角度理解文章议题。

每段请严格使用以下格式：

## Paragraph 1

### English
保留该段英文原文。

### 中文翻译
给出该段自然、准确的中文翻译。

### 长难句语法解构
- 句子：摘录该段中最值得分析的长难句；如果该段没有明显长难句，请选择信息密度最高的一句。
- 主干：指出句子主语、谓语、宾语/表语等核心结构。
- 修饰成分：解释从句、非谓语、介词短语、插入语、并列结构等。
- 理解难点：说明中文学习者容易卡住的地方。
- 参考译法：给出该句的中文翻译。

### 重点词汇/短语
请另起一行提取该段中的重点英文单词或短语。每段提取 3-6 个，使用表格：

| 单词/短语 | 音标 | 中文释义 | 原文语句 | 例句 |
|---|---|---|---|---|

词汇要求：
- 音标使用 IPA；如果不确定音标，请标注“音标待查”，不要编造。
- 原文语句必须来自该段原文。
- 例句要适合雅思写作或阅读语境，避免敏感政治、犯罪、灾难类内容。
- 中文释义要结合原文语境，不只给字典义。

然后继续处理 Paragraph 2、Paragraph 3，直到文章结束。

全文逐段处理完后，请增加以下收尾模块：

## 辩证观点

### 文章核心议题
用 1-2 句话概括文章讨论的核心问题。

### 支持观点
- 提炼文章中支持该议题的一方观点。
- 说明该观点的理由或证据。

### 反向观点
- 提出与文章观点形成张力的另一种合理看法。
- 说明这种看法可能成立的原因。

### 平衡判断
用中立、审慎的语言给出综合判断，避免绝对化表达。

### 雅思写作可借鉴表达
提取 3-5 个可用于雅思写作 Task 2 的英文表达，并给出中文含义。

文章来源：{source}
英文标题：{title}

英文原文：
{article}
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": "你是严谨的雅思阅读精读导师，擅长逐段翻译、长难句语法拆解、IPA 音标标注和考试高频词汇讲解。"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def build_markdown(article_info: dict, ai_note: str) -> str:
    today = get_today_str()

    md = f"""# {article_info['title']}

> Date: {today}
> Source: {article_info['source']}
> Link: {article_info['link']}

---

# 原文

{article_info['text']}

---

# Copilot / DeepSeek 学习笔记

{ai_note}
"""

    return md


def main():
    client = get_deepseek_client()

    article = select_article()

    output_path = get_output_path(article["title"])

    if output_path.exists():
        print(f"File already exists: {output_path}")
        return

    ai_note = ask_deepseek(
        client=client,
        title=article["title"],
        source=article["source"],
        article=article["text"]
    )

    markdown = build_markdown(article, ai_note)

    output_path.write_text(markdown, encoding="utf-8")

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
