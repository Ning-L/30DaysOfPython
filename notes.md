Following the 30 days of Python challenge: https://github.com/Asabeneh/30-Days-Of-Python

# Day 1: Data types

Difference between `list`, `set` and `tuple`:

| Feature         | List                            | Set                            | Tuple                            |
|:---------------:|:-------------------------------:|:------------------------------:|:--------------------------------:|
| **Mutability**  | Mutable (add/remove/change)     | Mutable (for adding/removing)  | Immutable                        |
| **Ordered**     | Ordered                         | Unordered                      | Ordered                          |
| **Duplicates**  | Allows duplicates               | Does not allow duplicates      | Allows duplicates                |
| **Syntax**      | Square brackets `[ ]`           | Curly braces `{ }` or `set()`  | Parentheses `( )`                |
| **Example**     | `my_list = [1, 2, 3, 'hello']`  | `my_set = {1, 2, 3, 'hello'}`  | `my_tuple = (1, 2, 3, 'hello')`  |
| **Use Cases**   | Mutable sequences (tasks list)  | Uniqueness checking (IDs)      | Immutable sequences (coords)     |

Typical use cases for each data structure:
  - **List**: Useful for managing ordered collections where elements can be modified, such as to-do lists.
  - **Set**: Ideal for ensuring uniqueness in collections, like managing unique user IDs or email addresses.
  - **Tuple**: Suitable for storing constant data that should not change after creation, such as geographic coordinates or configuration settings.


# Day 2

## Built-in functions

Docs for built-in functions: https://docs.python.org/3.9/library/functions.html

The corresponding R functions for the the most commonly used Python built-in functions:

| Python Function | Description                     | Corresponding R Function        |
|:---------------:|:-------------------------------:|:-------------------------------:|
| `print()`       | Prints output to the console    | `print()`                       |
| `len()`         | Returns the length of an object | `length()`                      |
| `type()`        | Returns the type of an object   | `typeof()` or `class()`         |
| `int()`         | Converts to an integer          | `as.integer()`                  |
| `float()`       | Converts to a float             | `as.numeric()`                  |
| `str()`         | Converts to a string            | `as.character()`                |
| `input()`       | Reads user input                | `readline(prompt = "")`         |
| `list()`        | Creates a list                  | `list()`                        |
| `dict()`        | Creates a dictionary            | `list()` (named elements)       |
| `min()`         | Returns the minimum value       | `min()`                         |
| `max()`         | Returns the maximum value       | `max()`                         |
| `sum()`         | Returns the sum of elements     | `sum()`                         |
| `sorted()`      | Returns a sorted list           | `sort()`                        |
| `open()`        | Opens a file                    | `file()`, `readLines()`, `write()` |
| `help()`        | Provides help/documentation     | `help()` or `?`                 |
| `dir()`         | Lists attributes of an object   | `ls()` for environment variables, `attributes()` for object attributes |

- **Dictionary Equivalent in R**: R doesn't have a direct equivalent of Python's dictionary. Instead, named lists or environments are often used for similar purposes.


The `zip()` is used to combine multiple iterable objects (such as lists, tuples, etc.) into tuples.
It creates an iterator that aggregates elements from each of the iterables.
The returned tuples contain elements from the input iterables that are at the same position.

```py
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped)) # output: [(1, 4), (2, 5), (3, 6)]
```

The `zip()` function stops creating tuples when the shortest input iterable is exhausted.
```py
list1 = [1, 2, 3, 4]
list2 = ['a', 'b']
zipped2 = zip(list1, list2)
print(list(zipped2))  # output: [(1, 'a'), (2, 'b')], stops at the shortest iterable
```

`zip()` in conjunction with the * operator can be used to unzip a list.
```py
x2, y2 = zip(*zipped)
x == list(x2) and y == list(y2)
```

## Variables

- Naming convention is snake_case.
- The assignment operator is `=`.
- Can declare multiple variables in one line: 
```py
first_name, last_name, age, city, is_married = "Dupont", "Grand", 30, "Paris", False
print("Name:", first_name, last_name, ",", age, "yrs old, married:",  is_married)
```
- Can take user input and assign to a variable:
```py
age = input("How old are you: ")
print(age)
```

## Data types

