import discord
from discord.ext import commands

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def music(self, ctx):
        mEmbed = discord.Embed(title="Music help", description="Music commands", color=0xfc1703)
        mEmbed.set_author(name=self.client.user.name, icon_url=str(self.client.user.avatar_url))
        mEmbed.add_field(name="Connect", value="s!connect | s!con [Connect the bot]", inline=False)
        mEmbed.add_field(name="Play", value="s!play (Name or link) [Play a song]", inline=False)
        mEmbed.add_field(name="Pause", value="s!pause [Pause the song]", inline=False)
        mEmbed.add_field(name="Resume", value="s!resume [Resume the song]", inline=False)
        mEmbed.add_field(name="Queue", value="s!queue [Show current queue]", inline=False)
        mEmbed.add_field(name="Now playing", value="s!nowplaying [Show current songs]", inline=False)
        mEmbed.add_field(name="Loop", value="s!loop [Loop current song or playlist]", inline=False)  
        mEmbed.add_field(name="Equalizer", value="s!equalizer [Equalizer]", inline=False)
        mEmbed.add_field(name="Seek", value="s!seek (seconds) [Seek player]", inline=False)              
        mEmbed.add_field(name="Disconnect", value="s!disconnext | s!dc [Disconnect bot]", inline=False)
        mEmbed.set_footer(text="Music extension:\n@Dismusic(pypi.org/project/dismusic/)")
        await ctx.message.channel.send(embed=mEmbed)

def setup(client):
    client.add_cog(music(client))
