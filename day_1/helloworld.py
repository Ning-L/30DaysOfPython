# Exercise: Level 1

## 1. Check the python version you are using
# in bash terminal
# python3 --version
## when python shell opened 
import sys
print(sys.version)

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
print(3 + 4) # addition(+)
print(3 - 4) # subtraction(-)
print(3 * 4) # multiplication(*)
print(3 % 4) # modulus(%)
print(3 / 4) # division(/)
print(3 ** 4) # exponential(**)
print(3 // 4) # floor division operator(//)

# 3. Write strings on the python interactive shell. The strings are the following:
print("dupont") # Your name
print("Grand") # Your family name
print("UN") # Your country
print("I am enjoying 30 days of python") # I am enjoying 30 days of python

# 4.Check the data types of the following data:
print(type(10)) # 10, int
print(type(9.8)) # 9.8, float
print(type(3.14)) # 3.14, float
print(type(4 - 4j)) # 4 - 4j, complex
print(type(['Asabeneh', 'Python', 'Finland'])) # ['Asabeneh', 'Python', 'Finland'], list
print(type("dupont")) # Your name, str
print(type("Grand")) # Your family name, str
print(type("UN")) # Your country, str



# Exercise: Level 2

# Create a folder named day_1 inside 30DaysOfPython folder. 
# Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4.
# Remember to use print() when you are working on a python file. 
# Navigate to the directory where you have saved your file, and run it.


# Exercise: Level 3

# Write an example for different Python data types such as Number
# (Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.

integer_example = 42
float_example = 3.14
complex_example = 1 + 2j
string_example = "Hello, World!"
boolean_example = True
list_example = [1, 2, 3, "four", 5.0, True]
tuple_example = (1, 2, 3, "four", 5.0, True)
set_example = {1, 2, 3, 4, 5}
dictionary_example = {
    "name": "lili",
    "age": "23",
    "job": "gardener"
}

print("integer:", integer_example)
print("float:", float_example)
print("complex:", complex_example)
print("string:", string_example)
print("bloolean:", boolean_example)
print("list:", list_example)
print("tuple:", tuple_example)
print("set:", set_example)
print("dictionary:", dictionary_example)

# Find an Euclidian distance between (2, 3) and (10, 8)
(2 - 3) ** 2 + (10 - 8) **2
