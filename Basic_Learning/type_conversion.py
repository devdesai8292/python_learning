#type conversion can be of two types
#1. Implicit type conversion
#2. Explicit type conversion
#Implicit type conversion is done automatically by the python interpreter
#Explicit type conversion is done by the user
#Explicit type conversion is also known as type casting

x = 5
#y will become int based on the implicit type conversion 
y = x * 2

print(type(y))

y = y * 2.5 #y will become float based on the implicit type conversion

print(type(y))
# it will print the class 'float'


#flowing point error. 


x = 0.1 
y = 0.2

z = x + y
print(z)



