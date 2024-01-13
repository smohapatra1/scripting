# #   https://leetcode.com/problems/palindrome-number/description/

# 9. Palindrome Number
# Solved
# Easy

# Topics
# Companies

# Hint
# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def Palindrome(x: int ) -> bool:
    if x < 0 or (x !=0 and x % 10 == 0):
        return False
    new_num=0
    orig_num=0
    while x > new_num:
        new_num = new_num * 10 + x % 10
        x//=10
    return x==new_num or x ==new_num//10 

if __name__ == "__main__":
    x=121
    print ("{}".format(Palindrome(x)))