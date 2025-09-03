def assign_grade(score):
    # Check for invalid input types
    if not isinstance(score, (int, float)):
        return "Invalid input: Score must be a number."
    # Check for out-of-range scores
    if score < 0 or score > 100:
        return "Invalid input: Score must be between 0 and 100."
    # Assign grades based on score ranges
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    user_input = input("Enter the score: ")
    try:
        score = float(user_input)
    except ValueError:
        print("Invalid input: Score must be a number.")
    else:
        print("Grade:", assign_grade(score))