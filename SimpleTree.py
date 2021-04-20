class Node:
    def __init__(self, data=None):
        self.data = data
        self.kiri = None
        self.kanan = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, angka):
        if self.root == None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.root.kiri = Tree()
            self.root.kanan = Tree()
        elif (self.root.data > angka):
            self.root.kiri.insert(angka)
        else:
            self.root.kanan.insert(angka)

    def preOrder(self):
        if self.root != None:
            print(self.root.data, end=' ')
            self.root.kiri.preOrder()
            self.root.kanan.preOrder()

    def inOrder(self):
        if self.root != None:
            self.root.kiri.inOrder()
            print(self.root.data, end=' ')
            self.root.kanan.inOrder()

    def postOrder(self):
        if self.root != None:
            self.root.kiri.postOrder()
            self.root.kanan.postOrder()
            print(self.root.data, end=' ')


pohon = Tree()
pohon.insert(5)
pohon.insert(6)
pohon.insert(4)
pohon.insert(1)
pohon.insert(7)
print("preOrder")
pohon.preOrder()
print("\ninOrder")
pohon.inOrder()
print("\npostOrder")
pohon.postOrder()
