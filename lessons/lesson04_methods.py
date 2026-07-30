class Bike:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Bike started {self.name}")


hunter = Bike("Hunter")
ktm = Bike("KTM")

hunter.start()
ktm.start()
