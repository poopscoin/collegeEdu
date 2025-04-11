from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class AreaCalculator:
    def calculate(self, shape: Shape):
        return shape.area()

circle = Circle(3)
rect = Rectangle(4, 5)

calc = AreaCalculator()
print(calc.calculate(circle))
print(calc.calculate(rect))