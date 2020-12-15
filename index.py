import discord

from dice_lib import dice
from neutre_lib import neutro

from facebook_scraper import get_posts

from env import bot_secret
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print(" ==== Bot Running ====")


@client.command(name="ajuda")
async def ajuda(ctx):
    output = f'''Olá {ctx.author.mention} 👋.

    No momento tenho apenas os comandos:

    **.roll** -  Rola um dado de RPG
    **.pollyn** - Cria uma votação de Sim, Não e Talvez
    **.steam** - Atualizo o canal de promoções da Steam Brasil
    **.sexo** - Manda sexo no canal sexo

    Se o corno do ADM trabalhar logo terei mais comandos.🥵'''
    return await ctx.send(output)


@client.command()
async def steam(ctx):

    channel = client.get_channel(769224265697329164)

    reader = open("steampost.txt", "r")
    list_string = reader.read()
    reader.close()

    writer = open("steampost.txt", "a")

    post_list = list_string.split(" ")

    try:
        for post in get_posts('comusteambrasil', pages=2):
            if str(post['post_id']) not in post_list:
                await channel.send(f"**{post['time']}**\r{post['text']}")
                writer.write(f" {post['post_id']}")
        writer.close()
        return

    except:
        print("ops")


@client.command()
async def roll(ctx, *, user_input):    

    result = dice(user_input)
    await ctx.message.add_reaction('👍')
    return await ctx.send(f"{ctx.author.mention}\r{result}")


@client.command()
async def pollyn(ctx, *, title):

    output = f"{ctx.author.mention} **iniciou uma votação:**\r\r**{title}**\r\r"
    poll_message = await ctx.send(output)
    await poll_message.add_reaction('👍')
    await poll_message.add_reaction('👎')
    await poll_message.add_reaction('🤷‍♂️')
    return 


@client.command()
async def sexo(ctx):
    channel = client.get_channel(760526973897932880)
    return await channel.send("sexo")


@client.command()
async def neutre(ctx, *, user_input):
    result = neutro(user_input)
    await ctx.send(result, tts=True)


@client.command()
async def teste(ctx):
    await ctx.send(f'''```ml
'Nome': John Cast 
'Vida' : 30/30
```''')


client.run(bot_secret)