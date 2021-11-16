import discord
from discord.ext import commands
import random

class gambling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gambling(self, ctx):
        gEmbed = discord.Embed(title="Gambling help", description="Commands for gambling", color=0xfc1703)
        gEmbed.set_author(name=self.client.user.name, icon_url=str(self.client.user.avatar_url))
        gEmbed.add_field(name="8ball", value="s!8ball (question) [Watch into the Future]", inline=False)
        gEmbed.add_field(name="Coinflip", value="s!coinflip [Flip a coin]", inline=False)
        gEmbed.set_footer(text="Developed by Senpаi#0001")
        await ctx.message.channel.send(embed=gEmbed)

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def coinflip(self, ctx):
        responses = ['heads','tails']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(gambling(client))