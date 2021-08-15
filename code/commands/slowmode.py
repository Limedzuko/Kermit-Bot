from discord.ext import commands


class slowmode(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(case_insensitive=True, aliases=['sm', 'cooldown', 'cd', 'Slowmode','ChatCool'])
  async def slowmode(self, ctx, x: int):
    if(not ctx.author.guild_permissions.manage_messages):
      await ctx.send('Invalid Permissions')
    if x == 0:

      


      await ctx.send("Slowmode's been set to `0`")
      await ctx.channel.edit(slowmode_delay = 0)

    elif x > 21600:
      await ctx.send("That is higher than discord's maximum slowmode of 6 hrs!")
      return

    else: 
      await ctx.channel.edit(slowmode_delay = x)
      await ctx.channel.send(f"Slowmode has been changed to `{x}`")
 

  @slowmode.error
  async def error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.channel.send("Please mention a value to set the slowmode to.")

 
     
def setup(bot):
  bot.add_cog(slowmode(bot))
