import discord
from discord.ext import commands
import converter as api
TOKEN = "ODAxNTkyMjM4Mzg3MzYzODUx.YAi68g.28JvvfLDVtOypMOYBr1jxK4nXSM"


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')



@bot.command()
async def test(ctx, arg):
    await ctx.send(f"The value of SCCN to {arg} is {api.api(str(arg))}")


bot.run(TOKEN)
