


"""This is just the tempelate for documentation of the module"""


a = 10
b  = 20
c = 30

"""This is the sum function which takes three arguments and returns the sum of the three arguments"""
def sum(a, b, c):
    return a + b + c

"""This is the product function which takes three arguments and returns the product of the three arguments"""
def product(a, b, c):
    return a * b * c


"""This is the main function which calls the sum and product function and prints the sum and product of the three arguments"""
def main(): 
    print("This is the main function")
    sum = sum(a, b, c)
    product = product(a, b, c)
    print(sum)
    print(product)



if __name__ == "__main__":
    main()



#you need to start the python shell 
#import the module 
#then use the help()  function to get the documentation of the module

