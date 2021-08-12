import discord
from discord.ext import commands
import random

class roast(commands.Cog):

  def __init__(self, client):
    self.client = client

  
  @commands.command()
  async def roast(self, ctx,member: discord.Member):
    roasts=['You’re the reason God created the middle finger.',
           'Your secrets are always safe with me. I never even listen when you tell me them.',
           'You bring everyone so much joy when you leave the room.',
           ' I may love to shop but I will never buy your bull.',
           'I’d give you a nasty look but you’ve already got one.',
           ' Someday you’ll go far. I hope you stay there.',
            'Were you born this stupid or did you take lessons?',
            'The people who tolerate you on a daily basis are the real heroes.',
            'You should really consider coming with a warning label smh',
            'You look like something that came out of a slow cooker.',
            'I don’t know what your problem is, but I’m guessing it’s hard to pronounce.',
            'If I wanted to hear from a moron, I’d fart and come to you.',
            'It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence.',
            'You look like something that came out of a slow cooker',
            'I will ignore you so hard you will start doubting your existence.',
            'Feed your own ego. I’m busy.',
            ' I’ll never forget the first time we met. But I’ll keep trying.',
            'You’re a grey sprinkle on a rainbow cupcake.',
            ' I thought of you today. It reminded me to take out the trash.',
            ' You are so full of poop, the toilet’s jealous.',
            'I love what you’ve done with your hair. How do you get it to come out of the nostrils like that?',
            'Stupidity isn’t a crime, so you’re free to go.',
            'I’ve been called worse by better.',
            'Don’t you get tired of putting makeup on your two faces every morning?',
            'Too bad you can’t Photoshop your ugly personality.',
            'Do your parents even realize they’re living proof that two wrongs don’t make a right?',
            'Jesus might love you, but everyone else definitely thinks you’re an idiot.',
            'Please just tell me you don’t plan to home-school your kids.',
            'You see that door? I want you on the other side of it.',
            'You’re like the end pieces of a loaf of bread. Everyone touches you, but nobody wants you.',
            'If you’re going to act like a turd, go lay on the yard.',
            'You are more disappointing than an unsalted pretzel.',
            'Your face makes onions cry.',
            'Don’t worry about me. Worry about your eyebrows.',
            'Where’d you get your clothes, girl, American Apparently Not?',
            'If laughter is the best medicine, your face must be curing the world.',
            'You’re not stupid! You just have bad luck when you’re thinking.',
            'Isn’t there a bullet somewhere you could be jumping in front of?',
            'I’d slap you but I don’t want to make your face look any better.',
            ' Have a nice day, ||somewhere else||.',
            'Everyone’s entitled to act stupid once in a while, but you really abuse the privilege.',
            'If ignorance is bliss, you must be the happiest person on the planet.',
            "I got too weak to roast you this time bud, but imma get you next time you hearin' me?",
            "Your family tree must be a cactus ‘cause you’re all a bunch of pricks.",
            'If I threw a stick, you’d leave, right?',
            'Somewhere out there, there’s a tree working very hard to produce oxygen so that you can breathe. I think you should go and apologize to it.',
            'You look like a ‘before’ picture.',
            'Light travels faster than sound which is why you seemed bright until you spoke.',
            'Hold still. I’m trying to imagine you with personality.',
            'You are the human version of period cramps.',
            'Don’t get bitter, just get better" - your very mom',
            '50. What doesn’t kill you, disappoints me.',
            'Aww, it’s so cute when you **try** to talk about things you don’t understand.',
            'Hey, your village called – they want their idiot back.',
            'Calling you an idiot would be an insult to all stupid people.',
            'I am returning your nose. I found it in my business.',
            'Good story, but in what chapter do you shut up?',
            'There are some remarkably dumb people in this world. Thanks for helping me understand that.',
            'You’re about as useful as an ashtray on a motorcycle.',
            'You’ll never be the man your mom is',
            'You need a kiss on the neck from a crocodile.',
            'May both sides of your pillow be uncomfortably warm.',
            'Your kid is so annoying, he makes his Happy Meal cry.',
            'Oh, I’m sorry. Did the middle of my sentence interrupt the beginning of yours?',
            'Oops, my bad. I could’ve sworn I was dealing with an adult.',
            'Did I invite you to the barbecue? Then why are you all up in my grill?'
            'I’m an acquired taste. If you don’t like me, acquire some taste.',
            'Somewhere out there is a tree tirelessly producing oxygen for you. You owe it an apology.',
            'Yeah? Well, you smell like hot dog water.',
            'Beauty is only skin deep, but ugly goes clean to the bone.',
            'Oh, you don’t like being treated the way you treat me? That must suck.',
            'Pierre Trudeau, a Canadian politician, used this clap back after learning that Richard Nixon had insulted him. The political shade!',
            'Well, the jerk store called. They’re running out of you.',
            '“What, like it’s hard?” — Elle Woods, Legally Blonde',
            'Sorry, not sorry bwo',
            'I’m busy right now; can I ignore you another time?',
            'If you have a problem with me, write the problem on a piece of paper, fold it, and shove it into your brain `lol`.',
            'You have an entire life to be an idiot. Why not take today off?',
            'No matter how much a snake sheds its skin, it’s still a snake.',
            'Some people are like slinkies — not really good for much, but they bring a smile to your face when pushed down the stairs.',
            'You’re the reason this country has to put directions on shampoo.',
            'Of course I’m talking like an idiot… how else could you understand me?',
            'Are you almost done with all of this drama? Because I need an intermission.',
            'I’d give you a nasty look, but you’ve already got one.',
            'I’d agree with you, but then we’d both be wrong.',
            'Since you know it all, you should know when to shut up.',
            ' Life is full of disappointments, and I just added you to the list.',
            'I treasure the time I don’t spend with you.',
            'I was going to make a joke about your life, but I see life beat me to the punch.',
            'The last time I saw something like you… I flushed.',
            'The only work-life balance I want is being away from you.',
            "When you start talking, I'd rather go `deaf`."]
            



    if member == ctx.message.author:
      await ctx.send('Imagine trying to roast yourself lol. What a nub.')
    else:
      await ctx.send(f"{ctx.author.name} roasted {member.name} by going, ❝{random.choice(roasts)}❞")


  @roast.error
  async def roast_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):  
       await ctx.send("Maybe try mentioning someone to roast next time, genius")


def setup(client):
  client.add_cog(roast(client))
