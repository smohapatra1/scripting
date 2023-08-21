# 239. Sliding Window Maximum

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

from collections import deque

def sliding_window_max(nums, k ):

    # Solution -01 - Using deque 
    l=len(nums)
    q = deque()
    result=[]
    for i in range(l):
        if i-k >=0:
            result.append(nums[q[0]])
            # Remove all the elements from the end that are <= new elements 
            while q and q[0] <=i-k:
                q.popleft()
        #Add the new element to the end of deque         
        while q and nums[i] > nums[q[-1]]:
            q.pop()
        q.append(i)
    result.append(nums[q[0]])
    return result

    #Using BFM 
    # l = len(nums)
    # max=0
    # for i in range (l-k +1):
    #     max=nums[i]
    #     for j in range(1, k):
    #         if nums[i+j] > max:
    #             max = nums[i+j]
    # #return max
    # print (str(max) + " ", end="" )

if __name__ == "__main__":
    nums=[1,4,3,-1,2,-4]
    #nums=[4,-2]
    #nums = [1,3,-1,-3,5,3,6,7]
    k=2 # number of consecutive elements 
    #sliding_window_max(nums, k )
    print ("The numbers are {}".format(sliding_window_max(nums, k )))