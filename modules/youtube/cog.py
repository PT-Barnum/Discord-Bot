import os
import random
import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
from urllib import parse, request
import re

class Youtube(commands.Cog, name="Youtube Cog"):
    """Receives ping commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def youtube(self, ctx:commands.Context , search: str):
        # https://www.youtube.com/results?search_query=...
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        # retrieves the ending tag for the https address which results in a video pulling up
        search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        # first result will be the closest match to the search query
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

def setup(bot: commands.Bot):
    bot.add_cog(Youtube(bot))