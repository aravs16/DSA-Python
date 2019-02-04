class Node:

    def __init__(self):
        self.value = data

    def get_value(self):
        return self.value

class BinaryTree:

    def __init__(self, node):
        self.root = node
        self.left = None
        self.right = None

    def insert_left(self, node):
        if self.left == None:
            self.left = BinaryTree(node)
        else:
            temp = self.left
            new = BinaryTree(node)
            new.left = temp
            self.left = new

    def insert_right(self, node):
        if self.right == None:
            self.right = BinaryTree(node)
        else:
            temp = self.right
            new = BinaryTree(node)
            self.right = new.right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root_val(self,node):
        self.root = node

    def get_root_val(self):
        return self.root


def in_order(tree):
    if tree:
        in_order(tree.get_left())
        print(tree.get_root_val())
        in_order(tree.get_right())


bt = BinaryTree(1)
bt.insert_left(2)
bt.insert_right(3)

bt2 = bt.get_left()
bt3 = bt.get_right()

bt2.insert_left(4)
bt2.insert_right(5)

bt3.insert_left(6)
bt3.insert_right(7)

in_order(bt)