import discord
from discord.ext import commands
import converter
TOKEN = "{bot token}"


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')



@bot.command()
async def test(ctx, arg):
    await ctx.send(f"{converter.convert(str(arg))}")


bot.run(TOKEN)
