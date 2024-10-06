class BankAccount:
    def __init__(self, initial_balance=0.0):
        """
        Initializes a new BankAccount instance with an optional initial balance.
        If no initial balance is provided, it defaults to 0.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deducts the specified amount from the account balance if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance

    # Ensure there is at least one command provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command and possible parameters from the first argument
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle the commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
