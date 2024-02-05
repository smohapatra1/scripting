# #   https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=false
# rsz_1438840048-2cf71ed69d-findangle.png  is a right triangle,  at .
# Therefore, .

# Point  is the midpoint of hypotenuse .

# You are given the lengths  and .
# Your task is to find  (angle , as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side .
# The second line contains the length of side .

# Constraints


# Lengths  and  are natural numbers.
# Output Format

# Output  in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


# Sample Input

# 10
# 10
# Sample Output

# 45°

from math import atan
from math import degrees

if __name__ == "__main__":
    ab=int(input().strip())
    bc=int(input().strip())
    print("{}°".format(int(round(degrees(atan(ab/bc))))))