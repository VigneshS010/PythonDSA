class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTrees:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_Node = Node(value)
        temp = self.root

        if not self.root:
            self.root = new_Node
            return True
        while True:
            if temp.value == new_Node.value:
                return False

            if temp.value > new_Node.value:
                if temp.left == None:
                    temp.left = new_Node
                    return True
                temp = temp.left

            else:
                if temp.value < new_Node.value:
                    if temp.right == None:
                        temp.right = new_Node
                        return True
                    temp = temp.right


    def in_order_successor(self, value):
        curr = self.root
        successor = curr.value

        while True:
            if curr == None:
                return successor
            if curr.value > value:
                successor = curr.value
                curr = curr.left
            if curr.value < value:
                successor = curr.value
                curr = curr.right
            if curr.value == value:
                break
            return successor



my_tree = BTrees()
my_tree.insert(10)
my_tree.insert(8)   #     10
my_tree.insert(12)  #  8      12
my_tree.insert(7)   #7   9   11   13
my_tree.insert(9)
my_tree.insert(11)
my_tree.insert(13)

print(my_tree.in_order_successor(1))