# #   https://leetcode.com/problems/sum-of-two-integers/

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

# Example 1:

# Input: a = 1, b = 2
# Output: 3
# Example 2:

# Input: a = 2, b = 3
# Output: 5

def getSum(a: int, b: int ) -> int:
    mask = 0xffffffff
    while ( b & mask ) > 0:
        carry=(a & b ) << 1
        a=(a^b)
        b=carry
    return (a & mask ) if b > 0 else a
    
 
if __name__ == "__main__":
    a=1
    b=2
    print ("{}".format(getSum(a,b)))