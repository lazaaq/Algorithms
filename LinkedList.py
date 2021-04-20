class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self, data):
        dataBaru = Node(data)
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            dataBaru.next = self.head
            self.head = dataBaru

    def addTail(self, data):
        dataBaru = Node(data)
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            dataBaru.prev = self.tail
            self.tail.next = dataBaru
            self.tail = dataBaru

    def removeHead(self):
        if self.head != None:
            self.head = self.head.next
            self.head.prev = None

    def removeTail(self):
        if self.head != None:
            self.tail = self.tail.prev
            self.tail.next = None

    def size(self):
        temp = self.head
        count_ = 0
        while temp != None:
            count_ += 1
            temp = temp.next
        return count_

    def addInsert(self, data, index):
        if index == 0:
            self.addHead(data)
        else:
            dataBaru = Node(data)
            temp = self.head
            inc = 0
            while inc != index:
                temp = temp.next
                inc += 1
            temp2 = temp.prev
            # menghubungkan antara temp2 dan dataBaru
            temp2.next = dataBaru
            dataBaru.prev = temp2
            # menghubungkan antara temp dan dataBaru
            dataBaru.next = temp
            temp.prev = dataBaru

    def display(self):
        p = self.head
        while p is not None:
            print(p.data, end=" ")
            p = p.next


linkedList = LinkedList()
linkedList.addHead("1")
linkedList.display()

print()
linkedList.addHead("2")
linkedList.display()

print()
linkedList.addTail("3")
linkedList.display()

print()
linkedList.addTail("4")
linkedList.display()

print()
linkedList.removeHead()
linkedList.display()

print()
linkedList.removeTail()
linkedList.display()

print()
linkedList.addInsert("5", 1)
linkedList.display()
