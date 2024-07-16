# Day 11: 30 Days of python programming

# Exercises: Level 1

# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2
add_two_numbers(1, 10)


# 2. Area of a circle is calculated as follows: area = π x r x r.
#  Write a function that calculates area_of_circle.
def area_of_circle(radium):
    return 3.14 * radium ** 2
area_of_circle(3)


# 3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
#  Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for i in args:
        if isinstance(i, (int, float)):
            total = total + i
        else: print(i, "is not a number and is excluded in addition.")
    return total
add_all_nums(1, 2, 3, 5)
add_all_nums(1, 2, 3, 5, "hello")


# 4. Temperature in °C can be converted to °F using this formula:
#  °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    print(f"The corresponding fahrenheit is {celsius * 9/5 + 32}")
convert_celsius_to_fahrenheit(25)


# 5. Write a function called check-season, it takes a month parameter and
#  returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in [9, 10, 11]:
        return "Autumn"
    elif month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else: print("Month should be any number between 1 and 12.")
check_season(3)
check_season(7)

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    print(f"The slope is {(y2 - y1)/(x2 - x1)}")
calculate_slope(1, 2, 3, 4)
                
# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0.
#  Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
import math
def solve_quadratic_eqn(a, b, c):
    """
    Args:
    - a (float or int): Coefficient of x^2.
    - b (float or int): Coefficient of x.
    - c (float or int): Constant term.

    x = (-b +/- sqrt(b^2 - 4ac))2a
    """
    sol1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    sol2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    return (sol1, sol2)
solve_quadratic_eqn(9, 6, 1)


# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)
print_list([1, 2, 3, "hello"])


# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
## print(reverse_list([1, 2, 3, 4, 5]))
### [5, 4, 3, 2, 1]
## print(reverse_list1(["A", "B", "C"]))
### ["C", "B", "A"]
def reverse_list(lst):
    out_list = []
    for i in range(len(lst)):
        out_list.append(lst[-1-i])
    return out_list
reverse_list([1, 2, 3, 4, 5])
reverse_list(["A", "B", "C"])


# 10. Declare a function named capitalize_list_items.
#  It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    out_lst = []
    for i in lst:
        out_lst.append(i.capitalize())
    return out_lst
capitalize_list_items(["apple", "banana", "peach"])


# 11. Declare a function named add_item. It takes a list and an item parameters.
#  It returns a list with the item added at the end.
## food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
## print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
## numbers = [2, 3, 7, 9];
## print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(lst, item):
    lst.append(item)
    return lst
add_item(lst = ['Potato', 'Tomato', 'Mango', 'Milk'], item = 'Meat')
add_item(lst = [2, 3, 7, 9], item = 5)


# 12. Declare a function named remove_item. It takes a list and an item parameters.
#  It returns a list with the item removed from it.
## food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
## print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
## numbers = [2, 3, 7, 9];
## print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst, item):
    lst.remove(item)
    return lst
remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], "Mango")
remove_item([2, 3, 7, 9], 3)


# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
## print(sum_of_numbers(5))  # 15
## print(sum_all_numbers(10)) # 55
## print(sum_all_numbers(100)) # 5050
def sum_of_numbers(nb):
    out = 0
    for i in range(nb + 1):
        out += i
    return out
sum_of_numbers(5)
sum_of_numbers(10)
sum_of_numbers(100)


# 14. Declare a function named sum_of_odds.
#  It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(nb):
    out = 0
    for i in range(nb + 1):
        if i % 2 == 1: 
            out += i
        else: print(f"skip {i} which is an even number.")
    return out
sum_of_odds(10)

# 15. Declare a function named sum_of_even.
#  It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(nb):
    out = 0
    for i in range(nb + 1):
        if i % 2 == 0: 
            out += i
        else: print(f"skip {i} which is an odd number.")
    return out
sum_of_even(10)


# Exercises: Level 2

# 1. Declare a function named evens_and_odds .
#  It takes a positive integer as parameter and it counts number of evens and odds in the number.
    ## print(evens_and_odds(100))
    ### The number of odds are 50.
    ### The number of evens are 51.
def evens_and_odds(pos_nb):
    odds_ct, even_ct = 0, 0
    for i in range(pos_nb + 1):
        if i % 2 == 0:
            even_ct += 1
        else:
            odds_ct += 1
    print(f"The number of odds are {odds_ct}")
    print(f"The number of evens are {even_ct}")

evens_and_odds(100)

# 2.Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(nb):
    out = 1
    for i in range(1, nb + 1):
        out *= i
    return f"The factorial of {nb} is {out}"
