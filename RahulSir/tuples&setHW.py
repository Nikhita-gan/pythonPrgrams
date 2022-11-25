#############HW

##1 . UNPACK THE TUPLE AND PRINT 0 AFTER UNPACKING IT

z = ([22,33], [True,False],[0,1],[111,999])

a,b,c,d = z

print(z[1])
print(a[1])
print('------unpacked-------')
# ##2. UNPACK THE TUPLE AND PRINT 0 AFTER UNPACKING IT 
t_num = (1,2,3,4,5,6,7,8,9)
_,_,c,_,_,_,_,_,_ = t_num 
print(_)
print(c)

# 3. 
# convert the list into sets:
name1 = ['R', 'A', 'H', 'U', 'L']
setName1 = set(name1)
print(setName1)
print('------------------------------------------------------')
name2 = ['A', 'K', 'S', 'H', 'A', 'Y']
setName2 = set(name2)
print(setName2)
print('------------------------------------------------------')
bool3 = [True, False, False, False, True]
setbool3 = set(bool3)
print(setbool3)
print('------------------------------------------------------')
# 4. find length of the set
#     use for loop to print the items of  the set
d = set([True, False, False, False, True])
print(d)
print(len(d))

for item in d:
    print(item)



t_num = (1,2,3,4,5,6,7,8,9)                                                                                                                                                                                                                                                                                                                                                                                             
_,_,c,_,_,_,_,_,_ = t_num 
print(_)
print(c)