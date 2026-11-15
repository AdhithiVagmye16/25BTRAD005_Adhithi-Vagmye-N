# ============================================================
# Lab Exercise 14: Bank Account System using OOP
# Name   : Adhithi Vagmye
# USN    : 25BTRAD005
# ============================================================

class BankAccount:
    def __init__(self, acc_no, holder, balance=0):
        self.acc_no = acc_no
        self.holder = holder
        self.__balance = balance      # private attribute (encapsulation)
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount. Deposit must be positive.")
            return
        self.__balance += amount
        self.history.append(f"Deposited Rs.{amount}")
        print(f"Deposited Rs.{amount}. New balance: Rs.{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount. Withdrawal must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance. Transaction declined.")
        else:
            self.__balance -= amount
            self.history.append(f"Withdrew Rs.{amount}")
            print(f"Withdrew Rs.{amount}. New balance: Rs.{self.__balance}")

    def get_balance(self):
        return self.__balance

    def show_history(self):
        if not self.history:
            print("No transactions yet.")
        for i, t in enumerate(self.history, 1):
            print(f"{i}. {t}")


name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")
opening = int(input("Enter opening balance: "))
account = BankAccount(acc_no, name, opening)
print(f"Account created for {account.holder} (A/C {account.acc_no}).")

while True:
    print("\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        account.deposit(int(input("Enter amount: ")))
    elif choice == "2":
        account.withdraw(int(input("Enter amount: ")))
    elif choice == "3":
        print(f"Current balance: Rs.{account.get_balance()}")
    elif choice == "4":
        account.show_history()
    elif choice == "5":
        print("Thank you for banking with us.")
        break
    else:
        print("Invalid choice.")
