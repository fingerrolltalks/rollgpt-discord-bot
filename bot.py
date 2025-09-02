import os
import sys
import discord
from discord.ext import commands
from openai import OpenAI

# Debug: print what env variables are available (masking sensitive info)
print("DEBUG: Checking environment variables...", flush=True)
for key in ["OPENAI_API_KEY", "DISCORD_BOT_TOKEN", "OPENAI_MODEL", "SYSTEM_PROMPT", "PYTHON_VERSION"]:
    val = os.environ.get(key)
    print(f"{key}: {'SET' if val else 'NOT SET'} (length: {len(val) if val else 0})", flush=True)

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o")
SYSTEM_PROMPT = os.environ.get(
    "SYSTEM_PROMPT",
    "You are RollGPT, an expert stock and options assistant. Be concise, actionable, and risk-aware."
)

if not OPENAI_API_KEY or not DISCORD_BOT_TOKEN:
    sys.exit("ERROR: Missing OPENAI_API_KEY or DISCORD_BOT_TOKEN env vars")

client = OpenAI(api_key=OPENAI_API_KEY)
