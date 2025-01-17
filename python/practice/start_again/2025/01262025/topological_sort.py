#   https://www.geeksforgeeks.org/problems/topological-sort/1

#   https://www.geeksforgeeks.org/python-program-for-topological-sorting/

# Recursive 

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v ):
        self.graph[u].append(v)
    def topologicalSortUtils(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtils(i, visited, stack)
        stack.insert(0, v )
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtils(i, visited, stack)
        print (stack)

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print ("Following is a Topological Sort of the given graph")
g.topologicalSort()

