class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

r1 = Rectangle(6, 15)
r2 = Rectangle(32, 18)

print(r1.calculate_area())
print(r2.calculate_area())
