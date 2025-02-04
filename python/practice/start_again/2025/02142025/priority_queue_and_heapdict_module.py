#   https://www.geeksforgeeks.org/priority-queue-using-queue-and-heapdict-module-in-python/

from queue import PriorityQueue 

q = PriorityQueue()
q.put((2, 'g')) 
q.put((3, 'e')) 
q.put((4, 'k')) 
q.put((5, 's')) 
q.put((1, 'e')) 
print (q.get())
print (q.get())
print('Items in queue :', q.qsize()) 
print('Is queue empty :', q.empty()) 
print('Is queue full :', q.full())