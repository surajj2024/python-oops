# ============================================================
# PYTHON OOP REVISION - PART 2
# ============================================================
#
# TOPICS:
#
# 1. Instance Variables
# 2. Class Variables
# 3. Instance Methods
# 4. Class Methods
# 5. self
# 6. cls
# 7. Factory Methods
#
# ============================================================


# ============================================================
# REAL-LIFE EXAMPLE
# ============================================================
#
# Imagine we are building an Employee Management System.
#
# Every employee has their own:
#
#     name
#     salary
#
# But all employees work for the same company.
#
# Therefore:
#
#     name   -> INSTANCE VARIABLE
#     salary -> INSTANCE VARIABLE
#     company -> CLASS VARIABLE
#
# ============================================================


class Employee:

    # ========================================================
    # CLASS VARIABLE
    # ========================================================
    #
    # company belongs to the CLASS.
    #
    # All Employee objects can access it.
    #
    # Example:
    #
    #     Employee.company
    #
    # gives:
    #
    #     Google
    #
    # ========================================================

    company = "Google"

    # ========================================================
    # CONSTRUCTOR
    # ========================================================
    #
    # __init__() runs automatically whenever an Employee
    # object is created.
    #
    # self represents the current object.
    #
    # ========================================================

    def __init__(self, name, salary):

        # ====================================================
        # INSTANCE VARIABLES
        # ====================================================
        #
        # These belong to the particular Employee object.
        #
        # If we create:
        #
        #     suraj = Employee("Suraj", 40000)
        #
        # then:
        #
        #     self = suraj
        #
        # and:
        #
        #     self.name = "Suraj"
        #     self.salary = 40000
        #
        # ====================================================

        self.name = name
        self.salary = salary

    # ========================================================
    # INSTANCE METHOD
    # ========================================================
    #
    # show_details() works with ONE particular employee.
    #
    # Therefore it uses self.
    #
    # Example:
    #
    #     suraj.show_details()
    #
    # approximately becomes:
    #
    #     Employee.show_details(suraj)
    #
    # ========================================================

    def show_details(self):

        print(f"Name    : {self.name}")
        print(f"Salary  : ₹{self.salary}")
        print(f"Company : {self.company}")

    # ========================================================
    # CLASS METHOD
    # ========================================================
    #
    # @classmethod tells Python:
    #
    # "Pass the CLASS automatically to this method."
    #
    # Instead of self, we use cls.
    #
    # self -> current OBJECT
    #
    # cls  -> current CLASS
    #
    # ========================================================

    @classmethod
    def change_company(cls, new_name):

        # ====================================================
        # We are changing data that belongs to the CLASS.
        #
        # Therefore we use:
        #
        #     cls.company
        #
        # NOT:
        #
        #     self.company
        #
        # because this method is working at class level.
        # ====================================================

        cls.company = new_name

    # ========================================================
    # FACTORY METHOD
    # ========================================================
    #
    # A factory method is a method that creates and returns
    # an object.
    #
    # Here we receive a dictionary and convert it into an
    # Employee object.
    #
    # Example input:
    #
    #     {
    #         "name": "Suraj",
    #         "salary": 40000
    #     }
    #
    # ========================================================

    @classmethod
    def from_dict(cls, data):

        # ====================================================
        # cls represents Employee.
        #
        # Therefore:
        #
        #     cls(...)
        #
        # creates an Employee object.
        #
        # This is approximately:
        #
        #     Employee(...)
        #
        # But using cls is better because it also works
        # correctly with inheritance/subclasses.
        #
        # We will understand that deeply when we learn
        # INHERITANCE.
        # ====================================================

        return cls(data["name"], data["salary"])


# ============================================================
# CREATE EMPLOYEE OBJECTS
# ============================================================

suraj = Employee("Suraj", 40000)

rahul = Employee("Rahul", 30000)


# ============================================================
# INSTANCE DATA
# ============================================================
#
# Every object has its own name and salary.
# ============================================================

print(suraj.name)
print(suraj.salary)

print(rahul.name)
print(rahul.salary)


# ============================================================
# CLASS DATA
# ============================================================
#
# Both objects can access the class variable.
# ============================================================

print(suraj.company)

print(rahul.company)

print(Employee.company)


# ============================================================
# CHANGE COMPANY
# ============================================================
#
# This operation belongs to the CLASS.
#
# Therefore, it is better to call the class method using
# the class itself.
#
# ============================================================

Employee.change_company("Microsoft")


# ============================================================
# BOTH EMPLOYEES NOW SEE THE NEW COMPANY
# ============================================================

print(suraj.company)

print(rahul.company)


# ============================================================
# SHOW DETAILS
# ============================================================

suraj.show_details()

rahul.show_details()


# ============================================================
# FACTORY METHOD
# ============================================================
#
# Imagine this data came from:
#
#     database
#     JSON
#     API
#     configuration file
#
# ============================================================

data = {"name": "Mohni", "salary": 35000}


# from_dict() creates an Employee object from the dictionary.

mohni = Employee.from_dict(data)


# ============================================================
# CHECK THE NEW OBJECT
# ============================================================

mohni.show_details()


# ============================================================
# IMPORTANT MEMORY
# ============================================================
#
# INSTANCE VARIABLE
# -----------------
#
# self.name
# self.salary
#
# Belongs to ONE object.
#
#
# CLASS VARIABLE
# --------------
#
# company
#
# Belongs to the CLASS and can be shared by objects.
#
#
# INSTANCE METHOD
# ---------------
#
# def show_details(self):
#
# Works with a particular object.
#
#
# CLASS METHOD
# ------------
#
# @classmethod
# def change_company(cls):
#
# Works with the class.
#
#
# self
# ----
#
# Current OBJECT.
#
#
# cls
# ---
#
# Current CLASS.
#
#
# FACTORY METHOD
# --------------
#
# A class method that creates/returns an object.
#
# Example:
#
#     Employee.from_dict(data)
#
# ============================================================
