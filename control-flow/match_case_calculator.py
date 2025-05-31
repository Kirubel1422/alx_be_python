num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
result = None

match operation:
    case "+":
        result = num1 + num2
    
    case "-":
        result = num1 - num2
    
    case "*":
        result = num1 * num2
    
    case "/":
        if(num2 == 0):
            print("Cannot divide by zero.")
            exit(0)
        else:
            result = num1 / num2

print(f"The result is {result}")