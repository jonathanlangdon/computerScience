# practice creating a class and its attributes, method


class Pokemon:
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power

    def would_defeat(self, other_pokemon):
        return self.power > other_pokemon.power
