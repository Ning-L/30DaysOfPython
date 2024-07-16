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

# Day 6: Tuples

Tuple is ordered and unchangeable, written with round brackets `()`.
The methods `add()`, `insert()` and `remove()` can not be used with tuples.

## Creation

Use `()` or `tuple()` to create an empty tuple.

```py
empty_tuple = ()
empty_tuple = tuple()

tpl = ("a", "b", "c") # init with values
```

## Length

Use built-in function `len()` to get the length of a tuple.

## Accessing

Similar to list, we can use positive or negative indexing.

* `count()`: to count occurrence of a speficied item
* `index()`: to find the index of a speficied item

## Slicing

Use a range of indexes (start and end) to slice out a sub-tuple.

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits[1:3] # ('orange', 'mango'), right side index exclusive
fruits[1:] # ('orange', 'mango', 'lemon')
fruits[-3:-1] # ('orange', 'mango'), item at index at the right is not included.
```

## Change tuple to list

Tuple is immutable, if we want to modify it, we should change it to a list and then change it back to tuple.

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

## Check an item in tuple

Use the `in` operator:

```py
"banana" in fruits
```

## Join tuples

Use the `+` operator to join more multiple tuples:

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

## Deleting tuples

Impossible to remove a single item as tuple is immutable, but we can delete the whole tuple with `del`:

```py
del fruits_and_vegetables
```

# Day 7: Sets

Set is unordered and un-indexed, set is used to store unique items, 
and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.

* Creation with the built-in function `set()` to create an empty set, and `{}` to initiate a set with values:

```py
my_set = set()
my_set = {"a", "b", "c"}
```

* Getting length with the built-in function `len()`.
* Accessing items in a set with loops to access itmes. See the loop section.
* Checking an item with the `in` operator.
* Adding items with `add()` or `update()` method.

```py
my_set.add("one item")
my_set.update(["one item", "two item"]) # update takes a list
```

* Removing items with `remove()` (raise error if item not found), `pop()` (remove a random item and return the removed item) or `discard()`

```py
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
removed_item = fruits.pop() # store the removed item in case we are interested in
```

* Clearing items of a set with `clear()` method.
* Deleting a set with the `del` statement.
* Converting: list and set can be converted to each other, set will remove duplicates and order is lost.

```py
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item1', 'item4', 'item3', 'item2'}
```

* Joining sets with `union()` or `update()` method.

```py
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

* Intersection: `st1.intersection(st2)`
* Subset or supperset: `st1.issubset(st2)`, `st1.issuperset(st2)`
* Difference: `st1.difference(st2)`
* Symmetric difference: `st1.symmetric_difference(st2)`, returns all items which exist only in one set.
* Check if two sets do not have any common item: `st2.isdisjoint(st1) `

# Day 8: Dictionaries

A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
The key should be unique.

* Creation with curly brackets `{}` or the built-in function `dict()`.
```py
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```
* Getting length with the `len()` function, it checks the number of 'key: value' pairs in the dictionary. 
* Accessing items via the key name: `dct["key1"]`. Can raise error if the key is not found.
We can use `get()` method to access items: `dct.get("keyXX")`, if key does not exist, it will return None, a NoneType object data type.
* Adding item should be a 'key: value' pair: `dct["key5"] = "value5"`
* Modifying items via the key:  `dct["key5"] = "value555"`
* Checking key with the `in` operator:  `"key5" in dct`
* Removing key: value pairs with `pop(key)`, `popitem()` or `del`
```py
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item (LIFO principle)
del dct['key2'] # removes key2 item
```
P.S.: 

