class Node:
    def __init__(self, angka=None):
        self.angka = angka
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, angka):
        if self.root is None:
            nodeBaru = Node(angka)
            self.root = nodeBaru
            self.root.left = BST()
            self.root.right = BST()
        else:
            if self.root.angka > angka:
                self.root.left.insert(angka)
            else:
                self.root.right.insert(angka)

    def preOrder(self):
        if self.root is not None:
            print(self.root.angka, end=" ")
            self.root.left.preOrder()
            self.root.right.preOrder()

    def inOrder(self):
        if self.root is not None:
            self.root.left.inOrder()
            print(self.root.angka, end=" ")
            self.root.right.inOrder()

    def postOrder(self):
        if self.root is not None:
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.angka, end=" ")

    def getTinggi(self):
        if self.root is None:
            return -1
        else:
            return 1 + max(self.root.left.getTinggi(), self.root.right.getTinggi())

    def getCountNode(self):  # menghitung ada berapa node
        if self.root is None:
            return 0
        else:
            return 1 + self.root.left.getCountNode() + self.root.right.getCountNode()

    def getSumNode(self):  # menjumlahkan semua nilai node
        if self.root is None:
            return 0
        else:
            return self.root.angka + self.root.left.getSumNode() + self.root.right.getSumNode()

    def getAverageNode(self):
        return self.getSumNode() / self.getCountNode()

    def getCountLeaf(self):
        if self.root is None:
            return 0
        else:
            if self.getTinggi() == 0:
                return 1
            else:
                return self.root.left.getCountLeaf() + self.root.right.getCountLeaf()

    def getSumLeaf(self):
        # print("akses")
        if self.root is None:
            return 0
        else:
            if self.getTinggi() == 0:
                return self.root.angka
            else:
                return self.root.left.getSumLeaf() + self.root.right.getSumLeaf()

    def getMaxNode(self):
        if self.root is not None:
            if self.root.right.root is not None:
                return self.root.right.getMaxNode()
            else:
                return self.root.angka

    def getMinNode(self):
        if self.root is not None:
            if self.root.left.root is not None:
                return self.root.left.getMinNode()
            else:
                return self.root.angka

    def getCountNodeDengan1Anak(self):
        if self.root is None:
            return 0
        else:
            # kalo kanan nya ada anak, tapi kirinya gaada
            if self.root.right.root is not None and self.root.left.root is None:
                return 1 + self.root.right.getCountNodeDengan1Anak()
            # kalo kiri nya ada anak, tapi kanannya gaada
            elif self.root.left.root is not None and self.root.right.root is None:
                return 1 + self.root.left.getCountNodeDengan1Anak()
            else:
                return self.root.right.getCountNodeDengan1Anak() + self.root.left.getCountNodeDengan1Anak()

    def getCountNodeDengan2Anak(self):
        if self.root is None:
            return 0
        else:
            if self.root.right.root is not None and self.root.left.root is not None:
                return 1 + self.root.right.getCountNodeDengan2Anak() + self.root.left.getCountNodeDengan2Anak()
            else:
                return 0

    def getSumNodeDengan1Anak(self):
        if self.root is None:
            return 0
        else:
            # kalo kanan nya ada anak, tapi kirinya gaada
            if self.root.right.root is not None and self.root.left.root is None:
                return self.root.angka + self.root.right.getSumNodeDengan1Anak()
            # kalo kiri nya ada anak, tapi kanannya gaada
            elif self.root.left.root is not None and self.root.right.root is None:
                return self.root.angka + self.root.left.getSumNodeDengan1Anak()
            else:
                return self.root.right.getSumNodeDengan1Anak() + self.root.left.getSumNodeDengan1Anak()

    def getSumNodeDengan2Anak(self):
        if self.root is None:
            return 0
        else:
            if self.root.right.root is not None and self.root.left.root is not None:
                return self.root.angka + self.root.right.getSumNodeDengan2Anak() + self.root.left.getSumNodeDengan2Anak()
            else:
                return 0

    def getCountNodeGenap(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka % 2 == 0:
                return 1 + self.root.left.getCountNodeGenap() + self.root.right.getCountNodeGenap()
            else:
                return self.root.left.getCountNodeGenap() + self.root.right.getCountNodeGenap()

    def getCountNodeGanjil(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka % 2 == 1:
                return 1 + self.root.left.getCountNodeGenap() + self.root.right.getCountNodeGenap()
            else:
                return self.root.left.getCountNodeGenap() + self.root.right.getCountNodeGenap()

    def getSumNodeGenap(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka % 2 == 0:
                return self.root.angka + self.root.left.getSumNodeGenap() + self.root.right.getSumNodeGenap()
            else:
                return self.root.left.getSumNodeGenap() + self.root.right.getSumNodeGenap()

    def getSumNodeGanjil(self):
        if self.root is None:
            return 0
        else:
            if self.root.angka % 2 == 1:
                return self.root.angka + self.root.left.getSumNodeGanjil() + self.root.right.getSumNodeGanjil()
            else:
                return self.root.left.getSumNodeGanjil() + self.root.right.getSumNodeGanjil()


pohon = BST()
pohon.insert(4)
pohon.insert(2)
pohon.insert(5)
pohon.insert(3)
print("preOrder")
pohon.preOrder()
print("\ninOrder")
pohon.inOrder()
print("\npostOrder")
pohon.postOrder()

print("\ngetTinggi()")
print(pohon.getTinggi())

print("\ngetCountNode()")
print(pohon.getCountNode())

print("\ngetSumNode()")
print(pohon.getSumNode())

print("\ngetAverageNode()")
print(pohon.getAverageNode())

print("\ngetCountLeaf()")
print(pohon.getCountLeaf())

print("\ngetSumLeaf()")
print(pohon.getSumLeaf())

print("\ngetMaxNode()")
print(pohon.getMaxNode())

print("\ngetMinNode()")
print(pohon.getMinNode())

print("getCountNodeDengan1Anak()")
print(pohon.getCountNodeDengan1Anak())

print("getCountNodeDengan2Anak()")
print(pohon.getCountNodeDengan2Anak())

print("getSumNodeDengan1Anak()")
print(pohon.getSumNodeDengan1Anak())

print("getSumNodeDengan2Anak()")
print(pohon.getSumNodeDengan2Anak())

print("getCountNodeGenap()")
print(pohon.getCountNodeGenap())

print("getCountNodedGanjil()")
print(pohon.getCountNodeGanjil())

print("getSumNodeGenap()")
print(pohon.getSumNodeGenap())

print("getSumNodedGanjil()")
print(pohon.getSumNodeGanjil())
