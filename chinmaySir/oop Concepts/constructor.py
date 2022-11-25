# program 
class StudentA:
    def __init__(self):
        self.name = "Aman"
        self.age = 32
        self.marks = 500
    def talk(self):
        print('Hi my name is ',self.name)
        print('Hi my age is ',self.age)
        print('Hi my marks is ',self.marks)

s1 = StudentA()
s1.talk()
print('--------------------------------------')
s2 = StudentA()
s2.talk()

# program 2

class Vehicle:
    def __init__(self,color,modelNo,seater):
        self.color = color
        self.modelNo = modelNo
        self.seater = seater
    
    def displayFeatures(self):
        print('The color of vehicle is :',self.color)
        print('The color of vehicle is :',self.modelNo)
        print('The color of vehicle is :',self.seater)

        
v1 = Vehicle('red','SUV 542',6)
v1.displayFeatures()
print('--------------------------------')
v2 = Vehicle('black','Xylo 451',7)
v2.displayFeatures()   

# program3

class StudentC:
    # class level variable
    language = "hindi"

    def __init__(self,name,age,marks):
        self.name = name
        self.age = age 
        self.marks  = marks


    # instance varaible
    def talk(self):
        print('Hi my name is ',self.name)
        print('Hi my age is ',self.age)
        print('Hi my marks is ',self.marks)
        print('Hi my marks is ',self.language)

    #class method 
    @classmethod()
    def changeLang(cls):
        cls.language = "English"



sarika = StudentC("sarika",24,700)
poorva = StudentC("sarika",24,700)

print(sarika.language)
print(poorva.language)

sarika.talk()

sarika.changeLang()
print(sarika.language)
print(poorva.language)
    
sarika.language = "english"
print(sarika.language)
print(poorva.language)

# Accessor and mutators
# get and set

class StudentD:
    def setName(self,name):
        self.name = name
  
    def getName(self):
        return self.name
    ####################################
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age

    ###################################
    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self):
        return self.marks

chinmayD = StudentD()
chinmayD.setMarks(900)
chinmayD.setName("chinmay D")
chinmayD.setAge(32)

age = chinmayD.getAge()
marks = chinmayD.getAge()
name = chinmayD.getName()
print(age)
print(marks)
print(name)

# // hardcode value 
# // constructor (hardvalues)
# // passing parameter to constructor 
# // using mutators and accessors
class Bird:
    wings = 2

    @classmethod
    def fly(cls,birdName):
        print("I have",cls.wings,"wings",birdName)


# Bird.fly('pigeon')
# Bird.fly('sparrow')