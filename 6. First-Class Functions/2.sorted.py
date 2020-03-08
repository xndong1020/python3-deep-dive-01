nums = 8, 2, 9, 3, 1, 6

# sorted always returns a new list
sorted_list = sorted(nums)
print(sorted_list)  # [1, 2, 3, 6, 8, 9]

letters = ["c", "B", "D", "a"]

# when sorting letters, it is using its charCode, not necessarily in alphabetic order
sorted_letters = sorted(letters)
print(sorted_letters)  # ['B', 'D', 'a', 'c']

# to fix
sorted_letters_real = sorted(letters, key=lambda l: l.upper())
print(sorted_letters_real)  #  ['a', 'B', 'c', 'D']


items = {"food": 200, "paper": 300, "mile": 100}
# By default, it is sorted by dictionary keys, and you will get the list of sorted keys
sorted_items = sorted(items)
print(sorted_items)  #  ['food', 'mile', 'paper']

# you can specify to sort by value, but still you will get a list of sorted keys
sorted_items_amount = sorted(items, key=lambda key: items[key])
print(sorted_items_amount)  #  ['mile', 'food', 'paper']  ->  [100, 200, 300]


for key in sorted_items_amount:
    print(items[key])

"""
100
200
300
"""


# How Python sort things if they have same value
students = ["Cleese", "Idle", "Palin", "Chapman", "Gilliam", "Jones"]
students_sorted = sorted(students, key=lambda name: name[-1])
#  ['Cleese', 'Idle', 'Gilliam', 'Palin', 'Chapman', 'Jones']
print(students_sorted)

"""
Why 'Palin' appears before 'Chapman', but the last char of their name are both 'n'?
It is because Python is using "stable sort", which means if 2 things are the same, 
then Python will use the order originally specified in the list which you want to sort
"""
