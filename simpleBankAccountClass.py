class BankAccount:

    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

# representation of bank account object
    def __repr__(self):
        return f"Owner is {self.owner} and account balance is {self.balance}"

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

print(acct)
