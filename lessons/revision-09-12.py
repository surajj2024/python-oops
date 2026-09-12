# ============================================================
# PYTHON OOP REVISION
# ============================================================
#
# TOPICS COVERED IN THIS FILE:
#
# 1. Class
# 2. Object
# 3. __init__()
# 4. self
# 5. Instance Variables
# 6. Instance Methods
#
# ============================================================


# ============================================================
# 1. CLASS
# ============================================================
#
# A CLASS is a blueprint/template for creating objects.
#
# Real-life example:
#
# Imagine a car manufacturing company.
#
# They don't manually design every car from scratch.
#
# They create a design/blueprint that says:
#
#     A car should have:
#         - brand
#         - model
#         - fuel
#
#     A car should be able to:
#         - start
#         - stop
#         - refuel
#
# In Python, we represent that blueprint using a CLASS.
# ============================================================


class Car:

    # ========================================================
    # 2. __init__() - CONSTRUCTOR
    # ========================================================
    #
    # __init__() is a special method.
    #
    # Python automatically calls __init__() when we create
    # an object.
    #
    # Example:
    #
    #     bmw = Car("BMW", "M3", 40)
    #
    # Python automatically calls:
    #
    #     Car.__init__(bmw, "BMW", "M3", 40)
    #
    # We will understand this "bmw" / "self" relationship
    # shortly.
    # ========================================================

    def __init__(self, brand, model, fuel):

        # ====================================================
        # 3. self
        # ====================================================
        #
        # self represents the CURRENT OBJECT.
        #
        # If we write:
        #
        #     bmw = Car("BMW", "M3", 40)
        #
        # then inside __init__():
        #
        #     self = bmw
        #
        # If we later create:
        #
        #     audi = Car("Audi", "A4", 50)
        #
        # then:
        #
        #     self = audi
        #
        # So self changes depending on which object is
        # calling the method.
        # ====================================================

        # ====================================================
        # 4. INSTANCE VARIABLES
        # ====================================================
        #
        # Variables created using self belong to the OBJECT.
        #
        # Therefore:
        #
        #     self.brand
        #     self.model
        #     self.fuel
        #
        # are INSTANCE VARIABLES.
        #
        # Each object gets its own values.
        #
        # Example:
        #
        # BMW:
        #     brand = BMW
        #     model = M3
        #     fuel  = 40
        #
        # Audi:
        #     brand = Audi
        #     model = A4
        #     fuel  = 50
        #
        # They don't share these values.
        # ====================================================

        self.brand = brand
        self.model = model
        self.fuel = fuel

    # ========================================================
    # 5. INSTANCE METHOD
    # ========================================================
    #
    # A method is a function defined inside a class.
    #
    # This is an INSTANCE METHOD because it works with the
    # data of a particular object.
    #
    # Example:
    #
    #     bmw.start()
    #
    # Python approximately treats this as:
    #
    #     Car.start(bmw)
    #
    # Therefore:
    #
    #     self = bmw
    # ========================================================

    def start(self):

        print(f"{self.brand} {self.model} started.")

    def stop(self):

        print(f"{self.brand} {self.model} stopped.")

    def refuel(self, liters):

        # We are changing the state of THIS particular car.
        #
        # Example:
        #
        # BMW currently has 40 liters.
        #
        # bmw.refuel(10)
        #
        # New fuel:
        #
        # 40 + 10 = 50

        self.fuel += liters

        print(f"{self.brand} {self.model} refueled with " f"{liters} liters.")

        print(f"Current fuel: {self.fuel} liters")


# ============================================================
# 6. CREATING AN OBJECT
# ============================================================
#
# Car = CLASS
#
# bmw = OBJECT
#
# We are creating an actual Car object from the Car blueprint.
# ============================================================

bmw = Car("BMW", "M3", 40)


# ============================================================
# 7. ACCESSING INSTANCE VARIABLES
# ============================================================
#
# bmw has its own:
#
#     brand
#     model
#     fuel
#
# We access them using:
#
#     object.variable
# ============================================================

print(bmw.brand)
print(bmw.model)
print(bmw.fuel)


# ============================================================
# 8. CALLING INSTANCE METHODS
# ============================================================

bmw.start()

bmw.refuel(10)

bmw.stop()


# ============================================================
# EXPECTED OUTPUT
# ============================================================
#
# BMW
# M3
# 40
# BMW M3 started.
# BMW M3 refueled with 10 liters.
# Current fuel: 50 liters
# BMW M3 stopped.
#
# ============================================================