- LIFO (Last-In, First-Out) order means that the most recently added element is the first one to be removed.
This principle is applied in the `popitem()` method of dictionaries in Python
- To determine the applicable data types for a given method, we can use:
  - `help()`, provides documentation about modules, functions, classes, and methods, ex: `help(list.append)`, `help(dict.popitem)`, `help(str.split)`;
  - `dir()`: lists all the attributes and methods of an object, ex: `dir(str)`
  - Check the [Python 3 doc](https://docs.python.org/3/)
  - Interactive inspection with the `__doc__` attribute, ex: `str.split.__doc__`, `list.append.__doc__`, etc.

* Chanage dictionary to list of tuples with the `items()` method: `dct.items()`
* Clearing a dictionary with the `clear()` method: `dct.clear()`
* Deleting a dictionary with `del` statement
* Copy a dictionary with `copy()` method
* Getting dictionary keys/values as a list with the `keys()`/`values()` method: `dct.keys()`, `dct.values()`.
We can do inverse, aka, build a dictionary based on two list: 
```py
my_keys = ['a', 'b', 'c']
my_values = [1, 2, 3]
# Create dictionary using zip() and dict()
my_dict = dict(zip(my_keys, my_values))
# Create dictionary using dictionary comprehension
my_dict = {k: v for k, v in zip(my_keys, my_values)}
## attention if lists with different length, zip() will stop pairing when the shortest list is exhausted
```

# Day 9: Conditionals

## `if` condition

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

## `if else`

```py
a = 3
if a > 0:
    print('A is a positive number')
else:
    print('A is not a positive number')
```

## `if elif else`

For more than two conditions, we can combine with `elif`.
```py
a = 3
if a > 0:
    print('A is a positive number')
elif a == 0:
    print("A is 0")
else:
    print('A is a negative number')
```

## Short hand

```py
code if condition else code # syntax

a = 3
print("A is 3") if a == 3 else print("A is not 3")
```

## Nested conditions

```py
# syntax
if condition:
    code
    if condition:
    code

a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

## `if` condition and Logical operators

* To avoid nested condition, we can write nested conditions by using logical operator `and`

```py
a = 0
if a > 0 and a % 2 == 0:
    print('A is a positive and even integer')
elif a > 0 and a % 2 !=  0:
    print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

* Combine the `or`

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

# Day 10: Loops

## `while` loop

Execute the code repeatedly while a given condition is satisfied,
when the condition becomes false, the codes after the loop will be continued.
```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
```

If we are interested to run block of code once the condition is no longer true, we can use else.
```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count) # execute this line when count is no longer <5
```

* Use `break` to get out of the loop.

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# only prints 0, 1, 2, when arrives at 3 it stops.
```

* Use `continue` to skip the current iteration and continue with the next.
```py
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
# only prints 0, 1, 2 and 4 (skips 3)
```

## `for` loop

`for` kiio iterates over a sequence (such as a list, tuple, string or range) and
executes a block of code for each item in the sequence.

```py
## with list
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)      # the numbers will be printed line by line, from 0 to 5

## with string
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

## with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

## with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)
# gives the keys of the dictionary

for key, value in person.items():
    print(key, value)
# this way we get both keys and values printed out

## with set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

* Use `break` when we like to stop our loop before it is completed.
```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
# loop stop when number gets to 3
```

* Use `continue` when we like to skip some of the steps in the iteration of the loop.
```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# standard 
for number in numbers:
    print(number)
    if number == 3:
        continue
    if number != 5: # will not be executed here when number is 3
        print('Next number should be', number + 1)
    else:
        print("loop's end")
print('outside the loop')

## 0
## Next number should be 1
## 1
## Next number should be 2
## 2
## Next number should be 3
## 3
## 4
## Next number should be 5
## 5
## loop's end
## outside the loop

# with a range(start,end,step), by default step is 1, need at least the argument "end"
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### Nested `for` loop

Write loops inside a loop.
```py
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill) # will print the skill one by one
```

### `for else`

Use `else` to execute something message when the loop ends.

```py
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

### `pass`

In python when statement is required (after semicolon),
but we don't like to execute any code there, we can write the word `pass` to avoid errors.
Also we can use it as a placeholder, for future statements.

```py
for number in range(6):
    pass
```

# Day 11: Functions

## Defining a function

Use the keyword `def` to declare a function, with or without parameters.
```py
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

## `return` in function
Function can return values, if it does not have a `return` statement, the value of the function is `None`.
We can return any kind of data types from a function.

```py
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

## Parameters
We can pass different data types(number, string, boolean, list, tuple, dictionary or set) as a parameter in a function.

```py
def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(current_year = 2021, birth_year = 1819))
```

We can pass default values to parameters.

