
# marks = input('enter your marks:')
# print('Your marks are: {}'.format(marks))

# print(type(marks))#----->it give the string even you enter the number 

# marks = int(input('enter your marks:'))#--->it convert str into integer
# print("Your marks are{}:".format(marks))

# print(type(marks))

print('----------------------------------------------------------')

#############if,elif,else

marks = 89

if(marks > 90):
    print('Grade A')
if(marks > 80):
    print('Grade B')
if(marks > 60):
    print('Grade C')
###Grade B
###Grade C
###   When we use if staement it check very if statement it give incorrect answer
print('--------------------------------------------------------')
if(marks > 90):
    print('Grade A')
elif(marks < 90 and marks > 80):
    print('Grade B')
elif(marks < 80 and marks >60):
    print('Grade C')

age_candite = int(input("enter your age :"))

if(age_candite > 0 and age_candite < 18):
    print('You are not eligiable for vote')
elif(age_candite > 18 and age_candite <45):
    print('You are eligiable for vot')
 
elif(age_candite > 45 and age_candite <60):
     print('You are eligiable for vot')
     print('you must exerices your rights properly')

elif(age_candite > 60 and age_candite < 99):
     print('You are eligiable for vot')
     print('You can ask for assistence of vote')

else:
    print('Enter you age properly')


# WHILE LOOP
################################################
# un-countable

#while expression
    # <statement>

i = 1 #initalizing the variable
while i <11: #expression
    print(i) #code to be executed
    i = i + 1 # some point where the expression to be