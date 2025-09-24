nums = input("Enter numbers separated by spaces: ")
nums = [int(i) for i in nums.strip().split()]
squares = [i * i for i in nums]
print(squares)
