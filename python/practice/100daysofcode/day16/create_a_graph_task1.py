#!/usr/bin/python
#Given a directed graph node (vertex), 
#return all the nodes' (vertices) key in an array by performing a breadth first search (BFS) traversal. 
#Assume that all nodes are reachable from the input node and the nodes' key is unique
"""
addEdge(0, 1, g);
		addEdge(0, 4, g);
		addEdge(1, 0, g);
		addEdge(1, 3, g);
		addEdge(1, 4, g);
		addEdge(2, 3, g);
		addEdge(2, 4, g);
		addEdge(3, 1, g);
		addEdge(3, 2, g);
		addEdge(4, 0, g);
		addEdge(4, 1, g);
		addEdge(4, 2, g);
  	System.out.print(BFS(0, g) + " ");
"""
#flist= []
#while flist < 0:
x = raw_input("Enter 4 lists as command separated : ") 
if len(x) <= 2  :
    print ("You must enter < 4 lists, you list is > 3")
else:
    cnt = 0 
    while cnt <= 3:
        x = raw_input("Enter 3 lists as command separated - %s : " % cnt)
        cnt +=1

#edge1 = [ 0, 1, 2 ]
#edge2 = [ 1, 3, 4 ]
#edge3 = [ 2, 4, 5 ]



