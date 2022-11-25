

# operators 

# 1)comparison  operator
# 2)logical operator

# < , > , == , !=  <= , >=
# entity < entity  ==================> boolean
# <  ==> less than
# >  ==> greate than
# <=  ==> less than or equal to
# >=  ==> greater then or equal to
# ==  ==> equal tham
# !=  ==> not equal

a = 10
b = 20
print(a < b)
print(11 < 10)  
print(33 > 12)  
print(11 <= 11) 
print(12 >= 11) 
print(12 >= 12) 
print(33 == 4)  
print(22 != 4)  
print(11 == 23) 

# or and  not

# and
# True  and  True  ==> True
# False and  True  ==> False
# True  and  False ==> False
# False and  False ==> False

#or

# True  or  True  ==> True
# False or  True  ==> True
# True  or  False ==> True
# False or  False ==> False

# not 

#True ==> False
#False ==> True 



print(12 < 13 and 7 == 7)   # True
print(12 >= 13 and 7 != 6)  # False
print(12 == 11 and 7 == 8)  # False
print(12 > 11 and 7 == 8)   #False



print(12 < 13 or 7 == 7)    # True
print(12 >= 13 or 7 != 6)   # True
print(12 == 11 or 7 == 8)   # False
print(12 > 11 or 7 == 8)    # True

print(not True)
print(not False)
print(not 8==8)


# conditional statement 
# single input =====>    multiple statement


#numberOfT > 0 and  numberOfT <= 5  ===> 5%
#numberOfT > 5 and  numberOfT <= 10 ===> 10%
#numberOfT > 10                     ===> 30%

# if(condition):
#     # statement 1
# else:
#     # statement 2


numberOfT = 7
if(numberOfT  > 0 and numberOfT <= 5):
    print(" 5 % discount ")

if(numberOfT  > 5 and numberOfT <= 10):
    print('10 % disocunt')

if(numberOfT  > 10):
    print('30 % disocunt')



numTicket = 4

if(numTicket > 0 and numTicket <=5):
    print(' 5% discounts')

elif(numTicket <5 and numTicket <= 10):
    print('10% discount')
    
elif(numTicket >10):
    print('20% discount')


marksA = 66

#when we use if conditional statement it check very if statement and we get incorrect output
if(marksA > 90):
    print('Grade A')
if(marksA > 75):
    print('Grade B')
if(marksA > 65):
    print('Grade C')



#if---elif check first condition if first condition is wrong then goes to second
#agin elif condition is wromg check third condition
#so we get correct output

marksA = 70

if(marksA > 90):
    print('Grade A')
elif(marksA > 75):
    print('Grade B')
elif(marksA > 65):
    print('Grade C')
