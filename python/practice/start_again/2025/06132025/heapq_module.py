#   https://www.geeksforgeeks.org/built-in-modules-in-python/

import heapq

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(numbers)
heapq.heappush(numbers, 7)
print (numbers)
heapq.heappop(numbers)
print (numbers)
heapq.heappushpop(numbers, 8 )
print (numbers)
heapq.nlargest(3, numbers)
print (numbers)
heapq.nsmallest(3, numbers)
print (numbers)