import discord
from discord.ext import commands

class cookie(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def cookie(self,ctx):
    cookiebed=discord.Embed(
        title = "You want a cookie boi?" ,
        description = f"Alright, here's a :cookie:" ,
        colour = discord.Colour.orange())
    await ctx.send(embed=cookiebed)

def setup(client):
  client.add_cog(cookie(client))
