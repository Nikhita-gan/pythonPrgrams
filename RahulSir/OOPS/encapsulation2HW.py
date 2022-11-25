class bank:
    def __init__(self,name, acc , bal, pin ):
        self.name  = name
        self.acc  = acc
        self.bal  = bal
        #making pin as private

        self.__pin  = pin

    def getPin(self):
        return self.__pin
    
    def setPin(self,newPin):
        self.__pin = newPin
        return self.__pin
        
     
roshan = bank("Roshan", 555 , 1000 , 1234)

#changing the pin value to 1111 by name mangling
print('----changing pin using mangling-----')
roshan._bank__pin = 1111
print(roshan._bank__pin)

#seeting the pin value to 2222 by setter method
print('----changing pin setter and getter methodcd---')
roshan.setPin(2222)
print(roshan.getPin())