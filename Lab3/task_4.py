def register_user(users_db):
    print("\n--- User Registration ---")
    username = input("Enter a username: ").strip()
    if username in users_db:
        print("Username already exists. Please try logging in.")
        return False
    password = input("Enter a password: ").strip()
    users_db[username] = password
    print("Registration successful! You can now log in.")
    return True

def login_user(users_db):
    print("\n--- User Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if users_db.get(username) == password:
        print(f"Login successful! Welcome, {username}.")
        user_page(username)
        return True
    else:
        print("Invalid username or password.")
        return False

def user_page(username):
    print(f"\n--- {username}'s Page ---")
    print("You are now logged in. (This is your user page.)")

def main():
    users_db = {}
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ").strip()
        if choice == '1':
            register_user(users_db)
        elif choice == '2':
            login_user(users_db)
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
