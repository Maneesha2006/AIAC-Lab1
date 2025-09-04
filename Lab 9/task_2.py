class Srustudent:
    def __init__(self, name, roll_no, hostel_status):
        """
        Initializes a new Srustudent object.

        Args:
            name (str): The name of the student.
            roll_no (str): The roll number of the student.
            hostel_status (str): Hostel status ('Yes' or 'No').
        """
        self.name = name  # Store student's name
        self.roll_no = roll_no  # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel status
        self.fee_paid = False  # Initialize fee status as unpaid

    def fee_update(self, status):
        """
        Updates the fee payment status of the student.

        Args:
            status (bool): True if fee is paid, False otherwise.
        """
        self.fee_paid = status  # Update fee status

    def display_details(self):
        """
        Displays the details of the student.
        """
        print(f"Name: {self.name}")  # Print student's name
        print(f"Roll No: {self.roll_no}")  # Print roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Print fee status

if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    hostel_status = input("Enter hostel status (Yes/No): ")
    student = Srustudent(name, roll_no, hostel_status)
    fee_status_input = input("Has the fee been paid? (Yes/No): ")
    student.fee_update(fee_status_input.strip().lower() == 'yes')
    print("\nStudent Details:")
    student.display_details()