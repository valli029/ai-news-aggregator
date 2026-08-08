"""
main.py - FastAPI application

Learn: FastAPI basics, routes, async endpoints
"""
from fastapi import FastAPI
from .models import Digest
from .research import RSSCollector, GitHubCollector, YouTubeCollector, NewsAPICollector

app = FastAPI(title="AI News Aggregator")

collectors = [
    RSSCollector(),
    GitHubCollector(),
    YouTubeCollector(),
    NewsAPICollector(),
]


@app.get("/")
async def root():
    return {"status": "AI News Aggregator is running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/trigger")
async def trigger():
    digest = await run_pipeline()
    return {"status": "completed", "articles": len(digest.articles)}


async def run_pipeline() -> Digest:
    all_articles = []
    for collector in collectors:
        try:
            articles = await collector.collect()
            all_articles.extend(articles)
            print(f"[{collector.name}] Collected {len(articles)} articles")
        except Exception as e:
            print(f"[{collector.name}] Error: {e}")

    return Digest(articles=all_articles, total_count=len(all_articles))
