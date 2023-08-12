# practice creating classes and instances of the class, now with positional arguments


class Number:
    def __init__(self, value, even):
        self.value = value
        self.even = even


number_instance = Number(101, False)

print(number_instance.value + number_instance.even)
