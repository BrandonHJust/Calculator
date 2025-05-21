import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot find square root of a negative number"

def calculator():
    print("Welcome to the calculator app")
    user_name = input("Please enter your name: ")
    print(f"Hello, {user_name}!")

    operation_count = 0

    while True:
        print("\nSimple Calculator with Math Library Operations")
        print("Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")

        choice = input("Enter the operation number (1-6): ")

        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice in ['1', '2', '3', '4', '5']:
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))
            else:
                x = float(input("Enter the base number: "))

            operations = {
                '1': add,
                '2': subtract,
                '3': multiply,
                '4': divide,
                '5': power,
                '6': square_root
            }

            operation_function = operations.get(str(choice))

            if operation_function:
                result = operation_function(x, y)
                print("Result:", result)
                operation_count += 1
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

    print(f"\nThank you, {user_name}! You performed {operation_count} operations.")

calculator()






