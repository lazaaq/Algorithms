import math


class Graph:
    def __init__(self):
        self.matriks = []  # array 2d berisi edge antar vertices
        self.matriksName = []  # array 1d berisi tentang nama nama tiap vertices
        self.vertices = 0  # banyak vertices

    def addVertices(self, name):
        for i in range(self.vertices):
            self.matriks[i].append(math.inf)  # math.inf bernilai tak terhingga
        self.vertices += 1
        # jika menambahkan vertices, maka self.matriks akan berubah ukurannya.
        self.matriks.append([math.inf for i in range(self.vertices)])
        self.matriksName.append(name)

    def addEdge(self, src, dest, weight=1):
        # mencari index
        try:
            src_idx = self.matriksName.index(src)
        except:
            print(f"there is no {src} vertices")
            return
        try:
            dest_idx = self.matriksName.index(dest)
        except:
            print(f"there is no {dest} vertices")
            return

        # mengganti nilai weight antar edge
        self.matriks[src_idx][dest_idx] = weight
        self.matriks[dest_idx][src_idx] = weight

    def display(self):
        for i in self.matriks:
            for j in i:
                print(j, end=' ')
            print()


# driver code
if __name__ == '__main__':
    graf = Graph()
    graf.addVertices("A")
    graf.addVertices("B")
    graf.addVertices("C")
    graf.addVertices("D")
    graf.addEdge("A", "B", 2)
    graf.addEdge("A", "C", 3)
    graf.addEdge("A", "D", 1)
    graf.addEdge("B", "C", 4)
    graf.addEdge("C", "D", 2)
    graf.addVertices("E")
    graf.display()

'''
program ini berisi tentang implementasi graph menggunakan adjacency matriks
'''
