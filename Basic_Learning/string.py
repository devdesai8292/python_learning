greet = "Hello"
name = "Dev"

#String Concatenation 
#indentation and space is important in this

print(greet + ", " + name + "!")
print("why are greeting me with" + greet + name)


#format method by placing the {} in the string and calling the format method on the string
#This can be used when you want to take the string as an input from the user and use it in your code as a string
#I can think of this as  
greet_format = "Hello, {}!"
print(greet_format.format(name))


#len() function to get the length of the string
#How is it useful in scripting? 
#I don't see much use in it. 



#Note - You can use """ to write a multi-line string

#Is it important to convert string into lower case of upper case? 
#why? 
#I don't see any use of it.


print(greet_format.format(name).lower())
print(greet_format.format(name).upper())



