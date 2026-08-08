"""
gemini_client.py - Google Gemini API wrapper

Learn: AI API integration, prompt engineering
"""
from google import genai
from ..config import settings


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text
