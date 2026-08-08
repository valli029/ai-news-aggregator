"""
newsapi_collector.py - NewsAPI.org collector

Learn: Query parameters, date filtering, API keys
"""
import httpx
from datetime import datetime, timedelta
from .base import BaseCollector
from ..models import Article, Category
from ..config import settings


class NewsAPICollector(BaseCollector):
    def __init__(self):
        super().__init__("newsapi")

    async def collect(self) -> list[Article]:
        articles = []
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    "https://newsapi.org/v2/everything",
                    params={
                        "q": "AI OR LLM OR agent",
                        "apiKey": settings.news_api_key,
                        "language": "en",
                        "sortBy": "publishedAt",
                        "pageSize": 10,
                        "from": (datetime.now() - timedelta(days=1)).isoformat(),
                    },
                    timeout=10,
                )
                data = response.json()
                for item in data.get("articles", []):
                    articles.append(Article(
                        title=item["title"],
                        url=item["url"],
                        description=item.get("description", "")[:200],
                        source="newsapi",
                        category=Category.INDUSTRY,
                        published_at=datetime.fromisoformat(
                            item["publishedAt"].replace("Z", "+00:00")
                        ),
                    ))
            except Exception as e:
                print(f"Error fetching NewsAPI: {e}")
        return articles
