# class Student:

#     def __init__(self, name, age, course, marks):
#         self.name = name
#         self.age = age
#         self.course = course
#         self.marks = marks

#     def study():
#         print(f"Started study")

#     def attend_class():
#         print(f"attend class")

#     def show_details(self):
#         print(f"name is {self.name} and age is {self.age} and marks is {self.marks}")

#     def add_marks(self, marks):
#         self.marks += marks


# suraj = Student("suraj", 21, "math", 90)
# mohni = Student("Moh", 22, "English", 89)

# suraj.show_details();

# suraj.add_marks(20);
# suraj.show_details();


# ============================================================
# PYTHON OOP REVISION
# TOPIC: CLASSES, OBJECTS, __init__, self & INSTANCE METHODS
# ============================================================
#
# REAL-LIFE EXAMPLE:
#
# Imagine we are building a Student Management System.
#
# Every student has their own:
#
#     name
#     age
#     course
#     marks
#
# Every student can also perform actions:
#
#     study()
#     attend_class()
#     show_details()
#     add_marks()
#
# OOP allows us to keep the student's DATA and BEHAVIOUR
# together inside one class.
#
# ============================================================


# ============================================================
# CLASS
# ============================================================
#
# A class is a BLUEPRINT.
#
# Student is not an actual student.
#
# It describes what every Student object should contain
# and what a Student object should be able to do.
# ============================================================


class Student:

    # ========================================================
    # CONSTRUCTOR
    # ========================================================
    #
    # __init__() runs automatically when we create an object.
    #
    # Example:
    #
    #     suraj = Student("Suraj", 21, "Math", 90)
    #
    # Python automatically calls __init__() for us.
    #
    # self represents the object currently being created.
    # ========================================================

    def __init__(self, name, age, course, marks):

        # These are INSTANCE VARIABLES.
        #
        # Instance variables belong to a particular object.
        #
        # Suraj will have his own values.
        # Mohni will have her own values.

        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    # ========================================================
    # INSTANCE METHOD
    # ========================================================
    #
    # study() is an instance method.
    #
    # Why?
    #
    # Because a particular Student object performs this action.
    #
    # Example:
    #
    #     suraj.study()
    #
    # Python approximately treats this as:
    #
    #     Student.study(suraj)
    #
    # Therefore Python passes "suraj" as self.
    # ========================================================

    def study(self):

        print(f"{self.name} started studying.")

    # ========================================================
    # ANOTHER INSTANCE METHOD
    # ========================================================
    #
    # attend_class() also belongs to an individual Student.
    #
    # Therefore it needs self.
    # ========================================================

    def attend_class(self):

        print(f"{self.name} is attending class.")

    # ========================================================
    # INSTANCE METHOD
    # ========================================================
    #
    # show_details() displays data belonging to THIS student.
    #
    # self.name
    # self.age
    # self.course
    # self.marks
    #
    # all belong to the current object.
    # ========================================================

    def show_details(self):

        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")
        print(f"Marks  : {self.marks}")

    # ========================================================
    # INSTANCE METHOD THAT CHANGES OBJECT STATE
    # ========================================================
    #
    # add_marks() changes the student's marks.
    #
    # Example:
    #
    #     Suraj currently has 90 marks.
    #
    #     suraj.add_marks(20)
    #
    #     90 + 20 = 110
    #
    # self.marks refers to the marks belonging to THIS student.
    # ========================================================

    def add_marks(self, additional_marks):

        self.marks += additional_marks


# ============================================================
# CREATE OBJECT 1
# ============================================================
#
# Student = CLASS
#
# suraj = OBJECT
#
# Suraj gets his own instance variables.
# ============================================================

suraj = Student("Suraj", 21, "Math", 90)


# ============================================================
# CREATE OBJECT 2
# ============================================================
#
# Mohni is a completely separate Student object.
#
# Her values do NOT belong to Suraj.
# ============================================================

mohni = Student("Mohni", 22, "English", 89)


# ============================================================
# CALL METHODS
# ============================================================

suraj.study()

suraj.attend_class()

suraj.show_details()


# ============================================================
# CHANGE ONLY SURAJ'S MARKS
# ============================================================

suraj.add_marks(20)


# Suraj's marks changed from 90 to 110.

suraj.show_details()


# ============================================================
# CHECK MOHNI
# ============================================================
#
# Mohni's marks should still be 89.
#
# Why?
#
# Because self referred to Suraj when we called:
#
#     suraj.add_marks(20)
#
# It did NOT refer to Mohni.
# ============================================================

mohni.show_details()


# ============================================================
# IMPORTANT REMEMBER
# ============================================================
#
# CLASS
#   ↓
# Blueprint
#
# OBJECT
#   ↓
# Actual thing created from the blueprint
#
# __init__()
#   ↓
# Automatically initializes the object
#
# self
#   ↓
# Current object
#
# self.name
#   ↓
# Name belonging to the current object
#
# Instance Variable
#   ↓
# Data belonging to one particular object
#
# Instance Method
#   ↓
# Behaviour/action performed by an object
#
# ============================================================

print(suraj.marks)
print(mohni.marks)
