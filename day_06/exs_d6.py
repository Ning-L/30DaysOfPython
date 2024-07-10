# Day 6: 30 Days of python programming

# Exercises: Level 1

# 1. Create an empty tuple
empty_tpl = ()
## or
empty_tpl = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("a", "b")
brothers = ("c", "d")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.extend(["papa", "mama"])

# Exercises: Level 2

# 1. Unpack siblings and parents from family_members
type(family_members)
a, b, c, d, *parents = family_members

# 2. Create fruits, vegetables and animal products tuples.
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "peach", "pineapple")
vegetables = ("tomato", "garlic", "cabbage")
animal = ("chicken", "beef", "pork")
food_stuff_tp = fruits + vegetables + animal

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp[len(food_stuff_tp) // 2]
food_stuff_lt[len(food_stuff_lt) // 2]

# 5. Slice out the first three items and the last three items from food_stuff_lt list
food_stuff_lt[:3]
food_stuff_lt[-3:]

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
    # 7-1. Check if 'Estonia' is a nordic country
    # 7-2. Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'Estonia' in nordic_countries # False
'Iceland' in nordic_countries # True