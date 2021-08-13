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


  @commands.command(aliases=['Contributers', 'devs','ppl','people', 'Devs'])
  async def contributers(self, ctx):
    cbs = discord.Embed(title=":reminder_ribbon: Cloudburst's Main Contributers", color = discord.Colour.teal())
    cbs.add_field(name='**Our Developers:**', value = '*Main Dev(s): **Limed***\n*BackupHelpDev: **MathIsCool***',inline=False)
    cbs.add_field(name='**Our Brainstormer(s):**', value ='***Limed***\n***BeastUnworn***',inline=False)
    cbs.set_footer(text='Discord tags blurred for privacy reasons')
    await ctx.send(embed=cbs)




def setup(client):
  client.add_cog(new(client))
