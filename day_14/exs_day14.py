# Day 14: 30 Days of python programming

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Exercises: Level 1

## 1. Explain the difference between map, filter, and reduce.
'''
map: it applies a function to each item of an iterable (like a list), it returns the same number of results as the iterable
filter: applies function to each item of an iterable but only return items for which the function returns `True`
reduce: it takes a function and an iterable, cumulatively apply the function, reduce them to single value as output
'''

## 2. Explain the difference between higher order function, closure and decorator
'''
higher order function: function which takes one or more function as arguments,
 it can also return a function as the result of a funciton
closure: function which capture the the outer scope of the enclosing function.
  It retains access to the variables from that scope even after the outer function has finished executing.
decorator: it's a specific type of higher order function that allows us to modify the behavoir of another function
'''


## 3. Define a call function before map, filter or reduce, see examples.
def get_exp2(base):
    return base ** 2
map_res = list(map(get_exp2, numbers))
print(map_res)

def bigger50(nb):
    if nb >= 50:
        return True
    else: 
        return False 
filter_res = list(filter(bigger50, map_res))
print(filter_res)

import functools
def diff(x1, x2):
    return x1 - x2
functools.reduce(diff, filter_res)


## 4. Use for loop to print each country in the countries list.
for i in countries:
    print(i)


## 5. Use for to print each name in the names list.
for i in names:
    print(i)


## 6. Use for to print each number in the numbers list.
for i in numbers:
    print(i)


# Exercises: Level 2
## 1. Use map to create a new list by changing each country to uppercase in the countries list
list(map(str.upper, countries))


## 2. Use map to create a new list by changing each number to its square in the numbers list
def square(i):
    return i ** 2
list(map(square, numbers))
## or
list(map(lambda x: x**2, numbers))

## 3. Use map to change each name to uppercase in the names list
list(map(str.upper, names))


## 4. Use filter to filter out countries containing 'land'.
def detect_land(i):
    return i.find("land") != -1

list(filter(detect_land, countries))
## or
list(filter(lambda x: x.find("land") != -1, countries))
## or
list(filter(lambda x: "land" in x, countries))


## 5. Use filter to filter out countries having exactly six characters.
list(filter(lambda x: len(x) == 6, countries))


## 6. Use filter to filter out countries containing six letters and more in the country list.
list(filter(lambda x: len(x) >= 6, countries))


## 7. Use filter to filter out countries starting with an 'E'
list(filter(lambda x: x.startswith("E"), countries))


## 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
from functools import reduce

lst = list(range(1, 6))

squared = map(lambda x: x ** 2, lst) # [1, 4, 9, 16, 25]
filtered = filter(lambda x: x > 10, squared) # [16, 25]
result = reduce(lambda x, y: x + y, filtered)
print(result) # 41


## 9. Declare a function called "get_string_lists" which
#  takes a list as a parameter and then
#  returns a list containing only string items.
my_lst = [42, 3.14, "Hello", [1, 2, 3], {"key": "value"}, (1, 2, 3)]

def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

get_string_lists(my_lst)


## 10. Use reduce to sum all the numbers in the numbers list.
reduce(lambda x, y: x + y, numbers)


## 11. Use reduce to concatenate all the countries and
#  to produce this sentence: "Estonia, Finland, Sweden, Denmark,
#  Norway, and Iceland are north European countries"
reduce(lambda x, y: f"{x}, {y}", countries[:-1]) + " and " + countries[-1] + " are north European countries"


## 12. Declare a function called "categorize_countries" that
#  returns a list of countries with some common pattern
#  (you can find the countries list in this repository
#  as countries.js(eg 'land', 'ia', 'island', 'stan')).
from countries import countries

def categorize_countries(lst, pattern):
    return [i for i in countries if pattern in i]

countries_with_land = categorize_countries(countries, 'land')
countries_with_ia = categorize_countries(countries, 'ia')
countries_with_island = categorize_countries(countries, 'island')
countries_with_stan = categorize_countries(countries, 'stan')

print("Countries with 'land':", countries_with_land)
print("Countries with 'ia':", countries_with_ia)
print("Countries with 'island':", countries_with_island)
print("Countries with 'stan':", countries_with_stan)

## 13. Create a function returning a dictionary,
#  where keys stand for starting letters of countries and
#  values are the number of country names starting with that letter.
from string import ascii_uppercase

def dict_country(lst):
    return {letter: len(list(filter(lambda x: x.startswith(letter), lst))) for letter in ascii_uppercase}

dict_country(countries)

# or combine to list then zip them to a dict
def dict_country2(lst):
    values = [len(list(filter(lambda x: x.startswith(letter), lst))) for letter in ascii_uppercase ]
    keys = list(ascii_uppercase)
    return {k: v for k, v in zip(keys, values)}

dict_country2(countries)


## 14. Declare a "get_first_ten_countries" function -
#  it returns a list of first ten countries from the countries.js list
#  in the data folder.
def get_first_ten_countries(lst):
    return lst[:10]

get_first_ten_countries(countries)


## 15. Declare a "get_last_ten_countries" function that
#  returns the last ten countries in the countries list.
def get_last_ten_countries(lst):
    return lst[-10:]

get_last_ten_countries(countries)


# Exercises: Level 3

## 1. Use the countries_data.py file and follow the tasks below:
import os

# path to data file
countries_data_path = os.path.abspath(os.getcwd() + "/countries_data.py")
# os.path.exists(countries_data_path) # check existance

# read the list from file
with open(countries_data_path) as f:
    countries_data = eval(f.read())

    ## 1-1. Sort countries by name, by capital, by population
sorted_by_name = sorted(countries_data, key = lambda x: x["name"])
sorted_by_capital = sorted(countries_data, key = lambda x: x["capital"])
sorted_by_population = sorted(countries_data, key = lambda x: x["population"])


    ## 1-2. Sort out the ten most spoken languages by location.
lang_count = {}
for country in countries_data:
    languages = country.get("languages")
    for i in languages:
        if i in lang_count: # if already exist in count dict, incredit 1
            lang_count[i] += 1
        else:
            lang_count[i] = 1 # otherwise, create a new key for the lang and affect to 1

ten_most_lang = sorted(lang_count.items(), key = lambda x: x[1], reverse = True)[:10]
print(
    "The ten most spoken languages are: ",
    [item[0] for item in ten_most_lang]
)

    ## 1-3. Sort out the ten most populated countries.
pop_sorted = sorted(countries_data, key = lambda x: x["population"], reverse = True)
print(
    "The ten most populated countries are: ",
    [item["name"] for item in pop_sorted[:10]]
)
## or
pop_list = [{country.get("name"): country.get("population")} for country in countries_data]
pop_sorted = sorted(pop_list, key = lambda x: list(x.values()), reverse = True)
print(
    "The ten most populated countries are: ",
    [list(item.keys())[0] for item in pop_sorted[:10]]
)
