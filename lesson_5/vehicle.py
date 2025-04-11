class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Паливо: {self.fuel_type}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def mileage_meter(self):
        print(f"Пробіг: {self.mileage} км")

v1 = Car("Toyota", "Corolla", 2020, "бензин")
v2 = Bicycle("Forte", "FT300-R1", 2021, 18000)

print(v1.make, v1.model, v1.year, v1.fuel_type)
v1.start_engine()

print(v2.make, v2.model, v2.year, v2.mileage)
v2.mileage_meter()
