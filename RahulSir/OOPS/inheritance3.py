# Inheritance
    # single
        # Method over riding
    # multiple
        # MRO Method resolution Objective
        # super()
    # multi level

    # Next class how to inherit constructor
        # _init_ 
        
# Encapsulation
    # private /protected
# Abstraction
# Polymorphism
# Inheritance


# revision

class Person:
    def person_info(self,name,age):
        self.name = name
        self.age =  age

    def character(self):
        print("Good Citizen")


class Employee(Person):
    def emp_info(self, salary):
        self.salary = salary

    def character(self):
        print("Good manager")

p1 =  Person()
p1.person_info("mahesh" , 2)
print(p1.name , p1.age)


p1.character()
e1 = Employee()

e1.character()
p1.character()



# MRO
class Person:
    def person_info(self,name,age):
        self.name = name
        self.age =  age

class Company1:
    def comp_info_reg(self):
        print("Google")
    def star(self):
        print("Star emp at Google")
    def views(self):
        print("You have 100 views in Google review")

class Company2:
    def comp_info_free(self):
        print("Youtube")
    def star(self):
        print("Star emp at Youtube")
    def views(self):
        print("You have 100 views in Youtube")



# class Employee(Person, Company1,Company2):
class Employee(Person, Company2,Company1):
    def emp_info(self, salary):
        self.salary = salary

    def character(self):
        print("Good manager")
        super().views()


p1 =  Person()
p1.person_info("mahesh" , 2)
print(p1.name , p1.age)

e1 = Employee()
e1.star()
    
# multi level

class Parent:
    def Pinfo():
        print(" Parents Property")

class Child(Parent):
    print(" Childs Property")

class GrCHild(Child):
    print(" Grand Child's Property")

class Nchild(GrCHild):
    print(" Nth  Child's Property")

c1= GrCHild()
n1 = Nchild() # we can go upto n level of inheritance


# constructor in inheritance


class Vehicle:
    def _init_(self, company, milage):
        print("I am Vehicle")
        self.company = company
        self.milage = milage


class Car(Vehicle):
    # def _init_(self) -> None:
    #     print("I am Car")
    def _init_(self, company, milage):
        super()._init_(company, milage)
        print("I am Car")
        print(company)
        print(milage)

c1 = Car("maruti" , 150)