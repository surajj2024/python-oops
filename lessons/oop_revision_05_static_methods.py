# ============================================================
# PYTHON OOP
# LESSON 5 - STATIC METHODS
# ============================================================
#
# We have now learned three types of methods:
#
# 1. Instance Method
# 2. Class Method
# 3. Static Method
#
# ============================================================
#
# QUICK MEMORY:
#
# Instance Method
#     ↓
# self
#     ↓
# Works with OBJECT
#
#
# Class Method
#     ↓
# cls
#     ↓
# Works with CLASS
#
#
# Static Method
#     ↓
# No self
# No cls
#     ↓
# Independent utility/function
#
# ============================================================


class Employee:

    # ========================================================
    # CLASS VARIABLE
    # ========================================================
    #
    # This belongs to the class.
    # ========================================================

    company = "Google"

    # ========================================================
    # CONSTRUCTOR
    # ========================================================
    #
    # Creates and initializes an Employee object.
    # ========================================================

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary

    # ========================================================
    # INSTANCE METHOD
    # ========================================================
    #
    # This method works with a particular Employee object.
    #
    # Therefore we use:
    #
    #     self
    #
    # Example:
    #
    #     suraj.show_details()
    #
    # self = suraj
    # ========================================================

    def show_details(self):

        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")

    # ========================================================
    # CLASS METHOD
    # ========================================================
    #
    # This method works with the CLASS.
    #
    # Therefore we use:
    #
    #     cls
    #
    # Example:
    #
    #     Employee.change_company("Microsoft")
    #
    # cls = Employee
    # ========================================================

    @classmethod
    def change_company(cls, new_company):

        cls.company = new_company

    # ========================================================
    # STATIC METHOD
    # ========================================================
    #
    # A static method does NOT receive:
    #
    #     self
    #
    # and does NOT receive:
    #
    #     cls
    #
    # It behaves like a normal function.
    #
    # The reason we put it inside the class is because the
    # functionality is logically related to Employee.
    #
    # ========================================================
    #
    # Example:
    #
    #     Employee.is_valid_salary(50000)
    #
    # We don't need an Employee object to answer:
    #
    #     "Is 50000 a valid salary?"
    #
    # We only need the salary value.
    # ========================================================

    @staticmethod
    def is_valid_salary(salary):

        # Salary should be greater than zero.

        return salary > 0


# ============================================================
# CREATE AN EMPLOYEE
# ============================================================

suraj = Employee("Suraj", 50000)


# ============================================================
# INSTANCE METHOD
# ============================================================
#
# Requires an object.
# ============================================================

suraj.show_details()


# ============================================================
# CLASS METHOD
# ============================================================
#
# Works with the class.
# ============================================================

Employee.change_company("Microsoft")


# Check the new company.

suraj.show_details()


# ============================================================
# STATIC METHOD
# ============================================================
#
# Notice something important:
#
# We don't need to create an Employee object to use this.
#
# We can directly call:
#
#     Employee.is_valid_salary()
#
# ============================================================

print(Employee.is_valid_salary(50000))

print(Employee.is_valid_salary(-5000))


# Expected:
#
# True
# False


# ============================================================
# IMPORTANT
# ============================================================
#
# Static methods are useful when:
#
# 1. The function is logically related to the class.
#
# 2. But the function doesn't need object data.
#
# 3. And it doesn't need class data.
#
# ============================================================
