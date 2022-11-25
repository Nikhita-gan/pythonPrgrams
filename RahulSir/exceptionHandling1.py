# REVISION EXCEPTION HANDLING

try:
    list_num = [0,1,2,3,4]
    print(list_num[0])
    print(10/0)
except IndexError as e:
    print("Some error occured" , e )
except ZeroDivisionError as e:
    print("Some error occured" , e )

else:
    print("Code exected successfully")

finally:
    print(" This will print irrespective of code status")


print("Welcome to Pune")



# user defined exception


# x = int(input("Enter an even number !!!"))
# if x %2 != 0:
#     raise Exception("Enter only even number")
# else:
#     print("The number is even ")

def div1(a):
    # a = int(input("Enter an non zero number !!!"))
    if a == 0:
        raise ZeroDivisionError("Enter a non zero num")
    else:
        print(100/a)


div1(10)
div1(0)