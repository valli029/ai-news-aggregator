"""
config.py - Environment variables and settings

Learn: Pydantic BaseSettings, .env files
"""
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    # API Keys
    gemini_api_key: str = ""
    github_pat: str = ""
    youtube_api_key: str = ""
    news_api_key: str = ""

    # Telegram
    telegram_bot_token: str = ""
    telegram_chat_id: str = ""

    # Gmail
    gmail_address: str = ""
    gmail_password: str = ""

    # App Config
    run_hour: int = 8
    run_minute: int = 0
    data_dir: Path = Path("data")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
