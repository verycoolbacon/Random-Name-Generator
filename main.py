# imports
import random
import string
import sys
# setting up variables
symbol_gen_var = False
random_upper_var = False
format_choice_var = False
shuffle_var = False
dev_mode_var = False
# function area start
# dev_mode
def dev_mode():
    global dev_mode_var
    global num_gen_output
    global symbol_gen_output
    global letter_gen_output
    dev_mode_var = True
    print("[DEBUG] dev mode enabled")
    letter_gen_output = letter_gen("R")
    num_gen_output = num_gen("R")
    symbol_gen_output = symbol_gen("R")
    print(f"""
{'='*45}
{"[DEBUG]".center(45)}
{'='*45}
    letter_gen = {letter_gen_output}
    number_gen = {num_gen_output}
    symble_gen = {symbol_gen_output}
    vaild_input 1 (should be error) = {vaild_input_for_gen("prompt_msg(test) ","error_msg(test) ")}
    vaild_input 2 (should be 123)= {vaild_input_for_gen(123,"error_msg(test) ")}
    randomize_upper = {randomize_upper_func(string.ascii_lowercase)}
    custom_format 1 (should be symbols) = {custom_format("S")}
    custom_format 2 (should be numbers) = {custom_format("N")}
    custom_format 3 (should be letters) = {custom_format("L")}
    shuffle_output = {shuffle_output(string.ascii_lowercase)}
{'='*45}
{"[DEBUG COMPLETE]".center(45)}
{'='*45}
""")
    sys.exit()
# dev mode end
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
    if dev_mode_var == True:
        user_input = prompt
    else:
        user_input = input(prompt)
    while True:
        try:
            if user_input in ("R","r"):
                return user_input
            elif user_input == "dev mode enable":
                dev_mode()
                return "R"
            else:
                int(user_input)
                return user_input
        except ValueError:
            if dev_mode_var == True:
                return error_msg
            else:
                user_input = input(error_msg)

def randomize_upper_func(debug_input):
    temp_letters = []
    # debug
    if dev_mode_var == True:
        for char in debug_input:
            upper_or_lower_var = random.randint(0, 1)
            if upper_or_lower_var == 1:
                temp_letters.append(char.upper())
            else:
                temp_letters.append(char)
    else:
    # normal
        for char in letter_gen_output:
            upper_or_lower_var = random.randint(0, 1)
            if upper_or_lower_var == 1:
                temp_letters.append(char.upper())
            else:
                temp_letters.append(char)

    return "".join(temp_letters)

def custom_format(pos):
    if dev_mode_var == True:
        answer = pos
    else:
        answer = input(f"\nEnter format. Current position {pos}. You can repeat.\nL for letters. N for numbers. S for symbols. [L/N/S] ")
    while True:
        if answer in ("l","L"):
            return letter_gen_output
        elif answer in ("n","N"):
            return num_gen_output
        elif answer in ("s","S"):
            return symbol_gen_output
        else:
            answer = input(f"Current position : {pos} Please enter L/N/S")

def shuffle_output(user_input):
    temp = list(user_input)
    random.shuffle(temp)
    result = "".join(temp)
    return result

def summary(final_answer):
    print(f"""

    Summary

    Symbol : {symbol_gen_var}
    Random uppercase : {random_upper_var}
    Custom format : {format_choice_var}
    Shuffled answer : {shuffle_var}

    Final answer : {final_answer}
    """)

# function area end
# dev mode

# main script start
letter_gen_output = letter_gen(vaild_input_for_gen("Enter amount of letters. R for random: ","Please enter any number or R: "))
num_gen_output = num_gen(vaild_input_for_gen("Enter amount of numbers. R for random: ","Please enter any number or R: "))

symbol_gen_choice = input("\nDo you want to generate symbols? [y/n] ")

# symbol gen choice check
if symbol_gen_choice in ("y","Y"):
    symbol_gen_var = True
    symbol_gen_output = symbol_gen(vaild_input_for_gen("Enter amount of symbols. R for random: ","Please enter any number or R: "))
else:
    symbol_gen_output = ""

####################################################################
#------------------------------------------------------------------#
#---> letter_gen_output = random_upper_output after this point <---#
#------------------------------------------------------------------#
####################################################################

random_upper_choice = input("\nDo you want random uppercase? [y/n] ")

# random upper case choice check
if random_upper_choice in ("y", "Y"):
    random_upper_var = True
    letter_gen_output = randomize_upper_func("")

format_choice = input("\nCurrent format: [Letter][Number][Symbol]\nDo you want to customize output format? [y/n] ")

# custom format choice check
if format_choice in ("y","Y"):
    format_choice_var = True
    first = custom_format(1)
    second = custom_format(2)
    third = custom_format(3)

else:
    first = letter_gen_output
    second = num_gen_output
    third = symbol_gen_output

# output shuffling
shuffle_choice = input("Do u want to shuffle the output? [y/n] ")

# final printing
if shuffle_choice in ("y","Y"):
    shuffle_var = True
    summary(shuffle_output(first + second + third))
else:
    summary(first + second + third)
