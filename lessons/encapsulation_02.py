# ============================================================
# ENCAPSULATION WITH @property
# ============================================================


class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner

        # ====================================================
        # PRIVATE ATTRIBUTE
        # ====================================================
        #
        # __balance is intended to be internal/private.
        #
        # Outside code should not directly modify it.
        # ====================================================

        self.__balance = balance

    # ========================================================
    # PROPERTY
    # ========================================================
    #
    # @property allows us to READ the private value using
    # normal attribute syntax.
    #
    # Instead of:
    #
    #     suraj.get_balance()
    #
    # we can write:
    #
    #     suraj.balance
    #
    # ========================================================

    @property
    def balance(self):

        return self.__balance

    # ========================================================
    # DEPOSIT
    # ========================================================

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.__balance += amount

        print(f"Deposited ₹{amount}")

    # ========================================================
    # WITHDRAW
    # ========================================================

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount

        print(f"Withdrawn ₹{amount}")


# ============================================================
# CREATE ACCOUNT
# ============================================================

suraj = BankAccount("Suraj", 5000)


# ============================================================
# READ BALANCE
# ============================================================
#
# Notice:
#
# We are using:
#
#     suraj.balance
#
# NOT:
#
#     suraj.__balance
#
# ============================================================

print(suraj.balance)


# ============================================================
# DEPOSIT
# ============================================================

suraj.deposit(1000)

print(suraj.balance)


# ============================================================
# WITHDRAW
# ============================================================

suraj.withdraw(500)

print(suraj.balance)


# ============================================================
# INVALID WITHDRAWAL
# ============================================================

suraj.withdraw(10000)

print(suraj.balance)


# ============================================================
# INVALID DEPOSIT
# ============================================================

suraj.deposit(-500)

print(suraj.balance)


# ============================================================
# TRY DIRECT MODIFICATION
# ============================================================
#
# Uncomment this and run it:
#
# suraj.balance = -100000
#
# Because we have created a property without a setter,
# Python will not allow assignment.
# ============================================================
