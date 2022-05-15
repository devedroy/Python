
from collections import defaultdict

#https://www.geeksforgeeks.org/detect-cycle-in-a-graph/?msclkid=714f3d11d07811ecaa713ab57ea44c03

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour] == True:
                return True
        
        recStack[v] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)

        for node in range(1, self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack):
                    return True

        return False

g = Graph(5)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)

if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")