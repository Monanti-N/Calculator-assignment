def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    operation = input("Enter operation (+, -, *, /): ")
    print(f"Operation entered: {operation}")
    num1 = float(input("Enter first number: "))
    print(f"First number entered: {num1}")
    num2 = float(input("Enter second number: "))
    print(f"Second number entered: {num2}")

    if operation == '+':
        print(f"The result is: {add(num1, num2)}")
    elif operation == '-':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == '*':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == '/':
        print(f"The result is: {divide(num1, num2)}")
    else:
        print("Invalid operation!")
        
calculator()  



