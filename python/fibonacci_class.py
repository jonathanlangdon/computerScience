# create and update fibonacci number using a class


class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0

    def next_number(self):
        next = self.back1 + self.back2
        self.back2 = self.back1
        self.back1 = next
        return next
