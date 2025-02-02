#   https://www.geeksforgeeks.org/python-library-for-linked-list/

import collections
ll = collections.deque()
ll.append('first')
ll.append('second')
ll.append('third')
print ("Elements in the ll : ", ll)
ll.insert(1, 'fourth')
print ("Elements in the ll : ", ll)
ll.pop()
print ("Elements in the ll : ", ll)
ll.remove('fourth')
print ("Elements in the ll : ", ll)