By adding `*` before the parameter name, we can create a function which takes arbitrary number of arguments.
`*args` captures any additional positional arguments that are not explicitly defined.
```py
def generate_groups(team, leader, *args):
    print(team)
    print(f"Leader: {leader}")
    print("Members:")
    for i in args:
        print(i)
print(generate_groups('Team-1', 'Asabeneh', 'Brook', 'David', 'Eyob'))

# another example
def example_function(pos1, pos2, default1 = 10, *args, kwonly1, kwonly2 = 20, **kwargs):
    print(f"pos1: {pos1}")
    print(f"pos2: {pos2}")
    print(f"default1: {default1}")
    print(f"args: {args}")
    print(f"kwonly1: {kwonly1}")
    print(f"kwonly2: {kwonly2}")
    print(f"kwargs: {kwargs}")

# Calling the function with various arguments
example_function(1, 2, 3, 4, 5, kwonly1 = 'kw1', extra = 'extra')
# pos1: 1
# pos2: 2
# default1: 3
# args: (4, 5)
# kwonly1: kw1
# kwonly2: 20
# kwargs: {'extra': 'extra'}
```

We can also pass functions around as parameters, for ex:

```py
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

# Day 12: Modules

A module is a file containing a set of codes or a set of functions which can be included to an application.
A module could be a file containing a single variable, a function or a big code base.
Modules allow you to organize your code into separate files for better manageability and reuse.

Use the keyword `import` to import a module, need to prefix the module name before the function: `mymodule.generate_full_name()`
Combining with the keyword `from`, we can import the functions differently, we can use directly the function: `generate_full_name()`
We can use the keyword `as` to rename module's name while importing,
we can use the rename function directly: `fullname()`

* `os` module: to perform operating system tasks
```py
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

* `sys` module: manipulate different parts of the Python runtime environment
```py
## example script.py
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

```bash
python script.py Asabeneh 30DaysOfPython
```

```py
## other useful sys commands:
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

* `statistics` module: provides functions for mathematical statistics of numeric data.
```py
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

* `math` module: provides many mathematical operations and constants.

```py
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

It's possible to import multiple function at once:
```py
from math import pi, sqrt, pow, floor, ceil, log10
```

* `string` module:
```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

* `random` module: gives random number.
```py
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```

# Day 13: List comprehension & lambda function

## List comprehension

List comprehension is a compact way of creating a list from a sequence.
It's a short way to create new list and faster than processing a list using the `for` loop.

```py
## syntax
[i for i in iterable if expression]

# Examples
## string to list
language = 'Python'
lst = list(language) # use list()
[i for i in language] # use list comprehension

## generate a list of numbers
[i for i in range(10)] # generate numbers from 0 to 9

## do math operation during iteration
[i * 2 for i in range(5)] # [0, 2, 4, 6, 8]

## generate a list of tuple
[(i, i * i) for i in range(5)] # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

## combine with `if`
[i for i in range(21) if i % 2 == 0] # even number in range 0 to 21

nbs = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
[i for i in nbs if i % 2 == 0 and i > 0] # filter out positive even nb from a list, [4, 6, 8, 10]

## to flatten a list of lists
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[number for row in list_of_lists for number in row] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
### outer loop `for row in list_of_lists`, which sublist is being processed
### inner loop `for number in row`, extract each item from that sublist
### output: number
# The outer loop starts and picks the first row. (row 1 [1,2,3], row 2 [4,5,6], row 3 [7,8,9])
# The inner loop executes for every number in that row. for row 1, the 1st number is 1, 2nd is 2, 3rd is 3
# After the inner loop completes for the first row, the outer loop moves to the next row.
# This process repeats until all rows have been processed.

# using loop will be:
output = []
for row in list_of_lists:
    for number in row:
        output.append(number)

```

## Lambda function

Lambda function is a small anonymous function without a name.
It can take any number of arguments, but **can only have one expression**. 
We need it when we want to write an anonymous function inside another function.

Use the keyword `lambda` to create it.
Lambda function **does not use return** but it explicitly returns the expression.

```py
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2

# Examples
## Named function
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
## Lets change the above function to a lambda function
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

## Self invoking lambda function
(lambda a, b: a + b)(2,3) # 5 - need to encapsulate it in print() to see the result in the console

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

## Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22


# lambda functiton inside another function
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
```

## Dictionary comprehension

```py
# syntax
{key_expression: value_expression for item in iterable if condition}

