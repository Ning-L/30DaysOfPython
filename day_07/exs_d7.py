# Day 7: 30 Days of python programming

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
# 1. Find the length of the set it_companies
len(it_companies) # 7

# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["company1", "company2"])

# 4. Remove one of the companies from the set it_companies
it_companies.remove("company1")
it_companies.remove("company3")
it_companies.discard("Twitter")
it_companies.discard("company3")

# 5. What is the difference between remove and discard
## `remove()` method will raise error if item not found,
## while `discard()` method will simply do nothing if the speficied item not found.


# Exercises: Level 2
# 1. Join A and B
C = A.union(B) # no diplicates items as it's a set

# 2. Find A intersection B
A.intersection(B) # {19, 20, 22, 24, 25, 26}

# 3. Is A subset of B
A.issubset(B) # True

# 4. Are A and B disjoint sets
A.isdisjoint(B) # False, because there are common items

# 5. Join A with B and B with A
A.union(B)
B.union(A)

# 6. What is the symmetric difference between A and B
A.symmetric_difference(B) # {27, 28}

# 7. Delete the sets completely
del A, B, C

# Exercises: Level 3
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_set = set(age)
len(age) == len(ages_set) # False
len(age) # 8, bigger length
len(ages_set) # 5

# 2. Explain the difference between the following data types: string, list, tuple and set
## string is a sequence of characters
## list is a collection of items, it's ordered, changeable, can contain duplicates
## tuple is a collection of items, it's ordered, non changeable, can contain duplicates
## set is a collection of items, it's unordered, changeable, cannot contain duplicates

# 3. "I am a teacher and I love to inspire and teach people."
# How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split(" ")
print("Number of unique words used is: ", len(set(words))) # 10 unique words