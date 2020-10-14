import discord
import random
from env import bot_secret
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print(" ==== Bot Running ====")


def roll_dice(dice):
    rolling_number, dice_value = dice.split('d')

    result = 0
    result_list = []

    for i in range(int(rolling_number)):
        random_value = random.randint(1, int(dice_value))
        result += random_value
        result_list.append(random_value)
    return result, result_list


def is_sum(user_input):
    return user_input.find('+') >= 0


def is_dice(value):
    return value.find('d') >= 0





@client.command()
async def roll(ctx, *, user_input):    

    user_input_string = user_input.replace(" ", "")

    if(is_dice(user_input_string)):
         result, result_list = roll_dice(user_input_string)
         return await ctx.send(f"**{result}** ⇐ {result_list} {user_input}")

    return await ctx.send(f":hot_face: Não consegui entender seu comando...")

    values = user_input.split('+')

    for i in range(0, len(values)):
        is_dice(values[i])
    total_list.append((result, result_list))
    total_result += result


    return await ctx.send(f"**{total_result}** ⇐ {total_list} {arg}")

    result, result_list = roll_dice(arg)
    return await ctx.send(f"**{result}** ⇐ {result_list} {arg}")

client.run(bot_secret)
