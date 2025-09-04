def sum_even_odd(numbers):
    """
    This module provides a function to calculate the sum of even and odd numbers in a list.
    Functions:
        sum_even_odd(numbers):
            Calculates the sum of even and odd numbers from the provided list.
    Usage:
        When run as a script, prompts the user to enter numbers separated by spaces,
        computes the sum of even and odd numbers, and prints the results.
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    numbers = list(map(int, user_input.strip().split()))
    even_sum, odd_sum = sum_even_odd(numbers)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Sum of odd numbers: {odd_sum}")
    