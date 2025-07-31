def find_max_number(numbers):
    max_num = max(numbers)
    print("The maximum number is:", max_num)
    return max_num

# Example usage:
nums = []
for i in range(3):
    num = float(input(f"Enter number {i+1}: "))
    nums.append(num)

find_max_number(nums)