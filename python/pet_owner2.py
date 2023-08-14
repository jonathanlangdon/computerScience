# practice accessing nested class attributes


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


def get_pets_string(the_owner):
    pet_names = [f"{pet.name.first} {pet.name.last}" for pet in the_owner.pets]
    return f"{the_owner.name.first} {the_owner.name.last}'s pets are: {', '.join(pet_names)}"
