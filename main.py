# Addition
from ast import Eq


def add(x, y):
    return x + y

# Substration
def subtract(x, y):
    return x - y

# Multiplication    
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

# Main program
def calculator():
    print("Simple Calculator")

    while True:
        # Display menu
        print("\nMenu:")
        print("+: Addition")
        print("-: Subtraction")
        print("*: Multiplication")
        print("/: Division")
        print("E: Exit")

        # User choice
        choice = input("Enter your choice (+, -, *, /, E)")

        # Exit 
        if choice == 'E':
            print("Thank you!")
            break

        # Check if the choice is a valid operation
        if choice in ['+', '-', '*', '/']:
            try:
                # Get user inputs
                x = float(input("Enter the first number: "))
                y = float(input("Enter the second number: "))

                # Perform the selected operation
                if choice == '+':
                    result = add(x, y)
                elif choice == '-':
                    result = subtract(x, y)
                elif choice == '*':
                    result = multiply(x, y)
                elif choice == '/':
                    # Check for division by zero before performing the operation
                        if y != 0:
                            result = divide(x, y)
                        else:
                            raise ZeroDivisionError("Error: Cannot divide by zero.")
                else:
                   result = "Invalid input."

                print("Result:", result)

            except ValueError:
                print("Error: Invalid input.")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")


# Run the calculator program
calculator()
