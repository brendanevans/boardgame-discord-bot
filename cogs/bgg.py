import requests
import json
import datetime
import asyncio
import os
from retry import retry

import discord
from discord import Game
from discord.ext.commands import Bot
from discord.ext import tasks, commands

class boardGameGeek(commands.Cog):
    def __init__(self, bot):

        url = "https://www.boardgamegeek.com/xmlapi2/"

        @commands.command(description = "Get plays from BoardGameGeek for a user")
        async def plays(self, ctx, bgguser, date):
            print("This is a placeholder.")


def setup(bot):
    bot.add_cog(boardGameGeek(bot))