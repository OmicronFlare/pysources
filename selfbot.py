### Made by omicron.nn

import discord
from discord.ext import commands

token = "" # Your token
prefix = "." # Change to wtv u want
intents = discord.Intents.all()

bot = commands.Bot(command_prefix={prefix}, intents=intents, self_bot=True)

@bot.event
async def on_ready():
    print(f"{bot.user.display_name} Connected ")


@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command
async def credits(ctx):
    await ctx.send("```[Creator] omicron.nn\n [Discord] https://discord.gg/5mJCYkjzFn```")

@bot.command()
async def invite(ctx):
    await ctx.send("discord.gg/5mJCYkjzFn")

@bot.command()
async def website(ctx):
    await ctx.send("@everyone | discord.gg/5mJCYkjzFn | https://omicrontools.netlify.app/ | Join")

bot.run(token, bot=False)


# this code will be in the repo : https://github.com/OmicronFlare/selfbotsrc
