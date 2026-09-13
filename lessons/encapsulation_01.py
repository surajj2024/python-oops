# ============================================================
# PYTHON OOP - LESSON 6
# ENCAPSULATION
# ============================================================
#
# Encapsulation means:
#
#     Keeping data and behavior together
#     AND controlling how the object's data is accessed
#     or modified.
#
# REAL-LIFE EXAMPLE:
#
# A bank account should control its balance.
#
# We should not allow random code to put the account into
# an invalid state.
#
# ============================================================


class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):

        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def show_balance(self):

        print(f"Balance: ₹{self.balance}")


# ============================================================
# CREATE ACCOUNT
# ============================================================

suraj = BankAccount("Suraj", 5000)

suraj.show_balance()


# ============================================================
# PROBLEM
# ============================================================
#
# balance is PUBLIC.
#
# Therefore, someone can directly change it.
# ============================================================

suraj.balance = -100000

suraj.show_balance()
