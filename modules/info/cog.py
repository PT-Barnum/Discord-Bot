import os
import random
import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from urllib import parse, request
import re

class Embed(commands.Cog, name="Embed Cog"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx: commands.Context):
        embed = discord.Embed(title=f"{ctx.guild.name}", description="Where people gather.", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        leaders = ""
        for member in ctx.guild.members:
            role_names = [role.name for role in member.roles]
            if "admin" in role_names:
                leaders += (f"{member.name}\n")
        embed.add_field(name="Leaders", value=f"{leaders}")
        embed.set_thumbnail(url="https://i.redd.it/28y7kc7ibn071.jpg")

        await ctx.channel.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(Embed(bot))