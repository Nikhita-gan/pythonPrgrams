##Methos of srting

# upper() :It convert all the char of string into upper case
name = "Nikhita"
n1 = name.upper()
print(n1)

animal = "elephant"
a1 = animal.upper()
print(a1)


#lower(): It convert the all char of string into lower case
nameA = "Nikhita"
n2 = name.lower()
print(n2)

animalA= "elephant"
a2 = animal.lower()
print(a2)

# isupper(): IT check the all the char of string is in upper case or not.If all char of string is in upper case then it return true

city = "Chandrapur"
c1 = city.isupper()
print(c1)


city1 = "NAGPUR"
c2 = city1.isupper()
print(c2)


# islower()
city3 = "Nashik"
c4 = city3.islower()
print(c4)


city4 = "nagbhid"
c5 = city4.islower()
print(c5)


#capitalize()

fruit = "apple" 
f = fruit.capitalize()
print(f)

fruit1 = "orange" 
f1 = fruit1.capitalize()
print(f1)

#startswith()

vegetable = "tomato"
v1 = vegetable.startswith("tom")
print(v1)


vegetable1 = "carrot"
v2 = vegetable1.startswith("rro")
print(v2)
#endswith()
fruit2 = "chikko"
f2 = fruit2.endswith("ko")
print(f2)

fruit3 = "cabbage"
f3 = fruit3.endswith("agr")
print(f3)

#index
#       0   1   2   3   4   5   6   7   8   9   10  11
#       w   a   t   e   r   m   e   l   o   o   a   n
fruitA = "Watermeloan"
fA = fruitA.index("m")
print(fA)

#count 
fb = fruitA.count("e")
print(fb)

fc = fruitA.count("a")
print(fc)

fd = fruitA.count("w")
print(fd)

# replace
string1 = """I am learning javascript.
I am very glad"""
s1 = string1.replace('javascript','python')
print(s1)