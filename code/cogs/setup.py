import discord
from discord.ext import commands

kermit = """
██╗░░██╗███████╗██████╗░███╗░░░███╗██╗████████╗
██║░██╔╝██╔════╝██╔══██╗████╗░████║██║╚══██╔══╝
█████═╝░█████╗░░██████╔╝██╔████╔██║██║░░░██║░░░
██╔═██╗░██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░░██║░░░
██║░╚██╗███████╗██║░░██║██║░╚═╝░██║██║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░
"""


class setup(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    print(kermit)

    
  @commands.Cog.listener()
  async def on_guild_join(self, ctx):
    guild = ctx.guild
    await guild.create_role(name="Muted")

def setup(client):
  client.add_cog(setup(client))
