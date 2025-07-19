def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    while True:

        num1_input = input("Enter first number (or 'exit' to stop): ")
        if num1_input.lower() == 'exit':
            print("Exiting calculator...")
            break
        
        op = input("Enter operation (+, -, *, /): ")
        
        num2_input = input("Enter second number: ")
        
    
        num1 = float(num1_input)
        num2 = float(num2_input)
            
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
                result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
        else:
            print("Error: Invalid operator! Use +, -, *, or /.")
            continue
            
        print(f"Result: {result}")
            
        
calculator()