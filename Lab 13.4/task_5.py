items_input = input("Enter numbers separated by spaces: ")
items = [int(n) for n in items_input.split()]
search_item = int(input("Enter the number to search for: "))

print("Found" if search_item in items else "Not Found")
