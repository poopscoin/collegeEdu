class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"Топливо: {self.fuel_type}")

    def display_info(self):
        print(f"Авто: {self.make} {self.model}, {self.year}, паливо: {self.fuel_type}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year)
        self.mileage = mileage

    def mileage_meter(self):
        print(f"Пробіг: {self.mileage} км")

    def display_info(self):
        print(f"Велосипед: {self.make} {self.model}, {self.year}, пробіг: {self.mileage}")

v1 = Car("Toyota", "Corolla", 2020, "бензин")
v2 = Bicycle("Forte", "FT300-R1", 2021, 18000)

for v in [v1, v2]:
    v.display_info()
