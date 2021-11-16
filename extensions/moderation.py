import discord
from discord.ext import commands

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def moderation(self, ctx):
        mEmbed = discord.Embed(title="Moderation help", description="Commands for moderation", color=0xfc1703)
        mEmbed.set_author(name=self.client.user.name, icon_url=str(self.client.user.avatar_url))
        mEmbed.add_field(name="Clear", value="s!clear (value) [Clear the chat]", inline=False)
        mEmbed.add_field(name="Change prefix", value="s!changeprefix [Change the command prefix]", inline=False)
        mEmbed.add_field(name="Kick", value="s!kick (Name) [Kick a member]", inline=False)
        mEmbed.add_field(name="Ban", value="s!ban (Name) [Ban a member]", inline=False)
        mEmbed.add_field(name="Unban", value="s!unban (Name#????) [Ban a member]", inline=False)
        mEmbed.set_footer(text="Developed by Senpаi#0001")
        await ctx.message.channel.send(embed=mEmbed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
	    await ctx.channel.purge(limit=amount + 1)
            
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *,member):
        banned_user = await ctx.guild.bans()

        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_user:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(moderation(client))