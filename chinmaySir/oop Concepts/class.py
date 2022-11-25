#program 
class Student:
    #constructor define
    def __init__(self,name,roll,age):
        self.name = name
        self.roll = roll
        self.age = age

    def displayName(self):
        print(self.name)

orvi = Student("orvi kumar",29,33)
amar = Student("amar rao",34,56)

print(orvi.name)
print(orvi.age)
print(orvi.roll)

print(amar.name)
print(amar.age)
print(amar.roll)


#program


class Sample:
    def __init__(self):
        # instance  variable
        self.x = 10

    def modify(self):
        self.x = self.x+1

q1 = Sample()
q2 = Sample()

print(q1.x)
print(q2.x)

q1.modify()
print(q1.x)

print(q2.x)


class Student2:
    # class variable
    language ="hindi"
    def __init__(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno
    
    def display(self):
        print(self.name)


nitesh = Student2('nitesh',31,101)
nitesh.display()







class Student3:
    # class variable
    language ="hindi"
    def __init__(self,name,age,rollNo):
        self.name = name
        self.age = age
        self.rollNo = rollNo

    def displayName(self):
        print(self.name)

    @classmethod
    def modifyLanguage(cls):
        cls.language = "marathi"

vikas = Student3("vikas",23,34)
sarika = Student3("sarika",33,44)

print(vikas.language)
print(sarika.language)

print(sarika.name)
print(sarika.rollNo)
print(sarika.age)

print(vikas.name)
print(vikas.rollNo)
print(vikas.age)

vikas.modifyLanguage()
print(vikas.language)
print(sarika.language)