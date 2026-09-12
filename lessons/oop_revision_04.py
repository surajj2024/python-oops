class Product:
    company = "Amazon"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        print(f"this is the name {self.name} and this is the price {self.price} ")

    def apply_discount(self, percent):
        self.price = self.price * (100 - percent) / 100

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"])


phone = Product("iPhone", 80000)
laptop = Product("Laptop", 60000)

phone.show_details()
phone.apply_discount(10)
phone.show_details()
phone.change_company("flipkart")
phone.show_details()
laptop.show_details()

data = {"name": "freeze", "price": 50000}
freeze = Product.from_dict(data)
freeze.show_details()

# Why is price an instance variable?
# because it point to a particular object

# Why is company a class variable?
# because it is for all the employee not for a particular employee for all the persons

# Why is change_company() a class method?
# because company is class 

# Why is from_dict() a class method?
# this i dont know i want to revise this topic once more 