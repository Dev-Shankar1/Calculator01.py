# This program functions as a command-line calculator with standard arithmetic
# and additional operations like squares, cubes, and roots.

import math

def get_number(prompt):
    """
    Prompts the user for a number and handles invalid input.
    Returns the number as a float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_calculation():
    """
    The main function to handle the calculator's logic.
    """
    print("Welcome to the Advanced Calculator!")
    print("Available operations:")
    print("  +   (Addition)")
    print("  -   (Subtraction)")
    print("  * (Multiplication)")
    print("  /   (Division)")
    print("  sq  (Square)")
    print("  cb  (Cube)")
    print("  sqrt (Square Root)")
    print("  cbrt (Cube Root)")
    print("  'exit' to quit")

    while True:
        choice = input("Enter an operation (e.g., +, sq, exit): ").strip().lower()

        # Handle 'exit' command to quit the program
        if choice == 'exit':
            print("Goodbye!")
            break

        # Operations requiring two numbers
        if choice in ['+', '-', '*', '/']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '+':
                result = num1 + num2
            elif choice == '-':
                result = num1 - num2
            elif choice == '*':
                result = num1 * num2
            elif choice == '/':
                # Handle division by zero
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            
            print(f"The result is: {result}")

        # Operations requiring one number
        elif choice in ['sq', 'cb', 'sqrt', 'cbrt']:
            num = get_number("Enter a number: ")

            if choice == 'sq':
                result = num ** 2
            elif choice == 'cb':
                result = num ** 3
            elif choice == 'sqrt':
                # Handle negative numbers for square root
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                    continue
                result = math.sqrt(num)
            elif choice == 'cbrt':
                # Cube root handles negative numbers, so no special check is needed.
                result = num ** (1/3)
            
            print(f"The result is: {result}")

        else:
            print("Invalid operation. Please choose from the list above.")

# Run the main calculation function
if __name__ == "__main__":
    perform_calculation()

