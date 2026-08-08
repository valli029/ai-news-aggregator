"""
rss_collector.py - RSS feed collector

Learn: HTTP clients (httpx), async/await, feed parsing
"""
import feedparser
import httpx
from .base import BaseCollector
from ..models import Article


class RSSCollector(BaseCollector):
    def __init__(self):
        super().__init__("rss")
        self.feeds = {
            "hacker_news": "https://hnrss.org/newest?q=AI+OR+LLM+OR+agent",
            "reddit_ml": "https://www.reddit.com/r/MachineLearning/.rss",
            "arxiv_ai": "http://export.arxiv.org/rss/cs.AI",
        }

    async def collect(self) -> list[Article]:
        articles = []
        async with httpx.AsyncClient() as client:
            for source, url in self.feeds.items():
                try:
                    response = await client.get(url, timeout=10)
                    feed = feedparser.parse(response.text)
                    for entry in feed.entries[:10]:
                        articles.append(Article(
                            title=entry.get("title", ""),
                            url=entry.get("link", ""),
                            description=entry.get("summary", "")[:200],
                            source=source,
                        ))
                except Exception as e:
                    print(f"Error fetching {source}: {e}")
        return articles
