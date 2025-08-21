def sum_to_n(n):
    """
    Calculates the sum of the first n natural numbers using a for loop.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total



def sum_to_n_while(n):
    """
    Calculates the sum of the first n natural numbers using a while loop.
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_to_n_formula(n):
    """
    Calculates the sum of the first n natural numbers using the formula.
    """
    return n * (n + 1) // 2

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer n to calculate the sum of first n numbers: "))
        if n < 1:
            print("Please enter a positive integer greater than 0.")
        else:
            print(f"Sum of first {n} numbers using for loop: {sum_to_n(n)}")
            print(f"Sum of first {n} numbers using while loop: {sum_to_n_while(n)}")
            print(f"Sum of first {n} numbers using formula: {sum_to_n_formula(n)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
