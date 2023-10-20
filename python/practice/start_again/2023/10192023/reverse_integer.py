# #   https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Medium
# 12K
# 13K
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1


def reverse_integer(x: int )-> int:
    retval=int(str(abs(x))[::-1])
    if retval.bit_length () > 31:
        return 0 
    return -1 * retval  if x < 0 else retval



if __name__ == "__main__":
    x=123
    print ("{}".format(reverse_integer(x)))