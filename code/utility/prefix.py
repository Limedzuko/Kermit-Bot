import json
from discord.ext import commands
import discord
import random



class prefix(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f) 

    prefixes[str(guild.id)] = '!'

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4) 

  @commands.Cog.listener()
  async def on_guild_remove(self, guild): 
    with open('prefixes.json', 'r') as f: 
        prefixes = json.load(f)

    prefixes.pop(str(guild.id)) 

    with open('prefixes.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)

  @commands.command()
  async def changeprefix(self, ctx, prefix): 
    if ctx.author.id == 758535252690862142:  
      with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

      with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        await ctx.send(f'Prefix changed to: {prefix}'

  @changeprefix.error
  async def changePrefixError(self, ctx, error):
    Yikeoof = ['YIKES!',
             'Owwiee!',
             'OH SNAP!',
             'Oops!',
             'OOF!',
             'Oof.']


    cb = discord.Embed(color=discord.Color.red(), title = f"{random.choice(Yikeoof)}", description = "**Specify the prefix, please.**")
    cb.set_footer(text='Turns out you made a bit of an oopsies while customizing your server prefix')
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send(embed=cb)


      

def setup(bot):
  bot.add_cog(prefix(bot))
