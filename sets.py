# defining a set 
# a set is totally unordered 
# prints in random order

st = {}
#or 
st = set()

st = {'item', 'item2', 'item3', 'item4'}
print(st)

print(len(st)) # 4

print("item4" in st) # True

# adding an item

st.add('item5')
print(st)

# adding multiple items
new_items = ('new1', 'new2')
st.update(new_items)
print(st)

# removing a set

st.remove('item3') # removes the item3

randomly_removed_item = st.pop() # randomly removes any item from the set 

print(st)

st.clear() # empties the set

del st # deletes the whole set 

# converting into a set

num = [1,23,45,56,33,33,68,907,3]
print(num)

set_of_num = set(num) # converts the list into set 
# also removes the extra 33 coz set doesnt include repitition
print(set_of_num)

cllg = {
	"tushar",
	"rohit",
	"archit"
}

schl = {
	"tushar",
	"dimri",
	"govind"
}

print(cllg.intersection(schl)) # "tushar" the common item from both sets

print(cllg.difference(schl)) # prints everyone excepts "tushar"


# symmetric difference btw 2 sets 
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# joining sets 

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False

even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
