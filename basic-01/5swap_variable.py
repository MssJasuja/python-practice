#Swapping of variable using third variable
a = 53
b = 7
temp = a                                #here temp is a third variable
a = b
b = temp
print (a,b)                              #Result after swapping a becomes b and b becomes a

#Swapping without third variable
x = 5
y = 9
x, y = y, x                                #Another way of swapping without using third variable
print(x,y)                                 #Result after swapping a becomes b and b becomes a
