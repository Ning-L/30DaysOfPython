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

# Day 3

## Operators

### Assignment

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

### Comparison

Apart from the ordinary comparison operators such as `>`, `<`, `==`, `!=`,
Python uses also the following keywords for comparison:

* *is*: Returns `True` if both variables are (point to) the same object (`x is y`) (equivalent to `identical() `in R)
* *is not*: Returns `True` if both variables are not the same object (`x is not y`)
* *in*: Returns `True` if the queried list contains a certain item (`x in y`) (equivalent to `%in%`in R)
* *not in*: Returns `True` if the queried list doesn't have a certain item (`x in y`)

### Logical operators

| Python  |     R    |
|:-------:|:--------:|
| a and b | and & b  |
| a or b  | and \| b |
| not a   | ! a      |

