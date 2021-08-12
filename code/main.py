import discord
import os
import random
from discord.ext import commands
import asyncio
import json

os.system('pip3 install -r installs.txt')

client = commands.Bot(command_prefix='ayo ', help_command=None)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in os.listdir('./moderation'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Code by Limed'))


# help cmd

@client.group(invoke_without_command=True)
async def help(ctx):
    h = discord.Embed(
        title="Command List"
    )
    h.add_field(name=':yen: Currency', value='`ayo help currency`')
    h.add_field(name=':shield: Moderation', value='`ayo help moderation`')
    h.add_field(name=':golf: Games', value='`ayo help games`')
    h.add_field(name=':taco: Fun', value='`ayo help fun`')
    h.add_field(name=':gear: Utility', value='`coming soon`')
    h.add_field(name=':information_source: Info', value='`ayo help info`')
    await ctx.send(embed=h)


@help.command(aliases=['information', 'inf', 'Information', 'Info'])
async def info(ctx):
    u = discord.Embed(
        title=':anchor: Information',
        description=':satellite: Info on new updates, patches, events and more'
    )
    u.add_field(name=':bulb: Updates', value='`ayo updates`')
    u.add_field(name=':bricks: Contributers', value='`ayo contributers`')
    u.set_footer(text='that info you asked for, justin')
    await ctx.send(embed=u)


@help.command(alaises=['mod', 'admin', 'Mod', 'Admin', 'Moderation'])
async def moderation(ctx):
    umod = ['banhammer time bois',
            'Discord Crime Alert',
            "991, Emergency, there's suspicious meme activity in #general",
            "Justin died smh",
            "Beluga's mods almost made this",
            "Hit 'em with the banhammer",
            "Nice Moderation commands ikr!",
            "The mod commands are lovely and marvelous, the English love it",
            'Shout out to LimedFox']

    u = discord.Embed(
        title=':tools: Moderation Commands',
        description=':hammer: Utility Commands'
    )
    u.add_field(name=':neutral_face: Mute', value='`ayo mute`')
    u.add_field(name=':link: Kick', value='`ayo kick`')
    u.add_field(name=':lock: ban', value='`ayo ban`')
    u.add_field(name=':closed_lock_with_key: tempban', value='`ayo tempban`')
    u.add_field(name=':wrench: cooldown', value='`ayo cooldown set`')
    u.set_footer(text=f'{random.choice(umod)}')
    await ctx.send(embed=u)


@help.command()
async def currency(ctx):
    c = discord.Embed(
        title=':money_with_wings: Currency ',
        description='Earn moneh big boi'
    )
    c.add_field(name=':fingers_crossed: beg', value='`ayo beg`')
    c.add_field(name=':sewing_needle: hunt', value='`ayo hunt`')
    c.add_field(name=':fish: fish', value='`ayo fish`')
    c.add_field(name=':moneybag: rob', value='`ayo rob`')
    c.add_field(name='hack', value='`ayo hack`')
    c.add_field(name=':bank: balance', value='`ayo bal`')
    c.add_field(name=':shopping_bags: shop', value='`ayo shop`')

    c.set_footer(text='more trash commands coming soon')

    await ctx.send(embed=c)


@help.command()
async def fun(ctx):
    f = discord.Embed(title=':smile: fun', description='Plays some games that the bot features brotha')
    f.add_field(name=':joy: meme', value='`ayo meme`')
    f.add_field(name=':archery: truth', value='`ayo truth`')
    f.add_field(name=':broken_heart: dare', value='`ayo dare`')
    f.add_field(name=':thinking: emojify', value='`ayo emojify <text>`')
    f.add_field(name=':grimacing: roast', value='`ayo roast <member>`')
    f.set_footer(text='more trash commands coming soon')

    await ctx.send(embed=f)


@help.command()
async def games(ctx):
    gchange = ["Trust me you'll need help for madlibs",
               "Brand NEW - Madlibs. Out right now!",
               "More trash games coming soon"]

    g = discord.Embed(title=':golf: Games', description='gameeengg yas yas')
    g.add_field(name=':8ball: 8ball', value='`ayo 8ball <question>`')
    g.add_field(name=':ledger: madlibs', value='`ayo help madlibs`')
    g.set_footer(text=f'{random.choice(gchange)}')

    await ctx.send(embed=g)


@client.group(name='madlibs', invoke_without_command=True)
async def madlibs(ctx):
    m = discord.Embed(title=':file_folder: Madlibs',
                      description=f':newspaper: Mad Libs is a phrasal template word game which consists of a player listing a list of words to substitute for blanks in a story before reading aloud and having a halarious moment!\n Madlibs Templates-'
                      )
    m.add_field(name=':lizard: Zoo Template', value='ayo madlibs zoo')
    m.set_footer(text='More templates coming soon')
    await ctx.send(embed=m)


@madlibs.command(name='zoo')
async def zoo(ctx):
    await ctx.send(f'{ctx.author.mention} Type out a qualitative adjective [`1/13`]')

    def check(m):
        return m.author.id == ctx.author.id

    message1 = await client.wait_for('message', check=check, timeout=30)

    await ctx.send(f'{ctx.author.mention} Type out an a noun [`2/13`]')
    message2 = await client.wait_for('message', check=check, timeout=30)

    await ctx.send(f'{ctx.author.mention} Type out a past tense verb [`3/13`]')

    message3 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type out an adverb [`4/13`]')

    message4 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type out another adjective [`5/13`]')

    message5 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type out another noun [`6/13`]|')

    message6 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type out another noun [`7/13`]')

    anothernoun = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type a descriptive adjective [`8/13`]')

    anotheradj = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f"{ctx.author.mention} Type a celebrity's name [`9/13`]")

    anotheradj2 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f"{ctx.author.mention} Type another adjective please? [`10/13`]")

    verb3 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type an adverb [`11/13`]')

    adverb2 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type a past tense verb [`12/13`]')

    past2 = await client.wait_for('message', check=check, timeout=30)
    await ctx.send(f'{ctx.author.mention} Type an adjective `[13/13`]')

    finaladj = await client.wait_for('message', check=check, timeout=30)
    z = discord.Embed(title=(f"{ctx.author.name}'s Day At The Zoo :palm_tree:"),
                      description=f"Today I went to the zoo. I saw an {message1.content} {message2.content} jumping up and down its tree.\n They {message3.content} {message4.content} through the large tunnel that led to its {message5.content} {message6.content}.\n I got some peanuts and passed them through the cage to a gigantic gray {anothernoun.content} towering above my head.\n Feeding that animal made me hungry. I went to get a {anotheradj.content} scoop of {anotheradj2.content}'s ice cream.\n It filled my stomach. Afterwards I had to {verb3.content} {adverb2.content} to catch the bus.\n When I got home I {past2.content} my mom for another {finaladj.content} day at the zoo")
    await ctx.send(embed=z)

client.run('TOKEN')
