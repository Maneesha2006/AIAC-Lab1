def classify_age_group(age):
    
    if age >= 0:
        if age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 35:
            return "Young Adult"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior Citizen"
    else:
        return "Invalid age"

try:
    user_age = int(input("Enter your age: "))
    group = classify_age_group(user_age)
    print(f"Age Group: {group}")
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")

