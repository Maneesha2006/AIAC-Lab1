class BankAccount:
    def __init__(self, name, balance=0.0):
        
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f}. New balance: {self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount:.2f}. New balance: {self.balance:.2f}")
    def check_balance(self):
        
        print(f"Current balance: {self.balance:.2f}")
def main():
    name = input("Enter account holder's name: ")
    while True:
        try:
            initial_balance = float(input("Enter initial balance: "))
            if initial_balance < 0:
                print("Initial balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for balance.")
    account = BankAccount(name, initial_balance)
    while True:
        print("\n--- Bank Account Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '2':
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using the Bank Account system.")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")
if __name__ == "__main__":
    main()
