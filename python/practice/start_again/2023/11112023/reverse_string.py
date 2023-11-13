# #   https://leetcode.com/problems/reverse-string/

# 344. Reverse String
# Easy
# 8K
# 1.1K
# Companies
# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

 

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
 

def reverseString(s: str) -> str:
    #return s[::-1]
    s[:] = s[::-1]

if __name__ == "__main__":
    s = ["h","e","l","l","o"]
    print ("The reverse of {} is {}".format(s,reverseString(s)))