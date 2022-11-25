import re

str= "chinmay got 56 marks and rahul got 90 marks"
e11 = re.findall(r'\d[\w]*\d',str)
print(e11)


str1 = "The meeting will start at 9am and will end at 8pm . please join at 8am"
e22 = re.findall(r'\d[\w]*',str1)
print(e22)
