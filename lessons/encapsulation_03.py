# ============================================================
# PYTHON OOP - ENCAPSULATION COMPLETE EXAMPLE
# ============================================================
#
# CONCEPTS:
#
# 1. Private attribute
# 2. @property
# 3. @setter
# 4. Data validation
#
# ============================================================

# ============================================================
# ENCAPSULATION - QUICK REVISION
# ============================================================
#
# PUBLIC
# -------
# self.balance
#
# Directly accessible from outside.
#
#
# PROTECTED CONVENTION
# --------------------
# self._balance
#
# Means:
# "This is intended for internal use."
#
# It is a convention, not strict privacy.
#
#
# PRIVATE / NAME MANGLED
# ----------------------
# self.__balance
#
# Python performs name mangling.
#
#
# @property
# ---------
# Allows us to READ a private/internal value using:
#
#     object.balance
#
#
# @setter
# -------
# Allows us to CONTROL how a property is changed:
#
#     object.balance = value
#
#
# GETTER
# ------
# Reads data.
#
#
# SETTER
# ------
# Changes data with validation/control.
#
#
# MAIN IDEA
# ---------
# Encapsulation protects an object's internal state and
# controls how that state can be accessed or modified.
#
# ============================================================


class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner

        # Private attribute.
        #
        # External code should interact with balance through
        # the property instead of directly modifying this.

        self.__balance = balance

    # ========================================================
    # GETTER / PROPERTY
    # ========================================================
    #
    # Allows us to READ the balance:
    #
    #     suraj.balance
    #
    # Internally:
    #
    #     return self.__balance
    # ========================================================

    @property
    def balance(self):

        return self.__balance

    # ========================================================
    # SETTER
    # ========================================================
    #
    # Allows us to CONTROL how balance is changed.
    #
    # When we write:
    #
    #     suraj.balance = 10000
    #
    # Python calls this setter.
    # ========================================================

    @balance.setter
    def balance(self, new_balance):

        if new_balance < 0:

            print("Balance cannot be negative.")

            return

        self.__balance = new_balance

    # ========================================================
    # DEPOSIT
    # ========================================================

    def deposit(self, amount):

        if amount <= 0:

            print("Deposit must be greater than 0.")

            return

        self.__balance += amount

    # ========================================================
    # WITHDRAW
    # ========================================================

    def withdraw(self, amount):

        if amount <= 0:

            print("Withdrawal must be greater than 0.")

            return

        if amount > self.__balance:

            print("Insufficient balance.")

            return

        self.__balance -= amount


# ============================================================
# CREATE ACCOUNT
# ============================================================

suraj = BankAccount("Suraj", 5000)


# ============================================================
# READ BALANCE
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
# SET BALANCE THROUGH PROPERTY
# ============================================================

suraj.balance = 10000

print(suraj.balance)


# ============================================================
# TRY INVALID BALANCE
# ============================================================

suraj.balance = -5000

print(suraj.balance)


# ============================================================
# ENCAPSULATION - QUICK REVISION
# ============================================================
#
# PUBLIC
# -------
# self.balance
#
# Directly accessible from outside.
#
#
# PROTECTED CONVENTION
# --------------------
# self._balance
#
# Means:
# "This is intended for internal use."
#
# It is a convention, not strict privacy.
#
#
# PRIVATE / NAME MANGLED
# ----------------------
# self.__balance
#
# Python performs name mangling.
#
#
# @property
# ---------
# Allows us to READ a private/internal value using:
#
#     object.balance
#
#
# @setter
# -------
# Allows us to CONTROL how a property is changed:
#
#     object.balance = value
#
#
# GETTER
# ------
# Reads data.
#
#
# SETTER
# ------
# Changes data with validation/control.
#
#
# MAIN IDEA
# ---------
# Encapsulation protects an object's internal state and
# controls how that state can be accessed or modified.
#
# ============================================================
