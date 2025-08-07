def factorial_builtin(n):
    import math
    return math.factorial(n)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"Factorial of {num} is {factorial_builtin(num)}")
