# masing masing data berupa objek node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # menambahkan data di depan head
    def addHead(self, data):
        dataBaru = Node(data)
        self.size += 1
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            dataBaru.next = self.head
            self.head.prev = dataBaru
            self.head = dataBaru

    # menambahkan data di belakang tail
    def addTail(self, data):
        dataBaru = Node(data)
        self.size += 1
        if self.head == None:
            self.head = dataBaru
            self.tail = dataBaru
        else:
            dataBaru.prev = self.tail
            self.tail.next = dataBaru
            self.tail = dataBaru

    # menghapus data head
    def removeHead(self):
        if self.head != None:
            self.size -= 1
            self.head = self.head.next
            self.head.prev = None

    # menghapus data tail
    def removeTail(self):
        if self.head != None:
            self.size -= 1
            self.tail = self.tail.prev
            self.tail.next = None

    # menambahkan data pada index tertentu
    def addInsert(self, data, index):
        if index == 0:
            self.addHead(data)
        elif index == self.size - 1:
            self.addTail(data)
        elif index < self.size:
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
        else:
            print("index out of range")
            return
        self.size += 1

    # menghapus data dengan nilai tertentu. jika tidak ditemukan, maka akan di print "data doesnt exist"
    def removeData(self, data):
        temp = self.head
        found = True
        while temp.data is not data:
            temp = temp.next
            if temp is None:
                found = False
                break
        if not found:
            print("the data doesn't exist")
        else:
            temp_prev = temp.prev
            temp_next = temp.next
            if temp_next is None:
                temp_prev.next = None
            elif temp_prev is None:
                temp_next.prev = None
            else:
                temp_prev.next = temp_next
                temp_next.prev = temp_prev
            self.size -= 1

    # menghapus data pada index tertentu
    def removeDataAtIndex(self, idx):
        inc = 0
        temp = self.head
        if idx >= self.size:
            print("index out of range")
            return
        if idx == self.size-1:
            self.removeTail()
            return
        if idx == 0:
            self.removeHead()
            return
        while inc < idx:
            temp = temp.next
            inc += 1
        temp_prev = temp.prev
        temp_next = temp.next
        temp_prev.next = temp_next
        temp_next.prev = temp_prev
        self.size -= 1

    # mencari data ada di index keberapa
    def search(self, data):
        temp = self.head
        idx = 0
        while temp:
            if temp.data == data:
                return idx
            temp = temp.next
            idx += 1
        return -1

    # menghapus semua data
    def clear(self):
        self.__init__()

    # meng-copy data yang ada pada linked list
    def copy(self):
        l = []
        temp = self.head
        while temp:
            l.append(temp.data)
            temp = temp.next
        return l

    # menghitung kemunculan data
    def count(self, data):
        cnt = 0
        temp = self.head
        while temp:
            if temp.data == data:
                cnt += 1
            temp = temp.next
        return cnt

    # reverse urutan dalam linked list
    def reverse(self):
        length = self.size // 2
        inc = 0
        forward = self.head
        backward = self.tail
        while inc < length and forward and backward:
            forward.data, backward.data = backward.data, forward.data
            forward = forward.next
            backward = backward.prev
            inc += 1

    # menggabungkan data data pada linked list menggunakan suatu delimiter
    def join(self, delimiter):
        l = self.copy()
        try:
            l = list(map(str, l))
            return delimiter.join(l)
        except:
            print("delimiter harus berupa string!")

    # sorting data pada linked list
    # def sort(self):
    #     temp = self.head
    #     for i in range(self.size):
    #         buff = temp
    #         while buff.prev and buff.data < buff.prev.data:
    #             temp_buff_data = buff.data
    #             buff.data = buff.prev.data
    #             buff.prev.data = temp_buff_data

    #             buff.prev = buff.prev.prev
    #             buff.next = buff.prev
    #         temp = temp.next

    # menampilkan data linked list di terminal
    def display(self):
        p = self.head
        while p is not None:
            print(p.data, end=" ")
            p = p.next


# buat objek linked list dulu
linkedList = LinkedList()

# memasukkan data
linkedList.addHead(1)
linkedList.display()

print()
linkedList.addHead(2)
linkedList.display()

print()
linkedList.addHead(9)
linkedList.display()

print()
linkedList.addTail(3)
linkedList.display()

print()
linkedList.addTail(4)
linkedList.display()

print()
linkedList.addInsert(5, 1)
linkedList.display()


# another method
print()
print(linkedList.search(2))

print(linkedList.copy())

print(linkedList.count(4))

print(linkedList.join("-"))

linkedList.reverse()
linkedList.display()

# print()
# linkedList.sort()
# linkedList.display()


# removing data
print()
linkedList.removeHead()
linkedList.display()

print()
linkedList.removeTail()
linkedList.display()


print()
linkedList.removeData(5)
linkedList.display()

print()
linkedList.removeDataAtIndex(0)
linkedList.display()

print()
linkedList.clear()
linkedList.display()
