


n =5; 
count = 0; 
a = 1; 
b = 1; 

while count < n:
    if count <= 1:
        print("1")
    else: 
        print(a + b)
        a,b = b, a+b  # this is multiple assignment
    count += 1


