# Day 10: 30 Days of python programming

# Exercises: Level 1

# 1.Iterate 0 to 10 using for loop, do the same using while loop.
## for loop
for i in range(11):
    print(i)

## while loop
i = 0
while i < 11:
    print(i)
    i = i + 1


# 2.Iterate 10 to 0 using for loop, do the same using while loop.
## for loop
for i in range(10, -1, -1):
    print(i)

## while loop
i = 10
while i >= 0:
    print(i)
    i = i - 1


# 3.Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

for i in range(7):
    print("#" * (i + 1)) # use the `*` operator to repeat character


# 4.Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for i in range(8): # in rows
    for j in range(8): # in columns
        print("#", end = " ") # string appended after the last value, default is a newline
    print() # Move to the next line after printing all columns in a row


# 5.Print the following pattern:

## 0 x 0 = 0
## 1 x 1 = 1
## 2 x 2 = 4
## 3 x 3 = 9
## 4 x 4 = 16
## 5 x 5 = 25
## 6 x 6 = 36
## 7 x 7 = 49
## 8 x 8 = 64
## 9 x 9 = 81
## 10 x 10 = 100

for i in range(11):
    print(f"{i} x {i} = {i*i}")


# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in range(len(skills)):
    print(skills[i])
## or iterate directly in the list
for i in skills:
    print(i)


# 7.Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)


# 8.Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 == 1:
        print(i)


# Exercises: Level 2

# 1.Use for loop to iterate from 0 to 100 and print the sum of all numbers.
## The sum of all numbers is 5050.
total = 0
for i in range(101):
    total = total + i
print("The sum of all numbers is", total)


# 2.Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
## The sum of all evens is 2550. And the sum of all odds is 2500.
total_odds, total_even = 0, 0
for i in range(101):
    if i % 2 == 0:
        total_even = total_even + i
    else:
        total_odds = total_odds + i
print("The sum of all evens is", total_even)
print("The sum of all odds is", total_odds)


# Exercises: Level 3

# 1. Go to the data folder and use the countries.py file (in day5 folder).
# Loop through the countries and extract all the countries containing the word land.
from countries import countries

countries_with_land = []
for i in countries:
    if i.find("land") != -1:
        countries_with_land.append(i)
print("Here are the countries containing the word land:", countries_with_land)


# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruit_lst = ['banana', 'orange', 'mango', 'lemon']
fruit_reorder = []
for i in range(len(fruit_lst)):
    fruit_reorder.append(fruit_lst[-1 - i])
print(fruit_reorder)
fruit_reorder == fruit_lst[::-1] # True


# 3. Go to the data folder and use the countries_data.py file.
import os
# path to data file
countries_data_path = os.path.abspath(os.getcwd() + "/countries_data.py")
os.path.exists(countries_data_path) # check existance
# read the list from file
with open(countries_data_path) as f:
    countries_data = eval(f.read())

## countries_data.py contains a list of dictionaries for 250 countries.
len(countries_data)

## 3-1.What are the total number of languages in the data
unique_lang = set()
for country_i in countries_data:
    # languages = country_i["languages"]
    languages = country_i.get("languages") # use get method to avoid error if key not exist in dictionary
    unique_lang.update(languages) # use update to add multiple items at once
print("The total number of languages in the data is :", len(unique_lang))


## 3-2.Find the ten most spoken languages from the data
### a) get all languages
all_lan = list()
for country_i in countries_data:
    languages = country_i.get("languages")
    all_lan.extend(languages)
### b) count occurrence
tab_occu = dict()
for lang_i in unique_lang:
    lang_count = all_lan.count(lang_i)
    tab_occu[lang_i] = lang_count
### c) the ten most spoken languages
# tab_occu.items() change dictionary to a list of tuples
# sorted(tab_occu.items(), reverse = True) # this sort by the 1st element of tuples
order_by_counts = sorted(tab_occu.items(), key = lambda x: x[1], reverse = True)
# `lambda x: x[1]` creates an anonymous function (lambda function) that takes one argument x and returns x[1].
# here: `x` represent each tuple `(key, value)`, x[1] gives access to the "value" in the tuple, which we want to sort by.
# if we change to x[0], it sorts by the 1st element "key" of tuple, just as we do not specify custom key
print(
    "The ten most spoken languages are:",
    [item[0] for item in order_by_counts[:10]] # extract 1st item for the top 10 and build a list
)

top_keys = [item[0] for item in order_by_counts[:10]]
## equals to:
top_keys = []
for item in order_by_counts[:10]:
    top_keys.append(item[0])
print(top_keys)


## or iterate through each country and count languages (give same results as step a+b):
languages_count = {}

for country_i in countries_data:
    languages = country_i.get("languages")
    for language_i in languages:
        if language_i in languages_count:
            languages_count[language_i] += 1
        else:
            languages_count[language_i] = 1



## 3-3.Find the 10 most populated countries in the world
pop_data = []
for country in countries_data:
    pop_data.append({
        "name": country.get("name"),
        "population": country.get("population")
    }) # extract only name and pop for each country, store in a list
pop_data_sorted = sorted(pop_data, key=lambda x: x["population"], reverse=True)

my_countries = list()
for i in pop_data_sorted[:10]:
    my_countries.append(i["name"])
print("The 10 most populated countries in the world are:", my_countries)