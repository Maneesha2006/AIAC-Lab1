def count_vowels_in_string():
    s = input("Enter a string: ")
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print(f"Number of vowels: {count}")

count_vowels_in_string()
