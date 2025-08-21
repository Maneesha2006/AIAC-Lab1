class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'

def main():
    students = []
    n = int(input("Enter the number of students: "))
    for i in range(n):
        print(f"\nEnter details for student {i+1}:")
        name = input("Enter name: ")
        roll_no = input("Enter roll number: ")
        while True:
            try:
                marks = float(input("Enter marks: "))
                break
            except ValueError:
                print("Invalid input for marks. Please enter a number.")
        student = Student(name, roll_no, marks)
        students.append(student)

    print("\nStudent Details:")
    for student in students:
        print("-" * 20)
        student.display_details()

if __name__ == "__main__":
    main()
