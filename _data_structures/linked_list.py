class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

    def set_data(self, data):
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def append_to_tail(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = node

    def print_ll(self):
        curr = self.head
        while True:
            print(curr.get_data())
            if curr.next == None:
                break
            else:
                curr = curr.next


ll = LinkedList()
ll.append_to_tail(5)
ll.append_to_tail(2)
ll.append_to_tail(3)
ll.append_to_tail(4)
ll.append_to_tail(0)
ll.print_ll()