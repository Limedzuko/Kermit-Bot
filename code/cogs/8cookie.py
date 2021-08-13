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
    
  @commands.command(aliases=['Magic8ball','8ball' , '8bal'])
  async def _8ball(self, ctx, *, question):
    responses =  ["It is certain.",
                  "It is decidedly so.",
                  "Without a doubt.",
                  "Yes - definitely.",
                  "You may rely on it.",
                  "As I see it, yes.",
                  "Most likely.",
                  "Outlook good.",
                  "Yes.",
                  "Signs point to yes.",
                  "Reply hazy, try again.",
                  "Ask again later.",
                  "Better not tell you now.",
                  "Cannot predict now.",
                  "Concentrate and ask again.",
                  "Don't count on it.",
                  "My reply is no.",
                  "My very terrible sources say no.",
                  "Outlook not so good.",
                  "Very doubtful."]
    await ctx.send(f'ur question: {question}\n my answer: {random.choice(responses)}')

def setup(client):
  client.add_cog(cookie(client))
