import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import logging
from extensions import maintenance, moderation, gambling, fun, music

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


cogs = [maintenance, moderation, gambling, fun, music]

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)
client.remove_command('help')

for i in range(len(cogs)):
    cogs[i].setup(client)

client.load_extension('dismusic')

client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier': 'MAIN',
        'password': 'anything',
        'region': 'rotterdam'
    }
]

client.run(TOKEN)