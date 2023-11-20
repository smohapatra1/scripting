# #   https://leetcode.com/problems/arranging-coins/
# 441. Arranging Coins
# Easy
# 3.7K
# 1.3K
# Companies
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 
def arrange_Coins(n: int )-> int:
    # Solution-01
    #return int((-1 + (1 + 8*n) ** 0.5)//2)

    #Solution-02
    # i = 0 
    # while n >=0:
    #     i +=1
    #     n=n-i
    # return i-1

    # Solution-03
    # if n == 1:
    #     return n
    # for i in range(1, n+1):
    #     n = n-i
    #     if n < 0:
    #         return i-1
    
    # Solution-04:
    left = 1
    right = n
    while left <= right:
        mid = (left + right )//2
        num = (mid /2) * (mid +1)
        if num <= n:
            left = mid +1
        else:
            right = mid -1
    return right 





if __name__ == "__main__":
    n=5
    print ("{}".format(arrange_Coins(n)))
