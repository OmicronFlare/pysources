
# Made by omicron.nn

import discord
from discord.ext import commands

token = "your token" # Change this to your discord token
prefix = "+" # you can change this prefix if you want too.

bot = commands.Bot(command_prefix={prefix}, self_bot=True)

@bot.event
async def on_ready():
    print("Bot connected")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def invite(ctx):
    await ctx.send("@everyone | discord.gg/5mJCYkjzFn | https://omicrontools.netlify.app/ | Join")

@bot.command()
async def credits(ctx):
    await ctx.send("Selfbot made by omicron fr src will be in github repository")


bot.run(token, bot=False)
