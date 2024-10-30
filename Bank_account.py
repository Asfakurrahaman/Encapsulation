class BankAccount:
    def __init__(self, account_holder, initial_balance, pin):
        # Public attribute
        self.account_holder = account_holder

        # Private attributes (encapsulated)
        self.__balance = initial_balance
        self.__pin = pin

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New Balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Invalid PIN. Access denied.")
            return
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New Balance: ${self.__balance}")

    # Public method to check balance (requires PIN)
    def get_balance(self, pin):
        if pin == self.__pin:
            print(f"Account Balance: ${self.__balance}")
        else:
            print("Invalid PIN. Access denied.")

    # Private method (for internal class use only)
    def __verify_pin(self, pin):
        return pin == self.__pin

    # Public method to change PIN (uses private method to verify)
    def change_pin(self, old_pin, new_pin):
        if self.__verify_pin(old_pin):
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN. PIN change failed.")


# Usage example
account = BankAccount("Alice", 1000, 1234)

# Public methods
account.deposit(200)  # Deposit money
account.withdraw(200, 1234)  # Withdraw money with correct PIN
account.get_balance(1234)  # Check balance with correct PIN
account.change_pin(1234, 5678)  # Change PIN with correct old PIN

# Trying to access private attribute directly (raises AttributeError)
# print(account.__balance)          # Not accessible directly
# print(account.__pin)              # Not accessible directly