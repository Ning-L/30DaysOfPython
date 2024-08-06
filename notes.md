Following the 30 days of Python challenge: <https://github.com/Asabeneh/30-Days-Of-Python>

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

Docs for built-in functions: <https://docs.python.org/3.9/library/functions.html>

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

- *is*: Returns `True` if both variables are (point to) the same object (`x is y`) (equivalent to `identical()` in R)
- *is not*: Returns `True` if both variables are not the same object (`x is not y`)
- *in*: Returns `True` if the queried list contains a certain item (`x in y`) (equivalent to `%in%` in R)
- *not in*: Returns `True` if the queried list doesn't have a certain item (`x not in y`)

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

- Use the assignment of new values to modify items

```py
fruits[1:3] = ["a", "b"] # ['banana', 'a', 'b', 'lemon']
```

- Adding

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

- Inserting

Use method `insert(idx, item)` to insert a single element at a specified index of a list.

```py
fruits.insert(2, 'watermelon')
```

- Removing

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

- `count()`: to count occurrence of a speficied item
- `index()`: to find the index of a speficied item

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

- Creation with the built-in function `set()` to create an empty set, and `{}` to initiate a set with values:

    ```py
    my_set = set()
    my_set = {"a", "b", "c"}
    ```

- Getting length with the built-in function `len()`.
- Accessing items in a set with loops to access itmes. See the loop section.
- Checking an item with the `in` operator.
- Adding items with `add()` or `update()` method.

    ```py
    my_set.add("one item")
    my_set.update(["one item", "two item"]) # update takes a list
    ```

- Removing items with `remove()` (raise error if item not found), `pop()` (remove a random item and return the removed item) or `discard()`

```py
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
removed_item = fruits.pop() # store the removed item in case we are interested in
```

- Clearing items of a set with `clear()` method.
- Deleting a set with the `del` statement.
- Converting: list and set can be converted to each other, set will remove duplicates and order is lost.

    ```py
    lst = ['item1', 'item2', 'item3', 'item4', 'item1']
    st = set(lst)  # {'item1', 'item4', 'item3', 'item2'}
    ```

- Joining sets with `union()` or `update()` method.

    ```py
    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item5', 'item6', 'item7', 'item8'}
    st3 = st1.union(st2)

    st1 = {'item1', 'item2', 'item3', 'item4'}
    st2 = {'item5', 'item6', 'item7', 'item8'}
    st1.update(st2) # st2 contents are added to st1
    ```

- Intersection: `st1.intersection(st2)`
- Subset or supperset: `st1.issubset(st2)`, `st1.issuperset(st2)`
- Difference: `st1.difference(st2)`
- Symmetric difference: `st1.symmetric_difference(st2)`, returns all items which exist only in one set.
- Check if two sets do not have any common item: `st2.isdisjoint(st1)`

# Day 8: Dictionaries

A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
The key should be unique.

- Creation with curly brackets `{}` or the built-in function `dict()`.

    ```py
    empty_dict = {}
    # Dictionary with data values
    dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
    ```

- Getting length with the `len()` function, it checks the number of 'key: value' pairs in the dictionary.
- Accessing items via the key name: `dct["key1"]`. Can raise error if the key is not found.
We can use `get()` method to access items: `dct.get("keyXX")`, if key does not exist, it will return None, a NoneType object data type.
- Adding item should be a 'key: value' pair: `dct["key5"] = "value5"`
- Modifying items via the key:  `dct["key5"] = "value555"`
- Checking key with the `in` operator:  `"key5" in dct`
- Removing key: value pairs with `pop(key)`, `popitem()` or `del`

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

- Change dictionary to list of tuples with the `items()` method: `dct.items()`
- Clearing a dictionary with the `clear()` method: `dct.clear()`
- Deleting a dictionary with `del` statement
- Copy a dictionary with `copy()` method
- Getting dictionary keys/values as a list with the `keys()`/`values()` method: `dct.keys()`, `dct.values()`.
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

- To avoid nested condition, we can write nested conditions by using logical operator `and`

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

- Combine the `or`

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

- Use `break` to get out of the loop.

    ```py
    count = 0
    while count < 5:
        print(count)
        count = count + 1
        if count == 3:
            break
    # only prints 0, 1, 2, when arrives at 3 it stops.
    ```

- Use `continue` to skip the current iteration and continue with the next.

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

- Use `break` when we like to stop our loop before it is completed.

    ```py
    numbers = (0,1,2,3,4,5)
    for number in numbers:
        print(number)
        if number == 3:
            break
    # loop stop when number gets to 3
    ```

- Use `continue` when we like to skip some of the steps in the iteration of the loop.

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

- `os` module: to perform operating system tasks

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

- `sys` module: manipulate different parts of the Python runtime environment

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

- `statistics` module: provides functions for mathematical statistics of numeric data.

    ```py
    from statistics import * # importing all the statistics modules,
    # no longer need to specify the module name before the methods.
    # but not recommended as "*" create ambiguity for functions available in the environment
    ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
    print(mean(ages))       # ~22.9
    print(median(ages))     # 23
    print(mode(ages))       # 20
    print(stdev(ages))      # ~2.3
    ```

- `math` module: provides many mathematical operations and constants.

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

- `string` module:

    ```py
    import string
    print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(string.digits)        # 0123456789
    print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    ```

- `random` module: gives random number.

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

- A function can take one or more functions as parameters
- A function can be returned as a result of another function
- A function can be modified
- A function can be assigned to a variable

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

Attention: **/!\ not very clear, to review this notion**

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

Attention: **/!\ not clear, to review this notion, why use it?**

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

- `map()`

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

- `filter()`

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

- `reduce()`

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

- **SyntaxError** indicates that there is something wrong with the structure of your code:
  - missing colons `:`,
  - unmatched parentheses/brackets/quotes,
  - inproper indentation,
  - using reserved keywords (`def = 2`),
  - invalide characters (`print(3 @ 2)`), etc.

- **NameError** indicates that Python can't find a variable or function with the name you provided:
  - using and undefined variable,
  - misspelling a variable name,
  - using a function before defining it,
  - incorrect scope (accessing a variable that is not in the global scope),
  - using non-existent imports, etc.

- **IndexError** indicates that you are trying to access an invalid index in a sequence:
  - accessing an index that is out of the range,
  - empty list access, etc.

- **ModuleNotFoundError** indicates that Python cannot locate the specified module:
  - incorrect module name,
  - module not installed,
  - using wrong Python environment,
  - module located in a different directory (without properly setting the Python path),
  - circular imports (when two or more modules attempt to import each other directly or indirectly, creating a loop in the import structure.), etc.

- **AttributeError** indicates that you're trying to access an attribute or method that does not exist on the object you're working with:
  - accessing a non-existent attribute,
  - calling a non-existent method,
  - misspelling the attribute name,
  - accessing an attribute from a non-object (like a function or a module),
  - accessing attributes in inherited classes, etc.

- **KeyError** indicates that you're trying to access a key that does not exist in a dictionary:
  - accessing a non-existent/non-defined key,
  - accessing keys after deletion,
  - typos (case sensitive), etc.

- **TypeError** indicates that an operation was applied to an object of an inappropriate type:
  - unsupported operations (`'2' + 4`),
  - incorrect argument type (like expected number but input string),
  - calling an non-callable object (like string or number),
  - indexing with a non-integer type (`lst['1']`),
  - providing incorrect number of argument to a function, etc.

