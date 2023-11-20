# #   https://leetcode.com/problems/valid-perfect-square/

# 367. Valid Perfect Square
# Easy
# 4K
# 294
# Companies
# Given a positive integer num, return true if num is a perfect square or false otherwise.

# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

# You must not use any built-in library function, such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
# Example 2:

# Input: num = 14
# Output: false
# Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.
 
def validSquare(num: int )-> bool:
    # Solution - 01

    # i = 1
    # while (num > 0):
    #     num -=i
    #     i +=2
    # return num == 0 
    
    # Solution - 02 

    left = 1
    right = num 
    while left <= right:
        mid = (left + right )//2
        if mid * mid == num:
            return True
        if mid * mid < num:
            left = mid +1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    #num = 16 
    num = 14
    print ("{} is a perfect Square : {}".format(num, validSquare(num)))