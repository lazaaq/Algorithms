class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # banyaknya vertices
        # akan berisi kumpulan head dari linked list
        self.graph = [None for i in range(self.V)]

    def addEdge(self, src, dest):  # source dan destination (tipe data int)
        # update linked list source
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # update linked list destination
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def display(self):
        for i in range(self.V):
            print("Adjacency list of data {}\n head({})".format(i, i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")


# driver code
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.addEdge(0, 1)
    graph.addEdge(0, 4)
    graph.addEdge(1, 2)
    graph.addEdge(1, 3)
    graph.addEdge(1, 4)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)

    graph.display()

'''
semua node berupa linked list
untuk menambah edge, maka kita ubah konfigurasi dari kedua node/linked list.
'''
