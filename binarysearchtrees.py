__author__ = 'mc'

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print self.data
        if self.right is not None:
            self.right.print_tree()


root = Node(8)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

root.print_tree()