factorial(4)
factorial(5)


# 3.Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(arg = ""):
    if arg == "":
        print("'arg' is empty")
    else:
        print("'arg' is not empty")
is_empty()
is_empty("ACE")


# 4.Write different functions which take lists. They should calculate_mean,
#  calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    return sum(lst)/len(lst)

calculate_mean([1, 2, 3, 4])

def calculate_median(lst):
    lst = sorted(lst) # order list just in case
    mid_pos = 0
    if len(lst) % 2 == 0:
        return (lst[int(len(lst) / 2 - 1)] + lst[int(len(lst) / 2)]) / 2
    else:
        return lst[int(len(lst) / 2)]

calculate_median([1, 2, 3, 4])
calculate_median([1, 2, 3])
calculate_median([1, 2, 3, 4, 5, 6])
calculate_median([1, 2, 3, 4, 5])
calculate_median([1, 7, 3, 4, 5])

def calculate_range(lst):
    lst = sorted(lst)
    return (min(lst), max(lst))
calculate_range([2, 3, 4, 5])
calculate_range([1, 7, 3, 4, 5])

def calculate_variance(lst):
    mean = calculate_mean(lst)
    diff_mean = []
    for i in lst:
        diff_mean.append((i - mean) ** 2)      # cumulate deviation from mean then sum in the next line
    variance = sum(diff_mean) / (len(lst) - 1) 
    return variance
calculate_variance([1, 7, 3, 4, 5])

def calculate_variance_bis(lst):
    mean = calculate_mean(lst)
    diff_mean_sum = 0
    for i in lst:
        diff_mean_sum += (i - mean) ** 2        # sum directly the deviation from mean
    variance = diff_mean_sum / (len(lst) - 1)
    return variance
calculate_variance_bis([1, 7, 3, 4, 5])

import math
def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
calculate_std([1, 7, 3, 4, 5])



# Exercises: Level 3

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    # Check if the number is less than 2
    if num <= 1:
        return False
    
    # Check for numbers 2 and 3 separately
    if num <= 3:
        return True
    
    # Check if the number is divisible by 2 or 3
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    # Check divisibility from 5 upwards to the square root of num
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    
    return True

# 2. Write a functions which checks if all items are unique in the list.
def check_unique(lst):
    my_set = set(lst)
    if len(my_set) < len(lst):
        return "There are duplicated items in the list"
    else:
        return "All items are unique."
    
check_unique([1, 2, 3, 4])
check_unique([1, 2, 3, 4, 3])


# 3. Write a function which checks if all the items of the list are of the same data type.
def check_dt_type(lst):
    dt_types = []
    for i in lst:
        dt_types.append(type(i))
    if dt_types.count(dt_types[0]) == len(lst):
        return "All items of the list are of the same data type."
    else:
        return "There are multiple data types in the list."
check_dt_type([1, 2, 3, 4])
check_dt_type([1, 2, 3, {4}])
check_dt_type([1, 2, "hello", {4}])


# 4. Write a function which check if provided variable is a valid python variable
import keyword

def is_valid_variable(variable):
    if not isinstance(variable, str):
        return False
    
    if not variable.isidentifier():
        return False
    
    if keyword.iskeyword(variable):
        return False
    
    return True

# 5. Go to the data folder and access the countries-data.py file.
import os
# path to data file
countries_data_path = os.path.abspath(os.getcwd() + "/countries_data.py")
os.path.exists(countries_data_path) # check existance
# read the list from file
with open(countries_data_path) as f:
    countries_data = eval(f.read())


# the data is a list of dictionaries
    ## 5-1.Create a function called the most_spoken_languages in the world.
    #  It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_languages(n_most):
    language_count = {} # init an empty dictionary to count each language
    for country in countries_data:
        languages = country.get("languages")
        for language in languages:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_count = sorted(language_count.items(), key = lambda x: x[1], reverse = True)
    return f"The {n_most} most spoken languages are: {[item[0] for item in sorted_count[:n_most]]}"
most_spoken_languages(10)
most_spoken_languages(20)


    ## 5-2.Create a function called the most_populated_countries.
    #  It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(n_most):
    pop_data = []
    for i in countries_data:
        pop_data.append({
            "name": i.get("name"),
            "population": i.get("population")
        })
    sorted_pop = sorted(pop_data, key=lambda x: x["population"], reverse=True)
    return f"The {n_most} most populated countries are: {[item['name'] for item in sorted_pop[:n_most]]}"

most_populated_countries(5)
most_populated_countries(10)
most_populated_countries(20)
