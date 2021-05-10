class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data)
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        if self.head is None:
            print("The queue is empty!")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


Q = Queue()
Q.insert(1)
Q.insert(3)
Q.insert(2)
Q.insert(4)
Q.pop()
Q.insert(5)
Q.pop()
Q.display()
