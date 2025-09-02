import os
import discord
from discord.ext import commands
from openai import OpenAI

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o")
SYSTEM_PROMPT = os.environ.get(
    "SYSTEM_PROMPT",
    "You are RollGPT, an expert stock and options assistant. Be concise, actionable, and risk-aware."
)

if not OPENAI_API_KEY or not DISCORD_BOT_TOKEN:
    raise RuntimeError("Missing OPENAI_API_KEY or DISCORD_BOT_TOKEN env vars")
