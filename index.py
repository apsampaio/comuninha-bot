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


def validate_sum(user_input):
    plus_count = user_input.count('+')

    new_list = user_input.split('+')
    filtered = list(filter(lambda x: x != "", new_list))

    if plus_count == 0:
        return False
    elif (plus_count != (len(filtered) - 1)):
        raise Exception
    else:
        return True


def is_dice(value):
    return value.find('d') >= 0


@client.command()
async def roll(ctx, *, user_input):    

    clean_string = user_input.replace(" ", "")

    try:
        if(validate_sum(clean_string)):
            return await ctx.send(f":yum: É uma soma válida...")
        else:
            return await ctx.send(f":hot_face: Não é uma soma válida...")

    
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
    except:
        return await ctx.send(f":x: Opa, deu erro...")



client.run(bot_secret)
