try:
    a, b = map(float, input("Please enter two numbers separated by space: ").split())
    print(a / b)
except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
except ValueError:
            print("Error: Invalid input again.")

