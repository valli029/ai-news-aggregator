"""
telegram_bot.py - Telegram message sender

Learn: Bot API, HTTP requests, message formatting
"""
import httpx
from ..models import Digest
from ..config import settings


class TelegramSender:
    def __init__(self):
        self.api_url = f"https://api.telegram.org/bot{settings.telegram_bot_token}"

    async def send(self, digest: Digest):
        message = self._format_message(digest)
        async with httpx.AsyncClient() as client:
            await client.post(
                f"{self.api_url}/sendMessage",
                json={
                    "chat_id": settings.telegram_chat_id,
                    "text": message,
                    "parse_mode": "Markdown",
                },
            )

    def _format_message(self, digest: Digest) -> str:
        lines = [f"*AI News Digest* - {digest.generated_at.strftime('%B %d, %Y')}\n"]

        for article in digest.articles[:10]:
            stars = "⭐" * article.importance if article.importance > 0 else ""
            lines.append(f"*{article.title}*")
            lines.append(f"{stars} `{article.category.value}` | [{article.source}]({article.url})\n")
            if article.summary:
                lines.append(f"{article.summary[:100]}...\n")

        return "\n".join(lines)
