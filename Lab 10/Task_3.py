name = input("Employee name: ")
salary = float(input("Salary: "))
percent = float(input("Increment %: "))
salary += salary * percent / 100
print(f"emp: {name} salary: {salary}")