- **ImportError**  indicates that Python cannot find the specified module or object during the import process:
  - module not found,
  - incorrect module path,
  - circular import,
  - inporting non-existent function, etc.

- **ValueError** indicates that a function received an argument of the right type but an inappropriate value:
  - incorrect value for a function (like `int('12a')`),
  - out of range (like `import math; math.sqrt(-1)`),
  - invalide data conversion (like `float('a')`),
  - wrong shape or size (value that does not fit the expected shape or size for data structure, like lenght of 2 but operate 3 times, unpacking values for wrong nb of variables), etc.

- **ZeroDivisionError** indicates you are dividing a number by zero.

# Day 16: Date time

The module `datetime` help to handle date and time in Python.

```py
import datetime
print(dir(datetime))
# ['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
```

## Getting datetime info

```py
from datetime import datetime
now = datetime.now()
print(now)                      # 2024-07-16 14:57:25.550344
day = now.day                   # 16
month = now.month               # 7
year = now.year                 # 2024
hour = now.hour                 # 14
minute = now.minute             # 57
second = now.second             # 25
timestamp = now.timestamp()     # number of sec elapsed from 1st of January 1970 UTC.
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 16/7/2024, 14:57
```

## Formatting date output using `strftime` method

```py
from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}, {a%}')  # 1/1/2020, 0:0
```

Here's the cheatsheet for Python strftime: <https://strftime.org/>

```py
from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)

time_one = now.strftime("%m/%d/%Y, %H:%M:%S") # mm/dd/YY H:M:S format
print("time one:", time_one)

time_two = now.strftime("%d/%m/%Y, %H:%M:%S") # dd/mm/YY H:M:S format
print("time two:", time_two) 

now.strftime("%m/%d/%Y, %A, %H:%M:%S") # '07/16/2024, 15:07:51, Tuesday'
```

## Parsing string to time using `strptime` method

```py
from datetime import datetime
date_string = "5 December, 2019" # "date_string = 5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) # "date_object = 2019-12-05 00:00:00"
```

## Using `date` from datetime

```py
from datetime import date
d = date(2024, 1, 1)
print(d)
print('Current date:', d.today())    # 2024-7-16
# date object of today's date
today = date.today()
print("Current year:", today.year)   # 2024
print("Current month:", today.month) # 7
print("Current day:", today.day)     # 16
```

## Time objects to represent time

```py
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)  # a = 00:00:00

# time(hour, minute and second)
b = time(10, 30, 50)
print("b =", b) # b = 10:30:50

# time(hour, minute and second)
c = time(hour=10, minute=30, second=50)
print("c =", c) # c = 10:30:50

# time(hour, minute, second, microsecond)
d = time(10, 30, 50, 200555)
print("d =", d) # d = 10:30:50.200555
```

## Difference between two time points

- using `date`

    ```py
    today = date(year=2019, month=12, day=5)
    new_year = date(year=2020, month=1, day=1)
    time_left_for_newyear = new_year - today
    # Time left for new year:  27 days, 0:00:00
    print('Time left for new year: ', time_left_for_newyear)
    ```

- using `datetime`

    ```py
    t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
    t2 = datetime(year = 2020, month = 1, day = 1, hour = 0, minute = 0, second = 0)
    diff = t2 - t1
    print('Time left for new year:', diff)
    ```

- using `timedelta`

    ```py
    from datetime import timedelta
    t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
    t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
    t3 = t1 - t2
    print("t3 =", t3)
    ```

# Day 17

## Exception handling

Use `try` and `expect` to handle errors and exit "gracefully".
Exceptions could be an incorrect input, wrong file name, unable to find a file, a malfunctioning, IO device, etc.

```py
# syntax
try:
    code in this block if things go well
except:
    code in this block run if things go wrong

# example:
try:
    print(10 + '5')
except:
    print('Something went wrong')
## "Something went wrong"

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
# "Something went wrong"
"""
the print() was not executed.
but we don't know exactly the problem.
so we can use different error type with except
"""

try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
# Enter your name: 11
# Year you were born: 22
# Type error occured

"""
now we know it's type error
next, we add additional block else and finally
"""
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur') # run here and following except when there is an exception
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block') # no exception, run here
finally:
    print('I alway run.') # always run here
# Enter your name:adam
# Year you born:1990
# Type error occur
# I alway run.

## shorten code
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
# Enter your name:adma
# Year you born:1990
# unsupported operand type(s) for -: 'int' and 'str'

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
finally:
    print("I'm the line that always executed")
# Enter your name:adam
# Year you born:1909
# unsupported operand type(s) for -: 'int' and 'str'
# I'm the line that always executed
```

## Packing and unpacking arguments

Use operator `*` for lists and tuples, use `**` for dictionaries.

### Unpacking

- for lists:

```py
## for lists
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

"""
This function take 5 args but we provide a list of 5 items,
we need to unpack the list to make it works
"""
print(sum_of_five_nums(*lst)) # 15


numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
```

- for tuples

```py
numbers = (1, 2, 3, 4, 5, 6, 7)
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7, the variable which capture multiple items as a list
```

- for dictionaries

```py
def unpacking_person_info(country, name, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

"""
When you unpack the dictionary into the function call using **dct,
The key names become the parameter names, and the corresponding values are passed as the arguments.
(so the key names should be able to matching with args names, order doesn't matter)
It is equivalent to calling the function with the key-value pairs as keyword arguments.
"""
```

### Packing

Can use the packing method to allow function to take unlimited or arbitary number of argumets.

- packing lists:

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

## equivalent when we provide a list, what is the real advantage to packing?
def sum_all_list(args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all_list([1, 2, 3]))  
```

- packing dictionaries

```py
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs
"""
'**kwargs' (abbr for keyword arguments, equivalent to '...' in R),
which captures the extra arguments and stores them as a dictionary
"""

print(packing_person_info(name="Asabeneh", ountry="Finland", city="Helsinki", age=250))
## output
# name = Asabeneh
# country = Finland
# city = Helsinki
# age = 250
# {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### Spreading

In Python, "spreading" typically refers to the use of the `*` and `**` operators to unpack iterable objects like lists, tuples, and dictionaries.

```py
### we can merge two lists using the `*` operator
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]

### we can merge two dictionaries using the `**` operator
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
# Merge dictionaries
merged_dict = {**dict1, **dict2}
print(merged_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

### Enumerate

We can use the builtin function `enumerate` to get the index in the list, tuple or dictionary.

```py
for index, item in enumerate([20, 30, 40]):
    print(index, item)
# 0 20
# 1 30
# 2 40

for index, item in enumerate((7, 8, 9)):
    print(index, item)
# 0 7
# 1 8
# 2 9

for index, item in enumerate({'a': 1, 'b': 2, 'c': 3, 'd': 4}):
    print(index, item)
# 0 a
# 1 b
# 2 c
# 3 d

