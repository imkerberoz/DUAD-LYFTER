# WEEK 12 - 4 PILLARS OF OOP (OBJECT-ORIENTED PROGRAMMING)
# - ENCAPSULATION: Bundling data (balance) and methods (deposit, withdraw) together, 
#   and protecting the data by making it an instance attribute (self.balance).
# - ABSTRACTION: Hiding complex details; users interact with simple methods like deposit/withdraw 
#   without knowing internal checks.
# - INHERITANCE: SavingsAccount inherits from BankAccount, reusing its methods and attributes.
# - POLYMORPHISM: The withdraw method is overridden in SavingsAccount to add extra behavior, 
#   but it can be called the same way as in BankAccount.

class BankAccount:
    # This is the base class for a general bank account.
    # It represents a simple account with a balance and basic operations.
    
    def __init__(self, initial_balance=0):
        # Constructor method: Called when creating a new object (e.g., account = BankAccount(100)).
        # - 'self' refers to the current object being created.
        # - 'initial_balance' is an optional parameter; defaults to 0 if not provided.
        # - We set 'self.balance' as an instance attribute: Each account object has its OWN balance.
        #   This is crucial because attributes defined here are unique to each instance, not shared.
        self.balance = initial_balance

    def deposit(self, amount):  # THIS IS THE METHOD TO ADD MONEY TO THE ACCOUNT
        # - 'amount' IS THE POSITIVE VALUE TO ADD TO THE BALANCE.
        # - IT CHECKS IF THE AMOUNT IS POSITIVE TO AVOID INVALID DEPOSITS.
        # - IF VALID, IT UPDATES THE BALANCE AND PRINTS A CONFIRMATION MESSAGE.
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount): # METHOD TO REMOVE MONEY FROM THE ACCOUNT
        # - 'amount' is the value to withdraw.
        # - Checks if amount is positive and if there's enough balance (balance >= amount).
        # - If valid, subtracts from balance and prints a message.
        # - If not, prints an error (no overdraft allowed in this basic account).
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


class SavingsAccount(BankAccount):
    # THIS IS A DERIVED CLASS (SUBCLASS) OF BankAccount, IT INHERITS FROM THE PRIMARY CLASS.
    # It adds a minimum balance requirement, demonstrating inheritance and polymorphism.
    # * Inherits balance, deposit, and withdraw from BankAccount.
    # - Overrides (redefines) withdraw to enforce the min_balance rule.
    
    def __init__(self, min_balance, initial_balance=0): # A CONSTRUCTOR FOR SAVINGS ACCOUNT IS REQUIRED TO SET MIN BALANCE
        # - Calls the parent class constructor using super() to initialize the balance.
        #   This reuses the code from BankAccount's __init__.
        # - 'min_balance' is required and set as an instance attribute: Each savings account can have its own minimum.
        # - 'initial_balance' is optional, passed to the parent.
        super().__init__(initial_balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        # Overridden withdraw method: Same name as in parent, but with added logic.
        # - This is polymorphism: You can call withdraw on a SavingsAccount object, 
        #   and it uses this version instead of the parent's.
        # - Checks if amount is positive and if (balance - amount) would still be >= min_balance.
        # - If yes, subtracts and prints success.
        # - If no, prints an error without changing the balance.
        # - Note: We could call super().withdraw(amount) if checks pass, but here we duplicate the subtraction 
        #   for simplicity (to avoid extra calls in this basic example).
        if amount > 0 and (self.balance - amount) >= self.min_balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Cannot withdraw. Balance would fall below minimum of {self.min_balance}. Current balance: {self.balance}")


# Example usage: This is not part of the classes, but shows how to test them.
# It's good practice to include examples or tests to verify the code works.

print("--- Testing Regular BankAccount ---")
regular_account = BankAccount(500)  # Create with initial balance 500
regular_account.deposit(300)        # Deposit 300 → balance 800
regular_account.withdraw(600)       # Withdraw 600 → balance 200
regular_account.withdraw(1000)      # Fails: insufficient funds

print("\n--- Testing SavingsAccount ---")
savings = SavingsAccount(min_balance=100, initial_balance=800)  # Min 100, start with 800
savings.deposit(500)                # Deposit 500 → balance 1300
savings.withdraw(900)               # Withdraw 900 → balance 400 (still >= 100)
savings.withdraw(350)               # Fails: 400 - 350 = 50 < 100