
def global_var():
    #x = 10  #local x variable
    #by putting global keyword, we are telling python that we are using the global x variable and not the local

    
    global x
    x = 20
    print(x)


#global x variable
x = 5

global_var()
print(x)