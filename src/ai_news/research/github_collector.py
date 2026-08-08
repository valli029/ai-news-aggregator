"""
github_collector.py - GitHub trending repos

Learn: REST APIs, authentication headers, pagination
"""
import httpx
from .base import BaseCollector
from ..models import Article, Category
from ..config import settings


class GitHubCollector(BaseCollector):
    def __init__(self):
        super().__init__("github")
        self.search_queries = [
            "claude-code extension",
            "cursor plugin",
            "ai coding assistant",
            "llm tool",
            "agent framework",
        ]

    async def collect(self) -> list[Article]:
        articles = []
        headers = {"Authorization": f"token {settings.github_pat}"}

        async with httpx.AsyncClient() as client:
            for query in self.search_queries:
                try:
                    response = await client.get(
                        "https://api.github.com/search/repositories",
                        params={"q": query, "sort": "stars", "per_page": 5},
                        headers=headers,
                        timeout=10,
                    )
                    data = response.json()
                    for repo in data.get("items", []):
                        articles.append(Article(
                            title=repo["full_name"],
                            url=repo["html_url"],
                            description=repo.get("description", "")[:200],
                            source="github",
                            category=Category.TOOL,
                            tags=[topic for topic in repo.get("topics", [])],
                        ))
                except Exception as e:
                    print(f"Error searching GitHub: {e}")
        return articles
