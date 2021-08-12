import discord
from discord.ext import commands
import aiohttp
import random
import json

class meme(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(pass_context=True)
  async def meme(self, ctx):
    embed = discord.Embed(title="", description="")

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0,25)]['data']['url'])
            await ctx.reply(embed=embed)




def setup(client):
  client.add_cog(meme(client))
