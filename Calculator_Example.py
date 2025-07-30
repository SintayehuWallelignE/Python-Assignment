# Simple Calculator Program

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose a mathematical operation
print("Choose an operation: + (addition), - (subtraction), * (multiplication), / (division)")
operation = input("Enter the operation symbol: ")

# Perform the selected operation
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation entered.")