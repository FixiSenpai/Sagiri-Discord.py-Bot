import discord
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, ctx, payload):
        message_id = payload.message_id
        if message_id == 909914587091071068:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

            role = discord.utils.get(guild.roles, name='')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(payload):
        pass


def setup(client):
    client.add_cog(fun(client))