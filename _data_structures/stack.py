class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        print(self.items)


s = Stack()
s.push('Aravind')
s.push('Singirikonda')
s.print_stack()
s.pop()
print(s.peek())
s.pop()
print(s.is_empty())
