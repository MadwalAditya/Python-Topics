# LOOPS IN PYTHON :-
print("loops in python.")

# while loop :

count = 0

while count < 5 :
    print(count)
    count += 1
    # print(count) # this print 1 2 3 4 5 coz it starts after +1 the count that is 0 becomes 1 and goes uuntil 5.

# while loop with a code break and else statement :-
    
while count < 5 :
    print(count)
    count += 1
    # count goes from 0 to 4
    # the code breaks 
else :
    print("the code goes wrong now !")
    # this is when the condition is ful filled

while count < 10 :
    print(count) 
    count += 1

    if count == 7 :
        print("the count reached 7.")
        print("loop broke")
        break

# ----------------------------------------------------------------
    
# for loop :-

numbers = [0, 1, 2, 3, 4, 5]
square_numbers = []

for n in numbers: 
    # n is temporary name to refer to the list's items, valid only inside this loop
    print(n) # the numbers will be printed line by line, from 0 to 5
# using loop to square numbers in a list :
for number in numbers :
    number = number*number
    print(number)
    square_numbers.append(number)    

print(square_numbers)

name = "rammamuttu iyer swami"

for letter in name :
    print(letter)
    # this prints one by one every letter in the name (including the spaces)

length_name = len(name)
print(length_name)

for i in range(len(name)) :
    # len(name) is the character length of the name !
    print(name[i]) # prints the same

    if i == 4 :
        print("loop reached 4th index so broke.")
        break

# for loop in tuple :

numbers_tuple = (0,1,2,3,4,5)

for number in numbers_tuple:
    print(number)
    if number == 3:
        break


