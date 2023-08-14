# making class Pet also add itself to the Owner class pet list


class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        owner.pets.append(self.name)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
