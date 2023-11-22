# #   https://leetcode.com/problems/sqrtx/
# 69. Sqrt(x)
# Easy
# 7.6K
# 4.4K
# Companies
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 
def mySqrt( x: int )-> int:
    # Solution - 01 
    # return (x ** 0.5)
    # Solution - 02 
    if x == 0:
        return 0
    first = 1 
    last = x
    while first <=last:
        mid = first + (last - first )//2
        if mid == x // mid:
            return mid
        elif mid > x//mid:
            last = mid - 1
        else:
            first = mid + 1
    return last

if __name__ == "__main__":
    x = 15
    print ("Square Root of {} is {}".format(x, mySqrt(x)))