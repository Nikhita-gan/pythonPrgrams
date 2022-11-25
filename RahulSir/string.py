# String
####string Formating
a = 10
b = 100
c=a + b

print("the value of a is:",a)
print("the value of a is:",b)
print("the value of a is:",c)

print("the values of",10,"+",100,"is",c)
print("the value of",a,"+",b,"is:",c)

print('---------------------------------------------------')

print('the value of {} + {} is: {}'.format(a,b,c))

n1 = "POOJA"
n2 = "Nikhil"
n3 = "Anjali"

print("The student are {0},{1},{2}".format(n1,n2,n3))
print("The student are {},{},{}".format(n1,n2,n3))

print("------------------------------------------------------------------")

x ="My name"
y = "is"
z= "Jhon"

print(x,y,z)

print("He said that ",x,y,z)

print("----------------------------------------------------------")

print("He said that {} {} {}".format(x,y,z))
print("He said that {0} {1} {2}".format(x,y,z))
print("he () said {2} {1} {0}".format(x,y,z) )# according ti o index giving inside {}

print("-------------------------------------------------------------")

a1 = "zero"
a2 = "one"
a3 = "Two"

print("thw value is:{} {} {}".format(a1,a2,a3))
print("thw value is:{0} {1} {2}".format(a1,a2,a3))
print("thw value is:{1} {0} {2}".format(a1,a2,a3))

print("thw value is:{} {} {}".format(a2,a3,a1))
print("thw value is:{} {} {}".format(a2,a1,a3))
print("thw value is:{} {} {}".format(a3,a1,a2,))
