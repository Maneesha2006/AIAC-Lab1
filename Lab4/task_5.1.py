def count_lines_in_lab4():
    try:
        with open("lab4.txt", "r") as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Number of lines: {num_lines}")
            return num_lines
    except FileNotFoundError:
        print("The file lab4.txt does not exist.")
        return 0

count_lines_in_lab4()
