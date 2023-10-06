# new class for a Queue function


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, new_item):
        self.queue.append(new_item)

    def dequeue(self):
        if self.queue == []:
            return None
        return self.queue.pop(0)


new_queue = Queue()
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
print(new_queue.dequeue())
print(new_queue.dequeue())
print(new_queue.dequeue())

# This will return 1, 2, 3 on separate lines
