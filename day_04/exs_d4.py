# Day 4: 30 Days of python programming

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
to_concate = ['Thirty', 'Days', 'Of', 'Python']
result = ' '.join(to_concate)
print(result)

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
to_concate = ['Coding', 'For' , 'All']
result = ' '.join(to_concate)
print(result)

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using `print()`.
print(company)

# 5. Print the length of the company string using `len()` method and `print()`.
print(len(company))

# 6. Change all the characters to uppercase letters using `upper()` method.
print(company.upper())

# 7. Change all the characters to lowercase letters using `lower()` method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string `Coding For All`.
my_string = "Coding For All"
my_string.capitalize()
my_string.title()
my_string.swapcase()

# 9. Cut(slice) out the first word of `Coding For All` string.
my_string[7:]

# 10. Check if `Coding For All` string contains a word "Coding" using the method index, find or other methods.
my_string.index("Coding")
my_string.find("Coding")

# 11. Replace the word coding in the string 'Coding For All' to Python.
my_string.replace("Coding", "Python")

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
my_string.replace("All", "Everyone")

# 13. Split the string 'Coding For All' using space as the separator (split()).
my_string.split(" ")

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", ")

# 15. What is the character at index 0 in the string `Coding For All`.
my_string[0] # C

# 16. What is the last index of the string `Coding For All`.
len(my_string) - 1 # 13

# 17. What character is at index 10 in "Coding For All" string.
my_string[10] # a space

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = 'Python For Everyone'
name.split()[0][0] + name.split()[1][0] + name.split()[2][0] # PFE

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
name = 'Coding For All'
name.split()[0][0] + name.split()[1][0] + name.split()[2][0] # CFA

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does '\'Coding For All' start with a substring `Coding`?
# 29. Does 'Coding For All' end with a substring `coding`?
# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
# 31. Which one of the following variables return True when we use the method isidentifier():
    ## - 30DaysOfPython
    ## - thirty_days_of_python
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# 33. Use the new line escape sequence to separate the following sentences.
    ## ```py
    ## I am enjoying this challenge.
    ## I just wonder what is next.
    ## ```
# 34. Use a tab escape sequence to write the following lines.
    ## ```py
    ## ge     Country   City
    ## 50     Finland   Helsinki
    ## ```
# 35. Use the string formatting method to display the following:
    ## ```sh
    ## radius = 10
    ## area = 3.14 * radius ** 2
    ## The area of a circle with radius 10 is 314 meters square.
    ## ```

# 36. Make the following using string formatting methods:
    ## ```sh
    ## 8 + 6 = 14
    ## 8 - 6 = 2
    ## 8 * 6 = 48
    ## 8 / 6 = 1.33
    ## 8 % 6 = 2
    ## 8 // 6 = 1
    ## 8 ** 6 = 262144
    ## ```