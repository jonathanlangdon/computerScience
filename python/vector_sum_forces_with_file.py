# take forces from a file and vector sum them


from math import sin, cos, atan2, radians, degrees, sqrt


def find_net_force_from_file(filename):
    file = open(filename, "r")
    horiz = 0
    vert = 0
    for line in file:
        [magnitude, angle] = line.split(" ")
        horiz += int(magnitude) * cos(radians(int(angle)))
        vert += int(magnitude) * sin(radians(int(angle)))
    file.close()
    magnitude = sqrt(horiz**2 + vert**2)
    angle = atan2(vert, horiz)
    return (round(magnitude, 1), round(degrees(angle), 1))
