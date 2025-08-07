def sort_numbers():
    try:
        nums = input("Enter numbers separated by spaces: ")
        num_list = [int(x) for x in nums.strip().split()]
    except ValueError:
        print("Invalid input. Please enter only integer numbers.")
        return

    order = input("Sort in ascending or descending order? (a/d): ").strip().lower()
    if order == 'a':
        sorted_list = sorted(num_list)
        print("Sorted numbers in ascending order:", *sorted_list)
    elif order == 'd':
        sorted_list = sorted(num_list, reverse=True)
        print("Sorted numbers in descending order:", *sorted_list)
    else:
        print("Invalid choice. Please enter 'a' for ascending or 'd' for descending.")

if __name__ == "__main__":
    sort_numbers()
