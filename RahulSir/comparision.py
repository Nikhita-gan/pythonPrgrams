# COMPARISON
'''
Python supports the usual comparison conditions from mathematics:
Equals:                     a == b
Not Equals:                 a != b
Less than:                  a < b
Less than or equal to:      a <= b
Greater than:               a > b
Greater than or equal to:   a >= b
'''


# Logical operators
#  AND , OR ,NOT 
# Identity operators
#  IS , NOT IS 
# Membership operators
# IN , NOT IN 


###################comparison

a = 100
b = 200
c = 200
d = 500
print(a > b)
print(a < b)
print(b == c) # comparison "=="

# logical 
print(a > b and  b==c)
print(d > c and b > a)


print("****OR***")
print(d > a or c > d)



# ########## membership

print("****membership***")

name1 = "nik"
print("a" in name1)

list1  = [2,4,6,8,10,12]
print(22 in list1)
print(22 not in list1)

##### CONDITIONAL STATEMENT IN PYTHON


a = 10
b = 20
c = 20
d = 50

#SYNTAX
# if <condition>: #condition has to be true 
#     <code>
# else: #
#     <code>



if b > a :
    print(" B is greater than A")


marks = 55

if marks > 45:
    print("Congratualation! You hav passed the test")
else:
    print("Soory! Try next Time")




# ####### input() AND TYPE CASTING

fname =input("Enter Your FirstName:")
lname = input("Enter you lastName:")

print("You full name is :{} {}".format(fname,lname))


marks = input("Enter your marks: ")
print("your marks are {}".format(marks))


p = int(input("Enter marks of Physics : "))
c = int(input("Enter marks of Chem : "))
m = int(input("Enter marks of Maths : "))
average = (p+c+m)/3
print(average)


print("your marks are {}".format(p))
print("your marks are {}".format(c))
print("your marks are {}".format(m))
print("your marks are:{} {} {} ".format(p,c,m))

print(type(p))
print(type(c))
print(type(m))



if average > 35 :
    print("Pass")
else:
    print("Try next time")


# eg: 
# voting age


age_candidate = int(input(" Enter your age :"))
print("your age is : {}".format(age_candidate))


if age_candidate >= 18: # boundary condition
    print(" You are eligible for voting")
else:
    print(" You are not  eligible for voting")