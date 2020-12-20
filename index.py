from dotenv import load_dotenv
load_dotenv()


import discord
import os
import requests
import json

from discord.ext import commands

from dice_lib import dice
from facebook_scraper import get_posts

client = commands.Bot(command_prefix=".")

SECRET = os.getenv("SECRET")
CAT_SECRET = os.getenv("CAT_SECRET")

@client.event
async def on_ready():
    print(" ==== Bot Running ====")


@client.command(name="ajuda")
async def ajuda(ctx):
    ##  ##
    output = f'''Olá {ctx.author.mention} 👋.

    No momento tenho apenas os comandos:

    **.roll** -  Rola um dado de RPG
    **.pollyn** - Cria uma votação de Sim, Não e Talvez
    **.steam** - Atualizo o canal de promoções da Steam Brasil
    **.sexo** - Manda sexo no canal sexo

    Se o corno do ADM trabalhar logo terei mais comandos.🥵'''
    return await ctx.send(output)
    ##  ##

@client.command()
async def steam(ctx):
    ##  ##
    channel = client.get_channel(769224265697329164)

    reader = open("steampost.txt", "r")
    list_string = reader.read()
    reader.close()

    writer = open("steampost.txt", "a")

    post_list = list_string.split(" ")

    try:
        for post in get_posts('comusteambrasil', pages=2):
            if str(post['post_id']) not in post_list:
                await channel.send(f'''```md
# {post['time']}
{post['text']}```''')
                writer.write(f" {post['post_id']}")
        writer.close()
        return

    except:
        print("ops")
    ##  ##

@client.command()
async def roll(ctx, *, user_input):    

    result = dice(user_input)
    await ctx.message.add_reaction('👍')
    return await ctx.send(f"{ctx.author.mention}\r{result}")


@client.command()
async def pollyn(ctx, *, title):
    ##  ##
    output = f"{ctx.author.mention} **iniciou uma votação:**\r\r**{title}**\r\r"
    poll_message = await ctx.send(output)
    await poll_message.add_reaction('👍')
    await poll_message.add_reaction('👎')
    await poll_message.add_reaction('🤷‍♂️')
    return 
    ##  ##


@client.command()
async def sexo(ctx):
    ##  ##
    channel = client.get_channel(760526973897932880)
    return await channel.send("sexo")
    ##  ##


@client.command()
async def neutre(ctx, *, user_input):
    ##  ##
    string_neutre = user_input.replace("a", "e")
    string_neutre = string_neutre.replace("o", "e")

    await ctx.send(string_neutre)
    ##  ##


@client.command()
async def cat(ctx):
    url = "https://api.thecatapi.com/v1/images/search"
    querystring = {"x-api-key":CAT_SECRET}
    payload = ""

    try:
        response = requests.request("GET", url, data=payload, params=querystring)
        value = json.loads(response.text)[0]
        embed = discord.Embed(title="Meow 😺", color=0xff5555)
        embed.set_image(url=value["url"])
        await ctx.send(embed=embed)
    except Exception as err:
        print(err)
        await ctx.send("Aconteceu um erro... 🙀")
        



client.run(SECRET)