import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
load_dotenv()

prefixes = ["+"]
bot = commands.Bot(command_prefix=prefixes, intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True, override_type=True)
@bot.event
async def on_ready():
    channel = bot.get_channel(881990844226367531)
    await channel.send('i am online')
    await bot.change_presence(activity=discord.Streaming(name='put status here', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.event
async def on_disconnect():
    channel = bot.get_channel(881990844226367531)
    await channel.send('i am going offline')

@slash.slash(name="bruh", description="bruh moment")
async def bruh(ctx: SlashContext):
    await ctx.send(content="bruh")

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            print(f"loaded: {filename}")
            bot.load_extension(f'cogs.{filename[:-3]}')

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)