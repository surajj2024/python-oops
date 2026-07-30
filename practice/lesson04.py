# class Bike:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

#     def start(self):
#         print(f"{self.brand} , ({self.color}) started")

#     def stop(self):
#         print(f"{self.brand} , ({self.color}) stopped")


# hunter = Bike("hunter 350", "white")
# ktm = Bike("ktm 350", "red")

# hunter.start()
# hunter.stop()
# ktm.start()
# ktm.stop()


class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def start(self):
        print(f"started {self.brand}")

    def stop(self):
        print(f"started {self.brand}")

    def refuel(self):
        print(f"{self.brand} refuel within the {self.fuel}")
        
bmw = Car("BMW", "m3", 40)

bmw.refuel()
