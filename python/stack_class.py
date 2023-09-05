# practice creating a class with a constructor (and creating my own pop method)


class Stack:
    def __init__(self):
        self.stack_list = []

    def stack_push(self, item):
        self.stack_list.append(item)

    def stack_pop(self):
        popped_item = self.stack_list[len(self.stack_list) - 1]
        self.stack_list = self.stack_list[:-1]
        return popped_item
