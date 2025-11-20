def is_even_modulo(n):
    return n % 2 == 0

def is_even_bitwise(n):
    return (n & 1) == 0

def is_even_repeated_sub(n):
    n = abs(n)
    while n >= 2:
        n -= 2
    
    return n == 0
test_numbers = [0, 1, 2, 7, 10, 13, 100, -4, -9]

print("Testing is_even_modulo:")
for num in test_numbers:
    print(f"{num} is even? {is_even_modulo(num)}")

print("\nTesting is_even_bitwise:")
for num in test_numbers:
    print(f"{num} is even? {is_even_bitwise(num)}")

print("\nTesting is_even_repeated_sub:")
for num in test_numbers:
    print(f"{num} is even? {is_even_repeated_sub(num)}")


