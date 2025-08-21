def print_multiples_for_loop(n):
    print(f"First 10 multiples of {n} using for loop:")
    for i in range(1, 11):
        print(n * i, end=' ')
    print()  # for newline

def print_multiples_while_loop(n):
    print(f"First 10 multiples of {n} using while loop:")
    i = 1
    while i <= 10:
        print(n * i, end=' ')
        i += 1
    print()  # for newline

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to print its first 10 multiples: "))
        print_multiples_for_loop(num)
        print_multiples_while_loop(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
