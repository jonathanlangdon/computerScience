# practice creating instances of a class


class Person:
    def __init__(self, name, age, father=None, mother=None):
        self.name = name
        self.age = age
        self.father = father
        self.mother = mother


mr_b = Person("Mr. Burdell", 53)
mrs_b = Person("Mrs. Burdell", 53)
george_p = Person("George P. Burdell", 25, mr_b, mrs_b)
