


def main(): 
    print("This is the main function")


def function_exp():
    print("This is the function example")
    return 0

print(__name__)
print(__file__)
print(__doc__)

if __name__ == "__main__":
    main()


#__name__ is a special variable in python which is used to check whether the code is run as a script or as a module.



#The __name__ variable is set to "__main__" when the python script is run as a script.

#The __name__ variable is set to the name of the module when the python script is imported as a module.