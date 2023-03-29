# Functions in python

# declaring a function 

def greet(name) :
    print(f"good morning {name}")

greet("aditya") # good morning aditya

def add(a, b) :
    print(f"{a} + {b} = {a+b}")

add(3, 5) # 3 + 5 = 8

# difference btw return and print

def greet(name) :
    return 'hello ' + name
    return "this is it" # this code is un reachable 

print(greet("aditya"))

def returns(a, b) :
    return a+b

print(returns(34,54))

print(returns(34,54) + 23)
# the returned result can be operated further

# returning a boolean

def is_even(number) :
    if number % 2 == 0 :
        print(f"{number} is even")
        return True
    return False

print(is_even(4)) # True
print(is_even(9)) # False

# returning a list

def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

def greetings (name = 'Peter'):
    # on calling the parameter as a different name the name also changes in the returned statement
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings())
print(greetings('Aditya'))

def data(name = 'adi' , section = 'B' , gender = 'male') :
    return f"name is {name} studying in section {section} and also is a {gender}."

print(data(name = 'priyanshu', gender = 'male', section = 'B'))
# these arguments works fine even being randomly placed due to the parameters alloted to them

# Arbitrary Number of Arguments
# If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

def sum_all_nums(*nums) :
    total = 0
    for i in nums :
        total = total + i
    return total

print(sum_all_nums(3,4,5,2,3,5,3,2,2,4,7,80,8,7,6,6))

def data_to_dict(name, section, *friends) :
    frnds_dict = {

    }
    frnds_dict["name"] = name
    frnds_dict["section"] = section
    frnds_list = []
    for friend in friends :
        frnds_list.append(friend)
    print(frnds_list)
    
    frnds_dict["friends"] = frnds_list
    return frnds_dict

print(data_to_dict('aditya' , 'B' , 'priyanshu', 'anurakht', 'tushar', 'archit'))

# print("hello world")

