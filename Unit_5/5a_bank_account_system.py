print("BANK ACCOUNT SYSTEM")

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\nAccount Holder:", self.name)
        print("Available Balance:", self.balance)

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))
account = BankAccount(name, balance)
deposit = float(input("Enter deposit amount: "))
account.deposit(deposit)
withdraw = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw)
account.display()
