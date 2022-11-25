#################################################
# HW
#################################################

t = (False,False,True,False,True)
#1. CONVERT THE ABOVE  TUPLE INTO A LIST
tList =(list(t))
print(tList)
print(type(tList))
print('-------------------------------------------------------')
#2. FIND THE MEMORY ADDRESS OF BOTH TUPLE AND LIST
print(id(t))
print(id(tList))
print('-------------------------------------------------------')
#3. APPEND 99 AT THE END OF THE LIST
tList[4]=99
print(tList)
print('-------------------------------------------------------')
#4. CONVERT BACK THE LIST  INTO TUPLE
print(tList)
t1 = tuple(tList)
print(t1)
#5. NOW FIND THE MEMORY ADDRESS OF THIS TUPLE
print(id(t1))