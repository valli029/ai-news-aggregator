"""
main.py - FastAPI application

Learn: FastAPI basics, routes, async endpoints
"""
from fastapi import FastAPI
from .models import Digest
from .research import RSSCollector, GitHubCollector, YouTubeCollector, NewsAPICollector
from .processing import ArticleSummarizer, ArticleCategorizer, Deduplicator
from .delivery import TelegramSender, EmailSender

app = FastAPI(title="AI News Aggregator")

collectors = [
    RSSCollector(),
    GitHubCollector(),
    YouTubeCollector(),
    NewsAPICollector(),
]

deduplicator = Deduplicator()
summarizer = ArticleSummarizer()
categorizer = ArticleCategorizer()
telegram_sender = TelegramSender()
email_sender = EmailSender()


@app.get("/")
async def root():
    return {"status": "AI News Aggregator is running"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/trigger")
async def trigger():
    digest = await run_pipeline()
    return {
        "status": "completed",
        "total_collected": digest.total_count,
        "articles": [
            {
                "title": a.title,
                "url": a.url,
                "source": a.source,
                "category": a.category.value,
                "summary": a.summary,
            }
            for a in digest.articles
        ],
    }


async def run_pipeline() -> Digest:
    all_articles = []
    for collector in collectors:
        try:
            articles = await collector.collect()
            all_articles.extend(articles)
            print(f"[{collector.name}] Collected {len(articles)} articles")
        except Exception as e:
            print(f"[{collector.name}] Error: {e}")

    new_articles = deduplicator.filter_new(all_articles)
    print(f"[dedup] {len(all_articles)} total, {len(new_articles)} new")

    summarized = await summarizer.batch_summarize(new_articles)
    print(f"[summarize] Summarized {len(summarized)} articles")

    categorized = await categorizer.batch_categorize(summarized)
    categorized.sort(key=lambda x: x.importance, reverse=True)
    print(f"[categorize] Categorized {len(categorized)} articles")

    digest = Digest(articles=categorized, total_count=len(categorized))

    # Send via Telegram
    try:
        await telegram_sender.send(digest)
        print("[telegram] Digest sent")
    except Exception as e:
        print(f"[telegram] Error: {e}")

    # Send via Email
    try:
        email_sender.send(digest)
        print("[email] Digest sent")
    except Exception as e:
        print(f"[email] Error: {e}")

    return digest
