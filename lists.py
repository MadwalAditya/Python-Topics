# lists in python

names = ['aditya', 'ayush', 'rahul', 'riya']
print(names)

# length of the list
print(len(names)) # 4

# indexing in a list

name_1 = names[0] # aditya
print(f"first name is {name_1}")

names[0] = "abhimanyu" # name_1 changed to abhimanyu from aditya
print(names)

names[0] = 'aditya'

siblings = names[0:2]
print(siblings)

names.append('abhimanyu')
print(names)

print(names.index('aditya'))

# sorting 

numbers = [1,23,56,6,23,564,35,5,354,3]

# deleting or removing some items 

fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']

del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']

del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']

del fruits          # whole fruits removed
# print(fruits)       # This should give: NameError: name 'fruits' is not defined

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []

