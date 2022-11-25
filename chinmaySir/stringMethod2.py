# startswith()---->check that give string is start with desired string or not
city = "Nagpur"
c1 = city.startswith("Nag")
print(c1)

#endswith()--->check that give string is end with desired string or not
city1 = "Nagpur"
c2 = city.endswith("pur")
print(c2)

#index()
city2 = "chandrapur"
c3 = city2.index("d")
print(c3)

#count()
c4 =city2.count("a")
print(c4)

c5 =city2.count("n")
print(c5)

#replace()---> replace the element in the string
str1 = "Good Mornning! I am using Javascript"
s1 = str1.replace("Mornning","afternoon")
print(s1)


# strip()-->remove the space
str2 = "  Nikhita  "
s2 = str2.strip()
print(s2)

# split()--->divide the string and convert it into list
str3 = "Nikhita.Swapnil.Ganvir"
s3 = str3.split(".")
print(s3)

str4 = "nikhitaganvir22@gmail.com"
s4 = str4.split("a")
print(s4)
#['nikhit', 'g', 'nvir22@gm', 'il.com']
#['Nikhita', 'Swapnil', 'Ganvir']

#isalpha()
a1 = "nikhita"
a11 = a1.isalpha()
print(a11)

a2 = "nikhita1245"
a12 = a2.isalpha()
print(a12)


#isdigit
b1 = "12457"
b11 = b1.isdigit()
print(b11)


b2 = "12457NIK"
b12 = b2.isdigit()
print(b12)


#isalnum
c1 = "nikhita1245"
c11 = c1.isalnum()
print(c11)


#isspace
d1 = " Nik khita"
d11 = d1.isspace()
print(d11)


# returns true if first  character of every method is capital
#istitle()-
str = "my title is Docu ment"
f11= str.istitle()
print(f11)


prq = "Mylitter"
p1 = prq.istitle()
print(p1)
#My Title Is Docu Ment
