# 20. Valid Parentheses
# Easy

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

def isValid(s):
    while len(s) > 0:
        l=len(s)
        s=s.replace( '()','').replace('{}','').replace('[]','')
        if l==len(s):
            return False
    return True

if __name__ == "__main__":
    #s = "()[]{}"
    s = "(]"
    print ("{} has valid parentheses :- {}".format(s, isValid(s)))