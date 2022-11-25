person = {
    'firstName':'Swapnil',
    'lastName':'GAnvir',
    'age':32,
    'skills':['C',"c++","Python","Javascript"]
}

#retrive

print(person['firstName'])
print(person['age'])

#update

person['age']=33
print(person)

#add

person['city'] = 'Nagpur'
print(person)


#delete

del(person['age'])
print(person)

#length
print(len(person))


student = {

    'firstName':"Nikhita",
    'lastName':"Jambhule",
    'rollNo':120,
    'subject':["english","Marathi","Math","science"]

}

#in---give the boolean value

print('rollNo' in student)

print('age' in student)

#not---give the boolean (if the property is not in dict then it give true)

print('age' not in student)



#copy====when we copy the one dict into another,if we update the property of new 
# dict then privous dict proprty also updated
vehicle = {
    'color':"red",
    "type":"seden"
}

vehicle2 = vehicle

vehicle2['color']='blue'
print(vehicle2)
print(vehicle)


#loop

student2 = {
    'firstName':"Priya",
    'lastName':"Raut",
    'age':30,
    "subject":["Marathi","hindi","English","Computer"]
}

for x in student2:
    print(x,student2[x])


#dictionary Method
#clear()----clear the dict

#student2.clear()
print(student2)

#copy ---copy the one dict into another dict but when we update the property 
#of new dict privious dict property could not be change

student3 = student2.copy()

student3['age']=32

print(student3)
print(student2)

#get=====get the value of the property

s1 = student2.get('firstName')
print(s1)

s2 = student2.get('age')
print(s2)

for key in student2.keys():
    print(key)



for value in student2.values():
    print(value)



for key,value in student2.items():
    print(key,value)



#update()----update the property of the dict

student2.update({'firstName':"Pri","age":25})
print(student2)

#pop()---to remove the perticular property from the dict

student2.pop('age')
print(student2)




#fromkeys()
#           key         key     key
keys = ["student1","student2","student3"]

y = None #value
d = dict.fromkeys(keys,y)
print(d)

#{'student1': None, 'student2': None, 'student3': None}

# setDefault()

student = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    "age":23,
    "skills":["pyhton","javascript"],
}

student.setdefault('city','pune')
print(student)