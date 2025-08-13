def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    print(f"Number of vowels in '{s}': {count}")

# Example usage:
user_input = input("Enter a string: ")
count_vowels(user_input)