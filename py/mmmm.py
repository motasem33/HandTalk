class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance =int(balance)

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(self.balance)

acc1 = BankAccount("Ali", 1000)
acc2 = BankAccount("Sara", 500)

acc1.deposit(200)
acc1.withdraw(150)

acc2.deposit(300)
acc2.withdraw(1000)