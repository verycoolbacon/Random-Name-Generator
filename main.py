import random
import string
# setting up variables
symbol_gen_var = False
random_upper_var = False
format_choice_var = False
# function area start

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
    func_list = str(string.digits)
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
    func_list = "?!@#$%^&*()_+=[]"
    temp = []
    if amount in ("r","R"):
        amount = random.randint(1,10)
    else:
        amount = amount
    for _ in range(0,int(amount),1):
        temp.append(random.choice(func_list))
    result = "".join(temp)
    return result

def vaild_input_for_gen(prompt,error_msg):
    user_input = input(prompt)
    while True:
        try:
            if user_input in ("R","r"):
                return user_input
            else:
                int(user_input)
                return user_input
        except ValueError:
            user_input = input(error_msg)

def randomize_upper_func():
    temp_letters = []

    for char in letter_gen_output:
        upper_or_lower_var = random.randint(0, 1)

        if upper_or_lower_var == 1:
            temp_letters.append(char.upper())
        else:
            temp_letters.append(char)

    return "".join(temp_letters)

def custom_format(answer):
    pos = 1
    if answer in ("l","L"):
        pos += 1
        return letter_gen_output
    elif answer in ("n","N"):
        pos += 1
        return num_gen_output
    elif answer in ("s","S"):
        pos += 1
        return symbol_gen_output
    else:
        print("Invaild input")

# function area end

letter_gen_output = letter_gen(vaild_input_for_gen("Enter amount of letters. R for random: ","Please enter any number or R: "))
num_gen_output = num_gen(vaild_input_for_gen("Enter amount of numbers. R for random: ","Please enter any number or R: "))

symbol_gen_choice = input("\nDo you want to generate symbols? [y/n] ")

# symbol gen choice check
if symbol_gen_choice in ("y","Y"):
    symbol_gen_var = True
    symbol_gen_output = symbol_gen(vaild_input_for_gen("Enter amount of letters. R for random: ","Please enter any number or R: "))
else:
    symbol_gen_output = ""

#---> letter_gen_output = random_upper_output after this point <---#

random_upper_choice = input("\nDo you want random uppercase? [y/n] ")

# random upper case choice check
if random_upper_choice in ("y", "Y"):
    random_upper_var = True
    letter_gen_output = randomize_upper_func()

format_choice = input("\nCurrent format: [Letter][Number][Symbol]\nDo you want to customize output format? [y/n] ")

# custom format choice check
if format_choice in ("y","Y"):
    format_choice_var = True
    first = custom_format(input("\nEnter format. Current position 1. You can repeat.\nL for letters. N for numbers. S for symbols. [L/N/S] "))
    second = custom_format(input("\nEnter format. Current position 2. You can repeat.\nL for letters. N for numbers. S for symbols. [L/N/S] "))
    third = custom_format(input("\nEnter format. Current position 3. You can repeat.\nL for letters. N for numbers. S for symbols. [L/N/S] "))
    print(f"""

    Summary

    Symbol : {symbol_gen_var}
    Random uppercase : {random_upper_var}
    Custom format : {format_choice_var}

    Final answer : {first}{second}{third}

    """)
else:
    print(f"""

    Summary

    Symbol : {symbol_gen_var}
    Random uppercase : {random_upper_var}
    Custom format : {format_choice_var}

    Final answer : {letter_gen_output}{num_gen_output}{symbol_gen_output}
    
    """)

