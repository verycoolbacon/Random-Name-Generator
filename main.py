import random
import string

# main function start

def letter_gen(amount):
    func_list = string.ascii_lowercase
    temp = []
    if amount in ("r","R"):
        amount = random.randint(1,10)
    else:
        amount = amount
    for _ in range(0,int(amount),1):
        temp.append(random.choice(func_list))
    result = "".join(temp)
    return result

def num_gen(amount):
    func_list = "0123456789"
    temp = []
    if amount in ("r","R"):
        amount = random.randint(1,10)
    else:
        amount = amount
    for _ in range(0,int(amount),1):
        temp.append(random.choice(func_list))
    result = "".join(temp)
    return result

def symbol_gen(amount):
    func_list = "!@#$%^&*()_+=[]"
    temp = []
    if amount in ("r","R"):
        amount = random.randint(1,10)
    else:
        amount = amount
    for _ in range(0,int(amount),1):
        temp.append(random.choice(func_list))
    result = "".join(temp)
    return result

# main function end

# main asking script start

letter_gen_input = input("Enter amount of letters. R for random: ")
while True:
    try:
        letter_gen_output = letter_gen(letter_gen_input)
        break
    except ValueError:
        letter_gen_input = input("Please enter any number or R for amounts of letters: ")

num_gen_input = input("Enter amount of numbers. R for random: ")
while True:
    try:
        num_gen_output = num_gen(num_gen_input)
        break
    except ValueError:
        num_gen_input = input("Please enter any number or R for amounts of numbers: ")

random_upper_choice = input("Randomize upper charaters? [y/n] ")
symbol_gen_choice = input("Generate random symbols? [y/n] ")

# main asking script end

# random uppercase choice

if random_upper_choice in ("y","Y"):
    temp_letters = []
    randomized_upper = ""
    for char in letter_gen_output:
        upper_or_lower_var = random.randint(0,1)
        if upper_or_lower_var == 1:
            temp_letters.append(char.upper())
        else:
            temp_letters.append(char)
    randomized_upper = "".join(temp_letters)
else:
    randomized_upper = letter_gen_output

# symbol generator choice

if symbol_gen_choice in ("y","Y"):
    symbol_gen_input = input("Enter amount of symbols. R for random: ")
    while True:
        try:
            symbol_gen_output = symbol_gen(symbol_gen_input)
            break
        except ValueError:
            symbol_gen_input = input("Please enter any number or R for amounts of symbols: ")
else:
    symbol_gen_output = ""

# final answer output
print(num_gen_output+randomized_upper+symbol_gen_output)
# this script is made by verycoolbacon
