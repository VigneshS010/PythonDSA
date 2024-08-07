class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenght = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

    def print_node(self):
        if self.head == None:
            return False
        curr = self.head
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()
        print(self.lenght)

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght+=1

    def insert(self, value, index):
        if index > self.lenght:
            return False
        else:
            new_node = Node(value)
            temp = self.head
            for _ in range(index-1):
                temp=temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.lenght += 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp= after










myClass = LL()

myClass.append(1)
myClass.append(10)
myClass.append(100)

myClass.prepend(0)
myClass.prepend(00)
myClass.prepend(000)

myClass.insert(200 ,3)

myClass.print_node()

myClass.reverse()

myClass.print_node()