- When we do arithmetic operations string numbers should be first converted to int or float, otherwise error.
- When we concatenate a number with a string, the number should be first converted to a string, otherwise error.
- String can be converted into a list:
```py
list("ABCSOIFE") # output: ['A', 'B', 'C', 'S', 'O', 'I', 'F', 'E']
```

# Day 3: Operators

## Assignment

Python use `=` for assignment, combine other operator with `=` can do operation then directly assign the value,
for example:

```py
x += 3
# equals to
x = x + 3

x *= 3
# equals to
x = x * 3

x |= 3
# equals to
x = x | 3

x ^= 3
# equals 
x = x ^ 3

x >>= 3
# equals 
x = x >> 3
```

Attention:

- In Python, the **`^`** is the bitwise XOR (exclusive OR) operator.
The corresponding version in R is the function `bitwOr()`.

The bitwise XOR operator compares each bit of its operands.
If the corresponding bits of the operands are different, the resulting bit is set to 1.
If the corresponding bits are the same, the resulting bit is set to 0.
For example:

```py
a = 5  # in binary: 0101
b = 3  # in binary: 0011

result = a ^ b  # result will be 0110 in binary, wichi equals to 6

print(result)  # Output: 6
```

- The **`<<`** and **`>>`** are the bitwise left and right shift operators in Python.
The equivalent in R is `bitwShiftL()` and `bitwShiftR`.

## Comparison

Apart from the ordinary comparison operators such as `>`, `<`, `==`, `!=`,
Python uses also the following keywords for comparison:

* *is*: Returns `True` if both variables are (point to) the same object (`x is y`) (equivalent to `identical()` in R)
* *is not*: Returns `True` if both variables are not the same object (`x is not y`)
* *in*: Returns `True` if the queried list contains a certain item (`x in y`) (equivalent to `%in%` in R)
* *not in*: Returns `True` if the queried list doesn't have a certain item (`x in y`)

## Logical operators

| Python  |     R    |
|:-------:|:--------:|
| a and b | and & b  |
| a or b  | and \| b |
| not a   | ! a      |

# Day 4: Strings

## Creation

