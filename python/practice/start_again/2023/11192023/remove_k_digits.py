# #   https://leetcode.com/problems/remove-k-digits/

# 402. Remove K Digits
# Medium
# 8.3K
# 363
# Companies
# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

def remove_k_digit(nums: str, k: int) -> str:
    if len(nums) and k == 2:
        return 0
    stack=[]
    for i in nums:
        while (stack and int(stack[-1]) > int(i) and k):    
            stack.pop()
            k-=1
        stack.append(str(i))
    while (k):
        stack.pop()
        k -=1
    i =0
    while (i < len(stack) and stack[i] == "0" ):
        i+=1
    return ''.join(stack[i:]) if (len(stack[i:]) > 0) else "0"  
              
    

if __name__ == "__main__":
    nums = "1432219"
    k = 3
    #nums = "10"
    #k = 2
    print ("{}".format(remove_k_digit(nums, k )))
