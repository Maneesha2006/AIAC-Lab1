numbers_input = input("Enter numbers separated by spaces: ")
numbers = [int(n) for n in numbers_input.split()]
squares = [n ** 2 for n in numbers]

# Print the result
print(squares)
