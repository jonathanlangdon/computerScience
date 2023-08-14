#


class Thing:
    def __init__(self, mass, volume):
        self.mass = mass
        self.volume = volume
        self.weight = round(mass * 9.8, 1)
        self.density = round(mass / volume, 1)

    def __str__(self):
        return f"Mass: {self.mass} kg\nVolume: {self.volume} m^3\nWeight: {self.weight} N\nDensity: {self.density} kg/m^3"