# example:
numbers = [1, 2, 3, 4, 5]
squared_dict = {num: num**2 for num in numbers}
print(squared_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_squared_dict = {num: num**2 for num in numbers if num % 2 == 0}
print(even_squared_dict) # {2: 4, 4: 16}

```
# Day 14: Higer oder functions

In Python, following operations are allowed:

* A function can take one or more functions as parameters
* A function can be returned as a result of another function
* A function can be modified
* A function can be assigned to a variable

## Function as a parameters

```py
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

## Function as a returned value

```py
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

## Python closures

**/!\ not very clear, to review this notion**

Python allows a nested function to access the outer scope of the enclosing function. 

```py
def outer_function(x):
    def inner_function(y):
        return x + y  # `x` is captured from the outer function
    return inner_function

# Create a closure
closure = outer_function(10)

# When outer_function(10) is called, it returns the inner_function but retains the value of x (which is 10).

# Call the closure
result = closure(5)  # This adds 10 (from outer) and 5 (from inner)
# when closure(5) is called, it uses the captured value of x to compute 10 + 5. (y is 5)
print(result)  # Output: 15

```

## Python decorators

**/!\ not clear, to review this notion, why use it?**

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
Decorators are usually called before the definition of a function you want to decorate.

```py
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator # applying the decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# another example
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()
"""
Something is happening before the function is called.
Hello!
Something is happening after the function is called.
"""
```

Decorator can take paramters:
```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh", 'Finland')
```

## Built-in higher order functions

Some of the built-in higher order functions that we cover in this part are map(), filter, and reduce.
Lambda function can be passed as a parameter.

* `map()`

```py
# syntax
map(function, iterable)

# examples
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

numbers_squared = map(lambda x : x ** 2, numbers) # apply it with a lambda function
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]


names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# apply with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

* `filter()`

The filter() function calls the specified function which returns boolean
for each item of the specified iterable (list). It filters the items that satisfy the filtering criteria.

```py
# syntax
filter(function, iterable)

# example
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

list(map(is_even, numbers))     # [False, True, False, True, False]

```

* `reduce()`

