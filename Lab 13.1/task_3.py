class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        print(f"Name: {self.name}\nAge: {self.age}")

    def total_marks(self):
        return sum(self.marks)

if __name__ == "__main__":
    
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    marks = []
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(1, num_subjects + 1):
        mark = int(input(f"Enter mark for subject {i}: "))
        marks.append(mark)

    student = Student(name, age, marks)
    print("\nStudent Details:")
    student.details()
    print(f"Marks: {', '.join(str(m) for m in student.marks)}")
    print(f"Total Marks: {student.total_marks()}")
