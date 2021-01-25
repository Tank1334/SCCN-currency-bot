import discord
from discord.ext import commands
import converter
TOKEN = "ODAxNTkyMjM4Mzg3MzYzODUx.YAi68g.PXA__fL8mR3Ne_Gk3qgkOKdPVI4"


bot = commands.Bot(command_prefix='s<')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')



@bot.command()
async def convert(ctx, arg):
    await ctx.send(f"{converter.convert(str(arg))}")


bot.run(TOKEN)
