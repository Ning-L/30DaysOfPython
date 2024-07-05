# Day 2: 30 Days of python programming

# Exercises: Level 1

# 1. Inside 30DaysOfPython create a folder called day_2. 
# Inside this folder create a file named variables.py

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'

# 3. Declare a first name variable and assign a value to it
first_name = "Dave"

# 4. Declare a last name variable and assign a value to it
last_name = "Le Mignon"

# 5. Declare a full name variable and assign a value to it
full_name = "Stuart"

# 6. Declare a country variable and assign a value to it
country = "US"

# 7. Declare a city variable and assign a value to it
city = "Paris"

# 8. Declare an age variable and assign a value to it
age = 3

# 9. Declare a year variable and assign a value to it
year = 2024

# 10. Declare a variable is_married and assign a value to it
is_married = True

# 11. Declare a variable is_true and assign a value to it
is_true = False

# 12. Declare a variable is_light_on and assign a value to it
is_light_on = True

# 13. Declare multiple variable on one line
movie, on_time, company = "Minions", "10th July 2024", "Illumination"


# Exercises: Level 2

# 1. Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_true))
print(type(is_light_on))
print(type(movie))
print(type(on_time))
print(type(company))


# 2. Using the len() built-in function, find the length of your first name
print(len(first_name))

# 3. Compare the length of your first name and your last name
print(len(first_name) > len(last_name))

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

    # 4-1. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

    # 4-2. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

    # 4-3. Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

    # 4-4. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

    # 4-5. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainer = num_two % num_one

    # 4-6. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

    # 4-7. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# 5. The radius of a circle is 30 meters.
    # 5-1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
r = 30
area_of_circle = 3.14 * r**2

    # 5-2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * 3.14 * r

    # 5-3. Take radius as user input and calculate the area.
custom_radius = input("Give me a radius wanted:")
print("The area of the customized radius circle is:", 3.14 * int(custom_radius) ** 2)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Your first name:")
last_name = input("Your last name:")
country = input("Your country:")
age = input("Your age:")

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
