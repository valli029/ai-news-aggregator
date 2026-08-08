# AI News Aggregator

An autonomous agent that researches new AI technologies, tools, and frameworks daily, then delivers a curated digest to your email and Telegram.

## What It Does

- **Researches** AI news from 5+ sources (Hacker News, Reddit, GitHub, YouTube, NewsAPI)
- **Discovers** new tools built on AI platforms (Claude Code extensions, Cursor plugins, agent frameworks)
- **Summarizes** articles using Google Gemini (free tier)
- **Categorizes** content (LLM, Agent, Tool, Paper, Tutorial, Industry)
- **Deduplicates** across runs using persistent storage
- **Delivers** daily digest via Telegram and Gmail

## Tech Stack

| Component | Tool |
|-----------|------|
| Framework | FastAPI |
| AI Summarization | Google Gemini |
| RSS Parsing | feedparser |
| GitHub | GitHub API |
| YouTube | YouTube Data API v3 |
| News | NewsAPI |
| Telegram | python-telegram-bot |
| Email | Gmail SMTP |
| Scheduler | APScheduler |

## Project Structure

```
ai-news/
├── src/ai_news/
│   ├── main.py                    # FastAPI app
│   ├── config.py                  # Environment settings
│   ├── models.py                  # Pydantic models
│   ├── research/                  # Data collectors
│   ├── processing/                # Summarization & categorization
│   ├── delivery/                  # Email & Telegram
│   └── scheduler/                 # Background tasks
├── templates/                     # HTML email templates
├── data/                          # Persistent storage
├── tests/                         # Test suite
├── docs/                          # Documentation
└── run.py                         # Entry point
```

## Quick Start

### 1. Install Dependencies

```bash
cd ai-news
uv sync
```

### 2. Get API Keys (All Free)

| Service | Get Key From |
|---------|-------------|
| Gemini | [aistudio.google.com](https://aistudio.google.com) |
| GitHub | Settings > Developer settings > Tokens |
| YouTube | Google Cloud Console |
| NewsAPI | [newsapi.org](https://newsapi.org) |
| Telegram | @BotFather on Telegram |
| Gmail | Google Account > App Passwords |

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 4. Run the Server

```bash
uv run uvicorn src.ai_news.main:app --reload
```

Open http://localhost:8000/docs for Swagger UI.

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Detailed health status |
| POST | `/trigger` | Manual pipeline trigger |

## Development

See [docs/phases.md](docs/phases.md) for the implementation roadmap.

## License

MIT
