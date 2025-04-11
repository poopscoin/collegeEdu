class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} : {self.sound}!")

a1 = Animal("Мурчик", "кіт", 3, "Мяу")
a2 = Animal("Бобік", "пес", 5, "Гав")

a1.make_sound()
a2.make_sound()
