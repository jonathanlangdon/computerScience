# given sides of triangle, solve hypotenuse and angle

import math


def solve_right_triangle(opposite, adjacent, use_degrees=False):
    hypo = math.sqrt(opposite**2 + adjacent**2)
    angle = math.atan(opposite / adjacent)
    if use_degrees:
        angle = math.degrees(angle)
    return hypo, angle
