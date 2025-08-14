def generate_student_ids():
    student_names = []
    n = int(input("Enter the number of students: "))
    for _ in range(n):
        name = input("Enter student full name (First Last): ").strip()
        student_names.append(name)

    print("\nGenerated Institutional IDs:")
    for name in student_names:
        parts = name.split()
        if len(parts) >= 2:
            firstname = parts[0].lower()
            lastname = parts[-1].lower()
            email = f"{firstname}{lastname}@sru.edu.in"
            print(f"{name}: {email}")
        else:
            print(f"{name}: Invalid name format")

# Example usage
if __name__ == "__main__":
    generate_student_ids()