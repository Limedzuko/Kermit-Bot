from discord.ext import commands
import discord
import random


class ban(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

 
  @commands.command()
  async def ban(self, ctx, member: discord.Member, *, reason=None):


    Yikeoof = ['YIKES!',
             'Owwiee!',
             'OH SNAP!',
             'Oops!',
             'OOF!',
             'Oof.']
  

    ea = discord.Embed(color=discord.Color.red())
    ea.add_field(name=f"{member} got banned!", value = f"Reason: **{reason}**")
    ea.set_footer(text=f"{random.choice(Yikeoof)}")

  
    await member.ban(reason=reason)
    await ctx.send(embed=ea)
    await member.send(f"You've been banned in {ctx.guild.name} for {reason}.")


  @commands.command(aliases=['ub'])
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

  
    for ban_entry in banned_users:
      user = ban_entry.user


      if(user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'`{member} has been unbanned!`')
        await member.send(f"You've been unbanned from {ctx.guild.name} :partying_face:!")
        return

  



def setup(bot):
  bot.add_cog(ban(bot))