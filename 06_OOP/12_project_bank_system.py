"""
=========================================================
            MINI PROJECT - BANK MANAGEMENT SYSTEM
=========================================================

Concepts Used

- Class
- Object
- Constructor
- Instance Variables
- Methods
- Encapsulation
- Loops
- Conditionals

"""


# =========================================================
# Bank Account Class
# =========================================================

class BankAccount:

    def __init__(self, account_holder, balance=0):

        self.account_holder = account_holder

        self.__balance = balance

        self.transactions = []

    # -----------------------------------------------------

    def deposit(self, amount):

        if amount <= 0:

            print("Invalid Amount")

            return

        self.__balance += amount

        self.transactions.append(f"Deposited ₹{amount}")

        print("Deposit Successful")

    # -----------------------------------------------------

    def withdraw(self, amount):

        if amount <= 0:

            print("Invalid Amount")

            return

        if amount > self.__balance:

            print("Insufficient Balance")

            return

        self.__balance -= amount

        self.transactions.append(f"Withdrawn ₹{amount}")

        print("Withdrawal Successful")

    # -----------------------------------------------------

    def check_balance(self):

        print(f"Current Balance : ₹{self.__balance}")

    # -----------------------------------------------------

    def show_transactions(self):

        print("\n========== TRANSACTIONS ==========")

        if len(self.transactions) == 0:

            print("No Transactions Found")

            return

        for transaction in self.transactions:

            print(transaction)

    # -----------------------------------------------------

    def account_details(self):

        print("\n========== ACCOUNT DETAILS ==========")

        print("Holder :", self.account_holder)

        print("Balance:", self.__balance)


# =========================================================
# Create Account
# =========================================================

account = BankAccount("Vinita", 5000)


# =========================================================
# Menu
# =========================================================

while True:

    print("\n========== BANK MENU ==========")

    print("1. Deposit")

    print("2. Withdraw")

    print("3. Check Balance")

    print("4. Transaction History")

    print("5. Account Details")

    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        amount = float(input("Enter Amount: "))

        account.deposit(amount)

    elif choice == "2":

        amount = float(input("Enter Amount: "))

        account.withdraw(amount)

    elif choice == "3":

        account.check_balance()

    elif choice == "4":

        account.show_transactions()

    elif choice == "5":

        account.account_details()

    elif choice == "6":

        print("\nThank You for Using Our Bank!")

        break

    else:

        print("Invalid Choice")