# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulated balance attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        print(f"Deposit method called with amount: {amount}")  # Debug statement
        if amount > 0:
            self._account_balance += amount
            # Ensure only one print statement
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()