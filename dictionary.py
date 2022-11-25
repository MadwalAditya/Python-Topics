# Dictionaries in python

dictionary = {
    'name' : 'aditya',
    'marks' : 94,
    'branch' : 'Computer Science',
}

print(dictionary)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,   
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print(len(person)) # 7 reads only the keys

print(person['last_name'])
print(person['skills'][2]) # since skills containa list
print(person['address']['zipcode'])

# adding item
person['nature'] = 'friendly'

# removing
del person['is_marred']

person.popitem() # removes the last item

person.clear() # clears the whole dictionary
print(person) # {}

