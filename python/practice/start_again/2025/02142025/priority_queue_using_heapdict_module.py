#   https://www.geeksforgeeks.org/priority-queue-using-queue-and-heapdict-module-in-python/

import heapdict
h = heapdict.heapdict()
h['g'] = 2
h['e'] = 1
h['k'] = 3
h['s'] = 4
print ('list of key:value pairs in h: ', list(h.items()))
print('pair with lowest priority    : ', h.peekitem()) 
print('list of keys in h            : ', list(h.keys())) 
print('list of values in h          : ', list(h.values())) 
print('remove pair with lowest priority: ',h.popitem()) 
print('get value for key 5 in h        : ',h.get(5, 'Not found'))
h.clear()
print (list(h.items()))