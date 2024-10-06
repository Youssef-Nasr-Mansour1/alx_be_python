# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
            # Only one print statement
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
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
        print("3. Current balance:")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            amount = input("Enter amount to deposit: ")
            try:
                amount = float(amount)
                if amount > 0:  # Validate positive amount
                    account.deposit(amount)
                else:
                    print("Amount must be greater than zero.")
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
