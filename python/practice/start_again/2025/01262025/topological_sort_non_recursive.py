#   https://www.geeksforgeeks.org/python-program-for-topological-sorting/

from collections import defaultdict

class Graph:
    def __init__ (self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    def addEdge(self, u, v ):
        self.graph[u].append(v)
    def Neighbor_Gen(self, v ):
        for k in self.graph[v]:
            yield k 
    def NonRecursiveTopologicalSortUtils(self, v, visited, stack):
        working_stack = [ (v, self.Neighbor_Gen(v))]
        while working_stack:
            v, gen = working_stack.pop()
            visited[v] = True
        for next_neighbor in gen:
            if not visited[next_neighbor]:
                working_stack.append((v, gen))
                working_stack.append((next_neighbor, self.Neighbor_Gen(next_neighbor)))
                break
        else:
            stack.append(v)
    def NonRecursiveTopologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if not (visited[i]):
                self.NonRecursiveTopologicalSortUtils(i, visited, stack)
        stack.reverse()
        print (stack)

g= Graph(6)
g.addEdge(5, 2);
g.addEdge(5, 0);
g.addEdge(4, 0);
g.addEdge(4, 1);
g.addEdge(2, 3);
g.addEdge(3, 1);
 
print("The following is a Topological Sort of the given graph")
g.NonRecursiveTopologicalSort()

