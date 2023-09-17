#   https://leetcode.com/problems/kth-largest-element-in-an-array/
# 215. Kth Largest Element in an Array
# Medium
# 16K
# 765
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


from heapq import heappush, heappushpop, heapify,  heappop
from typing import List

class Solutions:
    def Kthlargest(self, nums: List[int], k:int) -> int:
        #Solution-01
        #return sorted(nums, reverse=True)[k-1]
        #Solution-02
        heap=nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num )
        return heap[0]


if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print ("{}".format.Kthlargest(self, nums, k))


