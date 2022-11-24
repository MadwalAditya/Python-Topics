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

