# ============================================================
# PYTHON OOP - ENCAPSULATION
# BankAccount Example
# ============================================================
#
# MAIN IDEA:
#
# Encapsulation means protecting an object's internal data
# and controlling how that data can be accessed or changed.
#
# In this example:
#
#     __balance
#
# is our private/internal data.
#
# We don't want outside code to directly modify it.
#
# Instead, we provide controlled methods:
#
#     deposit()
#     withdraw()
#
# to change the balance.
#
# We also provide:
#
#     @property
#
# so that outside code can READ the balance safely.
# ============================================================


class BankAccount:

    # ========================================================
    # CONSTRUCTOR
    # ========================================================
    #
    # __init__ runs when we create a BankAccount object.
    #
    # Example:
    #
    #     suraj = BankAccount("Suraj", 5000)
    #
    # ========================================================

    def __init__(self, owner, balance):

        self.owner = owner

        # __balance is a private/internal attribute.
        #
        # We don't want users of this class to directly change
        # the balance.
        #
        # Instead, they should use deposit() and withdraw().

        self.__balance = balance

    # ========================================================
    # PROPERTY / GETTER
    # ========================================================
    #
    # @property allows us to READ __balance using:
    #
    #     suraj.balance
    #
    # instead of:
    #
    #     suraj.get_balance()
    #
    # The actual value is still stored in:
    #
    #     self.__balance
    # ========================================================

    @property
    def balance(self):

        return self.__balance

    # ========================================================
    # DEPOSIT
    # ========================================================
    #
    # This method changes the private balance in a controlled
    # way.
    #
    # amount = money we want to ADD.
    # ========================================================

    def deposit(self, amount):

        # Deposit amount must be positive.

        if amount <= 0:

            print("Deposit amount must be greater than 0.")

            return

        # Update the private balance.

        self.__balance += amount

        print(f"Deposited ₹{amount}")

    # ========================================================
    # WITHDRAW
    # ========================================================
    #
    # This method changes the private balance in a controlled
    # way.
    #
    # amount = money we want to REMOVE.
    # ========================================================

    def withdraw(self, amount):

        # Withdrawal amount must be positive.

        if amount <= 0:

            print("Withdrawal amount must be greater than 0.")

            return

        # Don't allow the account to go below zero.

        if amount > self.__balance:

            print("Insufficient balance.")

            return

        # Update the private balance.

        self.__balance -= amount

        print(f"Withdrawn ₹{amount}")


# ============================================================
# CREATE OBJECT
# ============================================================

suraj = BankAccount("Suraj", 5000)


# ============================================================
# READ BALANCE
# ============================================================
#
# This works because balance is exposed through @property.
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

suraj.withdraw(2000)

print(suraj.balance)


# ============================================================
# TEST INVALID WITHDRAWAL
# ============================================================

suraj.withdraw(10000)

print(suraj.balance)


# ============================================================
# TEST INVALID DEPOSIT
# ============================================================

suraj.deposit(-500)

print(suraj.balance)


# ============================================================
# TEST DIRECT MODIFICATION
# ============================================================
#
# This should FAIL because we did not create a setter.
#
# Python will raise an AttributeError.
#
# We can READ:
#
#     suraj.balance
#
# But we cannot directly SET:
#
#     suraj.balance = -100000
#
# This is one of the benefits of encapsulation.
# ============================================================

# suraj.balance = -100000
