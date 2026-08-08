"""
summarizer.py - Article summarization

Learn: Prompt design, batch processing, rate limiting
"""
import asyncio
from .gemini_client import GeminiClient
from ..models import Article


class ArticleSummarizer:
    def __init__(self):
        self.gemini = GeminiClient()

    async def summarize(self, article: Article) -> str:
        prompt = f"""Summarize this article in 2-3 sentences.
Focus on key insights and practical implications.

Title: {article.title}
Description: {article.description}
Source: {article.source}

Summary:"""
        return await self.gemini.generate(prompt)

    async def batch_summarize(self, articles: list[Article]) -> list[Article]:
        for i, article in enumerate(articles):
            if not article.summary:
                try:
                    article.summary = await self.summarize(article)
                    print(f"  [{i+1}/{len(articles)}] Summarized: {article.title[:40]}...")
                except Exception as e:
                    print(f"  [{i+1}/{len(articles)}] Error: {e}")
                    article.summary = article.description or "No summary available"
                # Rate limit: wait between calls
                if i < len(articles) - 1:
                    await asyncio.sleep(2)
        return articles
