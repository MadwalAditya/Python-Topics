my_list = []

do_continue = True

name = input("enter a name : ")

while do_continue :
    
    continue_or_not = input("add another name ?(y/n) : ")
    my_list.append(name)
    if continue_or_not == 'y' :
        name = input("enter another name : ")

    else :
        do_continue = False
        print(my_list) 

