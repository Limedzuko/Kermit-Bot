from discord.ext import commands
import random

class reverse(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def reverse(self, ctx, *, text: str):
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f" {t_rev}")

  @commands.command(aliases=["slots", "bet"])
  async def slot(self, ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

    if (a == b == c):
      await ctx.send(f"{slotmachine} All matching, you won!")
    elif (a == b) or (a == c) or (b == c):
      await ctx.send(f"{slotmachine} 2 in a row, you won!")
    else:
       await ctx.send(f"{slotmachine} No match, you lost")

  

    
def setup(client):
  client.add_cog(reverse(client))
