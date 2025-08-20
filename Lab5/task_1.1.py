def collect_user_data():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # At this point, we're handling raw user input.
    # Best practice: Do not store personally identifiable information (PII) in plain text.

    # Example: Hash the email address to anonymize it
    import hashlib
    hashed_email = hashlib.sha256(email.encode()).hexdigest()

    # You can also consider encrypting the entire dataset using a library like cryptography
    # This helps prevent unauthorized access if the data is stored

    # Store only what is necessary, and anonymize whenever possible
    user_data = {
        "name": name,             # Consider pseudonymization or not storing this directly
        "age": age,               # Non-sensitive, but still could be identifying
        "hashed_email": hashed_email  # Safer alternative to storing the raw email
    }

    # Print the protected version of the data
    print("Protected user data collected:")
    print(user_data)

# Run the function
collect_user_data()
