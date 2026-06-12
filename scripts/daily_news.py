import os
import re
import datetime
import hashlib
from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup
from openai import OpenAI


# ========== 基础配置 ==========

RSS_FEEDS = [
    {
        "name": "Reuters World",
        "url": "https://feeds.reuters.com/Reuters/worldNews"
    },
    {
        "name": "BBC World",
        "url": "https://feeds.bbci.co.uk/news/world/rss.xml"
    },
    {
        "name": "Nature News",
        "url": "https://www.nature.com/nature.rss"
    }
]

OUTPUT_DIR = Path("EnglishReading")
OUTPUT_DIR.mkdir(exist_ok=True)

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com"
)


# ========== 工具函数 ==========

def clean_filename(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]", "", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:80]


def get_today_str():
    return datetime.datetime.now().strftime("%Y-%m-%d")


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


def ask_deepseek(title: str, source: str, article: str) -> str:
    """
    调用 DeepSeek，把英文文章整理为中文学习笔记。
    """

    # 防止文章太长导致成本过高
    article = article[:8000]

    prompt = f"""
你是一名英文报刊阅读导师。请基于下面这篇英文文章，生成适合中文学习者的 Obsidian Markdown 笔记。

要求：
1. 保留英文标题。
2. 给出中文标题。
3. 给出 150 字以内中文摘要。
4. 分析文章核心观点。
5. 提取 10 个重点英文单词：英文、中文释义、原文语境、例句。
6. 提取 5 个地道表达：英文表达、中文解释、如何仿写。
7. 分析 3 个长难句。
8. 给出背景知识。
9. 最后给出 3 个英文仿写练习。
10. 全部使用 Markdown 格式。

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
                "content": "你是严谨的英语阅读导师，擅长报刊英语、新闻背景解释和中文教学。"
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
    if not DEEPSEEK_API_KEY:
        raise RuntimeError("DEEPSEEK_API_KEY is not set.")

    article = select_article()

    today = get_today_str()
    safe_title = clean_filename(article["title"])
    filename = f"{today}-{safe_title}.md"
    output_path = OUTPUT_DIR / filename

    if output_path.exists():
        print(f"File already exists: {output_path}")
        return

    ai_note = ask_deepseek(
        title=article["title"],
        source=article["source"],
        article=article["text"]
    )

    markdown = build_markdown(article, ai_note)

    output_path.write_text(markdown, encoding="utf-8")

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
