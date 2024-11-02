#   https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/?ref=leftbar-rightbar

from collections import defaultdict

def Graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0] , edge[1]
        graph[a].append(b)
        graph[b].append(a)
    return graph

if __name__ == "__main__":
    edges = [
        ["A", "B"], ["A", "E"], 
        ["A", "C"], ["B", "D"],
        ["B", "E"], ["C", "F"],
        ["C", "G"], ["D", "E"]
    ]
    print ("Results after building the graph : ", Graph(edges))