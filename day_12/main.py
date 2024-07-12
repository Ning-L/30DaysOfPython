# main.py file
# import mymodule
from mymodule import generate_full_name as fullname, sum_two_nums, person, gravity
print(fullname('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

print(mymodule.sum_two_nums(1, 9))

mass = 100
weight = mass * mymodule.gravity

print(weight)
print(mymodule.person["first_name"])