# take an variable amount of forces and vector sum them


from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt


def find_net_force(forces):
    horiz = 0
    vert = 0
    for [magnitude, angle] in forces:
        horiz += magnitude * cos(radians(angle))
        vert += magnitude * sin(radians(angle))
    magnitude = sqrt(horiz**2 + vert**2)
    angle = atan2(vert, horiz)
    return (round(magnitude, 1), round(degrees(angle), 1))
