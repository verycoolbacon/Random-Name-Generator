import random
def letter_gen(amount):
    func_list = "abcdefghijklmnopqrstuvwxyz"
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

letter_gen_input = input("Enter amount of letters. R for random: ")
num_gen_input = input("Enter amount of numbers. R for random: ")
letter_gen_output = letter_gen(letter_gen_input)
num_gen_output = num_gen(num_gen_input)

random_upper_choice = input("randomize upper charaters? [y/n] ")

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
print(num_gen_output+randomized_upper)
