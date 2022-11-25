# dict??

thisdict = {}
print(type(thisdict))

person = {
    'first_name':'nikhita',
    'last_name':'ganvir',
    'age':33,
    'rollNo':101
}

#retrive
print(person['first_name'])
print(person['last_name'])

#retrive by using get method
p1= person.get('first_name')
print(p1)
p2= person.get('last_name')
print(p2)


#update
person['age'] =35
print(person)


#add
person['city']='Nagpur'
print(person)


#delete
del person['rollNo']
print(person)
print('-----------------------------------')

vehicle = {
    'color':'red',
    'modelNo':'mh122',
    'type':'seden'
}
#retrive
print(vehicle['color'])
print(vehicle['type'])

#update
vehicle['color']='blue'

#add
vehicle['seter'] = 7
print(vehicle)

#delete
del vehicle['modelNo']
print(vehicle)
print('----------------------------------')
# duplicate key in dictionary----
#if duplicate key found in dicctory then it take last one bez it consider as updtaed once

student = {
        'name':'Arpita',
        'marks':225,
        'age':20,
        'marks':250,
        'rollNo':101,
        'branch':'cse'
}
print(student)

##dict with in membership  operator

print('age'   in student)
print('age'  not in  student)

##loop in dict

for key in student:
    print(key)


for values in student:
    print(values)