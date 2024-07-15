# Day 13: 30 Days of python programming

# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
[i for i in numbers if i <= 0] # [-4, -3, -2, -1, 0]


# 2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
[i for lst in list_of_lists for sublist in lst for i in sublist]
## output
##[1, 2, 3, 4, 5, 6, 7, 8, 9]


# 3. Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
[(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
## or
[(i, 1) + tuple(i**j for j in range(1, 6)) for i in range(11)] # iterate on exponent and on number, bind two tuples


# 4.Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
## output:
## [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
[
    [country[0].upper(), country[0][:3].upper(), country[1].upper()]
    for sublist in countries # each sublist is `[('Finland', 'Helsinki')]`
    for country in sublist # each country is the tuple `('Finland', 'Helsinki')`
]



# 5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
## output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
[
    {'country': country[0].upper(), 'city': country[1].upper()}
    for sublist in countries # each sublist is `[('Finland', 'Helsinki')]`
    for country in sublist # each country is the tuple `('Finland', 'Helsinki')`
]


# 6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
## output
## ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
[
    pair[0] + ' ' + pair[1] # concatenate strings
    for sublist in names
    for pair in sublist
]
## or
[
    f"{pair[0]} {pair[1]}" # using fstring format
    for sublist in names
    for pair in sublist
]
