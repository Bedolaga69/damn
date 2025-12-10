# arr = [5, 2, 9, 1, 5, 6]

# сортировка списка (возвращает новый список)
# sorted_arr = sorted(arr)
# print(sorted_arr)

# сортировка списка на месте
# arr.sort()
# print(arr)
#
#
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# arr = [64, 34, 25, 12, 22, 11, 90]
# print(bubble_sort(arr))

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def sides(self):
        """Returns the lengths of three sides of the triangle"""
        a = self.point1.distance_to(self.point2)
        b = self.point2.distance_to(self.point3)
        c = self.point3.distance_to(self.point1)
        return a, b, c

    def perimeter(self):
        """Calculates the perimeter of the triangle"""
        a, b, c = self.sides()
        return a + b + c

    def area(self):
        """Calculates the area of the triangle using Heron's formula"""
        a, b, c = self.sides()
        p = self.perimeter() / 2  # semi-perimeter

        # Heron's formula: S = √(p(p-a)(p-b)(p-c))
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return area

    def move(self, dx, dy):
        """Moves the triangle by given distances along x and y axes"""
        self.point1.x += dx
        self.point1.y += dy
        self.point2.x += dx
        self.point2.y += dy
        self.point3.x += dx
        self.point3.y += dy

    def __str__(self):
        return f"Triangle: A({self.point1.x}, {self.point1.y}), " \
               f"B({self.point2.x}, {self.point2.y}), " \
               f"C({self.point3.x}, {self.point3.y})"


# Example usage
if __name__ == "__main__":
    # Create three points
    A = Point(0, 0)
    B = Point(4, 0)
    C = Point(0, 3)

    # Create a triangle
    triangle = Triangle(A, B, C)

    print(triangle)
    print(f"Perimeter: {triangle.perimeter():.2f}")
    print(f"Area: {triangle.area():.2f}")

    # Move the triangle
    triangle.move(2, 1)
    print("\nAfter moving:")
    print(triangle)
    print(f"Perimeter: {triangle.perimeter():.2f}")
    print(f"Area: {triangle.area():.2f}")