from countries import countries
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
# The country Finland has been found at index 59
```

### Zip

Combine lists when looping through them.

```py
fruits = ['banana', 'orange']                    
vegetables = ['Tomato', 'Potato', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})
print(fruits_and_veges)
# [{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}]
"""
Attention, the two lists should have the same length,
otherwise, the combine will stop when the shortest list is exausted.
"""
```

# Day 18: Regular expressions

## The `re` module

The Python module `re` allow to use regular expression to search for a match in a string.

- `re.match()`: searches only in the beginning of the first line of the string and returns matched objects if found, else returns `None`.

```py
# syntax
re.match(substring, string, flags=0)
# substring is a string or a pattern, string is the text we look for a pattern 
# flags (optional), a bitwise OR of zero or more of the follwing flags:
# "re.IGNORECASE" or "re.I": Ignore case.
# "re.MULTILINE" or "re.M": Make `^` and `$` match the start and end of each line.
# "re.DOTALL" or "re.S": Make `.` match any character, including newline.
# "re.UNICODE" or "re.U": Use Unicode matching rules (this is the default).
# "re.VERBOSE" or "re.X": Enable verbose mode, which allows you to write regular expressions that are more readable by allowing you to add whitespace and comments.
# "re.ASCII" or "re.A": Make `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s`, and `\S` match only ASCII characters.

import re

txt = 'I love to teach python and javaScript'

match = re.match('I love to Teach', txt, re.I) # It returns an object with span, and match
print(match)
# <re.Match object; span=(0, 15), match='I love to teach'>
re.match('I love to Teach', txt) # not ignoring case
# None

print(re.match('to teach', txt, re.I)) # None
print(re.match('I lovve', txt, re.I)) # None
'''
Returns `None` because the match function returns an object only if the text starts with the pattern
'''

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15), a tuple

# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15

substring = txt[start:end]
print(substring)       # I love to teach
```

- `re.search()`: Returns a match (the 1st) object if there is one anywhere in the string, including multiline strings.

```py
# syntax
re.search(substring, string, flags=0)

re.search('to Teach', txt, re.I)
# <re.Match object; span=(7, 15), match='to teach'>
print(re.search('I lovve', txt, re.I)) # None

multiline_txt = '''This is a sentence
stored in multiple lines
'''
re.search('i', multiline_txt, re.I)
# <re.Match object; span=(2, 3), match='i'>
```

- `re.findall()`: Returns a list containing all matches

```py
# syntax
re.findall(substring, string, flags=0)

re.findall('is', multiline_txt)
# ['is', 'is']

long_txt = """learning Python and R, but
prefer python"""
re.findall('Py', long_txt, re.I) # ['Py', 'py']
## or
re.findall('[P|p]y', long_txt) # ['Py', 'py']

```

- `re.split()`: Takes a string, splits it at the match points, returns a list

```py
# syntax
re.split(substring, string, maxsplit=0, flags=0)

re.split('[P|p]y', long_txt)
# ['learning ', 'thon and R, but\nprefer ', 'thon']

re.split('\n', long_txt)
# ['learning Python and R, but', 'prefer python']
```

- `re.sub()`: Replaces one or many matches within a string

```py
# syntax
re.sub(pattern, repl, string, count=0, flags=0)

re.sub('Python|python', 'JavaScript', long_txt)
# 'learning JavaScript and R, but\nprefer JavaScript'
```

## RegEx patterns

- []: A set of characters
  - [a-c] means, a or b or c
  - [a-z] means, any letter from a to z
  - [A-Z] means, any character from A to Z
  - [0-3] means, 0 or 1 or 2 or 3
  - [0-9] means any number from 0 to 9
  - [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
- \\: uses to escape special characters
  - \d means: match where the string contains digits (numbers from 0-9)
  - \D means: match where the string does not contain digits
- . : any character except new line character(\n)
- ^:
  - r'^substring' eg r'^love', a sentence that **starts with** a word love
  - r'[^abc] means **not** a, not b, not c.
- $: ends with
  - r'substring$' eg r'love$', sentence  that ends with a word love
- *: zero or more times
  - r'[a]*' means a optional or it can occur many times.
- +: one or more times
  - r'[a]+' means at least once (or more)
- ?: zero or one time
  - r'[a]?' means zero times or once
- {3}: Exactly 3 characters
- {3,}: At least 3 characters
- {3,8}: 3 to 8 characters
- |: Either or
  - r'apple|banana' means either apple or a banana
- (): Capture and group

Use `r'` to prefix a string to tell Python that the string is a raw string,
to treat backslashes (`\`) as literal characters and not as escape characters.

```py
normal_string = "This is a newline character: \n"
print(normal_string)
# This is a newline character: 
# (followed by a new line)

raw_string = r"This is a newline character: \n"
# print(raw_string)
# This is a newline character: \n
```

# Day 19: File handling and file types

## File handling

File handling allows us to create, read, update and delete files.
In Python to handle data we use `open()` built-in function.

```py
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

- "r": Read - Default value. Opens a file for reading, it returns an error if the file does not exist
- "a": Append - Opens a file for appending, creates the file if it does not exist
- "w": Write - Opens a file for writing, creates the file if it does not exist
- "x": Create - Creates the specified file, returns an error if the file exists
- "t": Text - Default value. Text mode
- "b": Binary - Binary mode (e.g. images)

Opened file has different reading methods: `read()`, `readline()`, `readlines()`.
An opened file has to be closed with `close()` method.

### Opening for reading

- `read()`: read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
## output
# <class 'str'>
# This is an example to show how to open a file and read.
# This is the second line of the text.

## read only the first 10 characters
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
## output
# <class 'str'>
# This is an
```

- `readline()`: read only the 1st line, or read the next line as a string

```py
line = f.readline()
print(type(line))
print(line)
f.close()
## output
# <class 'str'>
# This is an example to show how to open a file and read.
```

- `readlines()`: reads all lines as a **list**

```py
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
## output
# <class 'list'>
# ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']

# Another way to get all the lines as a list is using `splitlines()`:
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
## output
# <class 'list'>
# ['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

A new way to have the file closed by itself using `with`:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
## output
# <class 'list'>
# ['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### Opening for writing and updating

Use the mode "a" (appending) or "w" (overwriting) in the parameter "mode" of `open()`.

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

# file.write(content) # writes a string to the file
# file.writelines(lines) # writes a list of strings to the file
```

### Deleting files

Use `remove` of `os` to remove a file.
It's better to check existance, if not the case, remove will raise an error.

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## File types

- `file.txt`
- `file.json` (a stringified Java object or a Python dictionary)

```py
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}

# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

Use the `loads` method from the `json` module to change a JSON to a dictionary.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

