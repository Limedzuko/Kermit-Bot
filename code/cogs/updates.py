import discord
from discord.ext import commands

class new(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['update','New', 'Updates','updates'])
  async def new(self, ctx):
    n = discord.Embed(title = 'LATEST UPDATES AND ADDITIONS TO CLOUDBURST!')
    n.add_field(name='Update 0.0.2', value = f"**PRESENTING THE BOT'S BIGGEST ADDITION YET- MADLIBS** :partying_face: We've been working on this feature for a while, it's finally been added. NOTE - *More Madlib templates comming soon, still under massive development.* Thank you, :wave:")
    await ctx.send(embed=n)

def setup(client):
  client.add_cog(new(client))
