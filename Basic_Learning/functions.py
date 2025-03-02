

#in any language it is important to divide your code into multiple functions


def function_exp():
    print("This is the function example")
    return 0



#when you are talking about function, you also need to mention the variable scope. 

#variable scope is the most important concept in the python
#variable scope is the range of the variable in which it is accessible


#local scope 

def local_scope():
    x = 10
    print(x)


#global scope
x = 10
def global_scope():
    print(x)


#nonlocal scope
def nonlocal_scope():
    x = 10
    def inner():
        nonlocal x
        x = 20
        print(x)
    inner()
    print(x)