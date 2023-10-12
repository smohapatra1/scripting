#   https://leetcode.com/problems/valid-parenthesis-string/

# 678. Valid Parenthesis String
# Medium
# 4.9K
# 123
# Companies
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true

def valid_string(s: str) -> bool:
    leftmin =0 
    leftmax=0
    for chars in s:
        if chars=="(":
            leftmax +=1
            leftmin +=1
        if chars == ")":
            leftmax -=1
            leftmin=max(0, leftmin -1)
        if chars == "*":
            leftmax+=1
            leftmin= max(0, leftmin-1)
        if leftmax < 0:
            return False
    if leftmin == 0:
        return True



if __name__ == "__main__":
    #s = "()"
    s = "(*))"
    print ("{}".format(valid_string(s)))