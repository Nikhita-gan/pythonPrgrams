# there is no inbuilt method to implemnt abstraction


# project : To build house
# Abstraction uses :
    # obj : Everything in the parent class should be written in child class !! 
    # Compulsory impleentation of all methods of parent class 
    # Parent class methods hidden/inaccessible to child class


from  abc import ABC , abstractmethod


class ModelHouse(ABC):
    def Door(self):
        print("Model Door")

    @abstractmethod
    def Window(self):
        print('Model Window')
    def Balcony(self):
        print('Model Balcony')


class DreamHouse(ModelHouse):
    def garden(self):
        print("DreamHouse garden")
    def door(self):
        print("DreamHouse Door")
        print("DreamHouse details")
    def Window(self):
        print('DreamHouse Window')
    def Balcony(self):
        print('DreamHouse Balcony')
    

d1 =  DreamHouse()
d1.garden()
d1.door()
d1.Window()
d1.Balcony()