"""
deduplicator.py - Remove duplicate articles

Learn: File I/O, JSON persistence, hashing
"""
import json
from pathlib import Path
from ..models import Article
from ..config import settings


class Deduplicator:
    def __init__(self):
        self.seen_file = settings.data_dir / "seen_articles.json"
        self.seen_file.parent.mkdir(parents=True, exist_ok=True)
        self._load()

    def _load(self):
        if self.seen_file.exists():
            self.seen: set[str] = set(json.loads(self.seen_file.read_text()))
        else:
            self.seen = set()

    def _save(self):
        self.seen_file.write_text(json.dumps(list(self.seen)))

    def is_new(self, article: Article) -> bool:
        return article.hash_id not in self.seen

    def mark_seen(self, articles: list[Article]):
        for article in articles:
            self.seen.add(article.hash_id)
        self._save()

    def filter_new(self, articles: list[Article]) -> list[Article]:
        new_articles = [a for a in articles if self.is_new(a)]
        self.mark_seen(new_articles)
        return new_articles
