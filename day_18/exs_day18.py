# Day 18: 30 Days of python programming

# Exercises: Level 1

# 1. What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re

## 1/ splite string into words
words = re.split(pattern = "[ |\. ]", string = paragraph)
## 2/ count occurrence
count = {word: words.count(word) for word in words}
# or
count = {}
for item in words:
    count[item] = count.get(item, 0) + 1
## 3/ sort count
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
print("The most frequent word is:", sorted_count[0][0])


# 2. "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
#  Extract these numbers from this whole text and find the distance between the two furthest particles.
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20

import re

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
numbers = re.findall(pattern = "([-]?[0-9]+)", string = text) # extract number text
numbers_sorted = sorted(list(map(int, numbers))) # convert to int and sort
print(
    'distance between the two furthest particles is', 
    f'{max(numbers_sorted)} - ({min(numbers_sorted)}) = {max(numbers_sorted) - min(numbers_sorted)}'
)
# distance between the two furthest particles is 8 - (-12) = 20


# Exercises: Level 2

# 1. Write a pattern which identifies if a string is a valid python variable
import re
def is_valid_variable(name):
    pattern = "^[a-zA-Z_]*$"
    return bool(re.match(pattern, name))

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True


# Exercises: Level 3

# 1. Clean the following text. After cleaning, count three most frequent words in the string.

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# clean_text = re.sub(pattern = "[^a-zA-Z\s\.,\?\!]", repl = "", string = sentence) # remove special characters
cleaned_text = re.sub(pattern = "[^a-zA-Z\s]", repl = "", string = sentence) # keep only words and spaces


# print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher

def most_frequent_words(text, n_most = 3):
    # a/ split text into words
    words = re.split(pattern = "[ |\. ]", string = text)
    # b/ count occurrence using dictionary
    count = {word: words.count(word) for word in words}
    # c/ sort the dictionary
    sorted_count = sorted(count.items(), key = lambda x: x[1], reverse = True)
    # d/ output the most frequent
    return sorted_count[:n_most]
    
most_frequent_words(cleaned_text) 
# [(3, 'I'), (2, 'teaching'), (2, 'teacher')]