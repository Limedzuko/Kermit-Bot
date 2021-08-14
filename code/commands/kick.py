from discord.ext import commands
import discord


class kick(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

 
  @commands.command()
  async def kick(self, ctx, member: discord.Member, *, reason=None):
  

    ea = discord.Embed(color=discord.Color.red())
    ea.add_field(name=f"{member} got kicked!", value = f"Reason: **{reason}**")
  
    await member.kick(reason=reason)
    await ctx.send(embed=ea)

    
def setup(bot):
  bot.add_cog(kick(bot))
