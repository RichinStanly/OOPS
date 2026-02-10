#abstraction
# implementation details and showing only essential features.

class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
                                   # Car and Bike override the start() method with their own implementations
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()
