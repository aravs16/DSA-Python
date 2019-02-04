class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def print_queue(self):
        print(self.items)



q = Queue()
q.enqueue("Aravind")
q.enqueue("Singirikonda")
q.print_queue()
q.dequeue()
q.print_queue()
