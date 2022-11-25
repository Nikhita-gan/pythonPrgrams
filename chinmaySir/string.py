#method of list
#copy:when you copy the one list into another list their is create the another memory location 
#so if we change any index value this cannot reflact by other list


list1 = [11,22,44]
list2 =list1.copy()

print(list1)
print(list2)

list1[1]=12

print(list1)
print(list2)


###################################################################

##String

#defining the string

first_Name = 'Nikhita'
first_Name2 = "Nikhita"

print(first_Name)
print(first_Name2)

multiline ='''
I am learning python alongwith cypress,
I am laerning JavaScript also
I am very glad'''

print(multiline)

# string strores the value by index

city = "nagpur"
#0  1   2   3   4   5
# n a   g   p   u   r

print(city[1])
print(city[3])

#basic loop

for i in city:
    print(i)

for x in (list1):
    print(x)


# loop by range

for char in range(len(city)):
    #print(char)
    print(city[char])

for x in range(5):
    print(x)
print('..........................................................')
city1 = "Ahmadnagar"
#   0   1   2   3   4   5   6   7   8   9
#   A   h   m   a   d   n   a   g   a   r
#  -10  -9  -8  -7  -6  -5  -4  -3  -2  -1 

print(len(city1))

for char in city1:
    print(char)

##slice 
print(city1[1:10:2])

##print reverse the string we use slice with step -1

print(city1[::-1])

print(city1[0:10:2])

print(city1[1:10:1])



x = "hello world"

x = x+10
print (x)