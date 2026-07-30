class BankAccount:
    bank_name: "SBI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Add {amount} to you account")
        print(f"bank balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance")
            return
        self.balance -= amount
        print(f"withdraw from your account {amount}")
        print(f"bank balance is {self.balance}")


suraj = BankAccount("suraj", 40000)
# suraj.deposit(10000)
suraj.withdraw(40000)
