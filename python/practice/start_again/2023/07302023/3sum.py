# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

#   Solution
#   1. Get the numbers 
#   2. 
def three_sum(arr):
    arr.sort()
    triplets=set()
    l = len(arr)
    for i in range(l-2):
        firstNum=arr[i]
        j= i+1
        k=l-1 
        while j < k:
            secondNum= arr[j]
            thirdNum=arr[k]
            potentialSum=firstNum + secondNum + thirdNum
            if potentialSum > 0:
                k-=1
            elif potentialSum < 0 :
                j+=1
            else:
                triplets.add((firstNum , secondNum , thirdNum))
                j+=1
                k-=1
    return triplets

if __name__ == "__main__":
    arr=[-1,0,1,2,-1,-4,5,3,2,1,3,1,2]
    print ("The three sum values are {}".format(three_sum(arr)))