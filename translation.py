from discord.ext import commands
from googletrans import Translator
import discord

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
translator = Translator()

@bot.event
async def on_ready():
    print("Bot is ready.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    try:
        detected_lang = translator.detect(message.content).lang
        if detected_lang != 'tr':  # If language is not turkish and you can change language
            translated_message = translator.translate(message.content, dest='tr').text
            await message.channel.send(translated_message)

    except Exception as e:
        error_msg = await message.channel.send(str(e))
        await error_msg.delete(delay=10)   # Delete the error message after 10 seconds

# Run bot
bot.run('your-discord-token')  # Replace 'your_token_here' with your actual Discord bot token