The reduce() function is defined in the functools module and we should import it from this module.
Like map and filter it takes two parameters, a function and an iterable.
However, it does not return another iterable, instead it returns a single value.

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str) 
'''
The reduce function applies `add_two_nums` cumulatively to the items of `numbers_str`,
from left to right, so as to reduce the iterable to a single value.
'''
print(total)    # 15
```


# Day 15: Error types

* **SyntaxError** indicates that there is something wrong with the structure of your code:
    - missing colons `:`,
    - unmatched parentheses/brackets/quotes,
    - inproper indentation,
    - using reserved keywords (`def = 2`),
    - invalide characters (`print(3 @ 2)`), etc.

* **NameError** indicates that Python can't find a variable or function with the name you provided: 
    - using and undefined variable,
    - misspelling a variable name,
    - using a function before defining it,
    - incorrect scope (accessing a variable that is not in the global scope),
    - using non-existent imports, etc.

* **IndexError** indicates that you are trying to access an invalid index in a sequence:
    - accessing an index that is out of the range,
    - empty list access, etc.

* **ModuleNotFoundError** indicates that Python cannot locate the specified module:
    - incorrect module name,
    - module not installed,
    - using wrong Python environment,
    - module located in a different directory (without properly setting the Python path),
    - circular imports (when two or more modules attempt to import each other directly or indirectly, creating a loop in the import structure.), etc.

* **AttributeError** indicates that you're trying to access an attribute or method that does not exist on the object you're working with: 
    - accessing a non-existent attribute,
    - calling a non-existent method,
    - misspelling the attribute name,
    - accessing an attribute from a non-object (like a function or a module),
    - accessing attributes in inherited classes, etc.

* **KeyError** indicates that you're trying to access a key that does not exist in a dictionary:
    - accessing a non-existent/non-defined key,
    - accessing keys after deletion,
    - typos (case sensitive), etc.

* **TypeError** indicates that an operation was applied to an object of an inappropriate type:
    - unsupported operations (`'2' + 4`),
    - incorrect argument type (like expected number but input string),
    - calling an non-callable object (like string or number),
    - indexing with a non-integer type (`lst['1']`),
    - providing incorrect number of argument to a function, etc.

* **ImportError**  indicates that Python cannot find the specified module or object during the import process:
    - module not found,
    - incorrect module path,
    - circular import,
    - inporting non-existent function, etc.
    
* **ValueError** indicates that a function received an argument of the right type but an inappropriate value:
    - incorrect value for a function (like `int('12a')`),
    - out of range (like `import math; math.sqrt(-1)`),
    - invalide data conversion (like `float('a')`),
    - wrong shape or size (value that does not fit the expected shape or size for data structure, like lenght of 2 but operate 3 times, unpacking values for wrong nb of variables), etc.

* **ZeroDivisionError** indicates you are dividing a number by zero.


# Built-in Function vs. Method

* Built-in Function: A function that is provided by Python and can be used across different types of objects.
For example, `len()` is a built-in function, it can be used with strings, tuples, dictionaries, and custom objects that implement the `__len__()` method.
* Method: A function that is associated with an object and is called on that object.
For example, `append()` is a method of the list object, we cannot do `list1.len()`

# Summary for common operation for manipulating different data types

Sure, here is the table with explanations added as the second column:

| Operation            | Action                                    | List                        | Tuple                        | Set                              | Dictionary                                 |
|:--------------------:|:-----------------------------------------:|:---------------------------:|:----------------------------:|:--------------------------------:|:------------------------------------------:|
| **Declaration**      | To create each data type                  | `list1 = [1, 2, 3]`         | `tuple1 = (1, 2, 3)`         | `set1 = {1, 2, 3}`               | `dict1 = {'a': 1, 'b': 2, 'c': 3}`         |
| **Accessing**        | To access elements                        | `list1[0]`                  | `tuple1[0]`                  | Not applicable (unordered)       | `dict1['a']`                               |
| **Slicing**          | To get a subset of elements               | `list1[1:3]`                | `tuple1[1:3]`                | Not applicable                   | Not applicable                             |
| **Modification**     | To change elements                        | `list1[0] = 10`             | Not allowed (immutable)      | `set1.add(4)`                    | `dict1['a'] = 10`                          |
| **Appending**        | To add elements to the end                | `list1.append(4)`           | Not allowed (immutable)      | `set1.add(4)`                    | `dict1['d'] = 4`                           |
| **Extending**        | To add multiple elements                  | `list1.extend([4, 5])`      | Not allowed (immutable)      | `set1.update([4, 5])`            | `dict1.update({'d': 4, 'e': 5})`           |
| **Inserting**        | To add an element at a specific position  | `list1.insert(1, 5)`        | Not allowed (immutable)      | Not applicable (unordered)       | Not applicable                             |
| **Removing**         | To remove a specific element              | `list1.remove(2)`           | Not allowed (immutable)      | `set1.remove(2)`                 | `del dict1['b']`                           |
| **Popping**          | To remove and return the last element     | `list1.pop()`               | Not allowed (immutable)      | `set1.pop()`                     | `dict1.pop('a')`                           |
| **Clearing**         | To remove all elements                    | `list1.clear()`             | Not allowed (immutable)      | `set1.clear()`                   | `dict1.clear()`                            |
| **Finding Length**   | To get the number of elements             | `len(list1)`                | `len(tuple1)`                | `len(set1)`                      | `len(dict1)`                               |
| **Membership Test**  | To check if an element exists             | `2 in list1`                | `2 in tuple1`                | `2 in set1`                      | `'a' in dict1`                             |
| **Iteration**        | To loop through elements                  | `for x in list1: print(x)`  | `for x in tuple1: print(x)`  | `for x in set1: print(x)`        | `for key, value in dict1.items(): print(key, value)` |
| **Sorting**          | To sort elements                          | `list1.sort()`              | Not allowed (immutable)      | `sorted(set1)` (returns a list)  | `sorted(dict1)` (returns sorted keys)      |
| **Reversing**        | To reverse the order of elements          | `list1.reverse()`           | Not allowed (immutable)      | Not applicable                   | Not applicable                             |
| **Comprehension** | Syntax | `[expression for item in iterable if condition]` | `tuple(expression for item in iterable if condition)` | `{expression for item in iterable if condition}` | `{key_expression: value_expression for item in iterable if condition}` |
| **Comprehension example** | concise ways to create collections by iterating over iterable objects and optionally filtering elements | `squared_numbers = [x**2 for x in range(10) if x % 2 == 0]` | `squared_tuple = tuple(x**2 for x in range(10))` | `squared_set = {x**2 for x in range(10)}` | `squared_dict = {x: x**2 for x in range(10)}` |


## Cheatsheets Python 3

https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf

https://www.pythoncheatsheet.org/cheatsheet/built-in-functions

## PEP 8 - Style guide for Python code

https://peps.python.org/pep-0008/