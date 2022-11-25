
#1. create a class Vehicle with below attributes/variables

class Vehicle:
    Brand  =  "Maruti"
    color =  "White"
    Capacity =  4
    Safety   =  True

#2. create an object c1 of class Vehicle and print all the attributes

c1 = Vehicle()
print(c1.Brand)
print(c1.color)
print(c1.Capacity)
print(c1.Safety)


# 3. create an object c2 of class Vehicle , 
# but change the value of Safety as False
# and then  print all the attributes

c2 = Vehicle()
c2.Safety = False
print(c2.Brand)
print(c2.color)
print(c2.Capacity)
print(c2.Safety)


# 4. also check if the class Vehicle can access the attributes/variables
# if yes , then print the attributes

print(Vehicle.Brand)
print(Vehicle.color)
print(Vehicle.Capacity)
print(Vehicle.Safety)

