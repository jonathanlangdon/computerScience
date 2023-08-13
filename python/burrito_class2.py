#  added cost method to the burrito class representing a burrito order


class Burrito:
    def __init__(
        self,
        meat,
        to_go,
        rice,
        beans,
        extra_meat=False,
        guacamole=False,
        cheese=False,
        pico=False,
        corn=False,
    ) -> None:
        self.set_meat(meat)
        self.set_to_go(to_go)
        self.set_rice(rice)
        self.set_beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_cost(self):
        base = 5.00
        base += 1.00 if self.meat in ["chicken", "pork", "tofu"] else 0.00
        base += 1.50 if self.meat == "steak" else 0.00
        base += 1.00 * self.extra_meat
        base += 0.75 * self.guacamole
        return round(base, 2)

    def set_meat(self, meat):
        valid = ["chicken", "pork", "steak", "tofu", False]
        self.meat = meat if meat in valid else False

    def set_to_go(self, to_go):
        valid = [True, False]
        self.to_go = to_go if to_go in valid else False

    def set_rice(self, rice):
        valid = ["brown", "white", False]
        self.rice = rice if rice in valid else False

    def set_beans(self, beans):
        valid = ["black", "pinto", False]
        self.beans = beans if beans in valid else False

    def set_extra_meat(self, extra_meat):
        valid = [True, False]
        self.extra_meat = extra_meat if extra_meat in valid else False

    def set_guacamole(self, guacamole):
        valid = [True, False]
        self.guacamole = guacamole if guacamole in valid else False

    def set_cheese(self, cheese):
        valid = [True, False]
        self.cheese = cheese if cheese in valid else False

    def set_pico(self, pico):
        valid = [True, False]
        self.pico = pico if pico in valid else False

    def set_corn(self, corn):
        valid = [True, False]
        self.corn = corn if corn in valid else False

    def get_meat(self):
        return self.meat

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice

    def get_beans(self):
        return self.beans

    def get_extra_meat(self):
        return self.extra_meat

    def get_guacamole(self):
        return self.guacamole

    def get_cheese(self):
        return self.cheese

    def get_pico(self):
        return self.pico

    def get_corn(self):
        return self.corn
