class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


acct = BankAccount("Hubert")
print(acct.owner)
print(acct.balance)

acct.deposit(20)
print(acct.balance)

acct.withdraw(10)
print(acct.balance)
