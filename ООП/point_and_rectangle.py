import math
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx * dx + dy * dy)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Rectangle:
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"{self.x}, {self.y}, {self.height}, {self.width}"


a = Point(1, 2)
b = Point(4, 6)
print(a.distance_to(b))
print(a)
a = Rectangle(1, 2, 1, 2)
b = Rectangle(4, 6, 4, 6)
print(a.perimeter())
print(a.area())
print(b.perimeter())
print(b.area())
