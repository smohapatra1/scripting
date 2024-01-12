# #   https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/



# Hint
# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

# Example 1:

# Input: low = 3, high = 7
# Output: 3
# Explanation: The odd numbers between 3 and 7 are [3,5,7].
# Example 2:

# Input: low = 8, high = 10
# Output: 1
# Explanation: The odd numbers between 8 and 10 are [9].

def CountOddNumbers( low: int, high : int ) -> int:
    # Solution - 01
    # if low % 2 == 0:
    #     return (high - low +1 )//2
    # return (high - low)//2+1 
    # Solution - 02 
    odd = (high - low )//2
    if low % 2 == 1 or high % 2 == 1:
        odd +=1
    return odd
        
        

if __name__ == "__main__":
    low = 3
    high = 7
    print ("{}".format(CountOddNumbers(low, high )))