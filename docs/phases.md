# Implementation Phases

## Phase 1: Foundation (Day 1)

- [x] Set up project structure with uv
- [x] Create FastAPI skeleton (`main.py`)
- [x] Configure environment variables (`config.py`)
- [x] Create Pydantic models (`models.py`)

## Phase 2: Research Layer (Day 2)

- [x] Implement base collector class (`research/base.py`)
- [x] Implement RSS collector (`research/rss_collector.py`)
  - Hacker News
  - Reddit r/MachineLearning
  - arXiv cs.AI
- [x] Implement GitHub collector (`research/github_collector.py`)
  - Search: "claude-code extension"
  - Search: "cursor plugin"
  - Search: "ai coding assistant"
- [x] Implement YouTube collector (`research/youtube_collector.py`)
  - Two Minute Papers
  - Yannic Kilcher
  - AI Jason
- [x] Implement NewsAPI collector (`research/newsapi_collector.py`)

## Phase 3: Processing Layer (Day 3)

- [x] Set up Gemini API client (`processing/gemini_client.py`)
- [x] Build summarizer with prompt templates (`processing/summarizer.py`)
- [x] Build categorizer for article tagging (`processing/categorizer.py`)
- [x] Build deduplicator with JSON persistence (`processing/deduplicator.py`)
- [x] Add rate limiting (2s delay between API calls)

## Phase 4: Delivery Layer (Day 4)

- [x] Set up Telegram bot via BotFather
- [x] Implement Telegram message formatter (`delivery/telegram_bot.py`)
- [x] Set up Gmail SMTP with app password
- [x] Create HTML email template (`templates/digest_email.html`)
- [x] Implement email sender (`delivery/email_sender.py`)

## Phase 5: Scheduler + Polish (Day 5)

- [ ] Set up APScheduler for daily 8am run (`scheduler/jobs.py`)
- [ ] Add error handling + logging
- [ ] Write comprehensive README
- [ ] Add tests for each layer
- [ ] Test full pipeline end-to-end

## API Keys Needed (All Free)

| Service | Free Limit |
|---------|------------|
| Google Gemini | 1500 req/day |
| GitHub API | 60 req/hr |
| YouTube API | 10k units/day |
| NewsAPI | 100 req/day |
| Telegram Bot | Unlimited |
| Gmail SMTP | Unlimited |

## Data Sources

### RSS Feeds
- `https://hnrss.org/newest?q=AI+OR+LLM+OR+agent`
- `https://www.reddit.com/r/MachineLearning/.rss`
- `http://export.arxiv.org/rss/cs.AI`

### GitHub Search Queries
- `claude-code extension`
- `cursor plugin`
- `ai coding assistant`
- `llm tool`
- `agent framework`

### YouTube Channels
- Two Minute Papers
- Yannic Kilcher
- AI Jason
