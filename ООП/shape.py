from math import pi
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass


# класс прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self): return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self): return self.radius * self.radius * pi


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self): return self.side * self.side


rect = Rectangle(30, 50)
print("Rectangle area:", rect.area())

circle = Circle(10)
print(f"circle area: {circle.area()}")

square = Square(9)
print(f"square area: {square.area()}")





class Shape(abc.ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abc.abstractmethod
    def area(self): pass  # абстрактный метод

    def print_point(self):  # неабстрактный метод
        print("X:", self.x, "\tY:", self.y)


# класс прямоугольника
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def area(self): return self.width * self.height


rect = Rectangle(10, 20, 100, 100)
rect.print_point()