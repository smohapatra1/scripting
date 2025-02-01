#   https://www.geeksforgeeks.org/dumping-queue-into-list-or-array-in-python/

from collections import deque

q = deque()
q.append('a')
q.append('b')
q.append('c')
print ("Initial queue")
print (q,"\n")
print (type(q))