## output
# <class 'dict'>
# {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
# Asabeneh
```

Use the `dumps` method from the `json` module to change a dictionary to a JSON.

```py
person_json = json.dumps(person_dct, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
# <class 'str'>
## JSON does not have type, it is a string type.
```

We can also save our data as a json file using the `json.dump()`,
it takes dictionary, outputfile, ensure_ascii and ident as parameters.

```py
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

- `file.csv`: store tabular data using the `csv` module

```py
## `csv_example.csv` contains following content:
# "name","country","city","skills"
# "Asabeneh","Finland","Helsinki","JavaScript"

import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

## output:
# Column names are :name, country, city, skills
#         Asabeneh is a teacher. He lives in Finland, Helsinki.
# Number of lines:  2
```

- `file.xlsx`: install the `xlrd` package to read excel file.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

- `file.xml`: XML is another strucutred data format wich looks like HTML.
Use the `xml.etree.ElementTree` module to read it. See: <https://docs.python.org/2/library/xml.etree.elementtree.html>

# Day 20: Python package manager `pip`

## Installing packages

Using `pip install packagename`.
Tere, the package name are **case-insensitive**.

- `numpy`: numeric python package
  - a powerful N-dimensional array object
  - sophisticated (broadcasting) functions
  - tools for integrating C/C++ and Fortran code
  - useful linear algebra, Fourier transform, and random number capabilities

```bash
pip install numpy
```

```py
import numpy
numpy.version.version

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)

lst * 2 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
np_arr * 2 # array([ 2,  4,  6,  8, 10]), support element wise operation
np_arr + 2 # array([3, 4, 5, 6, 7])
```

The NumPy arrays store element of the **same** data type.

- `pandas`: high-performance, easy-to-use data structures and data analysis tools

```bash
pip install pandas
```

```py
import pandas
```

- `webbrowser`: help us to open any website (installed by default with Python 3)

Useful when we want to open any number of websites at any time:

```py
import webbrowser # web browser module to open websites

# list of urls: learning python
url_lists = [
    'https://github.com/Asabeneh/30-Days-Of-Python/tree/master', # the training
    'https://github.com/Ning-L/30DaysOfPython/blob/main/notes.md', # my notes
    'https://chatgpt.com/', # the super helpful learning partner
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

- `requests`: allows to open a network connection and to implement CRUD (create, read, update and delete).

```bash
pip install requests
```

```py
## example
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries
```

## Other operation on packages

- Uninstall packages: `pip uninstall packagename`
- Check the installed packages: `pip list`
- Show package information: `pip show packagename` or `pip show --verbose packagename` (with more details)
- Generate installed packages with their version, output is suitable to use as a requirement file: `pip freeze`
- Create a package: A package is a folder containing one or more module files. A module can contain multiple objects, such as classes, functions, etc. Example: "mypackage" folder which contains:

  - init.py: store package's content, it lets Python to recognize it as a package. (The `init.py` exposes specified resources from its modules to be imported to other python files. An empty `init.py` file makes all functions available when a package is imported. The `init.py` is essential for the folder to be recognized by Python as a package.)
  - arithmetic.py
  - greet.py
  Then we can `from mypackage import arithmetics` and call `arithmetics.add_numbers(1, 2, 3, 5)`

## Usefull packages

- `SQLAlchemy` or `SQLObject` - Object oriented access to several different database systems
- `django` and `flask` for web development
- `beautifulsoup4` and `PyQuery` for HTML parser
- `ElementTree` for XML processing
- `requests`: send request to a server
- data analysis, data science and ML:
  - `NumPy`
  - `Pandas`
  - `SciPy`: ML library, contains modules for optimization, linear algebra, integration, image processing, and statistics.
  - `Scikit-Learn`: it is NumPy and SciPy. It is considered as one of the best libraries for working with complex data.
  - `TensorFlow`: ML pkg built by Google
  - `Keras`: ML library

# Day 21: Classes and objects

Python is an object oriented programming language.
Everything in Python is an object, with its properties and methods.
We initiate a class to create an object, the class is like an object constructor, it defines attributes and the behavoir of the object.
The object represent its class.
Everything in Python is an object of a class.

## Creation of a class

Use the keyword `class` to create a class,
the class name should be **CamelCase**.

```py
# syntax
class ClassName:
    code goes here

# example
class Person:
    pass

print(Person)
# <class '__main__.Person'>
```

## Creation of an object

We can create an object by calling the class

```py
p = Person()
print(p)
# <__main__.Person object at 0x103e93fd0>
```

## Class constructor

Use the built-in `init()` constructor function to make the class more useful,
the `init` constructor has `self` parameter which is a reference to the current instance of the class. For example:

```py
class Person:
    def __init__(self, name, age):
        # self allows to attach parameter to the class
        self.name = name # attribute
        self.age = age   # attribute

p = Person(name = "Abc", age = "25")
print(p) # <__main__.Person object at 0x100ded730>
print(p.name) # "Abc"
print(p.age) # 25
```

## Object method

Objects can have methods, the methods are functions which belongs to the object.

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def person_info(self): # method
        return f"{self.name} is {self.age} years old"

p = Person("Abc", 25)
print(p.name) # Abc
print(p.age) # 25
print(p.person_info()) # 'Abc is 25 years old'
```

## Object default method

We can dive default values for the parameters in the constructor.

```py
class Person:
    def __init__(self, name = "Abc", age = 25):
        self.name = name
        self.age = age
    def person_info(self): # method
        return f"{self.name} is {self.age} years old"

p1 = Person()
p1.person_info() # 'Abc is 25 years old'

p2 = Person("EDF", 27)
p2.person_info() # 'EDF is 27 years old'
```

## Method to modify class default values

```py
class Person:
    def __init__(self, name = "Abc", age = 25):
        self.name = name
        self.age = age
        self.skills = []
    def person_info(self): # method
        return f"{self.name} is {self.age} years old"
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
p1.person_info() # 'Abc is 25 years old'
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p1.skills # ['HTML', 'CSS', 'JavaScript']

p2 = Person("EDF", 27)
p2.person_info() # 'EDF is 27 years old'
p2.skills # []
```

## Inheritance

We can re-use parent class code.
Inheritance allows us to define a class that inherits all the methods and properties from parent class.

We don't need to call the `init` constructor in the child class,
but we still have access to all the properties from the parent class.

For example, let's create a "Student" class by inheriting from "Person" class:

```py
class Student(Person):
    pass

s1 = Student('Eyob', 30)
s1.person_info() # 'Eyob is 30 years old'

s2 = Student('ccc', 902)
s2.person_info() # 'ccc is 902 years old'
s2.add_skill("R")
s2.add_skill("Markdown")
s2.skills # ['R', 'Markdown']
```

If we do call the constructor, we can access the parent properties by calling `super()`.

```py
class Student(Person):
    def __init__(self, name = "aaa", age = 10, gender = "unknown"):
        self.gender = gender
        super().__init__(name, age) # use `super()` to call the parent class's `__init__` method
s3 = Student(gender = "female")
s3.name # "aaa"
s3.age # 10
s3.gender # 'female"
s3.person_info() # 'aaa is 10 years old'
```

## Overriding parent method

We can add new method to the child or we can override the parent class methods by creating the same method name in the child class.

```py
class Student(Person):
    def __init__(self, name = "aaa", age = 10, gender = "unknown"):
        self.gender = gender
        super().__init__(name, age) 
    def person_info(self):
        pronoun = "boy" if self.gender == "male" else "girl"
        return f"{self.name} is a {self.age} years old {pronoun}."

s3 = Student(gender = "female")
s3.person_info()
```

## Another example

Object-oriented programming (OOP) is a programming paradigm that uses "objects" to design applications and computer programs. Here’s an overview to help you understand the core concepts of OOP:

### Key Concepts of OOP

1. **Objects**: Objects are instances of classes that represent entities with attributes (data) and methods (functions or procedures) that operate on the data. For example, a `Car` object might have attributes like `color` and `model`, and methods like `start()` and `stop()`.

2. **Classes**: A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. For example, you might have a `Car` class that defines the properties and behaviors of a car.

3. **Encapsulation**: Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit or class. It also involves restricting direct access to some of the object's components, which is called information hiding. This helps in protecting the internal state of the object from unintended interference.

4. **Inheritance**: Inheritance is a mechanism where a new class (child class) inherits attributes and methods from an existing class (parent class). This helps in reusing existing code and creating a hierarchy of classes. For example, you might have a `Vehicle` class that is inherited by the `Car` class and `Bike` class.

5. **Polymorphism**: Polymorphism allows objects of different classes to be treated as objects of a common superclass. It also allows the same method to behave differently on different classes. For example, a method `draw()` might behave differently for objects of `Circle`, `Square`, and `Triangle` classes.

6. **Abstraction**: Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object. It helps in reducing programming complexity and effort.

### Examples in Python

Here's a simple example to illustrate these concepts in Python:

```py
# Define a class (blueprint)
class Car:
    def __init__(self, make, model, year):
        self.make = make  # attribute
        self.model = model  # attribute
        self.year = year  # attribute
        """
        __init__ is use to initialize the attributes of the class
        self is a keyword which refers to the current instance of the class being created
        """

    def start_engine(self):  # method
        print(f"{self.year} {self.make} {self.model} engine started.")

    def stop_engine(self):  # method
        print(f"{self.year} {self.make} {self.model} engine stopped.")

# Create an object (instance) of the class
my_car = Car("Toyota", "Camry", 2020)

# Access attributes
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)  # Output: 2020

# Call methods
my_car.start_engine()  # Output: 2020 Toyota Camry engine started.
my_car.stop_engine()  # Output: 2020 Toyota Camry engine stopped.
```

### Examples in R

Here's a simple example to illustrate these concepts in R using the S3 system:

```r
# Define a constructor function for a "Car" class (blueprint)
Car <- function(make, model, year) {
  obj <- list(make = make, model = model, year = year)
  class(obj) <- "Car"
  return(obj)
}

# Define a method to start the engine
start_engine <- function(car) {
  UseMethod("start_engine")
}

start_engine.Car <- function(car) {
  cat(car$year, car$make, car$model, "engine started.\n")
}

# Define a method to stop the engine
stop_engine <- function(car) {
  UseMethod("stop_engine")
}

stop_engine.Car <- function(car) {
  cat(car$year, car$make, car$model, "engine stopped.\n")
}

# Create an object (instance) of the class
my_car <- Car("Toyota", "Camry", 2020)

# Access attributes
print(my_car$make)  # Output: Toyota
print(my_car$model)  # Output: Camry
print(my_car$year)  # Output: 2020

# Call methods
start_engine(my_car)  # Output: 2020 Toyota Camry engine started.
stop_engine(my_car)  # Output: 2020 Toyota Camry engine stopped.
```

## An more complexe example

```py
class chat:  # Définition de notre classe Personne
    """Classe définissant un chat caractérisé par :
    - sa couleur
    - son âge
    - son caractère
    - son poids
    - son maitre
    - son nom

    L'objet chat a deux méthodes : nourrir et litiere"""

    def __init__(self): # to initialize the instantiated object
        # Notre méthode constructeur -
        # self c'est notre objet qu'on est en train de créer
        self.nom = ""
        self.couleur = "Roux"
        self.age = 10
        self.caractere = "Joueur"
        self.poids = 3
        self.maitre = "Jeanne"
        """Par défaut, notre ventre est vide"""
        self.ventre = ""

    def nourrir(self, nourriture):
        """Méthode permettant de donner à manger au chat.
        Si le ventre n'est pas vide, on met une virgule avant de rajouter
        la nourriture"""
        if self.ventre != "":
            self.ventre += ","
        self.ventre += nourriture

    def litiere(self):
        """Méthode permettant au chat d'aller à sa litière :
        en conséquence son ventre est vide"""
        self.ventre = ""
        print(self.nom, "a le ventre vide")

    def __getattribute__(self, key):
        return print(key, "n'est pas un attribut de la classe chat")

    def __repr__(self): # to modify its display
        return "Je suis une instance de la classe chat"

mon_chat = chat()
print(mon_chat.nom)
# Martin

mon_chat.origine
# origine n'est pas un attribut de la classe chat

print(mon_chat)
# <__main__.chat object at 0x7fd9a47c5d50>
# Je suis une instance de la classe chat
```

# Day 23: Virtual environment

Virtual environment helps to create an isolated environment,
which helps us to avoid conflicts in dependencies across projects.
Use "virtualenv" to have access only packages which are specific for that project. (like "renv" in R)

For example:

```bash
# first install virtualenv
pip install virtualenv

# create a test folder called "flask_project" inside the "30DaysOfPython"
cd ~/Desktop/30DaysOfPython
mkdir flask_project
cd flask_project

# create a virtual environment called "venv"
virtualenv venv
ls venv # check if the venv was created

# activate the virtual environment
soucre venv/bin/activate
# then the project directory is start with (venv)

# check available pkgs by pip freeze, nothing installed
pip freeze

# then install flask pkg in this project
pip install flask

# recheck installed pkgs
pip freeze
# blinker==1.8.2
# click==8.1.7
# Flask==3.0.3
# importlib_metadata==8.2.0
# itsdangerous==2.2.0
# Jinja2==3.1.4
# MarkupSafe==2.1.5
# Werkzeug==3.0.3
# zipp==3.19.2

# to deactivate project
deactivate # the (venv) dispeared before the path
```

# Days 24: Modules `statistics` and `numpy`

- `statistics` module provides fcts for calculating mathematical stats of numerical data, aimed at graphing and scitific calculators.

- `numpy` is the core library for scientific computing in Python. It provides high performance multidimensional array object and tools for working with arrays.

```py
import numpy as np
python_list = [1, 2, 3, 4, 5]
print(type(python_list)) # # <class 'list'>

"""Creation of numpy arrays"""
## int array
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list)) # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

## float array
numy_array_from_list2 = np.array(python_list, dtype = float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

## boolean array
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype = bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

## logic functions in Numpy
# count_nonzero(a, axis=None, *, keepdims=False)
# isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature])
y = np.array([np.nan, 0, 1])
np.count_nonzero(y) # 2
np.isnan(y) # array([ True, False, False])

np.random.seed(123)
x = np.random.normal(0, size=(3, 4))
x.shape # (3, 4), so axis 0 refers to rows (column-wise) and axis 1 refers to columns (row-wise)
np.any(x > 0) # check if the 2d array has at least one pos value
np.any(x > 0, axis = 0) # check if the 2d array has at least one pos value along rows
np.any(x > 0, axis = 1) # check if the 2d array has at least one pos value along cols

# Create multidimensional numpy array
## multi-dimensional array from list
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list)) #  <class 'numpy.ndarray'>
print(numpy_two_dimensional_list)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

## multi-dimensional array to list
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list)) #  <class 'list'>
print('one dimensional array:', np_to_list) # [1, 2, 3, 4, 5]

# Create numpy array from tuple
python_tuple = (1, 2, 3, 4, 5)
numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

"""
The `shape` method provides the array dimension as a tuple, with nrow and ncol.
If it's one dim array, it returns the size of the array.
"""
nums = np.array([1, 2, 3, 4, 5])
print(nums.shape) # (5, )

three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10, 11]])
print(three_by_four_array.shape) # (3, 4)

"""
The data types of numpy array are:
 str, int, float, complex, bool, list, None
Use the method `dtype` to get access of it.
"""
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)
print(int_array.dtype) # int64
print(float_array.dtype) # float64

"""
Use `size` to know the total nb of items in a numpy array
"""
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array(
    [[0, 1, 2],
     [3, 4, 5],
     [6, 7, 8]]
)
print(numpy_array_from_list.size) # 5
print(two_dimensional_list.size)  # 9

""" `ndim` gives the number of dimension """
numpy_array_from_list.ndim # 1
two_dimensional_list.ndim # 2

"""
Numpy array allows to do math operation without looping.
+, -, *, /, %(modules), //(floor division), *(exponetial)
"""
print(numpy_array_from_list // 3) # array([0, 0, 1, 1, 1])
print(numpy_array_from_list % 3) # array([1, 2, 0, 1, 2])

"""
We can convert data type using the "dtype" parameter or with `astype()` method
"""
numpy_float_list = np.array([1,2,3,4], dtype = 'float')
print(numpy_float_list)
# array([1., 2., 3., 4.])

print(np.array([-3, -2, 0, 1,2,3], dtype='bool'))
# array([True, True, False, True, True, True])

numpy_float_list.astype("int") # array([1, 2, 3, 4])
numpy_float_list.astype("str") # array(['1.0', '2.0', '3.0', '4.0'], dtype='<U32')

"""
Getting items from a numpy array
"""
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
print('First row:', first_row) # First row: [1 2 3]
first_column = two_dimension_array[:,0] # First column: [1 4 7]
## the colon `:` used to indicate slicing, it selects all elements along that axis. Here, before the comma, it means select all rows
## the comma `,` separates the dim in the array indexing, everything before applies to rows and everything after applies to the columns

"""
Slicing array with the index
"""
two_dimension_array[1:3, 0:2]
# array([[4, 5],
#        [7, 8]])

""" change array element """
numpy_array_from_list[0] = 11
# array([11,  2,  3,  4,  5])
numpy_array_from_list[1:3] = 22, 33
# array([11, 22, 33,  4,  5])

"""
Reverse the whole array
"""
two_dimension_array[::-1, ::-1]
# array([[9, 8, 7],
#        [6, 5, 4],
#        [3, 2, 1]])

"""
Reverse the rows
"""
two_dimension_array[::-1, :] # or two_dimension_array[::-1, ]
# array([[7, 8, 9],
#        [4, 5, 6],
#        [1, 2, 3]])

"""
To create array of ones, zeros or a specified number
"""
np.ones((3,3),dtype=int,order='C') # order 'C': array will be stored in memory in row-major order, 'F' is column-major order
# array([[1 1 1]
#        [1 1 1]
#        [1 1 1]])
np.zeros((3,3),dtype=int,order='C')
# array([[0, 0, 0],
#         [0, 0, 0],
#         [0, 0, 0]])

np.full((2, 3), 3.14)
# array([[3.14, 3.14, 3.14],
#        [3.14, 3.14, 3.14]])

"""
To create an identity matrix
"""
np.eye(3)
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])

"""
Reshape arrays with `numpy.reshape()` and `numpy.flatten()`
"""
first_shape = np.array([(1,2,3), (4,5,6)])
print(first_shape)
# array([[1 2 3]
#        [4 5 6]])
reshaped = first_shape.reshape(3,2)
print(reshaped)
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
first_shape.flatten()
# array([1, 2, 3, 4, 5, 6])

"""
Transpose arrays with `x.T` (method) or `numpy.transpose()` (function)
"""
first_shape.T
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
np.transpose(first_shape)
# array([[1, 4],
#        [2, 5],
#        [3, 6]])


"""
Add, insert, delete elements in arrays
"""
np.append(x, [1,2]) # add 1 and 2 at the end of the array
np.insert(x, [1,2], 99) # insert 99 to the positions 1 and 2
np.delete(x, [0,3]) # delete elements at positions 0 and 3

"""
Horizontal or vertical append arrays
"""
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])
print(np_list_one + np_list_two) # [5 7 9]
np.hstack((np_list_one, np_list_two))
# array([1, 2, 3, 4, 5, 6])
np.vstack((np_list_one, np_list_two)) 
# array([[1, 2, 3],
#        [4, 5, 6]])

## or np.concatenate()
np.concatenate((np_list_one, np_list_two))
# array([1, 2, 3, 4, 5, 6])

"""
Sorting or partial sorting on an array
"""
x = np.array([7, 2, 3, 1, 6, 0, 4])
np.sort(x)
# array([0, 1, 2, 3, 4, 6, 7])

np.partition(x, 5)
# array([0, 1, 3, 2, 4, 6, 7])
# partitions the array such that the element at index 5 (value "6") is in its sorted position,
# and all elements before index 5 are less than or equal to it,
# and all elements after index 5 are greater than or equal to it.
# Useful when we don't need to sort the entire array,
# such as finding the k-th smallest/biggest elements
k = 3
kth_smallest = np.partition(x, k)[k]
print(f"The {k+1}th smallest element is: {kth_smallest}") # The 4th smallest element is: 3

# finding the top-k elements
top_k_smallest = np.partition(x, k)[:k]
print(f"The top {k} smallest elements are: {top_k_smallest}") # The top 3 smallest elements are: [0 1 2]

"""
Generate random numbers
"""
## random integers
random_int = np.random.randint(0, 11, size = 4) # 4 random numbers between 0 and 10
random_int = np.random.randint(0, 11, size = (3, 3)) # 3 rows and 3 cols array of random number between 0 and 10

## random floats
random_float = np.random.random(5) # generate 5 random floats between 0 and 1 (not included)

## random number following the normal distribution
# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(0, 1, 10) # or np.random.randn()

## random number following the uniform distribution
# uniform(low=0.0, high=1.0, size=None)
uniform_array = np.random.uniform(0, 1, 3)

## random choice
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
# ['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']

"""
The `matrix` class in NumPy
"""
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
four_by_four_matrix
# matrix([[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]])
np.asarray(four_by_four_matrix)[2] = 2 # change value for the 3rd row
# or
four_by_four_matrix[2] = 2 # change value for the 3rd row
four_by_four_matrix
# matrix([[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [2., 2., 2., 2.],
#         [1., 1., 1., 1.]])

"""
Create evenly spaced array over a specified interval:
`arrange()`, `linspace()` and `logspace` methods
"""
# numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 10, 1)
whole_numbers
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9])

np.linspace(1.0, 5.0, num=5, endpoint = False) # even spaced numbers on a log scale
# array([1. , 1.8, 2.6, 3.4, 4.2])

np.logspace(1.0, 5.0, num=5) # even spaced numbers on a log scale
# array([1.e+01, 1.e+02, 1.e+03, 1.e+04, 1.e+05])
```

`whole_numbers.itemsize` provide size in bytes.

NumPy provides lots of useful stat fct as the min, max, mean, med, percentile, std, variance, etc.
It has also functions like `amin`, `amax` to find min or max value of an array along a specific axis. (axis = 0 finds the min value along the rows, axis = 1 applies for the columns)

```py
array_2d = np.array([[1,7,3],[4,2,6], [9,8,5]])
# array([[1, 7, 3],
#        [4, 2, 6],
#        [9, 8, 5]])
print('Column with minimum: ', np.amin(array_2d, axis = 0)) #min of each column
# Column with minimum:  [1 2 3]
print('Column with maximum: ', np.amax(array_2d, axis = 0)) # max of each column
# Column with maximum:  [9 8 6]
print('Row with minimum: ', np.amin(array_2d, axis = 1)) # min of each row
# Row with minimum:  [1 2 5]
```

To create repeating sequence, we can use `tile()` or `repeat()`.

```py
a = [1,2,3]

# Repeat whole of 'a' twice
print('Tile:   ', np.tile(a, 2))
# Tile:    [1 2 3 1 2 3]

# Repeat each element of 'a' twice
print('Repeat: ', np.repeat(a, 2))
# Repeat:  [1 1 2 2 3 3]
```

The function `scipy.stats.mode` provides the mode of a sequence.

```py
u = [0, 1]
v = [1, 0]

### addition using python lists
z = []
for n,m in zip(u, v):
    z.append(n+m)

### addtion using np array
z = np.array(u) + np.array(v)

y = [1, 2]
### scalar addition using python lists
z = []
for n in y:
    z.append(n * 2)

### scalar addition using np array
z = np.array(y) * 2

"""
`np.dot` performs dot product (product of two arrays)
"""
f = np.array([1,2,3])
g = np.array([4,5,3])
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23

"""
`np.matmul` performs matrix product of two arrays
"""
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7=19 (position 0, 0)
### 1*6+2*8=22 (position 0, 1)
### 3*5+4*7=43 (position 1, 0)
### 3*6+4*8=50 (position 1, 1)
np.matmul(h, i)
# array([[19, 22],
#        [43, 50]])

"""
deteminant of a matrix using `np.linalg.det()`
"""
mat = np.matmul(h, i)
np.linalg.det(mat)
# p.float64(4.000000000000017)

Z = np.zeros((8,8)) # an 8*8 array filled with zeros
Z[1::2,::2] = 1
# 1::2 means start at index 1 and take every second row, so rows 2,4,6,8
# ::2 means star ad index 0 and take every second column, so cols 1,3,5,7
# all theses positions are affected to 1
Z[::2,1::2] = 2
# start at index 0 and take every second row, so rows 1,3,5,7
# start at index 1 and take every second col, so cols 2,4,6,8
# change thses postions to 2
# array([[0., 2., 0., 2., 0., 2., 0., 2.],
#        [1., 0., 1., 0., 1., 0., 1., 0.],
#        [0., 2., 0., 2., 0., 2., 0., 2.],
#        [1., 0., 1., 0., 1., 0., 1., 0.],
#        [0., 2., 0., 2., 0., 2., 0., 2.],
#        [1., 0., 1., 0., 1., 0., 1., 0.],
#        [0., 2., 0., 2., 0., 2., 0., 2.],
#        [1., 0., 1., 0., 1., 0., 1., 0.]])


[x + 2 for x in range(0, 11)]
# equivalent
np.array(range(0, 11)) + 2
```

## Summary

- array support vectorized operations while list doesn't
- we can the the array size by creating a new one or overwrite it
- every array has only one data type for all items
- numpy arrays occupied less space than python lists
- numpy arrays support boolean indexing (ex: `Z == 0`, `Z[Z > 1]`, `Z[Z == 1]`)
- Attention, Numpy and Pandas don't know how to manage NaN in int, so we need to convert to the type float when series contain missing values.

# Day 25: `pandas` module

Pandas adds data structures and tools designed to work with table-like data which is *Series* and *Data Frames*.

`Pandas` provides tools for data manipulation:

- reshaping
- merging
- sorting
- slicing
- aggregation
- imputation.

A *series* is a column and a *DataFrame* is a multidimensional table.

## Series

Pandas series can be created by numpy one dimensional array or a python list/dictionary.

```py
import pandas as pd
import numpy as np

nums = [1, 2, 3, 4, 5]
s = pd.Series(nums) # with default index starts from 0
print(s)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

s = pd.Series(nums, index = [1, 2, 3, 4, 5]) # with customized index, be careful, this can be tricky, to use method "reset_index"
print(s)
# 1    1
# 2    2
# 3    3
# 4    4
# 5    5
# dtype: int64

fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=list(range(len(fruits)+1))[1:]) # or index = [1, 2, 3]
# 1    Orange
# 2    Banana
# 3     Mango
# dtype: object

"""
In `pandas`, when a `Series` contains strings or mixed types, the dtype is "object".
pandas has a type "category" which is equivalent to the "factor" in R.
"""
fruits.astype("category")
# 1    Orange
# 2    Banana
# 3     Mango
# dtype: category

len(fruits) # 3

fruits.index
# Index([1, 2, 3], dtype='int64')
fruits.values
# array(['Orange', 'Banana', 'Mango'], dtype=object)

dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
pd.Series(dct)
# name       Asabeneh
# country     Finland
# city       Helsinki
# dtype: object

# create a constant Series
pd.Series(10, index = [1,2,3,1]) 
# 1    10
# 2    10
# 3    10
# 1    10

"""
the index can have duplicates, will not raise errors
we can perform group by operation with it
"""

# linspace Series
s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

```

## DataFrame

Can be created from list of lists, dictionary or a list of dictionaries.

```py
## from a list of lists
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
#       Names  Country       City
# 0  Asabeneh  Finland    Helsink
# 1     David       UK     London
# 2      John   Sweden  Stockholm


## from a dictionary
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
pd.DataFrame(data)
#       Names  Country       City
# 0  Asabeneh  Finland    Helsink
# 1     David       UK     London
# 2      John   Sweden  Stockholm

## from a list of dictionaries
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
pd.DataFrame(data)
```

### Modifying a DataFrame

- create a new DataFrame

```py
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
#        Name  Country       City
# 0  Asabeneh  Finland   Helsinki
# 1     David       UK     London
# 2      John   Sweden  Stockholm
```

- add/remove columns
Adding a column to a DataFrame is like to add a 'key' to a dictionary.

```py
weights = [74, 78, 69]
df['Weight'] = weights
df
#        Name  Country       City  Weight
# 0  Asabeneh  Finland   Helsinki      74
# 1     David       UK     London      78
# 2      John   Sweden  Stockholm      69

df['Height'] = [173, 175, 169]
#        Name  Country       City  Weight  Height
# 0  Asabeneh  Finland   Helsinki      74     173
# 1     David       UK     London      78     175
# 2      John   Sweden  Stockholm      69     169
```

- modify existing columns

```py
df['Height'] = df['Height'] * 0.01
#        Name  Country       City  Weight  Height
# 0  Asabeneh  Finland   Helsinki      74    1.73
# 1     David       UK     London      78    1.75
# 2      John   Sweden  Stockholm      69    1.69
```

We can calculate BMI based on the weight and height.

```py
def calculate_bmi():
    weights = df["Weight"]
    heights = df["Height"]
    bmi = []
    for w,h in zip(weights, heights): # use zip to combine iterables
        bmi.append(w/(h**2))
    return bmi
df["BMI"] = calculate_bmi()
#        Name  Country       City  Weight  Height        BMI
# 0  Asabeneh  Finland   Helsinki      74    1.73  24.725183
# 1     David       UK     London      78    1.75  25.469388
# 2      John   Sweden  Stockholm      69    1.69  24.158818
```

- formating DataFrame columns using the `round()` fonction

```py
df["BMI"] = round(df["BMI"], 1)
df
#        Name  Country       City  Weight  Height   BMI
# 0  Asabeneh  Finland   Helsinki      74    1.73  24.7
# 1     David       UK     London      78    1.75  25.5
# 2      John   Sweden  Stockholm      69    1.69  24.2
```

- change data type of column values

Use `astype()` to change data type:

```py
df["current_year"] = pd.Series(2024, index=[0, 1, 2])
df["birth_year"] = ['1769', '1985', '1990']
df['birth_year'].dtype # dtype('O'), object

df['birth_year'] = df['birth_year'].astype("int")
df['birth_year'].dtype # dtype('int64')

df["age"] = df["current_year"] - df["birth_year"] 
df
#        Name  Country       City  ...  current_year  birth_year  age
# 0  Asabeneh  Finland   Helsinki  ...          2024        1769  255
# 1     David       UK     London  ...          2024        1985   39
# 2      John   Sweden  Stockholm  ...          2024        1990   34

# [3 rows x 9 columns]

# repalce the first age by the average
df.at[0, "age"] = np.mean(df["age"][1:])
## or 
df.loc[0, "age"] = np.mean(df["age"][1:])
"""
both raise warning about data incompatibility as original column is int,
but the replace value is a float,
consider change the type before add new value
"""
df["age"] = df["current_year"] - df["birth_year"] 
df["age"] = df["age"].astype("float")
df.at[0, "age"] = np.mean(df["age"][1:])
```

- Boolean indexing

```py
df[df["BMI"] > 24.5]
#        Name  Country      City  ...  current_year  birth_year   age
# 0  Asabeneh  Finland  Helsinki  ...          2024        1769  36.5
# 1     David       UK    London  ...          2024        1985  39.0

# [2 rows x 9 columns]
```

## Reading CSV using `pandas`

Using example from: `curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv` (stored in `data/`)

```py
df = pd.read_csv("data/weight-height.csv")
df.head() # show the first five rows
#   Gender     Height      Weight
# 0   Male  73.847017  241.893563
# 1   Male  68.781904  162.310473
# 2   Male  74.110105  212.740856
# 3   Male  71.730978  220.042470
# 4   Male  69.881796  206.349801
df.tail(n = 2) # show last two rows
#       Gender     Height      Weight
# 9998  Female  69.034243  163.852461
# 9999  Female  61.944246  113.649103

df.shape # data dimension
# (10000, 3)

df.columns # print all the columns
# Index(['Gender', 'Height', 'Weight'], dtype='object')

# get a specific column, it's a Series
heights = df['Height'] # this is now a series
# 0       73.847017
# 1       68.781904
# 2       74.110105
# 3       71.730978
# 4       69.881796
#           ...    
# 9995    66.172652
# 9996    67.067155
# 9997    63.867992
# 9998    69.034243
# 9999    61.944246
# Name: Height, Length: 10000, dtype: float64

df.describe(include = "all") # give stats info regardless data type
#        Gender        Height        Weight
# count   10000  10000.000000  10000.000000
# unique      2           NaN           NaN
# top      Male           NaN           NaN
# freq     5000           NaN           NaN
# mean      NaN     66.367560    161.440357
# std       NaN      3.847528     32.108439
# min       NaN     54.263133     64.700127
# 25%       NaN     63.505620    135.818051
# 50%       NaN     66.318070    161.212928
# 75%       NaN     69.174262    187.169525
# max       NaN     78.998742    269.989699

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 10000 entries, 0 to 9999
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype  
# ---  ------  --------------  -----  
#  0   Gender  10000 non-null  object 
#  1   Height  10000 non-null  float64
#  2   Weight  10000 non-null  float64
# dtypes: float64(2), object(1)
# memory usage: 234.5+ KB
```

## Operations on DataFrame

```py
# dataframe_name["column_name"] # Accesses single column
# dataframe_name[["column1", "column2"]] # Accesses multiple columns

## subset columns
df[['Name', 'Country', 'City']]
#        Name  Country       City
# 0  Asabeneh  Finland   Helsinki
# 1     David       UK     London
# 2      John   Sweden  Stockholm

## find unique values of a column
df["Name"].unique()

## `drop()` method to remove specific rows or columns,
# axis = 0: by column = column-wise = along the rows
# axis = 1: by row = row-wise = along the columns
dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)
dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)

## `dropna`() removes rows with missing NaN values from the DataFrame
dataframe_name.dropna(axis=0, inplace=True)

## `duplicated()` duplicate or repetitive values or records within a data set.
dataframe_name.duplicated()

## condition filtering
# filtered_df = dataframe_name[(Conditional_statements)]
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]

## `groupby()` slice df into groups based on criteria
# grouped = dataframe_name.groupby(
#     by, axis=0, level=None, as_index=True,
#     sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})

## `pandas.merge()` merge two df
merged_df = pd.merge(df1, df2, on=["column1", "column2"])

## `replace()` replaces specific values in a column with new values.
dataframe_name["column_name"].replace(old_value, new_value, inplace=True)
df["status"].replace("In Progress", "Active", inplace=True)


## access to a specific cell
df.iloc[1,2] # "London", 2nd row and the 3rd col
df.loc[1, "City"] # "London", 2nd row and the 3rd col

df.iloc[1,2:4]
# City      London
# Weight        78
# Name: 1, dtype: object

## comparison
df["age"] > 35
df[df["age"] > 35] # subset rows having age > 35

## save to CSV
df.to_csv("new_file.csv")
```

# Attributes vs. Methods

In Python, attributes and methods are both associated with objects, but they serve different purposes.

- **Attributes** are *variables* that belong to an object. They hold data or state information about the object.

```py
class Car:
    def __init__(self, make, model, color):
        self.make = make     # Attributes
        self.model = model
        self.color = color

my_car = Car('Toyota', 'Camry', 'blue')
print(my_car.color)  # Accessing an attribute
```

- **Methods** are *functions* that belong to an object and define behaviors or actions that the object can perform. Methods can manipulate the object's attributes or perform computations.

```py
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
    
    def drive(self):  # Method
        print(f"The {self.color} {self.make} {self.model} is driving.")

my_car = Car('Toyota', 'Camry', 'blue')
my_car.drive()  # Calling a method
```

# Built-in Function vs. Method

- Built-in Function: A function that is provided by Python and can be used across different types of objects.
For example, `len()` is a built-in function, it can be used with strings, tuples, dictionaries, and custom objects that implement the `__len__()` method.
- Method: A function that is associated with an object and is called on that object.
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

<https://perso.limsi.fr/pointal/_media/python:cours:mementopython3-english.pdf>

<https://www.pythoncheatsheet.org/cheatsheet/built-in-functions>

## PEP 8 - Style guide for Python code

<https://peps.python.org/pep-0008/>

# Unit tests

To automate the tests, we can use the [unittest](https://docs.python.org/3/library/unittest.html) package.
The idea is that in a controlled framework (we know the input and
as the designer of the function we know the output or,
at least, the properties of the output) we can test the output of a function.

The canonical test structure is as follows:

```py
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
```

The equivalent R code would be `testthat::expect_equal(fun(3), 4)`.

# `*args` and `**kwargs`

- `*args`: Used for passing a variable number of positional arguments; treated as a tuple.
- `**kwargs`: Used for passing a variable number of keyword arguments; treated as a dictionary.

```py
def print_args_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Call the function with both positional and keyword arguments
print_args_kwargs(1, 2, 3, name="Alice", age=30, city="New York")

# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30, 'city': 'New York'}
```
