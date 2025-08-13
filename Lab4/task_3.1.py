def swap_first_last_name():
    full_name = input("Enter the full name: ").strip()
    parts = full_name.split()
    if len(parts) < 2:
        print("Please enter at least first name and last name.")
        return
    swapped = parts[-1] + " " + " ".join(parts[:-1])
    print(swapped)

swap_first_last_name()
