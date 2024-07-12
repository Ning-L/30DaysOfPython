# Day 12: 30 Days of python programming

# Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
  ## print(random_user_id());
  ## '1ee33d'

import random
import string

def random_user_id():
    choice_pool = string.ascii_letters + string.digits # all alpha numeric characters
    user_id = ''.join([random.choice(choice_pool) for i in range(6)]) # concatenate characters
    return user_id
random_user_id()


# 2. Modify the previous task. Declare a function named user_id_gen_by_user.
#  It doesn’t take any parameters but it takes two inputs using input().
#  One of the inputs is the number of characters and 
# the second input is the number of IDs which are supposed to be generated.
## print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

## print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    nb_char = int(input("Number of characters: "))
    nb_ids = int(input("Number of IDs needed: "))
    choice_pool = string.ascii_letters + string.digits # all alpha numeric characters
    for n in range(nb_ids):
        user_id = ''.join([random.choice(choice_pool) for i in range(nb_char)]) # concatenate characters
        print(user_id)
user_id_gen_by_user() # 5 5
user_id_gen_by_user() # 16 5


# 3. Write a function named rgb_color_gen.
#  It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
from random import randint
def rgb_color_gen():
    rgb = [randint(0, 255) for i in range(3)]
    return f"rgb({rgb[0]},{rgb[1]},{rgb[2]})"
rgb_color_gen()


# Exercises: Level 2

# 1. Write a function list_of_hexa_colors which returns
#  any number of hexadecimal colors in an array
#  (six hexadecimal numbers written after #.
#  Hexadecimal numeral system is made out of 16 symbols,
#  0-9 and first 6 letters of the alphabet, a-f.
#  Check the task 6 for output examples).
import string
import random
def list_of_hexa_colors():
    pool = string.digits + string.ascii_lowercase[0:6]
    hexa = "#" + "".join([random.choice(pool) for i in range(6)])
    return hexa
list_of_hexa_colors()


# 2. Write a function list_of_rgb_colors which returns any number of
#  RGB colors in an array.
from random import randint
def list_of_rgb_colors():
    rgb = [random.randint(0, 255) for i in range(3)]
    return rgb
list_of_rgb_colors()


# 3.Write a function generate_colors which can generate any number
#  of hexa or rgb colors.
   ## generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   ## generate_colors('hexa', 1) # ['#b334ef']
   ## generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   ## generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
def generate_colors(color_type, nb):
    if color_type == "hexa":
        return [list_of_hexa_colors() for i in range(nb)]
    elif color_type == "rgb":
        return [rgb_color_gen() for i in range(nb)]
    else:
        return "color type should be either 'rgb' or 'hexa'!"
    
generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)
generate_colors('rbg', 1)


# Exercises: Level 3

# 1. Call your function shuffle_list, it takes a list as a parameter
#  and it returns a shuffled list
from random import shuffle
def shuffle_list(lst):
    shuffled_list = lst.copy() # make a copy of orignal list to avoid modifying
    shuffle(shuffled_list)
    return shuffled_list
shuffle_list([1, 3, 5, "a"])   


# 2. Write a function which returns an array of seven random numbers in a range of 0-9.
#  All the numbers must be unique.
from random import sample
def unique_seven():
    return sample(range(9), 7)
unique_seven()
