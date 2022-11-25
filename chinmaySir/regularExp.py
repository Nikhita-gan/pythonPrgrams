import re

#-----------------------------------------------------
#\w  ===>  [a-z] [A-Z][0-9]
#\b     ===> " " give the space 
#\W     ===> not [a-z][A-Z][0-9]
#\d     ===> [0,9]
#[\w]*=====> more than one repeation

str = 'an apple a day keeps the doctor away'
s= re.findall(r'\ba[\w]*\b',str)
print(s)

#o/p ===>['an', 'apple', 'a', 'away']
s1 = re.findall(r'a[\w]*',str)
print(s1)

#o/p ===>['an', 'apple', 'a', 'ay', 'away']

str1 = 'The public holiday on 15th augest and 26th Janwary'

#it give the only digit
s2 = re.findall(r'\d[w]*\d',str1)
print(s2)

str3 = "This is my 10th class marks 78 45 75 73"

s3 = re.findall(r'\d[w]*\d',str3)
print(s3)

s4 = re.findall(r'\b\w{4}\b',str3)
print(s4)

s5 = re.findall(r'\b\w{4,}\b',str3)
print(s5)

s5 = re.findall(r'\b\w{2,4}\b',str3)
print(s5)


str4 = "I got 86% in 10th class"

# s6 = re.findall(r'\b\W{2,4}\b',str4)
# print(s6)

s6 = re.search(r'\b\w{3,}\b',str4)
print(s6.group())


