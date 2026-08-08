"""
categorizer.py - Article categorization

Learn: Classification prompts, enum mapping, rate limiting
"""
import asyncio
from .gemini_client import GeminiClient
from ..models import Article, Category


class ArticleCategorizer:
    def __init__(self):
        self.gemini = GeminiClient()

    async def categorize(self, article: Article) -> Article:
        prompt = f"""Categorize this article into exactly ONE category:
- llm: Large language models, GPT, Claude, Gemini
- agent: AI agents, autonomous systems, tool use
- tool: Developer tools, IDE plugins, utilities
- paper: Research papers, academic work
- tutorial: How-to guides, educational content
- industry: Business news, company updates

Title: {article.title}
Description: {article.description}
Summary: {article.summary}

Category:"""
        result = await self.gemini.generate(prompt)
        try:
            article.category = Category(result.strip().lower())
        except ValueError:
            article.category = Category.OTHER
        return article

    async def batch_categorize(self, articles: list[Article]) -> list[Article]:
        for i, article in enumerate(articles):
            try:
                article = await self.categorize(article)
                print(f"  [{i+1}/{len(articles)}] Categorized: {article.title[:40]}... → {article.category.value}")
            except Exception as e:
                print(f"  [{i+1}/{len(articles)}] Error: {e}")
                article.category = Category.OTHER
            if i < len(articles) - 1:
                await asyncio.sleep(2)
        return articles
