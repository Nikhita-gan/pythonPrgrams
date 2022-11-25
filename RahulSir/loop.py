# while loop


#while expression
    # <statement>
    # condition , where it will come out of the loop


# i = 1
# while i < 11:
#     # print(i)
#     i = i + 1 #increment
#     print(i)



# infinite time asking user 

a = int(input("Enter -1 to quit thee game"))
while a != -1:
    a = int(input("Enter -1 to quit thee game"))
print("Good bye!!!")


# guessing game 

guess_num = int(input("Guess a number less than 10!!! "))
ans  = 5
while guess_num != ans:
    guess_num = int(input("Guess a number less than 10!!! "))

print("You have guessd it correct")



print("Using for loop")

for i in range(0,11):
    print(i)


print("Using while loop")

i = 0
while i < 11:
    print(i)
    i = i + 1



# pass
for i in range(0,11):
    pass

# break
print("Using  break in while loop")

i = 0
while i < 11:
    print(i)
    if i == 5:
        break
    i = i + 1


i = 0
while i < 11:
    pass
#by using pass we hold that statement 
#this canot give error we left that statement and add after you required