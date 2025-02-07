#   https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/


def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpath = find_all_path(graph, node, end, path)
        for new in newpath:
            paths.append(new)
    return paths  



graph ={ 
'a':['c'], 
'b':['d'], 
'c':['e'], 
'd':['a', 'd'], 
'e':['b', 'c'] 
} 

print (find_all_path(graph, 'd', 'c'))