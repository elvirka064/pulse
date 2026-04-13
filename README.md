# pulse

Telegram bot starter for Railway deployment.

## Local run

1. Create a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Export `BOT_TOKEN` or create `.env`.
4. Start bot:

```bash
python bot.py
```

## Railway deploy

1. Connect this repository in Railway.
2. Add `BOT_TOKEN` in service variables.
3. Deploy. Railway starts the worker from `Procfile`.
