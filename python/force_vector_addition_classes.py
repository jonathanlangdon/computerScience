# vector addition using a class

from math import sin, cos, atan2, radians, degrees


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
