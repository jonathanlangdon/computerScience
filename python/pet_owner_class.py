# practice accessing class attributes


class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last


class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []


def get_owner_string(a_pet):
    return f"{a_pet.name.first} {a_pet.name.last}'s owner is {a_pet.owner.name.first} {a_pet.owner.name.last}."
