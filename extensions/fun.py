import discord
from discord.ext import commands


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['baum'])
    async def tree(self, ctx):
        with open('extensions/pictures/tree.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.channel.send(file=picture)

    @commands.command(aliases=['fube'])
    async def gay(self, ctx):

        dev_id = 406540553262727180
        user_id = '610902170770079746'
        if ctx.message.author.id == dev_id:
            await ctx.channel.send(f'Gayest man alive <@{user_id}>\n https://scp-wiki.wikidot.com/scp-230')
            print(f'{ctx.message.author.id}')
        else:
            await ctx.message.channel.send('**Only the developer is able to use this command!**')

    @commands.command(aliases=['YEET'])
    async def yeet(self, ctx):
        with open('extensions/pictures/yeet.png', 'rb') as f:
            picture = discord.File(f)
        await ctx.channel.send(file=picture)
        await ctx.channel.send('YEET!')

def setup(client):
    client.add_cog(fun(client))
