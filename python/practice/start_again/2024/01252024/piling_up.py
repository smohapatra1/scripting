# #   https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=false


# There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .

# When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.

# Example

# Result: No

# After choosing the rightmost element, , choose the leftmost element, . After than, the choices are  and . These are both larger than the top block of size .


# Result: Yes

# Choose blocks from right to left in order to successfully stack the blocks.

# Input Format

# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

# Constraints




# Output Format

# For each test case, output a single line containing either Yes or No.

# Sample Input

# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
# Sample Output

# Yes
# No
# Explanation

# In the first test case, pick in this order: left - , right - , left - , right - , left - , right - .
# In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either  or .

from collections import deque

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        num=int(input().strip())
        deq=deque(list(map(int, input().strip().split(' '))))
        prev = max(deq[0], deq[-1])
        while deq:
            if prev > deq[0] and prev >=deq[-1]:
                if deq[0] >=deq [-1]:
                    prev=deq.popleft()
                else:
                    prev = deq.pop()
            else:
                break
        if len(deq) == 0:
            print ('Yes')
        else:
            print ('No')