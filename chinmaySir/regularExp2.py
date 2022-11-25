import re

#Program1
str = "an apple a day keep doctor away swapnil"
s = re.findall(r'a[\w]*',str)
print(s)

#Program2
str = "an apple a day keep doctor away"
s1 = re.findall(r'\ba[\w]*\b',str)
print(s1)

#program3

str1 = "The meeting will be conducted on 21st and 2nd of every month"
s2 = re.findall(r'\d[\w]*',str1)
print(s2)

#Program 4
str2 = "One two three four five six seven 8 9 10"
s3 = re.search(r'\b\w{5}',str2) #It give only first come
print(s3.group())

#Program 5
s4 = re.findall(r'\b\w{5}',str2) #It give only first come
print(s4)

#Program 6
s5 = re.findall(r'\b\w{3,5}',str2) #It give all which have 3 to 5 character
print(s5)


#Program 7
s6 = re.findall(r'\b\w{1,}',str2) #It give all which have 3 to 5 character
print(s6)

#Program 8
s7 = re.findall(r'\b\d{1,}',str2) #It give all which have 3 to 5 character
print(s7)

#Program 9
str3 = "nikhita8657326302"
#\d+ ====>only number with repetation
#\D+ =====>Not a number with repetating charaters
e1 = re.search(r'\D+',str3)
print(e1.group())


e2 = re.search(r'\d+',str3)
print(e2.group())



#Program 10

str11 = 'anil ankit amit aniket avinash avni ankur vijay manish'
e22 = re.findall(r'\ban[\w]*\b',str11)
print(e22)

e22 = re.findall(r'\ba[\w]*\b',str11)
print(e22)

e23 = re.findall(r'\ba[nv][\w]*\b',str11)
print(e23)


#Program 11

strE = 'nikhita 22-8-1989 swapnil 18-2-1980 Atharv 22-11-2015'
e24 = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',strE)
print(e24)

#program 12

strD = "Good Morning"
e33 = re.search(r'^Go',strD)
print(e33.group())
if e33:
    print('Sentence starts with He')
else:
    print('Sentence does not starts with He')


e34 = re.search(r'ng$',strD)
print(e34.group())
if e34:
    print('Sentence end with ng')
else:
    print('Sentence does not end with ng')




