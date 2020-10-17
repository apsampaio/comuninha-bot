import discord
from dice_lib import dice
from env import bot_secret
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print(" ==== Bot Running ====")


@client.command()
async def roll(ctx, *, user_input):    

    result = dice(user_input)
    return await ctx.send(result)



client.run(bot_secret)
