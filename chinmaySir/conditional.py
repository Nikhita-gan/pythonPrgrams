# 333conditional statement 

q = 11
t = 5

print("q is greater") if q > t else print("t is greater")

if(q > t):
    print("q is greater")
else :
    print("t is greater")

# not 

# program 2
animals = ["Cow","Dog","sheep","Cat"]
print("apple" in animals)
print("Dog" not in animals)

if("Cow" in animals):
    print('Cow is avaliable in animal')
else:
    print("cow is not availabe in animal")

if("rat"  not in animals):
    print('rat is not avaliable in animals')
else:
    print("rat is availabe in animals")



#program3

math = int(input('enter the math marks:'))
che = int(input('enter the che marks:'))
phy = int(input('enter the phy marks:'))
per = print((math+che+phy)/3)



# program 4

m1 = int(input('Enter the maths marks:'))
m2 = int(input('Enter the physics marks: '))
m3 = int(input('Enter the chemistry marks: '))

#print(type(m1))
print((m1+m2+m3)/3)

print("The marks for maths {}".format(m1))
print("The marks for chemistry {}".format(m2))
print("The marks for physics {}".format(m3))

print(float(23))
print(str(34))
print(int('34'))