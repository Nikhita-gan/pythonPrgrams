# Inheritance

# class Student():
#     def __init__(self ,name,age,adharNo):
#         self.name = name
#         self.age = age
#         self.adharNo = adharNo

#     def displayName(self):
#         print(self.name)


# # Case 3

# class Teacher(Student):
#     salary = 1000

# t1 = Teacher("Vikaram",34,124)
# print(t1.salary)
# print(t1.age)
# print(t1.adharNo)

# t1.displayName()


# #case- | no relationship()
# # chinmayT = Teacher()
# print(t1.salary)

# # case-I 
# s1 = Student("vaishali",32,123)
# print(s1.name)
# print(s1.age)
# print(s1.adharNo)
# s1.displayName()
############################################################
##Single inherutance###

class Student:
    def __init__(self,name, age , rollNo):
        self.name = name 
        self.age = age 
        self.rollNo = rollNo
    def displayName(self):
        print(self.name ,self.age ,self.rollNo)


class Teacher(Student):
    def __init__(self,name,age,rollNo,salary):
        super().__init__(name,age,rollNo)
        self.salary = salary


t1 = Teacher("Avinash",25,101,50000)
t1.name
t1.age
t1.rollNo
t1.salary
t1.displayName()

##################################################################3
#multilevel Inheritance

class Student():
    def __init__(self,fullName,age):
        self.fullName = fullName
        self.age = age

    def displayFullName(self):
        print(self.fullName)

class Teacher(Student):
    def __init__(self,fullName, age ,salary):
        super().__init__(fullName,age)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)


class Professor(Teacher):
    def __init__(self,fullName, age ,salary,spec):
        super().__init__(fullName, age ,salary)
        self.specialization = spec

    def displaySpec(self):
        print(self.fullName, self.specialization)


p1 = Professor("Atul Sharma",23,50000,'Biology') 

print(p1.fullName)
print(p1.age)
print(p1.salary)
print(p1.specialization)

p1.displayFullName()
p1.displaySalary()
p1.displaySpec()


# #  1 parent two childs

class Father():
    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def display(self):
        print(self.firstName , self.lastName)
    

class Son(Father):

    def __init__(self,firstName,lastName,sname):
        super().__init__(firstName,lastName)
        self.sname = sname

    def sdisplay(self):
        print(self.sname , self.lastName)
    

class Daughter(Father):
    def __init__(self,firstName,lastName,dname):
        super().__init__(firstName,lastName)
        self.dname = dname

    def ddisplay(self):
        print(self.dname , self.lastName)

Alisha = Daughter('Swapnil',"Ganvir","Alisha")
Athrav = Son('Swapnil',"Ganvir","Athrav")

Alisha.ddisplay()
Athrav.sdisplay()



# # Method order resolution


class FatherA:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print(self.firstName+self.lastName)
        print('Father method called')

class MotherA:
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print(self.firstName+self.lastName)
        print('Mother method called')

class SonB(MotherA,FatherA):
    pass
sb = SonB("vikas","jain")
sb.displayName()

# #--------------------------------------------

# class A(object):
#     def method(self):
#         print('A method called ') #3
#         super().method()

# class B(object):
#     def method(self):
#         print('B method called ') # 5
#         super().method()

# class C(object):
#     def method(self):
#         print('C method called ')  #6
     

# class X(A,B):
#     def method(self):
#         print('X method called ')  # 2
#         super().method()

# class Y(B,C):
#     def method(self):
#         print('Y method called ')   # 4
#         super().method()

# class P(X,Y,C):
#     def method(self):
#         print('P method called ') #1 
#         super().method()

# p = P()
# p.method()


