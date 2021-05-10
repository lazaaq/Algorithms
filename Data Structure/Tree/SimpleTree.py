from math import *


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.hasChild = 0
        self.height = -1

    # untuk insertion kita akan insert node ke level height terdekat,
    # sehingga height dari tree keseluruhan adalah minimum
    def insert(self, data):
        if self.root == None:
            newNode = Node(data)
            self.root = newNode
            self.root.left = Tree()
            self.root.right = Tree()
        else:
            if self.root.left.hasChild > self.root.right.hasChild:
                self.root.right.insert(data)  # masukkan ke anak right
            elif self.root.left.hasChild < self.root.right.hasChild:
                self.root.left.insert(data)  # masukkan ke anak left
            else:  # kalo rights dan left sama aja
                self.root.left.insert(data)  # masukkan ke anak left aja

        self.height = max(self.root.left.height,
                          self.root.right.height) + 1  # update the height
        self.hasChild += 1  # update the hasChild

    # def delete(self, data):
    #     if self.root is None:
    #         print("Tree kosong!")
    #         return
    #     elif self.height == 0:
    #         if self.root.data == data:
    #             self.root = None
    #         else:
    #             print("data tidak ditemukan!")
    #         return
    #     deepest_node = self.getTheDeepestNode()
    #     node_delete = self.getSpecifiedNode(data)
    #     if node_delete == None:
    #         print("data tidak ditemukan!")
    #         return
    #     else:
    #         if deepest_node.right.root is None:
    #             node_delete.data = deepest_node.left.root.data
    #             deepest_node.left.root = None
    #         else:
    #             node_delete.data = deepest_node.right.root.data
    #             deepest_node.right.root = None

    # def getSpecifiedNode(self, data):
    #     if self.root is not None:
    #         if self.root.data == data:
    #             return self.root
    #         kiri = self.root.left.getSpecifiedNode(data)
    #         kanan = self.root.right.getSpecifiedNode(data)
    #         if kiri != -1:
    #             return kiri
    #         elif kanan != -1:
    #             return kanan
    #         else:
    #             return -1
    #     else:
    #         return -1

    # def getTheDeepestNode(self):
    #     if self.root is None:
    #         return None
    #     elif self.height == 1:
    #         return self.root
    #     elif self.root.left.hasChild > self.root.right.hasChild:
    #         return self.root.left.getTheDeepestNode()
    #     elif self.root.left.hasChild < self.root.right.hasChild:
    #         return self.root.right.getTheDeepestNode()
    #     elif self.root.left.hasChild == self.root.right.hasChild:
    #         return self.root.right.getTheDeepestNode()

    def preOrder(self):
        if self.root is not None:
            print(self.root.data, end=' ')
            self.root.left.preOrder()
            self.root.right.preOrder()

    def inOrder(self):
        if self.root is not None:
            self.root.left.inOrder()
            print(self.root.data, end=' ')
            self.root.right.inOrder()

    def postOrder(self):
        if self.root is not None:
            self.root.left.postOrder()
            self.root.right.postOrder()
            print(self.root.data, end=' ')


pohon = Tree()
pohon.insert(5)
pohon.insert(6)
pohon.insert(4)
pohon.insert(1)
pohon.insert(7)
pohon.insert(8)
pohon.insert(9)
pohon.insert(10)

# pohon.delete(4)
# pohon.delete(6)

print("preOrder")
pohon.preOrder()
print("\ninOrder")
pohon.inOrder()
print("\npostOrder")
pohon.postOrder()