Multiline string can be created using triple double quote (""") or simple quote (''').
```py
long_string = """This is a very long string and I need to put it into
multiple line to finish the sentence otherwise
my eyes will be tired after read it haha.
"""
```

## Concatenation

Concatenate strings can be achieved by using the `+`.
```py
first_name = "Dupont"
middle_name = "Mickel"
last_name = "Grand"
full_name = first_name + ' ' + middle_name + ' ' + last_name
print(full_name)
```

## Formatting

### Old style using "%"

%s: string
%d: integers
%f: floating point numbers
%.number of digitsf: floating point numbers with a fixed precison

```py
## only strings
first_name, last_name, job = "Dupont", "Grand", "Gardener"
formatted_string = "I'm %s %s, my job is %s" %(first_name, last_name, job)
print(formatted_string)

viewed_notions = ['data types', 'vairables', 'operators']
print('The following are viewed python notions: %s' % (viewed_notions))

## strings and numbers
radius = 10
pi = 3.14159
area = pi * radius ** 2
print('The area of circle with a radius %d is %.2f.' %(radius, area))
```

### New style using str.format "{}"

```py
first_name, last_name, job = "Dupont", "Grand", "Gardener"
print("I'm {} {}, my job is {}. New one using string format {{}}".format(first_name, last_name, job))

viewed_notions = ['data types', 'vairables', 'operators']
print('The following are viewed python notions: %s' % (viewed_notions))

a = 4
b = 3
print('{} + {} = {}'.format(a, b, a + b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal

## strings and numbers
print('The area of circle with a radius {} is {:.1f}.'.format(radius, area))
```

### With string interpolation f-string (for Python 3.6+)

Strings start with f and we can inject the data in their corresponding positions.

```py
a = 4
b = 3
print(f'{a} + {b} = {a + b}')
print(f'{a} / {b} = {a / b:.2f}')
```

## Strings as sequences of characters

Python index starts from 0.

Use negative indexing if we want to start from right end.

```py
language = "Python"
language[0] # P
language[-2] # o

language[0:2] # slices the string from the start up to, but not including, index 2.
# or
language[:2]

language[3:6] # last 3 letters
# or
language[3:]
```

We can reverse a string as `language[::-1]`.

We can also skip characters while slicing, for example:
```py
letters = "abcdefghi"
letters[0:8:3] # slice from idx 0 to 9 and skip every 3 letters
```

## String methods

```py
challenge = 'thirty days of python'

## capitalize()
print(challenge.capitalize()) # 'Thirty days of python'

## count(substring, start = .., end = ..), count occurrences
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1 
print(challenge.count('th')) # 2`

## endwith()
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

## expandtabs(), replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

## find(), returns the index of the **first** occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
print(challenge.find('z')) # -1

## rfind(), returns the index of the **last** occurrence of a substring, if not found returns -1
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

## format(), see previous section

## index(), returns the **lowest** index of a substring,
# additional arguments indicate starting and ending index (default 0 and string length - 1). 
# If the substring is not found it raises a valueError.
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error, because we ask to start search from the 10th position
print(challenge.index(sub_string, 0, 9)) # ok, search between index 0 and 9
print(challenge.index(sub_string, 3)) # ok, search from the index 3

## rindex(), returns the **highest** index of a substring
example = 'abracadabra'
sub_string = 'abra'
print(example.index(sub_string))   # Output: 0 (first occurrence)
print(example.rindex(sub_string))  # Output: 7 (last occurrence)
```

P.S.: there's an error in the doc of day 4 [L376](https://github.com/Asabeneh/30-Days-Of-Python/blob/2f3a64c82fdca90f040f676d17aa6b0e430228ec/04_Day_Strings/04_strings.md?plain=1#L376),
the `print(challenge.rindex(sub_string))` should be 7 instead of 8.


```py
## isalnum(), checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = 'Thirty Days Python'
print(challenge.isalnum()) # False, space is not alphanumeric

## isalpha(), check if all elements belong to a-Z
"aa".isalpha() # True
"aa123".isalpha() # False
challenge.isalpha() # False, due to space

## isdecimal(), check if all elements belong to 0-9
challenge = '\u00B2'
challenge.isdecimal() # False

## isdigit(), check if all elements belong to 0-9 and other unicode characters for numbers
challenge = '\u00B2' # superscript 2
challenge.isdigit() # True

## isnumeric(), just like isdigit(), but accept more symbols
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False

```

Other examples:

| String   | `isdecimal()` | `isdigit()` | `isnumeric()` |
|:--------:|:-------------:|:-----------:|:-------------:|
| `123`    | `True`        | `True`      | `True`        |
| `123.45` | `False`       | `False`     | `False`       |
| `²`      | `False`       | `True`      | `True`        |
| `Ⅻ`     | `False`       | `False`     | `True`        |

```py
## isidentifier(), checks if a string is a valid variable name
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'TwoDaysOfPython'
print(challenge.isidentifier()) # True
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True

## islower(), checks if all alphabet characters in the string are lowercase
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

## isupper(), checks if all alphabet characters in the string are uppercase
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
challenge = 'Thirty days of python'
print(challenge.isupper()) # False

## join(), returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
result2 = '# '.join(web_tech)
print(result2) # 'HTML# CSS# JavaScript# React'

## strip(), removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))  # 'irty days of py'

### stey-by-step:
#### Stripping from the Beginning:
# The first character 't' is in 'noth', so it is removed.
# The next character 'h' is also in 'noth', so it is removed.
# The third character 'i' is not in 'noth', so stripping from the beginning stops here.
# At this point, the string becomes: 'irty days of pythoonnn'
#### Stripping from the End:
# The last character 'n' is in 'noth', so it is removed.
# The next character 'n' is also in 'noth', so it is removed.
# The next character 'n' is also in 'noth', so it is removed.
# The next character 'o' is in 'noth', so it is removed.
# The next character 'o' is in 'noth', so it is removed.
# The next character 'p' is not in 'noth', so stripping from the end stops here.
# The resulting string becomes: 'irty days of py'

challenge = 'thirty days onon of pythoonnn'
print(challenge.strip('noth')) #  'irty days onon of py'

## lstrip() or rstrip() for removing from left or right

## replace(), replaces substring with a given string
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

## split(), splits the string, using given string or space as a separator
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

## title(), returns a title cased string
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

## swapcase(), converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

## startswith(), checks if string starts with the specified string
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
print(challenge.startswith('30')) # False
```

# Day 5: Lists

| Data Type   | Mutable?       | Ordered? | Unique Elements? | Example                  |
|:-----------:|:--------------:|:--------:|:----------------:|:------------------------:|
| **List**    | Yes            | Yes      | Can contain duplicates | `['apple', 'banana', 'cherry']` |
| **Set**     | Yes            | No       | Unique elements only    | `{'apple', 'banana', 'cherry'}` |
| **Tuple**   |  No (Immutable) | Yes      | Can contain duplicates | `('apple', 'banana', 'cherry')` |
| **Dictionary** | Yes            | No       | Keys must be unique    | `{'apple': 'red', 'banana': 'yellow'}` |

A list can be empty or may have different data type items.

## Creation

```py
## init an empty list
empty_list = list() # use built-in fct
empty_list = [] # use square brackets

## list with different data type
lst = ["Dupont", 25, True, {"country": "France", "city": "Paris"}]
```

## Accessing items

Using index, which starts from **0** in case of using positive indexing.
We can also use negative indexing, where `-1` indicates the last item.

## Unpacking list items

Use the `*`:

```py
first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
```

## Slicing items

```py
## positive idx: lst[start(inclusive):end(exclusive):step]
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index, until the 3rd but not included
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
[1,2,3,4,5,6,7,8,9,10][1:7:2] # [2, 4, 6], from idx1 (2) to idx7 (8), every 2 step, and left side not included

## negative idx: lst[start:end:step]
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index, ['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
```

## Checking existance of list items

Use `in` operator.

```py
"lime" in fruits # False
"banana" in fruits # True
```

## Modifying items of a list

* Use the assignment of new values to modify items

```py
fruits[1:3] = ["a", "b"] # ['banana', 'a', 'b', 'lemon']
```

* Adding

Use the method `append()`

```py
fruits.append("apple")
print(fruits) # ['banana', 'a', 'b', 'lemon', 'apple']

fruits.append(['apple pie', 'peach']) #  only allow to add a single element, so stored as a list in the list
fruits.extend(["c", "d"]) # extend() allows to add multiple items at once
## or using extend() with a set or a tuple
```

P.S.: Python's extend() method is designed to concatenate elements to the end of a list,
regardless of the type of iterable used (list, tuple, or set).

* Inserting

Use method `insert(idx, item)` to insert a single element at a specified index of a list.

```py
fruits.insert(2, 'watermelon')
```

* Removing

1. Use method `remove(item)` to remove a specified item.

```py
fruits.remove('watermelon')
fruits.remove('c') # only remove the 1st occurrence

# Remove "banana" and "lemon" at once
fruits = [item for item in fruits if item not in ["banana", "lemon"]]
# Remove all occurrences of "d"
fruits = [item for item in fruits if item != 'd']
```

2. Use method `pop(idx)` to remove a specified item,
the last item will be removed if no index specified.

```py
fruits.pop(1)
fruits.pop() # last item removed
```

3. Use the keyword `del` can delete a item of a specified index,
items within index range, or delete the whole list.

```py
del fruits[0]
del fruits[:3]
del fruits
```

4. Emptying the list with the `clear()` method

```py
fruits.clear()
```

## Copying a list

1. by reassigning a list to a new variable: `list2 = list2`,
`list2` is now a reference of `list1`, the modification on `list2` will affect also `list1`.

2. use the `copy()` method

```py
lst = ['item1', 'item2']
lst2 = lst
lst2.remove("item1") 
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

## Joining lists

1. Use `+` operator, list3 = list1 + list2
2. Use the `extend()` method, list1.extend(list2)

## Counting items in a list

Use the `count()` method to return the number of times an item appears in a list.

```py
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24)) # 3
```

## Finding index of an item

The `index()` method returns the index of an item in the list:

```py
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24)) # 2, the 1st occurrence
```

## Reversing a list

Use the method `reverse()`, list1.reverse()

## Sorting items

Use the method `sort(reverse=False)` or the built-in function `sorted(reverse=False)`.
By default, both ways order the list in ascending order,
the method `sort()` will modify the original list. 

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits) # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse = True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
```

