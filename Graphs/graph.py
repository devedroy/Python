'''
In a graph:
V = [0, 1, 2, 3]
E = [(0, 1), (0, 2), (0, 3), (1, 2)]
G = (V, E)

Adjacency Matrix:
[
    [0, 1, 1, 1],
    [1, 0, 1, o],
    [1, 1, 0, 0],
    [1, 0, 0, 0]
    ]

Adjacency List:
0 -> 1 -> 2 -> 3
1 -> 0 -> 2
2 -> 0 -> 1
3 -> 0
'''

class Graph:
    def __init__(self, size) -> None:
        self.adjMatrix = []
        self.size = size
        
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        
    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            for val in row:
                print('{:4}'.format(val), end="")
            print()

    def add_edge(self, v1, v2):
        if v1 == v2:
            print("same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1

    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0    



graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.remove_edge(2, 3)
graph.print_matrix()