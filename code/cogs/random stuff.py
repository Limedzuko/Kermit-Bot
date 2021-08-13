import discord
from discord.ext import commands
import asyncio

class random(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def hi(self, ctx):
    message = await ctx.send("hello")
    await asyncio.sleep(0.2)
    await message.edit(content="hi")
    await asyncio.sleep(0.2)
    await message.edit(content="wassup")
    await asyncio.sleep(0.2)
    await message.edit(content=":wave:")
    await asyncio.sleep(0.2)
    await message.edit(content="how're ya doin'?")
    await asyncio.sleep(0.2)
    await message.edit(content="I'm not doin' too bad myself")
    await asyncio.sleep(0.2)
    await message.edit(content="Sorry if the messages are too fast to read")
    await asyncio.sleep(0.2)
    await message.edit(content="k gtg")
    await asyncio.sleep(0.2)
    await message.edit(content="peace bro")
    await asyncio.sleep(0.2)
    await message.edit(content=":wave:")
    await asyncio.sleep(0.2)
    await message.edit(content='bye `lol`')
  
  @commands.command()
  async def die(self, ctx):
    message = await ctx.send('u wanna kill ur `lmao`?')
    await asyncio.sleep(0.1)
    await message.edit(content='DIEEEEEEE')
    await asyncio.sleep(0.2)
    await message.edit(content='BURNNNNNNNN')
    await asyncio.sleep(0.2)
    await message.edit(content=':fire:')
    await asyncio.sleep(0.2)
    await message.edit(content='SHEEEESSSH')
    await asyncio.sleep(0.2)
    await message.edit(content='You manage to kill urself Good job! :clap:')
    await asyncio.sleep(0.2)


  @commands.command()
  async def poo(ctx):
    await ctx.message.reply('ewww why would you even tryy')
  
def setup(client):
  client.add_cog(random(client))
