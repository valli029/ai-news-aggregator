"""
base.py - Base collector class

Learn: Abstract base classes, inheritance
"""
from abc import ABC, abstractmethod
from ..models import Article


class BaseCollector(ABC):
    """Base class for all research collectors."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    async def collect(self) -> list[Article]:
        """Collect articles from the source."""
        pass

    async def health_check(self) -> bool:
        """Check if the source is available."""
        return True
