class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        print(f"New account initalized for {self.name}")

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} Deposited {amount} $. Current balance is: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} Withdrew {amount} $. Current balance is: {self.balance}")
        else:
            print(f"You don't have enough funds to withdraw. Current balance is: {self.balance}")

class Savings_Account(Account):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Added interest. Current balance is: {self.balance}")


account1 = Account("John Carter", "35647", 1000)
account1.deposit(500)
account1.withdraw(200)

print()

account2 = Savings_Account("Valentine Jons", "34566", 1000, 0.05)
account2.deposit(500)
account2.withdraw(200)
account2.add_interest()