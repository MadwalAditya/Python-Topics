# List Comprehension
# List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.

numbers = [i for i in range(11)] # 1 to 10 list
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [i*i for i in range(11)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# numbers and aquares

list3 = [(i , i*i) for i in range(11)]
print(list3)
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]

list4 = [[i , f"square is {i*i}"] for i in range(11)]
print(list4)

# list comprehension with conditionals

# even no.s list
even = [i for i in range(11) if i % 2 == 0]
print(even)
# [0, 2, 4, 6, 8, 10]

# odd no.s list
odd = [i for i in range(11) if i % 2 != 0]
print(odd)  
# [1, 3, 5, 7, 9]

