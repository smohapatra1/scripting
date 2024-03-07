# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-qheap1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four

# This question is designed to help you get a better understanding of basic heap operations.

# There are  types of query:

# " " - Add an element  to the heap.
# " " - Delete the element  from the heap.
# "" - Print the minimum of all the elements in the heap.
# NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.

# Input Format

# The first line contains the number of queries, .
# Each of the next  lines contains one of the  types of query.

# Constraints


# Output Format

# For each query of type , print the minimum value on a single line.

# Sample Input

# STDIN       Function
# -----       --------
# 5           Q = 5
# 1 4         insert 4
# 1 9         insert 9
# 3           print minimum
# 2 4         delete 4
# 3           print minimum
# Sample Output

# 4  
# 9 
# Explanation

# After the first  queries, the heap contains {}. Printing the minimum gives  as the output. Then, the  query deletes  from the heap, and the  query gives  as the output.



# Enter your code here. Read input from STDIN. Print output to STDOUT

import heapq
n=int(input())
h=[]
d=set()
for _ in range(n):
    v=list(map(int, input().split()))
    if v[0] == 1:
        heapq.heappush(h, v[1])
    elif v[0] == 2 :
        d.add(v[1])
    else:
        while h[0] in d:
            d.discard(h[0])
            heapq.heappop(h)
        print (h[0])