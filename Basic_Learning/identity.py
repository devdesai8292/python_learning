
#this is very important concept. 
#In python, everything is an object.
#Every object has an identity, a type, and a value.
#The identity of an object is unique and constant for the object during its lifetime.
#The type of an object defines the possible values and operations (methods) for objects of that type.
#The value of an object is the data stored in the object.
#In Python, the type of an object is determined by the object itself, not by the variable it is assigned to.
#The type of an object is determined at runtime by the object itself.
###In summary, each time you assign a new value to a variable, 
# Python creates a new object in memory and updates the variable reference to point to this new object. 
# The old object may be garbage collected if there are no other references to it.###





x = 10

print(id(x))
print(type(x))

x = "dev"

print(id(x))
print(type(x))



#y = x + 10 
y = x + " pooja"
print(y)



