def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    """
    Prompts the user to select a mathematical operation (add, subtract, multiply, divide)
    and enter two numbers. Performs the selected operation using the provided numbers
    and displays the result. Handles invalid input for numbers and operations.
    Returns:
        None
    """
    print("Select operation: add, subtract, multiply, divide")
    operation = input("Enter operation: ").strip().lower()
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    if operation == "add":
        result = add(num1, num2)
    elif operation == "subtract":
        result = subtract(num1, num2)
    elif operation == "multiply":
        result = multiply(num1, num2)
    elif operation == "divide":
        result = divide(num1, num2)
    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()