from discord.ext import commands
import discord


class mute(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

 
  @commands.command()
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title=f"{member} was muted!", description=f"Reason: {reason}", colour=discord.Colour.red())
    
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"You got muted from {ctx.guild.name} for `{reason}` by `{ctx.author.name}`.")

  @commands.command()
  async def unmute(self, ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f"You got unmuted from {ctx.guild.name} :partying_face:!")
   embed = discord.Embed(title=f"{member} got unmuted!", description=f"Unmuted by `{ctx.author}`",colour=discord.Colour.green())
   await ctx.send(embed=embed)
  



def setup(bot):
  bot.add_cog(mute(bot))