# 15.09.2023 Mikhail Porokhnya

import unittest
from calcularing_area import Circle, Triangle


class TestCircle(unittest.TestCase):
    def test_calculate_area_positive_radius(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), 78.54, places=2)  # checking that the area is close to 78.54

    def test_calculate_area_negative_radius(self):
        with self.assertRaises(ValueError):
            circle = Circle(-2)


class TestTriangle(unittest.TestCase):
    def test_calculate_area_valid_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.calculate_area(), 6.0, places=2)  # checking that the area is close to 6.0

    def test_calculate_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(1, 1, 3)  # impossible triangle

    def test_is_right_triangle_true(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

    def test_is_right_triangle_false(self):
        triangle = Triangle(5, 6, 7)
        self.assertFalse(triangle.is_right_triangle())


if __name__ == '__main__':
    unittest.main()
