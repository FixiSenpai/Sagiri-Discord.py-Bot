import os
import discord
from discord.ext import commands
import json


class maintenance(commands.Cog):
    def __init__(self, client):
        self.client = client

    #on ready
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game('s!help'))
        print('Logged in as', self.client.user.name,'!')

    #on member join
    @commands.Cog.listener()
    async def on_member_join(member):
        print(f'{member} has joined a server')

    #on member remove
    @commands.Cog.listener()
    async def on_member_remove(member):
        print(f'{member} has left a server')

    #error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.MissingRequiredArgument):
            message = f"Missing a required argument: {error.param}"
        else:
            message = "Oh no! Something went wrong while running the command!"

        await ctx.send(message, delete_after=5)
        await ctx.message.delete(delay=5)

    #prefix change
    @commands.Cog.listener()
    async def on_guild_join(guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = 's!'

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(guild):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        with open('prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Prefix changed to: {prefix}')
        name=f'{prefix}BotBot'

    #ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping = {round(self.client.latency * 1000)}ms')

    #standart help
    @commands.command()
    async def help(self, ctx):
        hEmbed = discord.Embed(title="Help", description="Bot commands", color=0xfc1703)
        hEmbed.set_author(name=self.client.user.name, icon_url=str(self.client.user.avatar_url))
        hEmbed.add_field(name="Ping", value="s!ping [Shows the Bot Latency]", inline=False)
        hEmbed.add_field(name="Version", value="s!version [Shows the Bot version]", inline=False)
        hEmbed.add_field(name="Music", value="s!music [Music commands]", inline=False)
        hEmbed.add_field(name="Moderation", value="s!moderation [Moderation commads]", inline=False)
        hEmbed.add_field(name="Gambling", value="s!gambling [Mambling commands]", inline=False)
        hEmbed.add_field(name="Tree", value="s!tree / s!baum [Posts a picture of a Tree]", inline=False)
        hEmbed.set_footer(text="Developed by Senpаi#0001")
        await ctx.message.channel.send(embed=hEmbed)

    #version
    @commands.command()
    async def version(self,ctx):
        vEmbed = discord.Embed(title="Current Version", color=0xfc1703)
        vEmbed.set_author(name=self.client.user.name, icon_url=str(self.client.user.avatar_url))
        vEmbed.add_field(name="Bot version:", value="v.1.1", inline=False)
        vEmbed.add_field(name="Bot status:", value="work in progress", inline=False)
        vEmbed.add_field(name="Relesed", value="November 12th, 2021")
        vEmbed.set_footer(text="Developed by Senpаi#0001")
        await ctx.message.channel.send(embed=vEmbed)

def setup(client):
    client.add_cog(maintenance(client))
