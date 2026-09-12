class BankAccount:
    bank_name = "SBI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, add_money):
        if add_money > 0:
            self.balance += add_money

    def withdraw(self, deduct_money):
        if deduct_money > 0:
            self.balance -= deduct_money

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(balance):
        return balance >= 0


# 1. Create two accounts
# 2. Deposit money
# 3. Withdraw money
# 4. Change bank name
# 5. Check valid amount
# 6. Check invalid amount

suraj = BankAccount("suraj", 500)
hem = BankAccount("Hem", 100)

suraj.deposit(500)

suraj.withdraw(100)

suraj.change_bank_name("FBI")

suraj.is_valid_amount(500)
suraj.is_valid_amount(-100)

# Why is deposit() an instance method?
# because it will have to deposite in a particular object/user

# Why is withdraw() an instance method?
# because it will have to deposite in a particular object/user

# Why is change_bank_name() a class method?
# because it has to update the global name of the bank

# Why is is_valid_amount() a static method?
# becuase it neither of the class not instance


# ============================================================
# THREE TYPES OF METHODS
# ============================================================
#
# 1. INSTANCE METHOD
# ------------------------------------------------------------
#
# def deposit(self, amount):
#
# Uses:
#     self
#
# self = current OBJECT
#
# Use when the method needs to work with data belonging
# to a particular object.
#
# Example:
#
#     suraj.deposit(500)
#
#
# ============================================================
#
# 2. CLASS METHOD
# ------------------------------------------------------------
#
# @classmethod
# def change_bank_name(cls, name):
#
# Uses:
#     cls
#
# cls = current CLASS
#
# Use when the method needs to work with class-level data
# or perform an operation related to the class itself.
#
# Example:
#
#     BankAccount.change_bank_name("HDFC")
#
#
# ============================================================
#
# 3. STATIC METHOD
# ------------------------------------------------------------
#
# @staticmethod
# def is_valid_amount(amount):
#
# Uses:
#     neither self nor cls
#
# Use when the method does not need object data or class data.
# It is simply utility logic that is logically related to
# the class.
#
# Example:
#
#     BankAccount.is_valid_amount(500)
#
#
# ============================================================
#
# EASY WAY TO REMEMBER
# ============================================================
#
# OBJECT?
#     ↓
# self
#
# CLASS?
#     ↓
# cls
#
# NEITHER?
#     ↓
# staticmethod
#
# ============================================================
