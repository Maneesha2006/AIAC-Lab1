def is_valid_email(email):
    # Check for @ and . characters
    if '@' not in email or '.' not in email:
        return False

    # Should not allow multiple @
    if email.count('@') != 1:
        return False

    # Must not start or end with special characters
    special_chars = '@._-'
    if email[0] in special_chars or email[-1] in special_chars:
        return False

    return True

def main():
    email = input("Enter an email address: ")
    if is_valid_email(email):
        print("Valid email:", email)
    else:
        print("Invalid email. Please follow the requirements.")

if __name__ == "__main__":
    main()