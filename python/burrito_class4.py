#  added total cost function to tally a bunch of burritos


def total_cost(burritos):
    cost = 0
    for burrito in burritos:
        cost += burrito.get_cost()
    return cost


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
        self.meat = Meat(meat)
        self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.set_extra_meat(extra_meat)
        self.set_guacamole(guacamole)
        self.set_cheese(cheese)
        self.set_pico(pico)
        self.set_corn(corn)

    def get_cost(self):
        base = 5.00
        base += 1.00 if self.meat.get_value() in ["chicken", "pork", "tofu"] else 0.00
        base += 1.50 if self.meat.get_value() == "steak" else 0.00
        base += 0 if self.meat.get_value() == False else 1.00 * self.extra_meat
        base += 0.75 * self.guacamole
        return round(base, 2)

    def set_meat(self, meat):
        self.meat.set_value(meat)

    def set_rice(self, rice):
        self.rice.set_value(rice)

    def set_beans(self, beans):
        self.beans.set_value(beans)

    def set_to_go(self, to_go):
        valid = [True, False]
        self.to_go = to_go if to_go in valid else False

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
        return self.meat.get_value()

    def get_to_go(self):
        return self.to_go

    def get_rice(self):
        return self.rice.get_value()

    def get_beans(self):
        return self.beans.get_value()

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


class Meat:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False


class Rice:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False


class Beans:
    def __init__(self, value=False):
        self.set_value(value)

    def get_value(self):
        return self.value

    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False


burrito_3 = Burrito(
    "tofu",
    True,
    "beefsteak",
    "black",
    extra_meat=True,
    guacamole=False,
    cheese=False,
    pico=False,
    corn=True,
)

print(burrito_3.get_cost())
burrito_3.set_meat(False)
print(burrito_3.get_cost())
