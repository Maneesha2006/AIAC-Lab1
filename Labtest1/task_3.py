def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes_in_range(n1, n2):
    primes = []
    for num in range(n1, n2 + 1):
        if num == 1 or is_prime(num):
            primes.append(num)
    return primes

# Example usage:
n1 = int(input("Enter start of range: "))
n2 = int(input("Enter end of range: "))
result = primes_in_range(n1, n2)
print("Prime numbers in range:", ",".join(str(x) for x in result))