# Example of ID
a = 10
b = 3.14
c = "Hello"
print("Id of a :" ,id(a))
print("Id of b :" ,id(b))
print("Id of c :" ,id(c))

#example os ID of same number
x = 12
y = 12
print("Id of x :" ,id(x))
print("Id of y :" ,id(y))
print("x and y are same object?" , id(x)==id(y))      #true as small number but may b differnt for large numbers