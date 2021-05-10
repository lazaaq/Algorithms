class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MinHeapTree:
    def __init__(self):
        self.root = None
        self.height = -1

    def insert(self, data):
        nodeBaru = Node(data)  # buat nodeBaru yang memiliki data
        if self.root is None:  # jika root belum berupa node
            self.root = nodeBaru
            self.root.left = MinHeapTree()  # anak kiri belum memiliki data
            self.root.right = MinHeapTree()  # anak kanan belum memiliki data
        # karena ini min heap, maka jika data yang akan dimasukkan lebih kecil dari data pada root, maka data pada root akan berubah menjadi data, kemudian data pada root akan di-insert kembali dengan asumsi data pada root sudah bernilai data.
        elif self.root.data > data:
            temp = self.root.data
            self.root.data = data
            self.insert(temp)
        elif self.root.left.root == None:  # jika anak kiri masih kosong
            self.root.left.insert(data)
        elif self.root.right.root == None:  # jika anak kanan masih kosong
            self.root.right.insert(data)
        elif self.root.left.root.data > self.root.right.root.data:  # jika anak kanan lebih kecil dari anak kiri
            self.root.right.insert(data)
        elif self.root.left.root.data < self.root.right.root.data:  # jika anak kiri lebih kecil dari anak kanan
            self.root.left.insert(data)

        # update height
        self.height = max(self.root.left.getHeight(),
                          self.root.right.getHeight()) + 1

    def getHeight(self):
        if self.root is None:
            return 0
        return max(self.root.left.getHeight(), self.root.right.getHeight()) + 1

    def preOrder(self):
        if self.root is not None:
            print(self.root.data, end=' ')
            self.root.left.preOrder()
            self.root.right.preOrder()

    def inOrder(self):
        if self.root is not None:
            self.root.left.inOrder()
            print(self.root.data, end=' ')
            self.root.right.postOrder()

    def postOrder(self):
        if self.root is not None:
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.data, end=' ')


minheaptree = MinHeapTree()
minheaptree.insert(1)
minheaptree.insert(2)
minheaptree.insert(3)
minheaptree.insert(4)
minheaptree.insert(5)
minheaptree.insert(6)
minheaptree.insert(7)
minheaptree.insert(8)
print("pre order : ")
minheaptree.preOrder()
print("\nin order : ")
minheaptree.inOrder()
print("\npost order : ")
minheaptree.postOrder()

'''
ada yang kurang sesuai dengan yang diharapkan.
tree tidak balance.
untuk balance, maka perlu membuat fungsi baru dalam class MinHeapTree.
'''
