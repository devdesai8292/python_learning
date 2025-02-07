


def calculator(x,y,op): 
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y
    else:
        return "Invalid operator"
    

op = input("Enter the operator: ")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


result = calculator(a,b,op)

print(f"The result of the operation is: {result}")




