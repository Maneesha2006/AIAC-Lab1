def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"Number of lines in '{filename}': {num_lines}")
            return num_lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return 0

# Example usage
count_lines_in_file('lab4.txt')