# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance  # Encapsulated balance attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited: ${amount:.2f}")
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

