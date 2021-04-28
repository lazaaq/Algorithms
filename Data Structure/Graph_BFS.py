from collections import defaultdict


class GraphBerarah:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = [s]
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.graph[s]:
                if visited[i] == False:  # jika belum pernah dikunjungi
                    queue.append(i)
                    visited[i] = True  # ubah status jadi true


class GraphTidakBerarah:
    def __init__(self):
        self.graph = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def BFS(self, s):
        visited = [False] * (len(self.graph))
        queue = [s]
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=' ')
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':

    print("Graf Berarah : ")
    g = GraphBerarah()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is BFS starting from vertex 0")
    g.BFS(0)
    print("\nFollowing is BFS starting from vertex 1")
    g.BFS(1)
    print("\nFollowing is BFS starting from vertex 2")
    g.BFS(2)
    print("\nFollowing is BFS starting from vertex 3")
    g.BFS(3)

    print("\n\nGraf Tidak Berarah : ")
    p = GraphTidakBerarah()
    p.addEdge(0, 1)
    p.addEdge(0, 2)
    p.addEdge(1, 2)
    p.addEdge(2, 0)
    p.addEdge(2, 3)
    p.addEdge(3, 3)
    print("Following is BFS starting from vertex 0")
    p.BFS(0)
    print("\nFollowing is BFS starting from vertex 1")
    p.BFS(1)
    print("\nFollowing is BFS starting from vertex 2")
    p.BFS(2)
    print("\nFollowing is BFS starting from vertex 3")
    p.BFS(3)
