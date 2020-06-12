import discord
from discord.ext import tasks, commands

class arkhamDB(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        url = "https://arkhamdb.com/api/public/"

    @commands.group(name="arkhamdb")
    async def arkhamdb_group(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid subcommand passed.")
    
    @arkhamdb_group.command(name='decklist')
    async def decklist_subcommand(self, ctx, number: int):
        await ctx.channel.send("Eventually this will retrieve a decklist")

def setup(bot):
    bot.add_cog(arkhamDB(bot))