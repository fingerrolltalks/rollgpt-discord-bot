
# RollGPT Discord Bot (Railway-ready)

A minimal Discord bot that connects to OpenAI to answer trading questions.

## What's inside
- `bot.py` — the bot source code (Discord + OpenAI).
- `requirements.txt` — Python dependencies for Railway/Render.
- `Procfile` — Tells Railway/Render how to start the bot.
- `.env.example` — Example environment variables you must set in Railway/Render.

## Quick Deploy (Railway)
1) Create a new project on https://railway.app and choose **Deploy from GitHub/Zip**.
2) Upload this zip or connect a repo containing these files.
3) In **Variables**, add:
   - `OPENAI_API_KEY` = your OpenAI API key
   - `DISCORD_BOT_TOKEN` = your Discord bot token
4) In **Service** settings, set **Start Command** to: `python bot.py` (Railway may auto-detect from `Procfile`).
5) Click **Deploy**. When logs show `RollGPT is live!`, you're good.
6) In your Discord server, use `!ask <question>` in your chosen channel (e.g., #ask-roll-gpt).

## Permissions & Intents (Discord Dev Portal)
- Turn on **MESSAGE CONTENT INTENT** and **SERVER MEMBERS INTENT**.
- Invite the bot with permissions: Send Messages, Read Message History, Embed Links, Use Slash Commands (even though the demo uses a `!ask` prefix).

## Notes
- This uses the modern OpenAI SDK (`openai>=1.0`) with the Responses API.
- Keep your keys secret. Don't commit `.env` files to GitHub.
# Rebuild trigger
