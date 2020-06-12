import json
import asyncio
import os
from random import randint

import discord
from discord.ext.commands import Bot
from discord.ext import tasks

#Load the config file
with open('config.json' ,'r') as r:
    config = json.load(r)

bot = Bot(command_prefix = config['bot']['prefix'])

@bot.event
async def on_ready():
    print("Connected and ready.")


if __name__ == '__main__':
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')
    bot.run(config['bot']['secret'])