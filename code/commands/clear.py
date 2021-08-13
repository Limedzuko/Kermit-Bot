from discord.ext import commands
import discord
import random


class clear(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  
  @commands.command(aliases=['purge', 'delete'])
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount: int):

    hff = discord.Embed(color=discord.Color.green(),
    title=f':white_check_mark: Cleared {amount} messages from the chat')

    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(embed=hff, delete_after=5)

  @commands.command()
  async def celar(self, ctx):
    await ctx.send('Maybe you meant "`!clear <amount>`"')
  
  
  @clear.error
  async def on_command_error(self, ctx, error):


    Yikeoof = ['YIKES!',
             'Owwiee!',
             'OH SNAP!',
             'Oops!',
             'OOF!',
             'Oof.']


    cb = discord.Embed(color=discord.Color.red(), title = f"{random.choice(Yikeoof)}", description = "**Specify an amount to clear, please.**")
    cb.set_footer(text='Turns out you made a bit of an oopsies while clearing the chat!')
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(embed=cb)

def setup(bot):
  bot.add_cog(clear(bot))
