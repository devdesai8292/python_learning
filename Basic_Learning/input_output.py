

#input functions can have the prompt message as an argument
#The input() function always returns a string.
input_name = input("What is your name?")    #input() function is used to take the input from the user
print("Hello, " + input_name + "!") 

#The input() function always returns a string. 
#If you want to take an integer as an input, you need to convert it to an integer using the int() function
print("What is your age?")
input_age = int(input())
print("You will be " + str(input_age + 1) + " in a year") 
#The str() function is used to convert the integer to a string. 
#You cannot concatenate a string with an integer.
#You can only concatenate a string with a string.
#So, you need to convert the integer to a string using the str() function.


