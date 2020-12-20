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
DOG_SECRET = os.getenv("DOG_SECRET")

@client.event
async def on_ready():
    print(" ==== Bot Running ====")


@client.command(name="ajuda")
async def ajuda(ctx):
    ##  ##
    await ctx.message.add_reaction('👍')
    output = f'''Olá {ctx.author.mention} 👋
    No momento tenho apenas os comandos:

    **.roll** -  Rola um dado de RPG
    Ex: .roll 1d6

    **.pollyn** - Cria uma votação de Sim, Não e Talvez
    Ex: .pollyn O Miranda é gay?

    **.steam** - Atualizo o canal de promoções da Steam Brasil

    **.sexo** - Manda sexo no canal sexo
    
    **.cat** - Manda imagem de um gatinho🐱

    **.dog** - Manda imagem de um cachorro🐶

    Se o corno do ADM trabalhar logo terei mais comandos.'''

    embed = discord.Embed(description=output, color=0xff5555)
    message = await ctx.send(embed=embed)
    await message.add_reaction('🥵')
    await message.add_reaction('🥶')
    ##  ##


@client.command()
async def steam(ctx):
    ##  ##
    await ctx.message.add_reaction('🎮')
    channel = client.get_channel(769224265697329164)
    reader = open("steampost.txt", "r")
    list_string = reader.read()
    reader.close()

    writer = open("steampost.txt", "a")

    post_list = list_string.split(" ")

    try:
        for post in get_posts('comusteambrasil', pages=2):
            if str(post['post_id']) not in post_list:
                embed = discord.Embed(title=str(post['time']), description=post['text'], color=0xff5555)
                message = await channel.send(embed=embed)
                await message.add_reaction('🥵')
                await message.add_reaction('🥶')
                writer.write(f" {post['post_id']}")
        writer.close()
        return

    except Exception as err:
        print(err)
    ##  ##


@client.command()
async def roll(ctx, *, user_input):    
    ##  ##
    result = dice(user_input)
    await ctx.message.add_reaction('👍')
    embed = discord.Embed(description=f"{ctx.author.mention}\r{result}", color=0xff5555)
    await ctx.send(embed=embed)
    ##  ##


@client.command()
async def pollyn(ctx, *, title):
    ##  ##
    await ctx.message.add_reaction('👍')
    embed = discord.Embed(title=title, description=f"{ctx.author.mention} iniciou uma votação.", color=0xff5555)
    message = await ctx.send(embed=embed)
    await message.add_reaction('👍')
    await message.add_reaction('👎')
    await message.add_reaction('🤷‍♂️')
    return 
    ##  ##


@client.command()
async def sexo(ctx):
    ##  ##
    await ctx.message.add_reaction('🥵')
    channel = client.get_channel(760526973897932880)
    return await channel.send("sexo")
    ##  ##


@client.command()
async def neutre(ctx, *, user_input):
    ##  ##
    await ctx.message.add_reaction('👍')
    string_neutre = user_input.replace("a", "e")
    string_neutre = string_neutre.replace("o", "e")
    discord.Embed(description=string_neutre, color=0xff5555)
    await ctx.send(embed=embed)
    ##  ##


@client.command()
async def cat(ctx):
    ##  ##
    await ctx.message.add_reaction('😸')
    url = "https://api.thecatapi.com/v1/images/search"
    querystring = {"x-api-key":CAT_SECRET}
    payload = ""

    try:
        response = requests.request("GET", url, data=payload, params=querystring)
        value = json.loads(response.text)[0]
        embed = discord.Embed(title="Kitty 😺", color=0xff5555)
        embed.set_image(url=value["url"])
        message = await ctx.send(embed=embed)
        await message.add_reaction('❤')
        await message.add_reaction('💔')
    except Exception as err:
        print(err)
        await ctx.send("Aconteceu um erro... 🙀")
    ##  ##


@client.command()
async def dog(ctx):
    ##  ##
    await ctx.message.add_reaction('🌭')
    url = "https://api.thedogapi.com/v1/images/search"
    querystring = {"x-api-key":DOG_SECRET}
    payload = ""
    try:
        response = requests.request("GET", url, data=payload, params=querystring)
        value = json.loads(response.text)[0]
        embed = discord.Embed(title="Doggo 🐶", color=0xff5555)
        embed.set_image(url=value["url"])
        message = await ctx.send(embed=embed)
        await message.add_reaction('❤')
        await message.add_reaction('💔')
    except Exception as err:
        print(err)
        await ctx.send("Aconteceu um erro... 🌭")
    ##  ##  


@client.command()
async def doge(ctx):
    ##  ##
    await ctx.message.add_reaction('🌭')
    url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"
    payload = ""
    try:
        response = requests.request("GET", url, data=payload)
        value = json.loads(response.text)
        embed = discord.Embed(title="Doge 🐕", color=0xff5555)
        embed.set_image(url=value[0])
        message = await ctx.send(embed=embed)
        await message.add_reaction('❤')
        await message.add_reaction('🌭')
    except Exception as err:
        print(err)
        await ctx.send("Aconteceu um erro... 😱")
    ##  ##  


client.run(SECRET)