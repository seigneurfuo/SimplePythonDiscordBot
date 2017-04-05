import discord
from discord.ext.commands import Bot
import secrets


from random import randint
from dtc import random_quote

__version__ = "0.0.4"

bot = Bot(command_prefix="!")

@bot.event
async def on_read():
    print("Nyaa is logged in!")
    

@bot.command()
async def echo(message: str):
    """Répète le texte entré"""
    await bot.say(message)    

    
@bot.command(pass_context=True, aliases=["Hello"])
async def hello(ctx, member: discord.Member = None):
    """Réponds par un message amical"""
    if member is None:
        member = ctx.message.author
    
    user = str(member).split("#")
    pseudo = user[0]
    id = user[1]
    
    msg = ["~~Nyaaa !", "Bonjour {0} !".format(pseudo), "Salut, {0} !".format(pseudo), "Je suis une fille chat !"]
    id_ = randint(0, len(msg)-1)
    
    return await bot.say(msg[id_])
    
    
@bot.command(aliases=["DTC"])
async def dtc(*args):
    """Affiche une quote alléatoire de DansTonChat"""
    quote = random_quote()
    return await bot.say(quote)
    

@bot.command(aliases=["Phrase"])
async def phrase(*args):
    """Affiche une phrase du père doriot aléatoire"""
    msg = ["Pour ce qui est de ce pignoler, il se masturbe toute la journée !", 
           "Le son, régler le son !",
           "A non ! Il n'en est pas question !",
           "Allez vous faire foutre ! Enfants de pute !",
           "Douze travelos ?!",
           "Des hommes ?!", 
           "C'est indéniable gaulois... C'est un échec !!",
           "Plus ils sont gros, plus je les aimes !"]
           
    id_ = randint(0, len(msg)-1)
    
    return await bot.say(msg[id_])


@bot.command(aliases=["Nyaa"])
async def nyaa(*args):
    """Interpèle le bot"""
    msg = ["Qui ose me déranger ?",
           "Oui, on me parle ?",
           "ZZzzzz...",
           "Oui, que puis-je faire pour vous ?",
           "C'est inyan missible de me réveiller ainsi"
           "Le matin ?! C'est déja le matin ?!",
           "Voici le code de ma carte banquaire... Enfaite non ^^"]
           
    id_ = randint(0, len(msg)-1)
    
    return await bot.say(msg[id_])
  
    
bot.run(secrets.BOT_TOKEN)
