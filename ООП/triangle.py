import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def distance(self, p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def sides(self):
        a = self.distance(self.point1, self.point2)  # AB
        b = self.distance(self.point2, self.point3)  # BC
        c = self.distance(self.point3, self.point1)  # CA
        return a, b, c

    def perimeter(self):
        a, b, c = self.sides()
        return a + b + c

    def area(self):
        a, b, c = self.sides()
        p = self.perimeter() / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def move(self, dx, dy):
        self.point1.x += dx
        self.point1.y += dy
        self.point2.x += dx
        self.point2.y += dy
        self.point3.x += dx
        self.point3.y += dy

    def __str__(self):
        return (f"Triangle: A({self.point1.x},{self.point1.y}), B({self.point2.x},{self.point2.y}),"
                f" C({self.point3.x},{self.point3.y})")


point1 = Point(0, 0)
point2 = Point(0, 3)
point3 = Point(4, 0)

triangle = Triangle(point1, point2, point3)
print(triangle)
print(f"Area: {triangle.area()}")