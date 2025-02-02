#   https://www.geeksforgeeks.org/dumping-queue-into-list-or-array-in-python/

from queue import Queue

que = Queue()
que.put('1')
que.put('2')
que.put('3')
que.put('4')
que.put('5')
print ("Print Initial Queue")
print (que.queue)
li = list(que.queue)
print ("\n Converted to list : ", li)   