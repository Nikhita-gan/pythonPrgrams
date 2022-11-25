# for and while 

x = 1
while x <= 10:
    print(x)
    x = x + 1


# x = 1 
# while(x <= 5):
#     print(x) # 1 # 2 # 3 #4 #5
#     x = x + 1  # 2 # 3 # 4 #5 #6

# y = 5
# while(y >= 1):
#     print(y) # 5 # 4 #3 #2 #1
#     y = y - 1  # 4 # 3 #2 #1 #0

#break:----Break keyword break the statement when condition is true and stop the excution 
q = 1
while(q <=5):
    print(q) # 1 #2
    if(q == 2):
        break
    q = q + 1 #2

e = 10
while(e >= 1):
    if(e == 6):
        break
    print(e) # 10 # 9 #8 # 7
    e = e - 1  # 9 # 8 #7 #6

e = 10
while(e >= 1):
    print(e) # 10 , 9 ,8 ,7 6
    if(e == 6):
        break
    e = e - 1  
#continue-------continue keyword make loop in continue when condition is true and goes to infinate loop
#so advoid this condition we have increment the condition then use continue satement


j = 1
while(j <=5):
    if(j == 3):
        j = j + 1 
        continue
    print(j)  #1 2  4 5
    j = j + 1 #2  3


a = 5
while(a >= 1):
    if(a == 2):
        a = a-1 # 1
        continue
    print(a) # 5 # 4 #3 #1
    a = a-1 # 4 #3 #2 # 0


# for loop
#             0         1       2         3
listName = ["Nikhit","Amit","Swapnil","Athrv"] 
for item in listName:
    print(item)

for x in range(len(listName)):
    #print(x)
    print(listName[x])

# continue and break
