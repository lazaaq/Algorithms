from collections import defaultdict


class GraphBerarah:
    def __init__(self):
        self.graph = defaultdict(list)

    # menambahkan edge pada graf
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # fungsi yang akan dipanggil oleh fungsi DFS
    def DFSUtil(self, v, visited):  # visited = set{}, v = vertices
        # vertices yang belum dikunjungi akan dimasukkan kedalam set visited
        visited.add(v)
        print(v, end=' ')

        # untuk semua tetangga dari suatu vertices
        for neighbour in self.graph[v]:
            if neighbour not in visited:  # kalo belum dikunjungi, maka lakukan rekursi
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

    def printGraph(self):
        print(self.graph)


class GraphTidakBerarah:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

    def printGraph(self):
        print(self.graph)


if __name__ == '__main__':
    g = GraphBerarah()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from vertex 0")
    g.DFS(0)
    print("\nFollowing is DFS from vertex 1")
    g.DFS(1)
    print("\nFollowing is DFS from vertex 2")
    g.DFS(2)
    print("\nFollowing is DFS from vertex 3")
    g.DFS(3)
    g.printGraph()

    p = GraphTidakBerarah()
    p.addEdge(0, 1)
    p.addEdge(0, 2)
    p.addEdge(1, 2)
    p.addEdge(2, 0)
    p.addEdge(2, 3)
    p.addEdge(3, 3)

    print("Following is DFS from vertex 0")
    p.DFS(0)
    print("\nFollowing is DFS from vertex 1")
    p.DFS(1)
    print("\nFollowing is DFS from vertex 2")
    p.DFS(2)
    print("\nFollowing is DFS from vertex 3")
    p.DFS(3)
    print()
    p.printGraph()
