# Day 5: 30 Days of python programming

### Exercises: Level 1

# 1. Declare an empty list
empty_list = []
empty_list = list()

# 2. Declare a list with more than 5 items
lst_five_items = ["a", "b", "c", "d", "f", "e"]

# 3. Find the length of your list
len(lst_five_items)

# 4. Get the first item, the middle item and the last item of the list
lst_five_items[0] # the 1st item
lst_five_items[len(lst_five_items) - 1] # the last item
lst_five_items[int(len(lst_five_items) / 2)] # the middle item

# 5. Declare a list called mixed_data_types,
# put your(name, age, height, marital status, address)
mixed_data_types = ["Dupont", 20, 165, True, "1 av. Foch"]

# 6. Declare a list variable named it_companies and assign initial values
#  Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list using `print()`
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies) / 2)])
## or
print(it_companies[len(it_companies) // 2])
print(it_companies[len(it_companies) -  1])

# 10. Print the list after modifying one of the companies
it_companies[0] = "X"
print(it_companies)

# 11. Add an IT company to it_companies
it_companies.append("MBS")

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, "middle_company")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()

# 14. Join the it_companies with a string '#; '
'#; '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list.
"ABC" in it_companies

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
it_companies[:2]

# 19. Slice out the last 3 companies from the list
it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
it_companies[len(it_companies) // 2]

# 21. Remove the first IT company from the list
del it_companies[0]
## or 
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
del it_companies[len(it_companies) // 2]
## or
middle_idx = len(it_companies) // 2
it_companies[:middle_idx-1] + it_companies[middle_idx+1:]

# 23. Remove the last IT company from the list
del it_companies[len(it_companies)-1]

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end + back_end
## or
# front_end.extend(back_end)

# 27. After joining the lists in question 26.
# Copy the joined list and assign it to a variable full_stack.
# Then insert Python and SQL after Redux.
full_stack = front_end + back_end
Redux_idx = full_stack.index("Redux")
full_stack.insert(Redux_idx + 1, "Python")
full_stack.insert(Redux_idx + 2, "SQL")

### Exercises: Level 2

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    ## - Sort the list and find the min and max age
ages.sort()
ages[0] # min
ages[len(ages)-1] # max

    ## - Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[len(ages)-1])

    ## - Find the median age (one middle item or two middle items divided by two)
ages.sort()
ages[len(ages) // 2] # 24

    ## - Find the average age (sum of all items divided by their number )
sum(ages) / len(ages) # 22.16

    ## - Find the range of the ages (max minus min)
max(ages) - min(ages) # 7

    ## - Compare the value of (min - average) and (max - average), use `abs()` method
min_age = min(ages)
max_age = max(ages)
avg_age = round(sum(ages) / len(ages), 2)
abs(min_age - avg_age) > abs(max_age - avg_age)

# 2. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
from countries import countries

len(countries) # 193 countries, it's an odd number
countries[len(countries)//2] # middle one is "Lesotho"

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:len(countries)//2] # 96 countries
second_half = countries[len(countries)//2:] # 97 countries

# 4. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'].
# Unpack the first three countries and the rest as scandic countries.
cn, rus, us, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(cn)
print(rus)
print(us)
print(scandic_countries)