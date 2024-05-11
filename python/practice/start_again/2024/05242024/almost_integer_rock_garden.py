# #   https://www.hackerrank.com/challenges/almost-integer-rock-garden/problem?isFullScreen=true

# Victor is building a Japanese rock garden in his  square courtyard. He overlaid the courtyard with a Cartesian coordinate system so that any point  in the courtyard has coordinates  and . Victor wants to place  stones in the garden according to the following rules:

# The center of each stone is located at some point , where  and  are integers .
# The coordinates of all twelve stones are pairwise distinct.
# The Euclidean distance from the center of any stone to the origin is not an integer.
# The sum of Euclidean distances between all twelve points and the origin is an almost integer, meaning the absolute difference between this sum and an integer must be .
# Given the values of  and  for the first stone Victor placed in the garden, place the remaining  stones according to the requirements above. For each stone you place, print two space-separated integers on a new line describing the respective  and  coordinates of the stone's location.

# Input Format

# Two space-separated integers describing the respective values of  and  for the first stone's location.

# Constraints

# Output Format

# Print  lines, where each line contains two space-separated integers describing the respective values of  and  for a stone's location.

# Sample Input 0

# 7 11
# Sample Output 0

# 11 1
# -2 12
# 5 4
# 12 -3
# 10 3
# 9 6
# -12 -7
# 1 11
# -6 -6
# 12 -4
# 4 12
# Explanation 0

# The diagram below depicts the placement of each stone and maps its distance to the origin (note that red denotes the first stone placed by Victor and blue denotes the eleven remaining stones we placed):

# image

# Now, let's determine if the sum of these distances is an almost integer. First, we find the distance from the origin to the stone Victor placed at , which is . Next, we calculate the distances for the remaining stones we placed in the graph above:

# When we sum these eleven distances with the distance for the stone Victor placed, we get . The nearest integer to this number is , and the distance between this sum and the nearest integer is  (meaning it's an almost integer). Because this configuration satisfies all of Victor's rules for his rock garden, we print eleven lines of x y coordinates describing the locations of the stones we placed.


#!/bin/python3

import math
import os
import random
import re
import sys


solutions = []
solutions.append({(7, 11), (11, 1), (-2, 12), (5, 4), (12, -3), (10, 3), (9, 6), (-12, -7), (1,11),(-6,-6),(12,-4),(4,12)})
solutions.append({(-12, 8), (9, -6), (10, 5), (-5, 1), (3, 3), (3, 1), (-10, -2), (2, 1), (7, 5), (2, 2), (6, 5), (9, 7)})
solutions.append({(10, 5), (-2, 1), (3, 3), (3, 1), (10, 2), (-7, -5), (12, 8), (2, 2), (6, -5), (5, 1), (-9, 6), (9, 7)})
solutions.append({(10, 2), (-2, 2), (12, 6), (3, -1), (-11, 3), (-7, -5), (2, 2), (5, 1), (9, 6), (1, 1), (6, 5), (12, 8)})
solutions.append({(9, 7), (3, 2), (-10, 2), (-5, 1), (7, 1), (7, -5), (3, 1), (-9, -6), (4, 2), (9, 6), (6, 5), (8, 4)})
solutions.append({(7, 3), (-12, -7), (6, -3), (11, 5), (12, 7), (9, 3), (7, 7), (-12, 7), (-3, 2), (10, 1), (4, 2), (9, 7)})
solutions.append({(7, 3), (10, 8), (-5, 1), (11, 4), (9, 1), (10, 6), (-11, -2), (12, 11), (6, -6), (12, 10), (-11, 7), (10, 9)})
solutions.append({(9, 7), (-9, -1), (12, 7), (-10, 4), (-3, 1), (11, 1), (12, 8), (8, -4), (12, 10), (10, 3), (1, 1), (5, 3)})
solutions.append({(11, 7), (3, 2), (10, 8), (11, 4), (9, 2), (-11, 1), (11, 2), (-7, 6), (-11, -1), (10, -8), (10, 1), (12, 11)})
solutions.append({(10, 8), (8, 3), (10, 5), (8, 1), (10, 6), (12, 6), (-11, 8), (-10, 5), (11, -5), (10, 3), (-11, -8), (12, 8)})
solutions.append({(12, 2), (8, 3), (-4, 4), (10, 4), (8, 1), (-10, -5), (10, 6), (9, 3), (7, 5), (-12, 8), (7, -4), (5, 2)})
solutions.append({(-9, 4), (11, 4), (12, 1), (8, 2), (7, 1), (-10, -8), (3, 1), (9, -4), (12, 4), (9, 4), (-12, 4), (4, 1)})
solutions.append({(10, 8), (12, 1), (11, 4), (5, 5), (-9, -4), (3, 1), (9, -4), (-6, 2), (6, 2), (9, 4), (-12, 4), (12, 3)})
solutions.append({(9, 7), (-12, 12), (-9, 5), (6, 1), (10, 6), (-10, -6), (9, -9), (8, 7), (9, 4), (8, 5), (10, 9), (5, 3)})
solutions.append({(-9, 4), (10, 10), (6, 1), (10, 6), (-11, -3), (10, -6), (8, 7), (-11, 11), (9, 5), (8, 5), (10, 9), (5, 3)})
solutions.append({(6, 4), (9, 7), (5, 5), (3, 1), (3, -2), (-7, -5), (-3, 2), (-12, 6), (5, 1), (9, 6), (6, 5), (10, 2)})
solutions.append({(8, -7), (3, 2), (5, 1), (-9, -1), (10, 7), (9, 2), (-7, 5), (11, 3), (-11, 4), (6, 2), (12, 10), (11, 6)})
solutions.append({(11, 4), (8, 2), (-12, -10), (11, 8), (8, 1), (9, 8), (9, 9), (-12, 10), (-7, 2), (12, -10), (11, 6), (8, 4)})
solutions.append({(10, 8), (12, 1), (9, 1), (7, 6), (9, 3), (11, 9), (2, 1), (-12, 11), (9, -4), (12, 11), (-6, 6), (-10, -1)})
solutions.append({(7, 3), (11, 10), (11, 5), (10, 7), (-8, -5), (-8, 5), (11, 3), (8, -5), (7, 5), (9, 5), (-9, 6), (6, 5)})
solutions.append({(12, 2), (9, 2), (10, 7), (-9, -4), (11, 9), (10, 6), (-12, 11), (9, -3), (8, 8), (11, 1), (-7, 2), (7, 2)})

solutions2 = []
for sol in solutions:
    solutions2.append(list(map(lambda p:(p[0], -p[1]) , sol)))
solutions += solutions2

solutions2 = []
for sol in solutions:
    solutions2.append(list(map(lambda p:(-p[0], p[1]) , sol)))
solutions += solutions2

solutions2 = []
for sol in solutions:
    solutions2.append(list(map(lambda p:(p[1], p[0]) , sol)))
solutions += solutions2

X,Y = map(int, sys.stdin.readline().split())

for sol in solutions:
    if (X, Y) in sol:
        for p in sol:
            if p != (X, Y):
                print(p[0], p[1])
        break


# if __name__ == '__main__':
#     first_multiple_input = input().rstrip().split()

#     x = int(first_multiple_input[0])

#     y = int(first_multiple_input[1])

#     # Write your code here
