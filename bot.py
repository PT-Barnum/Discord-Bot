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
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def rollcall(ctx):
    response = ""
    for member in ctx.guild.members:
        response += (f"{member.name} is present!\n")
        response += (f"{member.name} is {member.status}\n")
    await ctx.channel.send(f"{response}")

@bot.command()
async def say(ctx, *, text=''):
    if text == '':
        await ctx.channel.send("WHAT DO YOU WANT FROM ME??")
    else:
        await ctx.channel.send(f"{text}")

@bot.command()
async def debate(ctx):
    response = "Every food can be categorized as either a salad, soup, or sandwich"
    await ctx.channel.send(response)

@bot.command()
async def leaders(ctx):
    leaders = ""
    for member in ctx.guild.members:
        role_names = [role.name for role in member.roles]
        if "Purple Role" in role_names:
            leaders += (f"{member.name}\n")
    await ctx.channel.send(f"{leaders}")

# Work on this !!
@bot.command()
async def my_roles(ctx):
    response = "Your roles are:\n"
    for role in ctx.author.roles:
        response += (f"{role}\n")
    await ctx.channel.send(f"{response}")

@bot.command()
async def i_am(ctx):
    await ctx.channel.send(f"{ctx.author.name}")

@bot.command()
async def youtube(ctx, *, search):
    # https://www.youtube.com/results?search_query=...
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # retrieves the ending tag for the https address which results in a video pulling up
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    # first result will be the closest match to the search query
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Where tubas gather.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    leaders = ""
    for member in ctx.guild.members:
        role_names = [role.name for role in member.roles]
        if "admin" in role_names:
            leaders += (f"{member.name}\n")
    embed.add_field(name="Tuba Leaders", value=f"{leaders}")

    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.channel.send(embed=embed)

bot.run(TOKEN)