# 22. Generate Parentheses

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

#   Solution :- 
#   Idea is to add ')' only after valid '('
#   Use two variables left and right to see how many '(' & ')' are in the current string
#   If left < n, then add '(' to the current string 
#   If right < left, then add ')' to the current string 
 

def getparent(n):
    result=[]
    left = 0 
    right = 0
    q= [ (left, right, '')]
    while q:
        left, right, s = q.pop()
        if  len(s) == 2 * n:
            result.append(s)
        if left < n:
            q.append((left +1, right, s + '(' ))
        if right < left:
            q.append((left, right+1 , s + ')'))
    return result 
if __name__ == "__main__":
    n=4
    print ("The number of parentheses needed are {} and here they are :-  {}".format(n,getparent(n)))