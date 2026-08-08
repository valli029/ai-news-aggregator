"""
models.py - Data models

Learn: Pydantic models, data validation, enums
"""
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


class Category(str, Enum):
    LLM = "llm"
    AGENT = "agent"
    TOOL = "tool"
    PAPER = "paper"
    TUTORIAL = "tutorial"
    INDUSTRY = "industry"
    OTHER = "other"


class Article(BaseModel):
    title: str
    url: str
    description: str = ""
    source: str
    category: Category = Category.OTHER
    importance: int = Field(default=0, ge=0, le=5)
    summary: str = ""
    published_at: datetime | None = None
    collected_at: datetime = Field(default_factory=datetime.now)
    tags: list[str] = []

    @property
    def hash_id(self) -> str:
        import hashlib
        return hashlib.md5(self.url.encode()).hexdigest()


class Digest(BaseModel):
    articles: list[Article] = []
    generated_at: datetime = Field(default_factory=datetime.now)
    total_count: int = 0
