
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# --- Load env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are RollGPT, an expert stock and options assistant for a Discord trading community. Be concise, actionable, and risk-aware. Use plain language.")

if not OPENAI_API_KEY or not DISCORD_BOT_TOKEN:
    raise RuntimeError("Missing OPENAI_API_KEY or DISCORD_BOT_TOKEN env vars")

# --- OpenAI client (modern SDK)
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# --- Discord bot setup
intents = discord.Intents.default()
intents.message_content = True  # Required to read user messages
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# --- Helper: call OpenAI Responses API
async def ask_openai(prompt: str) -> str:
    try:
        response = client.responses.create(
            model=OPENAI_MODEL,
            input=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_output_tokens=800,
        )
        # Extract text safely
        # New SDK returns a structured "output" list
        text_parts = []
        for item in response.output or []:
            if getattr(item, "type", None) == "message":
                for content_part in item.content or []:
                    if getattr(content_part, "type", None) == "output_text":
                        text_parts.append(content_part.text)
        text = "\n".join(text_parts).strip() or "I couldn't generate a response. Try rephrasing your question."
        return text[:1900]  # Discord limit safety
    except Exception as e:
        return f"OpenAI error: {e}"

@bot.event
async def on_ready():
    print(f"RollGPT is live! Logged in as {bot.user} (ID: {bot.user.id})")

@bot.command(name="ask")
async def ask(ctx: commands.Context, *, question: str):
    """Ask RollGPT a question. Usage: !ask <your question>"""
    # Optional: restrict to a specific channel by name
    # if ctx.channel.name not in ("ask-roll-gpt", "live-trade-alerts"):
    #     return await ctx.reply("Please use this in #ask-roll-gpt.")
    thinking = await ctx.reply("Thinking… 🧠")
    answer = await ask_openai(question)
    await thinking.edit(content=answer)

@bot.command(name="help")
async def help_cmd(ctx: commands.Context):
    msg = (
        "**RollGPT Commands**\n"
        "`!ask <question>` → Ask trading questions (options, low caps, sentiment).\n\n"
        "**Examples:**\n"
        "- `!ask Analyze TSLA options chain for this week and call out unusual OI.`\n"
        "- `!ask Scan for low-cap stocks under $10 with 2x volume and news catalysts today.`\n"
        "- `!ask What’s the current sentiment on SPY and QQQ and how does it affect NVDA?`\n"
    )
    await ctx.reply(msg)

if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
