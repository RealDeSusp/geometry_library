# 15.09.2023 Mikhail Porokhnya

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError("radius cannot be negative")

    def calculate_area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            raise ValueError("Треугольник с такими сторонами невозможен")
        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            raise ValueError("Side lengths must be positive numbers")

    def calculate_area(self):
        # semi-perimeter of a triangle
        s = (self.side1 + self.side2 + self.side3) / 2

        # Heron's formula for calculating square
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    def is_right_triangle(self):
        # checking if a triangle is right-angled
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
