"""
youtube_collector.py - YouTube channel monitor

Learn: YouTube Data API, channel IDs, video search
"""
import httpx
from .base import BaseCollector
from ..models import Article, Category
from ..config import settings


class YouTubeCollector(BaseCollector):
    def __init__(self):
        super().__init__("youtube")
        self.channels = {
            "Two Minute Papers": "UCbfYPyI0KSyYCidkZ21pVmw",
            "Yannic Kilcher": "UCZHmQk67mSJGF_C7agsg7RQ",
            "AI Jason": "UCNIrJmySFLlKf73EhS9xFqw",
        }

    async def collect(self) -> list[Article]:
        articles = []
        async with httpx.AsyncClient() as client:
            for channel_name, channel_id in self.channels.items():
                try:
                    response = await client.get(
                        "https://www.googleapis.com/youtube/v3/search",
                        params={
                            "part": "snippet",
                            "channelId": channel_id,
                            "maxResults": 5,
                            "order": "date",
                            "type": "video",
                            "key": settings.youtube_api_key,
                        },
                        timeout=10,
                    )
                    data = response.json()
                    for item in data.get("items", []):
                        snippet = item["snippet"]
                        articles.append(Article(
                            title=snippet["title"],
                            url=f"https://youtube.com/watch?v={item['id']['videoId']}",
                            description=snippet.get("description", "")[:200],
                            source="youtube",
                            category=Category.TUTORIAL,
                        ))
                except Exception as e:
                    print(f"Error fetching YouTube: {e}")
        return articles
