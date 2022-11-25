############## HW

# 1. FIND THE DATA TYPE AND LENGHT OF z
z = "Repetition is the mother of learning"
print(type(z))
print(len(z))
print("---------------------------------------------------------")

# 2 . REVERSE THE STRING USING NEGATIVE INDEXING/SLICING 

k  = "Was it a car or a cat I saw? "
p = "Do geese see God?"
print(k[::-1])
print(p[::-1])
print("-------------------------------")
# 3 . PRINT THE FOLLOWING USING range()

h = "HYDERABAD"
c = "CHENNAI"
d = "DELHI"
for x in range(len(h)):
    print(h[x])

print("-------------------------------------------------")
for y in range(len(c)):
    print(c[y])

print("-------------------------------------------------")
for z in range(len(d)):
    print(d[z])

print("-------------------------------------------------")

# 4.  find number of spaces in song2
#     find count of Ganga in song2
#     replace  Ganga with "GANGA" in song2

song2 = '''
Jana Gana Mana Adhinaayak Jaya Hey, 
Bhaarat Bhaagya Vidhaataa 
Panjaab Sindhu Gujarat Maraatha, 
Draavid Utkal Banga 
Vindhya Himaachal Yamuna Ganga, 
Vindhya Himaachal Yamuna Ganga, 
Uchchhal Jaladhi Taranga
Tav Shubh Naamey Jaagey, 
Tav Shubh Aashish Maange Gaahey 
Tav Jayagaathaa 
Jana Gana Mangal Daayak, Jaya Hey Bhaarat Bhaagya Vidhaataa 
Jaya Hey, 
Jaya Hey, 
Jaya Hey, 
Jaya Jaya jaya, 
Jaya Hey
'''
q1 = song2.count(" ")
print(q1)
print("------------------------------------------------")
q2 = song2.count("Ganga")
print(q2)
print("------------------------------------------------")
q2 = song2.replace("Ganga","GANGA")
print(q2)
# 5 . using format() method print below  

s = "sun"
m = "moon"
e = "earth"


" sun is farthest from earth and nearest is moon"
print("{} is farthest from {} and nearest is {}".format(s,m,e))
print("---------------------------------------------------------")
"moon is nearest and sun is farthest from earth"
print("{1} is nearest and {0} is farthest from {2}".format(s,m,e))
print("-----------------------------------------------------")
"sun is biggest of earth and moon"
print("{0} is biggest of {2} and {1}".format(s,m,e))
print("----------------------------------------------------")
"the order is sun , earth and moon"
print("the order is {0} , {2} and {1}".format(s,m,e))
