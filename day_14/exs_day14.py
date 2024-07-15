# Day 14: 30 Days of python programming

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Exercises: Level 1

## 1. Explain the difference between map, filter, and reduce.
'''
map: it applies a function to each item of an iterable (like a list), it returns the same number of results as the iterable
filter: applies function to each item of an iterable but only return items for which the function returns `True`
reduce: it takes a function and an iterable,cumulatively apply the function, reduce them to single value as output
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
## 9. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
## 10. Use reduce to sum all the numbers in the numbers list.
## 11. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
## 12. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
## 13. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
## 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
## 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# Exercises: Level 3

## 1. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
## 2. Sort countries by name, by capital, by population
## 3. Sort out the ten most spoken languages by location.
## 4. Sort out the ten most populated countries.