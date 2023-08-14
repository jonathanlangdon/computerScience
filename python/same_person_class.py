# practice using a class with a function


class Person:
    def __init__(self, name, age, GTID):
        self.set_name(name)
        self.set_age(age)
        self.set_GTID(GTID)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_GTID(self, GTID):
        self.GTID = GTID

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_GTID(self):
        return self.GTID


def same_person(inst1, inst2):
    return inst1.GTID == inst2.GTID
