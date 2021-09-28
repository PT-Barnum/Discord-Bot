# The program to run for connecting the bot to the server.
# Uses commands from bot.py as well as cogs from the modules folder.

import os
import random
import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from urllib import parse, request
import re


load_dotenv()

GUILD = os.getenv('DISCORD_GUILD')
TOKEN = os.getenv('DISCORD_TOKEN')


intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix = '!', intents=intents)


@bot.event
async def on_ready():
    print("Bot has connected!\n")

@bot.event
async def on_member_update(before, after):
    if before.status is discord.Status.offline and after.status is discord.Status.online:
        print('was offline then online')
        channel = bot.get_channel(851132472191614979)  # notification channel
        await channel.send(f'{after.name} is now {after.status}')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.channel.send(f"{str(numOne + numTwo)}")

@bot.command()
async def rollcall(ctx):
    response = ""
    for member in ctx.guild.members:
        response += (f"{member.name} is present!\n")
        response += (f"{member.name} is {member.status}\n")
    await ctx.channel.send(f"{response}")

@bot.command()
async def debate(ctx):
    response = "Every food can be categorized as either a salad, soup, or sandwich"
    await ctx.channel.send(response)

@bot.command()
async def admins(ctx):
    admins = ""
    for member in ctx.guild.members:
        role_names = [role.name for role in member.roles]
        if "admin" in role_names:
            admins += (f"{member.name}\n")
    await ctx.channel.send(f"{admins}")

@bot.command()
async def my_roles(ctx):
    response = "Your roles are:\n"
    for role in ctx.author.roles:
        response += (f"{role}\n")
    await ctx.channel.send(f"{response}")

@bot.command()
async def i_am(ctx):
    await ctx.channel.send(f"{ctx.author.name}")

for folder in os.listdir("modules"):
    if os.path.exists(os.path.join("modules", folder, "cog.py")):
        bot.load_extension(f"modules.{folder}.cog")

bot.run(TOKEN)