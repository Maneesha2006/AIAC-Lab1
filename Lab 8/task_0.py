def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid input")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number input")
        return

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
calculator()
while True:
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if again in ('yes', 'y'):
        calculator()
    elif again in ('no', 'n'):
        print("Goodbye!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
