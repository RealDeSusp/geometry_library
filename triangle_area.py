# 15.09.2023 Mikhail Porokhnya

def triangle_area(side1, side2, side3):
    """
    Calculates the area of a triangle based on three sides using Heron's formula.

    :param side1: First side length.
    :param side2: Second side length.
    :param side3: Third side length.
    :return: Square of a triangle.
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Side lengths must be positive numbers")

    # Semi-perimeter of a triangle
    s = (side1 + side2 + side3) / 2

    # Heron's formula for calculating square
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area
