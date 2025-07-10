while True:
    num1 = input("Enter first number (or 'exit' to stop): ")
    
    if num1.lower() == "exit":
        print("Exiting...")
        break
    
    op = input("Enter operation (+, -, *, /): ")
    num2 = input("Enter second number: ")
    
    num1 = float(num1)
    num2 = float(num2)
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
            continue
        result = num1 / num2
    else:
        print("Error: Invalid operator! Use +, -, *, or /.")
        continue
    
    print(f"Result: {result}")
