# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulated balance attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds exist."""
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current balance: ${self._account_balance:.2f}")

# main-0.py

# main-0.py

import sys
from bank_account import BankAccount

def main():
    # Create a bank account with an initial balance (if provided)
    initial_balance = float(sys.argv[1]) if len(sys.argv) > 1 else 0
    account = BankAccount(initial_balance)

    while True:
        # Command-line interface for user input
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Current Balance:")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = input("Enter amount to deposit: ")
            try:
                amount = float(amount)
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number for the deposit amount.")
        elif choice == '2':
            amount = input("Enter amount to withdraw: ")
            try:
                amount = float(amount)
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number for the withdrawal amount.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
