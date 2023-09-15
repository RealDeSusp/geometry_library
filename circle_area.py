# 15.09.2023 Mikhail Porokhnya

import math


def circle_area(radius):
    """
    Calculates the area of a circle by radius

    :param radius: Circle radius.
    :return: Square of a circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2
