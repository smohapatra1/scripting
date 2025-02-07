#   https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/


from collections import defaultdict

graph = defaultdict(list)
def addEdge(graph, u, v ):
    graph[u].append(v)
def GenerateEdges(graph):
    edges = []
    for node in graph:
        for neighbor in graph[node]:
            edges.append((node, neighbor))
    return edges

addEdge(graph,'a','c') 
addEdge(graph,'b','c') 
addEdge(graph,'b','e') 
addEdge(graph,'c','d') 
addEdge(graph,'c','e') 
addEdge(graph,'c','a') 
addEdge(graph,'c','b') 
addEdge(graph,'e','b') 
addEdge(graph,'d','c') 
addEdge(graph,'e','c') 
print (GenerateEdges(graph))