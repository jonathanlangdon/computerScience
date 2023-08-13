# vector addition using a class

from math import sin, cos, atan2, radians, degrees, sqrt


class Force:
    def __init__(self, magnitude, angle) -> None:
        self.magnitude = magnitude
        self.angle = angle

    def get_horizontal(self):
        return self.magnitude * cos(radians(self.angle))

    def get_vertical(self):
        return self.magnitude * sin(radians(self.angle))

    def get_angle(self, use_degrees=True):
        angle = atan2(self.get_vertical(), self.get_horizontal())
        return degrees(angle) if use_degrees else angle


def find_net_force(forces):
    horiz = 0
    vert = 0
    for force in forces:
        horiz += force.get_horizontal()
        vert += force.get_vertical()
    magnitude = sqrt(horiz**2 + vert**2)
    angle = atan2(vert, horiz)
    return Force(z(magnitude, 1), round(degrees(angle), 1))
