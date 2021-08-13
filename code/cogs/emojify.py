import discord
from discord.ext import commands

class emojify(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def emojify(self, ctx,*,text):
    emojis = []
    for s in text.lower():
      if s.isdecimal():
        num2emo = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six', '7':'seven','8':'eight', '9':'nine'}
        emojis.append(f':{num2emo.get(s)}:')
      elif s.isalpha():
          emojis.append(f':regional_indicator_{s}:')
      else:
        emojis.append(s)
    await ctx.send(''.join(emojis))

  @emojify.error
  async def emojify_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("I honestly don't think that I can emojify air. Only letters on numbers.")

def setup(client):
  client.add_cog(emojify(client))
