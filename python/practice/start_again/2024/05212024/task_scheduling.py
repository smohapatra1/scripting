# #    https://www.hackerrank.com/challenges/task-scheduling/problem?isFullScreen=true


# You have a long list of tasks that you need to do today. To accomplish task  you need  minutes, and the deadline for this task is . You need not complete a task at a stretch. You can complete a part of it, switch to another task, and then switch back.

# You've realized that it might not be possible to complete all the tasks by their deadline. So you decide to do them in such a manner that the maximum amount by which a task's completion time overshoots its deadline is minimized.

# Input Format

# The first line contains the number of tasks, . Each of the next  lines contains two integers,  and .

# Constraints




# Output Format

# Output  lines. The  line contains the value of the maximum amount by which a task's completion time overshoots its deadline, when the first  tasks on your list are scheduled optimally. See the sample input for clarification.

# Sample Input

# 5
# 2 2
# 1 1
# 4 3
# 10 1
# 2 1
# Sample Output

# 0  
# 1  
# 2  
# 2  
# 3
# Explanation

# The first task alone can be completed in 2 minutes, and so you won't overshoot the deadline. 

# With the first two tasks, the optimal schedule can be:
# time 1: task 2
# time 2: task 1 
# time 3: task 1

# We've overshot task 1 by 1 minute, hence returning 1. 

# With the first three tasks, the optimal schedule can be:
# time 1 : task 2
# time 2 : task 1
# time 3 : task 3
# time 4 : task 1
# time 5 : task 3
# time 6 : task 3

# Task 1 has a deadline 2, and it finishes at time 4. So it exceeds its deadline by 2.
# Task 2 has a deadline 1, and it finishes at time 1. So it exceeds its deadline by 0.
# Task 3 has a deadline 4, and it finishes at time 6. So it exceeds its deadline by 2.

# Thus, the maximum time by which you overshoot a deadline is 2. No schedule can do better than this.

# Similar calculation can be done for the case containing 5 tasks.



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taskScheduling' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER m
#


class tree:
    __slots__ = ("left", "right", "free", "size")
    def __init__(self, size = 2):
        if size == 0:
            return None
        if size > 1:
            half = size // 2
            self.left = tree(size - half)
            self.right = tree(half)
        else:
            self.left = self.right = None
        self.free = size
        self.size = size

    def resize(self, n):
        while self.size < n:
            t = tree(0)
            t.left = self
            t.right = tree(self.size)
            t.free = t.left.size + t.right.size
            t.size = self.size * 2
            self = t
        return self

    def recfill(self, dur, end):
        if dur == 0:
            return 0
        if self.free == 0:
            return 0 
        if (self.size <= dur and dur <= end) or self.size == 1:
            r = self.free
            self.free = 0
            return r
        r = 0
        if self.left.size < end:
            r += self.right.recfill(dur, end - self.left.size)
        r += self.left.recfill(dur - r, end)
        self.free -= r
        return r

t = tree()
r = 0
nlines = int(sys.stdin.readline().strip())
for i in range(nlines):
    two_strings = sys.stdin.readline().strip().split(" ")
    end, dur = (int(i) for i in two_strings)
    t = t.resize(end)
    b = t.recfill(dur, end)
    r = r + dur - b
    print(r)
    

# def taskScheduling(d, m):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         d = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         result = taskScheduling(d, m)

#         fptr.write(str(result) + '\n')

#     fptr.close()
