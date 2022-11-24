# Operations on strings.
print("operations on strings.")

# a string

line1 = "i am dancing in the dark, with you between my arms."
print(line1)

# multiline strings

multiline_string = '''
aditya madwal 
ayush madwal
mamta madwal
pitamber dutt
givindi devi
'''
print(multiline_string)

# line breaks
string2 = "i am dancing\nin the dark\nwith you between my arms."
print(string2)

first_name = 'aditya'
last_name = 'madwal'

full_name = first_name + " " + last_name # we have to add the space in between
print(full_name)

print(len(first_name)) # 6 
print(len(last_name)) # 6
print(len(full_name)) # 13
 
print(len(full_name) > len(first_name)) # True
print("--------------------------")

# making a table out of a string

print('name\tmarks\tbranch')
print('aditya\t94\tCS')
print('anurkt\t93\tIT')
print('tushar\t97\tCSIT')

# how to write a double lash inside a single/double slashed string

print("my name is \"aditya madwal\"")
print('my name is "aditya madwal"')

# formating a string 

# adding two no.s

add = '{} + {} = {}'

print(add.format(3 , 4 , 3+4))

# STRING FORMATTING :


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# # output
# 4 + 3 = 7
# 4 - 3 = 1
# 4 * 3 = 12
# 4 / 3 = 1.33
# 4 % 3 = 1
# 4 // 3 = 1
# 4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)

# indexing of a string 

language = 'Python'

first_letter = language[0]
print(first_letter) # P

second_letter = language[1]
print(second_letter) # y

last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# string methods :

sample_string = "a lebrader dog sitting under the tree"

