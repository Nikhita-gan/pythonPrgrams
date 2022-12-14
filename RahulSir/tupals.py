
##TUPLES  IN PYTHON



# Default
# keyword
# Positional

# # string formatting 


zero = 0
one  = 1 
two = 2 


print( "The numbers are " , zero ,one , two)

# format()

print( "The numbers are   {} {}  {}".format(zero,one,two))
print( "The numbers are   {0} {1}  {2}".format(zero,one,two))
print( "The numbers are   {2} {1}  {0}".format(zero,one,two))


#f-string latest method
print( f" using f string The numbers are {zero} {one}  {two} ")




# ############################TUPLES  IN PYTHON


list1 = []
print(type(list1)) # <class 'list'>

t = ()
print(type(t)) #<class 'tuple'>

list1 = [11,22,33,44, True, "Now" ,"Pune" ,[2,4,6,8,[2,4,6,8]]]
print(type(list1)) #<class 'list'>

t = (11,22,33,44, True, "Now" ,"Pune" ,[2,4,6,8,[2,4,6,8]])
print(type(t)) #<class 'tuple'>

# accessing the items inside a tuple

print(list1[1])
print(list1[4])

print("accessing the items inside a tuple")
print(t[4])

#slicing in a tuple is same as list
    #    0 1 2 3 4 5
t_odd = (1,3,5,7,9,11,13)
print(t_odd[0:4])

# step /jump
# start:end:step
print(t_odd[0:8:2])
print(t_odd[0:8:3])


# reversal
print(t_odd[::-1])



# changing the values
list_even = [2,4,6,8,10,12]

list_even[0] = 20
print(list_even)

t_odd = (1,3,5,7,9,11,13)
# t_odd[0] = 10 #'tuple' object does not support item assignment
# print(t_odd)

# tuples are immutable data-types

coord_hotel = (12.33,33.33)
password13 = ("pass1","pass2")



t_odd = (1,3,5,7,9,11,13)
t_even = (2,4,6,8,10,10,12)
t = t_odd + t_even #concat , new tuple is formed
print(t)

# id() function to get the memory location of the data

print(id(t_odd))
print(id(t_even))
print(id(t))

# some functions on tuples
print(max(t_odd))
print(max(t_even))

print(min(t_odd))
print(min(t_even))


#methods 
# only 2 methods are available
# since we dont want to edit anyhting in tuple

t_even = (2,4,6,8,10,10,12)

print(t_even.count(10)) # count no of occurences
print(t_even.index(10)) # get you the 1st occurence