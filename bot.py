import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Slash sync failed: {e}")

# Slash command
@bot.tree.command(name="greet", description="Say hello!")
async def greet(interaction: discord.Interaction):
    await interaction.response.send_message("Hello! 👋 This is a slash command.")

def run_bot():
    bot.run(TOKEN)
