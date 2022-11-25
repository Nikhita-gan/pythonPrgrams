# Regular Expression

#Regular expression use to pattern match
#to replace the pattern
# to split the pattern
#to search the particular string
#findAll for particular (regular expression)
import re

#Mthods of Regular Expression
#search() 
#findAll()
#match()
#sub()
#split()

#search()--give the object
str = 'mop sun top man '
s1 = re.search(r'm\w\w',str)
print(s1)

print(s1.group())

str2 = 'cut the cotton with cutter'
s2 = re.search(r'cu\w',str2)
if s2:

    print('Match found')
    print(s2.group())
else:
    print('match not found')

#findAll()----find all the match and give the output in list

s3 = re.findall(r'c\w\w\w',str2)
print(s3)

for item in s3:
    print(item)


#match

s4 = re.match(r'cu\w',str2)
print(s4)
print(s4.group())


#sub()---this method use replace the string

str3 = " This is very good morning"

s5 = re.sub(r'morning','evening',str3)
print(s5)



#split()----split the string by special character  


str4 = "I am learning new things"
s6 = re.split(r'\W',str4)
print(s6)