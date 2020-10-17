import random

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

    if plus_count == 0:
        return False

    new_list = user_input.split('+')
    filtered = list(filter(lambda x: x != "", new_list))

    if (plus_count != (len(filtered) - 1)):
        raise Exception
    else:
        return True


def validate_dice(user_input):
    d_count = user_input.count('d')

    if (d_count == 0):
        return Exception

    new_list = user_input.split('d')
    filtered = list(filter(lambda x: x != "", new_list))
    
    if(len(filtered) != 2):
        return Exception

    if(filtered[0].isnumeric() == False or filtered[1].isnumeric() == False):
        raise Exception

    return True

def dice(user_input):
    clean_string = user_input.replace(" ", "")
    try:
        if(validate_sum(clean_string)):
            string_result = ""
            total_result = 0

            sum_list = clean_string.split('+')
            filtered_list = list(filter(lambda x: x != "", sum_list))

            for i in range(0, len(filtered_list)):
                if(filtered_list[i].isnumeric()):
                    string_result += f"{filtered_list[i]}"
                    if i != len(filtered_list) - 1: string_result += " + "
                    total_result += int(filtered_list[i])
                else:
                    if(validate_dice(filtered_list[i])):
                        result, result_list = roll_dice(filtered_list[i])

                        string_result += f"{result_list}{filtered_list[i]}"
                        if i != len(filtered_list) - 1: string_result += " + "
                        
                        total_result += result

            return f"**{total_result}** ⇐ {string_result}"
        else:
            if(validate_dice(clean_string)):
                result, result_list = roll_dice(clean_string)
                return f"**{result}** ⇐ {result_list}{clean_string}"

        return f":hot_face: Não consegui entender seu comando..."
    except:
        return f":gorilla: Seu comando foi Buro..."