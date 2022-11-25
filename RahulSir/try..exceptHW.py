

# 1. catch exception in below code using try... except 
# else print " Code Execution was successful"

try:
    list_z = [1,2,3,"a"]
    for i in range(5):
        if type(list_z[i]) == int:
            print("This is int")
        else:
            print("This is not int") 
except IndexError as e:
    print('error occure is:',e)
else:
    print('code excution was succesfully')



# 2. catch exception in below code using try... except
# else print " Code Execution was successful"

# f = open(r"one.txt")
# print(f.read())

# also close the file irrespective of operation on file

# 3. catch exception in below code using try... except

print("Nikhita\tGanvir")

