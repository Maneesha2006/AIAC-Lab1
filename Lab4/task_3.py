def swap_first_last_name():
    full_name = input("Enter the full name: ").strip()
    names = full_name.split()
    if len(names) < 2:
        print("Please enter at least first and last name.")
        return
    swapped_name = ' '.join([names[-1]] + names[:-1])
    print("Output:", swapped_name)

# Example usage
swap_first_last_name()