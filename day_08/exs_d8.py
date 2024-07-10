# Day 8: 30 Days of python programming

# 1. Create an empty dictionary called dog
dog = dict()
## or
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Milou",
    "color": "white",
    "breed": "Wire Fox Terrier",
    "age": "3"
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status,
# skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Dupond",
    "last_name": "Grand",
    "gender": "unspecified",
    "age": 25,
    "marital status": "married",
    "skills": ["Python", "R"],
    "country": "France",
    "city": "Paris",
    "address": "1 rue Foch"
}

# 4. Get the length of the student dictionary
len(student) # 9

# 5. Get the value of skills and check the data type, it should be a list
student["skills"] # ['Python', 'R']
type(student["skills"])

# 6. Modify the skills values by adding one or two skills
student["skills"].extend(["CSS", "HTML"])

# 7. Get the dictionary keys as a list
the_keys = list(student.keys())

# 8. Get the dictionary values as a list
the_values = list(student.values())

# 9. Change the dictionary to a list of tuples using items() method
student_list = student.items()
# student_list[0] # TypeError: 'dict_items' object is not subscriptable
list(student_list)[0]

# 10. Delete one of the items in the dictionary
del student["age"]

# 11. Delete one of the dictionaries
del student